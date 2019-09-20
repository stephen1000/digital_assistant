from adafruit_circuitplayground.express import cpx
import time
import random

def random_color():
    return tuple(random.randint(50,255) for _ in range(3))

cpx.pixels.brightness = .01

while True:
    time.sleep(.5)
    cpx.pixels.fill(random_color())
    # for pixel_index in range(len(cpx.pixels)):
    #     cpx.pixels[pixel_index] = random_color()
    