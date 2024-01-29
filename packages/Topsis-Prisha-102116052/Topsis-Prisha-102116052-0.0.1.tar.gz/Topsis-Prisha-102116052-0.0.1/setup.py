from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'TOPSIS Application'
LONG_DESCRIPTION = 'A package that allows to help in mutiple factor decisions using the method of TOPSIS.'

# Setting up
setup(
    name="Topsis-Prisha-102116052",
    version=VERSION,
    author="Prisha Sawhney",
    author_email="psawhney_be21@thapar.edu",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['sys', 'os', 'pandas', 'numpy'],
    keywords=['python', 'topsis'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)