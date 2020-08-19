from setuptools import setup, find_packages
from os.path import join, dirname

import configger

setup(
    name='py-configger',
    version=configger.__version__,
    license='MIT',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author="@PaperDevil",
    author_email="ketov-x@yandex.ru",
    download_url='https://github.com/PaperDevil/pyconfigger/blob/master/dist/py-configger-0.1.2a0.tar.gz'
)
