# Python Packaging Tutorial

## Overview
This project serves as a practical guide to learn and understand the process of packaging Python modules. The aim is to demonstrate best practices in creating a Python package, managing dependencies, and preparing it for distribution via PyPI (Python Package Index).

## Objectives
- Learn how to structure a Python project.
- Understand the use of `pyproject.toml` and `setup.py` files.
- Explore how to define package metadata and manage package dependencies.
- Practice building, installing, and distributing a Python package.

## Project Structure
The project is structured as follows:

```bash
- mypackage/
    - README.md
    - pyproject.toml
    - setup.py
    - mypackage/
        - __init__.py
        - module1.py
        - module2.py
    - tests/
        - test_module1.py
        - test_module2.py
```


- **src/**: Contains the source code of the package.
- **tests/**: Contains unit tests for the package modules.
- **README.md**: Provides a comprehensive overview of the project.
- **setup.py**: The build script for setuptools.
- **pyproject.toml**: Specifies the build system requirements.

## Installation
To install this package locally, run the following command from the root directory of the project:

```bash
pip install .
```

## Building the Package

```bash
python -m build
```

This command generates distribution archives in the dist/ directory.

## Testing

```bash
pytest tests/
```
