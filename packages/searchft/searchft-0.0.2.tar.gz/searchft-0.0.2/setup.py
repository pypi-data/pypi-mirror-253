from setuptools import setup, find_packages

with open('README.md', 'r') as arq:
    readme = arq.read()

VERSION = '0.0.2'
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
    install_requires = ['googlesearch', 'webbrowser'],

    keywords = ['python', 'web', 'search'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ]
 
)