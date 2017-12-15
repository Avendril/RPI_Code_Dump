import serial
import time

def Read_Weight():
	time.sleep(2)

	ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate = 115200,
        bytesize = serial.EIGHTBITS,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        xonxoff = False,
        rtscts = False,
        dsrdtr = False,
        timeout = 1
        )

	while 1:
		
		for _ in range(1):
			data = ser.readline()
			return data
#			Serial.flush();
		Serial.flush();
