#!/usr/bin/env python3

from setuptools import setup

setup (name = 'unrival',
       version = '1.0',
       packages = ['unrival'],
       entry_points = {
           'console_scripts' : [
               'unrival = unrival.cli:main'
           ]
       })
