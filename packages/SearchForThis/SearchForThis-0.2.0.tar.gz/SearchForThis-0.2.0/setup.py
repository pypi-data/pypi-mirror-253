from setuptools import setup, find_packages
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    readme = '\n' + fh.read()
 
VERSION = '0.2.0'
DESCRIPTION = 'Projeto final da disciplina de Programação Orientada a Objetos II'

setup(
    name = 'SearchForThis',
    version = VERSION,
    author = 'liedson',
    author_email = 'fabricoliedson@gamil.com',
    description = DESCRIPTION,
    long_description = readme,
    long_description_content_type = 'text/markdown',
    packages = ['SearchForThis'],
    python_requires = '>=3.6',
    install_requires = ['googlesearch-python==1.2.3'],

    keywords = ['python', 'web', 'search'],
    classifiers = [
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ]
 
)

# pypi-AgEIcHlwaS5vcmcCJGM1MjY4MWQyLWFhYmEtNDA5ZS05ZDNjLTQxNWY0Mzc3OTM1NwACKlszLCIxZWNkZDA1Yi0zM2VlLTQ4ZDAtOWIxZS05ZjM0NjRkYjFmYjEiXQAABiBCi99wIevAE2UyLF9i1S1QmY3bIn_V4lJyh5XJnnXwvQ
