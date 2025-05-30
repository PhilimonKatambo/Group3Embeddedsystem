import serial
from Registry import showID

class Arduino:
    def __init__(self):
        self.arduino = serial.Serial('COM6',9600)


    def sendToDB(self):
        while True:
            if self.arduino.in_waiting > 0:
                data = self.arduino.readline().decode('utf-8').strip()
                print(str(data).replace(" ",""))
                showID(str(data).replace(" ",""))

arduino = Arduino()
arduino.sendToDB()