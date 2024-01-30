from setuptools import setup, find_packages
import codecs
import os

VERSION = "1.0.9"
DESCRIPTION = "Pacote para mnipulação de arquivos"

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()



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
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    keywords=['python', 'files', 'Pyl3s', 'Pyl3sLib, libpyles'],

)
