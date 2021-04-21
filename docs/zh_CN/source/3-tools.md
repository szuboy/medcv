# 工具类函数

## 图像转换

### med2med
```
medcv.tools.med2med(med_image, width=None, level=None, dtype=np.float64, invert=False)
```
#### 参数
- **med_image** (np.ndarray)：医学图像，二维or三维都可
- **width** (int)：显示的窗宽，默认为```None```
- **level** (int)：显示的窗位，默认为```None```
- **dtype**：输出的数据类型，默认为```np.float64```
- **invert**：是否进行反色操作，即为倒序映射，默认为```False```

#### 使用实例


### med2grey
```
medcv.tools.med2grey(med_image, width=None, level=None)
```

#### 参数
- **med_image** (np.ndarray)：二维样式的医学图像
- **width** (int)：显示的窗宽，默认为```None```
- **level** (int)：显示的窗位，默认为```None```
- **invert**：是否进行反色操作，即为倒序映射，默认为```False```


#### 使用实例



### med2rgb
```
medcv.tools.med2rgb(med_image, width=None, level=None)
```

#### 参数
- **med_image** (np.ndarray)：二维样式的医学图像
- **width** (int)：显示的窗宽，默认为```None```
- **level** (int)：显示的窗位，默认为```None```
- **invert**：是否进行反色操作，即为倒序映射，默认为```False```


#### 使用实例






