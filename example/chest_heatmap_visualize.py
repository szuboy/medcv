# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from medcv.tools.transform import med2rgb
from medcv.data import chest_dcm, chest_heatmap
from medcv.visualize.cls import image_with_heatmap

# load chest dcm image and its heatmap
chest_dcm_image = chest_dcm()
chest_heatmap_image = chest_heatmap()

# dcm to rgb image with image window width and level
chest_rgb_image = med2rgb(chest_dcm_image, width=22135, level=12209)

# dcm with heatmap
chest_image_with_heatmap = image_with_heatmap(chest_dcm_image, chest_heatmap_image, width=22135, level=12209)

# plot visualize
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.title('origin image')
plt.imshow(np.squeeze(chest_dcm_image))
plt.subplot(1, 4, 2)
plt.title('rgb image')
plt.imshow(chest_rgb_image)
plt.subplot(1, 4, 3)
plt.title('heatmap image')
plt.imshow(chest_heatmap_image)
plt.subplot(1, 4, 4)
plt.title('chest with heatmap image')
plt.imshow(chest_image_with_heatmap)
plt.show()

