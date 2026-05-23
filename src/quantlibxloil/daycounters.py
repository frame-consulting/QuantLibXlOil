import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import first_key, UNKNOWN_KEY, UNKNOWN_VALUE
from .date import qDate

QL_DAYCOUNTER = {
    "ACTUAL360": ql.Actual360(),
    "ACTUAL364": ql.Actual364(),
    "ACTUAL36525": ql.Actual36525(),
    "ACTUAL365FIXED": ql.Actual365Fixed(),
    "ACTUAL366": ql.Actual366(),
    "ACTUALACTUAL": ql.ActualActual(ql.ActualActual.ISMA),
    "BUSINESS252": ql.Business252(),
    "ONEDAYCOUNTER": ql.OneDayCounter(),
    "SIMPLEDAYCOUNTER": ql.SimpleDayCounter(),
    "THIRTY360": ql.Thirty360(ql.Thirty360.ISMA),
    "THIRTY365": ql.Thirty365(),
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

def _qDayCounter(name: str) -> ql.DayCounter:
    daycounter = QL_DAYCOUNTER.get(name.upper())
    if daycounter is None:
        raise ValueError(f"Unknown day counter: {name}")
    return daycounter

@xlo.converter()
def qDayCounter(s : str) -> ql.DayCounter:
    return _qDayCounter(s)

@xlo.returner(target=ql.DayCounter, register=True)
def xDayCounter(daycounter : ql.DayCounter):
    return daycounter.name()

@xlo.func(
    help='Create a QuantLib DayCounter object from a name.',
    args={
        'DayCounter': 'The name of the day count convention.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDayCounter(daycounter_name : str, Trigger = None) -> ql.DayCounter:
    return _qDayCounter(daycounter_name)

@xlo.func(
    help='Return the day count between two dates using the given day counter.',
    args={
        'DayCounter': 'QuantLib DayCounter.',
        'StartDate': 'Start date.',
        'EndDate': 'End date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDayCounterDayCount(daycounter : qDayCounter, start_date : qDate, end_date : qDate, Trigger = None) -> int:
    return daycounter.dayCount(start_date, end_date)


@xlo.func(
    help='Return the year fraction between two dates using the given day counter.',
    args={
        'DayCounter': 'QuantLib DayCounter.',
        'StartDate': 'Start date.',
        'EndDate': 'End date.',
        'RefStartDate': 'Reference start date (optional).',
        'RefEndDate': 'Reference end date (optional).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDayCounterYearFraction(daycounter : qDayCounter, start_date : qDate, end_date : qDate, ref_start_date : qDate = ql.Date(), ref_end_date : qDate = ql.Date(), Trigger = None) -> float:
    return daycounter.yearFraction(start_date, end_date, ref_start_date, ref_end_date)

@xlo.func(
    help='Return the name of a QuantLib DayCounter.',
    args={
        'DayCounter': 'QuantLib DayCounter.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDayCounterName(daycounter : qDayCounter, Trigger = None) -> str:
    return daycounter.name()


@xlo.func(
    help='Check if a QuantLib DayCounter is empty (i.e., not initialized).',
    args={      'DayCounter': 'QuantLib DayCounter.',   },
    group=EXCEL_GROUP_NAME,
)
def qlDayCounterEmpty(daycounter : qDayCounter, Trigger = None) -> bool:
    return daycounter.empty()


@xlo.func(
    help='Return the date corresponding to a given year fraction from a reference date using the specified day counter.',
    args={
        'DayCounter': 'QuantLib DayCounter.',
        'RefDate': 'Reference date.',
        'YearFraction': 'Year fraction to convert to a date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDayCounterYearFractionToDate(daycounter : qDayCounter, RefDate : qDate, YearFraction : float, Trigger = None) -> qDate:
    return ql.yearFractionToDate(daycounter, RefDate, YearFraction)
