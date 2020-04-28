import time
import RPi.GPIO as GPIO

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

try:
    BLINK_SEQUENCES = [ "1001", "0110", "1010", "0101", "1100", "0011"]

    def recordBlinkSequence():
        print("You have 4 seconds to record the blink")
        t_end = time.time() + 4
        recorded_bits = ""
        while time.time() < t_end:
            bit = GPIO.input(sensor)
            recorded_bits += str(bit)
            time.sleep(0.1)
        print(recorded_bits)
        return recorded_bits

    def countDown():
        print("Record the blink sequence on count of 3")
        time.sleep(1)
        for i in range(3):
            print(i%3 + 1)
            time.sleep(1)

    def storeBlinkSequence(blink_sequence, recorded_bits):
        print("Storing the recorded blink sequence")
        with open("../data/" + blink_sequence + ".csv", 'a') as fd:
            fd.write("\n" + recorded_bits)

    if __name__=="__main__":

        for blink_sequence in BLINK_SEQUENCES:
            print("Recording: " + blink_sequence)
            countDown()
            recorded_bits = recordBlinkSequence()
            storeBlinkSequence(blink_sequence, recorded_bits)


except KeyboardInterrupt:
    GPIO.cleanup()
