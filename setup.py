#!/usr/bin/env python

from setuptools import setup

setup(
    name='fampipeline',
    version='0.0.2',
    author='Bernie Pope, Khalid Mahmood, Jessica Chung',
    author_email='kmahmood@unimelb.edu.au',
    packages=['src'],
    entry_points={
        'console_scripts': ['fampipeline = src.main:main']
    },
    url='https://github.com/khalidm/fampipeline',
    license='LICENSE',
    description='fampipeline is a pipeline system for bioinformatics workflows\
     with support for running pipeline stages on a distributed compute cluster.',
    long_description=open('README.md').read(),
    install_requires=[
        "pipeline_base == 1.0.0",
        "ruffus == 2.6.3",
    ],
)
