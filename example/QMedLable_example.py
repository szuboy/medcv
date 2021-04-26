# !/usr/bin/env python
# -*- coding:utf-8 -*-

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
