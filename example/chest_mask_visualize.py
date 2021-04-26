# !/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
from medcv.tools.transform import med2rgb
from medcv.data import chest_dcm, chest_mask
from medcv.visualize.seg import image_with_mask

# load chest dcm image and its heatmap
chest_dcm_image = chest_dcm()
chest_mask_image = chest_mask()

# dcm to rgb image with image window width and level
chest_rgb_image = med2rgb(chest_dcm_image, width=22135, level=12209)

# visualize colors
colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255)]

# alpha=0.2
chest_image_with_mask1 = image_with_mask(chest_dcm_image, chest_mask_image, colors=colors, alpha=0.2, width=22135, level=12209)
# alpha=0.5 (default alpha=0.5)
chest_image_with_mask2 = image_with_mask(chest_dcm_image, chest_mask_image, colors=colors, alpha=0.5, width=22135, level=12209)
# alpha=0.8
chest_image_with_mask3 = image_with_mask(chest_dcm_image, chest_mask_image, colors=colors, alpha=0.8, width=22135, level=12209)

# plot visualize
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.title('chest rgb image')
plt.imshow(chest_rgb_image)
plt.subplot(1, 4, 2)
plt.title('alpha=0.2')
plt.imshow(chest_image_with_mask1)
plt.subplot(1, 4, 3)
plt.title('alpha=0.5')
plt.imshow(chest_image_with_mask2)
plt.subplot(1, 4, 4)
plt.title('alpha=0.8')
plt.imshow(chest_image_with_mask3)
plt.show()
