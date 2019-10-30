""" Provide tweening between two values based on a percent progress.
Algorithms are imported here for convenience """
import tweening_algorithms

class Tweener(object):
    """ A tweener object that provides intermediate values for
    a given range of time, based on a provided algorithm object """
    
    def __init__(self, algorithm:tweening_algorithms.TweeningAlgorithm, lo:float=0.0, hi:float=0.0):
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
