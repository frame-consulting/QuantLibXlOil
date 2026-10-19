import QuantLib as ql

from quantlib_xloil.calendars import (
    qBusinessDayConvention,
    qCalendar,
    qJointCalendarRule,
    qlBespokeCalendar,
    qlBespokeCalendarAddWeekend,
    qlCalendar,
    qlCalendarAddHoliday,
    qlCalendarAddedHolidays,
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
    qlCalendarJointCalendar2,
    qlCalendarJointCalendar3,
    qlCalendarJointCalendarN,
    qlCalendarName,
    qlCalendarRemoveHoliday,
    qlCalendarRemovedHolidays,
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


def test_qlCalendar_new_143_calendars():
    for name in (
        "Croatia",
        "Israel_Telbor",
        "Malta",
        "Montenegro",
        "NorthMacedonia",
        "Serbia",
        "Slovenia",
        "Uzbekistan",
    ):
        assert qlCalendar(name) is not None


def test_qlCalendar_missing_calendars():
    for name in (
        "China_ib",
        "Germany_Settlement",
        "Germany_Eurex",
        "Germany_Xetra",
        "Israel_Tase",
        "Israel_Shir",
        "Italy_Exchange",
        "NewZealand_Auckland",
        "Poland_WSE",
        "Russia_MOEX",
        "SouthKorea_Settlement",
    ):
        assert qlCalendar(name) is not None


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
    assert holidays == (qlDate(2026, 1, 1),)


def test_qlCalendarBusinessDayList():
    calendar = qlCalendar("TARGET")
    date_from = qlDate(2026, 1, 1)
    date_to = qlDate(2026, 1, 5)
    business_days = qlCalendarBusinessDayList(calendar, date_from, date_to)
    assert business_days == (qlDate(2026, 1, 2), qlDate(2026, 1, 5))


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


def test_qlCalendarAddedAndRemovedHolidays():
    calendar = qlCalendar("TARGET")
    date_added = qlDate(2026, 5, 29)
    date_removed = qlDate(2026, 1, 1)
    qlCalendarAddHoliday(calendar, date_added)
    qlCalendarRemoveHoliday(calendar, date_removed)

    assert date_added in qlCalendarAddedHolidays(calendar)
    assert date_removed in qlCalendarRemovedHolidays(calendar)
    qlCalendarResetAddedAndRemovedHolidays(calendar)
    qlCalendarAddHoliday(calendar, date_added)
    qlCalendarRemoveHoliday(calendar, date_removed)
    assert qlCalendarIsHoliday(calendar, date_added) == True
    assert qlCalendarIsHoliday(calendar, date_removed) == False
    qlCalendarResetAddedAndRemovedHolidays(calendar)
    assert qlCalendarIsHoliday(calendar, date_added) == False
    assert qlCalendarIsHoliday(calendar, date_removed) == True


def test_qlCalendarAdjust():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 1, 31)  # Saturday
    convention = qBusinessDayConvention.__wrapped__("Following")
    adjusted_date = qlCalendarAdjust(calendar, date, convention)
    assert adjusted_date == qlDate(2026, 2, 2)  # following Monday


def test_qlCalendarAdvance():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 1, 31)  # Saturday
    period = qlPeriod(3, ql.Months)
    convention = qBusinessDayConvention.__wrapped__("Following")
    advanced_date = qlCalendarAdvance(calendar, date, period, convention)
    assert advanced_date == qlDate(2026, 4, 30)


def test_qlCalendarAdvance2():
    calendar = qlCalendar("TARGET")
    date = qlDate(2026, 1, 31)  # Saturday
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
    joint_calendar = qlCalendarJointCalendar2(calendar1, calendar2, calendar3)
    assert joint_calendar is not None


def test_qlCalendarJointCalendar3():
    calendar1 = qlCalendar("TARGET")
    calendar2 = qlCalendar("UnitedKingdom")
    calendar3 = qlCalendar("Germany")
    calendar4 = qlCalendar("France")
    rule = qJointCalendarRule.__wrapped__("JOINHOLIDAYS")

    joint_calendar = qlCalendarJointCalendar3(
        calendar1, calendar2, calendar3, calendar4, rule
    )
    assert joint_calendar is not None
    assert isinstance(joint_calendar, ql.JointCalendar)


