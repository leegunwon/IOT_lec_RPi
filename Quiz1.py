import smbus
import RPi.GPIO as g
import time
import Adafruit_DHT
import threading

LED = 12
dhtPin = 13


# motor Pin control
motorA_1_Pin = 23 # forward
motorA_2_Pin = 24 # backward

g.setwarnings(False)

# set GPIO Pin
g.setmode(g.BCM)

# set the using Pin

g.setup(LED, g.OUT)
g.setup(dhtPin, g.OUT)  # send signal
g.setup(motorA_1_Pin, g.OUT)
g.setup(motorA_2_Pin, g.OUT)


sType = Adafruit_DHT.DHT22
I2C_CH = 1

# set PWM objects for using PWM control 
motorA_1_PWM = g.PWM(motorA_1_Pin, 100)
motorA_2_PWM = g.PWM(motorA_2_Pin, 100)

# start PWM
motorA_1_PWM.start(0)
motorA_2_PWM.start(0)

# set lux sensor
BH1750_DEV_ADDR = 0x23


CONT_H_RES_MODE = 0x10
CONT_H_RES_MODE2 = 0x11
CONT_L_RES_MODE = 0x13
ONETIME_H_RES_MODE = 0x20
ONETIME_H_RES_MODE2 = 0x21
ONETIME_L_RES_MODE = 0x23

def readLux() :
    # create i2c channel 
    i2c = smbus.SMBus(I2C_CH)
    # recieve 2bytes data from i2c with CONT_H_RES_MODE
    luxBytes = i2c.read_i2c_block_data(BH1750_DEV_ADDR, CONT_H_RES_MODE, 2)
    # change format of data to int from byte vector
    lux = int.from_bytes(luxBytes, byteorder='big')
    i2c.close()
    return lux

def led_on(pin):
    g.output(pin, True)
    
def led_off(pin):
    g.output(pin, False)

def run_motor(lux):
    if (lux > 100):
        motorA_1_PWM.ChangeDutyCycle(100)
        led_on(LED)
        
    elif (lux < 100):
        motorA_1_PWM.ChangeDutyCycle(50)
        led_off(LED)
    print("no_lux")
        
def readData(sensor, pin):
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    lux = readLux()
    return hum, temp, lux

try:
    # write code which can occur errors
    rotate = 0
    while(True):
        hum, temp, lux = readData(sType, dhtPin)
        
        if(temp >= 24):
            run_motor(lux)
        elif(temp < 24):
            motorA_1_PWM.ChangeDutyCycle(0)
            
        
except Exception as e:
    # write the code control error massages
    print(e)
    
finally:
    # Regardless the error, finally this code will be executed
    motorA_1_PWM.stop() # end PWM 
    g.cleanup() # reset GPIO Pin







