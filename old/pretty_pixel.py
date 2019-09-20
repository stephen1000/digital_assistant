"""
A pixel that's pretty!

Given a target color and brightness, the pixel will gradually tick towards
the target from its current position (in the specified interval).

Will probably do a sine ease.
"""


class PrettyColor:
    """
    A very pretty color
    """

    def __init__(self, start_time, color, brightness, interval=1):
        self.color = self.color_correct(color)
        self.brightness = brightness
        self.interval = interval

    def tick(self, now):
        diff = (now - self.start_time) / self.interval

    def color_correct(self, color):
        return [int(255*v) if v < 1 else v for v in color]


class PrettyPixel:
    """
    The prettiest pixel of them all!
    """

    def __init__(self, pixel, initial):
        self.pixel = pixel
        self.initial = initial