def test_qlCalendarJointCalendarN_2_calendars():
    calendars = [qlCalendar("TARGET"), qlCalendar("UnitedKingdom")]
    joint_calendar = qlCalendarJointCalendarN(calendars)
    assert joint_calendar is not None
    assert isinstance(joint_calendar, ql.JointCalendar)


def test_qlCalendarJointCalendarN_3_calendars():
    calendars = [
        qlCalendar("TARGET"),
        qlCalendar("UnitedKingdom"),
        qlCalendar("Germany"),
    ]
    joint_calendar = qlCalendarJointCalendarN(calendars)
    assert joint_calendar is not None


def test_qlCalendarJointCalendarN_5_calendars():
    calendars = [
        qlCalendar("TARGET"),
        qlCalendar("UnitedKingdom"),
        qlCalendar("Germany"),
        qlCalendar("France"),
        qlCalendar("Switzerland"),
    ]
    joint_calendar = qlCalendarJointCalendarN(calendars)
    assert joint_calendar is not None


def test_qlCalendarJointCalendarN_invalid_input():
    try:
        qlCalendarJointCalendarN([qlCalendar("TARGET")])
        assert False, "Expected ValueError for less than 2 calendars"
    except ValueError as e:
        assert "At least 2 calendars are required" in str(e)


def test_qCalendar_JointCalendar_2_calendars():
    joint_cal = qCalendar.__wrapped__("JOINTCALENDAR(TARGET,UNITEDKINGDOM)")
    assert joint_cal is not None
    assert isinstance(joint_cal, ql.JointCalendar)


def test_qCalendar_JointCalendar_3_calendars():
    joint_cal = qCalendar.__wrapped__("JOINTCALENDAR(TARGET,UNITEDKINGDOM,GERMANY)")
    assert joint_cal is not None


def test_qCalendar_JointCalendar_4_calendars():
    joint_cal = qCalendar.__wrapped__(
        "JOINTCALENDAR(TARGET,UNITEDKINGDOM,GERMANY,FRANCE)"
    )
    assert joint_cal is not None


def test_qCalendar_JointCalendar_5_calendars():
    joint_cal = qCalendar.__wrapped__(
        "JOINTCALENDAR(TARGET,UNITEDKINGDOM,GERMANY,FRANCE,SWITZERLAND)"
    )
    assert joint_cal is not None


def test_qCalendar_JointCalendar_with_rule_JOINHOLIDAYS():
    joint_cal = qCalendar.__wrapped__(
        "JOINTCALENDAR(TARGET,UNITEDKINGDOM,rule=JOINHOLIDAYS)"
    )
    assert joint_cal is not None


def test_qCalendar_JointCalendar_with_rule_JOINBUSINESSDAYS():
    joint_cal = qCalendar.__wrapped__(
        "JOINTCALENDAR(TARGET,UNITEDKINGDOM,rule=JOINBUSINESSDAYS)"
    )
    assert joint_cal is not None


def test_qCalendar_JointCalendar_rule_case_insensitive():
    joint_cal1 = qCalendar.__wrapped__(
        "JOINTCALENDAR(TARGET,UNITEDKINGDOM,rule=joinbusinessdays)"
    )
    assert joint_cal1 is not None
    joint_cal2 = qCalendar.__wrapped__(
        "JOINTCALENDAR(TARGET,UNITEDKINGDOM,rule=JoinHolidays)"
    )
    assert joint_cal2 is not None


def test_qCalendar_JointCalendar_functionality():
    joint_cal = qCalendar.__wrapped__("JOINTCALENDAR(TARGET,UNITEDKINGDOM)")
    christmas = qlDate(2023, 12, 25)
    assert joint_cal.isHoliday(christmas) == True


def test_qCalendar_JointCalendar_different_rules():
    joint_holidays = qCalendar.__wrapped__("JOINTCALENDAR(TARGET,UNITEDKINGDOM)")
    joint_business = qCalendar.__wrapped__(
        "JOINTCALENDAR(TARGET,UNITEDKINGDOM,rule=JOINBUSINESSDAYS)"
    )
    assert joint_holidays is not None
    assert joint_business is not None


def test_qCalendar_JointCalendar_invalid_rule():
    try:
        qCalendar.__wrapped__("JOINTCALENDAR(TARGET,UNITEDKINGDOM,rule=INVALID)")
        assert False, "Expected ValueError for invalid rule"
    except ValueError:
        pass


