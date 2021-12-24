#!/usr/bin/env python

from distutils.core import setup

setup(name='convexvalue',
      version='1.0',
      description='Python API wrapper library for Convex Value API',
      author='@aaronsdevera',
      author_email='aaronsdevera@protonmail.com',
      url='https://github.com/aaronsdevera/convex-value-python',
      packages=['convexvalue'],
      install_requires=['distutils', 'distutils.command','requests','urllib','urllib.parse'],
     )
