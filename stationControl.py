import serial

class satC_Device():
    def __init__(self):
        super().__init__()

        # Set some defalule parameters 
        self.port = "COM4"
        self.boudRate = 9600
        self.timeOut = 0.1
        self.statusD = False
        self.fdata = []

    def connectToDevice(self,portN="",boudRateN=0,timeOutN=0.1):
        self.port = portN
        self.boudRate = boudRateN
        self.timeOut = timeOutN

        try:
            self.device = serial.Serial(port=self.port, baudrate=self.boudRate, timeout=self.timeOut)
            self.statusD = True
            print("Connecting Establish Successfully")
            #return True
        except:
            self.statusD = False 
            print("Connecting Establish Falied")
            #return False  
    
    def isConnect(self):
        if(self.statusD):
            return True
        else:
            return False

    def giveData(self):

        try:
            if(self.isConnect()):
                ser_bytes = self.device.readline()
                data = (ser_bytes[0:len(ser_bytes)-2]).decode("utf-8")
                print(data)
                self.fdata = []

                self.fdata = data.split(",")
                if(self.fdata == ['']):
                    return None
                else:
                    return self.fdata
            else:
                return None
        except:
            print("Board ERROR")