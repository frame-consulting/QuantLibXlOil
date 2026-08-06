---
name: add-interface-file

description: Add a new interface file to the project or extend the existing interface file with new functions. Use this skill when asked to add new wrapper functions for a QuantLib-SWIG interface file to the QuantLibXlOil project.

---


Read the `README.md` file in the project root directory for more information on the QuantLibXlOil project.

Identify the interface file from the user prompt and store it in a variable `interface_file`. If the interface file is not specified, stop the execution and ask the user to provide the interface file name.

Identify the QuantLib version by running the following script:

```python
import QuantLib
print(QuantLib.__version__)
```

Store the QuantLib version in a variable `quantlib_version`.

Read the QuantLib-SWIG interface specifications from the `QuantLib-SWIG` repository for the specified version. You can find the interface specifications in the `QuantLib-SWIG` repository on GitHub: https://github.com/lballabio/QuantLib-SWIG/tree/`swig_version`/SWIG/

The interface specifications are defined in the `*.i` files in the `SWIG` directory.

The relevant interface file for this skill is `interface_file` with `*.i` file extension, which is located in the `SWIG` directory of the QuantLib-SWIG repository.

Consider only interface specifications for Python or for all platforms. The interface specifications for Python are marked with the `#if defined(SWIGPYTHON)` directive in the SWIG interface files.

QuantLibXlOil interface files are located in the folder `src/quantlib_xloil/`. Read the coding guidelines from the file `src/quantlib_xloil/README.md`.

Create a new interface file in the folder `src/quantlib_xloil/` with the name `interface_file` and the file extension `.py`. If the interface file already exists, extend it with new functions.

Add new wrapper functions for QuantLib object creation and method calls to the interface file. The wrapper functions should follow follow the patterns used in the existing interface files and the coding guidelines specified in the `src/quantlib_xloil/README.md` file.

Python unit tests for the project are located in the folder `tests/unittests/`. The unit tests are organized in files named `test_*.py`, where `*` corresponds to the name of the interface file being tested.

Add new unit tests for the new wrapper functions in the interface file. The unit tests should follow the patterns used in the existing unit test files and the guidelines specified in the file `tests/README.md`.

Test the new wrapper functions and unit tests to ensure they work correctly and pass all tests. For test execution, use Windows CMD prompt and Python from the conda environment `xloil`. Do not attempt to run the tests with bash or zsh shells as they do not work with the conda environment.

Do not attempt to implement workbook tests in the folder `tests/workbooktests/` as they are not required for this skill.

Create a git commit with the message "Add new interface file `interface_file`" or "Extend existing interface file `interface_file`" depending on whether the interface file was created or extended. Add to the commit message a brief description of the new functions added to the interface file.
