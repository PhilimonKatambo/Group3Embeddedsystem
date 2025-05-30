from PySide6.QtWidgets import (QApplication,QMessageBox)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys
from Database import DataBase as db
import threading
import serial
import time

class Registry1():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.arduino = serial.Serial('COM6', 9600)

        msg = "Registry\n"
        self.arduino.write(msg.encode())

        #Registry
        self.file = QFile("C:/Users/DELL/Desktop/OpenSourceInterface/Authentication.ui")
        self.loader = QUiLoader()
        self.window = self.loader.load(self.file)
        self.cardID=""
        self.window.submit.clicked.connect(lambda: self.GetIntoDB2())
        self.window.submit.setStyleSheet(self.css())
        self.window.regLabel.setStyleSheet(self.css())
        self.window.name.setStyleSheet(self.css())
        self.window.roomNumber.setStyleSheet(self.css())
        self.window.cardText.setStyleSheet(self.css())
        self.window.RouteReg1.clicked.connect(lambda: self.route1(1))
        self.thread2 = threading.Thread(target=self.GetID1)

        self.file = QFile("C:/Users/DELL/Desktop/OpenSourceInterface/Login.ui")
        self.loader = QUiLoader()
        self.window2 = self.loader.load(self.file)
        self.cardID = ""
        self.window2.RouteReg.clicked.connect(lambda: self.route1(2))
        self.window2.FaceLog.clicked.connect(lambda: self.faceLog())

        self.route1(1)

        self.app.exec()

    def route1(self,vibe):
        if vibe==1:
            self.window.close()
            self.window2.show()

            msg = "Entry\n"
            self.arduino.write(msg.encode())
        else:
            self.window2.close()
            self.window.show()

            msg = "Registry\n"
            self.arduino.write(msg.encode())

    def faceLog(self):
        from FaceRecLog import Login
        face = Login()
        logData=face.logs()

        print(logData)
        if logData== True:
            print(str(logData)+"1")
            self.changeNumber(1)
        else:
            print(str(logData) + "1")
            self.changeNumber(2)

    def css(self):
        with open("Registry.css", 'r') as f:
            cont = f.read()
            return cont


    def GetID1(self):
        while True:
            if self.arduino.in_waiting > 0:
                data = self.arduino.readline().decode('utf-8').strip()
                self.cardID=str(data).replace(" ", "")
                if len(self.cardID) > 0 and len(self.cardID) <= 8:
                    self.showID1()
                elif len(self.cardID) > 0 and len(self.cardID) <= 9:
                    self.showID2()

    def showID1(self,):
        self.window.cardText.setText("Card ID: " + self.cardID)

    def showID2(self):
        self.window2.cardText2.setText("Card ID: " + self.cardID[:-1] + "   Room Number selected: "+self.cardID[8])
        self.Entrance2()

    def GetIntoDB2(self):
        if (
                self.window.name.text() != "" and self.window.roomNumber.value() > 0 and self.window.roomNumber.value() <= 14):
            if (len(self.cardID) > 0 and len(self.cardID) <= 8):
                data=db().GetIntoDB(self.cardID, self.window.name.text(), self.window.roomNumber.value())
                self.window.cardText.setText(str(data))
            else:
                self.window.cardText.setText("Invalid card ID")
        else:
            self.window.cardText.setText("Fill all the fields")


    def Entrance2(self):
        if(self.cardID!=""):
            check=db().Entrance(self.cardID[:-1],self.cardID[8])
            if(check):
                self.window2.cardText1.setText("Successful operation")
                self.changeNumber(1)
            else:
                self.window2.cardText1.setText("Unsuccessful operation")
                self.changeNumber(2)
        else:
            print("Enter in all fields")
            self.window2.cardText1.setText("Enter in all fields")#

    def changeNumber(self,num):
        if num == 1:
            print(1)
            msg = "1\n"
            self.arduino.write(msg.encode())
        else:
            print(2)
            msg = "2\n"
            self.arduino.write(msg.encode())

    def dialog(self,msg):
        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.setWindowTitle("Confirmation")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()



Registry = Registry1()