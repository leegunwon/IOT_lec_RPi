import RPi.GPIO as g
import time

sPin = 21
yledPin = 12
rledPin = 20


g.setmode(g.BCM)
g.setup(sPin, g.OUT)
g.setup(yledPin, g.OUT)
g.setup(rledPin, g.OUT)

pwmV = g.PWM(sPin, 50)

pwmV.start(0)


def led_on(pin):
    g.output(pin, True)
    
def led_off(pin):
    g.output(pin, False)

try:
    rotateN = 2.5
    while (True):
        
        pwmV.ChangeDutyCycle(rotateN)
        
        if (rotateN == 2.5) :
            led_off(rledPin)
            led_on(yledPin)

        if (rotateN == 5) :
            led_off(yledPin)
            
        rotateN += 2.5
            
        if (rotateN > 12.5) :
            rotateN = 2.5
            led_on(rledPin)

        time.sleep(2)
    
except Exception as e:
    print(e)
    
finally:
    pwmV.stop()
    g.cleanup()
