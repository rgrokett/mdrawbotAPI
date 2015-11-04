#!/user/bin/env python
#
# test to verify USB port connection
#
# Edit the Serial Port as needed
# Edit the Pen Down/Up values as needed


import serial, time
# CHANGE TO YOUR USB SERIAL PORT
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=20)

time.sleep(2)  # just give some time for port open if Windows

ser.write('M10' + '\n')
print ("EPROM:"+ser.readline())
print (ser.readline())
print ("FINISHED")
ser.close()

