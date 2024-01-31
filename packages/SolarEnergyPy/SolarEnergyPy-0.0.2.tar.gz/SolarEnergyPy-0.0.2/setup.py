import codecs
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'A package for fundamental information of solar energy.'

setup(
    name="SolarEnergyPy",
    version=VERSION,
    author="Liqun He",
    author_email="heliqun@ustc.edu.cn",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    license='MIT',
    url = 'https://pypi.org/project/SolarEnergyPy/',
    keywords=['python', 'solarenergyPy','windows'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
