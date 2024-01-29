from setuptools import setup, find_packages

setup(
    name='AYVAZIHA',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'yaml>=2.0.2',
        'logging>=0.27.1',
    ]
)