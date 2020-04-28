import RPi.GPIO as GPIO
import time
import applications as app

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

try:
    commands = {
            "1001" : app.app1,
            "1101" : app.app2,
            "1010" : app.app3,
            "1100" : app.app4
            }

    while True:
        print("Initiate")
        while True:
            i = 0
            initiator = ""
            while(i < 2):
                #time.sleep(2)
                bit = GPIO.input(sensor)
                # print(bit)
                initiator += str(bit)
                i += 1
            if(initiator == "00"):
                break   
        print("New command")
        sequence = ""
        i = 0
        while(i < 4):
            print("Open or blink")
            #time.sleep(2)
            bit = GPIO.input(sensor)
            print("Recorded bit: " + str(bit))
            sequence += str(bit)
            i += 1
        print(sequence)
        time.sleep(3)
        commands[sequence]()

except KeyboardInterrupt:
    GPIO.cleanup()
   
