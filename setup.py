# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("Readme.md").read()
except IOError:
    long_description = ""

setup(
    name="web-automation-example",
    version="0.1.0",
    description="A pip package",
    license="MIT",
    author="Matheus Barbachan",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.12",
    ]
)
