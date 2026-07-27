# Workbook Testing

In this document, we specify the semi-automatic workbook testing framework.

## General Setup

Workbook testing utilizes the `pytest` framework.

The testing methodology is implemented in [test_workbooks.py](./test_workbooks.py), function `test_workbook(...)`.

The tests check all formulas in all worksheets. The cell content is emitted as log message. If a cell shows an unexpected value, e.g. `#NAME?` or `Error`, then the log message is emitted as `ERROR`. Otherwise, the message is emitted as `INFO`.

Note that an `ERROR` log message does not cause the test to fail. Test failure only occurs if `test_workbook(...)` encounters an error.

## Usage

Workbook tests can be run from the project root directory via

```
pytest -o log_cli=true --log-level=INFO --log-file=log\workbooktests.log  tests\workbooktests
```

Here,

- `-o log_cli=true` shows live log in the console,
- `--log-level=INFO` emits all log messages, use `--log-level=WARN` to only show errors (and warnings),
- `--log-file=log\workbooktests.log` writes the log messages to file.

## Limitations

We iterate and calculate individual cells. This approach  raises Python exceptions if the workbook contains formulas that span multiple cells. Such formulas are typically displayed as `{=<formula name>}` with enclosing braces `{}`.

Do not use formulas that span multiple cells in workbook tests. 

Write the formula in a single cell and use Excel's spill range functionality. Alternatively, combine the formula with the Excel `INDEX()` function.

## Troubleshooting

- Make sure Excel is available and xlOil is installed in the current Python environment. Compare `xloil_path()` function.

- Try running a single test by modifying, e.g., `workbook_names = ["test_swap.xlsx"]`.

- Comment (disable) `app.quit()` and `wb.close(save=False)` to inspect the tested workbook manually.
