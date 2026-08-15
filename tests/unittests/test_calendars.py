import QuantLib as ql

from quantlib_xloil.calendars import (
    qBusinessDayConvention,
    qCalendar,
    qJointCalendarRule,
    qlCalendar,
    qlCalendarAddHoliday,
    qlCalendarAdjust,
    qlCalendarAdvance,
    qlCalendarAdvance2,
    qlCalendarBusinessDayList,
    qlCalendarBusinessDaysBetween,
    qlCalendarEmpty,
    qlCalendarEndOfMonth,
    qlCalendarHolidayList,
    qlCalendarIsBusinessDay,
    qlCalendarIsEndOfMonth,
    qlCalendarIsHoliday,
    qlCalendarIsStartOfMonth,
    qlCalendarisWeekend,
    qlCalendarJointCalendar,
    qlCalendarName,
    qlCalendarRemoveHoliday,
    qlCalendarResetAddedAndRemovedHolidays,
    qlCalendarStartOfMonth,
)
from quantlib_xloil.date import qlDate, qlDateWeekday, qlPeriod, qTimeUnit, qWeekday


def test_qCalendar():
    calendar = qCalendar.__wrapped__("TARGET")
    assert calendar is not None


def test_qBusinessDayConvention():
    convention = qBusinessDayConvention.__wrapped__("Following")
    assert convention is not None


def test_qJointCalendarRule():
    rule = qJointCalendarRule.__wrapped__("JOINHOLIDAYS")
    assert rule is not None


def test_qlCalenndar_Argentina():
    calendar = qlCalendar("Argentina")
    assert calendar is not None


def test_qlCalendar_Australia():
    calendar = qlCalendar("Australia")
    assert calendar is not None


def test_qlCalendar_Botswana():
    calendar = qlCalendar("Botswana")
    assert calendar is not None


def test_qlCalendar_Brazil():
    calendar = qlCalendar("Brazil")
    assert calendar is not None


def test_qlCalendar_Canada():
    calendar = qlCalendar("Canada")
    assert calendar is not None


def test_qlCalendar_Chile():
    calendar = qlCalendar("Chile")
    assert calendar is not None


def test_qlCalendar_China():
    calendar = qlCalendar("China")
    assert calendar is not None


def test_qlCalendar_CzechRepublic():
    calendar = qlCalendar("CzechRepublic")
    assert calendar is not None


def test_qlCalendar_Denmark():
    calendar = qlCalendar("Denmark")
    assert calendar is not None


def test_qlCalendar_Finland():
    calendar = qlCalendar("Finland")
    assert calendar is not None


def test_qlCalendar_France():
    calendar = qlCalendar("France")
    assert calendar is not None


def test_qlCalendar_Germany():
    calendar = qlCalendar("Germany")
    assert calendar is not None


def test_qlCalendar_HongKong():
    calendar = qlCalendar("HongKong")
    assert calendar is not None


def test_qlCalendar_Hungary():
    calendar = qlCalendar("Hungary")
    assert calendar is not None


def test_qlCalendar_Iceland():
    calendar = qlCalendar("Iceland")
    assert calendar is not None


def test_qlCalendar_India():
    calendar = qlCalendar("India")
    assert calendar is not None


def test_qlCalendar_Indonesia():
    calendar = qlCalendar("Indonesia")
    assert calendar is not None


def test_qlCalendar_Israel():
    calendar = qlCalendar("Israel")
    assert calendar is not None


def test_qlCalendar_Italy():
    calendar = qlCalendar("Italy")
    assert calendar is not None


def test_qlCalendar_Japan():
    calendar = qlCalendar("Japan")
    assert calendar is not None


def test_qlCalendar_Mexico():
    calendar = qlCalendar("Mexico")
    assert calendar is not None


def test_qlCalendar_Newzealand():
    calendar = qlCalendar("NewZealand")
    assert calendar is not None


