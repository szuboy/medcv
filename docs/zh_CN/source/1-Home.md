# MedCV:基于Python的医学可视化库

## 这就是MedCV
MedCV是一个高级医学图像可视化库，MedCV由纯Python编写而并基于[Numpy](https://github.com/numpy/numpy) 、[OpenCV](https://github.com/opencv/opencv-python) 完成图像的可视化，提供[PyQt5](https://pypi.org/project/PyQt5/) 可复用的控件。MedCV为解决OpenCV对医学图像兼容而生，能够把你的结果迅速可视化，如果你有如下需求，请选择MedCV：

- 简易和快速的医学可视化设计（MedCV具有高度模块函数接口，极简，和可扩充特性）
- 建立医学图像交互平台

MedCV兼容的Python版本：Python3+

## 设计原则

- **用户友好**：MedCV是为人类而不是外星人设计的API。用户的使用体验始终是我们考虑的首要和中心内容。MedCV遵循减少认知困难的最佳实践：MedCV提供一致而简洁的API，快速地完成可视化任务。
- **模块性**：具体而言，MedCV有可视化、工具类、GUI控件三个独立的模块，你可以使用它们来定制自己的可视化操作或者搭建交互平台。
- **与Python协作**：MedCV没有单独的模型配置文件类型，模型由Python代码描述，使其更紧凑和更易debug，并提供了扩展的便利性。

## 当前的版本与更新

本文档是MedCV的中文文档，包括MedCV的全部内容，以及更多的例子、解释和建议

由于作者水平和研究方向所限，无法对医学图像可视化操作都非常精通，因此MedCV代码和文档中不可避免的会出现各种错误、疏漏和不足之处。如果您在使用过程中有任何意见、建议和疑问，欢迎发送邮件到moyan_work@foxmail.com与我取得联系。

您对文档的任何贡献，包括文档的翻译、查缺补漏、概念解释、发现和修改问题、贡献示例程序等，均会被记录在致谢，十分感谢您对MedCV的贡献！

## 安装

在安装MedCV之前，请安装以下依赖：
- Numpy（用于图像矩阵的运算）
- OpenCV（兼容调用完成可视化）
- PyQt5（定制医学图像版本的设计控件）

然后你就可以安装MedCV本身了。用两种方法安装MedCV：

- **使用PyPI安装MedCV（推荐）**
```
sudo pip install medcv
```
如果你使用virtualenv虚拟环境，你可以避免使用sudo：
```
pip install medcv
```

- **或者：使用Github源码安装MedCV：**

首先，使用```git```来克隆MedCV：
```
git clone https://github.com/szuboy/medcv.git
```
然后，```cd```到MedCV目录并且运行安装命令：
```
cd medcv
sudo python setup.py install
```

## 技术支持
你可以在下列网址提问或加入MedCV开发讨论：

- MedCV Google group

- 你也可以在Github issues里提问或请求新特性（在提问之前请确保你阅读过我们的指导，我本人会经常为大家解答）

