from mpu6050 import mpu6050
from time import sleep
import paho.mqtt.publish as publish

sensor = mpu6050(0x68)
print " waiting for the sensor to callibrate..."
sleep(2)
while True:
	accel_data = sensor.get_accel_data()
	gyro_data = sensor.get_gyro_data()
	temp = sensor.get_temp()
	print("Accelerometer Data")
	print("x: " +str(accel_data['x']))
	print("y: " +str(accel_data['y']))
	print("z: " +str(accel_data['z']))

	publish_data("Accelerometer","x: " +str(accel_data['x']))
	publish_data("Accelerometer","y: " +str(accel_data['y']))
	publish_data("Accelerometer","z: " +str(accel_data['z']))
	
	print("Gyroscope data")
	print("x: " + str(gyro_data['x']))
	print("y: " + str(gyro_data['y']))
	print("z: " + str(gyro_data['z']))
	print("Temp: " + str(temp) + " C")
	sleep(2)

	publish_data("Gyroscope","x: " +str(gyro_data['x']))
	publish_data("Gyroscope","y: " +str(gyro_data['y']))
	publish_data("Gyroscope","z: " +str(gyro_data['z']))

	publish_data("Temperature","Temp: " +str(temp)+ "C")

def publish_data(queue,message):
	publish.single(str(queue), str(message), hostname="10.37.28.64")