def test_qlCalendar_Norway():
    calendar = qlCalendar("Norway")
    assert calendar is not None


def test_qlCalendar_Poland():
    calendar = qlCalendar("Poland")
    assert calendar is not None


def test_qlCalendar_Romania():
    calendar = qlCalendar("Romania")
    assert calendar is not None


def test_qlCalendar_Russia():
    calendar = qlCalendar("Russia")
    assert calendar is not None


def test_qlCalendar_SaudiArabia():
    calendar = qlCalendar("SaudiArabia")
    assert calendar is not None


def test_qlCalendar_Singapore():
    calendar = qlCalendar("Singapore")
    assert calendar is not None


def test_qlCalendar_Singapore():
    calendar = qlCalendar("SouthAfrica")
    assert calendar is not None


def test_qlCalendar_Slovakia():
    calendar = qlCalendar("Slovakia")
    assert calendar is not None


def test_qlCalendar_SouthAfrica():
    calendar = qlCalendar("SouthAfrica")
    assert calendar is not None


def test_qlCalendar_SouthKorea():
    calendar = qlCalendar("SouthKorea")
    assert calendar is not None


def test_qlCalendar_Sweden():
    calendar = qlCalendar("Sweden")
    assert calendar is not None


def test_qlCalendar_Switzerland():
    calendar = qlCalendar("Switzerland")
    assert calendar is not None


def test_qlCalendar_Taiwan():
    calendar = qlCalendar("Taiwan")
    assert calendar is not None


def test_qlCalendar_Target():
    calendar = qlCalendar("TARGET")
    assert calendar is not None


def test_qlCalendar_Thailand():
    calendar = qlCalendar("Thailand")
    assert calendar is not None


def test_qlCalendar_Turkey():
    calendar = qlCalendar("Turkey")
    assert calendar is not None


def test_qlCalendar_Ukraine():
    calendar = qlCalendar("Ukraine")
    assert calendar is not None


def test_qlCalendar_UnitedKingdom():
    calendar = qlCalendar("UnitedKingdom")
    assert calendar is not None


def test_qlCalendar_NullCalendar():
    calendar = qlCalendar("NullCalendar")
    assert calendar is not None


def test_qlCalendar_Weekendsonly():
    calendar = qlCalendar("Weekendsonly")
    assert calendar is not None


def test_qlCalendarisWeekend():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 5, 29)  # This is a Friday
    weekday = qlDateWeekday(date)
    assert qlCalendarisWeekend(calendar, qWeekday.__wrapped__(weekday)) == False


def test_qlCalendarStartOfMonth():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 5, 29)
    assert qlCalendarStartOfMonth(calendar, date) == qlDate(2026, 5, 4)


def test_qlCalendarEndOfMonth():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 5, 29)
    assert qlCalendarEndOfMonth(calendar, date) == qlDate(2026, 5, 29)


def test_qlCalendarIsBusinessDay():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 5, 29)  # This is a Friday
    assert qlCalendarIsBusinessDay(calendar, date) == True


def test_qlClendarIsHoliday():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 5, 29)
    assert qlCalendarIsHoliday(calendar, date) == False


def test_qlCalendarIsEndOfMonth():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 5, 29)
    assert qlCalendarIsEndOfMonth(calendar, date) == True


def test_qlCalendarIsStartOfMonth():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 5, 29)
    assert qlCalendarIsStartOfMonth(calendar, date) == False


def test_qlCalendarHolidayList():
    calendar = qlCalendar("TARGET")
    date_from = qlDate(2026, 1, 1)
    date_to = qlDate(2026, 1, 5)
    holidays = qlCalendarHolidayList(calendar, date_from, date_to)
    assert holidays == [qlDate(2026, 1, 1)]


def test_qlCalendarBusinessDayList():
    calendar = qlCalendar("TARGET")
    date_from = qlDate(2026, 1, 1)
    date_to = qlDate(2026, 1, 5)
    business_days = qlCalendarBusinessDayList(calendar, date_from, date_to)
    assert business_days == [qlDate(2026, 1, 2), qlDate(2026, 1, 5)]


