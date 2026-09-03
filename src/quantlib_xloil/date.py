import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import enum_value, first_key, UNKNOWN_KEY, UNKNOWN_VALUE

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


def _qDate(serialnumber) -> ql.Date:
    if isinstance(serialnumber, ql.Date):
        return serialnumber  # If it's already a QuantLib Date, return it as is.
    if isinstance(serialnumber, (int, float)):
        return ql.Date(
            round(serialnumber)
        )  # Excel dates are floats, but QuantLib Date expects an integer serial number.
    return ql.Date()  # default empty date value


def _qFrequency(s: str) -> int:
    return enum_value(s, QL_FREQUENCY)


def _qPeriod(s: str) -> ql.Period:
    if isinstance(s, ql.Period):  # handle default values
        return s
    return ql.Period(s)


def _qTimeUnit(s: str) -> int:
    return enum_value(s, QL_TIMEUNIT)


def _qWeekday(s: str) -> int:
    return enum_value(s, QL_WEEKDAY)


def _to_date_list(values) -> list[ql.Date]:
    return [_qDate(v) for v in values]


@xlo.converter()
def qDate(serialnumber) -> ql.Date:
    return _qDate(serialnumber)


@xlo.converter()
def qFrequency(s: str) -> int:
    return _qFrequency(s)


@xlo.converter()
def qPeriod(s: str) -> ql.Period:
    return _qPeriod(s)


@xlo.converter()
def qTimeUnit(s: str) -> int:
    return _qTimeUnit(s)


@xlo.converter()
def qWeekday(s: str) -> int:
    return _qWeekday(s)


@xlo.returner(target=ql.Date, register=True)
def xDate(date: ql.Date):
    return date.serialNumber()


@xlo.returner(target=ql.Period, register=True)
def xPeriod(period: ql.Period):
    return str(period)


@xlo.func(
    help="Create a QuantLib Period from an integer and a time unit.",
    args={
        "n": "The number of time units.",
        "unit": 'The time unit (e.g. "DAYS", "MONTHS", "YEARS").',
    },
    group=EXCEL_GROUP_NAME,
)
def qlPeriod(n: int, unit: qTimeUnit, trigger=None) -> ql.Period:
    return ql.Period(n, unit)


