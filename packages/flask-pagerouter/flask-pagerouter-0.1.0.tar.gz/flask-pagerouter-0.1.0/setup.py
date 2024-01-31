from setuptools import setup, find_packages

setup(
    name='flask-pagerouter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
    ],
    author='Etienne DTS',
    description='A lightweight Python library for page routing in Flask applications.',
    license='MIT',
)