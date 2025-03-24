import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

while True:
    time.sleep(0.5)
    GPIO.output(24, 1)
    time.sleep(0.5)
    GPIO.output(24, 0)