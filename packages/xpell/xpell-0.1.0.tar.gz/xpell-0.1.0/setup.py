# setup.py

from setuptools import setup, find_packages

setup(
    name='xpell',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'uuid',
        'threading',
        'asyncio',
        'websocket-client',
        # ... other dependencies
    ],
)
