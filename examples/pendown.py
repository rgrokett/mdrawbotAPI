#!/user/bin/env python
#
# test of pen down
#
# Edit the Serial Port as needed
# Edit the Pen Down/Up values as needed


import serial, time
# SET YOUR VALUES FOR PEN UP/DOWN
PENUP = "160"
PENDN = "130"
# CHANGE TO YOUR USB SERIAL PORT
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=20)

time.sleep(2)  # just give some time for port open if Windows

ser.write('M10' + '\n')
print ("EPROM:"+ser.readline())
print (ser.readline())
ser.write('M1 '+PENDN+ '\n')
print ("Pen Down:"+ser.readline())
time.sleep(5)
ser.close()

