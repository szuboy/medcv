# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

from medcv.utils.lut import generate_lut_array


def med2grey(med_image, width=None, level=None, invert=False):
    med_image = np.squeeze(med_image)
    if len(np.shape(med_image)) != 2:
        raise ValueError('medical image should have rank 2, but received input shape: %s' % len(np.shape(med_image)))
    if width is None or level is None:
        min_value, max_value = np.min(med_image), np.max(med_image)
        width, level = int(max_value - min_value), int((max_value + min_value) / 2)
    offset, lut_array = generate_lut_array(med_image, width, level, y_min=0, y_max=255, dtype=np.uint8, invert=invert)
    return np.take(lut_array, med_image - offset)
