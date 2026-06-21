import numpy as np
import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate, _to_date_list
from .daycounters import qDayCounter
from .interpolatedyieldcurves import QL_INTERPOLATION_TRAITS, QL_INTERPOLATORS
from .utilities import to_object_list

QL_PIECEWISE_CURVES = {
    ("FORWARDRATE", "BACKWARDFLAT"): ql.PiecewiseFlatForward,
    ("FORWARDRATE", "CUBIC"): ql.PiecewiseConvexMonotoneForward,
    ("FORWARDRATE", "LINEAR"): ql.PiecewiseLinearForward,
    #
    ("LOGDISCOUNT", "CUBIC"): ql.PiecewiseNaturalLogCubicDiscount,
    ("LOGDISCOUNT", "LINEAR"): ql.PiecewiseLogLinearDiscount,
    ("LOGDISCOUNT", "KRUGER"): ql.PiecewiseKrugerLogDiscount,
    #
    ("ZERORATE", "CUBIC"): ql.PiecewiseNaturalCubicZero,
    ("ZERORATE", "KRUGER"): ql.PiecewiseKrugerZero,
    ("ZERORATE", "LINEAR"): ql.PiecewiseLinearZero,
    ("ZERORATE", "MONOTONICCUBIC"): ql.PiecewiseConvexMonotoneZero,
}

QL_PIECEWISE_SPREAD_CURVES = {
    ("LOGDISCOUNT", "CUBIC"): ql.PiecewiseNaturalLogCubicSpreadDiscount,
    ("LOGDISCOUNT", "LINEAR"): ql.PiecewiseLogLinearSpreadDiscount,
}


