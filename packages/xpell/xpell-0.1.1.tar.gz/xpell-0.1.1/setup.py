# setup.py

from setuptools import setup, find_packages

setup(
    name='xpell',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'uuid',
        'asyncio',
        'websocket-client',
        # ... other dependencies
    ],
)
