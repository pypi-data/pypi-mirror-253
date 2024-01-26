![SimpleWhois logo](https://mauricelambert.github.io/info/python/code/SimpleWhois_small.png "SimpleWhois logo")

# SimpleWhois

## Description

This module implements WHOIS protocol and performs WHOIS requests.

> This module is a pure python implementation and doesn't use `whois` executable.

## Requirements

This package require:
 - python3
 - python3 Standard Library

## Installation

```bash
python3 -m pip install SimpleWhois
```

```bash
git clone "https://github.com/mauricelambert/SimpleWhois.git"
cd "SimpleWhois"
python3 -m pip install .
```

## Usages

### Command line

```bash
SimpleWhois              # Using CLI package executable
python3 -m SimpleWhois   # Using python module
python3 SimpleWhois.pyz  # Using python executable
SimpleWhois.exe          # Using python Windows executable

SimpleWhois 8.8.8.8
SimpleWhois example.com 2001:1c00::78
```

### Python script

```python
from SimpleWhois import *
whois("8.8.8.8")
whois("example.com")
whois("2001:1c00::78")
```

## Links

 - [Pypi](https://pypi.org/project/SimpleWhois)
 - [Github](https://github.com/mauricelambert/SimpleWhois)
 - [Documentation](https://mauricelambert.github.io/info/python/code/SimpleWhois.html)
 - [Python executable](https://mauricelambert.github.io/info/python/code/SimpleWhois.pyz)
 - [Python Windows executable](https://mauricelambert.github.io/info/python/code/SimpleWhois.exe)

## License

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
