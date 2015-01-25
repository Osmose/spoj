#!/usr/bin/env python
import codecs
import os
import re
from setuptools import setup, find_packages


def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts), encoding='utf8').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='spoj',
    description='Utility for solving Sphere Online Judge problems in Python.',
    long_description=read('README.rst'),
    version=find_version('spoj.py'),
    packages=find_packages(),
    author='Michael Kelly',
    author_email='me@mkelly.me',
    url='https://github.com/Osmose/spoj',
    license='MIT',
    install_requires=[
        'argh>=0.26.1',
        'beautifulsoup4>=4.3.2',
        'blessings>=1.6',
        'requests>=2.5.1',
    ],
    include_package_data=True,
    entry_points={
      'console_scripts':[
          'spoj = spoj:main'
      ]
   }
)
