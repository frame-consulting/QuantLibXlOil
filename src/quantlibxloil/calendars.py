import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate, qWeekday
from .utilities import first_key, UNKNOWN_KEY, UNKNOWN_VALUE


QL_CALENDAR= {
    "ARGENTINA": ql.Argentina,
    "AUSTRALIA": ql.Australia, 
    "AUSTRIA": ql.Austria,
    "BOTSWANA": ql.Botswana,
    "BRAZIL": ql.Brazil,
    "CANADA": ql.Canada,
    "CHILE": ql.Chile,
    "CHINA": ql.China, 
    "CZECHREPUBLIC": ql.CzechRepublic,
    "DENMARK": ql.Denmark,
    "FINLAND": ql.Finland,
    "FRANCE": ql.France,
    "GERMANY": ql.Germany,
    "HONGKONG": ql.HongKong,
    "HUNGARY": ql.Hungary,
    "ICELAND": ql.Iceland,
    "INDIA": ql.India,
    "INDONESIA": ql.Indonesia,
    "ISRAEL": ql.Israel,
    "ITALY": ql.Italy,
    "JAPAN": ql.Japan,
    #"MALTA": ql.Malta,
    "MEXICO": ql.Mexico,
    #"MONTENEGRO": ql.Montenegro,
    "NEWZEALAND": ql.NewZealand,
    #"NORTHMACEDONIA": ql.NorthMacedonia,
    "NORWAY": ql.Norway,
    "POLAND": ql.Poland,
    "ROMANIA": ql.Romania,
    "RUSSIA": ql.Russia,
    "SAUDIARABIA": ql.SaudiArabia,
    #"SERBIA": ql.Serbia,
    "SINGAPORE": ql.Singapore,
    "SLOVAKIA": ql.Slovakia,
    #"SLOVENIA": ql.Slovenia,
    "SOUTHAFRICA": ql.SouthAfrica,
    "SOUTHKOREA": ql.SouthKorea,
    "SWEDEN": ql.Sweden,
    "SWITZERLAND": ql.Switzerland,
    "TAIWAN": ql.Taiwan,
    "TARGET": ql.TARGET,
    "THAILAND": ql.Thailand,
    "TURKEY": ql.Turkey,
    "UKRAINE": ql.Ukraine,
    "UNITEDSTATES": ql.UnitedStates,
    "UNITEDKINGDOM": ql.UnitedKingdom,
    #"UZBEKISTAN": ql.Uzbekistan,
    "NULLCALENDAR": ql.NullCalendar,
    "WEEKENDSONLY": ql.WeekendsOnly,
    "JOINTCALENDAR": ql.JointCalendar,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_BUSINESSDAYCONVENTION = {
    "Following": ql.Following,
    "Preceding": ql.Preceding,
    "ModifiedFollowing": ql.ModifiedFollowing,
    "ModifiedPreceding": ql.ModifiedPreceding,
    "Unadjusted": ql.Unadjusted,
    "HalfMonthModifiedFollowing": ql.HalfMonthModifiedFollowing,
    "Nearest": ql.Nearest,
}

QL_MARKET = {
    "NYSE": ql.NYSE,
    "LSE": ql.LSE,
    "TSE": ql.TSE,
    "HKEX": ql.HKEX,
    "SSE": ql.SSE,
    "BSE": ql.BSE,
    "NSE": ql.NSE,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_JOINTCALENDARRULE = {
    "JoinHolidays": ql.JoinHolidays,
    "JoinBusinessDays": ql.JoinBusinessDays,
}

def _calendars_by_name(name: str) -> ql.Calendar:
    if name is None:
        return ql.NullCalendar()
    name = str(name).strip()
    if not name:
        return ql.NullCalendar()
    calendar = QL_CALENDAR.get(name.upper())
    if calendar is UNKNOWN_VALUE or calendar is None:
        raise ValueError(f"Unknown calendar: {name}")
    return calendar()

@xlo.converter()
def qCalendar(calendarname : str) -> ql.Calendar:
    return _calendars_by_name(calendarname)

@xlo.returner(target=ql.Calendar, register=True)
def xCalendar(calendar : ql.Calendar):
    return calendar.name()


@xlo.func(
    help='Return a QuantLib Calendar object given its name.',
    args={
        'CalendarName': 'The name of the calendar.',
    },
    group=EXCEL_GROUP_NAME,
)

def qlCalendar(calendar_name: str, Trigger = None) -> ql.Calendar:
    return _calendars_by_name(calendar_name)

@xlo.func(
    help='Check if a day is a weekend day.',
    args={
        'Weekday': 'The day of the week (0=Sunday, 1=Monday, ..., 6=Saturday).',
    },
    group=EXCEL_GROUP_NAME,
)   
def qlCalendarisWeekend(calendar: qCalendar, weekday: qWeekday, Trigger = None) -> bool:
    return calendar.isWeekend(weekday)
#weekday in (ql.Saturday, ql.Sunday)

@xlo.func(
    help='Return the first day of the month for a given date.',
    args={
        'Date': 'The date for which to find the start of the month.',
    },
    group=EXCEL_GROUP_NAME,
)

def qlCalendarStartOfMonth(calendar : qCalendar, date : qDate, Trigger = None) -> ql.Date:
    return calendar.startOfMonth(date) 
#l.Date(ql.startOfMonth(date))

@xlo.func(
    help='Return the last day of the month for a given date.',
    args={
        'Date': 'The date for which to find the end of the month.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarEndOfMonth(calendar : qCalendar, date : qDate, Trigger = None) -> ql.Date:
    return calendar.endOfMonth(date) 
#ql.Date(ql.endOfMonth(date))

@xlo.func(
    help='Check if a date is a business day.',
    args={
        'Date': 'The date to check.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarIsBusinessDay(calendar : qCalendar, date : qDate, Trigger = None) -> bool:
    return calendar.isBusinessDay(date)

@xlo.func(
    help='Check if a date is a holiday.',
    args={
        'Date': 'The date to check.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarIsHoliday(calendar : qCalendar, date : qDate, Trigger = None) -> bool:
    return calendar.isHoliday(date) 

@xlo.func(
    help='Check if a date is the end of the month.',
    args={
        'Date': 'The date to check.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarIsEndOfMonth(calendar : qCalendar, date : qDate, Trigger = None) -> bool:
    return calendar.isEndOfMonth(date)

@xlo.func(
    help='Check if a date is the start of the month.',
    args={
        'Date': 'The date to check.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarIsStartOfMonth(calendar : qCalendar, date : qDate, Trigger = None) -> bool:
    return calendar.isStartOfMonth(date)

@xlo.func(
    help='Add a holiday to the calendar.',
    args={
        'Date': 'The date to add as a holiday.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarAddHoliday(calendar : qCalendar, date : qDate, Trigger = None) -> None:
    calendar.addHoliday(date)

@xlo.func(
    help='Remove a holiday from the calendar.',
    args={
        'Date': 'The date to remove as a holiday.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarRemoveHoliday(calendar :qCalendar, date : qDate, Trigger = None) -> None:
    calendar.removeHoliday(date)

@xlo.func(
    help='Reset the added and removed holidays for the calendar.',
    args={},
    group=EXCEL_GROUP_NAME,
)
def qlCalendarResetAddedAndRemovedHolidays(calendar : qCalendar, Trigger = None) -> None:
    calendar.resetAddedAndRemovedHolidays()

"""
@xlo.func(
    help='Adjust a date according to the calendar and business day convention.',
    args={
        'Date': 'The date to adjust.',
        'Calendar': 'The calendar to use for adjustment.',
        'Convention': 'The business day convention to apply.',
    },
    group=EXCEL_GROUP_NAME,
)

def qlCalendarAdjust(date : ql.Date, calendar : ql.Calendar, convention : ql.BusinessDayConvention, Trigger = None) -> ql.Date:
    return calendar.adjust(date, convention)

@xlo.func(
    help='Advance a date by a given number of time units according to the calendar and business day convention.',
    args={
        'Date': 'The date to advance.',
        'Calendar': 'The calendar to use for advancement.',
        'N': 'The number of time units to advance.',
        'Unit': 'The time unit for advancement.',
        'Convention': 'The business day convention to apply.',
        'EndOfMonth': 'Whether to adjust to the end of the month.',
    },
    group=EXCEL_GROUP_NAME,
)   
def qlCalendarAdvance(calendar : ql.Calendar, date : ql.Date, n : int, unit : qTimeUnit, convention : ql.BusinessDayConvention, end_of_month : bool, Trigger = None) -> ql.Date:
    return calendar.advance(date, n, unit, convention, end_of_month)   

@xlo.func(
    help='Advance a date by a given period according to the calendar and business day convention.',
    args={
        'Date': 'The date to advance.',
        'Calendar': 'The calendar to use for advancement.',
        'Period': 'The period by which to advance.',
        'Convention': 'The business day convention to apply.',
        'EndOfMonth': 'Whether to adjust to the end of the month.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarAdvance(calendar : ql.Calendar, date : ql.Date, period : ql.Period, convention : ql.BusinessDayConvention, end_of_month : bool, Trigger = None) -> ql.Date:
    return calendar.advance(date, period, convention, end_of_month)

        """
@xlo.func(
    help='Return the number of business days between two QuantLib Dates according to the calendar.',
    args={
        'Calendar': 'The calendar to use.',
        'FromDate': 'The starting date.',
        'ToDate': 'The ending date.',
        'IncludeFirst': 'Whether to include the first date.',
        'IncludeLast': 'Whether to include the last date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarBusinessDaysBetween(calendar : qCalendar, from_date : qDate, to_date : qDate, includeFirst : bool = True, includeLast : bool = False, Trigger = None) -> int:
    return calendar.businessDaysBetween(from_date, to_date, includeFirst, includeLast)

@xlo.func(
    help='Return the list of holidays in the calendar.',
    args={
        'Calendar': 'The calendar for which to list holidays.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarHolidayList(calendar : qCalendar, from_date : qDate, to_date : qDate,Trigger = None) -> list:
    return list(calendar.holidayList(from_date, to_date)) 


@xlo.func(
    help='Return the list of business days in the calendar.',
    args={
        'Calendar': 'The calendar for which to list business days.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarBusinessDayList(calendar : qCalendar, from_date : qDate, to_date : qDate, Trigger = None) -> list:
    return list(calendar.businessDayList(from_date, to_date))

@xlo.func(
    help='Return the name of the calendar.',
    args={
        'Calendar': 'The calendar for which to get the name.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarName(calendar : qCalendar, Trigger = None) -> str:
    return calendar.name()

@xlo.func(
    help='Check if the calendar is empty.',
    args={
        'Calendar': 'The calendar to check.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarEmpty(calendar : qCalendar, Trigger = None) -> bool:
    return calendar.empty()

