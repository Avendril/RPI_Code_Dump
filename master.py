import serial
import time
import os

import temp3 as temperature
import testDB as database

hostname = "87.44.19.170"#Ubuntu VM: 87.44.19.170  Local Machine(bchmielewski laptop):10.37.28.64
temperatureQueue1 = "SmartHive/Temperature/Temp1"
temperatureQueue2 = "SmartHive/Temperature/Temp2"

try:
	print("Starting mqtt publishing")

	while True:
		os.system("mosquitto_pub -h " + hostname + " -t SmartHive/Hostname -m " + hostname)
	
		os.system("mosquitto_pub -h " + hostname + " -t " + temperatureQueue1 + " -m " + temperature.Read_Temp1())
		database.upload_to_db('temperature', temperature.Read_Temp1())

		os.system("mosquitto_pub -h " + hostname + " -t " + temperatureQueue2 + " -m " + temperature.Read_Temp2() )
		database.upload_to_db('temperature2', temperature.Read_Temp2())

		time.sleep(5)

except Exception as e:
	pass
