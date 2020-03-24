#!/usr/bin/env python

import glob
from distutils.core import setup

setup(name='pandamia',
      version='1.0',
      description='Python COVID-19 analysis framework',
      author='Gonzalo Figueroa',
      author_email='gfigue@gmail.com',
      url='https://github.com/ph1t0/covid19.git',
      packages=['covid19'],
      scripts=glob.glob("apps/*"),
      install_requires=['pandas', 'matplotlib', 'ipython', 'sh'],
     )
