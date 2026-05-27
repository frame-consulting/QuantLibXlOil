# Interpolated YieldTermStructures are scattered across several QuantLib-SWIG files but share common properties.
# We combine YieldTermStructure constructors and methods from the following files:
# - discountcurve.i
# - forwardcurve.i
# - zerocurve.i


import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import _qDate
from .calendars import qCalendar
from .daycounters import qDayCounter


QL_INTERPOLATION_TRAITS = (
    'LOGDISCOUNT',
    'FORWARDRATE',
    'ZERORATE',
)

QL_INTERPOLATORS = (
    'BACKWARDFLAT',
    'FORWARDFLAT',
    'LINEAR',
    'CUBIC',
    'MONOTONICCUBIC',
    'KRUGER',
)

QL_INTERPOLATED_CURVES = {
    ('LOGDISCOUNT', 'LINEAR'): ql.DiscountCurve,
    ('LOGDISCOUNT', 'CUBIC'): ql.NaturalLogCubicDiscountCurve,
    ('LOGDISCOUNT', 'KRUGER'): ql.KrugerLogDiscountCurve,
    #
    ('FORWARDRATE', 'BACKWARDFLAT'): ql.ForwardCurve,
    ('FORWARDRATE', 'FORWARDFLAT'): ql.ForwardFlatForwardCurve,
    ('FORWARDRATE', 'LINEAR'): ql.LinearForwardCurve,
    ('FORWARDRATE', 'CUBIC'): ql.NaturalCubicForwardCurve,
    #
    ('ZERORATE', 'LINEAR'): ql.ZeroCurve,
    ('ZERORATE', 'CUBIC'): ql.NaturalCubicZeroCurve,
    ('ZERORATE', 'MONOTONICCUBIC'): ql.MonotonicCubicZeroCurve,
    ('ZERORATE', 'KRUGER'): ql.KrugerZeroCurve,
}

@xlo.func(
    help="Construct an interpolated discount curve from a set of dates and discount factors.",
    args={
        "Dates" : "The dates corresponding to the discount factors.",
        "Discounts" : "The discount factors corresponding to the dates.",
        "DayCounter" : "The day count convention to use for the curve.",
        "Calendar" : "The calendar to use for the curve.",
        "Traits" : "The interpolation traits: 'Discount', 'ForwardRate', 'ZeroRate'.",
        "Interpolator" : "The interpolation method to use for the curve.",
        "MixedInterpolationBehavior" : "The behavior to use for mixed interpolation.",
        "MixedInterpolationN" : "The where to switch interpolation methods.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterpolatedYieldCurve(
        dates : xlo.Array(dims=1),
        discounts : xlo.Array(dims=1),
        daycounter : qDayCounter,
        calendar : qCalendar,
        traits : str,
        interpolator : str,
        mixed_interpolation_behavior : str = None,
        mixed_interpolation_n : int = None,
        trigger = None,
    ) -> ql.YieldTermStructureHandle:
    if mixed_interpolation_behavior or mixed_interpolation_n:
        raise ValueError("Mixed interpolation not implemented.")
    _dates = [_qDate(d) for d in dates]
    _discounts = [float(d) for d in discounts]
    #
    traits = str(traits).strip().upper()
    if traits not in QL_INTERPOLATION_TRAITS:
        raise ValueError("Invalid traits. Valid values are: " + ", ".join(QL_INTERPOLATION_TRAITS))
    #
    interpolator = str(interpolator).strip().upper()
    if interpolator not in QL_INTERPOLATORS:
        raise ValueError("Invalid interpolator. Valid values are: " + ", ".join(QL_INTERPOLATORS))
    #
    curve = QL_INTERPOLATED_CURVES.get((traits, interpolator))
    if curve is None:
        raise ValueError(f"Interpolation method not implemented for traits '{traits}' and interpolator '{interpolator}'.")
    yts = curve(_dates, _discounts, daycounter, calendar)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a log-linear interpolated discount curve.",
    args={
        "Dates" : "The dates corresponding to the discount factors.",
        "Discounts" : "The discount factors corresponding to the dates.",
        "DayCounter" : "The day count convention to use for the curve.",
        "Calendar" : "The calendar to use for the curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDiscountCurve(
        dates : xlo.Array(dims=1),
        discounts : xlo.Array(dims=1),
        daycounter : qDayCounter = ql.Actual365Fixed(),
        calendar : qCalendar = ql.NullCalendar(),
        trigger = None,
    ) -> ql.YieldTermStructureHandle:
    _dates = [_qDate(d) for d in dates]
    _discounts = [float(d) for d in discounts]
    yts = ql.DiscountCurve(_dates, _discounts, daycounter, calendar)
    return ql.YieldTermStructureHandle(yts)

@xlo.func(
    help="Construct a backward-flat interpolated forward rate curve.",
    args={
        "Dates" : "The dates corresponding to the forward rates.",
        "Forwards" : "The forward rates corresponding to the dates.",
        "DayCounter" : "The day count convention to use for the curve.",
        "Calendar" : "The calendar to use for the curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlForwardCurve(
        dates : xlo.Array(dims=1),
        forwards : xlo.Array(dims=1),
        daycounter : qDayCounter = ql.Actual365Fixed(),
        calendar : qCalendar = ql.NullCalendar(),
        trigger = None,
    ) -> ql.YieldTermStructureHandle:
    _dates = [_qDate(d) for d in dates]
    _forwards = [float(f) for f in forwards]
    yts = ql.ForwardCurve(_dates, _forwards, daycounter, calendar)
    return ql.YieldTermStructureHandle(yts)

@xlo.func(
    help="Construct a linear interpolated zero rate curve.",
    args={
        "Dates" : "The dates corresponding to the zero rates.",
        "ZeroRates" : "The zero rates corresponding to the dates.",
        "DayCounter" : "The day count convention to use for the curve.",
        "Calendar" : "The calendar to use for the curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCurve(
        dates : xlo.Array(dims=1),
        zerorates : xlo.Array(dims=1),
        daycounter : qDayCounter = ql.Actual365Fixed(),
        calendar : qCalendar = ql.NullCalendar(),
        trigger = None,
    ) -> ql.YieldTermStructureHandle:
    _dates = [_qDate(d) for d in dates]
    _zerorates = [float(z) for z in zerorates]
    yts = ql.ZeroCurve(_dates, _zerorates, daycounter, calendar)
    return ql.YieldTermStructureHandle(yts)
