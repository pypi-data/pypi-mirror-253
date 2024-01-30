from setuptools import setup, find_packages

VERSION = '0.3.3'
DESCRIPTION = 'Busca produtos na web'
LONG_DESCRIPTION = 'Realiza uma busca por produtos nos sites, filtrando por nome e valor máximo.'

setup(
    name = "buscarProdutos",
    version = VERSION,
    author = "Alison",
    author_email = 'alissonmarqueshm30@gmail.com',
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    packages = find_packages(),
    install_requires = ['requests', 'beautifulsoup4'],
    keywords=['python', 'busca', 'web', 'produto', 'preço', 'mercado livre', 'magazine luiza'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

)
