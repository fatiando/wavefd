"""
Classes to evaluate and sample wavelets.
"""
import copy

import numpy as np


class BaseWavelet():
    """
    Base class for wavelets.

    Implements the ``sample`` method to extract samples with a given sampling
    rate.
    """

    def __init__(self, frequency, amplitude, delay):
        assert frequency > 0, 'Frequency must be >= 0.'
        self.amplitude = amplitude
        self._delay = delay
        self.frequency = frequency
        self.default_delay = 0

    @property
    def delay(self):
        """
        Use the user specified or default delay.
        """
        if self._delay == 'default':
            return self.default_delay
        return self._delay

    def copy(self):
        """
        Return a deep copy of the wavelet.
        """
        return copy.deepcopy(self)

    def sample(self, dt, duration=None):
        """
        Sample the wavelet with the given sampling interval and duration.

        Parameters
        ----------
        * dt : float
            The sampling interval.
        * duration : float or ``None``
            The time duration of the sampling. If not ``None`` will use twice
            the *delay* attribute.

        Returns
        -------
        * samples : 1d-array
            An array of sample values of the wavelet.

        """
        if duration is None:
            duration = self.delay + 1/self.frequency
        times = np.arange(0, duration, dt)
        samples = self(times)
        return samples


class RickerWavelet(BaseWavelet):
    r"""
    The Ricker (mexican hat) wavelet.

    .. math::

        w(t) = A \left(1 - 2(\pi f t)^2 \right)e^{-(\pi f t)^2}

    This class can be called as a function to evaluate the wavelet at given
    times. See the examples below.

    Parameters
    ----------
    * frequency : float
        The peak (or central) frequency of the wavelet (:math:`f`).
    * amplitude : float
        The amplitude of the wavelet (:math:`A`).
    * delay : float or ``'default'``
        A time delay to be applied to the wavelet function. If ``'default'``
        will delay the wavelet by :math:`1/f` to guarantee that the
        wavelet starts approximately after time 0.

    Examples:

    >>> w1 = RickerWavelet(frequency=2)
    >>> times = np.linspace(0, 1, 7)
    >>> # The wavelet class can be called as function of time
    >>> values = w1(times)
    >>> # which gives the wavelet values at those times
    >>> print('[{}]'.format(' '.join(['{:.3f}'.format(v) for v in values])))
    [-0.001 -0.097 -0.399 1.000 -0.399 -0.097 -0.001]
    >>> # Notice that the wavelet is symmetric around the 1 amplitude value

    >>> # We can control the delay. 0 will make the peak amplitude at t=0.
    >>> w2 = RickerWavelet(frequency=1, delay=0)
    >>> values = w2(times)
    >>> print('[{}]'.format(' '.join(['{:.3f}'.format(v) for v in values])))
    [1.000 0.343 -0.399 -0.334 -0.097 -0.013 -0.001]

    >>> # We can also control the amplitude of the wavelet
    >>> w3 = RickerWavelet(frequency=2, amplitude=-0.5)
    >>> values = w3(times)
    >>> print('[{}]'.format(' '.join(['{:.3f}'.format(v) for v in values])))
    [0.000 0.048 0.199 -0.500 0.199 0.048 0.000]

    >>> # Use the 'sample' method to extract samples at a given time interval
    >>> w4 = RickerWavelet(frequency=5, amplitude=10)
    >>> samples = w4.sample(dt=0.05)
    >>> print('[{}]'.format(' '.join(['{:.3f}'.format(v) for v in samples])))
    [-0.010 -0.392 -3.337 -1.261 10.000 -1.261 -3.337 -0.392]
    >>> # Notice that the end point is not included because 'sample' uses
    >>> # numpy.arange.
    >>> # The default duration of the sampling is usually enough to get the
    >>> # whole wavelet but you can control this if you want.
    >>> samples = w4.sample(dt=0.05, duration=0.25)
    >>> print('[{}]'.format(' '.join(['{:.3f}'.format(v) for v in samples])))
    [-0.010 -0.392 -3.337 -1.261 10.000]

    """

    def __init__(self, frequency, amplitude=1, delay='default'):
        super().__init__(frequency, amplitude, delay)
        self.default_delay = 1/self.frequency

    def __call__(self, time):
        """
        Evaluate the wavelet function at a given time.

        Parameters:

        * time : int, float or array
            The time(s) at which to evaluate the wavelet.

        Returns:

        * wavelet : int, float or array
            The wavelet function values at the given time(s).

        """
        t = time - self.delay
        aux = (np.pi*self.frequency*t)**2
        res = (1 - 2*aux)*np.exp(-aux)
        return self.amplitude*res
