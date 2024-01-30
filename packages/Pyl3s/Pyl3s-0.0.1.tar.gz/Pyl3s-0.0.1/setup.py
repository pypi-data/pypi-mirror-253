from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='Pyl3s',
    version='0.0.1',
    license='MIT License',
    author='Pedro Vitor, Marcos Andre',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='pedro.passos@ufpi.edu.br',
    keywords='files',
    description=u'Ainda em desenvolvimento',
    packages=['pyl3s'],
    install_requires=['fpdf', 'PyPDF2', 're'],)