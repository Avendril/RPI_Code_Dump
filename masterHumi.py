import serial
import time
import os

import humidity as humi
import testDB as database

hostname = "87.44.19.170"#Ubuntu VM: 87.44.19.170  Local Machine(bchmielewski laptop):10.37.28.64
humidityQueue = "SmartHive/Humidity"

try:
        print("Starting mqtt publishing")

        while True:
                os.system("mosquitto_pub -h " + hostname + " -t " + humidityQueue + " -m " + humi.Read_Humidity())
                database.upload_to_db('humidity', humi.Read_Humidity())

except KeyboardInterrupt:
        print("Loop was stopped manually")
