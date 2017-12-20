import serial
import time
import os

import testDB as database

ser = serial.Serial('/dev/ttyACM0', 9600)
try:
	while True:
	    data = ser.readline()
	#    print data
	    os.system("mosquitto_pub -h 87.44.19.170 -t SmartHive/Weight -m " + data)
	    database.upload_to_db_String('weight', data)

except Exception as e:
	pass
