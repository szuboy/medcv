# Utils API

## LUT
Lookup Table(LUT) is an array that replaces complex operations by indexing, and converts input data into a more ideal output format, thereby saving a lot of processing time. Especially in the interactive interface, the fluency of the interaction directly determines the user's experience.

For the processing of medical images(always with a three-dimensional format), the image window adjustment and image format conversion are completed efficiently by establishing of LUT, which provide a guarantee for the smoothness of the interaction of the GUI controls.

### Mapping function
Medical images usually have a high dynamic range (for example, the dynamic range of CT is generally -1024~1024), and the image display can be completed through the mapping function. According to [DICOM](https://dicom.innolitics.com/ciods/ct-image/voi-lut/00281056)
, three mapping functions are defined: ```LINEAR```、```LINEAR_EXACT```、```SIGMOID```(MedCV uses```LINEAR```by default). Each function is related to dual variables of window level and window width, please refer to the [code](https://github.com/szuboy/medcv/blob/master/medcv/utils/lut_fn.py) for details.


### LUT building
```
medcv.utils.generate_lut_array(image, width, center, y_min=0, y_max=255, dtype=np.uint8, invert=False, mode=medcv.LINEAR_MODE)
```
This function generates the LUT array based on the incoming image data, and the return value is: ```offset``` and ```lut_array```, please refer to the [code](https://github.com/szuboy/medcv/blob/master/medcv/utils/lut.py) for details.

#### Parameter
- **image** (np.ndarray): medical image array, support 2-dim and 3-dim
- **width** (int): window width for medical image
- **center** (int): window center(level) for medical image
- **y_min** (number): minimum value corresponding to the mapping function, the default is ```0```
- **y_max** (number): maximum value corresponding to the mapping function, the default is ```255```
- **dtype**: ```lut_array``` data type, default is ```np.uint8```
- **invert** (bool): reverse mapping mode, default is ```False```
- **mode**：mapping function selection, the options are:```LINEAR```、```LINEAR_EXACT``` and ```SIGMOID```, default is ```LINEAR```


<div class="admonition warning">
<p class="first admonition-title">Warning</p>
<p class="last">window width parameter must be set to be greater than or equal to 1</p>
</div>


## Argument validate
```
medcv.utils.expected_type(*type_args, **type_kwargs)
```
Based on the Python closure and decorator, combined with the ```inspect``` library ```signature``` method, the inspection and verification of the function parameter types are elegantly and concisely completed, please refer to the [code](https://github.com/szuboy/medcv/blob/master/medcv/utils/arg_support.py) for details.

