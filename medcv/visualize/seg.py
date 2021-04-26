# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

from medcv.tools.transform import med2rgb
from medcv.utils.colors import generate_rand_color

import cv2
is_cv3_version = cv2.__version__.startswith('3')


def image_with_mask(image, mask, alpha=0.5, colors=None, width=None, level=None):

    rgb_image = med2rgb(image, width=width, level=level)

    mask = np.squeeze(mask)
    if len(np.shape(mask)) != 2:
        raise ValueError('mask image should have rank 2, but received input shape: %s' % len(np.shape(mask)))

    mask_unique = np.unique(mask)
    mask_labels = mask_unique[np.nonzero(mask_unique)]
    if np.size(mask_labels) < 1:
        raise ValueError('mask must have nonzero label')

    colors = colors or generate_rand_color(n_color=np.size(mask_labels))

    for i, label in enumerate(mask_labels):
        for c in range(3):
            rgb_image[:, :, c] = np.where(mask == label, rgb_image[:, :, c] * (1 - alpha) + colors[i][c] * alpha, rgb_image[:, :, c])
    return rgb_image


def image_with_contours(image, mask, colors=None, thickness=1, width=None, level=None):

    rgb_image = med2rgb(image, width=width, level=level)

    mask = np.squeeze(mask)
    if len(np.shape(mask)) != 2:
        raise ValueError('mask image should have rank 2, but received input shape: %s' % len(np.shape(mask)))

    mask_unique = np.unique(mask)
    mask_labels = mask_unique[np.nonzero(mask_unique)]
    if np.size(mask_labels) < 1:
        raise ValueError('mask must have nonzero label')

    colors = colors or generate_rand_color(n_color=np.size(mask_labels))

    for i, label in enumerate(mask_labels):
        zero_mask = np.zeros_like(mask, dtype=np.uint8)
        zero_mask[mask == label] = 1
        if is_cv3_version:
            _, contours, _ = cv2.findContours(zero_mask, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
            rgb_image = cv2.drawContours(rgb_image, contours, contourIdx=-1, color=colors[i], thickness=thickness)
    return rgb_image

