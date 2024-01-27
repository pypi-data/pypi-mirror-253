#!/usr/bin/env python
# coding: utf-8
from setuptools import setup
from setuptools import find_packages

VERSION = '0.1.2'

setup(
    name='cc-notion',  # package name
    version=VERSION,  # package version
    description='my notion package',  # package description
    packages=find_packages(),
    url="https://github.com/houm01/cc-notion",
    zip_safe=False,
)

