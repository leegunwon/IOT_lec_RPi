import smbus
import time
import RPi.GPIO as g
import threading

LED = 12

g.setwarnings(False)
g.setmode(g.BCM)
g.setup(LED, g.OUT)

LED_PWM = g.PWM(LED, 100)
LED_PWM.start(0)

I2C_CH = 1

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

def main() :
    while True :
        luxV = readLux()
        print(f"{luxV} lux")

        if (int(luxV) < 100) :
            LED_PWM.ChangeDutyCycle(20)
            
        elif (int(luxV) < 300) :
            LED_PWM.ChangeDutyCycle(50)
            
        elif (int(luxV) < 500) :
            LED_PWM.ChangeDutyCycle(100)
        time.sleep(5)
        
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        g.cleanup()

