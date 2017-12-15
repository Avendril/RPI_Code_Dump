import Adafruit_DHT
import time

#Humidity, Temp = Adafruit_DHT.read_retry(22, 17)
#print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(Temp, Humidity)

def Read_Humidity():
	while True:
		Humidity, Temp = Adafruit_DHT.read_retry(22, 17)		
		humi = str(Humidity)
		return humi
