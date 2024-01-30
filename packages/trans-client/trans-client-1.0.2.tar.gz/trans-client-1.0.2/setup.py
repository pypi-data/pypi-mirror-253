#! /usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='trans-client',
    version='1.0.2',
    py_modules=['tclient'],
    description='A data exchange script based on ssh',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='fetch150zy',
    author_email='zhewei@stu.xidian.edu.cn',
    license='MIT',
    entry_points={
        'console_scripts': [
            'tcl=tclient:main',
        ],
    },
    python_requires='>=3.8',
)
