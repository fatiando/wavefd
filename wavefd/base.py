"""
Base simulation class.
"""
import numpy as np


class BaseFD2D():
    """
    Base class for the 2D simulations.
    """

    def __init__(self):
        self.bla = 10

    def some_method(self):
        """
        Do something.
        """
        return np.ones(self.bla)

    def another(self):
        """
        Do another thing.
        """
        return np.zeros(self.bla)
