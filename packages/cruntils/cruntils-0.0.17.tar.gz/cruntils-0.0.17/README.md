# Introduction

A collection of utilities. Mainly for me. Others may find them useful.

# Updating package

To update the package, take the following steps:
- Delete the **/dist** folder
- Delete the **/cruntils.egg-info** folder
- Update versions in **pyproject.toml** and **setup.py**
- Build new package with **py -m build**
- Upload to PyPi with **py -m twine upload dist/\***

# Package Creation

Okay, this guide was also really useful:
https://packaging.python.org/en/latest/tutorials/packaging-projects/

Used the following guide to create the package:
https://python-packaging.readthedocs.io/en/latest/minimal.html

