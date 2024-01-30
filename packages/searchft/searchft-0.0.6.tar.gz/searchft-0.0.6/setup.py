from setuptools import setup, find_packages

with open('README.md', 'r') as arq:
    readme = arq.read()

VERSION = '0.0.6'
DESCRIPTION = 'Projeto final da disciplina de Programação Orientada a Objetos II'


setup(
    name = 'searchft',
    version = VERSION,
    author = 'liedson',
    author_email = 'fabricoliedson@gamil.com',
    description = DESCRIPTION,
    long_description = readme,
    long_description_content_type = 'text/markdown',
    packages = ['searchft'],
    install_requires = ['googlesearch-python==1.2.3', 'webbrowser'],

    keywords = ['python', 'web', 'search'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ]
 
)

# pypi-AgEIcHlwaS5vcmcCJGM1MjY4MWQyLWFhYmEtNDA5ZS05ZDNjLTQxNWY0Mzc3OTM1NwACKlszLCIxZWNkZDA1Yi0zM2VlLTQ4ZDAtOWIxZS05ZjM0NjRkYjFmYjEiXQAABiBCi99wIevAE2UyLF9i1S1QmY3bIn_V4lJyh5XJnnXwvQ