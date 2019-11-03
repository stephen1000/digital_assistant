from adafruit_circuitplayground.express import cpx
import time
from tween import Tweener, tweening_algorithms, ColorTweener
import random


cpx.pixels.brightness = 0.01


def random_color():
    return tuple(random.randint(50, 255) for _ in range(3))


def normalize(val, lo, hi):
    """ Normalize a value within a provide range """
    return (val - lo) / (hi - lo)


def normalize_color(val, lo, hi):
    """ Same as ``normalize``, but multiplies by 255 to get an rgb value """
    return int(abs(normalize(val, lo, hi)) * 255)


def temp_color():
    temp = cpx.temperature
    blue = normalize_color(temp, 10, 30) if temp <= 25 else 0
    red = normalize_color(temp, 10, 30) if temp >= 15 else 0
    green = 0
    return (red, green, blue)


cpx.pixels.brightness = 0.01

MAX_Y = 0.5

linear_tweener = Tweener(tweening_algorithms.TweenLinear(), hi=MAX_Y)
quadratic_tweener = Tweener(tweening_algorithms.TweenQuadratic(), hi=MAX_Y)
cubic_tweener = Tweener(tweening_algorithms.TweenQuadratic(pwr=3), hi=MAX_Y)
random_tweener = Tweener(tweening_algorithms.TweenRandomStep(), hi=MAX_Y)
sin_tweener = Tweener(tweening_algorithms.TweenSinusoidal(), hi=MAX_Y)
exp_tweener = Tweener(tweening_algorithms.TweenExponential(), hi=MAX_Y)

tweener = linear_tweener

pos = 0

c1 = (255, 0, 0)
c2 = (0, 255, 0)
c3 = (0, 0, 255)
pallette = [
    (241, 80, 37),
    (46, 134, 171),
    (27, 153, 139),
    (162, 59, 144),
    (241, 143, 1),
]
color_tweener = ColorTweener(tweening_algorithms.TweenLinear(), c1, c2, c3, *pallette)

while True:
    if cpx.touch_A1:
        print("using linear tweener")
        tweener = linear_tweener
    elif cpx.touch_A2:
        print("using quadratic tweener")
        tweener = quadratic_tweener
    elif cpx.touch_A3:
        print("using random tweener")
        tweener = random_tweener
    elif cpx.touch_A4:
        print("using sin tweener")
        tweener = sin_tweener
    elif cpx.touch_A5:
        print("using cubic tweener")
        tweener = cubic_tweener
    elif cpx.touch_A6:
        print("using exp tweener")
        tweener = exp_tweener

    time.sleep(0.1)
    pos += 0.05
    y = round(tweener.get_pos(pos), 4)

    print("x", pos, ", y", y)

    cpx.pixels.brightness = y

    tweened_color = color_tweener.get_color(pos)
    cpx.pixels.fill(tweened_color)

    pos %= 1

    # blue = int(y)
    # red = int(MAX_Y - y)

    # c = (red, 0 , blue)

    # print('color',c)

    # if cpx.switch:
    #     cpx.pixels.fill(c)
    # else:
    #     cpx.pixels.fill(temp_color())

