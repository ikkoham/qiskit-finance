# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import setuptools
import inspect
import sys
import os

long_description = """Qiskit Finance is a open-source library of quantum computing finance experiments.
 """

requirements = [
    "qiskit-terra>=0.17.0",
    "qiskit-optimization",
    "scipy>=1.4",
    "numpy>=1.17",
    "psutil>=5",
    "scikit-learn>=0.20.0",
    "fastdtw",
    "setuptools>=40.1.0",
    "pandas",
    "quandl",
    "yfinance",
]

if not hasattr(setuptools, 'find_namespace_packages') or not inspect.ismethod(setuptools.find_namespace_packages):
    print("Your setuptools version:'{}' does not support PEP 420 (find_namespace_packages). "
          "Upgrade it to version >='40.1.0' and repeat install.".format(setuptools.__version__))
    sys.exit(1)

VERSION_PATH = os.path.join(os.path.dirname(__file__), "qiskit_finance", "VERSION.txt")
with open(VERSION_PATH, "r") as version_file:
    VERSION = version_file.read().strip()

setuptools.setup(
    name='qiskit-finance',
    version=VERSION,
    description='Qiskit Finance: A library of quantum computing finance experiments',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Qiskit/qiskit-finance',
    author='Qiskit Finance Development Team',
    author_email='hello@qiskit.org',
    license='Apache-2.0',
    classifiers=(
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering"
    ),
    keywords='qiskit sdk quantum finance',
    packages=setuptools.find_packages(include=['qiskit_finance', 'qiskit_finance.*']),
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.6",
    zip_safe=False
)
