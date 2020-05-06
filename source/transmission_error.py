import RPi.GPIO as GPIO
import time

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

try:
    GROUND_TRUTH = ""
    for i in range(10):
        GROUND_TRUTH += 10*str((i+1)%2)

    def recordBits():
        print("Start now...")
        recorded_bits = ""
        while len(recorded_bits) < 100: 
            bit = GPIO.input(sensor)
            recorded_bits += str(bit)
            time.sleep(0.1)
        print(recorded_bits)
        return recorded_bits

    def storeBits(recorded_bits):
        print("Storing trial...")
        with open("../data/trials.txt", 'a') as fd:
            fd.write("\n" + recorded_bits)
   
    def hammingDistance(string1, string2):
        hamming_distance = 0
        i = 0
        while i < len(string1):
            if(string1[i] != string2[i]):
                hamming_distance += 1
            i += 1
        return hamming_distance 
    
    def mean(lst):
        return reduce(lambda a, b: a + b, lst) / len(lst)

    def calculateTransmissionError():
        percent_transmission_error = []
        with open("../data/trials.txt") as fd:
            lines = (line.rstrip() for line in fd) 
            lines = (line for line in lines if line)
            for line in lines:
                hd = hammingDistance(line, GROUND_TRUTH)
                ptr = float(hd) / len(GROUND_TRUTH)
                percent_transmission_error.append(ptr)

        print(percent_transmission_error)
        average_transmission_error = mean(percent_transmission_error)
        print("Probability of error in transmission: " + str(average_transmission_error))
        return percent_transmission_error

    
    if __name__ == "__main__":
        print(GROUND_TRUTH)
        print("Keep blinking...")
        recorded_bits = recordBits()
        storeBits(recorded_bits)
        calculateTransmissionError()
        


except KeyboardInterrupt:
    GPIO.cleanup()
