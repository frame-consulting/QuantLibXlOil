import QuantLib as ql
import re
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate, qPeriod, qTimeUnit, qWeekday
from .utilities import enum_value, UNKNOWN_KEY, UNKNOWN_VALUE

# JointCalendar and BespokeCalendar should cache by name so that instances
# with identical parameters reuse the same implementation instead of creating
# a new calendar each time.

_BESPOKE_CALENDAR_REGISTRY = {}
_JOINT_CALENDAR_REGISTRY = {}


def _get_or_create_bespoke_calendar(name: str) -> ql.BespokeCalendar:
    if name not in _BESPOKE_CALENDAR_REGISTRY:
        _BESPOKE_CALENDAR_REGISTRY[name] = ql.BespokeCalendar(name)
    return _BESPOKE_CALENDAR_REGISTRY[name]


def _get_or_create_joint_calendar(calendar_str: str) -> ql.Calendar:
    if calendar_str not in _JOINT_CALENDAR_REGISTRY:
        inside = calendar_str[len("JOINTCALENDAR(") : -1].strip()
        rule = ql.JoinHolidays
        valid_rules = "|".join(QL_JOINTCALENDARRULE.keys())
        rule_match = re.search(rf"rule\s*=\s*({valid_rules})", inside, re.IGNORECASE)
        if rule_match:
            rule_str = rule_match.group(1).upper()
            inside = re.sub(
                rf"rule\s*=\s*({valid_rules})", "", inside, flags=re.IGNORECASE
            ).strip()
            rule = QL_JOINTCALENDARRULE[rule_str]

        cal_names = [c.strip().upper() for c in inside.split(",") if c.strip()]
        if not cal_names:
            raise ValueError(f"Invalid JointCalendar syntax: {calendar_str}")

        calendars = _to_calendar_list(cal_names)

        if len(calendars) >= 2:
            _JOINT_CALENDAR_REGISTRY[calendar_str] = ql.JointCalendar(
                _to_calendar_list(cal_names), rule
            )
        else:
            raise ValueError(
                f"JointCalendar requires at least 2 calendars (got {len(calendars)})."
            )
    return _JOINT_CALENDAR_REGISTRY[calendar_str]


