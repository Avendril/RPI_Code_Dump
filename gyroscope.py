from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)

#Accelerometer Readings functions
def Accelerometer_Read_X():
	while True:
		accel_data = sensor.get_accel_data()
		x = str(accel_data['x'])
		
#		time.sleep(1)
		return x	

def Accelerometer_Read_Y():
        while True:
                accel_data = sensor.get_accel_data()
                y = str(accel_data['y'])
                
#		time.sleep(1)
		return y   

def Accelerometer_Read_Z():
        while True:
                accel_data = sensor.get_accel_data()
                z = str(accel_data['z'])

#		time.sleep(1)
                return z   


#Gyroscope Readings functions
def Gyroscope_Read_X():
	while True:
		gyro_data = sensor.get_gyro_data()
        	a = str(gyro_data['x'])
        	
#		time.sleep(1)
		return a

def Gyroscope_Read_Y():
        while True:
                gyro_data = sensor.get_gyro_data()
                b = str(gyro_data['y'])

 #               time.sleep(1)
                return b


def Gyroscope_Read_Z():
        while True:
                gyro_data = sensor.get_gyro_data()
                c = str(gyro_data['z'])

#                time.sleep(1)
                return c


#Temperature Readings functions
def Temperature_Read_MPU():
	while True:
		temp =str(sensor.get_temp())

#		time.sleep(1)
		return temp
