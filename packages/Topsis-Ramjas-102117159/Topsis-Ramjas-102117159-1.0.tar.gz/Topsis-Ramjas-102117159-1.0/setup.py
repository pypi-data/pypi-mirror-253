from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0'
DESCRIPTION = 'Topsis-Ramjas-102117159'
LONG_DESCRIPTION = 'A multi-criteria decision-making method'

# Setting up
setup(
    name="Topsis-Ramjas-102117159",
    version=VERSION,
    author="RAMJAS",
    author_email="<rlangdi_be21@thapar.edu>",
    description='Topsis package',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['python', 'numpy', 'pandas', 'sys'],
    keywords=['python', 'topsis'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)