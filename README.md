# QuantLibXlOil

[![CI](https://github.com/frame-consulting/QuantLibXlOil/actions/workflows/ci.yml/badge.svg)](https://github.com/frame-consulting/QuantLibXlOil/actions/workflows/ci.yml)

[![Documentation](https://img.shields.io/badge/Documentation-dev-blue)](https://frame-consulting.github.io/QuantLibXlOil/)

QuantLibXlOil is an interface package to make functions of the open-source [QuantLib](https://github.com/lballabio/QuantLib) pricing library available in Excel.

The interface builds on the Python bindings for QuantLib via [QuantLib-SWIG](https://github.com/lballabio/QuantLib-SWIG).

We use [xlOil](https://github.com/cunnane/xloil) to make the QuantLib Python objects and functions available in Excel.

The QuantLibXlOil package largely contains wrapper functions in Python which delegate calls to QuantLib constructors and method/function call. The wrapper functions are made available to Excel via xlOil's function decorator. In addition, the package provides converter functions between Excel data types and QuantLib types.

We support recent versions of QuantLib. See section [Versioning](#versioning).

## Getting Started

QuantLibXlOil can be installed via pip.

**Note:** Remove any installation of the classical QuantLib Excel add-in if installed prior to installing QuantLibXlOil.


### Setup Python Environment

We recommend setting up a clean Python environment with [`conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) (or `venv`).

```
conda create -n xloil python
conda activate xloil
```

### Install QuantLibXlOil and Dependencies

QuantLibXlOil is available via pip.

```
pip install -U quantlib_xloil
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

![image](./docs/source/xloVersion.png)

### Load QuantLibXlOil Functions

To make the QuantLib wrapper functions available in Excel, the xlOil add-in needs to be configured.

xlOil comes with a custom menu ribbon *xlOil Py*. The menu block *Modules* contains a text input field *Load Modules*.

Add `QuantLib_xlOil` to the text field *Load Modules*. Use comma separation without spaces. The resulting entry in *Load Modules* should be

```
xloil.xloil_ribbon,QuantLib_xlOil
```

![image](./docs/source/xloil_load_modules.png)

Restart Excel and open a blank workbook.

Test the QuantLib functions by entering `=qlVersion()` in an empty cell. This should produce a result like `1.41`.

![image](./docs/source/qlVersion.png)

Now, you are all set for QuantLib in Excel.

## Examples

An illustrative example of QuantLib in Excel is provided via the [interest rate derivatives sheet](./tests/workbooktests/workbooks/extras/example_interest_rate_derivatives.xlsx). You can download the sheet using the *Download raw file* icon.

![image](./docs/source/example_interest_rate_derivatives.png)

A comprehensive list of examples are specified in the [workbook test sheets](./tests/workbooktests/workbooks/) folder.

## QuantLib Functions and Function Arguments

A list of available QuantLib functions and links to their implementation can be queried in Excel via `=qlListFunctions()`.

![image](./docs/source/qlListFunctions.png)

Many QuantLib function arguments encode QuantLib enumerations or *enumerated* classes. Examples are business day conventions and day counters.

QuantLib enumerations and *enumerated* classes are represented as strings organised via dictionaries in QuantLibXlOil. A list of dictionaries and links to their implementation can be viewed in Excel via `=qlListDictionaries()`.

![image](./docs/source/qlListDictionaries.png)

For each dictionary, the entries can be inspected via `qlListDictionaryEntries(...)`

![image](./docs/source/qlListDictionaryEntries.png)

For above `QL_DAYCOUNTER` example, some string keys are mapped directly to QuantLib classes. Other classes, that need additional parameters to construct objects, are wrapped in lambda expressions which do not give a sensible output here. Please check the source code to see the actual QuantLib implementation.


## QuantLib Objects in Excel

Return values of QuantLib functions can be of basic type (string, integer, float and boolean) or complex type. Results of basic types are represented directly in the Excel cell.

Results which are list-like objects are unpacked and the elements of the list are shown in the Excel cells.

Complex result types are, for example, QuantLib classes. Such results are stored in an xlOil object repository. The return value is a string with a reference to the QuantLib object in the repository.

![image](./docs/source/qlEstr.png)

xlOil uses a particular [methodology](https://xloil.readthedocs.io/en/stable/xlOil_Python/TypeConversion.html#cached-objects) to compose and resolve the object references. In particular, the Mandarin xīn symbol 欣 (*happy, joyful*) is used to identify cache strings.

Such cache strings can be passed as arguments back in QuantLib functions. xlOil resolves the corresponding object and passes it to the function in Python.

An approach for more user-friendly object reference names is documented [here](./docs/source/40_quantlib_xloil_extras.md#alias-repository).

## Versioning

Current QuantLibXlOil version is specified [here](./src/quantlib_xloil/__about__.py).

We use a major version `0` for the time being until interfaces are well tested, coverage is sufficiently high and our upgrade process to new QuantLib versions works smoothly.

Minor versions are aligned with the QuantLib minor version supported. That is, QuantLibXlOil `v0.41` works with QuantLib `v1.41`. Similarly, QuantLibXlOil `v0.42` works with QuantLib `v1.42`.

QuantLibXlOil patch versions are used to capture bug fixes and new features for a QuantLib version specified by the minor version.

The QuantLib version supported by a given QuantLibXlOil version is installed automatically as [dependency](./pyproject.toml) when running `pip install -U quantlib_xloil`.


## Why Another QuantLib Interface?

Excel is widely adapted in the industry as calculation tool and GUI for a large variety of use cases.

QuantLib has the classical [QuantLibXL](https://www.quantlib.org/quantlibxl/) interface for Excel. However, QuantLibXL was last updated for QuantLib v1.22 (April 2021). The QuantLibXL object and interface specification is quite complex and closely linked to QuantLib internals. This makes maintenance quite challenging.

The QuantLib Python interface is probably the best QuantLib interface in terms of coverage and maintenance. With the QuantLibXlOil package, we aim at leveraging the matured QuantLib Python interface.

As an additional objective, we want to disentangle QuantLib developments from Excel interface development. This is particularly relevant for QuantLib C++ internals. For example, switching from `boost::something` to `std::something` should not affect the Excel interface. This motivates building on top of an existing high-level language interface.

Linking between Python and Excel is a well understood task. There are [several tools](https://xloil.readthedocs.io/en/stable/Introduction.html#why-xloil-was-created) that implement that bridge. We opt for xlOil because it is open-source and works well for the use cases tested.
