# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oglhclient",
    version="1.0.1",
    author="Lighthouse Team",
    author_email="engineering@opengear.com",
    description="An API client library for Opengear Lighthouse",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/opengear/oglhclient",
    project_urls={
        "Bug Tracker": "https://github.com/opengear/oglhclient/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        'requests', 'pyyaml',
    ],
)
