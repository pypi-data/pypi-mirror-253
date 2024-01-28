from setuptools import setup

setup(
    name='hqdata_api_wrapper',
    version='0.0.2',
    description='A Python wrapper for the HQData API',
    long_description='This is a Python package that provides a convenient wrapper for interacting with the HQData API. It allows you to easily run and fetch job/result data from the HQData service.',
    long_description_content_type='text/markdown',
    author='Marco Capuano',
    author_email='marco.capuano@starux.ch',
    url='https://hqdata.com',
    packages=['HQDataAPIWrapper'],
    install_requires=[
        'requests'
    ],
)