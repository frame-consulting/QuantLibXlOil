import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate, qPeriod, qWeekday, qTimeUnit
from .utilities import first_key, UNKNOWN_KEY, UNKNOWN_VALUE, enum_value

# Todo BespokeCalendars, explicit JointCalendars, JointCalenders and USCalenders

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
    "UNITEDSTATES": ql.UnitedStates(ql.UnitedStates.NYSE),
    "UNITEDKINGDOM": ql.UnitedKingdom,
    #"UZBEKISTAN": ql.Uzbekistan,
    "NULLCALENDAR": ql.NullCalendar,
    "WEEKENDSONLY": ql.WeekendsOnly,
    "JOINTCALENDAR": ql.JointCalendar,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_BUSINESSDAYCONVENTION = {
    "FOLLOWING": ql.Following,
    "PRECEDING": ql.Preceding,
    "MODIFIEDFOLLOWING": ql.ModifiedFollowing,
    "MODIFIEDPRECEDING": ql.ModifiedPreceding,
    "UNADJUSTED": ql.Unadjusted,
    "HALFMONTHMODIFIEDFOLLOWING": ql.HalfMonthModifiedFollowing,
    "NEAREST": ql.Nearest,
}

QL_JOINTCALENDARRULE = {
    "JOINHOLIDAYS": ql.JoinHolidays,
    "JOINBUSINESSDAYS": ql.JoinBusinessDays,
}

def _qCalendar(name : str) -> ql.Calendar:
    if isinstance(name, ql.Calendar): # capture default argument values
        return name
    if isinstance(name, str):
        name = name.strip().upper()
        if name in QL_CALENDAR:
            return QL_CALENDAR[name]()
    raise ValueError(f"Unknown calendar: {name}")

@xlo.converter()
def qCalendar(calendarname : str) -> ql.Calendar:
    return _qCalendar(calendarname)

@xlo.returner(target=ql.Calendar, register=True)
def xCalendar(calendar : ql.Calendar):
    return calendar.name()

def _qBusinessDayConvention(conventionname : str):
    return enum_value(conventionname, QL_BUSINESSDAYCONVENTION)

@xlo.converter()
def qBusinessDayConvention(conventionname : str):
    return _qBusinessDayConvention(conventionname)


def _qJointCalendarRule(rule_name : str):
    return enum_value(rule_name, QL_JOINTCALENDARRULE)

@xlo.converter()
def qJointCalendarRule(rule_name : str):
    return _qJointCalendarRule(rule_name)

@xlo.func(
    help='Return a QuantLib Calendar object given its name.',
    args={
        'calendar_name': 'The name of the calendar.',
    },
    group=EXCEL_GROUP_NAME,
)

def qlCalendar(calendar_name: str, trigger = None) -> ql.Calendar:
    return _qCalendar(calendar_name)

@xlo.func(
    help='Check if a day is a weekend day.',
    args={
        'weekday': 'The day of the week (0=Sunday, 1=Monday, ..., 6=Saturday).',
    },
    group=EXCEL_GROUP_NAME,
)  
def qlCalendarisWeekend(calendar: qCalendar, weekday: qWeekday, trigger = None) -> bool:
    return calendar.isWeekend(weekday)
#weekday in (ql.Saturday, ql.Sunday)

@xlo.func(
    help='Return the first day of the month for a given date.',
    args={
        'date': 'The date for which to find the start of the month.',
    },
    group=EXCEL_GROUP_NAME,
)

def qlCalendarStartOfMonth(calendar : qCalendar, date : qDate, trigger = None) -> ql.Date:
    return calendar.startOfMonth(date) 
#l.Date(ql.startOfMonth(date))

