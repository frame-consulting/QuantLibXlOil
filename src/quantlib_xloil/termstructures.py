import QuantLib as ql
from tomlkit import date
import xloil as xlo

from .calendars import qCalendar
from .config import EXCEL_GROUP_NAME
from .date import qDate, qFrequency
from .daycounters import qDayCounter
from .utilities import enum_value

## TermStructure interface

# TODO: Move QL_COMPOUNDING and converter to interestrate.py

QL_COMPOUNDING = {
    "COMPOUNDED": ql.Compounded,
    "COMPOUNDEDTHENSIMPLE": ql.CompoundedThenSimple,
    "CONTINUOUS": ql.Continuous,
    "SIMPLE": ql.Simple,
    "SIMPLETHENCOMPOUNDED": ql.SimpleThenCompounded,
}


def _qCompounding(compounding: str) -> ql.Compounding:
    return enum_value(compounding, QL_COMPOUNDING)


@xlo.converter()
def qCompounding(compounding: str):
    return _qCompounding(compounding)


@xlo.func(
    help="Get the day counter of a yield term structure.",
    args={
        "ytsh": "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureDayCounter(
    ytsh: ql.YieldTermStructureHandle, trigger=None
) -> ql.DayCounter:
    return ytsh.dayCounter()


@xlo.func(
    help="Get the reference date of a yield term structure.",
    args={
        "ytsh": "The yield term structure handle to query.",
        "date": "The date for which to calculate the time from reference.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureTimeFromReference(
    ytsh: ql.YieldTermStructureHandle, date: qDate, trigger=None
) -> float:
    return ytsh.timeFromReference(date)


@xlo.func(
    help="Get the calendar of a yield term structure.",
    args={
        "ytsh": "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureCalendar(
    ytsh: ql.YieldTermStructureHandle, trigger=None
) -> ql.Calendar:
    return ytsh.calendar()


@xlo.func(
    help="Get the reference date of a yield term structure.",
    args={
        "ytsh": "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureReferenceDate(
    ytsh: ql.YieldTermStructureHandle, trigger=None
) -> ql.Date:
    return ytsh.referenceDate()


@xlo.func(
    help="Get the maximum date of a yield term structure.",
    args={
        "ytsh": "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureMaxDate(ytsh: ql.YieldTermStructureHandle, trigger=None) -> ql.Date:
    return ytsh.maxDate()


@xlo.func(
    help="Get the maximum time of a yield term structure.",
    args={
        "ytsh": "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureMaxTime(ytsh: ql.YieldTermStructureHandle) -> float:
    return ytsh.maxTime()


@xlo.func(
    help="Allow extrapolation for a yield term structure.",
    args={
        "ytsh": "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureEnableExrapolation(ytsh: ql.YieldTermStructureHandle, trigger=None):
    ytsh.enableExtrapolation()
    return True


@xlo.func(
    help="Disallow extrapolation for a yield term structure.",
    args={
        "ytsh": "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureDisableExrapolation(ytsh: ql.YieldTermStructureHandle, trigger=None):
    ytsh.disableExtrapolation()
    return True


@xlo.func(
    help="Check if extrapolation is allowed for a yield term structure.",
    args={
        "ytsh": "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureAllowsExtrapolation(
    ytsh: ql.YieldTermStructureHandle, trigger=None
) -> bool:
    return ytsh.allowsExtrapolation()


## YieldTermStructure interface


@xlo.func(
    help="Get the discount factor for a yield term structure.",
    args={
        "ytsh": "The yield term structure handle to query.",
        "date": "The date for which to calculate the discount factor.",
        "extrapolate": "Whether to extrapolate if the date is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureDiscount(
    ytsh: ql.YieldTermStructureHandle,
    date: qDate,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ytsh.discount(date, extrapolate)


@xlo.func(
    help="Get the discount factor for a yield term structure from a time.",
    args={
        "ytsh": "The yield term structure handle to query.",
        "time": "The time for which to calculate the discount factor.",
        "extrapolate": "Whether to extrapolate if the time is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureDiscountFromTime(
    ytsh: ql.YieldTermStructureHandle,
    time: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ytsh.discount(time, extrapolate)


@xlo.func(
    help="Get the zero rate for a yield term structure.",
    args={
        "ytsh": "The yield term structure handle to query.",
        "date": "The date for which to calculate the zero rate.",
        "daycounter": "The day count convention to use for the calculation.",
        "compounding": "The compounding convention to use for the calculation.",
        "frequency": "The frequency to use for the calculation.",
        "extrapolate": "Whether to extrapolate if the date is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureZeroRate(
    ytsh: ql.YieldTermStructureHandle,
    date: qDate,
    daycounter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ytsh.zeroRate(date, daycounter, compounding, frequency, extrapolate).rate()


@xlo.func(
    help="Get the zero rate for a yield term structure from a time.",
    args={
        "ytsh": "The yield term structure handle to query.",
        "time": "The time for which to calculate the zero rate.",
        "compounding": "The compounding convention to use for the calculation.",
        "frequency": "The frequency to use for the calculation.",
        "extrapolate": "Whether to extrapolate if the time is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureZeroRateFromTime(
    ytsh: ql.YieldTermStructureHandle,
    time: float,
    compounding: qCompounding,
    frequency: qFrequency,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ytsh.zeroRate(time, compounding, frequency, extrapolate).rate()


@xlo.func(
    help="Get the forward rate for a yield term structure.",
    args={
        "ytsh": "The yield term structure handle to query.",
        "date1": "The start date for the forward rate calculation.",
        "date2": "The end date for the forward rate calculation.",
        "daycounter": "The day count convention to use for the calculation.",
        "compounding": "The compounding convention to use for the calculation.",
        "frequency": "The frequency to use for the calculation.",
        "extrapolate": "Whether to extrapolate if the dates are outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureForwardRate(
    ytsh: ql.YieldTermStructureHandle,
    date1: qDate,
    date2: qDate,
    daycounter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ytsh.forwardRate(
        date1, date2, daycounter, compounding, frequency, extrapolate
    ).rate()


@xlo.func(
    help="Get the forward rate for a yield term structure from times.",
    args={
        "ytsh": "The yield term structure handle to query.",
        "time1": "The start time for the forward rate calculation.",
        "time2": "The end time for the forward rate calculation.",
        "compounding": "The compounding convention to use for the calculation.",
        "frequency": "The frequency to use for the calculation.",
        "extrapolate": "Whether to extrapolate if the times are outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureForwardRateFromTime(
    ytsh: ql.YieldTermStructureHandle,
    time1: float,
    time2: float,
    compounding: qCompounding,
    frequency: qFrequency,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ytsh.forwardRate(time1, time2, compounding, frequency, extrapolate).rate()


## FlatForward


@xlo.func(
    help="Construct a flat forward curve from a reference date and a forward rate.",
    args={
        "reference_date": "The reference date for the curve.",
        "forward_rate": "The forward rate for the curve.",
        "daycounter": "The day count convention to use for the curve.",
        "compounding": "The compounding convention to use for the curve.",
        "frequency": "The frequency to use for the curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFlatForward(
    reference_date: qDate,
    forward_rate: float,
    daycounter: qDayCounter,
    compounding: qCompounding = ql.Continuous,
    frequency: qFrequency = ql.Annual,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    yts = ql.FlatForward(
        reference_date, forward_rate, daycounter, compounding, frequency
    )
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a flat forward curve from settlement days, a calendar and a forward rate.",
    args={
        "settlement_days": "The number of settlement days for the curve.",
        "calendar": "The calendar to use for the curve.",
        "forward_rate": "The forward rate for the curve.",
        "daycounter": "The day count convention to use for the curve.",
        "compounding": "The compounding convention to use for the curve.",
        "frequency": "The frequency to use for the curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFlatForward2(
    settlement_days: int,
    calendar: qCalendar,
    forward_rate: float,
    daycounter: qDayCounter,
    compounding: qCompounding = ql.Continuous,
    frequency: qFrequency = ql.Annual,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    yts = ql.FlatForward(
        settlement_days, calendar, forward_rate, daycounter, compounding, frequency
    )
    return ql.YieldTermStructureHandle(yts)


## Implied term structure


@xlo.func(
    help="Construct an implied term structure from a base term structure and a reference date.",
    args={
        "ytsh": "The base yield term structure handle.",
        "reference_date": "The reference date for the implied term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlImpliedTermStructure(
    ytsh: ql.YieldTermStructureHandle,
    reference_date: qDate,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    yts = ql.ImpliedTermStructure(ytsh, reference_date)
    return ql.YieldTermStructureHandle(yts)


## Spreaded term structures


@xlo.func(
    help="Construct a zero spreaded term structure from a base term structure and a spread.",
    args={
        "base": "The base yield term structure handle.",
        "spread": "The spread to add to the zero rates of the base term structure.",
        "compounding": "The compounding convention to use for the spread.",
        "frequency": "The frequency to use for the spread.",
        "daycounter": "The day count convention to use for the spread.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroSpreadedTermStructure(
    base: ql.YieldTermStructureHandle,
    spread: float,
    compounding: qCompounding = ql.Continuous,
    frequency: qFrequency = ql.NoFrequency,
    daycounter=None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    spread_handle = ql.QuoteHandle(ql.SimpleQuote(spread))
    args = [base, spread_handle, compounding, frequency]

    if daycounter is not None:
        daycounter = qDayCounter.__wrapped__(daycounter)
        args.append(daycounter)

    yts = ql.ZeroSpreadedTermStructure(*args)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a forward spreaded term structure from a base term structure and a spread.",
    args={
        "base": "The base yield term structure handle.",
        "spread": "The spread to add to the forward rates of the base term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlForwardSpreadedTermStructure(
    base: ql.YieldTermStructureHandle,
    spread: float,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    spread_handle = ql.QuoteHandle(ql.SimpleQuote(spread))
    yts = ql.ForwardSpreadedTermStructure(base, spread_handle)
    return ql.YieldTermStructureHandle(yts)


QL_COMPOSITE_OPERATORS = {"+": lambda z1, z2: z1 + z2, "-": lambda z1, z2: z1 - z2}


@xlo.func(
    help="Construct a composite zero yield structure from two base term structures and an operator.",
    args={
        "curve1": "The first yield term structure handle.",
        "curve2": "The second yield term structure handle.",
        "operator": "The operator to combine the curves. Valid values are: +, -",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCompositeZeroYieldStructure(
    curve1: ql.YieldTermStructureHandle,
    curve2: ql.YieldTermStructureHandle,
    operator: str,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    if operator in QL_COMPOSITE_OPERATORS:
        yts = ql.CompositeZeroYieldStructure(
            curve1, curve2, QL_COMPOSITE_OPERATORS[operator]
        )
    else:
        raise ValueError("Invalid operator. Valid values are: +, -")
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct an ultimate forward term structure with smoothing between liquid and ultimate rates.",
    args={
        "ytsh": "The base yield term structure handle.",
        "last_liquid_forward": "The last liquid forward rate (as a float, internally converted to QuoteHandle).",
        "ultimate_forward": "The ultimate forward rate (as a float, internally converted to QuoteHandle).",
        "first_smoothing_point": "The period from the reference date after which smoothing begins (e.g., 1Y).",
        "alpha": "The smoothing parameter (0 = abrupt transition, higher values = smoother transition).",
        "rounding_digits": "Optional number of digits for rounding (default: None).",
        "compounding": "The compounding convention (default: COMPOUNDED).",
        "frequency": "The frequency for compounding (default: ANNUAL).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlUltimateForwardTermStructure(
    ytsh: ql.YieldTermStructureHandle,
    last_liquid_forward: float,
    ultimate_forward: float,
    first_smoothing_point: ql.Period,
    alpha: float,
    rounding_digits: int = None,
    compounding: qCompounding = ql.Compounded,
    frequency: qFrequency = ql.Annual,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    last_liquid_handle = ql.QuoteHandle(ql.SimpleQuote(last_liquid_forward))
    ultimate_handle = ql.QuoteHandle(ql.SimpleQuote(ultimate_forward))
    yts = ql.UltimateForwardTermStructure(
        ytsh,
        last_liquid_handle,
        ultimate_handle,
        first_smoothing_point,
        alpha,
        rounding_digits,
        compounding,
        frequency,
    )
    return ql.YieldTermStructureHandle(yts)


## Interpolated Piecewise Zero Spreaded Term Structures


@xlo.func(
    help="Construct a piecewise zero spreaded term structure with linear interpolation.",
    args={
        "base_curve": "The base yield term structure handle.",
        "spreads": "List of spread values (floats) for each date.",
        "dates": "List of dates (as qDate) corresponding to the spreads.",
        "compounding": "Compounding convention (default: CONTINUOUS).",
        "frequency": "Frequency for compounding (default: NOFREQUENCY).",
        "daycounter": "Day counter for the spreads (default: base curve's day counter).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseZeroSpreadedTermStructure(
    base_curve: ql.YieldTermStructureHandle,
    spreads: xlo.Array(dims=1),
    dates: xlo.Array(dims=1),
    compounding: qCompounding = ql.Continuous,
    frequency: qFrequency = ql.NoFrequency,
    daycounter=None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    spread_handles = [ql.QuoteHandle(ql.SimpleQuote(s)) for s in spreads]
    ql_dates = [d if isinstance(d, ql.Date) else qDate.__wrapped__(d) for d in dates]
    args = [base_curve, spread_handles, ql_dates, compounding, frequency]
    if daycounter is not None:
        daycounter = qDayCounter.__wrapped__(daycounter)
        args.append(daycounter)
    yts = ql.PiecewiseZeroSpreadedTermStructure(*args)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a spreaded linear zero interpolated term structure.",
    args={
        "base_curve": "The base yield term structure handle.",
        "spreads": "List of spread values (floats) for each date.",
        "dates": "List of dates (as qDate) corresponding to the spreads.",
        "compounding": "Compounding convention (default: CONTINUOUS).",
        "frequency": "Frequency for compounding (default: NOFREQUENCY).",
        "daycounter": "Day counter for the spreads (default: base curve's day counter).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSpreadedLinearZeroInterpolatedTermStructure(
    base_curve: ql.YieldTermStructureHandle,
    spreads: xlo.Array(dims=1),
    dates: xlo.Array(dims=1),
    compounding: qCompounding = ql.Continuous,
    frequency: qFrequency = ql.NoFrequency,
    daycounter=None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    spread_handles = [ql.QuoteHandle(ql.SimpleQuote(s)) for s in spreads]
    ql_dates = [d if isinstance(d, ql.Date) else qDate.__wrapped__(d) for d in dates]
    args = [base_curve, spread_handles, ql_dates, compounding, frequency]
    if daycounter is not None:
        daycounter = qDayCounter.__wrapped__(daycounter)
        args.append(daycounter)
    yts = ql.SpreadedLinearZeroInterpolatedTermStructure(*args)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a spreaded backward-flat zero interpolated term structure.",
    args={
        "base_curve": "The base yield term structure handle.",
        "spreads": "List of spread values (floats) for each date.",
        "dates": "List of dates (as qDate) corresponding to the spreads.",
        "compounding": "Compounding convention (default: CONTINUOUS).",
        "frequency": "Frequency for compounding (default: NOFREQUENCY).",
        "daycounter": "Day counter for the spreads (default: base curve's day counter).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSpreadedBackwardFlatZeroInterpolatedTermStructure(
    base_curve: ql.YieldTermStructureHandle,
    spreads: xlo.Array(dims=1),
    dates: xlo.Array(dims=1),
    compounding: qCompounding = ql.Continuous,
    frequency: qFrequency = ql.NoFrequency,
    daycounter=None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    spread_handles = [ql.QuoteHandle(ql.SimpleQuote(s)) for s in spreads]
    ql_dates = [d if isinstance(d, ql.Date) else qDate.__wrapped__(d) for d in dates]
    args = [base_curve, spread_handles, ql_dates, compounding, frequency]
    if daycounter is not None:
        daycounter = qDayCounter.__wrapped__(daycounter)
        args.append(daycounter)
    yts = ql.SpreadedBackwardFlatZeroInterpolatedTermStructure(*args)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a spreaded cubic zero interpolated term structure.",
    args={
        "base_curve": "The base yield term structure handle.",
        "spreads": "List of spread values (floats) for each date.",
        "dates": "List of dates (as qDate) corresponding to the spreads.",
        "compounding": "Compounding convention (default: CONTINUOUS).",
        "frequency": "Frequency for compounding (default: NOFREQUENCY).",
        "daycounter": "Day counter for the spreads (default: base curve's day counter).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSpreadedCubicZeroInterpolatedTermStructure(
    base_curve: ql.YieldTermStructureHandle,
    spreads: xlo.Array(dims=1),
    dates: xlo.Array(dims=1),
    compounding: qCompounding = ql.Continuous,
    frequency: qFrequency = ql.NoFrequency,
    daycounter=None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    spread_handles = [ql.QuoteHandle(ql.SimpleQuote(s)) for s in spreads]
    ql_dates = [d if isinstance(d, ql.Date) else qDate.__wrapped__(d) for d in dates]
    args = [base_curve, spread_handles, ql_dates, compounding, frequency]
    if daycounter is not None:
        daycounter = qDayCounter.__wrapped__(daycounter)
        args.append(daycounter)
    yts = ql.SpreadedCubicZeroInterpolatedTermStructure(*args)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a spreaded Kruger zero interpolated term structure (monotone convex).",
    args={
        "base_curve": "The base yield term structure handle.",
        "spreads": "List of spread values (floats) for each date.",
        "dates": "List of dates (as qDate) corresponding to the spreads.",
        "compounding": "Compounding convention (default: CONTINUOUS).",
        "frequency": "Frequency for compounding (default: NOFREQUENCY).",
        "daycounter": "Day counter for the spreads (default: base curve's day counter).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSpreadedKrugerZeroInterpolatedTermStructure(
    base_curve: ql.YieldTermStructureHandle,
    spreads: xlo.Array(dims=1),
    dates: xlo.Array(dims=1),
    compounding: qCompounding = ql.Continuous,
    frequency: qFrequency = ql.NoFrequency,
    daycounter=None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    spread_handles = [ql.QuoteHandle(ql.SimpleQuote(s)) for s in spreads]
    ql_dates = [d if isinstance(d, ql.Date) else qDate.__wrapped__(d) for d in dates]
    args = [base_curve, spread_handles, ql_dates, compounding, frequency]
    if daycounter is not None:
        daycounter = qDayCounter.__wrapped__(daycounter)
        args.append(daycounter)
    yts = ql.SpreadedKrugerZeroInterpolatedTermStructure(*args)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a spreaded spline cubic zero interpolated term structure.",
    args={
        "base_curve": "The base yield term structure handle.",
        "spreads": "List of spread values (floats) for each date.",
        "dates": "List of dates (as qDate) corresponding to the spreads.",
        "compounding": "Compounding convention (default: CONTINUOUS).",
        "frequency": "Frequency for compounding (default: NOFREQUENCY).",
        "daycounter": "Day counter for the spreads (default: base curve's day counter).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSpreadedSplineCubicZeroInterpolatedTermStructure(
    base_curve: ql.YieldTermStructureHandle,
    spreads: xlo.Array(dims=1),
    dates: xlo.Array(dims=1),
    compounding: qCompounding = ql.Continuous,
    frequency: qFrequency = ql.NoFrequency,
    daycounter=None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    spread_handles = [ql.QuoteHandle(ql.SimpleQuote(s)) for s in spreads]
    ql_dates = [d if isinstance(d, ql.Date) else qDate.__wrapped__(d) for d in dates]
    args = [base_curve, spread_handles, ql_dates, compounding, frequency]
    if daycounter is not None:
        daycounter = qDayCounter.__wrapped__(daycounter)
        args.append(daycounter)
    yts = ql.SpreadedSplineCubicZeroInterpolatedTermStructure(*args)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a spreaded parabolic cubic zero interpolated term structure.",
    args={
        "base_curve": "The base yield term structure handle.",
        "spreads": "List of spread values (floats) for each date.",
        "dates": "List of dates (as qDate) corresponding to the spreads.",
        "compounding": "Compounding convention (default: CONTINUOUS).",
        "frequency": "Frequency for compounding (default: NOFREQUENCY).",
        "daycounter": "Day counter for the spreads (default: base curve's day counter).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSpreadedParabolicCubicZeroInterpolatedTermStructure(
    base_curve: ql.YieldTermStructureHandle,
    spreads: xlo.Array(dims=1),
    dates: xlo.Array(dims=1),
    compounding: qCompounding = ql.Continuous,
    frequency: qFrequency = ql.NoFrequency,
    daycounter=None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    spread_handles = [ql.QuoteHandle(ql.SimpleQuote(s)) for s in spreads]
    ql_dates = [d if isinstance(d, ql.Date) else qDate.__wrapped__(d) for d in dates]
    args = [base_curve, spread_handles, ql_dates, compounding, frequency]
    if daycounter is not None:
        daycounter = qDayCounter.__wrapped__(daycounter)
        args.append(daycounter)
    yts = ql.SpreadedParabolicCubicZeroInterpolatedTermStructure(*args)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a spreaded monotonic parabolic cubic zero interpolated term structure.",
    args={
        "base_curve": "The base yield term structure handle.",
        "spreads": "List of spread values (floats) for each date.",
        "dates": "List of dates (as qDate) corresponding to the spreads.",
        "compounding": "Compounding convention (default: CONTINUOUS).",
        "frequency": "Frequency for compounding (default: NOFREQUENCY).",
        "daycounter": "Day counter for the spreads (default: base curve's day counter).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSpreadedMonotonicParabolicCubicZeroInterpolatedTermStructure(
    base_curve: ql.YieldTermStructureHandle,
    spreads: xlo.Array(dims=1),
    dates: xlo.Array(dims=1),
    compounding: qCompounding = ql.Continuous,
    frequency: qFrequency = ql.NoFrequency,
    daycounter=None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    spread_handles = [ql.QuoteHandle(ql.SimpleQuote(s)) for s in spreads]
    ql_dates = [d if isinstance(d, ql.Date) else qDate.__wrapped__(d) for d in dates]
    args = [base_curve, spread_handles, ql_dates, compounding, frequency]
    if daycounter is not None:
        daycounter = qDayCounter.__wrapped__(daycounter)
        args.append(daycounter)
    yts = ql.SpreadedMonotonicParabolicCubicZeroInterpolatedTermStructure(*args)
    return ql.YieldTermStructureHandle(yts)


## Piecewise Forward Spreaded Term Structures


@xlo.func(
    help="Construct a piecewise forward spreaded term structure with backward-flat interpolation.",
    args={
        "base_curve": "The base yield term structure handle.",
        "spreads": "List of spread values (floats) for each date.",
        "dates": "List of dates (as qDate) corresponding to the spreads.",
        "daycounter": "Day counter for the spreads (default: base curve's day counter).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseForwardSpreadedTermStructure(
    base_curve: ql.YieldTermStructureHandle,
    spreads: xlo.Array(dims=1),
    dates: xlo.Array(dims=1),
    daycounter=None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    spread_handles = [ql.QuoteHandle(ql.SimpleQuote(s)) for s in spreads]
    ql_dates = [d if isinstance(d, ql.Date) else qDate.__wrapped__(d) for d in dates]
    args = [base_curve, spread_handles, ql_dates]
    if daycounter is not None:
        daycounter = qDayCounter.__wrapped__(daycounter)
        args.append(daycounter)
    yts = ql.PiecewiseForwardSpreadedTermStructure(*args)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a piecewise linear forward spreaded term structure.",
    args={
        "base_curve": "The base yield term structure handle.",
        "spreads": "List of spread values (floats) for each date.",
        "dates": "List of dates (as qDate) corresponding to the spreads.",
        "daycounter": "Day counter for the spreads (default: base curve's day counter).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseLinearForwardSpreadedTermStructure(
    base_curve: ql.YieldTermStructureHandle,
    spreads: xlo.Array(dims=1),
    dates: xlo.Array(dims=1),
    daycounter=None,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    spread_handles = [ql.QuoteHandle(ql.SimpleQuote(s)) for s in spreads]
    ql_dates = [d if isinstance(d, ql.Date) else qDate.__wrapped__(d) for d in dates]
    args = [base_curve, spread_handles, ql_dates]
    if daycounter is not None:
        daycounter = qDayCounter.__wrapped__(daycounter)
        args.append(daycounter)
    yts = ql.PiecewiseLinearForwardSpreadedTermStructure(*args)
    return ql.YieldTermStructureHandle(yts)


## Quanto Term Structure


@xlo.func(
    help="Construct a quanto term structure for cross-currency derivatives pricing.",
    args={
        "underlying_dividend_ts": "The yield term structure for the underlying dividend (domestic).",
        "risk_free_ts": "The risk-free yield term structure (domestic).",
        "foreign_risk_free_ts": "The risk-free yield term structure (foreign).",
        "underlying_black_vol_ts": "The black volatility term structure for the underlying.",
        "strike": "The strike price for the quanto adjustment.",
        "exch_rate_black_vol_ts": "The black volatility term structure for the exchange rate.",
        "exch_rate_atm_level": "The at-the-money level for the exchange rate.",
        "underlying_exch_rate_correlation": "The correlation between the underlying and exchange rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoTermStructure(
    underlying_dividend_ts: ql.YieldTermStructureHandle,
    risk_free_ts: ql.YieldTermStructureHandle,
    foreign_risk_free_ts: ql.YieldTermStructureHandle,
    underlying_black_vol_ts: ql.BlackVolTermStructureHandle,
    strike: float,
    exch_rate_black_vol_ts: ql.BlackVolTermStructureHandle,
    exch_rate_atm_level: float,
    underlying_exch_rate_correlation: float,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    yts = ql.QuantoTermStructure(
        underlying_dividend_ts,
        risk_free_ts,
        foreign_risk_free_ts,
        underlying_black_vol_ts,
        strike,
        exch_rate_black_vol_ts,
        exch_rate_atm_level,
        underlying_exch_rate_correlation,
    )
    return ql.YieldTermStructureHandle(yts)
