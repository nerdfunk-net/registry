"""Setup configuration for the registry package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="registry",
    version="0.1.0",
    author="nerdfunk-net",
    description="A simple registry implementation for storing and retrieving key-value pairs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nerdfunk-net/registry",
    py_modules=["registry"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
