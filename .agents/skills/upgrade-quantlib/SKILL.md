---
name: upgrade-quantlib

description: Upgrade wrapper functions and add new wrapper functions for using a new version of QuantLib in the QuantLibXlOil project. Use this skill when asked to upgrade the QuantLib version used in the QuantLibXlOil project.
---

# Upgrade QuantLib

Follow exactly the steps below to upgrade the QuantLib version used in the QuantLibXlOil project. This skill will help you identify changes in the QuantLib-SWIG repository and update the wrapper functions accordingly.

## Tools Required

Python code must be run in the conda environment `xloil`.

If using `bash`, activate the conda environment `xloil` using the following command:

```bash
source C:/ProgramData/miniconda3/etc/profile.d/conda.sh && conda activate xloil
```

If using `cmd`, activate the conda environment `xloil` using the following command:

```cmd
C:\ProgramData\miniconda3\Scripts\activate.bat && conda activate xloil
```

If you cannot activate the conda environment `xloil`, you must stop the execution and ask the user to provide the conda environment `xloil` before proceeding.

To run python code in the conda environment `xloil`, use the following command:

If using `bash`, run the following command:

```bash
python source C:/ProgramData/miniconda3/etc/profile.d/conda.sh && conda activate xloil && python <python_code>
```

If using `cmd`, run the following command:

```cmd
C:\ProgramData\miniconda3\Scripts\activate.bat && conda activate xloil && python <python_code>
```


## Prerequisites

Read the `README.md` file in the project root directory for more information on the QuantLibXlOil project.

Identify the current QuantLib version from the user prompt and store it in a variable `current_quantlib_version`. If the current QuantLib version is not specified, stop the execution and ask the user to provide the current QuantLib version.

Identify the new QuantLib version from the user prompt and store it in a variable `new_quantlib_version`. If the new QuantLib version is not specified, stop the execution and ask the user to provide the new QuantLib version.

Identify the QuantLib version currently installed.

If using `bash`, run the following command:

```bash
source C:/ProgramData/miniconda3/etc/profile.d/conda.sh && conda activate xloil && python -c 'import QuantLib; print(QuantLib.__version__)'
```

if using `cmd`, run the following command:

```cmd
C:\ProgramData\miniconda3\Scripts\activate.bat && conda activate xloil && python -c "import QuantLib; print(QuantLib.__version__)"
```

Store the QuantLib version in a variable `installed_quantlib_version`.

Verify that the `installed_quantlib_version` in the conda environment `xloil` matches the `new_quantlib_version`. This is required to allow testing the added and updated wrapper functions against the new QuantLib version.

If `installed_quantlib_version` does not match `new_quantlib_version`, stop the execution and ask the user to install QuantLib `new_quantlib_version` in the `xloil` conda environment or provide a conda environment where QuantLib `new_quantlib_version` is installed.

Create a message for the user indicating that the QuantLib version will be upgraded from `current_quantlib_version` to `new_quantlib_version`.


## Identify Changes in QuantLib-SWIG

From the project root directory, navigate to the `.qlswig/QuantLib-SWIG` directory.

Execute the following command to list all new SWIG files and modified SWIG files in the QuantLib-SWIG repository between the `current_quantlib_version` and `new_quantlib_version`:

```bash
git diff --name-only current_quantlib_version new_quantlib_version SWIG/*.i
```

Store the list of new and modified SWIG files in a variable `swig_changes`.


## Upgrade Wrapper Functions

Wrapper functions are implemented in the Python files located in the folder `src/quantlib_xloil/`. Typically, the swig file name corresponds to the Python file name. For example, the wrapper functions for `SWIG/options.i` are implemented in `src/quantlib_xloil/options.py`. There is the following exception: the wrapper functions for
- `SWIG/discountcurve.i,
- `SWIG/forwardcurve.i, and
- `SWIG/zerocurve.i`
are implemented in `src/quantlib_xloil/interpolatedyieldcurves.py`.

Unit tests for the wrapper functions are implemented in the Python files located in the folder `tests/unittests/`. The Python wrapper file name corresponds to the test file name. For example, the unit tests for `src/quantlib_xloil/options.py` are implemented in `tests/unittests/test_options.py`.

New wrapper functions should follow the patterns used in the wrapper function files and the coding guidelines specified in the  file `src/quantlib_xloil/README.md`.


Iterate through each SWIG file in `swig_changes` and perform the following steps:

1. From the project root directory, navigate to the `.qlswig/QuantLib-SWIG` directory. Run the following command to identify the changes in the SWIG file between the `current_quantlib_version` and `new_quantlib_version`:

```bash
git diff current_quantlib_version new_quantlib_version SWIG/<swig_file>
```

2. Store the output of the command in a variable `swig_diff`.

3. Read the corresponding Python file in `src/quantlib_xloil/` and identify the wrapper functions that need to be added, removed or updated based on the changes in `swig_diff`. Store the list of wrapper functions to be added, removed or updated in a variable `wrapper_functions_to_change`.

4. Update the corresponding Python file in `src/quantlib_xloil/` with the changes in `wrapper_functions_to_change`. If new wrapper functions are added, ensure that they follow the patterns used in the existing wrapper function files and the coding guidelines specified in the file `src/quantlib_xloil/README.md`.

5. Update the corresponding unit test file in `tests/unittests/` with new unit tests for the new wrapper functions. Ensure that the unit tests follow the patterns used in the existing unit test files and the guidelines specified in the file `tests/README.md`.

6. After updating the wrapper functions and unit tests, run the unit tests to verify that the changes are correct and do not break existing functionality. If any unit tests fail and cannot be fixed, stop the execution and ask the user to fix the issues before proceeding.


After iterating through all SWIG files in `swig_changes`, generate a summary message for the user indicating the changes that have been made to the wrapper functions. Save  the summary message in the file `UpgradeSummary.md` in the project root directory. The summary message should include the following information:
- The list of SWIG files that were changed.
- The list of wrapper functions that were added, removed or updated.
- The list of unit tests that were added, removed or updated.

Stop the execution and ask the user to review the changes in the `UpgradeSummary.md`.
