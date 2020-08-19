from setuptools import setup, find_packages
from os.path import join, dirname

import configger

setup(
    name='py-configger',
    version=configger.__version__,
    license='MIT',
    packages=find_packages(),
    description="Simple package for easy configuration of your projects.",
    author="@PaperDevil",
    author_email="ketov-x@yandex.ru",
    download_url='https://github.com/PaperDevil/pyconfigger/blob/master/dist/py-configger-0.1.2a0.tar.gz'
)
