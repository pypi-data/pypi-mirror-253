#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : nickdecodes
@Email   : nickdecodes@163.com
@Usage   :
@FileName: setup.py
@DateTime: 2024/1/28 18:50
@SoftWare: 
"""

from setuptools import setup, find_packages

setup(
    name='python-lottery',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'selenium>=4.11.2',
        'webdriver_manager>=4.0.0',
        'pandas>=2.0.3',
        'numpy>=1.24.3',
        'statsmodels>=0.14.0',
        'Pillow>=9.5.0',
        'scikit-learn>=1.3.2',
        'pmdarima>=2.0.4',
        'twine'
    ],
)
