===========
可视化接口
===========

图像分类
==========

image_with_heatmap
---------------------
.. code-block:: python

    medcv.visualize.cls.image_with_heatmap(image, heatmap, alpha=0.8, beta=0.3, colormap=cv2.COLORMAP_JET, width=None, level=None):

将关注热图在原图上进行可视化，例如：深度学习分类网络的Grad-CAM热图叠加在医学图像上进行可视化。

本函数内部采用 ``cv2.addWdighted`` 函数实现，是一种图像融合方法，但对图像赋予不同的权重，以使其具有融合或透明的效果。根据以下等式进行融合：

.. math::
    dst = \alpha \cdot image + \beta \cdot heatmap + \gamma

参数
^^^^^^
- **image** (np.ndarray)：二维样式的医学图像原图
- **heatmap** (np.ndarray)：``image`` 对应的关注热图
- **alpha** (float)：，默认0.8
- **beta** (float)：，默认0.3
- **colormap**：，默认COLORMAP_JET
- **width** (int)：
- **level** (int)：

使用示例
^^^^^^^^

.. code-block:: python

    import os
    # 选择使用0号卡
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'

    from paddlex.det import transforms
    import paddlex as pdx

    model = pdx.load_model('insect_epoch_270')
    eval_dataset = pdx.datasets.VOCDetection(
        data_dir='insect_det',
        file_list='insect_det/val_list.txt',
        label_list='insect_det/labels.txt',
        transforms=model.eval_transforms)
    metrics, evaluate_details = model.evaluate(eval_dataset, batch_size=8, return_details=True)
    gt = evaluate_details['gt']
    bbox = evaluate_details['bbox']
    pdx.det.draw_pr_curve(gt=gt, pred_bbox=bbox, save_dir='./insect')



目标检测
==========
目标检测可视化


实例分割
==========
实例分割
