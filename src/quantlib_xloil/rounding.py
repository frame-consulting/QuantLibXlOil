import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME

QL_ROUNDING_METHODS = {
    'UP': ql.UpRounding,
    'DOWN': ql.DownRounding,
    'CLOSEST': ql.ClosestRounding,
    'CEILING': ql.CeilingTruncation,
    'FLOOR': ql.FloorTruncation,
}

def _qRoundingMethod(method : str):
    if isinstance(method, type):  # capture default value as type not object here
        return method
    if isinstance(method, str):
        method = method.strip().upper()
        if method in QL_ROUNDING_METHODS:
            return QL_ROUNDING_METHODS[method]  # do not call the constructor here, as rounding types require arguments
    raise ValueError(f"Unknown rounding method: {method}")

@xlo.converter()
def qRoundingMethod(method : str):
    return _qRoundingMethod(method)


@xlo.func(
    help="Create a QuantLib Rounding object based on the specified method and precision.",
    args={
        "method" : "The rounding method to use: 'UP', 'DOWN', 'CLOSEST', 'CEILING', 'FLOOR'.",
        "precision" : "The number of decimal places to round to.",
        "digit" : "The digit to use for rounding (default is 5).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRounding(method : qRoundingMethod, precision : int, digit : int = 5, trigger = None) -> ql.Rounding:
    return method(precision, digit)


@xlo.func(
    help="Apply a QuantLib Rounding object to a value.",
    args={
        "rounding" : "The QuantLib Rounding object to apply.",
        "value" : "The value to round.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRoundingApply(rounding : ql.Rounding, value : float, trigger = None) -> float:
    return rounding(value)
