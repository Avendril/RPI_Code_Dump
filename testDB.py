from influxdb import InfluxDBClient
import random

def upload_to_db(place, sensorRead):
	readings = float(sensorRead)
	json_body = [
    	        {
       		    "measurement": place,
       		    "tags": {
       		        "location": "Bio-diversity lab"
       		    },
       		    "fields": {
            		 "value": readings
           	    }
   	         }
   	    ]

	client = InfluxDBClient('87.44.19.156', 8086, 'bart', 'sm4rth1v3', 'SmartHiveTestDB')
	client.write_points(json_body)

def upload_to_db_String(place, sensorRead):
	if sensorRead is None:
		print('No data')
	else:
		
	        readings = sensorRead
	        json_body = [
	                {
	                    "measurement": place,
	                    "tags": {
	                        "location": "Bio-diversity lab"
	                    },
	                    "fields": {
	                         "value": readings
	                    }
	                 }
	            ]
	
	        client = InfluxDBClient('87.44.19.156', 8086, 'bart', 'sm4rth1v3', 'SmartHiveTestDB')
	        client.write_points(json_body)


#result = client.query('select * from temperature;')
#
#print("Result: {0}".format(result))
