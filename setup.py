# -*- coding: utf-8 -*-

"""
python-2gis
============

A Python library for accessing the 2gis API
"""

from setuptools import setup, find_packages


setup(
    name='2gis',
    version='0.8.6',
    author='IRK.ru',
    author_email='support@irk.ru',
    url='https://github.com/irkru/python-2gis',
    description='2gis library for Python',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(),
    install_requires=('requests'),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
    ),
)
