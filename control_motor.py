import RPi.GPIO as g
import time
import Adafruit_DHT


# motor Pin control
motorA_1_Pin = 23 # forward
motorA_2_Pin = 24 # backward


# set GPIO Pin
g.setmode(g.BCM)

# set the using Pin
g.setup(motorA_1_Pin, g.OUT)
g.setup(motorA_2_Pin, g.OUT)

# set PWM objects for using PWM control 
motorA_1_PWM = g.PWM(motorA_1_Pin, 100)
motorA_2_PWM = g.PWM(motorA_2_Pin, 100)

# start PWM
motorA_1_PWM.start(0)
motorA_2_PWM.start(0)



try:
    # write code which can occur errors
    rotate = 0
    while(True):
        motorA_1_PWM.ChangeDutyCycle(rotate)
        time.sleep(5)
        rotate += 10
        if (rotate > 100):
            break
        
except Exception as e:
    # write the code control error massages
    print(e)
    
finally:
    # Regardless the error, finally this code will be executed
    motorA_1_PWM.stop() # end PWM 
    g.cleanup() # reset GPIO Pin







