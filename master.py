import serial
import time
import os

import temp3 as temperature
import gyroscope as gyro
import humidity as humi
import testDB as database

hostname = "87.44.19.170"#Ubuntu VM: 87.44.19.170  Local Machine(bchmielewski laptop):10.37.28.64
temperatureQueue1 = "SmartHive/Temperature/Temp1"
temperatureQueue2 = "SmartHive/Temperature/Temp2"
humidityQueue = "SmartHive/Humidity"
gyroscopeQueueX = "SmartHive/Gyroscope/Axis-X"
gyroscopeQueueY = "SmartHive/Gyroscope/Axis-Y"
gyroscopeQueueZ = "SmartHive/Gyroscope/Axis-Z"

try:
	print("Starting mqtt publishing")

	while True:
		os.system("mosquitto_pub -h " + hostname + " -t " + temperatureQueue1 + " -m " + temperature.Read_Temp1())
		database.upload_to_db('temperature', temperature.Read_Temp1())

		os.system("mosquitto_pub -h " + hostname + " -t " + temperatureQueue2 + " -m " + temperature.Read_Temp2() )
		database.upload_to_db('temperature2', temperature.Read_Temp2())

		os.system("mosquitto_pub -h " + hostname + " -t " + humidityQueue + " -m " + humi.Read_Humidity())
		database.upload_to_db('humidity', humi.Read_Humidity())

		os.system("mosquitto_pub -h " + hostname + " -t " + gyroscopeQueueX + " -m " + gyro.Gyroscope_Read_X())
		database.upload_to_db('gyro_axis_x', gyro.Gyroscope_Read_X())
		os.system("mosquitto_pub -h " + hostname + " -t " + gyroscopeQueueY + " -m " + gyro.Gyroscope_Read_Y())
		database.upload_to_db('gyro_axis_y', gyro.Gyroscope_Read_Y())
		os.system("mosquitto_pub -h " + hostname + " -t " + gyroscopeQueueZ + " -m " + gyro.Gyroscope_Read_Z())
		database.upload_to_db('gyro_axis_z', gyro.Gyroscope_Read_Z())
		time.sleep(0.1)

except KeyboardInterrupt:
	print("Loop was stopped manually")
