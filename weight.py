import serial
import time

ser = serial.Serial(port='/dev/ttyACM0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=0)
try:
	ser.isOpen()
	print("Serial port is open")
except:
	print("Serial port is not open")

while true:
	ser.readline()
