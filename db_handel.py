import pandas as pd
import csv

class database():
    def __init__(self):
        super().__init__()
        self.collectData = []

        self.graphChartLen = 8
        self.graphTemp = [0,0,0,0,0,0,0,0]
        self.graphHumi = [0,0,0,0,0,0,0,0]
        self.graphAlti = [0,0,0,0,0,0,0,0]      

        self.graphTempP = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        self.graphHumiP = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        self.graphAltiP = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]   

    #BACKUP File
    def createLiveData(self,fname,data):
        #vanish = self.getData()
        try:
            with open(('live_{}.csv'.format(fname)), 'a', newline='') as self.file:
                writer = csv.writer(self.file)
                writer.writerow(data)
                self.collectData.append(data)
                self.closeFile()
            print("Backup Successfully")
        except:
            print("Backup Failed")

    def getGraphData(self):
        self.graphData = self.collectData[len(self.collectData)-self.graphChartLen:len(self.collectData)]
        countT = 0
        for i in self.graphData:
            self.graphTempP[1][countT] = i[15]
            self.graphTempP[0][countT] = i[2]
            countT+=1
        #print(self.graphTempP)
        countA = 0
        for i in self.graphData:
            self.graphAltiP[1][countA] = i[12]
            self.graphAltiP[0][countA] = i[2]
            countA+=1
        #print(self.graphAltiP)
        countH = 0
        for i in self.graphData:
            self.graphHumiP[1][countH] = i[14]
            self.graphHumiP[0][countH] = i[2]
            countH+=1
        #print(self.graphHumiP)
        return [self.graphTempP,self.graphHumiP,self.graphAltiP]


    def dumpData(self,data):
        self.collectData.append(data)
    def getData(self):
        try:
            print(self.collectData[-5:0:-1])
            return self.collectData[-5:0:-1]
        except:
            print("incomplete data")
            return None

    def downloadData(self,fname):
        try:
            print("Datas which are collected are: {}".format(self.collectData))
            fileN = ('download_{}.csv'.format(fname))
            print("File Name: {}".format(fileN))
            with open(fileN, 'w', newline='') as self.fileD:
                writer = csv.writer(self.fileD)
                writer.writerows(self.collectData)
                self.fileD.close()
        except:
            print("Failed to download")

    def closeFile(self):
        try:
            self.file.close()
        except:
            print("Failed to close the file")
