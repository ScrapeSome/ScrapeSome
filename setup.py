"""
Setup Script for ScrapeSome Package
-----------------------------------

This script uses setuptools to package and distribute the `scrapesome` Python project.

Features:
- Provides metadata about the package such as name, version, author, and description.
- Automatically finds and includes all packages using `find_packages()`.
- Loads the long description from `README.md` for display on PyPI.
- Defines Python version requirements and package classifiers.

    To upload to PyPI (after configuring credentials):
        $ twine upload dist/*
"""

import pathlib
import re
from setuptools import setup

here = pathlib.Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")


# Read the version string from scrapesome/__init__.py without importing the package
def read_version():
    """Read version dynamically"""
    version_file = here / "scrapesome" / "__init__.py"
    version_content = version_file.read_text(encoding="utf-8")
    version_match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', version_content, re.MULTILINE)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

version = read_version()

setup(
    name="scrapesome",
    version=version,
    author="Vishnu Vardhan Reddy",
    author_email="gvvr2024@gmail.com",
    description="A Powerful Web Scraper with dynamic rendering support.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scrapesome/scrapesome"
)
