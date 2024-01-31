from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='flask-pagerouter',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
    ],
    author='Etienne DTS',
    description='A lightweight Python library for page routing in Flask applications.',
    license='MIT',
    long_description=description,
    long_description_content_type ="text/markdown"
)