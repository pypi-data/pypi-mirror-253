from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='hqdata_api_wrapper',
    version='0.0.3',
    description='A Python wrapper for the HQData API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Marco Capuano',
    author_email='marco.capuano@starux.ch',
    url='https://hqdata.com',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
)