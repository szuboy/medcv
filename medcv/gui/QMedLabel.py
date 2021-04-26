# !/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
from PyQt5.QtWidgets import QLabel

from medcv.gui.QMedManger import QMedManager
from medcv.utils.arg_support import expected_type


class QMedLabel(QLabel):
    def __init__(self, *args):
        super(QMedLabel, self).__init__(*args)

        self.image_manager = QMedManager()

    def lutImage(self) -> np.ndarray:
        if not self.image_manager:
            raise AttributeError('medical image must be initialized before lutImage() method called')
        return self.image_manager.lut_image()

    @expected_type(medicalImage=np.ndarray)
    def setMedicalImage(self, medicalImage):
        self.image_manager.set_medical_image(medicalImage)
        self.setPixmap(self.image_manager.pixmap())

    def getMedicalImage(self) -> np.ndarray:
        return self.image_manager.get_medical_image()

    @expected_type(windowLevel=int)
    def setImageWindowLevel(self, windowLevel: int):
        if not self.image_manager:
            raise AttributeError('medical image must be initialized before setImageWindowLevel() method called')
        self.image_manager.set_image_window_level(windowLevel)
        self.setPixmap(self.image_manager.pixmap())

    def getImageWindowLevel(self) -> int:
        return self.image_manager.get_image_window_level()

    @expected_type(windowWidth=int)
    def setImageWindowWidth(self, windowWidth: int):
        if not self.image_manager:
            raise AttributeError('medical image must be initialized before setImageWindowWidth() method called')
        self.image_manager.set_image_window_width(windowWidth)
        self.setPixmap(self.image_manager.pixmap())

    def getImageWindowWidth(self) -> int:
        return self.image_manager.get_image_window_width()

    @expected_type(windowWidth=int, windowLevel=int)
    def setImageWindow(self, windowWidth: int, windowLevel: int):
        if not self.image_manager:
            raise AttributeError('medical image must be initialized before setImageWindow() method called')
        self.image_manager.set_image_window(windowWidth, windowLevel)
        self.setPixmap(self.image_manager.pixmap())

    def getImageWindow(self) -> (int, int):
        return self.image_manager.get_image_window()

