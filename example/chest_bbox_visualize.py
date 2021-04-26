# !/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
from medcv.tools.transform import med2rgb
from medcv.data import chest_dcm, chest_bbox
from medcv.visualize.det import image_with_bbox

# load chest dcm image and its heatmap
chest_dcm_image = chest_dcm()
chest_bbox_dict = chest_bbox()

# bbox list, because chest_bbox_dict has left-lung and right-lung bbox
bbox_list = chest_bbox_dict.values()

# dcm to rgb image with image window width and level
chest_rgb_image = med2rgb(chest_dcm_image, width=22135, level=12209)

# dcm with bbox, default is different bbox id
chest_image_with_bbox = image_with_bbox(chest_dcm_image, bbox_list, width=22135, level=12209, thickness=10)

# dcm with bbox with thickness=20
chest_image_with_bold_bbox = image_with_bbox(chest_dcm_image, bbox_list, width=22135, level=12209, thickness=20)

# dcm with same bbox id
chest_image_with_same_bbox = image_with_bbox(chest_dcm_image, bbox_list, bbox_ids=[0, 0], width=22135, level=12209, thickness=10)

# plot visualize
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.title('chest rgb image')
plt.imshow(chest_rgb_image)
plt.subplot(1, 4, 2)
plt.title('bbox image')
plt.imshow(chest_image_with_bbox)
plt.subplot(1, 4, 3)
plt.title('bold thickness')
plt.imshow(chest_image_with_bold_bbox)
plt.subplot(1, 4, 4)
plt.title('same bbox id')
plt.imshow(chest_image_with_same_bbox)
plt.show()

