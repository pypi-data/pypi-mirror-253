from setuptools import setup
from setuptools import find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='uestcnet',
    version='0.4',
    packages=find_packages(),
    long_description=long_description,
    author='atfwus',
    author_email='atfwus@qq.com',
    install_requires=[
        'Requests==2.31.0',
    ],
)