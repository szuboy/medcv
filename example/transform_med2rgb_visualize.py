# !/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
from medcv.data import chest_dcm
from medcv.tools.transform import med2rgb

# load chest dcm image
chest_dcm_image = chest_dcm()

# width=50000, level=20000
rgb_image1 = med2rgb(chest_dcm_image, width=50000, level=20000)

# width=20000, level=15000
rgb_image2 = med2rgb(chest_dcm_image, width=20000, level=15000)

# width=20000, level=15000, invert=True
rgb_image3 = med2rgb(chest_dcm_image, width=20000, level=15000, invert=True)

# plot visualize
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.title('chest origin image')
plt.imshow(med2rgb(chest_dcm_image))
plt.subplot(1, 4, 2)
plt.title('width=70000,level=20000')
plt.imshow(rgb_image1)
plt.subplot(1, 4, 3)
plt.title('width=20000,level=15000')
plt.imshow(rgb_image2)
plt.subplot(1, 4, 4)
plt.title('invert=True')
plt.imshow(rgb_image3)
plt.show()
