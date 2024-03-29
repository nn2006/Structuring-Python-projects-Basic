# -*- coding: utf-8 -*-

# Learn more: https://github.com/nn2006/Structuring-Python-projects-Basic/setup.py
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Structuring-Python-projects-Basic',
    version='0.1.0',
    description='Structuring package for Python-Guide.org',
    long_description=readme,
    author='Muhammad Adil',
    author_email='nn2006@gmail.com',
    url='https://github.com/nn2006/Structuring-Python-projects-Basic',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

