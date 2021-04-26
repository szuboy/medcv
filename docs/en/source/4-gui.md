# MedQt API

## QMedManger
```
medcv.gui.QMedManager()
```
Medical image manager, used to manage medical image information and data format conversion. This class is also the built-in manager of other GUI controls, completing the efficient collaboration between medical images and PyQt5.


### API

#### set
- ```set_invert(invert)```: sets invert mode to the invert parameter
- ```set_medical_image(medical_image)```: sets medical image
- ```set_image_window_width(window_width)```: sets medical image window width
- ```set_image_window_level(window_level)```: sets medical image window level
- ```set_image_window(window_width, window_level)```: sets medical image window

#### get
- ```is_invert()```: gets invert mode
- ```get_medical_image()```: gets medical image
- ```get_image_window_width()```: gets medical image window width
- ```get_image_window_level()```: gets medical image window level
- ```get_image_window()```: gets medical image window of the manager


#### other
- ```pixmap()```: return```pixmap``` format image
- ```update_lut_array()```: update mapping lookup table


## QMedLabel
```
medcv.gui.QMedLabel()
```
This class inherits from the ```QLabel``` class of PyQt5, and is encapsulated as a display panel for medical images, which can quickly complete the display of medical images.

<div class="admonition note">
    <p class="first admonition-title">Note</p>
    <p class="last">The code style of the inherited control is not Python's PEP8, but follows the Qt's CamelCase format</p>
</div>

### API

#### set
- ```setInvert(invert)```: sets invert mode to the invert parameter
- ```setMedicalImage(medicalImage)```: sets medical image
- ```setImageWindowWidth(windowWidth)```: sets medical image window width
- ```setImageWindowLevel(windowLevel)```: sets medical image window level
- ```setImageWindow(windowWidth, windowLevel)```: sets medical image window

#### get
- ```isInvert()```: gets invert mode
- ```getMedicalImage()```: gets medical image
- ```getImageWindowWidth()```: gets medical image window width
- ```getImageWindowLevel()```: gets medical image window level
- ```getImageWindow()```: gets medical image window of the manager

### Usage
```
import sys
from medcv.gui import QMedLabel
from medcv.data import chest_dcm
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider


application = QApplication(sys.argv)

main_widget = QWidget()
layout = QVBoxLayout(main_widget)

med_label = QMedLabel()
med_label.setMaximumSize(600, 600)
med_label.setScaledContents(True)
med_label.setMedicalImage(chest_dcm())


width_slider = QSlider(Qt.Horizontal)
level_slider = QSlider(Qt.Horizontal)
width_slider.setRange(1, 50000)
width_slider.valueChanged.connect(med_label.setImageWindowWidth)
level_slider.setRange(0, 50000)
level_slider.valueChanged.connect(med_label.setImageWindowLevel)

layout.addWidget(med_label)
layout.addWidget(width_slider)
layout.addWidget(level_slider)

main_widget.show()

sys.exit(application.exec_())
```
