from setuptools import setup, find_packages

VERSION = "1.0.7"
DESCRIPTION = "Pacote para mnipulação de arquivos"
LONG_DESCRIPTION = "Pacote para mnipulação de arquivos, diretorios e conversão"

REQUIRED_PACKAGES = [
    'PyPDF2',
    'fpdf'
]

setup(
    name="libpyles",
    version=VERSION,
    author="PedroVitor",
    author_email="pedro.passos@ufpi.edu.br",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    keywords=['python', 'files', 'Pyl3s', 'Pyl3sLib'],

)
