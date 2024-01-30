from setuptools import setup, find_packages

VERSION = "1.0.0"
DESCRIPTION = "Pacote de teste"
LONG_DESCRIPTION = "Biblioteca Python para manipulações de arquivos."


REQUIRED_PACKAGES = [
    'PyPDF2',
    'fpdf'
]

setup(
    # the name must match the folder name
    name="libpyles",
    version=VERSION,
    author="PedroVitor",
    author_email="pedro.passos@ufpi.edu.br",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,  # adiciona bibliotecas adicionais
    keywords=['python', 'files', 'Pyl3s', 'Pyl3sLib'],

)
