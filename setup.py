# !/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import setuptools
from setuptools import setup

with open('requirements.txt', 'r') as fp:
    requirements = list(filter(bool, (line.strip() for line in fp)))

with open('README.md', 'rb') as fp:
    long_description = fp.read().decode('utf-8')

package_data = ['%s/%s' % ('data', filename) for filename in os.listdir('medcv/data') if not filename.endswith('.py')]

setup(
    name='medcv',

    url='https://github.com/szuboy/medcv#readme',
    project_urls={
        'Documentation': 'https://medcv.readthedocs.io/en/latest/index.html',
        'Github': 'https://github.com/szuboy/medcv'
    },

    author='szuboy',
    author_email='medcv@googlegroups.com',

    version='1.0.0',

    packages=setuptools.find_packages(),

    package_data={'medcv': package_data},

    description='OpenCV for medical image',
    long_description=long_description,
    long_description_content_type="text/markdown",

    license='Apache License',

    keywords='OpenCV medical visualization',

    install_requires=requirements,

    python_requires='>=3.0'
)