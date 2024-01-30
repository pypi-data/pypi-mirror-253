#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    author='Silique',
    author_email='egarette@silique.fr',
    name='rougail',
    version='0.1',
    description='Configuration templating engine',
    url='https://forge.cadoles.com/Infra/rougail',
    packages=find_packages('src'),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={"": ["data/*.dtd"]}
)
