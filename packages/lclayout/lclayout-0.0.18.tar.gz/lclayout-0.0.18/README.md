<!--
SPDX-FileCopyrightText: 2022 Thomas Kramer

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# LibreCell
LibreCell aims to be a toolbox for automated synthesis of CMOS logic cells.

LibreCell is structured in multiple sub-projects:
* [librecell-layout](https://codeberg.org/librecell/lclayout): Automated layout generator for CMOS standard cells.
* [lctime](https://codeberg.org/librecell/lctime): Characterization kit for CMOS cells and tool for handling liberty files.

The project is in a very early stage and might not yet be ready for productive use.
Project structure and API might change heavily in near future.

### Getting started
LibreCell can be installed using the Python package manager `pip` or directly from the git repository.

#### Dependencies
The following dependencies must be installed manually:
* python3
* z3 https://github.com/Z3Prover/z3 : SMT solver.

Optional dependencies (not required for default configuration):
* GLPK https://www.gnu.org/software/glpk : ILP/MIP solver

Depending on your linux distribution this packages can be installed using the package manager.

#### Installing from git
It is recommended to use a Python 'virtual environment' for installing all Python dependencies:
```sh
# Create a new virtual environment
python3 -m venv my-librecell-env
# Activate the virtual environment
source ./my-librecell-env/bin/activate
```

Install from git:
```sh
git clone https://codeberg.org/tok/librecell.git
cd librecell
./install.sh

# Alternatively use ./install_develop.sh to install symlinks.
# This allows to edit the code with immediate effect on the installed program.
```

Now, check if the command-line scripts are in the current search path:
```sh
lclayout --help
```
If this shows the documentation of the `lclayout` command, then things are fine. Otherwise, the `PATH` environment variable needs to be updated to include `$HOME/.local/bin`.

```sh
# Instead of executing this line each time it can be added to ~/.bashrc
export PATH=$PATH:$HOME/.local/bin
```

#### Installing with pip
*Note*: The version PyPI is often not the most recent one. Consider installing from git to get the most recent version.

It is recommended to use a Python 'virtual environment' for installing all Python dependencies:
```sh
# Create a new virtual environment
python3 -m venv my-librecell-env
# Activate the virtual environment
source ./my-librecell-env/bin/activate

pip3 install lclayout
```

### Generate a layout
Generate a layout from a SPICE netlist which includes the transistor sizes:
* --output-dir: Directory which will be used to store GDS and LEF of the cell
* --tech: Python script file containing design rules and technology related data
* --netlist: A SPICE netlist containing the netlist of the cell as a sub circuit (`.subckt`).
* --cell: Name of the cell. Must match the name of the sub circuit in the SPICE netlist.

```sh
mkdir mylibrary
lclayout --output-dir mylibrary --tech examples/dummy_tech.py --netlist examples/cells.sp --cell AND2X1
```

## Adapting design rules
Design rulesi and technology related data need to be encoded in a Python script file as shown in `examples/dummy_tech.py`.

### Known issues

#### Reproducibility
You may want to generate standard cells in a fully reproducable manner.
Right now there is some non-determinism in LibreCell that has not been investigated yet.
The current workaround is to set the `PYTHONHASHSEED` environment variable.

```sh
export PYTHONHASHSEED=42
lclayout ...
```

## Contact
```python
"codextkramerych".replace("x", "@").replace("y", ".")
```
