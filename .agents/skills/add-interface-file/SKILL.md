---
name: add-interface-file

description: Add a new interface file to the project or extend the existing interface file with new functions. Use this skill when asked to add new wrapper functions for a QuantLib-SWIG interface file to the QuantLibXlOil project.

---

# Add or Extend an Interface Wrapper

Use this skill to add QuantLib-SWIG wrappers to QuantLibXlOil. Follow the sequence
below. Stop and ask the user when a required input, environment, or source reference is
missing; do not guess.

## Inputs and source version

1. Read `README.md`, `src/quantlib_xloil/README.md`, and `tests/README.md`.
2. Obtain `interface_file` from the user. Accept `foo` or `foo.i`; normalize to
   `foo.i` for SWIG and `foo` for Python. If absent, stop and ask.
3. Use a **CMD terminal** for all environment and test commands. Do not nest CMD in
   PowerShell, mix shell separators, or redirect output to temporary files.

   ```cmd
   call C:\ProgramData\miniconda3\Scripts\activate.bat && conda activate xloil && python -c "import QuantLib; print(QuantLib.__version__)"
   ```

   Store the output as `quantlib_version`. If it fails, stop and ask the user to repair
   or locate the `xloil` environment.
4. Confirm `.qlswig\QuantLib-SWIG` exists and is a Git worktree. It is the source of
   truth for SWIG specifications.
5. Resolve `swig_version` from `quantlib_version` as the matching tag
   `v<quantlib_version>` (for example, QuantLib `1.42.1` uses SWIG `v1.42.1`). Verify
   it without CMD's caret-sensitive revision syntax:

   ```cmd
   git -C .qlswig\QuantLib-SWIG show-ref --tags --verify refs/tags/v<quantlib_version>
   ```

   If the tag is missing, stop and ask the user for the compatible SWIG reference. Keep
   the chosen reference fixed for the remainder of the task.
6. Tell the user the normalized interface and QuantLib/SWIG versions before editing.

## Inspect and implement

1. Read the specification directly from the pinned tag:

   ```cmd
   git -C .qlswig\QuantLib-SWIG show v<quantlib_version>:SWIG/interface_file
   ```

   If it is absent, stop and ask the user to confirm the interface or reference.
2. Consider shared declarations and `#if defined(SWIGPYTHON)` declarations only. Do
   not wrap declarations restricted to another language.
3. Select useful constructors and method/function calls; do not mechanically wrap every
   declaration. Verify uncertain constructors, defaults, enums, handles, and engine
   pairings against the live Python binding in `xloil` before editing.
4. Map the specification to `src/quantlib_xloil/<module>.py`. Inspect that module (if
   present) and one nearby analogous wrapper. If no clear mapping exists, stop and ask.
5. Create or extend the wrapper following local naming, conversion, annotation, help,
   and return conventions. Add the module import to `src/quantlib_xloil/__init__.py`
   when creating a new module.
6. Track each added wrapper as `(module, symbol, action, reason)` for the final summary.

## Test and commit

1. Create or update `tests/unittests/test_<module>.py`. Cover each wrapper, optional
   arguments, and representative method calls. For pricing engines, assign the engine
   to a compatible instrument and assert a representative NPV. Use fixed seeds for
   Monte Carlo tests. Do not add workbook tests.
2. Run the focused tests in the same CMD terminal:

   ```cmd
   call C:\ProgramData\miniconda3\Scripts\activate.bat && conda activate xloil && pytest tests\unittests\test_<module>.py -v
   ```

   Fix implementation/test failures and rerun this command. Stop only for environment
   or dependency failures. Add a focused regression test when shared helpers, handles,
   fixings, or engine wiring changes.
3. Inspect `git status --short` and `git diff --check`. Stage only task files; never use
   `git add .` when unrelated changes are present. Commit the scoped change after tests
   pass:

   ```text
   Add new interface file `foo` - add <brief function summary>
   Extend existing interface file `foo` - add <brief function summary>
   ```

   If unrelated changes prevent identifying a scoped file set, stop and ask the user.
