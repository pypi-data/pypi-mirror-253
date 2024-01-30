from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.11'
DESCRIPTION = 'Tools to facilitate the automation of Aspen Plus through Python'
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="plustools",
    version=VERSION,
    author="Albert Lenk",
    author_email="albert.lenk@outlook.de",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    license= "GNU GPLv3",
    license_files = r'C:\Users\alber\PycharmProjects\plustools\LICENSE',
    packages=find_packages(),
    install_requires=['pandas', 'itertools', 'os', 'win32com'],
    keywords=['python', 'aspen plus', 'process simulation', 'automation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
