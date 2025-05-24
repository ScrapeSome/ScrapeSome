"""
Setup Script for ScrapeSome Package
-----------------------------------

This script uses setuptools to package and distribute the `scrapesome` Python project.

Features:
- Provides metadata about the package such as name, version, author, and description.
- Automatically finds and includes all packages using `find_packages()`.
- Loads the long description from `README.md` for display on PyPI.
- Defines Python version requirements and package classifiers.

Usage:
    To build and install the package locally:
        $ python setup.py sdist bdist_wheel
        $ pip install dist/scrapesome-0.0.1-py3-none-any.whl

    To upload to PyPI (after configuring credentials):
        $ twine upload dist/*
"""

from setuptools import setup, find_packages

setup(
    name="scrapesome",
    version="0.0.1",
    author="Vishnu Vardhan Reddy",
    author_email="gvvr2001@gmail.com",
    description="web scraper with dynamic rendering support.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ScrapeSome/ScrapeSome",
    packages=find_packages(include=["scrapesome", "scrapesome.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
