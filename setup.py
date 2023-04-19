# This file identifies where the __init__.py file is in the working directory
#, and builds python packages.
from setuptools import setup, find_packages


setup(
    name="src",
    version="0.0.1",
    description="Working on MLops",
    author="Oham",
    packages=find_packages(),
    license="MIT"
)