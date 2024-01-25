# Twissed

## Overview

Twissed is a Python package 🐍 that provides a large number of data analysis tools for **beam dynamics** and **laser wakefield acceleration** simulations.

Twissed is multi-OS (Windows, Linux, Mac) and can be easily installed everywhere thanks to its low number of dependencies (numpy, pandas, scipy, h5py). It is especially made to run on HPC clusters. 

Twissed can read and write data from several sources

* [FBPIC](https://fbpic.github.io/)
* [Smilei](https://smileipic.github.io/Smilei/)
* [Smilei via happi package](https://smileipic.github.io/Smilei/)
* [TraceWin](https://dacm-logiciels.fr/)
* [Astra]()

## Installation
### Requirement

Python 3.7 or greater

* Mandatory packages: numpy pandas scipy h5py. 
* Optional packages: matplotlib seaborn happi(smilei)

### Installation

After downloading the project:

* Mac OS/Linux
```shell
python -m pip install -e .
```

* Windows
```shell
py -m pip install -e .
```

## Tutorial

Examples Twissed use are available at https://github.com/Twissed/Twissed_tutorial