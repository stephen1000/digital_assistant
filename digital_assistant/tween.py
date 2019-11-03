""" Provide tweening between two values based on a percent progress.
Algorithms are imported here for convenience """
import tweening_algorithms


class Tweener(object):
    """ A tweener object that provides intermediate values for
    a given range of time, based on a provided algorithm object """

    def __init__(
        self,
        algorithm: tweening_algorithms.TweeningAlgorithm,
        lo: float = 0.0,
        hi: float = 1.0,
    ):
        self.algorithm = algorithm
        self.lo = lo
        self.hi = hi

    @property
    def range(self):
        """ The difference between ``hi`` (max) and ``lo`` (min) """
        return self.hi - self.lo

    def _fit_to_range(self, val: float) -> float:
        """ fits a normalized value into this object's range of values """
        return self.lo + (val * self.range)

    def get_pos(self, t: float) -> float:
        """ gets the position at %time t """
        pos = self.algorithm.get_pos(t)
        return self._fit_to_range(pos)


class ColorTweener(object):
    """ A tweener for two colors """

    def __init__(
        self, algorithm: tweening_algorithms.TweeningAlgorithm, *colors: tuple
    ):
        self.algorithm = algorithm
        self.colors = colors
        self.color_index = 0

        # lazilly load tweeners as needed
        self.red_tweener = None
        self.green_tweener = None
        self.blue_tweener = None
        self._reset_tweeners()

    @property
    def color(self) -> tuple:
        return self.colors[self.color_index]

    @property
    def next_color(self) -> tuple:
        index = self.color_index + 1
        index %= len(self.colors)
        return self.colors[index]

    def _move_to_next_color(self) -> tuple:
        """ Advance to the next color in list and return its value """
        self.color_index += 1
        self.color_index %= len(self.colors)
        self._reset_tweeners()
        return self.color

    def _reset_tweeners(self):
        """ Blank out tweeners """
        self.red_tweener = Tweener(
            self.algorithm, lo=self.color[0], hi=self.next_color[0]
        )
        self.green_tweener = Tweener(
            self.algorithm, lo=self.color[1], hi=self.next_color[1]
        )
        self.blue_tweener = Tweener(
            self.algorithm, lo=self.color[2], hi=self.next_color[2]
        )

    def get_color(self, t: float) -> tuple:
        print("getting diff between", self.color, "and", self.next_color)
        color = (
            int(self.red_tweener.get_pos(t)),
            int(self.green_tweener.get_pos(t)),
            int(self.blue_tweener.get_pos(t)),
        )

        if t >= 1:
            self._move_to_next_color()

        return color
