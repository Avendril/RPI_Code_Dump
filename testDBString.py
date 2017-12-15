from influxdb import InfluxDBClient
import random

def upload_to_db(place, sensorRead):
#       while 1:
        readings = str(sensorRead)
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

