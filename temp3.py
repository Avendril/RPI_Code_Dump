import time
from influxdb import InfluxDBClient

	
#tempfile = open("/sys/bus/w1/devices/28-03168a5521ff/w1_slave")
#text = tempfile.read()
#tempfile.close()
#tempdata = text.split("\n")[1].split(" ")[9]
#temperature = float(tempdata[2:])
#temperature = temperature / 1000
#BCTemp1 = str(temperature)
#
#json_body = [
#{
#	"measurement": "temperature",
#        "tags": {
#        	"officename": "Infrastructure Group"
#         },
#         "fields": {
# 	        "value": BCTemp1  
#         }
#}
#]
#
#client=InfluxDBClient('87.44.19.156',8086,'sysadmin','syst1m4x','IGGroup')          
#client.write_points(json_body)
#result = client.query('select * from temperature;')
#print("Result: {0}".format(result))
#
def Read_Temp1():
	while 1:
		tempfile = open("/sys/bus/w1/devices/28-03168a5521ff/w1_slave")
		text = tempfile.read()
		tempfile.close()
		
		tempdata = text.split("\n")[1].split(" ")[9]
		temperature = float(tempdata[2:])
		temperature = temperature / 1000
		BCTemp1 = str(temperature)

		json_body = [
	        {
	            "measurement": "temperature",
	            "tags": {
	                "officename": "Infrastructure Group"
	            },
	            "fields": {
	                "value": BCTemp1
	            }
	        }
	    	]
#		time.sleep(1)
		client=InfluxDBClient('87.44.19.156',8086,'sysadmin','syst1m4x','IGGroup')
		client.write_points(json_body)
		result = client.query('select * from temperature;')		
		return BCTemp1

def Read_Temp2():
	while 1:
		tempfile2 = open("/sys/bus/w1/devices/28-03168a7071ff/w1_slave")
		text2 = tempfile2.read()
		tempfile2.close()

		tempdata2 = text2.split("\n")[1].split(" ")[9]
		temperature2 = float(tempdata2[2:])
		temperature2 = temperature2 / 1000
		BCTemp2 = str(temperature2)

#		time.sleep(1)

		return BCTemp2

def Read_Temp_Both():
	while 1:
		tempfile = open("/sys/bus/w1/devices/28-03168a7071ff/w1_slave")
		tempfile2 = open("/sys/bus/w1/devices/28-03168a5521ff/w1_slave")
		
		text = tempfile.read()
		text2 = tempfile2.read()
		tempfile.close()
		tempfile2.close()
	
		tempdata = text.split("\n")[1].split(" ")[9]
		tempdata2 = text2.split("\n")[1].split(" ")[9]

		temperature = float(tempdata[2:])
		temperature2 = float(tempdata2[2:])

		temperature = temperature / 1000
		temperature2 = temperature2 / 1000
		BCTemp1 = str(temperature)
		BCTemp2 = str(temperature2)
	
		time.sleep(1)

		return BCTemp1,BCtemp2
