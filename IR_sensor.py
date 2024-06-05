import RPi.GPIO as g
import time

trgPin = 4
echPin = 17
RledP = 21

g.setmode(g.BCM)
g.setup(trgPin, g.OUT)
g.setup(echPin, g.IN)
g.setup(RledP, g.OUT)

while(True):
    g.output(trgPin, False)
    time.sleep(1)

    g.output(trgPin, True)
    time.sleep(0.0001)
    g.output(trgPin, False)
 
    while(g.input(echPin) == False):
        startTime = time.time()
    while(g.input(echPin) == True):
        endTime = time.time()
    ditTim = endTime - startTime
    distance = (ditTim * 34400) / 2
    if (distance < 10):
        g.output(RledP, True)
    else:
        g.output(RledP, False)
    
    print("distance :", distance, " cm")