def test_qlBespokeCalendar():
    calendar = qlBespokeCalendar("MyCustomCalendar")
    assert calendar is not None
    assert isinstance(calendar, ql.Calendar)
    assert calendar.name() == "MyCustomCalendar"


def test_qlBespokeCalendar_multiple_names():
    cal1 = qlBespokeCalendar("Calendar1")
    cal2 = qlBespokeCalendar("Calendar2")
    assert cal1 is not None
    assert cal2 is not None
    assert cal1.name() == "Calendar1"
    assert cal2.name() == "Calendar2"


def test_qlBespokeCalendar_default_behavior():
    calendar = qlBespokeCalendar("TestCalendar")
    for day in range(7):
        dates = [
            qlDate(2026, 10, 4),  # Sunday
            qlDate(2026, 10, 5),  # Monday
            qlDate(2026, 10, 6),  # Tuesday
            qlDate(2026, 10, 7),  # Wednesday
            qlDate(2026, 10, 8),  # Thursday
            qlDate(2026, 10, 9),  # Friday
            qlDate(2026, 10, 10),  # Saturday
        ]
        assert calendar.isBusinessDay(dates[day]) == True


def test_qlBespokeCalendarAddWeekend_single():
    calendar = qlBespokeCalendar("TestCalendar")
    monday = ql.Monday
    result = qlBespokeCalendarAddWeekend(calendar, monday)
    assert result == True
    monday_date = qlDate(2026, 10, 5)  # Monday
    assert calendar.isBusinessDay(monday_date) == False
    tuesday_date = qlDate(2026, 10, 6)  # Tuesday
    assert calendar.isBusinessDay(tuesday_date) == True


def test_qlBespokeCalendarAddWeekend_multiple():
    calendar = qlBespokeCalendar("TestCalendar")
    monday = ql.Monday
    friday = ql.Friday
    qlBespokeCalendarAddWeekend(calendar, monday)
    qlBespokeCalendarAddWeekend(calendar, friday)

    monday_date = qlDate(2026, 10, 5)  # Monday
    friday_date = qlDate(2026, 10, 9)  # Friday
    assert calendar.isBusinessDay(monday_date) == False
    assert calendar.isBusinessDay(friday_date) == False

    tuesday_date = qlDate(2026, 10, 6)  # Tuesday
    assert calendar.isBusinessDay(tuesday_date) == True


def test_qlBespokeCalendarAddWeekend_all_days():
    calendar = qlBespokeCalendar("AllWeekendCalendar")
    weekdays = [
        ql.Sunday,
        ql.Monday,
        ql.Tuesday,
        ql.Wednesday,
        ql.Thursday,
        ql.Friday,
        ql.Saturday,
    ]
    for weekday in weekdays:
        qlBespokeCalendarAddWeekend(calendar, weekday)

    for day in range(7):
        dates = [
            qlDate(2026, 10, 4),  # Sunday
            qlDate(2026, 10, 5),  # Monday
            qlDate(2026, 10, 6),  # Tuesday
            qlDate(2026, 10, 7),  # Wednesday
            qlDate(2026, 10, 8),  # Thursday
            qlDate(2026, 10, 9),  # Friday
            qlDate(2026, 10, 10),  # Saturday
        ]
        assert calendar.isBusinessDay(dates[day]) == False


def test_qlBespokeCalendar_with_qCalendar_converter():
    """Test creating a bespoke calendar via qCalendar converter with BESPOKECALENDAR syntax."""
    calendar = qCalendar.__wrapped__("BESPOKECALENDAR(MyCustomCalendar)")
    assert calendar is not None
    assert isinstance(calendar, ql.Calendar)
    assert calendar.name() == "MYCUSTOMCALENDAR"


def test_qlBespokeCalendarAddWeekend_return_value():
    calendar = qlBespokeCalendar("TestCalendar")
    monday = ql.Monday
    result = qlBespokeCalendarAddWeekend(calendar, monday)
    assert result == True


def test_qlBespokeCalendar_with_qWeekday_converter():
    calendar = qlBespokeCalendar("TestCalendar")
    monday = qWeekday.__wrapped__("MONDAY")
    result = qlBespokeCalendarAddWeekend(calendar, monday)
    assert result == True
    monday_date = qlDate(2026, 10, 5)  # Monday
    assert calendar.isBusinessDay(monday_date) == False
