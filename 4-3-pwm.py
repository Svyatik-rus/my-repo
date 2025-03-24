import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwm_pin = 21
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 100)

pwm.start(0)

try:
    while True:
        user = input()
        if user.lower() == 'q':
            print('Interrupt')
            break
        try:
            cycle = float(user)
            if cycle < 0 or cycle > 100:
                print("Limits")
                continue

            pwm.ChangeDutyCycle(cycle)

            volt = (cycle/100)*3.3
            print(volt)
        except ValueError:
            print("Non num")
finally:
    pwm.stop()
    GPIO.cleanup()