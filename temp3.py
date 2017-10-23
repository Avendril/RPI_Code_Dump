import time

while 1:
	tempfile = open("/sys/bus/w1/devices/28-03168a72f7ff/w1_slave")
	tempfile2 = open("/sys/bus/w1/devices/28-03168a5521ff/w1_slave")
	thetext = tempfile.read()
	thetext2 = tempfile2.read()
	tempfile.close()
	tempfile2.close()
	tempdata = thetext.split("\n")[1].split(" ")[9]
	tempdata2 = thetext2.split("\n")[1].split(" ")[9]
	temperature = float(tempdata[2:])
	temperature2 = float(tempdata2[2:])
	temperature = temperature / 1000
	temperature2 = temperature2 / 1000
	print'temperature1: ', temperature
	print'temperature2: ', temperature2

	time.sleep(1)
