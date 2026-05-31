import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import first_key, UNKNOWN_KEY, UNKNOWN_VALUE
from .date import qDate

QL_DAYCOUNTER = {
    "ACTUAL360": ql.Actual360,
    "ACTUAL364": ql.Actual364,
    "ACTUAL36525": ql.Actual36525,
    "ACTUAL365FIXED": ql.Actual365Fixed,
    "ACTUAL366": ql.Actual366,
    "ACTUALACTUAL": lambda : ql.ActualActual(ql.ActualActual.ISMA),
    "BUSINESS252": ql.Business252,
    "ONEDAYCOUNTER": ql.OneDayCounter,
    "SIMPLEDAYCOUNTER": ql.SimpleDayCounter,
    "THIRTY360": lambda :ql.Thirty360(ql.Thirty360.ISMA),
    "THIRTY365": ql.Thirty365,
    # display names
    "ACTUAL/360": ql.Actual360,
    "ACTUAL/364": ql.Actual364,
    "ACTUAL/365.25": ql.Actual36525,
    "ACTUAL/365 (FIXED)": ql.Actual365Fixed,
    "ACTUAL/366": ql.Actual366,
    "ACTUAL/ACTUAL (ISMA)": lambda : ql.ActualActual(ql.ActualActual.ISMA),
    "BUSINESS/252(BRAZIL)": ql.Business252,
    "1/1": ql.OneDayCounter,
    "SIMPLE": ql.SimpleDayCounter,
    "30/360 (BOND BASIS)": lambda :ql.Thirty360(ql.Thirty360.BondBasis),
    "30/365": ql.Thirty365,
    # short cuts
    "ACT/360": ql.Actual360,
    "ACT/365": ql.Actual365Fixed,
    "30/360" : lambda :ql.Thirty360(ql.Thirty360.BondBasis),
    #
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

def _qDayCounter(name: str) -> ql.DayCounter:
    if isinstance(name, ql.DayCounter):  # capture default argument values
        return name
    if isinstance(name, str):
        name = name.strip().upper()
        if name in QL_DAYCOUNTER:
            return QL_DAYCOUNTER[name]()
    raise ValueError(f"Unknown day counter: {name}")

@xlo.converter()
def qDayCounter(s : str) -> ql.DayCounter:
    return _qDayCounter(s)

@xlo.returner(target=ql.DayCounter, register=True)
def xDayCounter(daycounter : ql.DayCounter):
    return daycounter.name()

@xlo.func(
    help='Create a QuantLib DayCounter object from a name.',
    args={
        'daycounter_name': 'The name of the day count convention.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDayCounter(daycounter_name : str, trigger = None) -> ql.DayCounter:
    return _qDayCounter(daycounter_name)

@xlo.func(
    help='Return the day count between two dates using the given day counter.',
    args={
        'daycounter': 'QuantLib DayCounter.',
        'start_date': 'Start date.',
        'end_date': 'End date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDayCounterDayCount(daycounter : qDayCounter, start_date : qDate, end_date : qDate, trigger = None) -> int:
    return daycounter.dayCount(start_date, end_date)


@xlo.func(
    help='Return the year fraction between two dates using the given day counter.',
    args={
        'daycounter': 'QuantLib DayCounter.',
        'start_date': 'Start date.',
        'end_date': 'End date.',
        'ref_start_date': 'Reference start date (optional).',
        'ref_end_date': 'Reference end date (optional).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDayCounterYearFraction(daycounter : qDayCounter, start_date : qDate, end_date : qDate, ref_start_date : qDate = ql.Date(), ref_end_date : qDate = ql.Date(), trigger = None) -> float:
    return daycounter.yearFraction(start_date, end_date, ref_start_date, ref_end_date)

@xlo.func(
    help='Return the name of a QuantLib DayCounter.',
    args={
        'daycounter': 'QuantLib DayCounter.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDayCounterName(daycounter : qDayCounter, trigger = None) -> str:
    return daycounter.name()


@xlo.func(
    help='Check if a QuantLib DayCounter is empty (i.e., not initialized).',
    args={      'daycounter': 'QuantLib DayCounter.',   },
    group=EXCEL_GROUP_NAME,
)
def qlDayCounterEmpty(daycounter : qDayCounter, trigger = None) -> bool:
    return daycounter.empty()


@xlo.func(
    help='Return the date corresponding to a given year fraction from a reference date using the specified day counter.',
    args={
        'daycounter': 'QuantLib DayCounter.',
        'ref_date': 'Reference date.',
        'year_fraction': 'Year fraction to convert to a date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDayCounterYearFractionToDate(daycounter : qDayCounter, ref_date : qDate, year_fraction : float, trigger = None) -> qDate:
    return ql.yearFractionToDate(daycounter, ref_date, year_fraction)
