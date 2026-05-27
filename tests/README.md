# Unit Test Suite

This folder contains test cases for the project code.

We use *unit tests* and Excel *workbook tests*. Unit tests are stored in folder `tests/unittests`. Workbook tests are stored in folder `tests/workbooks`.

We use `pytest` as test framework for unit tests. Test automation for workbook tests is tbd.

## Test File Names

Test file names are of the form `test_sourcefilename.py` and analogously for workbook tests.

Here, `test_` is a fixed and common prefix. The part `sourcefilename` mirrors the file name of the source code being tested.

## Unit Test Case Specification

Unit test cases are formulated for individual source functions.

Each unit test case is implemented by a function of the following form.

```
def test_qlFunctionName():
    import QuantLib as ql
    from quantlib_xloil import qlFunctionName, ...
    ...
    assert ...
```

Function name prefix is `test_`. The part `qlFunctionName` corresponds to the name of the source function being tested.
 
## Workbook Test Case Specification

Workbook test cases are formulated for individual source functions.

Each workbook test case is implemented by one or more cell function calls `=qlFunctionName(...)`. Function calls should be grouped by function name on individual Worksheets. The Worksheet name is set to the function name tested.

Inputs should be provided in separate cells with description and be references by the test case function calls.

Inputs and function calls should be placed in the upper left part of the sheet.
