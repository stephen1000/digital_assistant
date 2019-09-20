"""For a detailed guide on all the features of the Circuit Playground Express (cpx) library:
https://adafru.it/cp-made-easy-on-cpx"""
import time
import random
import microcontroller
from adafruit_circuitplayground.express import cpx


# Set TONE_PIANO to True to enable a tone piano on the touch pads!
TONE_PIANO = False

# Set this as a float from 0 to 1 to change the brightness. The decimal represents a percentage.
# So, 0.3 means 30% brightness!
cpx.pixels.brightness = .01

# Changes to NeoPixel state will not happen without explicitly calling show()
cpx.pixels.auto_write = False

# Startup behavior is based on your board's unique ID!
# uid returns a bytearray. The individual numbers are summed then modulo by 3.
board_id = 2  # sum(microcontroller.cpu.uid) % 3


def color_wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition red - green - blue - back to red.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (int(255 - pos*3), int(pos*3), 0)
    if pos < 170:
        pos -= 85
        return (0, int(255 - pos*3), int(pos*3))
    pos -= 170
    return (int(pos * 3), 0, int(255 - (pos*3)))


# Digi-Key colors: red and white!
digi_key_colors = ((255, 0, 0), (180, 180, 150))
# Python colors: blue and yellow!
python_colors = ((32, 64, 255), (255, 180, 20))

color_index = 0
pixel_number = 0
# time.monotonic() allows for non-blocking LED animations!
start = time.monotonic()


def flicker_light():
    cpx.red_led = int(time.monotonic()) % 2 == 0


def digi_key(now):
    # Flash Dnowigi-Key colors!
    if now - start > 0.5:
        color_index = (color_index + 1) % len(digi_key_colors)
        cpx.pixels.fill(digi_key_colors[color_index])
        cpx.pixels.show()
        start = now


def python_colors(now):
    # Flash Python colors!
    if now - start > 0.5:
        color_index = (color_index + 1) % len(python_colors)
        cpx.pixels.fill(python_colors[color_index])
        cpx.pixels.show()
        start = now


def red_comet(*args):
    # Red-comet rainbow swirl!
    pixel_number = (pixel_number + 1) % 10
    for p in range(10):
        color = color_wheel(25 * ((pixel_number + p) % 10))
        cpx.pixels[p] = tuple(
            [int(c * (10 - (pixel_number + p) % 10) / 10.0) for c in color])
        cpx.pixels.show()

# def fancy_mode():
#     cpx.play_file('drama.wav')


target_color = list(
    random.randint(50, 255) for _ in range(3),
)
# target_color=(0,0,255)

samples = []


def dont_throw_me_bro():
    movement = cpx.acceleration
    # cpx.pixels.fill((255,0,255))
    speed = sum(abs(thing) for thing in movement)
    x, y, z = movement
    this_color = [int(abs(m*5)) if m < 255 else 255 for m in movement]

    samples.append(this_color)
    if len(samples) >= 10:
        samples.pop(0)
    x_sum = 0
    y_sum = 0
    z_sum = 0
    for sample in samples:
        x_sum += sample[0]
        y_sum += sample[1]
        z_sum += sample[2]
    l = len(samples)
    if l:
        color = (x_sum//l, y_sum//l, z_sum//l)
    else:
        color = (255, 0, 255)

    # speed = abs(z)
    cpx.pixels.fill(color)
    decay = .15

    if speed > 15:
        cpx.pixels.brightness += speed / 100
        if cpx.pixels.brightness >= .3:
            cpx.pixels.brightness = .3
        # cpx.start_tone(1000+speed*25)
    else:
        # cpx.stop_tone()
        if cpx.pixels.brightness > decay:
            cpx.pixels.brightness -= decay
        else:
            cpx.pixels.brightness = .01

    for i, pixel in enumerate(cpx.pixels):
        if i < len(cpx.pixels)//2:
            cpx.pixels[i] = target_color
    cpx.pixels.show()
    time.sleep(.01)
    return color


def tone_piano():
    if cpx.touch_A1:
        cpx.start_tone(262)
    elif cpx.touch_A2:
        cpx.start_tone(294)
    elif cpx.touch_A3:
        cpx.start_tone(330)
    elif cpx.touch_A4:
        cpx.start_tone(349)
    elif cpx.touch_A5:
        cpx.start_tone(392)
    elif cpx.touch_A6:
        cpx.start_tone(440)
    elif cpx.touch_A7:
        cpx.start_tone(494)
    else:
        cpx.stop_tone()


modes = {
    0: digi_key,
    1: python_colors,
    2: red_comet,
    # 3: fancy_mode
}

# cpx.pixels.show()


pixel_count = len(cpx.pixels)
pixel_num = 1


def spin2win(now):
    pass
    # pixel_num+=1
    # if now - start < .5:
    #     continue

    #cpx.pixels[pixel_num] = (110,0,110)
    # c = color_wheel(100)
    # max_arc_length = 3
    # pixel_num = (pixel_num + 1) % pixel_count
    # pixels = []
    # for arc_length in range(0, max_arc_length):
    #     pixel = pixel_num - arc_length
    #     if pixel < 0:
    #         pixel += max_arc_length
    #     pixels.append(pixel)
    # for pixel in pixels:
    #     cpx.pixels[pixel] = c

    # cpx.pixels.show()
    # sleep(1)


while True:
    now = time.monotonic()
    flicker_light()
    # cpx.play_file("drama.wav")
    # modes[board_id]()
    color = None
    if now - start < 3:
        cpx.pixels.fill(target_color)
        cpx.pixels.show()
    else:
        color = dont_throw_me_bro()
    # dont_throw_me_bro()

    if not color:
        continue

    diff = 0
    for c, t in zip(color, target_color):
        diff += abs(c-t)

    if diff < 150:
        break

while True:
    if int(time.monotonic()) % 2 == 0:
        cpx.pixels.fill(target_color)
        cpx.pixels.show()
    else:
        cpx.pixels.hide()
