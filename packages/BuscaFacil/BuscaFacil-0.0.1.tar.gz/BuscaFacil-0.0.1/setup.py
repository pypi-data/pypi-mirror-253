from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Busca produtos na web'
LONG_DESCRIPTION = 'Realiza uma busca por produtos nos sites, filtrando por nome e valor máximo.'

setup(
    name="BuscaFacil",
    version=VERSION,
    author="Alison",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'beautifulsoup4'],
    keywords=['python', 'busca', 'web', 'produto', 'preço', 'mercado livre', 'magazine luiza'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

)