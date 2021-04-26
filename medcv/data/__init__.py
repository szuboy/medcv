# !/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import cv2
import json
import SimpleITK as sitk

data_dir = os.path.abspath(os.path.dirname(__file__))


def chest_dcm():
    sitk_image = sitk.ReadImage(os.path.join(data_dir, 'chest.dcm'))
    return sitk.GetArrayFromImage(sitk_image)


def chest_heatmap():
    return cv2.imread(os.path.join(data_dir, 'heatmap.jpg'))


def chest_bbox():
    with open(os.path.join(data_dir, 'lung_bbox.json'), mode='r') as f:
        bbox = json.load(f)
    return bbox


def chest_mask():
    sitk_image = sitk.ReadImage(os.path.join(data_dir, 'lung_mask.nii.gz'))
    return sitk.GetArrayFromImage(sitk_image)

