from setuptools import setup, find_packages
import os

VERSION = "1.0.0"
DESCRIPTION = "Open-source tool for climatological time series reconstruction, extension and validation"

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
    
setup(
    name = "rascal-ties",
    version = VERSION,
    author = "Alvaro Gonzalez-Cervera",
    author_email="<alvaro@intermet.es>",
    description = DESCRIPTION,
    readme = "README.md",
    packages = find_packages(),
    install_requires = [
        "pandas>=1.3.5",
        "tqdm>=4.64.0",
        "numpy>=1.21.6",
        "xarray>=0.20.2",
        "eofs>=1.4.0",
        "dask>=2021.10.0",
        "scipy>=1.7.3",
        "seaborn>=0.11.2",
        "matplotlib>=3.5.2",
        "scikit-learn>=1.0.2"
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url = "https://github.com/alvaro-gc95/RASCAL",
    long_description=read('README.md')
)
