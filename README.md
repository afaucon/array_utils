# Python data types - generic pretty printers and dump functions

This package provides helpers for pretty printing and to dump pyhon data types.

## Installation

### For users

Install the package [from GitHub](https://pip.pypa.io/en/stable/reference/pip_install/#git).

```
(venv) ~>pip install git+https://github.com/afaucon/pdttools.git
(venv) ~>pip list
```

### For developpers

Clone the package from GitHub and install it in editable mode (i.e. [setuptools "develop mode"](https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode)).

```
(venv) ~>git clone git+https://github.com/afaucon/pdttools.git
(venv) ~>pip install --editable pdttools
(venv) ~>pip list
```

## Usage

Within a python module:

```python
import pdttools

pdttools.__author__
pdttools.__version__
```

```python
import pdttools

my_list = [1, 2, 3]
pdttools.gprint(my_list)
```

## How to contribute?

### Running non regression tests

```
(venv) ~>git clone git+https://github.com/afaucon/pdttools.git
(venv) ~>pip install --editable pdttools
(venv) ~>cd pdttools
(venv) ~>pytest
```