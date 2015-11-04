#!/user/bin/env python
#
# test to draw a box
#
# Edit the Serial Port as needed
# Edit the Pen Down/Up values as needed


import serial, time
# SET YOUR VALUES FOR PEN UP/DOWN
PENUP = "160"
PENDN = "130"

# CHANGE SERIAL PORT AS NEEDED
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=20)
time.sleep(2)  # just give some time for port open if Windows

settle = 0.3

ser.write('M10' + '\n')
print ("EPROM:"+ser.readline())
print (ser.readline())
ser.write('M1 '+PENUP+ '\n')
print ("Pen Up:"+ser.readline())
time.sleep(settle)  
# Move to initial spot
ser.write('G1 X-200.00 Y175.00 A0' + '\n')
print ("Move:"+ser.readline())
ser.write('M1 '+PENDN+ '\n')
print ("Pen Down:"+ser.readline())
time.sleep(settle)  

# LETS DRAW
ser.write('G1 X-250.00 Y175.00 A0' + '\n')
print ("Draw:"+ser.readline())
ser.write('G1 X-250.00 Y125.00 A0' + '\n')
print ("Draw:"+ser.readline())
ser.write('G1 X-200.00 Y125.00 A0' + '\n')
print ("Draw:"+ser.readline())
ser.write('G1 X-200.00 Y175.00 A0' + '\n')
print ("Draw:"+ser.readline())

# FINISH
ser.write('M1 '+PENUP+ '\n')
print ("Pen Up:"+ser.readline())
time.sleep(settle)  # just give some time for port open if Windows
ser.write('G28' + '\n')
print ("Home:"+ser.readline())
ser.write('P1' + '\n')
print ("Current Pos:"+ser.readline())
time.sleep(1)
print ("FINISHED")
ser.close()

