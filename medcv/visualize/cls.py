# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jeremy.zhang(szujeremy@gmail.com, Shenzhen University, China)

import cv2
import numpy as np

from medcv.tools.transform import med2rgb


def image_with_heatmap(image, heatmap, alpha=0.8, beta=0.3, colormap=cv2.COLORMAP_JET, width=None, level=None):
    rgb_image = med2rgb(image, width=width, level=level)
    uint8_heatmap = np.uint8((heatmap - np.min(heatmap)) / (np.max(heatmap) - np.min(heatmap) + 1e-5) * 255)
    color_heatmap = cv2.applyColorMap(src=uint8_heatmap, colormap=colormap)
    return cv2.addWeighted(src1=rgb_image, alpha=alpha, src2=color_heatmap, beta=beta, gamma=0)

