# 工具类函数

## 图像转换
图像转换是通过建立相应的LUT，将医学图像原图映射到一个理想的输出格式，可用于医学图像窗宽窗位的调节、医学图像转自然图像格式（映射到0 - 255之间）等场景。

### med2med
```
medcv.tools.med2med(med_image, width=None, level=None, dtype=np.float64, invert=False)
```
该函数主要用于进行高效地医学图像窗宽窗位的调节，返回调窗后的医学图像，支持二维或者三维的输入。

#### 参数
- **med_image** (np.ndarray)：医学图像，二维or三维都可
- **width** (int)：显示的窗宽，默认为```None```，则```width=max(image)-min(image)```
- **level** (int)：显示的窗位，默认为```None```，则```level=(max(image)+min(image))/2```
- **dtype**：输出的数据类型，默认为```np.float64```
- **invert**：是否进行反色操作，即为倒序映射，默认为```False```

#### 使用实例
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

#### 可视化
![](/_static/med2med_visualize.png)



### med2grey
```
medcv.tools.med2grey(med_image, width=None, level=None, invert=False)
```
该函数功能是将二维的医学图像转为灰度图，支持窗宽窗位设置，返回转换后的灰度图，以此来兼容OpenCV的输入格式。

#### 参数
- **med_image** (np.ndarray)：二维样式的医学图像
- **width** (int)：显示的窗宽，默认为```None```，则```width=max(image)-min(image)```
- **level** (int)：显示的窗位，默认为```None```，则```level=(max(image)+min(image))/2```
- **invert**：是否进行反色操作，即为倒序映射，默认为```False```


#### 使用实例
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

#### 可视化
![](/_static/med2med_visualize.png)



### med2rgb
```
medcv.tools.med2rgb(med_image, width=None, level=None, invert=False)
```
该函数功能是将二维的医学图像转为rgb格式的自然图像，支持窗宽窗位设置，返回转换后的RGB图像，以此来兼容OpenCV的输入格式。

#### 参数
- **med_image** (np.ndarray)：二维样式的医学图像
- **width** (int)：显示的窗宽，默认为```None```，则```width=max(image)-min(image)```
- **level** (int)：显示的窗位，默认为```None```，则```level=(max(image)+min(image))/2```
- **invert**：是否进行反色操作，即为倒序映射，默认为```False```


#### 使用实例
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

#### 可视化
![](/_static/med2med_visualize.png)

