import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

input_value = GPIO.input(21)
GPIO.output(24, input_value)

