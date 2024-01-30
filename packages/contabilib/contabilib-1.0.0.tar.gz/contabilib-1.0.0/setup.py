from setuptools import setup, find_packages

VERSION = "1.0.0"
DESCRIPTION = "Biblioteca para manipulações de serviços de contabilidade."
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
