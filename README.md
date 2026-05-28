# QuantLibXlOil

[![Documentation](https://img.shields.io/badge/Documentation-dev-blue)](https://frame-consulting.github.io/QuantLibXlOil/)

QuantLibXlOil is an interface package to make functions of the open-source [QuantLib](https://github.com/lballabio/QuantLib) pricing library available in Excel.

The interface builds on the Python bindings for QuantLib via [QuantLib-SWIG](https://github.com/lballabio/QuantLib-SWIG).

We use [xlOil](https://github.com/cunnane/xloil) to make the QuantLib Python objects and functions available in Excel.

The QuantLibXlOil package largely contains wrapper functions in Python which delegate calls to QuantLib constructors and method/function call. The wrapper functions are made available to Excel via xlOil's function decorator. In addition, the package provides converter functions between Excel data types and QuantLib types.

## Getting Started

QuantLibXlOil can be installed via pip.

**Note:** Remove any installation of the classical QuantLib Excel add-in if installed prior to installing QuantLibXlOil.


### Setup Python Environment

We recommend setting up a clean Python environment with `conda` (or `venv`).

```
conda create -n xloil python
conda activate xloil
```

### Install QuantLibXlOil and Dependencies

QuantLibXlOil is available via pip.

```
pip install quantlib_xloil
```

This step also installs the following dependencies:

- xlOil for interfacing Python and Excel.
- QuantLib library with Python interface.

### Install xlOil Excel Add-in

xlOil comes with an installer script which can be run on the command line within the Python environment.

```
xloil install
```

Above step installs the xlOil Excel add-in and an `xlOil.ini` configuration file. Details on xlOil installation can also be found [here](https://xloil.readthedocs.io/en/stable/xlOil_Python/GettingStarted.html#introduction).

Installation can be verified by opening Excel with a blank workbook. Type `=xloVersion()` in an empty cell and enter. This should display an output similar to the one below.

| <!-- --> | <!-- -->      |
|----------|---------------|
|Version   |  0.22.99      |
|BuildDate | "May 22 2026" |

### Load QuantLibXlOil Functions

To make the QuantLib wrapper functions available in Excel, the xlOil add-in needs to be configured.

xlOil comes with a custom menu ribbon *xlOil Py*. The menu block *Modules* contains a text input field *Load Modules*.

Add `QuantLib_xlOil` to the text field *Load Modules*. Use comma separation without spaces. The resulting entry in *Load Modules* should be

```
xloil.xloil_ribbon,QuantLib_xlOil
```

Restart Excel and open a blank workbook.

Test the QuantLib functions by entering `=qlVersion()` in an empty cell. This should produce a result like `1.41`.

Now, you are all set for QuantLib in Excel.


## Why Another QuantLib Interface?

Excel is widely adapted in the industry as calculation tool and GUI for a large variety of use cases.

QuantLib has the classical [QuantLibXL](https://www.quantlib.org/quantlibxl/) interface for Excel. However, QuantLibXL was last updated for QuantLib v1.22 (April 2021). The QuantLibXL object and interface specification is quite complex and closely linked to QuantLib internals. This makes maintenance quite challenging.

The QuantLib Python interface is probably the best QuantLib interface in terms of coverage and maintenance. With the QuantLibXlOil package, we aim at leveraging the matured QuantLib Python interface.

As an additional objective, we want to disentangle QuantLib developments from Excel interface development. This is particularly relevant for QuantLib C++ internals. For example, switching from `boost::something` to `std::something` should not affect the Excel interface. This motivates building on top of an existing high-level language interface.

Linking between Python and Excel is a well understood task. There are [several tools](https://xloil.readthedocs.io/en/stable/Introduction.html#why-xloil-was-created) that implement that bridge. We opt for xlOil because it is open-source and works well for the use cases tested.
