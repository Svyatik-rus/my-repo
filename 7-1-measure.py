import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def update_leds(value):
    binary = decimal2binary(int(value/3.3*255))
    GPIO.output(leds, binary)

def adc():
    start = time.time()
    value = 128

    # GPIO.output(dac, decimal2binary(value + 128))
    # time.sleep(0.0007)
    # if GPIO.input(comp) == 0:
    #     value += 128

    GPIO.output(dac, decimal2binary(value + 64))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        value += 64
    else:
        value -= 64

    GPIO.output(dac, decimal2binary(value + 32))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        value += 32
    else:
        value -= 32

    GPIO.output(dac, decimal2binary(value + 16))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        value += 16
    else:
        value -= 16

    GPIO.output(dac, decimal2binary(value + 8))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        value += 8
    else:
        value -= 8

    GPIO.output(dac, decimal2binary(value + 4))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        value += 4
    else:
        value -= 4

    GPIO.output(dac, decimal2binary(value + 2))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        value += 2
    else:
        value -= 2

    GPIO.output(dac, decimal2binary(value + 1))
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        value += 1
    else:
        value -= 1

    end = time.time()
    res = end - start
    return value, res

try:
    print("Start")
    measurements = []
    start_time = time.time()


    GPIO.output(troyka, 1)
    while True:
        value, _ = adc()
        voltage = value *3.3/256
        measurements.append(voltage)
        update_leds(voltage)
        # time.sleep(0.01)
        if voltage >= 0.97*3.3:
            break

    GPIO.output(troyka, 0)
    while True:
        value, _ = adc()
        voltage = value *3.3/256
        measurements.append(voltage)
        update_leds(voltage)
        # time.sleep(0.01)
        if voltage <= 0.02*3.3:
            break

    end_time = time.time()
    duration = end_time - start_time
    rate = len(measurements)/duration
    step = 3.3/256


    plt.plot(measurements)
    plt.grid()
    plt.show()

    with open("data.txt", "w") as data_file:
        data_file.write("\n".join(map(str, measurements)))
    with open("setting.txt", "w") as settings_file:
        settings_file.write(f"Time poln: {duration:.2f} c\n")
        settings_file.write(f"Time 1 izm: {1 / rate:.6f} c\n")
        settings_file.write(f"Rate: {rate:.2f} Hertz\n")
        settings_file.write(f"Step: {step:.3f} V")
    
    print(f"Time poln: {duration:.2f} c\n")
    print(f"Time 1 izm: {1 / rate:.6f} c\n")
    print(f"Rate: {rate:.2f} Hertz\n")
    print(f"Step: {step:.3f} V")

finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()


