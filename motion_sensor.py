import RPi.GPIO as g
import time

pirP = 20
sPin = 21

g.setmode(g.BCM)
g.setup(sPin, g.OUT)
g.setup(pirP, g.IN)

pwmV = g.PWM(sPin, 50)

pwmV.start(0)

try:
    while ( True ):

        
        if (g.input(pirP) == True):
            print("Motion On")
            pwmV.ChangeDutyCycle(10)
            time.sleep(4)
            pwmV.ChangeDutyCycle(2.5)

        else:
            print("Motion Off")

        time.sleep(2)

except Exception as e:
    print(e)

finally:
    print("end")
    pwmV.stop()
    g.cleanup()
    