@xlo.func(
    help="Return Period length.",
    args={
        "period": "QuantLib Period.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPeriodLength(period: qPeriod, trigger=None) -> int:
    return period.length()


@xlo.func(
    help="Return Period time unit.",
    args={
        "period": "QuantLib Period.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPeriodUnits(period: qPeriod, trigger=None) -> qTimeUnit:
    return first_key(QL_TIMEUNIT, period.units(), UNKNOWN_VALUE)


@xlo.func(
    help="Return Period frequency.",
    args={
        "period": "QuantLib Period.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPeriodFrequency(period: qPeriod, trigger=None) -> qFrequency:
    return first_key(QL_FREQUENCY, period.frequency(), ql.NoFrequency)


@xlo.func(
    help="Return a normalized version of a QuantLib Period.",
    args={
        "period": "QuantLib Period.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPeriodNormalized(period: qPeriod, trigger=None) -> ql.Period:
    return period.normalized()


@xlo.func(
    help="Create a QuantLib Date from year, month and day.",
    args={
        "year": "The year.",
        "month": "The month.",
        "day": "The day.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDate(year: int, month: int, day: int, trigger=None) -> ql.Date:
    return ql.Date(day, month, year)


@xlo.func(
    help="Return the weekday of a QuantLib Date.",
    args={
        "date": "QuantLib Date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateWeekday(date: qDate, trigger=None) -> str:
    return first_key(QL_WEEKDAY, date.weekday(), UNKNOWN_VALUE)


@xlo.func(
    help="Return the day of the month of a QuantLib Date.",
    args={
        "date": "QuantLib Date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateDayOfMonth(date: qDate, trigger=None) -> int:
    return date.dayOfMonth()


@xlo.func(
    help="Return the day of the year of a QuantLib Date.",
    args={
        "date": "QuantLib Date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateDayOfYear(date: qDate, trigger=None) -> int:
    return date.dayOfYear()


@xlo.func(
    help="Return the month of a QuantLib Date.",
    args={
        "date": "QuantLib Date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateMonth(date: qDate, trigger=None) -> int:
    return date.month()


@xlo.func(
    help="Return the year of a QuantLib Date.",
    args={
        "date": "QuantLib Date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateYear(date: qDate, trigger=None) -> int:
    return date.year()


@xlo.func(
    help="Return whether a year is a leap year.",
    args={
        "year": "The year.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateIsLeap(year: int, trigger=None) -> bool:
    return ql.Date.isLeap(year)


@xlo.func(
    help="Return the QuantLib's minimum date.",
    group=EXCEL_GROUP_NAME,
)
def qlDateMinDate(trigger=None) -> ql.Date:
    return ql.Date.minDate()


@xlo.func(
    help="Return the QuantLib's maximum date.",
    group=EXCEL_GROUP_NAME,
)
def qlDateMaxDate(trigger=None) -> ql.Date:
    return ql.Date.maxDate()


@xlo.func(
    help="Return the QuantLib's today's date.",
    group=EXCEL_GROUP_NAME,
)
def qlDateTodaysDate(trigger=None) -> ql.Date:
    return ql.Date.todaysDate()


@xlo.func(
    help="Return the start of the month for a given QuantLib Date.",
    args={
        "date": "QuantLib Date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateStartOfMonth(date: qDate, trigger=None) -> ql.Date:
    return ql.Date.startOfMonth(date)


@xlo.func(
    help="Return the end of the month for a given QuantLib Date.",
    args={
        "date": "QuantLib Date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateEndOfMonth(date: qDate, trigger=None) -> ql.Date:
    return ql.Date.endOfMonth(date)


@xlo.func(
    help="Return whether a date is the start of the month.",
    args={
        "date": "QuantLib Date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateIsStartOfMonth(date: qDate, trigger=None) -> bool:
    return ql.Date.isStartOfMonth(date)


@xlo.func(
    help="Return whether a date is the end of the month.",
    args={
        "date": "QuantLib Date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateIsEndOfMonth(date: qDate, trigger=None) -> bool:
    return ql.Date.isEndOfMonth(date)


@xlo.func(
    help="Return the next date of a given weekday.",
    args={
        "date": "QuantLib Date.",
        "weekday": "The weekday.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateNextWeekday(date: qDate, weekday: qWeekday, trigger=None) -> ql.Date:
    return ql.Date.nextWeekday(date, weekday)


@xlo.func(
    help="Return the nth occurrence of a weekday in a month and year.",
    args={
        "n": "The occurrence (1 for first, 2 for second, etc.).",
        "weekday": "The weekday.",
        "month": "The month.",
        "year": "The year.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateNthWeekday(
    n: int, weekday: qWeekday, month: int, year: int, trigger=None
) -> ql.Date:
    return ql.Date.nthWeekday(n, weekday, month, year)


@xlo.func(
    help="Return whether a date is an ECB meeting date.",
    args={
        "date": "QuantLib Date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlECBIsECBDate(date: qDate, trigger=None) -> bool:
    return ql.ECB.isECBdate(date)


@xlo.func(
    help="Return whether a string is a valid ECB date code.",
    args={
        "ecb_code": "ECB date code string.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlECBIsECBCode(ecb_code: str, trigger=None) -> bool:
    return ql.ECB.isECBcode(ecb_code)


@xlo.func(
    help="Return ECB date code for a QuantLib Date.",
    args={
        "date": "QuantLib Date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlECBCode(date: qDate, trigger=None) -> str:
    return ql.ECB.code(date)


@xlo.func(
    help="Return ECB date for a month and year.",
    args={
        "month": "Month number.",
        "year": "Year.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlECBDate(month: int, year: int, trigger=None) -> ql.Date:
    return ql.ECB.date(month, year)


@xlo.func(
    help="Return ECB date for an ECB date code.",
    args={
        "ecb_code": "ECB date code string.",
        "reference_date": "Optional reference date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlECBDateFromCode(
    ecb_code: str,
    reference_date: qDate = ql.Date(),
    trigger=None,
) -> ql.Date:
    return ql.ECB.date(ecb_code, reference_date)


@xlo.func(
    help="Return next ECB date from a reference date.",
    args={
        "date": "Optional reference date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlECBNextDate(date: qDate = ql.Date(), trigger=None) -> ql.Date:
    return ql.ECB.nextDate(date)


@xlo.func(
    help="Return next ECB date from an ECB date code.",
    args={
        "ecb_code": "ECB date code string.",
        "reference_date": "Optional reference date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlECBNextDateFromCode(
    ecb_code: str,
    reference_date: qDate = ql.Date(),
    trigger=None,
) -> ql.Date:
    return ql.ECB.nextDate(ecb_code, reference_date)


@xlo.func(
    help="Return all next ECB dates from a reference date.",
    args={
        "date": "Optional reference date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlECBNextDates(date: qDate = ql.Date(), trigger=None) -> list:
    return list(ql.ECB.nextDates(date))


@xlo.func(
    help="Return all next ECB dates from an ECB date code.",
    args={
        "ecb_code": "ECB date code string.",
        "reference_date": "Optional reference date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlECBNextDatesFromCode(
    ecb_code: str,
    reference_date: qDate = ql.Date(),
    trigger=None,
) -> list:
    return list(ql.ECB.nextDates(ecb_code, reference_date))


@xlo.func(
    help="Return next ECB date code from a reference date.",
    args={
        "date": "Optional reference date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlECBNextCode(date: qDate = ql.Date(), trigger=None) -> str:
    return ql.ECB.nextCode(date)


@xlo.func(
    help="Return next ECB date code from an ECB date code.",
    args={
        "ecb_code": "ECB date code string.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlECBNextCodeFromCode(ecb_code: str, trigger=None) -> str:
    return ql.ECB.nextCode(ecb_code)


@xlo.func(
    help="Parse a date string using a specified format.",
    args={
        "date_string": "The date string to parse.",
        "format_string": 'The format string (e.g. "YYYY-MM-DD").',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateParserParseFormatted(
    date_string: str, format_string: str, trigger=None
) -> ql.Date:
    return ql.DateParser.parseFormatted(date_string, format_string)


@xlo.func(
    help="Parse a date string in ISO format.",
    args={
        "date_string": "The date string to parse.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDateParserParseISO(date_string: str, trigger=None) -> ql.Date:
    return ql.DateParser.parseISO(date_string)


@xlo.func(
    help="Parse a period string.",
    args={
        "period_string": "The period string to parse.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPeriodParserParse(period_string: str, trigger=None) -> ql.Period:
    return ql.PeriodParser.parse(period_string)
