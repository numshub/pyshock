#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    numpy,
    scipy
    # TODO: put package requirements here
]

test_requirements = [
    pytest,
    # TODO: put package test requirements here
]

setup(
    name='pyshock',
    version='0.1.0',
    description="A python library to calculate shock response spectra.",
    long_description=readme + '\n\n' + history,
    author="Pierpaolo Da Fieno",
    author_email='pierpaolo.dafieno@gmail.com',
    url='https://github.com/numshub/pyshock',
    packages=[
        'pyshock',
    ],
    package_dir={'pyshock':
                 'pyshock'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pyshock',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
