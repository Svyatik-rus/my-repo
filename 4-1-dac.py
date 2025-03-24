import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 8, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, 0)

def dec_bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]


try:
    while True:
        user = input()
        if user == 'q':
            print("Interrupt")
            break

        try:
            val = int(user)
            if val < 0:
                print("Negative")
                continue
            if val > 255:
                print("Limits")
                continue
            bin_val = dec_bin(val)
            GPIO.output(dac, bin_val)
            volt = (val/255)*3.3
            print(volt)
        except ValueError:
            print("Non num")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()