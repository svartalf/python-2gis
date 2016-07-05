# -*- coding: utf-8 -*-

"""
python-2gis
============

A Python library for accessing the 2gis API
"""

from setuptools import setup, find_packages


setup(
    name='2gis',
    version='1.3.1',
    author='svartalf',
    author_email='self@svartalf.info',
    url='https://github.com/svartalf/python-2gis',
    description='2gis library for Python',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(),
    install_requires=('requests', 'six'),
    test_suite='tests',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
    ),
)
