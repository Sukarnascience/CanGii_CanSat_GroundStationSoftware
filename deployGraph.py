import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import socket
from collections import deque
import random
import threading

max_len = 20

class DataPlotter:
    def __init__(self, broadcast_host, broadcast_port):
        self.broadcast_host = broadcast_host
        self.broadcast_port = broadcast_port
        self.temp_data = deque(maxlen=max_len)
        self.humidity_data = deque(maxlen=max_len)
        self.pressure_data = deque(maxlen=max_len)
        self.altitude_data = deque(maxlen=max_len)

        # Set up UDP socket for receiving broadcasted data
        self.receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receive_socket.bind((self.broadcast_host, self.broadcast_port))

    def receive_data(self):
        while True:
            data, _ = self.receive_socket.recvfrom(1024)
            data = data.decode('utf-8').split(',')
            if len(data) == 4:
                temp, humidity, pressure, altitude = map(float, data)
                self.temp_data.append(temp)
                self.humidity_data.append(humidity)
                self.pressure_data.append(pressure)
                self.altitude_data.append(altitude)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sensor Data Plotter")

        self.data_plotter = DataPlotter(broadcast_host='localhost', broadcast_port=12345)

        self.create_widgets()

        # Start a separate thread to continuously receive data
        self.receive_thread = threading.Thread(target=self.data_plotter.receive_data)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.plot_data()

    def create_widgets(self):
        self.fig = Figure(figsize=(12, 8), dpi=100)
        self.temp_plot_area = self.fig.add_subplot(221)
        self.humidity_plot_area = self.fig.add_subplot(222)
        self.pressure_plot_area = self.fig.add_subplot(223)
        self.altitude_plot_area = self.fig.add_subplot(224)

        self.temp_plot_area.set_xlabel('Time')
        self.temp_plot_area.set_ylabel('Temperature')

        self.humidity_plot_area.set_xlabel('Time')
        self.humidity_plot_area.set_ylabel('Humidity')

        self.pressure_plot_area.set_xlabel('Time')
        self.pressure_plot_area.set_ylabel('Pressure')

        self.altitude_plot_area.set_xlabel('Time')
        self.altitude_plot_area.set_ylabel('Altitude')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def plot_data(self):
        self.temp_plot_area.clear()
        self.humidity_plot_area.clear()
        self.pressure_plot_area.clear()
        self.altitude_plot_area.clear()

        if self.data_plotter.temp_data:
            temp_avg = sum(self.data_plotter.temp_data) / len(self.data_plotter.temp_data)
            self.temp_plot_area.plot(range(len(self.data_plotter.temp_data)), [temp_avg] * len(self.data_plotter.temp_data), 'r--', label='Average')
            self.temp_plot_area.plot(self.data_plotter.temp_data, 'b-', label='Temperature')
            self.temp_plot_area.legend()

        if self.data_plotter.humidity_data:
            humidity_avg = sum(self.data_plotter.humidity_data) / len(self.data_plotter.humidity_data)
            self.humidity_plot_area.plot(range(len(self.data_plotter.humidity_data)), [humidity_avg] * len(self.data_plotter.humidity_data), 'r--', label='Average')
            self.humidity_plot_area.plot(self.data_plotter.humidity_data, 'g-', label='Humidity')
            self.humidity_plot_area.legend()

        if self.data_plotter.pressure_data:
            pressure_avg = sum(self.data_plotter.pressure_data) / len(self.data_plotter.pressure_data)
            self.pressure_plot_area.plot(range(len(self.data_plotter.pressure_data)), [pressure_avg] * len(self.data_plotter.pressure_data), 'r--', label='Average')
            self.pressure_plot_area.plot(self.data_plotter.pressure_data, 'm-', label='Pressure')
            self.pressure_plot_area.legend()

        if self.data_plotter.altitude_data:
            altitude_avg = sum(self.data_plotter.altitude_data) / len(self.data_plotter.altitude_data)
            self.altitude_plot_area.plot(range(len(self.data_plotter.altitude_data)), [altitude_avg] * len(self.data_plotter.altitude_data), 'r--', label='Average')
            self.altitude_plot_area.plot(self.data_plotter.altitude_data, 'y-', label='Altitude')
            self.altitude_plot_area.legend()

        self.canvas.draw()

        self.root.after(1000, self.plot_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
