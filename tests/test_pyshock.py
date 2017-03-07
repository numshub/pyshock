#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyshock
----------------------------------

Tests for `pyshock` module.
"""

import numpy as np
import pytest


from pyshock import pyshock


@pytest.fixture
def bands():
    """Reference bands
    """
    return np.arange(21)


def test_nth_band():
    assert pyshock.nth_octave(10) == 3
    assert pyshock.nth_octave(20) == 6
    assert pyshock.nth_octave(40) == 12
    assert pyshock.nth_octave(80) == 24


def test_center_frequency(bands):
    freqs = pyshock.center_frequency(bands)
    right = np.array([1., 1.12, 1.26, 1.41, 1.58,
                      1.78, 2., 2.24, 2.51, 2.82,
                      3.16, 3.55, 3.98, 4.47, 5.01,
                      5.62, 6.31, 7.08, 7.94, 8.91, 10.])
    np.testing.assert_array_equal(freqs, right)
