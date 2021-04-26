# !/usr/bin/env python
# -*- coding:utf-8 -*-

# link: https://dicom.innolitics.com/ciods/ct-image/voi-lut/00281056

import medcv
import numpy as np

from .lut_fn import generate_lut_fn
from .arg_support import expected_type


@expected_type(np.ndarray, int, int, invert=bool)
def generate_lut_array(image, width, center, y_min=0, y_max=255, dtype=np.uint8, invert=False, mode=medcv.LINEAR_MODE):

    min_value, max_value = np.min(image), np.max(image)
    offset = min(min_value, 0)
    length = max_value - offset + 1
    lut_array = np.zeros(length, dtype=dtype)

    lut_fn = generate_lut_fn(width, center, y_min, y_max, mode)

    if invert:
        for x in range(min_value, max_value + 1):
            lut_array[x - offset] = y_max - lut_fn(x)
    else:
        for x in range(min_value, max_value + 1):
            lut_array[x - offset] = lut_fn(x)
    return offset, lut_array

