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
    name='depscanner',
    version='0.1',
    keywords=['depscanner', 'python', 'dependency'],
    packages=find_packages(),
    author="nickdecodes",
    author_email="nickdecodes@163.com",
    description="Python Dependency Scanner",
    python_requires=">=3.6",
    install_requires=[
        'stdlib_list',
        'twine'
    ],
)
