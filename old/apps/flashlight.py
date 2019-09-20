from base_app import BaseApp
from adafruit_circuitplayground.express import cpx
from colors import WHITE


class FlashlightApp(BaseApp):
    """ An app that lights up the room """

    APP_NAME = "flashlight"
    BRIGHTNESS = 1
    COLOR = WHITE

    def __init__(self):
        self.last_brightness = cpx.pixels.brightness
        self.last_colors = [x for x in cpx.pixels]

    def start(self):
        print('color is-', ', '.join(str(x) for x in cpx.pixels))
        print('color gon be', self.COLOR)
        cpx.pixels.fill(self.COLOR)
        print('color is-', ', '.join(str(x) for x in cpx.pixels))
        print('bright is', cpx.pixels.brightness)
        print('bright gon be', self.BRIGHTNESS)
        cpx.pixels.brightness = self.BRIGHTNESS
        print('bright is', cpx.pixels.brightness)

    def stop(self):
        cpx.pixels.brightness = self.last_brightness
        for index, color in enumerate(self.last_colors):
            cpx.pixels[index] = color
