import serial

ser = serial.Serial('COM6', 9600)

def turn_on_led():
    ser.write(b'1')

def turn_off_led():
    ser.write(b'0')

while True:
    h=str(input("Enter 1:for LED on\nEnter 0:for LED off\n:"))
    if h=='1':
        turn_on_led()
    elif h=='0':
        turn_off_led()
    else:
        print("Invalid input")
        ser.close()
        break


