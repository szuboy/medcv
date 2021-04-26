# !/usr/bin/env python
# -*- coding:utf-8 -*-

import medcv
import numpy as np


def linear_fn(width, center, y_min, y_max):
    def fn(x):
        if x <= center - 0.5 - (width - 1) / 2:
            y = y_min
        elif x > center - 0.5 + (width - 1) / 2:
            y = y_max
        else:
            y = ((x - (center - 0.5)) / (width - 1) + 0.5) * (y_max - y_min) + y_min
        return y
    return fn


def sigmoid_fn(width, center, y_min, y_max):
    def fn(x):
        return (y_max - y_min) / (1 + np.exp(-4 * (x - center) / width)) + y_min
    return fn


def linear_extract_fn(width, center, y_min, y_max):
    def fn(x):
        if x <= center - width / 2:
            y = y_min
        elif x > center + width / 2:
            y = y_max
        else:
            y = ((x - center) / width + 0.5) * (y_max - y_min) + y_min
        return y
    return fn


def generate_lut_fn(width, center, y_min, y_max, mode):
    if width < 1:
        raise TypeError('width must be greater than 0')

    if mode == medcv.LINEAR_MODE:
        return linear_fn(width, center, y_min, y_max)
    elif mode == medcv.SIGMOID_MODE:
        return sigmoid_fn(width, center, y_min, y_max)
    else:
        return linear_extract_fn(width, center, y_min, y_max)

