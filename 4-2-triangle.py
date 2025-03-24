import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 8, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]


try:
    per = float(input("Ener the signal time in seconds: "))

    while True:
        for val in range(256):
            bin_val = dec2bin(val)
            GPIO.output(dac, bin_val)
            time.sleep(per / 512)
        for val in range(255, -1, -1):
            bin_val = dec2bin(val)
            GPIO.output(dac, bin_val)
            time.sleep(per / 512)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()