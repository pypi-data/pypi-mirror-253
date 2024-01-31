from setuptools import setup, find_packages
from os import path

# lê o conteúdo do arquivo README.md
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()



setup(
    name="contabilib",
    version="5.1.0",
    author="crisly, erik",
    author_email="crislymaria21@gmail.com",
    description="Biblioteca para cálculos contábeis.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'seaborn',
        'fpdf',
    ],  # adiciona bibliotecas adicionais
    keywords=['python', 'contablidade'],
    classifiers=["Development Status :: 3 - Alpha",]
)
