# chemparse

**Authors:** Grayson Boyer and Victor Ignatenko

A lightweight package for parsing chemical formula strings into python dictionaries. 

## Features

* Convert a chemical formula string into a python dictionary.
    - example: `"CH4"` returns `{"C":1.0, "H":4.0}`
* Handles fractional stoichiometry.
    - example: `"C1.5O3"` returns `{"C":1.5, "O":3.0}`
    - example: `"H2e-1O1e-1"` returns `{"H":0.2, "O":0.1}`
* Handles groups with parentheses.
    - example: `"(CH3)2(CH2)4"` returns `{"C":6.0, "H":14.0}`
* **New in 2024:** Chemparse now handles nested paretheses!
    - example: `"((CH3)2)3"` returns `{'C': 6, 'H': 18}`
* **New in 2024:** Chemparse now handles square brackets
    - example: `"K4[Fe(SCN)6]"` returns `{'Fe': 1.0, 'K': 4.0, 'N': 6.0, 'S': 6.0, 'C': 6.0}`

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

## Contribute

Install python

Clone `chemparse` using git: \
`git clone https://github.com/gmboyer/chemparse.git`

Go to the `chemparse` directory: \
`cd chemparse`

Install requirements: \
`pip install -r requirements.txt`

Now you are ready to contribute!