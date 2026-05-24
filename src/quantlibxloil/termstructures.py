import QuantLib as ql
from tomlkit import date
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate, qFrequency
from .calendars import qCalendar
from .daycounters import qDayCounter
from .utilities import enum_value


## TermStructure interface

@xlo.func(
    help="Get the day counter of a yield term structure.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureDayCounter(ytsh : ql.YieldTermStructureHandle, Trigger = None) -> ql.DayCounter:
    return ytsh.dayCounter()

@xlo.func(
    help="Get the reference date of a yield term structure.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
        "Date" : "The date for which to calculate the time from reference.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureTimeFromReference(ytsh : ql.YieldTermStructureHandle, date : qDate, Trigger = None) -> float:
    return ytsh.timeFromReference(date)

@xlo.func(
    help="Get the calendar of a yield term structure.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureCalendar(ytsh : ql.YieldTermStructureHandle, Trigger = None) -> ql.Calendar:
    return ytsh.calendar()

@xlo.func(
    help="Get the reference date of a yield term structure.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureReferenceDate(ytsh : ql.YieldTermStructureHandle, Trigger = None) -> qDate:
    return ytsh.referenceDate()

@xlo.func(
    help="Get the maximum date of a yield term structure.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureMaxDate(ytsh : ql.YieldTermStructureHandle, Trigger = None) -> qDate:
    return ytsh.maxDate()

@xlo.func(
    help="Get the maximum time of a yield term structure.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureMaxTime(ytsh : ql.YieldTermStructureHandle) -> float:
    return ytsh.maxTime()

@xlo.func(
    help="Allow extrapolation for a yield term structure.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureEnableExrapolation(ytsh : ql.YieldTermStructureHandle, Trigger = None):
    ytsh.enableExtrapolation()
    return True

@xlo.func(
    help="Disallow extrapolation for a yield term structure.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureDisableExrapolation(ytsh : ql.YieldTermStructureHandle, Trigger = None):
    ytsh.disableExtrapolation()
    return True

@xlo.func(
    help="Check if extrapolation is allowed for a yield term structure.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTermStructureAllowsExtrapolation(ytsh : ql.YieldTermStructureHandle, Trigger = None) -> bool:
    return ytsh.allowsExtrapolation()


## YieldTermStructure interface

# TODO: Move QL_COMPOUNDING and converter to interestrate.py

QL_COMPOUNDING = {
    "SIMPLE": ql.Simple,
    "COMPOUNDED": ql.Compounded,
    "CONTINUOUS": ql.Continuous,
    "SIMPLETHENCOMPOUNDED": ql.SimpleThenCompounded,
    "COMPOUNDEDTHENSIMPLE": ql.CompoundedThenSimple
}

def _qCompounding(compounding : str) -> ql.Compounding:
    return enum_value(compounding, QL_COMPOUNDING)

@xlo.converter()
def qCompounding(compounding : str):
    return _qCompounding(compounding)

@xlo.func(
    help="Get the discount factor for a yield term structure.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
        "Date" : "The date for which to calculate the discount factor.",
        "Extrapolate" : "Whether to extrapolate if the date is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureDiscount(
    ytsh : ql.YieldTermStructureHandle,
    date : qDate,
    extrapolate : bool = False,
    Trigger = None,
    ) -> float:
    return ytsh.discount(date, extrapolate)

@xlo.func(
    help="Get the discount factor for a yield term structure from a time.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
        "Time" : "The time for which to calculate the discount factor.",
        "Extrapolate" : "Whether to extrapolate if the time is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureDiscountFromTime(
    ytsh : ql.YieldTermStructureHandle,
    time : float,
    extrapolate : bool = False,
    Trigger = None,
    ) -> float:
    return ytsh.discount(time, extrapolate)

@xlo.func(
    help="Get the zero rate for a yield term structure.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
        "Date" : "The date for which to calculate the zero rate.",
        "DayCounter" : "The day count convention to use for the calculation.",
        "Compounding" : "The compounding convention to use for the calculation.",
        "Frequency" : "The frequency to use for the calculation.",
        "Extrapolate" : "Whether to extrapolate if the date is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureZeroRate(
    ytsh : ql.YieldTermStructureHandle,
    date : qDate,
    daycounter : qDayCounter,
    compounding : qCompounding,
    frequency : qFrequency,
    extrapolate : bool = False,
    Trigger = None,
    ) -> float:
    return ytsh.zeroRate(date, daycounter, compounding, frequency, extrapolate).rate()

@xlo.func(
    help="Get the zero rate for a yield term structure from a time.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
        "Time" : "The time for which to calculate the zero rate.",
        "Compounding" : "The compounding convention to use for the calculation.",
        "Frequency" : "The frequency to use for the calculation.",
        "Extrapolate" : "Whether to extrapolate if the time is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureZeroRateFromTime(
    ytsh : ql.YieldTermStructureHandle,
    time : float,
    compounding : qCompounding,
    frequency : qFrequency,
    extrapolate : bool = False,
    Trigger = None,
    ) -> float:
    return ytsh.zeroRate(time, compounding, frequency, extrapolate).rate()

@xlo.func(
    help="Get the forward rate for a yield term structure.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
        "Date1" : "The start date for the forward rate calculation.",
        "Date2" : "The end date for the forward rate calculation.",
        "DayCounter" : "The day count convention to use for the calculation.",
        "Compounding" : "The compounding convention to use for the calculation.",
        "Frequency" : "The frequency to use for the calculation.",
        "Extrapolate" : "Whether to extrapolate if the dates are outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureForwardRate(
    ytsh : ql.YieldTermStructureHandle,
    date1 : qDate,
    date2 : qDate,
    daycounter : qDayCounter,
    compounding : qCompounding,
    frequency : qFrequency,
    extrapolate : bool = False,
    Trigger = None,
    ) -> float:
    return ytsh.forwardRate(date1, date2, daycounter, compounding, frequency, extrapolate).rate()

@xlo.func(
    help="Get the forward rate for a yield term structure from times.",
    args={
        "YieldTermStructureHandle" : "The yield term structure handle to query.",
        "Time1" : "The start time for the forward rate calculation.",
        "Time2" : "The end time for the forward rate calculation.",
        "Compounding" : "The compounding convention to use for the calculation.",
        "Frequency" : "The frequency to use for the calculation.",
        "Extrapolate" : "Whether to extrapolate if the times are outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYieldTermStructureForwardRateFromTime(
    ytsh : ql.YieldTermStructureHandle,
    time1 : float,
    time2 : float,
    compounding : qCompounding,
    frequency : qFrequency,
    extrapolate : bool = False,
    Trigger = None,
    ) -> float:
    return ytsh.forwardRate(time1, time2, compounding, frequency, extrapolate).rate()


## FlatForward

@xlo.func(
    help="Construct a flat forward curve from a reference date and a forward rate.",
    args={
        "ReferenceDate" : "The reference date for the curve.",
        "ForwardRate" : "The forward rate for the curve.",
        "DayCounter" : "The day count convention to use for the curve.",
        "Compounding" : "The compounding convention to use for the curve.",
        "Frequency" : "The frequency to use for the curve.",
        "Calendar" : "The calendar to use for the curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFlatForward(
    referenceDate : qDate,
    forwardRate : float,
    daycounter : qDayCounter = ql.Actual365Fixed(),
    compounding : qCompounding = ql.Compounded,
    frequency : qFrequency = ql.NoFrequency,
    calendar : qCalendar = ql.NullCalendar(),
    Trigger = None,
    ) -> ql.YieldTermStructureHandle:
    yts = ql.FlatForward(referenceDate, forwardRate, daycounter, compounding, frequency)
    return ql.YieldTermStructureHandle(yts)


## Implied term structure

@xlo.func(
    help="Construct an implied term structure from a base term structure and a reference date.",
    args={
        "YieldTermStructureHandle" : "The base yield term structure handle.",
        "ReferenceDate" : "The reference date for the implied term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlImpliedTermStructure(
    ytsh : ql.YieldTermStructureHandle,
    referenceDate : qDate,
    Trigger = None,
    ) -> ql.YieldTermStructureHandle:
    yts = ql.ImpliedTermStructure(ytsh, referenceDate)
    return ql.YieldTermStructureHandle(yts)

## Spreaded term structures

@xlo.func(
    help="Construct a zero spreaded term structure from a base term structure and a spread.",
    args={
        "YieldTermStructureHandle" : "The base yield term structure handle.",
        "Spread" : "The spread to add to the zero rates of the base term structure.",
        "Compounding" : "The compounding convention to use for the spread.",
        "Frequency" : "The frequency to use for the spread.",
        "DayCounter" : "The day count convention to use for the spread.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroSpreadedTermStructure(
    base : ql.YieldTermStructureHandle,
    spread : float,
    compounding : qCompounding = ql.Compounded,
    frequency : qFrequency = ql.NoFrequency,
    daycounter : qDayCounter = ql.Actual365Fixed(),
    Trigger = None,
    ) -> ql.YieldTermStructureHandle:
    sprad_qh = ql.QuoteHandle(ql.SimpleQuote(spread))
    yts = ql.ZeroSpreadedTermStructure(base, sprad_qh, compounding, frequency, daycounter)
    return ql.YieldTermStructureHandle(yts)


@xlo.func(
    help="Construct a forward spreaded term structure from a base term structure and a spread.",
    args={
        "YieldTermStructureHandle" : "The base yield term structure handle.",
        "Spread" : "The spread to add to the forward rates of the base term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlForwardSpreadedTermStructure(
    base : ql.YieldTermStructureHandle,
    spread : float,
    Trigger = None,
    ) -> ql.YieldTermStructureHandle:
    sprad_qh = ql.QuoteHandle(ql.SimpleQuote(spread))
    yts = ql.ForwardSpreadedTermStructure(base, sprad_qh)
    return ql.YieldTermStructureHandle(yts)


QL_COMPOSITE_OPERATORS = {
    "+": lambda z1, z2: z1 + z2,
    "-": lambda z1, z2: z1 - z2
}

@xlo.func(
    help="Construct a composite zero yield structure from two base term structures and an operator.",
    args={
        "Curve1" : "The first yield term structure handle.",
        "Curve2" : "The second yield term structure handle.",
        "Operator" : "The operator to combine the curves. Valid values are: +, -",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCompositeZeroYieldStructure(
    curve1 : ql.YieldTermStructureHandle,
    curve2 : ql.YieldTermStructureHandle,
    operator : str,
    Trigger = None,
    ) -> ql.YieldTermStructureHandle:
    if operator in QL_COMPOSITE_OPERATORS:
        yts = ql.CompositeZeroYieldStructure(curve1, curve2, QL_COMPOSITE_OPERATORS[operator])
    else:
        raise ValueError("Invalid operator. Valid values are: +, -")
    return ql.YieldTermStructureHandle(yts)