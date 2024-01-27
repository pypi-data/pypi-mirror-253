import pathlib

import setuptools

from setuptools import setup, find_packages

setup(
    name='train_time',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'keras',
    ],
    author='Akinyemi Arabambi',
    description='A Keras callback to estimate remaining training time',
    long_description= pathlib.Path('README.md').read_text(),
    long_description_content_type = 'text/markdown',
    url='https://https://github.com/2abet/TrainTime',
)
