from setuptools import setup, find_packages

VERSION = "0.0.3"
DESCRIPTION = "Pacote de teste"
LONG_DESCRIPTION = "Biblioteca Python para manipulações de serviços de contabilidade."


REQUIRED_PACKAGES = [
    'numpy',
    'matplotlib',
    'fpdf'
]

setup(
    # the name must match the folder name
    name="Contablibi",
    version=VERSION,
    author="crisly, erik",
    author_email="eriklustosa8@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,  # adiciona bibliotecas adicionais
    keywords=['python', 'contablib'],
    classifiers=["Development Status :: 3 - Alpha",]

)
