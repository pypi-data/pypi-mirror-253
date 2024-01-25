# -*- coding: utf-8 -*-
import os
import sys
from setuptools import find_packages, setup


def read(fname):
    with open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), fname),
        "r",
        encoding="utf-8",
    ) as fin:
        return fin.read()

if sys.version_info < (3, 8):
    pmg_version = "pymatgen"
    monty_version = "monty<=2021.12.1" # removed os.path.which
else:
    pmg_version = "pymatgen >= 2022.2.7" # removed monty os.path.which
    monty_version = "monty"

setup(
    name="dspawpy",
    version="1.1.7",
    packages=find_packages(),
    url="http://www.hzwtech.com/",
    license="MIT",
    author="Hzwtech",
    author_email="ZhengZhilin@hzwtech.com",
    description="Tools for dspaw",
    install_requires=[
        pmg_version, 
        "statsmodels",
        "h5py",
        monty_version,
        # "statsmodels>=0.12.0",
        # "h5py >= 3.7",
        "prompt_toolkit",
        "loguru",
    ],  # numpy can be >=1.25, UserWarning about longdouble relates to WSL1, not numpy.
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["cli=dspawpy.cli.cli:main", "ecli=dspawpy.cli.cli_en:main"]
    },
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license_files=("LICENSE.txt",),
)
