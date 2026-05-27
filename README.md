# QuantLibXlOil

QuantLibXlOil is an interface package to make functions of the open-source [QuantLib](https://github.com/lballabio/QuantLib) pricing library available in Excel.

The interface builds on the Python bindings for QuantLib via [QuantLib-SWIG](https://github.com/lballabio/QuantLib-SWIG).

We use [xlOil](https://github.com/cunnane/xloil) to make the QuantLib Python objects and functions available in Excel.

The QuantLibXlOil package largely contains wrapper functions in Python which delegate calls to QuantLib constructors and method/function call. The wrapper functions are made available to Excel via xlOil's function decorator. In addition, the package provides converter functions between Excel data types and QuantLib types.

## Why Another QuantLib Interface?

Excel is widely adapted in the industry as calculation tool and GUI for a large variety of use cases.

QuantLib has the classical [QuantLibXL](https://www.quantlib.org/quantlibxl/) interface for Excel. However, QuantLibXL was last updated for QuantLib v1.22 (April 2021). The QuantLibXL object and interface specification is quite complex and closely linked to QuantLib internals. This makes maintenance quite challenging.

The QuantLib Python interface is probably the best QuantLib interface in terms of coverage and maintenance. With the QuantLibXlOil package, we aim at leveraging the matured QuantLib Python interface.

As an additional objective, we want to disentangle QuantLib developments from Excel interface development. This is particularly relevant for QuantLib C++ internals. For example, switching from `boost::something` to `std::something` should not affect the Excel interface. This motivates building on top of an existing high-level language interface.

Linking between Python and Excel is a well understood task. There are [several tools](https://xloil.readthedocs.io/en/stable/Introduction.html#why-xloil-was-created) that implement that bridge. We opt for xlOil because it is open-source and works well for the use cases tested.

## Getting Started

The manual way...

### Setup Python Environment

Set up a Python environment via `conda` or `pip` and with the following packages:

- `quanlib-python`,
- `numpy`,
- `pandas` (Version 2).

### Install xlOil

xlOil is available via pip and `pip install xloil`.

Install the xlOil Excel add-in by running `xloil install` from the command line of the Python environment.

Open Excel and create a new Workbook. The *xlOil Py* add-in should appear as a new ribbon.

Navigate to the *xlOil Py* ribbon and select the Python environment with `xloil` package installed in the *Environment* drop-down menu.

Run `=xloVersion()` in a Workbook cell. This should output version and build date details in the Excel cells.

Details on getting started with xlOil are documented [here](https://xloil.readthedocs.io/en/stable/xlOil_Python/GettingStarted.html#getting-started).

### Install QuantLibXlOil

Clone the QuantLibXlOil repository.

Add the complete path to `C:\...\QuantLibXlOil\src\` in the *Search Path* tet field.

Add `quantlib_xloil` to the *Load Modules* text field. Use comma separator and *no* blanks. The resulting input of the *Load Modules* text field should then be:

```
xloil.xloil_ribbon,quantlib_xloil
```

Restart Excel and open a blank Workbook.

Now, the QuantLibXlOil functions should be available in Excel.

Test the QuantLibXlOil functions by typing `=qlVersion()` in an empty cell. This should give the QuantLib version number.

