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


def _to_jump_quote_handles(jumps) -> list[ql.QuoteHandle]:
    if jumps is None:
        return []
    return [ql.QuoteHandle(ql.SimpleQuote(float(jump))) for jump in jumps]


QL_INTERPOLATION_TRAITS = (
    "FORWARDRATE",
    "LOGDISCOUNT",
    "SIMPLEZERORATE",
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
    ("SIMPLEZERORATE", "LINEAR"): ql.SimpleZeroCurve,
    #
    ("ZERORATE", "CUBIC"): ql.NaturalCubicZeroCurve,
    ("ZERORATE", "LINEAR"): ql.ZeroCurve,
    ("ZERORATE", "MONOTONICCUBIC"): ql.MonotonicCubicZeroCurve,
}


@xlo.func(
    help="Construct an interpolated discount curve from a set of dates and discount factors.",
    args={
        "dates": "The dates corresponding to the curve values.",
        "values": "The values corresponding to the dates and traits.",
        "daycounter": "The day count convention to use for the curve.",
        "calendar": "The calendar to use for the curve.",
        "traits": "The interpolation traits: 'LogDiscount', 'ForwardRate', 'ZeroRate'.",
        "interpolator": "The interpolation method to use for the curve.",
        "mixed_interpolation_behavior": "The behavior to use for mixed interpolation.",
        "mixed_interpolation_n": "The where to switch interpolation methods.",
        "jumps": "Optional jump quotes for the curve.",
        "jump_dates": "Dates corresponding to the jump quotes.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterpolatedYieldCurve(
    dates: xlo.Array(dims=1),
    values: xlo.Array(dims=1),
    daycounter: qDayCounter,
    calendar: qCalendar,
    traits: str,
    interpolator: str,
    mixed_interpolation_behavior: str = None,
    mixed_interpolation_n: int = None,
    jumps: xlo.Array(dims=1) = None,
    jump_dates: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    if mixed_interpolation_behavior or mixed_interpolation_n:
        raise ValueError("Mixed interpolation not implemented.")
    _dates = _to_date_list(dates)
    _values = to_float_list(values)
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
    if jumps is None and jump_dates is None:
        yts = curve(_dates, _values, daycounter, calendar)
    else:
        yts = curve(
            _dates,
            _values,
            daycounter,
            calendar,
            _to_jump_quote_handles(jumps),
            _to_date_list(jump_dates) if jump_dates is not None else [],
        )
    return ql.YieldTermStructureHandle(yts)


# uses LogLinear interpolator internally
@xlo.func(
    help="Construct a log-linear interpolated discount curve.",
    args={
        "dates": "The dates corresponding to the discount factors.",
        "discounts": "The discount factors corresponding to the dates.",
        "daycounter": "The day count convention to use for the curve.",
        "calendar": "The calendar to use for the curve.",
        "jumps": "Optional jump quotes for the curve.",
        "jump_dates": "Dates corresponding to the jump quotes.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDiscountCurve(
    dates: xlo.Array(dims=1),
    discounts: xlo.Array(dims=1),
    daycounter: qDayCounter,
    calendar=None,
    jumps: xlo.Array(dims=1) = None,
    jump_dates: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    if jumps is not None or jump_dates is not None:
        calendar = qCalendar.__wrapped__(calendar) if calendar is not None else ql.Calendar()
        return ql.YieldTermStructureHandle(
            ql.DiscountCurve(
                _to_date_list(dates),
                to_float_list(discounts),
                daycounter,
                calendar,
                _to_jump_quote_handles(jumps),
                _to_date_list(jump_dates) if jump_dates is not None else [],
            )
        )
    args = [
        _to_date_list(dates),
        to_float_list(discounts),
        daycounter,
    ]
    if calendar is not None:
        calendar = qCalendar.__wrapped__(calendar)
        args.append(calendar)
    yts = ql.DiscountCurve(*args)
    return ql.YieldTermStructureHandle(yts)


# uses BackwardFlat interpolator internally
@xlo.func(
    help="Construct a backward-flat interpolated forward rate curve.",
    args={
        "dates": "The dates corresponding to the forward rates.",
        "forwards": "The forward rates corresponding to the dates.",
        "daycounter": "The day count convention to use for the curve.",
        "calendar": "The calendar to use for the curve.",
        "jumps": "Optional jump quotes for the curve.",
        "jump_dates": "Dates corresponding to the jump quotes.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlForwardCurve(
    dates: xlo.Array(dims=1),
    forwards: xlo.Array(dims=1),
    daycounter: qDayCounter,
    calendar=None,
    jumps: xlo.Array(dims=1) = None,
    jump_dates: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    if jumps is not None or jump_dates is not None:
        calendar = qCalendar.__wrapped__(calendar) if calendar is not None else ql.Calendar()
        return ql.YieldTermStructureHandle(
            ql.ForwardCurve(
                _to_date_list(dates),
                to_float_list(forwards),
                daycounter,
                calendar,
                _to_jump_quote_handles(jumps),
                _to_date_list(jump_dates) if jump_dates is not None else [],
            )
        )
    args = [
        _to_date_list(dates),
        to_float_list(forwards),
        daycounter,
    ]
    if calendar is not None:
        calendar = qCalendar.__wrapped__(calendar)
        args.append(calendar)
    yts = ql.ForwardCurve(*args)
    return ql.YieldTermStructureHandle(yts)


# uses Linear interpolator internally
@xlo.func(
    help="Construct a linear interpolated zero rate curve.",
    args={
        "dates": "The dates corresponding to the zero rates.",
        "zerorates": "The zero rates corresponding to the dates.",
        "daycounter": "The day count convention to use for the curve.",
        "calendar": "The calendar to use for the curve.",
        "jumps": "Optional jump quotes for the curve.",
        "jump_dates": "Dates corresponding to the jump quotes.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCurve(
    dates: xlo.Array(dims=1),
    zerorates: xlo.Array(dims=1),
    daycounter: qDayCounter = ql.Actual365Fixed(),
    calendar=None,
    jumps: xlo.Array(dims=1) = None,
    jump_dates: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    if jumps is not None or jump_dates is not None:
        calendar = qCalendar.__wrapped__(calendar) if calendar is not None else ql.Calendar()
        return ql.YieldTermStructureHandle(
            ql.ZeroCurve(
                _to_date_list(dates),
                to_float_list(zerorates),
                daycounter,
                calendar,
                _to_jump_quote_handles(jumps),
                _to_date_list(jump_dates) if jump_dates is not None else [],
            )
        )
    args = [
        _to_date_list(dates),
        to_float_list(zerorates),
        daycounter,
    ]
    if calendar is not None:
        calendar = qCalendar.__wrapped__(calendar)
        args.append(calendar)
    yts = ql.ZeroCurve(*args)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a linear interpolated simple zero curve.",
    args={
        "dates": "The dates corresponding to the zero yields.",
        "yields": "The simple zero yields corresponding to the dates.",
        "daycounter": "The day count convention to use for the curve.",
        "calendar": "The calendar to use for the curve.",
        "jumps": "Optional jump quotes for the curve.",
        "jump_dates": "Dates corresponding to the jump quotes.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSimpleZeroCurve(
    dates: xlo.Array(dims=1),
    yields: xlo.Array(dims=1),
    daycounter: qDayCounter,
    calendar=None,
    jumps: xlo.Array(dims=1) = None,
    jump_dates: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    args = [
        _to_date_list(dates),
        to_float_list(yields),
        daycounter,
    ]
    if calendar is not None:
        calendar = qCalendar.__wrapped__(calendar)
        args.append(calendar)
    if jumps is not None or jump_dates is not None:
        calendar = qCalendar.__wrapped__(calendar) if calendar is not None else ql.Calendar()
        return ql.YieldTermStructureHandle(
            ql.SimpleZeroCurve(
                args[0],
                args[1],
                daycounter,
                calendar,
                _to_jump_quote_handles(jumps),
                _to_date_list(jump_dates) if jump_dates is not None else [],
            )
        )
    return ql.YieldTermStructureHandle(ql.SimpleZeroCurve(*args))


@xlo.func(
    help="Construct an interpolated simple zero curve object.",
    args={
        "dates": "The dates corresponding to the zero yields.",
        "yields": "The simple zero yields corresponding to the dates.",
        "daycounter": "The day count convention to use for the curve.",
        "calendar": "The calendar to use for the curve.",
        "jumps": "Optional jump quotes for the curve.",
        "jump_dates": "Dates corresponding to the jump quotes.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSimpleZeroCurveAsObject(
    dates: xlo.Array(dims=1),
    yields: xlo.Array(dims=1),
    daycounter: qDayCounter,
    calendar=None,
    jumps: xlo.Array(dims=1) = None,
    jump_dates: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.SimpleZeroCurve:
    calendar = qCalendar.__wrapped__(calendar) if calendar is not None else ql.Calendar()
    return ql.SimpleZeroCurve(
        _to_date_list(dates),
        to_float_list(yields),
        daycounter,
        calendar,
        _to_jump_quote_handles(jumps),
        _to_date_list(jump_dates) if jump_dates is not None else [],
    )


@xlo.func(
    help="Return the dates of an interpolated simple zero curve.",
    args={"curve": "The interpolated simple zero curve."},
    group=EXCEL_GROUP_NAME,
)
def qlSimpleZeroCurveDates(curve: ql.SimpleZeroCurve, trigger=None) -> list[ql.Date]:
    return curve.dates()


@xlo.func(
    help="Return the times of an interpolated simple zero curve.",
    args={"curve": "The interpolated simple zero curve."},
    group=EXCEL_GROUP_NAME,
)
def qlSimpleZeroCurveTimes(curve: ql.SimpleZeroCurve, trigger=None) -> list[float]:
    return curve.times()


@xlo.func(
    help="Return the zero-rate data of an interpolated simple zero curve.",
    args={"curve": "The interpolated simple zero curve."},
    group=EXCEL_GROUP_NAME,
)
def qlSimpleZeroCurveData(curve: ql.SimpleZeroCurve, trigger=None) -> list[float]:
    return curve.data()


@xlo.func(
    help="Return the zero rates of an interpolated simple zero curve.",
    args={"curve": "The interpolated simple zero curve."},
    group=EXCEL_GROUP_NAME,
)
def qlSimpleZeroCurveZeroRates(curve: ql.SimpleZeroCurve, trigger=None) -> list[float]:
    return curve.zeroRates()


@xlo.func(
    help="Construct a log-cubic spread discount curve.",
    args={
        "base_curve": "The base yield term structure handle.",
        "dates": "The dates corresponding to spread discount factors.",
        "discount_factors": "The spread discount factors.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLogCubicSpreadDiscountCurve(
    base_curve: ql.YieldTermStructureHandle,
    dates: xlo.Array(dims=1),
    discount_factors: xlo.Array(dims=1),
    trigger=None,
) -> ql.LogCubicSpreadDiscountCurve:
    return ql.LogCubicSpreadDiscountCurve(
        base_curve, _to_date_list(dates), to_float_list(discount_factors)
    )
