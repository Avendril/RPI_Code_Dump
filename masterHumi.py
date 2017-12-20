import serial
import time
import os

import humidity as humi
import testDB as database

hostname = "87.44.19.170"#Ubuntu VM: 87.44.19.170  Local Machine(bchmielewski laptop):10.37.28.64
humidityQueue = "SmartHive/Humidity"

print("Started sending data to mqtt publisher")

while True:
	try:
        
	        while True:
	                os.system("mosquitto_pub -h " + hostname + " -t " + humidityQueue + " -m " + humi.Read_Humidity())
	                database.upload_to_db('humidity', humi.Read_Humidity())

	except:
		print("ERROR")
		pass
