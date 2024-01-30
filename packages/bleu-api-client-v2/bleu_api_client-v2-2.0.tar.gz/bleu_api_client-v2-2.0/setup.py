# faceki_sdk/setup.py
from setuptools import setup, find_packages

setup(
    name='bleu_api_client-v2',
    version='2.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
