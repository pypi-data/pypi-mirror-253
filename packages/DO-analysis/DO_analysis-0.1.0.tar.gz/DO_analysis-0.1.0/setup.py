from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='DO_analysis',
    version='0.1.0',
    description='A simple Python library for calculating Dissimilarity Overlap Curve and alpha/beta diversity',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Valeriia Ivanova',
    packages=find_packages(include=['DOC_analysis']),
    license="MIT",
    download_url = 'https://github.com/IvanovaVA/DOC_analysis/archive/refs/tags/0.1.0.tar.gz',
)
