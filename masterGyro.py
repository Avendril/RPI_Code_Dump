import serial
import time
import os

import gyroscope as gyro
import testDB as database

print("Starting mqtt publishing")

while True:
	try:

	        while True:
        	        os.system("mosquitto_pub -h 87.44.19.170 -t SmartHive/Gyroscope/Axis-X -m " + gyro.Gyroscope_Read_X())
             		database.upload_to_db('gyro_axis_x', gyro.Gyroscope_Read_X())
             		os.system("mosquitto_pub -h 87.44.19.170 -t SmartHive/Gyroscope/Axis-Y -m " + gyro.Gyroscope_Read_Y())
	                database.upload_to_db('gyro_axis_y', gyro.Gyroscope_Read_Y())
	                os.system("mosquitto_pub -h 87.44.19.170 -t SmartHive/Gyroscope/Axis-Z -m " + gyro.Gyroscope_Read_Z())
	                database.upload_to_db('gyro_axis_z', gyro.Gyroscope_Read_Z())
	                time.sleep(10)

	except Exception:
		print("ERROR,AGAIN")
		pass
#except KeyboardInterrupt:
#        print("Loop was stopped manually")




