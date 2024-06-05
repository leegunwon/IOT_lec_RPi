import RPi.GPIO as g
import time
import Adafruit_DHT

dhtPin = 13
GledP = 20
RledP = 21

g.setmode(g.BCM)  # GPIO pin setting
                    # BOARD, BCM
g.setup(dhtPin, g.OUT)  # send signal
g.setup(GledP, g.OUT)
g.setup(RledP, g.OUT)

sType = Adafruit_DHT.DHT22

def led_on(pin):
    g.output(pin, True)
    
def led_off(pin):
    g.output(pin, False)

def readData(sensor, pin):
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    if hum is not None and temp is not None:
        print(f'Hum:{hum} temp:{temp}')
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
    if (hum > 70):
        led_on(GledP)
    else:
        led_off(GledP)
    if (temp > 25.5):
        led_on(RledP)
    else:
        led_off(RledP)
    time.sleep(2)
    
def main():
    print("call main function")
    while (True):
        readData(sType, dhtPin)
        
    
if (__name__ == "__main__"):
    main()


