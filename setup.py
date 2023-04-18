#!/usr/bin/env python

from distutils.core import setup
from convexvalue.__version__ import getVersion

setup(
      name='convexvalue',
      version=getVersion(),
      description='Python API wrapper library for Convex Value API',
      author='@aaronsdevera',
      author_email='aaronsdevera@protonmail.com',
      url='https://github.com/aaronsdevera/convex-value-python',
      packages=['convexvalue']
)