@xlo.func(
    help="Convert a YieldTermStructure to a YieldTermStructureHandle.",
    args={
        "curve": "The YieldTermStructure to convert.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureHandle(
    curve: ql.YieldTermStructure,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    # To access class methods, we add constructors for YieldTermStructures '*AsYts'.
    # We want to also allow conversion into a Handle to use the curve as input to
    # other functions.
    return ql.YieldTermStructureHandle(curve)


@xlo.func(
    help="Get the dates of a PiecewiseYieldCurve.",
    args={
        "curve": "The PiecewiseYieldCurve to get the dates from.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYieldCurveDates(
    curve: ql.YieldTermStructure,
    trigger=None,
) -> list[int]:
    return [d.serialNumber() for d in curve.dates()]


@xlo.func(
    help="Get the times of a PiecewiseYieldCurve.",
    args={
        "curve": "The PiecewiseYieldCurve to get the times from.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYieldCurveTimes(
    curve: ql.YieldTermStructure,
    trigger=None,
) -> list[float]:
    return curve.times()


@xlo.func(
    help="Get the traits data of a PiecewiseYieldCurve.",
    args={
        "curve": "The PiecewiseYieldCurve to get the data from.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYieldCurveData(
    curve: ql.YieldTermStructure,
    trigger=None,
) -> list[float]:
    return curve.data()


@xlo.func(
    help="Construct a PiecewiseYieldCurve as YieldTermStructure from a set of rate helpers.",
    args={
        "reference_date": "The reference date for the curve.",
        "instruments": "The rate helpers to use for the curve.",
        "daycounter": "The day count convention to use for the curve.",
        "traits": "The interpolation traits: 'LogDiscount', 'ForwardRate', 'ZeroRate'.",
        "interpolator": "The interpolation method to use for the curve.",
        "mixed_interpolation_behavior": "The behavior to use for mixed interpolation.",
        "mixed_interpolation_n": "The where to switch interpolation methods.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYieldCurveAsYts(
    reference_date: qDate,
    instruments: xlo.Array(dims=1),
    daycounter: qDayCounter,
    traits: str,
    interpolator: str,
    mixed_interpolation_behavior: str = None,
    mixed_interpolation_n: int = None,
    trigger=None,
) -> ql.YieldTermStructure:
    #
    if mixed_interpolation_behavior or mixed_interpolation_n:
        raise ValueError("Mixed interpolation not implemented.")
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
    curve_class = QL_PIECEWISE_CURVES.get((traits, interpolator))
    if curve_class is None:
        raise ValueError(
            f"Interpolation method not implemented for traits '{traits}' and interpolator '{interpolator}'."
        )
    yts = curve_class(
        reference_date, to_object_list(instruments, ql.RateHelper), daycounter
    )
    return yts


@xlo.func(
    help="Construct a PiecewiseYieldCurve as Handle from a set of rate helpers.",
    args={
        "reference_date": "The reference date for the curve.",
        "instruments": "The rate helpers to use for the curve.",
        "daycounter": "The day count convention to use for the curve.",
        "traits": "The interpolation traits: 'LogDiscount', 'ForwardRate', 'ZeroRate'.",
        "interpolator": "The interpolation method to use for the curve.",
        "mixed_interpolation_behavior": "The behavior to use for mixed interpolation.",
        "mixed_interpolation_n": "The where to switch interpolation methods.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYieldCurve(
    reference_date: qDate,
    instruments: xlo.Array(dims=1),
    daycounter: qDayCounter,
    traits: str,
    interpolator: str,
    mixed_interpolation_behavior: str = None,
    mixed_interpolation_n: int = None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    #
    return ql.YieldTermStructureHandle(
        qlPiecewiseYieldCurveAsYts(
            reference_date,
            instruments,
            daycounter,
            traits,
            interpolator,
            mixed_interpolation_behavior,
            mixed_interpolation_n,
            trigger,
        )
    )


@xlo.func(
    help="Construct a PiecewiseYieldCurve as YieldTermStructure with jumps from a set of rate helpers.",
    args={
        "reference_date": "The reference date for the curve.",
        "instruments": "The rate helpers to use for the curve.",
        "daycounter": "The day count convention to use for the curve.",
        "jumps": "The jump sizes to use for the curve.",
        "jump_dates": "The jump dates to use for the curve.",
        "traits": "The interpolation traits: 'LogDiscount', 'ForwardRate', 'ZeroRate'.",
        "interpolator": "The interpolation method to use for the curve.",
        "mixed_interpolation_behavior": "The behavior to use for mixed interpolation.",
        "mixed_interpolation_n": "The where to switch interpolation methods.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYieldCurveWithJumpsAsYts(
    reference_date: qDate,
    instruments: xlo.Array(dims=1),
    daycounter: qDayCounter,
    jumps: xlo.Array(dims=1),
    jump_dates: xlo.Array(dims=1),
    traits: str,
    interpolator: str,
    mixed_interpolation_behavior: str = None,
    mixed_interpolation_n: int = None,
    trigger=None,
) -> ql.YieldTermStructure:
    #
    if mixed_interpolation_behavior or mixed_interpolation_n:
        raise ValueError("Mixed interpolation not implemented.")
    #
    jumps = [ql.QuoteHandle(ql.SimpleQuote(float(j))) for j in jumps]
    jump_dates = _to_date_list(jump_dates)
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
    curve_class = QL_PIECEWISE_CURVES.get((traits, interpolator))
    if curve_class is None:
        raise ValueError(
            f"Interpolation method not implemented for traits '{traits}' and interpolator '{interpolator}'."
        )
    yts = curve_class(
        reference_date,
        to_object_list(instruments, ql.RateHelper),
        daycounter,
        jumps,
        jump_dates,
    )
    return yts


@xlo.func(
    help="Construct a PiecewiseYieldCurve as Handle with jumps from a set of rate helpers.",
    args={
        "reference_date": "The reference date for the curve.",
        "instruments": "The rate helpers to use for the curve.",
        "daycounter": "The day count convention to use for the curve.",
        "jumps": "The jump sizes to use for the curve.",
        "jump_dates": "The jump dates to use for the curve.",
        "traits": "The interpolation traits: 'LogDiscount', 'ForwardRate', 'ZeroRate'.",
        "interpolator": "The interpolation method to use for the curve.",
        "mixed_interpolation_behavior": "The behavior to use for mixed interpolation.",
        "mixed_interpolation_n": "The where to switch interpolation methods.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYieldCurveWithJumps(
    reference_date: qDate,
    instruments: xlo.Array(dims=1),
    daycounter: qDayCounter,
    jumps: xlo.Array(dims=1),
    jump_dates: xlo.Array(dims=1),
    traits: str,
    interpolator: str,
    mixed_interpolation_behavior: str = None,
    mixed_interpolation_n: int = None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    #
    return ql.YieldTermStructureHandle(
        qlPiecewiseYieldCurveWithJumpsAsYts(
            reference_date,
            instruments,
            daycounter,
            jumps,
            jump_dates,
            traits,
            interpolator,
            mixed_interpolation_behavior,
            mixed_interpolation_n,
            trigger,
        )
    )


@xlo.func(
    help="Construct a PiecewiseSpreadYieldCurve as YieldTermStructure from a set of rate helpers and a base curve.",
    args={
        "base_curve": "The base curve to use for the spread curve.",
        "instruments": "The rate helpers to use for the curve.",
        "traits": "The interpolation traits: 'LogDiscount', 'ForwardRate', 'ZeroRate'.",
        "interpolator": "The interpolation method to use for the curve.",
        "mixed_interpolation_behavior": "The behavior to use for mixed interpolation.",
        "mixed_interpolation_n": "The where to switch interpolation methods.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseSpreadYieldCurveAsYts(
    base_curve: ql.YieldTermStructureHandle,
    instruments: xlo.Array(dims=1),
    traits: str,
    interpolator: str,
    mixed_interpolation_behavior: str = None,
    mixed_interpolation_n: int = None,
    trigger=None,
) -> ql.YieldTermStructure:
    #
    if mixed_interpolation_behavior or mixed_interpolation_n:
        raise ValueError("Mixed interpolation not implemented.")
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
    curve_class = QL_PIECEWISE_SPREAD_CURVES.get((traits, interpolator))
    if curve_class is None:
        raise ValueError(
            f"Interpolation method not implemented for traits '{traits}' and interpolator '{interpolator}'."
        )
    yts = curve_class(base_curve, to_object_list(instruments, ql.RateHelper))
    return yts


@xlo.func(
    help="Construct a PiecewiseSpreadYieldCurve as Handle from a set of rate helpers and a base curve.",
    args={
        "base_curve": "The base curve to use for the spread curve.",
        "instruments": "The rate helpers to use for the curve.",
        "traits": "The interpolation traits: 'LogDiscount', 'ForwardRate', 'ZeroRate'.",
        "interpolator": "The interpolation method to use for the curve.",
        "mixed_interpolation_behavior": "The behavior to use for mixed interpolation.",
        "mixed_interpolation_n": "The where to switch interpolation methods.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseSpreadYieldCurve(
    base_curve: ql.YieldTermStructureHandle,
    instruments: xlo.Array(dims=1),
    traits: str,
    interpolator: str,
    mixed_interpolation_behavior: str = None,
    mixed_interpolation_n: int = None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    #
    return ql.YieldTermStructureHandle(
        qlPiecewiseSpreadYieldCurveAsYts(
            base_curve,
            instruments,
            traits,
            interpolator,
            mixed_interpolation_behavior,
            mixed_interpolation_n,
            trigger,
        )
    )
