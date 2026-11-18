# Contributing to QuantLibXlOil

We encourage contributions to the package to increase coverage, fix issues and improve tests and documentation.

In this section, we explain the workflow for contributing to the QuantLibXlOil package.

Please read the coding guides [here](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/README.md) and the test case guide [here](https://github.com/frame-consulting/QuantLibXlOil/blob/main/tests/README.md).
 
1.  Uninstall any pre-installed QuantLibXlOil package from the Python environment

    ```
    pip uninstall quantlib_xloil
    ```

    Make sure xlOil remains installed in the Python environment. 

1.  Fork the repository on GitHub.

1.  Clone the forked repository.

    ```
    git clone https://github.com/[your-username]/QuantLibXlOil
    ```
 
1.  Add source path 

    ```
    C:\[...]\QuantLibXlOil\src
    ```

    to Excel / xlOil Py / Modules / Search Paths.

    Make sure Excel / xlOil Py / Modules / Load Modules contains the `QuantLib_xlOil` entry.

1.  Add an example function and double-check that you can access it from Excel.

1.  Implement a new feature.

    1. Add wrapper code to `C:\[...]\QuantLibXlOil\src`.

    1. Add unit tests to `C:\[...]\QuantLibXlOil\tests\unittests`.

    1. Add a test workbook to `C:\[...]\QuantLibXlOil\tests\workbooks`.

1.  Push changes to your GitHub repository.

1.  Create a pull request.
