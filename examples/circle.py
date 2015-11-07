#!/user/bin/env python
#
# test to draw a circle
#
# Edit the Serial Port as needed
# Edit the Pen Down/Up values as needed


import serial, time, math
# SET YOUR VALUES FOR PEN UP/DOWN
PENUP = "160"
PENDN = "125"

DEBUG = 0

# CHANGE SERIAL PORT AS NEEDED
if not DEBUG:
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=20)
else:
    # Write to a file instead of serial for debugging
    ser = open("output.txt", "w")

time.sleep(2)  # just give some time for port open if Windows

settle = 0.3

# CIRCLE
pi2  = 2*math.pi
step = pi2/20	# Note must be an exact division of 2*PI radians to avoid gaps
XPOS = -250.00
YPOS = 150.00
RAD  = 40

# STARTUP
ser.write('M10' + '\n')
if not DEBUG:
    print ("EPROM:"+ser.readline())
    print (ser.readline())
ser.write('M1 '+PENUP+ '\n')
if not DEBUG:
    print ("Pen Up:"+ser.readline())
time.sleep(settle)  

# LETS DRAW
theta = 0.0
first_loop = 1
while (theta <= pi2):
    x = XPOS + RAD*math.cos(theta)
    y = YPOS + RAD*math.sin(theta)
    theta += step
    if first_loop:
	# Move to initial spot
    	ser.write('G1 X'+str(x)+' Y'+str(y)+' A0' + '\n')
	if not DEBUG:
    	    print ("Move:"+ser.readline())
	ser.write('M1 '+PENDN+ '\n')
	if not DEBUG:
    	    print ("Pen Down:"+ser.readline())
	time.sleep(settle)  
	first_loop = 0
    else:
    	ser.write('G1 X'+str(x)+' Y'+str(y)+' A0' + '\n')
    	if not DEBUG:
            print ("Draw:"+ser.readline())

# FINISH
ser.write('M1 '+PENUP+ '\n')
if not DEBUG:
    print ("Pen Up:"+ser.readline())
time.sleep(settle)  # just give some time for port open if Windows
ser.write('G28' + '\n')
if not DEBUG:
    print ("Home:"+ser.readline())
ser.write('P1' + '\n')
if not DEBUG:
    print ("Current Pos:"+ser.readline())
time.sleep(1)
print ("FINISHED")
ser.close()

