import random
import colors


class Cycler:
    """
    Manages cycling the wheel of pixels
    """

    def __init__(self, pixels, length, start_position=0):
        self.pixels = pixels
        self.length = length
        self.position = start_position
        self.direction = True

    def next(self):
        """ moves either forward or back """
        if self.direction:
            self.forward()
        else:
            self.back()
        self.show()

    def reverse(self):
        """ change directions """
        self.direction = not self.direction

    def forward(self):
        """ Increments position, bound to max length """
        self.position += 1
        self.position %= len(self.pixels)

    def back(self):
        """ Decrements position """
        self.position -= 1
        if self.position < 0:
            self.position += len(self.pixels)

    def show(self):
        for pixel_num in range(len(self.pixels)):
            if (pixel_num in self.arced_pixels):
                self.pixels[pixel_num] = self.random_color
            else:
                self.pixels[pixel_num] = colors.BLACK
        self.pixels.show()

    @property
    def arced_pixels(self):
        """ Returns the current position, and the trailing pixels. """
        arced_pixels = []
        for spaces_back in range(self.length):
            arced_pixels.append((self.position - spaces_back) %
                                len(self.pixels))
        return arced_pixels

    @property
    def random_color(self):
        return list(random.randint(50, 255) for _ in range(3))
