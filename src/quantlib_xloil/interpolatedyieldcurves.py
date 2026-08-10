# Interpolated YieldTermStructures are scattered across several QuantLib-SWIG files but share common properties.
# We combine YieldTermStructure constructors and methods from the following files:
# - discountcurve.i
# - forwardcurve.i
# - zerocurve.i


import QuantLib as ql
import xloil as xlo

from .calendars import qCalendar
from .config import EXCEL_GROUP_NAME
from .date import _to_date_list
from .daycounters import qDayCounter
from .utilities import to_float_list

QL_INTERPOLATION_TRAITS = (
    "FORWARDRATE",
    "LOGDISCOUNT",
    "ZERORATE",
)

QL_INTERPOLATORS = (
    "BACKWARDFLAT",
    "CUBIC",
    "FORWARDFLAT",
    "KRUGER",
    "LINEAR",
    "MONOTONICCUBIC",
)

QL_INTERPOLATED_CURVES = {
    ("FORWARDRATE", "BACKWARDFLAT"): ql.ForwardCurve,
    ("FORWARDRATE", "CUBIC"): ql.NaturalCubicForwardCurve,
    ("FORWARDRATE", "FORWARDFLAT"): ql.ForwardFlatForwardCurve,
    ("FORWARDRATE", "LINEAR"): ql.LinearForwardCurve,
    #
    ("LOGDISCOUNT", "CUBIC"): ql.NaturalLogCubicDiscountCurve,
    ("LOGDISCOUNT", "KRUGER"): ql.KrugerLogDiscountCurve,
    ("LOGDISCOUNT", "LINEAR"): ql.DiscountCurve,
    #
    ("ZERORATE", "CUBIC"): ql.NaturalCubicZeroCurve,
    ("ZERORATE", "KRUGER"): ql.CubicZeroCurve,
    ("ZERORATE", "LINEAR"): ql.ZeroCurve,
    ("ZERORATE", "MONOTONICCUBIC"): ql.MonotonicCubicZeroCurve,
}


@xlo.func(
    help="Construct an interpolated discount curve from a set of dates and discount factors.",
    args={
        "dates": "The dates corresponding to the discount factors.",
        "discounts": "The discount factors corresponding to the dates.",
        "daycounter": "The day count convention to use for the curve.",
        "calendar": "The calendar to use for the curve.",
        "traits": "The interpolation traits: 'LogDiscount', 'ForwardRate', 'ZeroRate'.",
        "interpolator": "The interpolation method to use for the curve.",
        "mixed_interpolation_behavior": "The behavior to use for mixed interpolation.",
        "mixed_interpolation_n": "The where to switch interpolation methods.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterpolatedYieldCurve(
    dates: xlo.Array(dims=1),
    discounts: xlo.Array(dims=1),
    daycounter: qDayCounter,
    calendar: qCalendar,
    traits: str,
    interpolator: str,
    mixed_interpolation_behavior: str = None,
    mixed_interpolation_n: int = None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    if mixed_interpolation_behavior or mixed_interpolation_n:
        raise ValueError("Mixed interpolation not implemented.")
    _dates = _to_date_list(dates)
    _discounts = to_float_list(discounts)
    #
    traits = str(traits).strip().upper()
    if traits not in QL_INTERPOLATION_TRAITS:
        raise ValueError(
            "Invalid traits. Valid values are: " + ", ".join(QL_INTERPOLATION_TRAITS)
        )
    #
    interpolator = str(interpolator).strip().upper()
    if interpolator not in QL_INTERPOLATORS:
        raise ValueError(
            "Invalid interpolator. Valid values are: " + ", ".join(QL_INTERPOLATORS)
        )
    #
    curve = QL_INTERPOLATED_CURVES.get((traits, interpolator))
    if curve is None:
        raise ValueError(
            f"Interpolation method not implemented for traits '{traits}' and interpolator '{interpolator}'."
        )
    yts = curve(_dates, _discounts, daycounter, calendar)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a log-linear interpolated discount curve.",
    args={
        "dates": "The dates corresponding to the discount factors.",
        "discounts": "The discount factors corresponding to the dates.",
        "daycounter": "The day count convention to use for the curve.",
        "calendar": "The calendar to use for the curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDiscountCurve(
    dates: xlo.Array(dims=1),
    discounts: xlo.Array(dims=1),
    daycounter: qDayCounter = ql.Actual365Fixed(),
    calendar: qCalendar = ql.NullCalendar(),
    trigger=None,
) -> ql.YieldTermStructureHandle:
    yts = ql.DiscountCurve(
        _to_date_list(dates), to_float_list(discounts), daycounter, calendar
    )
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a backward-flat interpolated forward rate curve.",
    args={
        "dates": "The dates corresponding to the forward rates.",
        "forwards": "The forward rates corresponding to the dates.",
        "daycounter": "The day count convention to use for the curve.",
        "calendar": "The calendar to use for the curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlForwardCurve(
    dates: xlo.Array(dims=1),
    forwards: xlo.Array(dims=1),
    daycounter: qDayCounter = ql.Actual365Fixed(),
    calendar: qCalendar = ql.NullCalendar(),
    trigger=None,
) -> ql.YieldTermStructureHandle:
    yts = ql.ForwardCurve(
        _to_date_list(dates), to_float_list(forwards), daycounter, calendar
    )
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a linear interpolated zero rate curve.",
    args={
        "dates": "The dates corresponding to the zero rates.",
        "zerorates": "The zero rates corresponding to the dates.",
        "daycounter": "The day count convention to use for the curve.",
        "calendar": "The calendar to use for the curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCurve(
    dates: xlo.Array(dims=1),
    zerorates: xlo.Array(dims=1),
    daycounter: qDayCounter = ql.Actual365Fixed(),
    calendar: qCalendar = ql.NullCalendar(),
    trigger=None,
) -> ql.YieldTermStructureHandle:
    yts = ql.ZeroCurve(
        _to_date_list(dates), to_float_list(zerorates), daycounter, calendar
    )
    return ql.YieldTermStructureHandle(yts)
