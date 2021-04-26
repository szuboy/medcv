# MedCV: OpenCV for Medical

## You have just found MedCV 
MedCV is an advanced medical image visualization library, which is written by [Numpy](https://github.com/numpy/numpy) and [OpenCV](https://github.com/opencv/opencv-python) to complete image visualization. MedCV was born to solve the compatibility between OpenCV and medical images. It would help you to quickly visualize your results. 

If you have the following requirements, please choose MedCV:

- Simple and fast medical visualization design (MedCV is highly modular, minimalist, and expandable)
- Establish a medical image interactive platform


## Guiding principles

- **Friendly**. MedCV is an API designed for humans. MedCV follows best practices for reducing cognitive difficulties: MedCV provides a consistent and concise API to quickly complete visualization tasks.
- **Modularity**. MedCV has three independent modules: visualize, tools, and GUI controls. You can use them to customize your own visualization operations or build an interactive platform. 
- **Work with Python**. No separate configuration files in a declarative format. Models are described in Python code, which is compact, easier to debug, and allows for ease of extensibility.


## Version and update

This document is the English document of MedCV, including all the contents of MedCV, as well as more examples, explanations and suggestions.
If you have any comments, suggestions or questions during the use process, please send email to moyan_work@foxmail.com to get in touch with me.

Any contribution you made to the document, including document translation, checking for deficiencies, conceptual explanations, finding and modifying problems, contributing sample programs, etc., will be recorded in the acknowledgment. Thank you very much for your contribution to MedCV!


## Installation
Before installing MedCV, please install the following requirements:
- Numpy (used for image matrix operations)
- OpenCV (Compatible call completion visualization)
- PyQt5 (design control for customized medical image version)

Install MedCV in two ways:

- **Use PyPI to install MedCV(recommended)**
```
sudo pip install medcv
```
If you use virtual environment, you can avoid using sudo:
```
pip install medcv
```

- **Or：use Github source code to install MedCV**

First, use```git```to clone MedCV:
```
git clone https://github.com/szuboy/medcv.git
```
Then, ```cd```to the MedCV directory and run the installation command:
```
cd medcv
sudo python setup.py install
```

## Support
You can ask questions or join the MedCV development discussion at the following URL:
- MedCV [Google group](https://groups.google.com/g/medcv)
- You can also ask questions or request new features in [Github issues](https://github.com/szuboy/medcv/issues) (please make sure you read our guide before asking questions, and I will answer it frequently for you)

