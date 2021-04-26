# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

from medcv.utils.lut import generate_lut_array


def med2med(med_image, width=None, level=None, dtype=np.float64, invert=False):
    if width is None or level is None:
        min_value, max_value = np.min(med_image), np.max(med_image)
        width, level = int(max_value - min_value), int((max_value + min_value) / 2)
    y_min, y_max = level - width / 2, level + width / 2
    offset, lut_array = generate_lut_array(med_image, width, level, y_min=y_min, y_max=y_max, invert=invert, dtype=dtype)
    return np.take(lut_array, med_image - offset)

