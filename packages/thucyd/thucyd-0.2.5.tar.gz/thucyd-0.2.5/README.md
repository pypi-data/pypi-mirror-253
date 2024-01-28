<img src="https://gitlab.com/thucyd-dev/thucyd/raw/master/images/thucyd-tile-logo.1500px.png" alt="thucyd-logo" height="150"> 

# Advanced Eigenanalysis 

[![pipeline status](https://gitlab.com/thucyd-dev/thucyd/badges/master/pipeline.svg)](https://gitlab.com/thucyd-dev/thucyd/pipelines)
[![coverage report](https://gitlab.com/thucyd-dev/thucyd/badges/master/coverage.svg)](https://gitlab.com/thucyd-dev/thucyd/commits/master)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://gitlab.com/thucyd-dev/thucyd/blob/master/LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![python versions](https://img.shields.io/badge/py-%3E%3D3.7-blue)](https://pypi.python.org/pypi/thucyd)
[![numpy versions](https://img.shields.io/badge/numpy-%3E%3D1.23-blue)](https://www.numpy.org/)
[![pypi version](https://img.shields.io/pypi/v/thucyd.svg)](https://pypi.python.org/pypi/thucyd)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/thucyd.svg)](https://anaconda.org/conda-forge/thucyd)

## What is `thucyd`?

`thucyd` (thoo'-sid) delivers a reference implementation of advanced eigenanalysis tools. When more performant libraries are created (elsewhere) then they can use this version as a golden source. 

See [A consistently oriented basis for eigenanalysis](https://link.springer.com/article/10.1007/s41060-020-00227-z) (2020) in the _International Journal of Data Science and Analytics_ for details of the functions provided in `thucyd`.


## Package Installation

The two package hosts for `thucyd` are [PyPi](https://pypi.org/project/thucyd/) and [Conda-Forge](). The packages are identical and the only difference is the means of delivery. From PyPi, use `pip`,

```bash
$ pip install thucyd
```

and from Conda-Forge use `conda`:

```bash
$ conda install -c conda-forge thucyd
```

Once installed, the package is importable to Python:

```python
>>> import thucyd
```

A quick example call to the `eigen` subpackage would be

```python
>>> import numpy as np
>>> V = np.eye(3).dot(np.diag([1., -1., 1.]))
>>> E = np.arange(3)[::-1]
>>> Vor, Eor, signs, thetas, _ = thucyd.eigen.orient_eigenvectors(V, E)
>>> Vor
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
>>> signs
array([ 1., -1.,  1.])
```


## Package Dependency

The only dependencies `thucyd` has at this time is on [python >= 3.7](https://www.python.org/) and [numpy >= 1.23](https://www.numpy.org/). 


## About `thucyd`

[Thucydides](https://en.wikipedia.org/wiki/Thucydides) was the first Western writer and historian who applied scientific principles to the recording of Western history. Although Herodotus, who predates Thucydides by less than a generation, started the transformation away from the epic poetry enshrined by Homer to a more objective record, it was Thucydides who engaged in inquiry and cross validation of all accounts in his History of the Peloponnesian Wars.


## Buell Lane Press

[Buell Lane Press](https://buell-lane-press.co) is the package sponsor. 


