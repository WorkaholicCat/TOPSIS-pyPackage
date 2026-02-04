from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text() 
setup(
    name='Topsis-Aartha-102302941',
    version='1.0.5',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    author='Aartha Singh',
    author_email='Aartha.tab@gmail.com',
    license='MIT',
     project_urls={
           'Source Repository': 'https://github.com/WorkaholicCat/TOPSIS-pyPackage' 
    }
)
