import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

# def adc():
#     start = time.time()
#     value = 0
#     for i in range(8):
#         value += 2**(7-i)
#         GPIO.output(dac, decimal2binary(value))
#         time.sleep(0.0007)
#         if GPIO.input(comp) == 1:
#             value -= 2**(7-i)
#     end = time.time()
#     res = end - start
#     return value, res

def adc():
    start = time.time()
    value = 128

    # GPIO.output(dac, decimal2binary(value + 128))
    # time.sleep(0.0007)
    # if GPIO.input(comp) == 0:
    #     value += 128

    GPIO.output(dac, decimal2binary(value + 64))
    time.sleep(0.0007)
    if GPIO.input(comp) == 0:
        value += 64
    else:
        value -= 64

    GPIO.output(dac, decimal2binary(value + 32))
    time.sleep(0.0007)
    if GPIO.input(comp) == 0:
        value += 32
    else:
        value -= 32

    GPIO.output(dac, decimal2binary(value + 16))
    time.sleep(0.0007)
    if GPIO.input(comp) == 0:
        value += 16
    else:
        value -= 16

    GPIO.output(dac, decimal2binary(value + 8))
    time.sleep(0.0007)
    if GPIO.input(comp) == 0:
        value += 8
    else:
        value -= 8

    GPIO.output(dac, decimal2binary(value + 4))
    time.sleep(0.0007)
    if GPIO.input(comp) == 0:
        value += 4
    else:
        value -= 4

    GPIO.output(dac, decimal2binary(value + 2))
    time.sleep(0.0007)
    if GPIO.input(comp) == 0:
        value += 2
    else:
        value -= 2

    GPIO.output(dac, decimal2binary(value + 1))
    time.sleep(0.0007)
    if GPIO.input(comp) == 0:
        value += 1
    else:
        value -= 1

    end = time.time()
    res = end - start
    return value, res

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
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()