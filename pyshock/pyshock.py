# -*- coding: utf-8 -*-
"""
pyshock
=====

Python Shock Response Spectrum (SRS) Library.
"""

import numpy as np
from scipy.integrate import cumtrapz

REFERENCE_FREQUENCY = 1


def nth_octave(steps):
    """return n\ :sup:`th`\ octave equivalent to steps

    :param n: number of steps
    :tye n: int
    :return: n\ :sup:`th`\ -octave

    :Example:

    >>> import pyshock
    >>> pyshock.nth_octave(40)
    12
    """
    return steps // 10 * 3


def center_frequency(n, reference=REFERENCE_FREQUENCY, steps=20):
    """returns center frequency of the n\ :sup:`th`\ -band

    :param n: band numbers
    :param reference: reference frequency
    :param steps: number of steps
    :type n: numpy.ndarray
    :type reference: int
    :type steps: int
    :return: centre frequency of nth-octave band
    :rtype: numpy.ndarray

    :Example:

    >>> import pyshock
    >>> import numpy as np
    >>> pyshock.center_frequency(np.arange(3), 1, 20)
    array([ 1.  ,  1.12,  1.26])

    """
    return (reference * 10 ** ((3 / 10 / nth_octave(steps)) * n)).round(2)
