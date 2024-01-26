import codecs
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.6'
DESCRIPTION = 'feluda'

# Setting up
setup(
    name="Feluda",
    version=VERSION,
    author="Soumyajit Pan",
    author_email="soumyajitpan29@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['excel', 'excelreader', 'excelwriter', 'python', 'excel reader and writer', 'read excel data using python', 'write data in excel using python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
