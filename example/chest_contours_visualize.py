# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from medcv.tools.transform import med2rgb
from medcv.data import chest_dcm, chest_mask
from medcv.visualize.seg import image_with_contours

# load chest dcm image and its heatmap
chest_dcm_image = chest_dcm()
chest_mask_image = chest_mask()

# dcm to rgb image with image window width and level
chest_rgb_image = med2rgb(chest_dcm_image, width=22135, level=12209)

# ground truth
gt_mask = np.zeros_like(chest_mask_image)
gt_mask[np.logical_or(chest_mask_image == 1, chest_mask_image == 2)] = 1
chest_image_with_gt = image_with_contours(chest_dcm_image, gt_mask, thickness=10, width=22135, level=12209)
# model segmentation
seg_mask = np.zeros_like(chest_mask_image)
seg_mask[np.logical_or(chest_mask_image == 1, chest_mask_image == 3)] = 1
chest_image_with_seg = image_with_contours(chest_dcm_image, seg_mask, thickness=10, width=22135, level=12209)
# difference between ground truth and model segmentation
diff_mask = np.zeros_like(chest_mask_image)
diff_mask[np.logical_or(chest_mask_image == 2, chest_mask_image == 3)] = 1
chest_image_with_diff = image_with_contours(chest_dcm_image, diff_mask, thickness=10, width=22135, level=12209)

# plot visualize
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.title('chest rgb image')
plt.imshow(chest_rgb_image)
plt.subplot(1, 4, 2)
plt.title('ground truth')
plt.imshow(chest_image_with_gt)
plt.subplot(1, 4, 3)
plt.title('model segmentation')
plt.imshow(chest_image_with_seg)
plt.subplot(1, 4, 4)
plt.title('difference')
plt.imshow(chest_image_with_diff)
plt.show()
