#!/usr/bin/env python
from setuptools import setup
import sys

version = sys.version_info[:2]
if version < (2, 7):
    print('crawl requires Python version 2.7 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)
elif (3, 0) < version < (3, 3):
    print('crawl requires Python version 3.3 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)

VERSION = '0.1'

install_requires = ['dryscrape', 'docopt', 'reppy']

setup(
    name='crawl',
    version=VERSION,
    description="A not-so-magnificent website crawler.",
    author='Michael Dreiling',
    author_email='michaeldreiling@localprojects.net',
    url='https://github.com/local-projects/crawl',
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    scripts=['crawl'],
)