def test_qlCalendarAddHoliday():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 5, 29)
    assert qlCalendarIsHoliday(calendar, date) == False
    qlCalendarAddHoliday(calendar, date)
    assert qlCalendarIsHoliday(calendar, date) == True
    qlCalendarResetAddedAndRemovedHolidays(calendar)


def test_qlCalendarRemoveHoliday():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 1, 1)
    assert qlCalendarIsHoliday(calendar, date) == True
    qlCalendarRemoveHoliday(calendar, date)
    assert qlCalendarIsHoliday(calendar, date) == False
    qlCalendarResetAddedAndRemovedHolidays(calendar)


def test_qlCalendarResetAddedAndRemovedHolidays():
    calendar = qlCalendar("TARGET")
    date_added = qlDate(2026, 5, 29)
    date_removed = qlDate(2026, 1, 1)
    assert qlCalendarIsHoliday(calendar, date_added) == False
    assert qlCalendarIsHoliday(calendar, date_removed) == True
    qlCalendarAddHoliday(calendar, date_added)
    qlCalendarRemoveHoliday(calendar, date_removed)
    assert qlCalendarIsHoliday(calendar, date_added) == True
    assert qlCalendarIsHoliday(calendar, date_removed) == False
    qlCalendarResetAddedAndRemovedHolidays(calendar)
    assert qlCalendarIsHoliday(calendar, date_added) == False
    assert qlCalendarIsHoliday(calendar, date_removed) == True


def test_qlCalendarAdjust():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 1, 31)  # This is a Saturday
    convention = qBusinessDayConvention.__wrapped__("Following")
    adjusted_date = qlCalendarAdjust(calendar, date, convention)
    assert adjusted_date == qlDate(2026, 2, 2)  # This is the following Monday


def test_qlCalendarAdvance():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 1, 31)  # This is a Saturday
    period = qlPeriod(3, ql.Months)
    convention = qBusinessDayConvention.__wrapped__("Following")
    advanced_date = qlCalendarAdvance(calendar, date, period, convention)
    assert advanced_date == qlDate(2026, 4, 30)


def test_qlCalendarAdvance2():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 1, 31)  # This is a Saturday
    n = 10
    unit = qTimeUnit.__wrapped__("DAYS")
    convention = qBusinessDayConvention.__wrapped__("Following")
    advanced_date = qlCalendarAdvance2(calendar, date, n, unit, convention)
    assert advanced_date == qlDate(2026, 2, 13)


def test_qlCalendarBusinessDaysBetween():
    calendar = qlCalendar("TARGET")
    from_date = qlDate(2026, 1, 1)
    to_date = qlDate(2026, 1, 5)
    assert qlCalendarBusinessDaysBetween(calendar, from_date, to_date) == 1
    assert qlCalendarBusinessDaysBetween(calendar, from_date, to_date, True, True) == 2


def test_qlCalendarName():
    calendar = qlCalendar("TARGET")
    assert qlCalendarName(calendar) == "TARGET"


def test_qlCalendarEmpty():
    calendar = qlCalendar("TARGET")
    assert qlCalendarEmpty(calendar) == False


def test_qlCalendarJointCalendar():
    calendar1 = qlCalendar("TARGET")
    calendar2 = qlCalendar("UnitedKingdom")
    rule = qJointCalendarRule.__wrapped__("JOINHOLIDAYS")
    joint_calendar = qlCalendarJointCalendar(calendar1, calendar2, rule)
    assert joint_calendar is not None


def test_qlCalendarJointCalendar2():
    calendar1 = qlCalendar("TARGET")
    calendar2 = qlCalendar("UnitedKingdom")
    calendar3 = qlCalendar("Sweden")
    joint_calendar = qlCalendarJointCalendar(calendar1, calendar2, calendar3)
    assert joint_calendar is not None
