import QuantLib as ql
import xloil as xlo

from quantlib_xloil.utilities import enum_class

from .config import EXCEL_GROUP_NAME

QL_ROUNDING_METHODS = {
    "CEILING": ql.CeilingTruncation,
    "CLOSEST": ql.ClosestRounding,
    "DOWN": ql.DownRounding,
    "FLOOR": ql.FloorTruncation,
    "UP": ql.UpRounding,
}


def _qRoundingMethod(method: str):
    if isinstance(method, type):  # capture default value as type not object here
        return method
    return enum_class(method, QL_ROUNDING_METHODS, type)


@xlo.converter()
def qRoundingMethod(method: str):
    return _qRoundingMethod(method)


@xlo.func(
    help="Create a QuantLib Rounding object based on the specified method and precision.",
    args={
        "method": "The rounding method to use: 'UP', 'DOWN', 'CLOSEST', 'CEILING', 'FLOOR'.",
        "precision": "The number of decimal places to round to.",
        "digit": "The digit to use for rounding (default is 5).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRounding(
    method: qRoundingMethod, precision: int, digit: int = 5, trigger=None
) -> ql.Rounding:
    return method(precision, digit)


@xlo.func(
    help="Apply a QuantLib Rounding object to a value.",
    args={
        "rounding": "The QuantLib Rounding object to apply.",
        "value": "The value to round.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRoundingApply(rounding: ql.Rounding, value: float, trigger=None) -> float:
    return rounding(value)
