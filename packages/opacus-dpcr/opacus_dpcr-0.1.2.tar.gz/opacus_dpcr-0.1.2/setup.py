#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Cai Jianping
# Mail: jpingcai@163.com
# Created Time:  2022-11-22 11:25:34 PM
#############################################


from setuptools import setup, find_packages

setup(
    name = "opacus_dpcr",
    version = "0.1.2",
    keywords = ("opacus","dpcr","DPLearning"),
    description = "Opacus-DPCR extended by Opacus, Using DPCR to obtain better accuracy...",
    long_description = "We extend Opacus for private learning and design a new framework Opacus-DPCR to support private learning with differential privacy continuous data release (DPCR). Opacus-DPCR integrates various DPCR models and keeps high compatibility with the original Opacus framework.",
    license = "MIT Licence",

    url = "https://github.com/imcjp/Opacus-DPCR",
    author = "Cai Jianping",
    author_email = "jpingcai@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['dpcrpy','torch','opacus==1.1.2']
)
