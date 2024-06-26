If you liked it, please show your support by donating. 👇
<p><a href="https://www.buymeacoffee.com/sukarnajana"> <img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="sukarnajana" /></a></p>
<br>
<br>
<br>
<br>

![Logo](./logo.png)
# CanGii V8.14.20 

> **Whats New in V8.14.20 ?** : Adding PC TimeStamp in the place of ```self.dataCame[2]``` into ```current_timestamp = get_current_timestamp()```

CanGii is a Python-based satellite data visualization tool for real-time monitoring and analysis of telemetry data. It offers a user-friendly interface and supports various satellite communication protocols.

![GUI](./CanGiiGUI.png)

## Setup

To set up CanGii on your system, follow these steps:

1. **Install Python:** Ensure that Python 3 is installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

2. **Create a Virtual Environment (Optional):** It's recommended to create a virtual environment to isolate dependencies. Run the following command to create a virtual environment named `env`:
   ```
   python -m venv env
   ```

3. **Activate the Virtual Environment (Optional):** If you've created a virtual environment, you need to activate it before installing dependencies. On Windows, run the following command to activate the virtual environment:
   ```
   .\env\Scripts\activate
   ```
   On macOS/Linux, run:
   ```
   source env/bin/activate
   ```

4. **Install Dependencies:** Run the `setup.bat` file to install all required dependencies. This script will automatically install the necessary packages using pip.
   ```
   setup.bat
   ```

## Usage

After setting up the environment, you can start CanGii by running the `startApp.bat` file. This script will deploy the software and launch the application.

To start CanGii, simply double-click on `startApp.bat`.

## Description

CanGii is a Python-based satellite data visualization tool designed for real-time monitoring and analysis of telemetry data. It provides a user-friendly interface for visualizing temperature, humidity, pressure, and altitude data from satellites. CanGii supports various satellite communication protocols and offers features for data logging and historical trend analysis.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
