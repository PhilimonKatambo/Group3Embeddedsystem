from PySide6.QtWidgets import (QApplication)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys
from Database import DataBase as db
import threading

class Entry():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.file = QFile("C:/Users/DELL/Desktop/OpenSourceInterface/Login.ui")
        self.loader = QUiLoader()
        self.window2 = self.loader.load(self.file)
        self.cardID2=""

        self.thread3 = threading.Thread(target=self.window2.show())


        thread4 = threading.Thread(target=self.GetID)
        thread4.start()

        self.app.exec()

    def css(self):
        with open("Registry.css", 'r') as f:
            cont = f.read()
            return cont


    def GetID2(self):
        while True:
            if self.arduino.in_waiting > 0:
                data = self.arduino.readline().decode('utf-8').strip()
                self.cardID2=str(data).replace(" ", "")
                print(self.cardID2)
                if(len(self.cardID2) > 0 and len(self.cardID2) <= 9):
                    self.showID()


    def showID2(self,):
        self.window2.cardText2.setText("Card ID: " + self.cardID2[:-1] + "   Room Number selected: "+self.cardID2[8])
        self.Entrance1()


    def Entrance12(self):
        if(self.cardID2!=""):
            check=db().Entrance(self.cardID2[:-1],self.cardID2[8])
            if(check):
                self.window2.cardText1.setText("Successful operation")
                msg="1\n"
                self.arduino.write(msg.encode())
            else:
                self.window2.cardText1.setText("Unsuccessful operation")
                msg = "2\n"
                self.arduino.write(msg.encode())
        else:
            print("Enter in all fields")

    # def showWindow(self):
    #     thread3 = threading.Thread(target=self.window2.show())
    #     thread3.start()