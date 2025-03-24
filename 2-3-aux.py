import RPi.GPIO as GPIO
import time

leds=[2, 3, 4, 17, 27,22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
aux = [21, 20, 26, 16, 19, 25, 23, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)``
GPIO.setup(aux, GPIO.IN, pull_up_down=GPIO.PUD_UP)
state = [0, 0, 0, 0, 0, 0, 0, 0]

while True:
    GPIO.output(dac, state)
    time.sleep(0.1)
    for i in range(len(leds)):
        state[i] = GPIO.input(aux[i])
        # aux_t = GPIO.input(aux[i])
        # led_t = not aux_t
        # GPIO.output(leds[i], led_t)
    GPIO.output(leds, state)


GPIO.ouput(leds, [0]*len(leds))
GPIO.cleanup()