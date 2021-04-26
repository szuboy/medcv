# Tools API

## Transform
Image transform is to map the medical image to output format by establishing a corresponding lookup table(LUT), which can be used to adjust the medical image window and convert the medical image to the natural image format (mapping between 0-255) and other scenes.

### med2med
```
medcv.tools.med2med(med_image, width=None, level=None, dtype=np.float64, invert=False)
```
This function is mainly used to efficiently adjust image window, return the medical image after window adjustment, and support two-dimensional or three-dimensional input.


#### Parameter
- **med_image** (np.ndarray): medical image, support 2-dim or 3-dim
- **width** (int): window width for image, default is ``None``, which is ``width=max(image)-min(image))``
- **level** (int): window level for image, default is ``None``, which is ``level=((image)+min(image))/2``
- **dtype**: output's data type, default is ```np.float64```
- **invert**: whether to reverse mapping, default is ```False```


#### Usage
```
import matplotlib.pyplot as plt
from medcv.data import chest_dcm
from medcv.tools.transform import med2med, med2rgb

# load chest dcm image
chest_dcm_image = chest_dcm()

# width=50000, level=20000
adjust_image1 = med2med(chest_dcm_image, width=50000, level=20000)

# width=20000, level=15000
adjust_image2 = med2med(chest_dcm_image, width=20000, level=15000)

# width=20000, level=15000, invert=True
adjust_image3 = med2med(chest_dcm_image, width=20000, level=15000, invert=True)

# plot visualize
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.title('chest origin image')
plt.imshow(med2rgb(chest_dcm_image))
plt.subplot(1, 4, 2)
plt.title('width=70000,level=20000')
plt.imshow(med2rgb(adjust_image1))
plt.subplot(1, 4, 3)
plt.title('width=20000,level=15000')
plt.imshow(med2rgb(adjust_image2))
plt.subplot(1, 4, 4)
plt.title('invert=True')
plt.imshow(med2rgb(adjust_image3))
plt.show()

```

#### Result
![](/_static/med2med_visualize.png)



### med2grey
```
medcv.tools.med2grey(med_image, width=None, level=None, invert=False)
```
The function is to convert a two-dimensional medical image into a grayscale image, which supports window adjust and returns the converted grayscale image to be compatible with the OpenCV input format.

#### Parameter
- **med_image** (np.ndarray): medical image with 2-dim
- **width** (int): window width for image, default is ``None``, which is ``width=max(image)-min(image))``
- **level** (int): window level for image, default is ``None``, which is ``level=((image)+min(image))/2``
- **invert**: whether to reverse mapping, default is ```False```

#### Usage
```
import matplotlib.pyplot as plt
from medcv.data import chest_dcm
from medcv.tools.transform import med2grey

# load chest dcm image
chest_dcm_image = chest_dcm()

# width=50000, level=20000
grey_image1 = med2grey(chest_dcm_image, width=50000, level=20000)

# width=20000, level=15000
grey_image2 = med2grey(chest_dcm_image, width=20000, level=15000)

# width=20000, level=15000, invert=True
grey_image3 = med2grey(chest_dcm_image, width=20000, level=15000, invert=True)

# plot visualize
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.title('chest origin image')
plt.imshow(med2grey(chest_dcm_image), cmap='gray')
plt.subplot(1, 4, 2)
plt.title('width=70000,level=20000')
plt.imshow(grey_image1, cmap='gray')
plt.subplot(1, 4, 3)
plt.title('width=20000,level=15000')
plt.imshow(grey_image2, cmap='gray')
plt.subplot(1, 4, 4)
plt.title('invert=True')
plt.imshow(grey_image3, cmap='gray')
plt.show()

```

#### Result
![](/_static/med2med_visualize.png)



### med2rgb
```
medcv.tools.med2rgb(med_image, width=None, level=None, invert=False)
```

The function is to convert a two-dimensional medical image into a rgb image, which supports window adjust and returns the converted rgb image to be compatible with the OpenCV input format.


#### Parameter
- **med_image** (np.ndarray): medical image with 2-dim
- **width** (int): window width for image, default is ``None``, which is ``width=max(image)-min(image))``
- **level** (int): window level for image, default is ``None``, which is ``level=((image)+min(image))/2``
- **invert**: whether to reverse mapping, default is ```False```


#### Usage
```
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
```

#### Result
![](/_static/med2med_visualize.png)

