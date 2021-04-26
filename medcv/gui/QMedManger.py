# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
from PIL import Image

import medcv
from medcv.utils.lut_fn import generate_lut_fn
from medcv.utils.arg_support import expected_type


class QMedManager(object):
    def __init__(self, *args, **kwargs):

        self.window_width = None
        self.window_level = None

        self.min_value = None
        self.max_value = None

        self.invert = False

        self.offset = None
        self.lut_array = None
        self.medical_image = None

    def pixmap(self):
        if self.medical_image is None:
            raise AttributeError('medical image must be initialized before pixmap() method called')
        slice_image = np.take(self.lut_array, self.medical_image - self.offset)
        rgb_image = np.dstack((slice_image, slice_image, slice_image))
        return Image.fromarray(rgb_image, mode='RGB').toqpixmap()

    def lut_image(self):
        if self.medical_image is None:
            raise AttributeError('medical image must be initialized before lut_image() method called')
        return np.take(self.lut_array, self.medical_image - self.offset)

    def update_lut_array(self):
        lut_fn = generate_lut_fn(self.window_width, self.window_level, y_min=0, y_max=255, mode=medcv.LINEAR_MODE)
        if self.invert:
            for x in range(self.min_value, self.max_value + 1):
                self.lut_array[x - self.offset] = 255 - lut_fn(x)
        else:
            for x in range(self.min_value, self.max_value + 1):
                self.lut_array[x - self.offset] = lut_fn(x)

    @expected_type(invert=bool)
    def set_invert(self, invert):
        self.invert = invert

    def is_invert(self) -> bool:
        return self.invert

    @expected_type(medical_image=np.ndarray)
    def set_medical_image(self, medical_image):
        self.medical_image = np.squeeze(medical_image)
        self.min_value, self.max_value = np.min(self.medical_image), np.max(self.medical_image)

        if self.window_width is None:
            self.window_width = max(int(self.max_value - self.min_value), 1)
        if self.window_level is None:
            self.window_level = int((self.max_value + self.min_value) / 2)

        self.offset = min(self.min_value, 0)
        self.lut_array = np.zeros(self.max_value - self.offset + 1, dtype=np.uint8)
        self.update_lut_array()

    def get_medical_image(self) -> np.ndarray:
        return self.medical_image

    @expected_type(window_width=int)
    def set_image_window_width(self, window_width):
        if window_width < 1:
            raise TypeError('window width must be greater than 0')
        self.window_width = window_width
        self.update_lut_array()

    def get_image_window_width(self) -> int:
        return self.window_width

    @expected_type(window_level=int)
    def set_image_window_level(self, window_level):
        self.window_level = window_level
        self.update_lut_array()

    def get_image_window_level(self) -> int:
        return self.window_level

    @expected_type(window_width=int, window_level=int)
    def set_image_window(self, window_width, window_level):
        if window_width < 1:
            raise TypeError('width must be greater than 0')
        self.window_width, self.window_level = window_width, window_level
        self.update_lut_array()

    def get_image_window(self) -> (int, int):
        return self.window_width, self.window_level

    def __bool__(self):
        return self.medical_image is not None

