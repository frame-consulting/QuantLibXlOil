import logging
import os
import pytest
import re
import sys
import time

LOGGER = logging.getLogger(__name__)


def xloil_path():
    python_exe = sys.executable  # with absolute path
    m = re.match(r"(.*[a-zA-Z])(.*)(python\.exe)", python_exe)
    if not m:
        raise Exception(f"Could not parse python executable path: {python_exe}")
    python_path = m.group(1)
    path_delim = m.group(2)
    xlOil_xll = (
        python_path
        + path_delim
        + "share"
        + path_delim
        + "xloil"
        + path_delim
        + "xlOil.xll"
    )
    if not os.path.isfile(xlOil_xll):
        raise Exception(f"xlOil.xll not found at path: {xlOil_xll}")
    return xlOil_xll


def _workbooks_path():
    m = re.match(r"(.*[a-zA-Z])(.*)(test_workbooks\.py)", __file__)
    this_path = m.group(1)
    path_delim = m.group(2)
    workbooks = this_path + path_delim + "workbooks" + path_delim
    if not os.path.exists(workbooks):
        raise Exception(f"workbooks path not found at: {workbooks}")
    return workbooks


def _workbook_file_names():
    workbook_dir = _workbooks_path()
    this_path = os.getcwd()
    os.chdir(workbook_dir)
    workbook_names = [
        os.path.join(root, filename)[2:]
        for root, _, files in os.walk(".")
        for filename in files
    ]
    os.chdir(this_path)
    return workbook_names


@pytest.fixture(scope="module", autouse=True)
def workbooks_path():
    yield _workbooks_path()


# not used
def workbook_recaclulate_manual(wb, delay=0.0):
    for ws in wb.to_com().Sheets:
        ws.Cells.Replace(
            What="=",
            Replacement="=",
            LookAt=2,  # xlPart
            SearchOrder=1,  # xlByRows
            MatchCase=False,
        )
    time.sleep(delay)
    return None


@pytest.fixture(scope="module", autouse=True)
def excel_app():
    import xloil as xlo

    # Create a new Excel instance and make it visible
    LOGGER.info("Open Excel app.")
    app = xlo.Application()
    app.visible = True

    LOGGER.info("Try loading xlOil.xll.")
    xlOil_xll = xloil_path()
    if not app.RegisterXLL(xlOil_xll):
        raise Exception("Cannot load xlOil.xll.")
    LOGGER.info("xlOil.xll loaded successfully.")
    #
    yield app
    #
    LOGGER.info("Quit Excel app...")
    app.quit()
    LOGGER.info("Finished.")


# prepare workbook tests
workbook_dir = _workbooks_path()
workbook_names = [
    # "test_swap.xlsx",
]
workbook_names = _workbook_file_names()
test_args = workbook_names


@pytest.mark.parametrize("file_path", test_args)
def test_workbook(excel_app, workbooks_path, file_path):
    LOGGER.info(f"Open workbook: {file_path}")
    wb = excel_app.open(workbooks_path + file_path, read_only=True)
    try:
        delay = 1.0  # seconds
        #
        LOGGER.info(f"Calculate workbook 1st attempt and wait {delay} seconds.")
        excel_app.to_com().CalculateFull()
        time.sleep(delay)
        # workbook_recaclulate_manual(wb, delay)
        #
        LOGGER.info(f"Calculate workbook 2nd attempt and wait {delay} seconds.")
        excel_app.to_com().CalculateFull()
        time.sleep(delay)
        # workbook_recaclulate_manual(wb, delay)
        #
        LOGGER.info(f"Calculate workbook 3rd attempt and wait {delay} seconds.")
        excel_app.to_com().CalculateFull()
        time.sleep(delay)
        # workbook_recaclulate_manual(wb, delay)
        #
        LOGGER.info("Test excel cells for errors.")
        #
        for ws in wb.to_com().Sheets:
            ws_name = str(ws.Name)
            if ws_name.upper().startswith("SKIP_ME"):
                LOGGER.info("Skip worksheet: " + ws_name)
                continue
            LOGGER.info("Test excel worksheet: " + ws_name)
            for cell in ws.UsedRange:
                if cell.HasFormula:
                    cell.Calculate()
                    # time.sleep(0.1)  # wait for calculation to complete
                    adress = str(cell.Address)
                    formula = str(cell.Formula)
                    text = str(cell.Text)
                    log = LOGGER.info
                    # Check for wrong references in the formula
                    if "#REF!" in formula:
                        log = LOGGER.error
                    # Check for wrong function calls
                    if "#NAME?" in text:
                        log = LOGGER.error
                    # Check for wrong values in the cell text
                    if "#VALUE?" in text:
                        log = LOGGER.error
                    # Check #NUM!
                    if "#NUM!" in text:
                        log = LOGGER.error
                    # Check #N/A
                    if "#N/A" in text:
                        log = LOGGER.error
                    # Check for errors in the cell text
                    if "Error" in text or "error" in text:
                        log = LOGGER.error
                    #
                    text = text.split("\n")[0]  # only first line of text
                    #
                    msg = ws_name + " : " + adress + " : " + formula + " = " + text
                    log(msg)
    finally:
        LOGGER.info("Close workbook.")
        wb.close(save=False)
    return None
