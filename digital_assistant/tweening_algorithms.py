""" Algorithms used for tweening values """

import random

# from abc import ABC

# assume val is between 0 and 1
# return pos between 0 and 1
MAX_POS = 1
MIN_POS = 0


class TweeningAlgorithm(object):
    """ A tweening algorithm, used to determine where an object should be
    along a range, given a % progress """

    min_pos = MIN_POS
    max_pos = MAX_POS

    def set_min(self, val: float):
        """ Sets ``min_pos`` to ``val``"""
        self.min_pos = val

    def set_max(self, val: float):
        """ Sets ``max_pos`` to ``val``"""
        self.max_pos = val

    def set_min_max(self, lo: float, hi: float):
        """ Sets ``min_pos`` to ``lo`` and ``max_pos`` to ``hi``"""
        self.min = lo
        self.max = hi

    def _calc(self, t: float) -> float:
        """ Implement this as a way to find the current position as a function of time """
        raise NotImplementedError

    def get_pos(self, t: float, **kwargs) -> float:
        pos = self._calc(t, **kwargs)
        if pos > self.max_pos:
            return self.max_pos
        return pos


class TweenLinear(TweeningAlgorithm):
    """ Linear algorithm, given a slope (default 1)"""

    def __init__(self, slope: float = 1.0):
        self.slope = slope

    def _calc(self, t: float, slope: float = None):
        """ Calculate position linearally """
        if slope is None:
            slope = self.slope
        return t * slope


class TweenQuadratic(TweeningAlgorithm):
    """ Quadratic algorithm, given a power (default 2) """

    def __init__(self, pwr: int = 2):
        self.pwr = pwr

    def _calc(self, t: float, pwr: int = None) -> float:
        """ Quadratic (square) algorithm """
        if pwr is None:
            pwr = self.pwr
        return t ** pwr


class TweenRandomStep(TweeningAlgorithm):
    """ Tween a random amount of progress forward, up to a max (default .1)"""

    def __init__(self, max_step: float = 0.1):
        self.max_step = max_step

    def _calc(self, t: float, max_step: float = None) -> float:
        """ Random step algorithm """
        if max_step is None:
            max_step = self.max_step
        step = random.uniform(0, max_step)
        return t + step
