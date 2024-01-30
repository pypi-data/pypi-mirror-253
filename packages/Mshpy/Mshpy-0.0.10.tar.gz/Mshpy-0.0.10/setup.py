from setuptools import setup, find_packages
from pathlib import Path
DESCRIPTION = 'Simplified Earth magnetosheath model'

this_directory = Path(__file__).parent
LONG_DESCRIPTION =  (this_directory / "README.md").read_text()

setup(
    name='Mshpy',
    version='0.0.10',
    packages=find_packages(),
    install_requires=[
        'sympy'
    ],
)