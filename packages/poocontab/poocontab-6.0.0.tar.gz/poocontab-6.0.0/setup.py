from setuptools import setup, find_packages
from os import path

# lê o conteúdo do arquivo README.md
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

REQUIRED_PACKAGES = [
    'numpy',
    'matplotlib',
    'seaborn',
    'reportlab',
]


setup(
    name="poocontab",
    version="6.0.0",
    author="crisly",
    author_email="crislymaria21@gmail.com",
    description="Pacote de teste",
    long_description=long_description,
    # especifica que o long_description está em Markdown
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    keywords=['python', 'cont'],
    classifiers=["Development Status :: 3 - Alpha",]
)
