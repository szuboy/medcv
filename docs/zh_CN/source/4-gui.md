# PyQt5控件

## QMedManger
```
medcv.gui.QMedManager()
```
医学图像管理者，用以管理医学图像信息以及的数据格式转换。该类同时也是其他GUI控件的内置管理者，完成医学图像与PyQt5的高效协作。

### API接口

#### 设置
- ```set_invert(invert)```：设置反色模式
- ```set_medical_image(medical_image)```：设置二维的医学图像
- ```set_image_window_width(window_width)```：设置图像窗宽
- ```set_image_window_level(window_level)```：设置图像窗位
- ```set_image_window(window_width, window_level)```：设置窗宽窗位

#### 获取
- ```is_invert()```：是否为反色模式
- ```get_medical_image()```：获取二维的医学图像
- ```get_image_window_width()```：获取图像窗宽
- ```get_image_window_level()```：获取图像窗位
- ```get_image_window()```：获取窗宽窗位


#### 其他
- ```pixmap()```：返回```pixmap```的格式图像
- ```update_lut_array()```：更新映射的LUT

### 使用示例
```
使用示例
```

## QMedLabel
```
medcv.gui.QMedLabel()
```
该类继承于PyQt5的```QLabel```类，封装为医学图像的显示面板，可快速完成医学图像的显示。

<div class="admonition note">
    <p class="first admonition-title">注意</p>
    <p class="last">继承控件的代码风格不是Python的PEP8，而是遵照Qt的CamelCase格式</p>
</div>

### API接口

#### 设置
- ```setInvert(invert)```：设置反色模式
- ```setMedicalImage(medicalImage)```：设置二维的医学图像
- ```setImageWindowWidth(windowWidth)```：设置图像窗宽
- ```setImageWindowLevel(windowLevel)```：设置图像窗位
- ```setImageWindow(windowWidth, windowLevel)```：设置窗宽窗位

#### 获取
- ```isInvert()```：是否为反色模式
- ```getMedicalImage()```：获取二维的医学图像
- ```getImageWindowWidth()```：获取图像窗宽
- ```getImageWindowLevel()```：获取图像窗位
- ```getImageWindow()```：获取窗宽窗位

### 使用示例
```
使用示例
```

