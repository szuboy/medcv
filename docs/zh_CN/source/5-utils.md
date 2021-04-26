# Utils基础类

## LUT
查找表（Lookup Table, LUT）是一个数组，通过索引LUT取代复杂的操作，将输入数据转化为更理想的输出格式，从而节省大量的处理时间。尤其是在交互界面时，交互的流畅性直接决定着用户的使用体验。

针对医学图像的处理，常见的大小为512×512，更有是三维的图像格式。通过建立LUT，高效地完成图像调窗操作，以及图像格式的转换，为GUI控件的交互的流畅性提供了保障。

### 映射函数
医学图像通常有很高的动态范围（比如：CT的动态范围一般为-1024~1024），可以通过映射函数以完成图像的显示。依据[DICOM协议](https://dicom.innolitics.com/ciods/ct-image/voi-lut/00281056)
中，主要定义了三个映射函数：```LINEAR```、```LINEAR_EXACT```、```SIGMOID```（MedCV内部默认使用```LINEAR```），每个函数都与窗口中心（窗位）和窗口宽度（窗宽）双变量相关，具体请参考[源码](https://github.com/szuboy/medcv/blob/master/medcv/utils/lut_fn.py)


### LUT建立
```
medcv.utils.generate_lut_array(image, width, center, y_min=0, y_max=255, dtype=np.uint8, invert=False, mode=medcv.LINEAR_MODE)
```
该函数根据传入的图像数据生成对应的LUT，返回值为：```offset```和```lut_array```，具体请参考[源码](https://github.com/szuboy/medcv/blob/master/medcv/utils/lut.py)

#### 参数
- **image** (np.ndarray)：医学图像格式，支持二维or三维输入
- **width** (int)：图像窗宽
- **center** (int)：图像窗位
- **y_min** (number)：映射函数对应的最小值，默认为```0```
- **y_max** (number)：映射函数对应的最大值，默认为```255```
- **dtype**：```lut_array```数据类型，默认为```np.uint8```
- **invert** (bool)：是否为反色模式，默认为```False```
- **mode**：映射函数选择，可选```LINEAR```、```LINEAR_EXACT```和```SIGMOID```，默认为```LINEAR```


<div class="admonition warning">
<p class="first admonition-title">警告</p>
<p class="last">窗宽参数（width）必须设置为大于或等于1</p>
</div>


## 参数校验
```
medcv.utils.expected_type(*type_args, **type_kwargs)
```
基于Python函数闭包特性和装饰器机制，结合```inspect```库```signature```方法，优雅且简洁地完成函数形参类型的检查与校验，具体请参考[源码](https://github.com/szuboy/medcv/blob/master/medcv/utils/arg_support.py)

