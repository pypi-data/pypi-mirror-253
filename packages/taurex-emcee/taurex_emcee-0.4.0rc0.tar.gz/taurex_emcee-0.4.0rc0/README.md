# ``taurex-emcee``

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Documentation Status](https://readthedocs.org/projects/taurex-emcee/badge/?version=latest)](https://taurex-emcee.readthedocs.io/en/latest/?badge=latest)
[![status](https://joss.theoj.org/papers/54464cd302ddd06fc2305634889f1a14/status.svg)](https://joss.theoj.org/papers/54464cd302ddd06fc2305634889f1a14)

## Introduction

`taurex-emcee` is a plugin for [TauREx 3.1](https://github.com/ucl-exoplanets/TauREx3_public) that provides the [Emcee](https://emcee.readthedocs.io/en/stable/) sampler by Dan Foreman-Mackey & contributors for the retrieval.

## Table of contents

- [``taurex-emcee``](#taurex-emcee)
  - [Introduction](#introduction)
  - [Table of contents](#table-of-contents)
  - [How to install](#how-to-install)
    - [Install from PyPI](#install-from-pypi)
    - [Install from source code](#install-from-source-code)
      - [Test your installation](#test-your-installation)
  - [Documentation](#documentation)
    - [Build the html documentation](#build-the-html-documentation)
    - [Build the pdf documentation](#build-the-pdf-documentation)
  - [How to contribute](#how-to-contribute)
  - [How to cite](#how-to-cite)

## How to install

Instructions on how to install ``taurex-emcee``.

### Install from PyPI

``taurex-emcee`` is available on PyPI and can be installed via pip as

    pip install taurex_emcee

### Install from source code

``taurex-emcee`` is compatible (tested) with Python 3.8, 3.9 and 3.10

To install from source, clone the [repository](https://github.com/ExObsSim/taurex-emcee) and move inside the directory.

Then use `pip` as

    pip install .

#### Test your installation

Try importing ``taurex-emcee`` as

    python -c "import taurex_emcee"

You can verify if the plugin is functioning by seeing if TauREx successfully detects ``taurex-emcee``.

    taurex --plugins

If there are no errors then the installation was successful!

## Documentation

``taurex-emcee`` comes with a documentation, which can be built using Sphinx.
The documentation includes a tutorial, a user guide and a reference guide.

To build the documentation, install the needed packages first via:

    pip install -e ".[docs]"

### Build the html documentation

To build the html documentation, move into the `docs` directory and run

    make html

The documentation will be produced into the `build/html` directory inside `docs`.
Open `index.html` to read the documentation.

### Build the pdf documentation

To build the pdf, move into the `docs` directory and run

    make latexpdf

The documentation will be produced into the `build/latex` directory inside `docs`.
Open `taurex_emcee.pdf` to read the documentation.

The developers use `pdflatex`; if you have another compiler for LaTex, please refer to [sphinx documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html#latex-options).

## How to contribute

You can contribute to ``taurex-emcee`` by reporting bugs, suggesting new features, or contributing to the code itself.
If you wish to contribute to the code, please follow the steps described in the documentation under `Developer guide`.

## How to cite

A dedicated publication has been submitted and the relative information will be published soon.
In the meanwhile, please, send an email to the developers.
