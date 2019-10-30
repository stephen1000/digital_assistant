from adafruit_circuitplayground.express import cpx
import time
#import datetime as dt
import random


cpx.pixels.brightness = .01

def random_color():
    return tuple(random.randint(50,255) for _ in range(3))

def normalize(val, lo, hi):
    """ Normalize a value within a provide range """
    return (
        (val - lo) /
        (hi - lo)
    )

def normalize_color(val, lo, hi):
    """ Same as ``normalize``, but multiplies by 255 to get an rgb value """
    return (abs(normalize(val, lo, hi)) * 255) // 1

def temp_color():
    temp = cpx.temperature
    blue = normalize_color(temp, 0, 40) if temp <= 25 else 0 
    red = normalize_color(temp, 0, 40) if temp >= 15 else 0 
    green = 0
    return (red,blue,green)

cpx.pixels.brightness = .01

while True:
    time.sleep(.075)
    if cpx.switch:
        cpx.pixels.fill(random_color())
    else:
        cpx.pixels.fill(temp_color())