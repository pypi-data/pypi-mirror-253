#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


VERSION = '0.0.6'

setup(
    name='cc-dida365',  # package name
    version=VERSION,  # package version
    description='my dida package',  # package description
    packages=find_packages(),
    url="https://github.com/houm01/cc-dida365",
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown'
)

