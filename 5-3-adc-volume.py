import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
led_pins = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(led_pins, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    start = time.time()
    value = 0
    for i in range(8):
        value += 2**(7-i)
        GPIO.output(dac, decimal2binary(value))
        time.sleep(0.0007)
        if GPIO.input(comp) == 1:
            value -= 2**(7-i)
    end = time.time()
    res = end - start
    return value, res

def light_leds(num_leds):
    for i in range(len(led_pins)):
        if i < num_leds:
            GPIO.output(led_pins[i], GPIO.HIGH)
        else:
            GPIO.output(led_pins[i], GPIO.LOW)

# def adc():
#     for value in range(256):
#         GPIO.output(dac, decimal2binary(value))
#         time.sleep(0.0007)
#         if GPIO.input(comp) == 1:
#             return value
#     return 255


try:
    while True:
        digital_val, res = adc()
        volt = digital_val * 3.3 / 256
        print("Digital Val: {:3d}, Volt: {:.2f} V, Time: {:.6f}".format(digital_val, volt, res))
        num_leds = int((volt / 3.3) * len(led_pins))
        num_leds = max(0, min(num_leds, len(led_pins)))

        light_leds(num_leds)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.output(led_pins, GPIO.LOW)
    GPIO.cleanup()