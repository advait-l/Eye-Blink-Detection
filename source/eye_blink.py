import RPi.GPIO as GPIO
import time

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)

try:
    while True:
        print(GPIO.input(sensor))


except KeyboardInterrupt:
    GPIO.cleanup()
