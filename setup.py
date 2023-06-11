from setuptools import setup, find_packages

with open('requirements/default.txt') as r:
    install_requires = r.readlines()

setup(
    name='example',
    version='1.0.0',
    packages=['example'],
    install_requires= install_requires,
)
