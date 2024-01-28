#!/usr/bin/env python
"""Setup script for the project."""

import re

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description: str = f.read()


with open("orb/requirements.txt", "r", encoding="utf-8") as f:
    requirements: list[str] = f.read().splitlines()


with open("orb/requirements-dev.txt", "r", encoding="utf-8") as f:
    requirements_dev: list[str] = f.read().splitlines()


with open("orb/__init__.py", "r", encoding="utf-8") as fh:
    version_re = re.search(r"^__version__ = \"([^\"]*)\"", fh.read(), re.MULTILINE)
assert version_re is not None, "Could not find version in orb/__init__.py"
version: str = version_re.group(1)


setup(
    name="openorb",
    version=version,
    description="The orb project",
    author="Matthew Freed",
    url="https://github.com/dpshai/orb",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.11",
    install_requires=requirements,
    tests_require=requirements_dev,
    entry_points={
        "console_scripts": [
            "start-orb=orb.cli.virtual:main",
        ],
    },
    extras_require={"dev": requirements_dev},
)
