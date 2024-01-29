from setuptools import setup, find_packages
import os

VERSION = '0.0.10'
DESCRIPTION = 'Tools to facilitate the Automation of Aspen Plus through Python'
LONG_DESCRIPTION = 'N/A'

# Setting up
setup(
    name="plustools",
    version=VERSION,
    author="Albert Lenk",
    author_email="albert.lenk@outlook.de",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'itertools', 'os', 'win32com'],
    keywords=['python', 'aspen plus', 'process simulation', 'automation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
