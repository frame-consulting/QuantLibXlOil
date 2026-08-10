---
name: upgrade-quantlib

description: Upgrade the QuantLibXlOil project to use a new QuantLib version by updating and adding wrapper functions. Use this skill when asked to upgrade the QuantLib version used in the QuantLibXlOil project.
---

# Upgrade QuantLib

Use this skill when the user wants to upgrade the QuantLib version used by QuantLibXlOil. Follow the steps in order. If information or dependencies are missing, stop and ask the user instead of guessing.

## Required setup

Run Python in the conda environment named `xloil`.

Unless otherwise specified, use `bash` syntax for all commands. If the active terminal is `cmd`, replace `bash` blocks with the equivalent `cmd` syntax provided below.

- For `bash`, activate the environment with:

```bash
source C:/ProgramData/miniconda3/etc/profile.d/conda.sh && conda activate xloil
```

- For `cmd`, activate the environment with:

```cmd
C:\ProgramData\miniconda3\Scripts\activate.bat && conda activate xloil
```

If the environment cannot be activated, stop and ask the user to provide or create the `xloil` environment before continuing.

After activation, run Python commands inline (e.g., `python -c "import QuantLib; print(QuantLib.__version__)"`) or via script files (`python <script.py>`).

## Required inputs

1. Read the project README at the repository root to understand the project layout and expected workflow.
2. Confirm that the repository root is the current working directory.
3. Obtain `new_quantlib_version` from the user's request. If it is missing, stop and ask the user for it.
4. Check the installed QuantLib version in the `xloil` environment:

   - For `bash`, run:

```bash
source C:/ProgramData/miniconda3/etc/profile.d/conda.sh && conda activate xloil && python -c 'import QuantLib; print(QuantLib.__version__)'
```

   - For `cmd`, run:

```cmd
C:\ProgramData\miniconda3\Scripts\activate.bat && conda activate xloil && python -c "import QuantLib; print(QuantLib.__version__)"
```

   Store the result in `installed_quantlib_version`. If this fails (e.g., QuantLib is not installed), set `installed_quantlib_version` to `None`.
5. Determine `current_quantlib_version`:
   - If the user explicitly provided it, use that value.
   - Otherwise, use `installed_quantlib_version`.
   - If neither is available, stop and ask the user to provide `current_quantlib_version`.
6. Confirm that the QuantLib-SWIG repository exists at `.qlswig/QuantLib-SWIG`.
   - If it does not exist, stop and ask the user to clone it or provide its location.
   - Verify that both `current_quantlib_version` and `new_quantlib_version` are valid git tags, branches, or commit hashes in that repository.
   - If either version is not a valid git reference, stop and ask the user to correct it.

**Note**: In all commands below, replace placeholder variables (e.g., `current_quantlib_version`, `new_quantlib_version`, `<swig_file>`, `<module>`) with their actual values.
7. Verify that `installed_quantlib_version` matches `new_quantlib_version`.
   - If it does not, stop and ask the user to install QuantLib `new_quantlib_version` in the `xloil` environment or to provide a different environment that already has it.
8. Tell the user that the upgrade is planned from `current_quantlib_version` to `new_quantlib_version`.

## Identify changes in QuantLib-SWIG

1. Change to the project root if needed, then enter `.qlswig/QuantLib-SWIG`.
2. Run the following command to list changed SWIG interface files between the two versions (replace placeholders with actual values):

```bash
git diff --name-status current_quantlib_version new_quantlib_version -- SWIG/*.i
```

3. Store the resulting file list (including added, modified, and removed files) in `swig_changes`.
4. If `swig_changes` is empty, inspect the broader diff for non-SWIG changes that could still affect wrappers, such as QuantLib-SWIG C++ headers or related interface files.
   - Run (replace placeholders): `git diff --name-status current_quantlib_version new_quantlib_version`
   - If there are no relevant changes to SWIG interfaces or wrapper-related code, stop and ask the user whether to proceed with no wrapper updates.
   - Do not invent wrapper updates when there is no evidence that the upgrade affects the wrapper layer.

## Update wrapper functions and tests

Wrapper modules are implemented in `src/quantlib_xloil/`. Unit tests live in `tests/unittests/`.

### SWIG-to-Wrapper Mapping

The mapping from SWIG interface files to Python wrapper modules is usually one-to-one by module name (e.g., `SWIG/foo.i` → `src/quantlib_xloil/foo.py`). Known exceptions:

| SWIG File | Wrapper Module |
|-----------|----------------|
| `SWIG/discountcurve.i` | `src/quantlib_xloil/interpolatedyieldcurves.py` |
| `SWIG/forwardcurve.i` | `src/quantlib_xloil/interpolatedyieldcurves.py` |
| `SWIG/zerocurve.i` | `src/quantlib_xloil/interpolatedyieldcurves.py` |

If a SWIG file does not have an obvious corresponding wrapper module, search `src/quantlib_xloil/` for references to the SWIG file name or its classes/functions to identify the correct mapping. If no mapping exists, ask the user to confirm.

Before editing, inspect the existing wrapper module and the matching test file for naming patterns and style. Follow the coding guidelines in `src/quantlib_xloil/README.md` and `tests/README.md`. If these files are missing, follow the existing code style in the repository.

For each SWIG file listed in `swig_changes`, perform the following steps:

1. Inspect the diff for that file with (replace placeholders with actual values):

```bash
git diff current_quantlib_version new_quantlib_version -- SWIG/<swig_file>
```

2. Determine whether the file was added, modified, or removed.
3. Map the SWIG file to the corresponding wrapper module using the rules above.
4. Take action based on the SWIG file status:
   - **Added or modified**: Update the existing wrapper module or create a new one following existing patterns.
   - **Removed**: Mark the corresponding wrapper functions or classes as deprecated in the wrapper module. Remove them only if the user confirms that removal is intended or if the symbols are no longer used anywhere in the repository.
5. Maintain an internal list `wrapper_functions_to_change` tracking all wrapper functions or classes that are added, removed, or updated. This is only for the summary and does not need to be stored in a file.
6. Update or add unit tests in the matching test module (for example, `tests/unittests/test_<module>.py`). If no matching test module exists, create one following the structure of existing test files in `tests/unittests/` (e.g., `test_<existing_module>.py`).
7. Run all tests for the affected module with (replace `<module>` with the actual module name):
   ```bash
   pytest tests/unittests/test_<module>.py -v
   ```
   If tests fail and the failure is not caused by the local environment (e.g., missing dependencies), fix the issue. Otherwise, stop and ask the user for help.

## Finish the upgrade

After all SWIG files have been processed:

1. Write a summary to `UpgradeSummary.md` in the repository root. Use the following markdown template:

```markdown
# QuantLib Upgrade Summary

- **From Version**: `current_quantlib_version`
- **To Version**: `new_quantlib_version`

## SWIG Interface Changes
- Added: `<list of added SWIG files>`
- Modified: `<list of modified SWIG files>`
- Removed: `<list of removed SWIG files>`

## Wrapper Module Changes
- Added: `<list of new wrapper modules>`
- Modified: `<list of updated wrapper modules>`
- Removed/Deprecated: `<list of deprecated or removed wrapper modules>`

## Test Changes
- Added: `<list of new test modules>`
- Modified: `<list of updated test modules>`
- Removed: `<list of removed test modules>`
```

Populate the template with the actual changes made. Include specific function/class names where relevant.

2. Stop and ask the user to review the summary and the edited files.
