# setup.py
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gaussian_theorems",
    version="1.1",  # Update to a new version number
    description="Gaussian and Binomial distributions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Makoha Dharren Pius',
    author_email='dharrenpius@outlook.com',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)