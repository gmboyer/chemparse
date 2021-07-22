# chemparse

A lightweight package for parsing chemical formula strings into python dictionaries. 

## Features

* Convert a chemical formula string into a python dictionary.
    - example: `"CH4"` returns `{"C":1.0, "H":4.0}`
* Handles fractional stoichiometry.
    - example: `"C1.5O3"` returns `{"C":1.5, "O":3.0}`
    - example: `"H2e-1O1e-1"` returns `{"H":0.2, "O":0.1}`
* Handles groups with parentheses.
    - example: `"(CH3)2(CH2)4"` returns `{"C":6.0, "H":14.0}`
    - Note: chemparse currently only handles non-nested paretheses. A formula with nested parentheses like `"CH3(C2(CH3)2)3CH3"` will not work properly.

## Installation

Install `chemparse` with pip:

```
$ pip install chemparse
```

## Usage

Import chemparse in python and use the parse_formula function:

```
import chemparse

print(chemparse.parse_formula("C6H12O6"))
```