@xlo.func(
    help='Return the last day of the month for a given date.',
    args={
        'date': 'The date for which to find the end of the month.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarEndOfMonth(calendar : qCalendar, date : qDate, trigger = None) -> ql.Date:
    return calendar.endOfMonth(date) 
#ql.Date(ql.endOfMonth(date))

@xlo.func(
    help='Check if a date is a business day.',
    args={
        'date': 'The date to check.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarIsBusinessDay(calendar : qCalendar, date : qDate, trigger = None) -> bool:
    return calendar.isBusinessDay(date)

@xlo.func(
    help='Check if a date is a holiday.',
    args={
        'date': 'The date to check.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarIsHoliday(calendar : qCalendar, date : qDate, trigger = None) -> bool:
    return calendar.isHoliday(date) 

@xlo.func(
    help='Check if a date is the end of the month.',
    args={
        'date': 'The date to check.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarIsEndOfMonth(calendar : qCalendar, date : qDate, trigger = None) -> bool:
    return calendar.isEndOfMonth(date)

@xlo.func(
    help='Check if a date is the start of the month.',
    args={
        'date': 'The date to check.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarIsStartOfMonth(calendar : qCalendar, date : qDate, trigger = None) -> bool:
    return calendar.isStartOfMonth(date)

@xlo.func(
    help='Add a holiday to the calendar.',
    args={
        'date': 'The date to add as a holiday.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarAddHoliday(calendar : qCalendar, date : qDate, trigger = None) -> None:
    calendar.addHoliday(date)

@xlo.func(
    help='Remove a holiday from the calendar.',
    args={
        'date': 'The date to remove as a holiday.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarRemoveHoliday(calendar :qCalendar, date : qDate, trigger = None) -> None:
    calendar.removeHoliday(date)

@xlo.func(
    help='Reset the added and removed holidays for the calendar.',
    args={},
    group=EXCEL_GROUP_NAME,
)
def qlCalendarResetAddedAndRemovedHolidays(calendar : qCalendar, trigger = None) -> None:
    calendar.resetAddedAndRemovedHolidays()


@xlo.func(
    help='Adjust a date according to the calendar and business day convention.',
    args={
        'date': 'The date to adjust.',
        'calendar': 'The calendar to use for adjustment.',
        'convention': 'The business day convention to apply.',
    },
    group=EXCEL_GROUP_NAME,
)

def qlCalendarAdjust(calendar : qCalendar, date : qDate,  convention : qBusinessDayConvention = "Following", trigger = None) -> ql.Date:
    return  calendar.adjust(date, convention)

@xlo.func(
    help='Advance a date by a given number of time units according to the calendar and business day convention.',
    args={
        'date': 'The date to advance.',
        'calendar': 'The calendar to use for advancement.',
        'n': 'The number of time units to advance',
        'unit': 'The time unit to advance (e.g. "DAYS", "MONTHS", "YEARS").',
        'convention': 'The business day convention to apply.',
        'end_of_month': 'Whether to adjust to the end of the month.',
    },
    group=EXCEL_GROUP_NAME,
)   
def qlCalendarAdvance(calendar : qCalendar, date : qDate, n : int, unit : qTimeUnit, convention : qBusinessDayConvention = "Following", end_of_month : bool = False, trigger = None) -> ql.Date:
    return calendar.advance(date, n, unit, convention, end_of_month)
   
@xlo.func(
    help='Advance a date by a given period according to the calendar and business day convention.',
    args={
        'date': 'The date to advance.',
        'calendar': 'The calendar to use for advancement.',
        'period': 'The period by which to advance.',
        'convention': 'The business day convention to apply.',
        'end_of_month': 'Whether to adjust to the end of the month.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarAdvance2(calendar : qCalendar, date : qDate, period : qPeriod, convention : qBusinessDayConvention = "Following", end_of_month : bool = False, trigger = None) -> ql.Date:
    return calendar.advance(date, period, convention, end_of_month)


@xlo.func(
    help='Return the number of business days between two QuantLib Dates according to the calendar.',
    args={
        'calendar': 'The calendar to use.',
        'from_date': 'The starting date.',
        'to_date': 'The ending date.',
        'include_first': 'Whether to include the first date.',
        'include_last': 'Whether to include the last date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarBusinessDaysBetween(calendar : qCalendar, from_date : qDate, to_date : qDate, include_first : bool = True, include_last : bool = False, trigger = None) -> int:
    return calendar.businessDaysBetween(from_date, to_date, include_first, include_last)

@xlo.func(
    help='Return the list of holidays in the calendar.',
    args={
        'calendar': 'The calendar for which to list holidays.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarHolidayList(calendar : qCalendar, from_date : qDate, to_date : qDate,trigger = None) -> list:
    return list(calendar.holidayList(from_date, to_date)) 


@xlo.func(
    help='Return the list of business days in the calendar.',
    args={
        'calendar': 'The calendar for which to list business days.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarBusinessDayList(calendar : qCalendar, from_date : qDate, to_date : qDate, trigger = None) -> list:
    return list(calendar.businessDayList(from_date, to_date))

@xlo.func(
    help='Return the name of the calendar.',
    args={
        'calendar': 'The calendar for which to get the name.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarName(calendar : qCalendar, trigger = None) -> str:
    return calendar.name()

@xlo.func(
    help='Check if the calendar is empty.',
    args={
        'calendar': 'The calendar to check.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarEmpty(calendar : qCalendar, trigger = None) -> bool:
    return calendar.empty()

@xlo.func(
    help='Return a calendar that represents the union of two calendars.',
    args={
        'calendar1': 'The first calendar.',
        'calendar2': 'The second calendar.',
        'rule': 'The rule for combining the calendars.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarJointCalendar(calendar1 : qCalendar, calendar2 : qCalendar, rule : qJointCalendarRule =  "JOINHOLIDAYS") -> ql.Calendar:
    return ql.JointCalendar(calendar1, calendar2, rule)

@xlo.func(
    help='Return a calendar that represents the union of three calendars.',
    args={
        'calendar1': 'The first calendar.',
        'calendar2': 'The second calendar.',
        'calendar3': 'The third calendar.',
        'rule': 'The rule for combining the calendars.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarJointCalendar2(calendar1 : qCalendar, calendar2 : qCalendar, calendar3 : qCalendar, rule : qJointCalendarRule =  "JOINHOLIDAYS", trigger = None) -> ql.Calendar:
    return ql.JointCalendar(calendar1, calendar2, calendar3, rule)





