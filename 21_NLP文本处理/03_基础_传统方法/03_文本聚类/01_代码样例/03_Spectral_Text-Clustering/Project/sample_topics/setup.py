# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:35:33 2019

@author: lenovo
"""
# 使用Anaconda Prompt
# cd至当前文件夹
# python setup.py build_ext --inplace

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
 
ext_modules=[
   Extension("sample",sources=["sample.pyx",'gamma.c'])
]
 
setup(
   name = "sample",
   ext_modules = cythonize(ext_modules)
)