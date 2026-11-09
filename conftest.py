import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))


def pytest_addoption(parser):
    parser.addoption(
        "--wb",
        action="store",
        default=None,
        help="Run the workbook test for this workbook filename",
    )