QL_CALENDAR = {
    "ARGENTINA": ql.Argentina,
    "BUENOS AIRES STOCK EXCHANGE": ql.Argentina,
    "AUSTRALIA": ql.Australia,
    "AUSTRALIA SETTLEMENT": ql.Australia,
    "AUSTRIA": ql.Austria,
    "AUSTRIAN SETTLEMENT": ql.Austria,
    "BOTSWANA": ql.Botswana,
    "BRAZIL": ql.Brazil,
    "BRAZIL_EXCHANGE": lambda: ql.Brazil(ql.Brazil.Exchange),
    "BOVESPA": lambda: ql.Brazil(ql.Brazil.Exchange),
    "CANADA": ql.Canada,
    "CANADA_TSX": lambda: ql.Canada(ql.Canada.TSX),
    "TSX": lambda: ql.Canada(ql.Canada.TSX),
    "CHILE": ql.Chile,
    "SANTIAGO STOCK EXCHANGE": ql.Chile,
    "CHINA": ql.China,
    "CHINA_IB": lambda: ql.China(ql.China.IB),
    "CHINA INTER BANK MARKET": lambda: ql.China(ql.China.IB),
    "SHANGHAI STOCK EXCHANGE": ql.China,
    "CROATIA": ql.Croatia,
    "ZAGREB STOCK EXCHANGE": ql.Croatia,
    "CZECHREPUBLIC": ql.CzechRepublic,
    "PRAGUE STOCK EXCHANGE": ql.CzechRepublic,
    "DENMARK": ql.Denmark,
    "FINLAND": ql.Finland,
    "FRANCE": ql.France,
    "FRENCH SETTLEMENT": ql.France,
    "FRANCE_EXCHANGE": lambda: ql.France(ql.France.Exchange),
    "PARIS STOCK EXCHANGE": lambda: ql.France(ql.France.Exchange),
    "GERMANY": ql.Germany,
    "FRANKFURT STOCK EXCHANGE": ql.Germany,
    "GERMANY_SETTLEMENT": lambda: ql.Germany(ql.Germany.Settlement),
    "GERMAN SETTLEMENT": lambda: ql.Germany(ql.Germany.Settlement),
    "GERMANY_XETRA": lambda: ql.Germany(ql.Germany.Xetra),
    "XETRA": lambda: ql.Germany(ql.Germany.Xetra),
    "GERMANY_EUREX": lambda: ql.Germany(ql.Germany.Eurex),
    "EUREX": lambda: ql.Germany(ql.Germany.Eurex),
    "HONGKONG": ql.HongKong,
    "HONG KONG STOCK EXCHANGE": ql.HongKong,
    "HUNGARY": ql.Hungary,
    "ICELAND": ql.Iceland,
    "ICELAND STOCK EXCHANGE": ql.Iceland,
    "INDIA": ql.India,
    "NATIONAL STOCK EXCHANGE OF INDIA": ql.India,
    "INDONESIA": ql.Indonesia,
    "JAKARTA STOCK EXCHANGE": ql.Indonesia,
    "ISRAEL": ql.Israel,
    "TEL AVIV STOCK EXCHANGE": ql.Israel,
    "ISRAEL_TASE": lambda: ql.Israel(ql.Israel.TASE),
    "ISRAEL_SHIR": lambda: ql.Israel(ql.Israel.SHIR),
    "SHIR FIXING CALENDAR": lambda: ql.Israel(ql.Israel.SHIR),
    "ISRAEL_TELBOR": lambda: ql.Israel(ql.Israel.Telbor),
    "TELBOR FIXING CALENDAR": lambda: ql.Israel(ql.Israel.Telbor),
    "ITALY": ql.Italy,
    "ITALIAN SETTLEMENT": ql.Italy,
    "ITALY_EXCHANGE": lambda: ql.Italy(ql.Italy.Exchange),
    "MILAN STOCK EXCHANGE": lambda: ql.Italy(ql.Italy.Exchange),
    "JAPAN": ql.Japan,
    "MEXICO": ql.Mexico,
    "MEXICAN STOCK EXCHANGE": ql.Mexico,
    "MALTA": ql.Malta,
    "MALTA STOCK EXCHANGE": ql.Malta,
    "MALAYSIA": ql.Malaysia,
    "MONTENEGRO": ql.Montenegro,
    "MONTENEGRO STOCK EXCHANGE": ql.Montenegro,
    "NORTHMACEDONIA": ql.NorthMacedonia,
    "MACEDONIAN STOCK EXCHANGE": ql.NorthMacedonia,
    "NEWZEALAND": ql.NewZealand,
    "NEW ZEALAND (WELLINGTON)": ql.NewZealand,
    "NEWZEALAND_AUCKLAND": lambda: ql.NewZealand(ql.NewZealand.Auckland),
    "NEW ZEALAND (AUCKLAND)": lambda: ql.NewZealand(ql.NewZealand.Auckland),
    "NORWAY": ql.Norway,
    "PHILIPPINES": ql.Philippines,
    "POLAND": ql.Poland,
    "POLAND SETTLEMENT": ql.Poland,
    "POLAND_WSE": lambda: ql.Poland(ql.Poland.WSE),
    "WARSAW STOCK EXCHANGE": lambda: ql.Poland(ql.Poland.WSE),
    "ROMANIA": ql.Romania,
    "BUCHAREST STOCK EXCHANGE": ql.Romania,
    "RUSSIA": ql.Russia,
    "RUSSIAN SETTLEMENT": ql.Russia,
    "RUSSIA_MOEX": lambda: ql.Russia(ql.Russia.MOEX),
    "MOSCOW EXCHANGE": lambda: ql.Russia(ql.Russia.MOEX),
    "SAUDIARABIA": ql.SaudiArabia,
    "SERBIA": ql.Serbia,
    "BELGRADE STOCK EXCHANGE": ql.Serbia,
    "SINGAPORE": ql.Singapore,
    "SINGAPORE EXCHANGE": ql.Singapore,
    "SLOVAKIA": ql.Slovakia,
    "BRATISLAVA STOCK EXCHANGE": ql.Slovakia,
    "SLOVENIA": ql.Slovenia,
    "LJUBLJANA STOCK EXCHANGE": ql.Slovenia,
    "SOUTHAFRICA": ql.SouthAfrica,
    "SOUTH AFRICA": ql.SouthAfrica,
    "SOUTHKOREA": ql.SouthKorea,
    "SOUTH-KOREA EXCHANGE": ql.SouthKorea,
    "SOUTHKOREA_SETTLEMENT": lambda: ql.SouthKorea(ql.SouthKorea.Settlement),
    "SOUTH-KOREAN SETTLEMENT": lambda: ql.SouthKorea(ql.SouthKorea.Settlement),
    "SWEDEN": ql.Sweden,
    "SWITZERLAND": ql.Switzerland,
    "TAIWAN": ql.Taiwan,
    "TAIWAN STOCK EXCHANGE": ql.Taiwan,
    "TARGET": ql.TARGET,
    "THAILAND": ql.Thailand,
    "THAILAND STOCK EXCHANGE": ql.Thailand,
    "TURKEY": ql.Turkey,
    "UKRAINE": ql.Ukraine,
    "UKRAINIAN STOCK EXCHANGE": ql.Ukraine,
    "UNITEDSTATES": lambda: ql.UnitedStates(ql.UnitedStates.NYSE),
    "UNITEDKINGDOM": ql.UnitedKingdom,
    "UZBEKISTAN": ql.Uzbekistan,
    "UZBEKISTAN STOCK EXCHANGE": ql.Uzbekistan,
    "NULLCALENDAR": ql.NullCalendar,
    "WEEKENDSONLY": ql.WeekendsOnly,
    "BESPOKECALENDAR": ql.BespokeCalendar,
    "JOINTCALENDAR": ql.JointCalendar,
    #
    "LONDON": ql.UnitedKingdom,
    "LDN": ql.UnitedKingdom,
    "NEWYORK": lambda: ql.UnitedStates(ql.UnitedStates.NYSE),
    "NYC": lambda: ql.UnitedStates(ql.UnitedStates.NYSE),
    #
    "UK_SETTLEMENT": lambda: ql.UnitedKingdom(ql.UnitedKingdom.Settlement),
    "UK_EXCHANGE": lambda: ql.UnitedKingdom(ql.UnitedKingdom.Exchange),
    "UK_METALS": lambda: ql.UnitedKingdom(ql.UnitedKingdom.Metals),
    #
    "US_SETTLEMENT": lambda: ql.UnitedStates(ql.UnitedStates.Settlement),
    "US_NYSE": lambda: ql.UnitedStates(ql.UnitedStates.NYSE),
    "US_GOVERNMENTBOND": lambda: ql.UnitedStates(ql.UnitedStates.GovernmentBond),
    "US_NERC": lambda: ql.UnitedStates(ql.UnitedStates.NERC),
    "US_LIBORIMPACT": lambda: ql.UnitedStates(ql.UnitedStates.LiborImpact),
    "US_FEDERALRESERVE": lambda: ql.UnitedStates(ql.UnitedStates.FederalReserve),
    "US_SOFR": lambda: ql.UnitedStates(ql.UnitedStates.SOFR),
    #
    "UK SETTLEMENT": ql.UnitedKingdom,
    "NEW YORK STOCK EXCHANGE": lambda: ql.UnitedStates(ql.UnitedStates.NYSE),
    #
    "LONDON STOCK EXCHANGE": lambda: ql.UnitedKingdom(ql.UnitedKingdom.Exchange),
    "LONDON METAL EXCHANGE": lambda: ql.UnitedKingdom(ql.UnitedKingdom.Metals),
    #
    "US SETTLEMENT": lambda: ql.UnitedStates(ql.UnitedStates.Settlement),
    "US GOVERNMENT BOND MARKET": lambda: ql.UnitedStates(
        ql.UnitedStates.GovernmentBond
    ),
    "NORTH AMERICAN ENERGY RELIABILITY COUNCIL": lambda: ql.UnitedStates(
        ql.UnitedStates.NERC
    ),
    "US WITH LIBOR IMPACT": lambda: ql.UnitedStates(ql.UnitedStates.LiborImpact),
    "FEDERAL RESERVE BANKWIRE SYSTEM": lambda: ql.UnitedStates(
        ql.UnitedStates.FederalReserve
    ),
    "SOFR FIXING CALENDAR": lambda: ql.UnitedStates(ql.UnitedStates.SOFR),
    #
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_BUSINESSDAYCONVENTION = {
    "FOLLOWING": ql.Following,
    "HALFMONTHMODIFIEDFOLLOWING": ql.HalfMonthModifiedFollowing,
    "MODIFIEDFOLLOWING": ql.ModifiedFollowing,
    "MODIFIEDPRECEDING": ql.ModifiedPreceding,
    "NEAREST": ql.Nearest,
    "PRECEDING": ql.Preceding,
    "UNADJUSTED": ql.Unadjusted,
    # short cuts
    "F": ql.Following,
    "H": ql.HalfMonthModifiedFollowing,
    "MF": ql.ModifiedFollowing,
    "MP": ql.ModifiedPreceding,
    "N": ql.Nearest,
    "P": ql.Preceding,
    "U": ql.Unadjusted,
}

QL_JOINTCALENDARRULE = {
    "JOINBUSINESSDAYS": ql.JoinBusinessDays,
    "JOINHOLIDAYS": ql.JoinHolidays,
}


def _to_calendar_list(values) -> list[ql.Calendar]:
    return [_qCalendar(v) for v in values]


def _qBusinessDayConvention(conventionname: str):
    return enum_value(conventionname, QL_BUSINESSDAYCONVENTION)


def _qCalendar(name: str) -> ql.Calendar:
    if isinstance(name, ql.Calendar):
        return name
    if isinstance(name, str):
        cal_str = name.strip().upper()
        if cal_str.startswith("BESPOKECALENDAR(") and cal_str.endswith(")"):
            inside = cal_str[len("BESPOKECALENDAR(") : -1].strip()
            if not inside:
                raise ValueError("BespokeCalendar requires a name")
            return _get_or_create_bespoke_calendar(inside)
        for rule_name, rule_value in QL_JOINTCALENDARRULE.items():
            prefix = rule_name + "("
            if cal_str.startswith(prefix) and cal_str.endswith(")"):
                inside = cal_str[len(prefix) : -1].strip()
                joint_cal_str = f"JOINTCALENDAR({inside}, rule={rule_name})"
                return _get_or_create_joint_calendar(joint_cal_str)

        if cal_str.startswith("JOINTCALENDAR(") and cal_str.endswith(")"):
            return _get_or_create_joint_calendar(cal_str)

        if cal_str in QL_CALENDAR:
            entry = QL_CALENDAR[cal_str]
            return entry() if callable(entry) else entry

    raise ValueError(f"Unknown calendar: {name}")


def _qJointCalendarRule(rule_name: str):
    return enum_value(rule_name, QL_JOINTCALENDARRULE)


@xlo.converter()
def qCalendar(calendarname: str) -> ql.Calendar:
    return _qCalendar(calendarname)


@xlo.converter()
def qBusinessDayConvention(conventionname: str) -> int:
    return _qBusinessDayConvention(conventionname)


@xlo.converter()
def qJointCalendarRule(rule_name: str):
    return _qJointCalendarRule(rule_name)


@xlo.returner(target=ql.Calendar, register=True)
def xCalendar(calendar: ql.Calendar):
    if isinstance(calendar, ql.BespokeCalendar):
        if calendar.name() not in _BESPOKE_CALENDAR_REGISTRY:
            _BESPOKE_CALENDAR_REGISTRY[calendar.name()] = calendar
        return f"BESPOKECALENDAR({calendar.name()})"
    elif isinstance(calendar, ql.JointCalendar):
        try:
            component_calendars = calendar.calendars()
            cal_names = [c.name() for c in component_calendars]
            cal_str = f"JOINTCALENDAR({','.join(cal_names)})"
            if cal_str not in _JOINT_CALENDAR_REGISTRY:
                _JOINT_CALENDAR_REGISTRY[cal_str] = calendar
            return cal_str
        except (AttributeError, TypeError):
            pass
    return calendar.name()


@xlo.func(
    help="Return a QuantLib Calendar object given its name.",
    args={
        "calendar_name": "The name of the calendar.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendar(calendar_name: str, trigger=None) -> ql.Calendar:
    return _qCalendar(calendar_name)


@xlo.func(
    help="Check if a day is a weekend day.",
    args={
        "weekday": "The day of the week (0=Sunday, 1=Monday, ..., 6=Saturday).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarisWeekend(calendar: qCalendar, weekday: qWeekday, trigger=None) -> bool:
    return calendar.isWeekend(weekday)


@xlo.func(
    help="Return the first day of the month for a given date.",
    args={
        "date": "The date for which to find the start of the month.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarStartOfMonth(calendar: qCalendar, date: qDate, trigger=None) -> ql.Date:
    return calendar.startOfMonth(date)


@xlo.func(
    help="Return the last day of the month for a given date.",
    args={
        "date": "The date for which to find the end of the month.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarEndOfMonth(calendar: qCalendar, date: qDate, trigger=None) -> ql.Date:
    return calendar.endOfMonth(date)


@xlo.func(
    help="Check if a date is a business day.",
    args={
        "date": "The date to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarIsBusinessDay(calendar: qCalendar, date: qDate, trigger=None) -> bool:
    return calendar.isBusinessDay(date)


@xlo.func(
    help="Check if a date is a holiday.",
    args={
        "date": "The date to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarIsHoliday(calendar: qCalendar, date: qDate, trigger=None) -> bool:
    return calendar.isHoliday(date)


@xlo.func(
    help="Check if a date is the end of the month.",
    args={
        "date": "The date to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarIsEndOfMonth(calendar: qCalendar, date: qDate, trigger=None) -> bool:
    return calendar.isEndOfMonth(date)


@xlo.func(
    help="Check if a date is the start of the month.",
    args={
        "date": "The date to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarIsStartOfMonth(calendar: qCalendar, date: qDate, trigger=None) -> bool:
    return calendar.isStartOfMonth(date)


@xlo.func(
    help="Add a holiday to the calendar.",
    args={
        "date": "The date to add as a holiday.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarAddHoliday(calendar: qCalendar, date: qDate, trigger=None) -> bool:
    calendar.addHoliday(date)
    return True


@xlo.func(
    help="Remove a holiday from the calendar.",
    args={
        "date": "The date to remove as a holiday.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarRemoveHoliday(calendar: qCalendar, date: qDate, trigger=None) -> bool:
    calendar.removeHoliday(date)
    return True


@xlo.func(
    help="Reset the added and removed holidays for the calendar.",
    args={},
    group=EXCEL_GROUP_NAME,
)
def qlCalendarResetAddedAndRemovedHolidays(calendar: qCalendar, trigger=None) -> bool:
    calendar.resetAddedAndRemovedHolidays()
    return True


@xlo.func(
    help="Return holidays added to the calendar.",
    args={"calendar": "The calendar to query."},
    group=EXCEL_GROUP_NAME,
)
def qlCalendarAddedHolidays(calendar: qCalendar, trigger=None) -> list:
    return calendar.addedHolidays()


@xlo.func(
    help="Return holidays removed from the calendar.",
    args={"calendar": "The calendar to query."},
    group=EXCEL_GROUP_NAME,
)
def qlCalendarRemovedHolidays(calendar: qCalendar, trigger=None) -> list:
    return calendar.removedHolidays()


@xlo.func(
    help="Adjust a date according to the calendar and business day convention.",
    args={
        "date": "The date to adjust.",
        "calendar": "The calendar to use for adjustment.",
        "convention": "The business day convention to apply.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarAdjust(
    calendar: qCalendar,
    date: qDate,
    convention: qBusinessDayConvention = ql.Following,
    trigger=None,
) -> ql.Date:
    return calendar.adjust(date, convention)


@xlo.func(
    help="Advance a date by a given period according to the calendar and business day convention.",
    args={
        "date": "The date to advance.",
        "calendar": "The calendar to use for advancement.",
        "period": "The period by which to advance.",
        "convention": "The business day convention to apply.",
        "end_of_month": "Whether to adjust to the end of the month.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarAdvance(
    calendar: qCalendar,
    date: qDate,
    period: qPeriod,
    convention: qBusinessDayConvention = ql.Following,
    end_of_month: bool = False,
    trigger=None,
) -> ql.Date:
    return calendar.advance(date, period, convention, end_of_month)


@xlo.func(
    help="Advance a date by a given number of time units according to the calendar and business day convention.",
    args={
        "date": "The date to advance.",
        "calendar": "The calendar to use for advancement.",
        "n": "The number of time units to advance",
        "unit": 'The time unit to advance (e.g. "DAYS", "MONTHS", "YEARS").',
        "convention": "The business day convention to apply.",
        "end_of_month": "Whether to adjust to the end of the month.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarAdvance2(
    calendar: qCalendar,
    date: qDate,
    n: int,
    unit: qTimeUnit,
    convention: qBusinessDayConvention = ql.Following,
    end_of_month: bool = False,
    trigger=None,
) -> ql.Date:
    return calendar.advance(date, n, unit, convention, end_of_month)


@xlo.func(
    help="Return the number of business days between two QuantLib Dates according to the calendar.",
    args={
        "calendar": "The calendar to use.",
        "from_date": "The starting date.",
        "to_date": "The ending date.",
        "include_first": "Whether to include the first date.",
        "include_last": "Whether to include the last date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarBusinessDaysBetween(
    calendar: qCalendar,
    from_date: qDate,
    to_date: qDate,
    include_first: bool = True,
    include_last: bool = False,
    trigger=None,
) -> int:
    return calendar.businessDaysBetween(from_date, to_date, include_first, include_last)


@xlo.func(
    help="Return the list of holidays in the calendar.",
    args={
        "calendar": "The calendar for which to list holidays.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarHolidayList(
    calendar: qCalendar, from_date: qDate, to_date: qDate, trigger=None
) -> list:
    return calendar.holidayList(from_date, to_date)


@xlo.func(
    help="Return the list of business days in the calendar.",
    args={
        "calendar": "The calendar for which to list business days.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarBusinessDayList(
    calendar: qCalendar, from_date: qDate, to_date: qDate, trigger=None
) -> list:
    return calendar.businessDayList(from_date, to_date)


@xlo.func(
    help="Return the name of the calendar.",
    args={
        "calendar": "The calendar for which to get the name.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarName(calendar: qCalendar, trigger=None) -> str:
    return calendar.name()


@xlo.func(
    help="Check if the calendar is empty.",
    args={
        "calendar": "The calendar to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarEmpty(calendar: qCalendar, trigger=None) -> bool:
    return calendar.empty()


@xlo.func(
    help="Return a calendar that represents the union of two calendars.",
    args={
        "calendar1": "The first calendar.",
        "calendar2": "The second calendar.",
        "rule": "The rule for combining the calendars.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarJointCalendar(
    calendar1: qCalendar,
    calendar2: qCalendar,
    rule: qJointCalendarRule = ql.JoinHolidays,
) -> ql.Calendar:
    return ql.JointCalendar(calendar1, calendar2, rule)


@xlo.func(
    help="Return a calendar that represents the union of three calendars.",
    args={
        "calendar1": "The first calendar.",
        "calendar2": "The second calendar.",
        "calendar3": "The third calendar.",
        "rule": "The rule for combining the calendars.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarJointCalendar2(
    calendar1: qCalendar,
    calendar2: qCalendar,
    calendar3: qCalendar,
    rule: qJointCalendarRule = ql.JoinHolidays,
    trigger=None,
) -> ql.Calendar:
    return ql.JointCalendar(calendar1, calendar2, calendar3, rule)


@xlo.func(
    help="Return a calendar that represents the union of four calendars.",
    args={
        "calendar1": "The first calendar.",
        "calendar2": "The second calendar.",
        "calendar3": "The third calendar.",
        "calendar4": "The fourth calendar.",
        "rule": "The rule for combining the calendars (JOINHOLIDAYS or JOINBUSINESSDAYS).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarJointCalendar3(
    calendar1: qCalendar,
    calendar2: qCalendar,
    calendar3: qCalendar,
    calendar4: qCalendar,
    rule: qJointCalendarRule = ql.JoinHolidays,
    trigger=None,
) -> ql.Calendar:
    return ql.JointCalendar(calendar1, calendar2, calendar3, calendar4, rule)


@xlo.func(
    help="Return a calendar that represents the union of multiple calendars (2+).",
    args={
        "calendars": "A list of calendars to combine (e.g., [GERMANY, TARGET]).",
        "rule": "The rule for combining the calendars.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalendarJointCalendarN(
    calendars: xlo.Array(dims=1),
    rule: qJointCalendarRule = ql.JoinHolidays,
    trigger=None,
) -> ql.Calendar:
    if len(calendars) < 2:
        raise ValueError("At least 2 calendars are required for JointCalendar.")
    calendars_list = _to_calendar_list(calendars)
    if rule == ql.JoinHolidays:
        return ql.JointCalendar(calendars_list)
    else:
        return ql.JointCalendar(calendars_list, rule)


@xlo.func(
    help="Create a bespoke calendar with a given name.",
    args={
        "name": "The name of the bespoke calendar.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBespokeCalendar(name: str, trigger=None) -> ql.Calendar:
    return ql.BespokeCalendar(name)


@xlo.func(
    help="Add a weekday as a weekend day to a bespoke calendar.",
    args={
        "calendar": "The bespoke calendar to modify.",
        "weekday": "The weekday to add as a weekend (0=Sunday, 1=Monday, ..., 6=Saturday).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBespokeCalendarAddWeekend(
    calendar: qCalendar, weekday: qWeekday, trigger=None
) -> bool:
    calendar.addWeekend(weekday)
    return True
