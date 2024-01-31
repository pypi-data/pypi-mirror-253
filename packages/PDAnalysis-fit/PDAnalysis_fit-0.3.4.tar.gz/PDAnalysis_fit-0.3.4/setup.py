from pathlib import Path

from setuptools import setup

requirements = [
    "numpy>=1.20.3",
    "scipy>=1.6.3",
    "lmfit>=1.0.3",
    "matplotlib>=3.4.2",
    "pandas>=1.2.4",
    "s3fs[boto3]",
    "xarray",
    "zarr>=2.10.1",
]

version_file = Path.cwd() / "PDAnalysis_fit" / "_version.py"
with open(version_file) as f:
    version = f.readlines()[-1].split()[-1].strip("\"'")

info = {
    "name": "PDAnalysis_fit",
    "version": version,
    "maintainer": "Xanadu Inc.",
    "license": "MIT License",
    "description": "Package for Proccessing PD Data",
    "long_description": open("README.md", encoding="utf-8").read(),
    "long_description_content_type": "text/markdown",
    "packages": ["PDAnalysis_fit"],
    "provides": ["PDAnalysis_fit"],
    "install_requires": requirements,
}

classifiers = [
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: POSIX",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Scientific/Engineering :: Physics",
]

setup(classifiers=classifiers, **(info), python_requires=">3.8.0")