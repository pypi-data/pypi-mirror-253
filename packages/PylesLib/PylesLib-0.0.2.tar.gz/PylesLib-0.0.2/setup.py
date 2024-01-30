from setuptools import setup, find_packages

VERSION = "0.0.2"
DESCRIPTION = "Pacote de teste"
LONG_DESCRIPTION = "Biblioteca Python para manipulações de arquivos."


REQUIRED_PACKAGES = [
    'PyPDF2',
    'fpdf'
]

setup(
    # the name must match the folder name
    name="PylesLib",
    version=VERSION,
    author="MarcoAndre",
    author_email="marcosofc04@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,  # adiciona bibliotecas adicionais
    keywords=['python', 'files', 'Pyles', 'PylesLib'],

)
