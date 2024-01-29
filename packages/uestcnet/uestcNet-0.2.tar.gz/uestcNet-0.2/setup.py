from setuptools import setup
from setuptools import find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='uestcNet',
    version='0.2',
    packages=find_packages(),
    long_description=long_description,
    install_requires=[
        'Requests==2.31.0',
    ],
)
