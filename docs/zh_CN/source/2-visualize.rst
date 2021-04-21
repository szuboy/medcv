===========
可视化接口
===========

图像分类
==========

image_with_heatmap
---------------------
.. code-block:: python

    medcv.visualize.cls.image_with_heatmap(image, heatmap, alpha=0.8, beta=0.3, colormap=cv2.COLORMAP_JET, width=None, level=None)

将关注热图在原图上进行可视化，例如：深度学习分类网络的Grad-CAM热图叠加在医学图像上进行可视化。

本函数内部采用 ``cv2.addWdighted`` 函数实现，是一种图像融合方法，但对图像赋予不同的权重，以使其具有融合或透明的效果。根据以下等式进行融合：

.. math::
    dst = \alpha \cdot image + \beta \cdot heatmap + \gamma

参数
^^^^^^
- **image** (np.ndarray)：二维样式的医学图像原图
- **heatmap** (np.ndarray)：``image`` 对应的热图矩阵
- **alpha** (float)： ``image`` 对应的权重，取值范围为 ``0 ~ 1`` ，默认为 ``0.8``
- **beta** (float)： ``heatmap`` 对应的权重，取值范围为 ``0 ~ 1`` ，默认为 ``0.3``
- **colormap**：颜色图类型，默认为 ``cv2.COLORMAP_JET`` ，详情参考 `此文档 <https://docs.opencv.org/master/d3/d50/group__imgproc__colormap.html>`_
- **width** (int)：显示的窗宽，默认为 ``None``
- **level** (int)：显示的窗位，默认为 ``None``

使用示例
^^^^^^^^

.. code-block:: python

    import os
    # 选择使用0号卡
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'

    from paddlex.det import transforms
    import paddlex as pdx


可视化
^^^^^^^^
详细信息显示


目标检测
==========

image_with_bbox
---------------------
.. code-block:: python

    medcv.visualize.det.imag_with_bbox(image, bbox, bbox_ids=None, colors=None, thickness=1, width=None, level=None)

将目标检测框在原图上进行可视化，通过指定 ``bbox_ids`` 参数支持多个不同对象框的可视化

参数
^^^^^^
- **image** (np.ndarray)：二维样式的医学图像原图
- **bbox** (list)：检测框列表，形式为 ``[(x, y, w, h), (x, y, w, h), ...]``
- **bbox_ids** (list)：检测框的id列表，每个检测框对应一个id，以区分不同的对象，默认为 ``None`` ，即每个检测框对应不同的对象
- **colors** (list)：不同id对应rgb颜色列表，形式为 ``[(r, g, b), (r, g, b), ...]``
- **thickness** (int)：边框的像素大小
- **width** (int)：显示的窗宽，默认为 ``None``
- **level** (int)：显示的窗位，默认为 ``None``

使用示例
^^^^^^^^

.. code-block:: python

    import os
    # 选择使用0号卡
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'

    from paddlex.det import transforms
    import paddlex as pdx


可视化
^^^^^^^^
详细信息显示




实例分割
==========

imag_with_mask
---------------------
.. code-block:: python

    medcv.visualize.seg.imag_with_mask(image, mask, alpha=0.5, colors=None, width=None, level=None)

将标注的Mask在原图上进行可视化，例如：对比分割结果与金标准的重叠程度的可视化。


参数
^^^^^^
- **image** (np.ndarray)：二维样式的医学图像原图
- **mask** (np.ndarray)：``image`` 对应的mask，默认0为背景，非零值为ROI
- **alpha** (float)： ``mask`` 对应的加权值，取值范围为 ``0 ~ 1`` ，默认为 ``0.5``
- **colors** (list)：不同ROI对应rgb颜色列表，按照ROI的标注值进行升序索引，形式为 ``[(r, g, b), (r, g, b), ...]``
- **width** (int)：显示的窗宽，默认为 ``None``
- **level** (int)：显示的窗位，默认为 ``None``

使用示例
^^^^^^^^

.. code-block:: python

    import os
    # 选择使用0号卡
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'

    from paddlex.det import transforms
    import paddlex as pdx


可视化
^^^^^^^^
详细信息显示



image_with_contours
---------------------
.. code-block:: python

    medcv.visualize.seg.image_with_contours(image, mask, colors=None, thickness=1, width=None, level=None)

本函数内部采用 ``cv2.drawContours`` 函数实现，将标注的Mask的边缘轮廓在原图上进行可视化，例如：对比分割结果与金标准的边缘信息的可视化。


参数
^^^^^^
- **image** (np.ndarray)：二维样式的医学图像原图
- **mask** (np.ndarray)：``image`` 对应的mask，默认0为背景，非零值为ROI
- **colors** (list)：不同ROI对应rgb颜色列表，按照ROI的标注值进行升序索引，形式为 ``[(r, g, b), (r, g, b), ...]``
- **thickness** (int)：边缘轮廓线的像素大小
- **width** (int)：显示的窗宽，默认为 ``None``
- **level** (int)：显示的窗位，默认为 ``None``

使用示例
^^^^^^^^

.. code-block:: python

    import os
    # 选择使用0号卡
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'

    from paddlex.det import transforms
    import paddlex as pdx


可视化
^^^^^^^^
详细信息显示
