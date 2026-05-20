import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import first_key, UNKNOWN_KEY, UNKNOWN_VALUE

QL_WEEKDAY = {
    "MONDAY": ql.Monday,
    "TUESDAY": ql.Tuesday,
    "WEDNESDAY": ql.Wednesday,
    "THURSDAY": ql.Thursday,
    "FRIDAY": ql.Friday,
    "SATURDAY": ql.Saturday,
    "SUNDAY": ql.Sunday,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_FREQUENCY = {
    "ANNUAL": ql.Annual,
    "BIMONTHLY": ql.Bimonthly,
    "BIWEEKLY": ql.Biweekly,
    "DAILY": ql.Daily,
    "EVERYFOURTHMONTH": ql.EveryFourthMonth,
    "EVERYFOURTHWEEK": ql.EveryFourthWeek,
    "MONTHLY": ql.Monthly,
    "NOFREQUENCY": ql.NoFrequency,
    "ONCE": ql.Once,
    "OTHERFREQUENCY": ql.OtherFrequency,
    "QUARTERLY": ql.Quarterly,
    "SEMIANNUAL": ql.Semiannual,
    "WEEKLY": ql.Weekly,
}

QL_TIMEUNIT = {
    "DAYS": ql.Days,
    "HOURS": ql.Hours,
    "MICROSECONDS": ql.Microseconds,
    "MILLISECONDS": ql.Milliseconds,
    "MINUTES": ql.Minutes,
    "MONTHS": ql.Months,
    "SECONDS": ql.Seconds,
    "WEEKS": ql.Weeks,
    "YEARS": ql.Years,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

@xlo.converter()
def qWeekday(s : str) -> int:
    return QL_WEEKDAY.get(s.upper())

@xlo.converter()
def qFrequency(s : str) -> int:
    return QL_FREQUENCY.get(s.upper())

@xlo.converter()
def qTimeUnit(s : str) -> int:
    return QL_TIMEUNIT.get(s.upper())

@xlo.converter()
def qPeriod(s : str) -> ql.Period:
    return ql.Period(s)

@xlo.returner(target=ql.Period, register=True)
def xPeriod(period : ql.Period):
  return str(period)

@xlo.func(
    help='Create a QuantLib Period from an integer and a time unit.',
    args={
        'n': 'The number of time units.',
        'unit': 'The time unit (e.g. "DAYS", "MONTHS", "YEARS").',
    },
    group=EXCEL_GROUP_NAME,
)
def qlPeriod(n : int, unit : qTimeUnit, Trigger = None) -> ql.Period:
    return ql.Period(n, unit)

@xlo.func(
    help='Return Period length.',
    args={
        'Period': 'QuantLib Period.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlPeriodLength(period : qPeriod, Trigger = None) -> int:
    return period.length()

@xlo.func(
    help='Return Period time unit.',
    args={
        'Period': 'QuantLib Period.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlPeriodUnits(period : qPeriod, Trigger = None) -> qTimeUnit:
    return first_key(QL_TIMEUNIT, period.units(), UNKNOWN_VALUE)

@xlo.func(
    help='Return Period frequency.',
    args={
        'Period': 'QuantLib Period.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlPeriodFrequency(period : qPeriod, Trigger = None) -> qFrequency:
    return first_key(QL_FREQUENCY, period.frequency(), ql.NoFrequency)

@xlo.func(
    help='Return a normalized version of a QuantLib Period.',
    args={
        'Period': 'QuantLib Period.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlPeriodNormalized(period : qPeriod, Trigger = None) -> qPeriod:
    return period.normalized()


@xlo.converter()
def qDate(serialnumber) -> ql.Date:
    if serialnumber is None or (isinstance(serialnumber, str) and not serialnumber.strip()):
        return None
    return ql.Date(round(serialnumber))  # Excel dates are floats, but QuantLib Date expects an integer serial number.

@xlo.returner(target=ql.Date, register=True)
def xDate(date : ql.Date):
    return date.serialNumber()

@xlo.func(
    help='Create a QuantLib Date from year, month and day.',
    args={
        'Year': 'The year.',
        'Month': 'The month.',
        'Day': 'The day.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDate(year : int, month : int, day : int, Trigger = None) -> ql.Date:
    return ql.Date(day, month, year)

@xlo.func(
    help='Return the weekday of a QuantLib Date.',
    args={
        'Date': 'QuantLib Date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateWeekday(date : qDate, Trigger = None) -> str:
    return first_key(QL_WEEKDAY, date.weekday(), UNKNOWN_VALUE)

@xlo.func(
    help='Return the day of the month of a QuantLib Date.',
    args={
        'Date': 'QuantLib Date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateDayOfMonth(date : qDate, Trigger = None) -> int:
    return date.dayOfMonth()

@xlo.func(
    help='Return the day of the year of a QuantLib Date.',
    args={
        'Date': 'QuantLib Date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateDayOfYear(date : qDate, Trigger = None) -> int:
    return date.dayOfYear()

@xlo.func(
    help='Return the month of a QuantLib Date.',
    args={
        'Date': 'QuantLib Date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateMonth(date : qDate, Trigger = None) -> int:
    return date.month()

@xlo.func(
    help='Return the year of a QuantLib Date.',
    args={
        'Date': 'QuantLib Date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateYear(date : qDate, Trigger = None) -> int:
    return date.year()

@xlo.func(
    help='Return whether a year is a leap year.',
    args={
        'Year': 'The year.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateIsLeap(year : int, Trigger = None) -> bool:
    return ql.Date.isLeap(year)

@xlo.func(
    help='Return the QuantLib\'s minimum date.',
    group=EXCEL_GROUP_NAME,
)
def qlDateMinDate(Trigger = None) -> ql.Date:
    return ql.Date.minDate()

@xlo.func(
    help='Return the QuantLib\'s maximum date.',
    group=EXCEL_GROUP_NAME,
)
def qlDateMaxDate(Trigger = None) -> ql.Date:
    return ql.Date.maxDate()

@xlo.func(
    help='Return the QuantLib\'s today\'s date.',
    group=EXCEL_GROUP_NAME,
)
def qlDateTodaysDate(Trigger = None) -> ql.Date:
    return ql.Date.todaysDate()

@xlo.func(
    help='Return the start of the month for a given QuantLib Date.',
    args={
        'Date': 'QuantLib Date.',
    },
)
def qlDateStartOfMonth(date : qDate, Trigger = None) -> ql.Date:
    return ql.Date.startOfMonth(date)

@xlo.func(
    help='Return the end of the month for a given QuantLib Date.',
    args={
        'Date': 'QuantLib Date.',
    },
)
def qlDateEndOfMonth(date : qDate, Trigger = None) -> ql.Date:
    return ql.Date.endOfMonth(date)

@xlo.func(
    help='Return whether a date is the start of the month.',
    args={
        'Date': 'QuantLib Date.',
    },
)
def qlDateIsStartOfMonth(date : qDate, Trigger = None) -> bool:
    return ql.Date.isStartOfMonth(date)

@xlo.func(
    help='Return whether a date is the end of the month.',
    args={
        'Date': 'QuantLib Date.',
    },
)
def qlDateIsEndOfMonth(date : qDate, Trigger = None) -> bool:
    return ql.Date.isEndOfMonth(date)

@xlo.func(
    help='Return the next date of a given weekday.',
    args={
        'Date': 'QuantLib Date.',
        'Weekday': 'The weekday.',
    },
)
def qlDateNextWeekday(date : qDate, weekday : qWeekday, Trigger = None) -> ql.Date:
    return ql.Date.nextWeekday(date, weekday)

@xlo.func(
    help='Return the nth occurrence of a weekday in a month and year.',
    args={
        'N': 'The occurrence (1 for first, 2 for second, etc.).',
        'Weekday': 'The weekday.',
        'Month': 'The month.',
        'Year': 'The year.',
    },
)
def qlDateNthWeekday(n : int, weekday : qWeekday, month : int, year : int, Trigger = None) -> ql.Date:
    return ql.Date.nthWeekday(n, weekday, month, year)


@xlo.func(
    help='Parse a date string using a specified format.',
    args={
        'DateString': 'The date string to parse.',
        'FormatString': 'The format string (e.g. "YYYY-MM-DD").',
    },
)
def qlDateParserParseFormatted(date_string : str, format_string : str, Trigger = None) -> ql.Date:
    return ql.DateParser.parseFormatted(date_string, format_string)

@xlo.func(
    help='Parse a date string in ISO format.',
    args={
        'DateString': 'The date string to parse.',
    },
)
def qlDateParserParseISO(date_string : str, Trigger = None) -> ql.Date:
    return ql.DateParser.parseISO(date_string)

@xlo.func(
    help='Parse a period string.',
    args={
        'PeriodString': 'The period string to parse.',
    },
)
def qlPeriodParserParse(period_string : str, Trigger = None) -> ql.Period:
    return ql.PeriodParser.parse(period_string)
