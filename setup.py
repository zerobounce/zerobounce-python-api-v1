#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup


with open('requirements.txt') as fp:
    reqs = fp.read()

setup(
    name='zerobounce',
    version='0.1',
    description='ZeroBounce Python API - https://www.zerobounce.net.',
    author='<Author>',
    author_email='<author email>',
    url='http://github.com/zerobounce/zerobounce-python-api',
    install_requires=reqs,
    packages=[
        'zerobounce',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
