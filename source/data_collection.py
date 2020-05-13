import time
import RPi.GPIO as GPIO

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

try:
    BLINK_SEQUENCES = ["1010", "0101", "1100", "0011"]


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

    def majorityLogic(sequence):
        detected_sequence = ""
        index = 0
        for i in range(4):
            ones = sequence.count("1", index, index + 10)
            zeros = sequence.count("0", index, index + 10)
            if(zeros >= ones):
                detected_sequence += "0"
            else:
                detected_sequence += "1"
            index += 10
        print("Detecting sequence...")
        print(detected_sequence)
        return detected_sequence


    def storeBlinkSequence(blink_sequence, recorded_bits, detected_sequence):
        print("Storing the recorded blink sequence...")
        status = "Failure"
        if(blink_sequence == detected_sequence):
            status = "Success"

        with open("../data/detected_sequences.csv", 'a') as fd:
            fd.write("\n" + blink_sequence + "," + recorded_bits + "," + detected_sequence + "," + status + ";")

    if __name__=="__main__":

        for blink_sequence in BLINK_SEQUENCES:
            print("****************************************")
            print("Recording: " + blink_sequence)
            countDown()
            recorded_bits = recordBlinkSequence()
            detected_sequence = majorityLogic(recorded_bits)
            storeBlinkSequence(blink_sequence, recorded_bits, detected_sequence)


except KeyboardInterrupt:
    GPIO.cleanup()
