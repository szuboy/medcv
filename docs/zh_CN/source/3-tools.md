# 工具类函数

## 图像转换

### med2med
```
medcv.tools.med2med(med_image, width=None, level=None, dtype=np.float64, invert=False)
```
该函数主要进行医学图像窗宽窗位的调节，返回调窗后的医学图像，支持二维或者三维的输入。

#### 参数
- **med_image** (np.ndarray)：医学图像，二维or三维都可
- **width** (int)：显示的窗宽，默认为```None```
- **level** (int)：显示的窗位，默认为```None```
- **dtype**：输出的数据类型，默认为```np.float64```
- **invert**：是否进行反色操作，即为倒序映射，默认为```False```

#### 使用实例
```
def med2rgb(med_image, width=None, level=None):
    med_image = np.squeeze(med_image)
    if len(np.shape(med_image)) != 2:
        raise ValueError('medical image should have rank 2, but received input shape: %s' % len(np.shape(med_image)))
    if width is None or level is None:
        min_value, max_value = np.min(med_image), np.max(med_image)
        width, level = int(max_value - min_value), int((max_value + min_value) / 2)
    offset, uint8_lut_array = generate_lut_array(med_image, width, level, y_min=0, y_max=255, dtype=np.uint8)
    grey_image = np.take(uint8_lut_array, med_image - offset)
    return np.dstack((grey_image, grey_image, grey_image))
```

### med2grey
```
medcv.tools.med2grey(med_image, width=None, level=None, invert=False)
```
该函数功能是将二维的医学图像转为灰度图，支持窗宽窗位设置，返回转换后的灰度图矩阵。

#### 参数
- **med_image** (np.ndarray)：二维样式的医学图像
- **width** (int)：显示的窗宽，默认为```None```
- **level** (int)：显示的窗位，默认为```None```
- **invert**：是否进行反色操作，即为倒序映射，默认为```False```


#### 使用实例
```
def med2rgb(med_image, width=None, level=None):
    med_image = np.squeeze(med_image)
    if len(np.shape(med_image)) != 2:
        raise ValueError('medical image should have rank 2, but received input shape: %s' % len(np.shape(med_image)))
    if width is None or level is None:
        min_value, max_value = np.min(med_image), np.max(med_image)
        width, level = int(max_value - min_value), int((max_value + min_value) / 2)
    offset, uint8_lut_array = generate_lut_array(med_image, width, level, y_min=0, y_max=255, dtype=np.uint8)
    grey_image = np.take(uint8_lut_array, med_image - offset)
    return np.dstack((grey_image, grey_image, grey_image))
```



### med2rgb
```
medcv.tools.med2rgb(med_image, width=None, level=None, invert=False)
```
该函数功能是将二维的医学图像转为rgb格式的自然图像，支持窗宽窗位设置，返回转换后的图像矩阵。

#### 参数
- **med_image** (np.ndarray)：二维样式的医学图像
- **width** (int)：显示的窗宽，默认为```None```
- **level** (int)：显示的窗位，默认为```None```
- **invert**：是否进行反色操作，即为倒序映射，默认为```False```


#### 使用实例
```
def med2rgb(med_image, width=None, level=None):
    med_image = np.squeeze(med_image)
    if len(np.shape(med_image)) != 2:
        raise ValueError('medical image should have rank 2, but received input shape: %s' % len(np.shape(med_image)))
    if width is None or level is None:
        min_value, max_value = np.min(med_image), np.max(med_image)
        width, level = int(max_value - min_value), int((max_value + min_value) / 2)
    offset, uint8_lut_array = generate_lut_array(med_image, width, level, y_min=0, y_max=255, dtype=np.uint8)
    grey_image = np.take(uint8_lut_array, med_image - offset)
    return np.dstack((grey_image, grey_image, grey_image))
```
