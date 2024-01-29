# Data Utility Packages: _Core_

[![test](https://github.com/korawica/ddeutil/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/korawica/ddeutil/actions/workflows/tests.yml)
[![python support version](https://img.shields.io/pypi/pyversions/ddeutil)](https://pypi.org/project/ddeutil/)
[![size](https://img.shields.io/github/languages/code-size/korawica/ddeutil)](https://github.com/korawica/ddeutil)

**Table of Contents:**:

- [Features](#features)
  - [Base Utility Functions](#base-utility-functions)
  - [Utility Functions](#utility-functions)

The **Core Utility** package implements the utility functions and objects
that was created on sub-package namespace, `ddeutil`, design for independent
installation. I make this package able to extend with any sub-extension with this
namespace. This namespace able to scale out the coding with folder
structure design. You can add any extension features and import by
`import ddeutil.{extension}`.

This package provide the Base Utility functions and objects for any data package
or data application.

**Install from PyPI**:

```shell
pip install ddeutil
```

## Features

### Base Utility Functions

```text
core.base
    - cache
    - checker
    - convert
    - elements
    - hash
    - merge
    - sorting
    - splitter
```

### Utility Functions

```text
core
    - decorator
    - dtutils
    - randomly
```

## License

This project was licensed under the terms of the [MIT license](LICENSE).
