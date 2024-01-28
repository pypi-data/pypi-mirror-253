# Component Contribution

[![PyPI version](https://badge.fury.io/py/component-contribution.svg)](https://badge.fury.io/py/component-contribution)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/component-contribution/badges/version.svg)](https://anaconda.org/conda-forge/component-contribution)
[![Python version](https://img.shields.io/pypi/pyversions/component-contribution.svg)](https://www.python.org/downloads)
[![MIT license](https://img.shields.io/pypi/l/component-contribution.svg)](https://mit-license.org/)

[![pipeline status](https://gitlab.com/elad.noor/component-contribution/badges/develop/pipeline.svg)](https://gitlab.com/elad.noor/component-contribution/commits/develop)
[![codecov](https://codecov.io/gl/equilibrator/component-contribution/branch/develop/graph/badge.svg?token=OxxaCqgaLs)](https://codecov.io/gl/equilibrator/component-contribution)
[![Join our Google group](https://img.shields.io/badge/google_group-equilibrator_users-blue)](https://groups.google.com/g/equilibrator-users)
[![Documentation Status](https://readthedocs.org/projects/equilibrator/badge/?version=latest)](https://equilibrator.readthedocs.io/en/latest/?badge=latest)

A method for estimating the standard reaction Gibbs energy of biochemical reactions. 

## Cite us

For more information on the method behind component-contribution, please view our open
access paper:

Noor E, Haraldsdóttir HS, Milo R, Fleming RMT (2013)
[Consistent Estimation of Gibbs Energy Using Component Contributions](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003098),
PLoS Comput Biol 9:e1003098, DOI: 10.1371/journal.pcbi.1003098

Please, cite this paper if you publish work that uses `component-contribution`.

## Installation

* `pip install component-contribution`

## Dependencies

* Python 3.9+
* PyPI dependencies for prediction:
  - equilibrator-cache
  - numpy
  - scipy
  - pandas
  - pint
  - path
  - periodictable
  - uncertainties
* PyPI dependencies for training a new model:
  - openbabel
  - equilibrator-assets

## Data sources

* [Training data for the component contribution method](https://zenodo.org/record/3978440)
* [Chemical group definitions for the component-contribution method](https://zenodo.org/record/4010930)
