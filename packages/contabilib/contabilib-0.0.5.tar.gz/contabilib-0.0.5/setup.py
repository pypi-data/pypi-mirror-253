from setuptools import setup, find_packages

VERSION = "0.0.5"
DESCRIPTION = "Biblioteca para calculos contabeis."
LONG_DESCRIPTION = "Biblioteca Python para manipulações de serviços de contabilidade."


REQUIRED_PACKAGES = [
    'numpy',
    'matplotlib',
    'fpdf'
]

setup(
    # the name must match the folder name
    name="contabilib",
    version=VERSION,
    author="crisly",
    author_email="crislymaria21@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,  # adiciona bibliotecas adicionais
    keywords=['python'],
    classifiers=["Development Status :: 3 - Alpha",]

)
