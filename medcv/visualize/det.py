# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jeremy.zhang(szujeremy@gmail.com, Shenzhen University, China)


import numpy as np

from medcv.tools.transform import med2rgb
from medcv.utils.colors import generate_rand_color

import cv2


def image_with_bbox(image, bbox, bbox_ids=None, colors=None, thickness=1, width=None, level=None):

    rgb_image = med2rgb(image, width=width, level=level)

    if bbox_ids is not None and len(bbox_ids) != len(bbox):
        raise ValueError('bbox_ids should have same length as bbox')

    bbox_ids = bbox_ids or list(range(len(bbox)))
    colors = colors or generate_rand_color(n_color=np.max(bbox_ids)+1)

    for i, (x, y, w, h) in enumerate(bbox):
        rgb_image = cv2.rectangle(rgb_image, pt1=(x, y), pt2=(x+w, y+h), color=colors[bbox_ids[i]], thickness=thickness)
    return rgb_image

