import QuantLib as ql

from quantlib_xloil.date import (
    qlECBCode,
    qlECBDate,
    qlECBDateFromCode,
    qlECBIsECBCode,
    qlECBIsECBDate,
    qlECBNextCode,
    qlECBNextCodeFromCode,
    qlECBNextDate,
    qlECBNextDateFromCode,
    qlECBNextDates,
    qlECBNextDatesFromCode,
    qDate,
    qFrequency,
    qPeriod,
    qTimeUnit,
    qWeekday,
    qlDate,
    qlDateDayOfMonth,
    qlDateDayOfYear,
    qlDateEndOfMonth,
    qlDateIsEndOfMonth,
    qlDateIsLeap,
    qlDateIsStartOfMonth,
    qlDateMaxDate,
    qlDateMinDate,
    qlDateMonth,
    qlDateNthWeekday,
    qlDateParserParseFormatted,
    qlDateParserParseISO,
    qlDateStartOfMonth,
    qlDateTodaysDate,
    qlDateWeekday,
    qlDateYear,
    qlDateNextWeekday,
    qlPeriod,
    qlPeriodFrequency,
    qlPeriodLength,
    qlPeriodNormalized,
    qlPeriodUnits,
)


def test_qWeekday():
    assert qWeekday.__wrapped__("Monday") == ql.Monday


def test_qFrequency():
    assert qFrequency.__wrapped__("Annual") == ql.Annual


def test_qTimeUnit():
    assert qTimeUnit.__wrapped__("Months") == ql.Months


def test_qPeriod():
    period = qPeriod.__wrapped__("3M")
    assert isinstance(period, ql.Period)
    assert period.length() == 3
    assert period.units() == ql.Months


def test_qDate():
    date = qDate.__wrapped__(43845)  # Excel serial number for 2020-01-15
    assert date == ql.Date(15, 1, 2020)
    assert (
        qDate.__wrapped__(date) == date
    )  # If it's already a QuantLib Date, it should return the same date
    assert (
        qDate.__wrapped__("invalid") == ql.Date()
    )  # Invalid input should return default empty date value


def test_qlPeriod():
    period = qlPeriod(3, ql.Months)
    assert isinstance(period, ql.Period)


def test_qlPeriodLength():
    period = qlPeriod(3, ql.Months)
    assert qlPeriodLength(period) == 3


def test_qlPeriodUnits():
    period = qlPeriod(3, ql.Months)
    assert qlPeriodUnits(period) == "MONTHS"


def test_qlPeriodFrequency():
    period = qlPeriod(3, ql.Months)
    assert qlPeriodFrequency(period) == "QUARTERLY"


def test_qlPeriodNormalized():
    period = qlPeriod(12, ql.Months)
    normalized_period = qlPeriodNormalized(period)
    assert normalized_period.length() == 1
    assert normalized_period.units() == ql.Years


def test_qlDate():
    date = qlDate(2020, 1, 15)
    assert isinstance(date, ql.Date)


def test_qlDateDayOfMonth():
    date = qlDate(2020, 1, 15)
    assert qlDateDayOfMonth(date) == 15


def test_qlDateDayOfYear():
    date = qlDate(2020, 2, 15)
    assert qlDateDayOfYear(date) == 31 + 15


def test_qlDateMonth():
    date = qlDate(2020, 1, 15)
    assert qlDateMonth(date) == 1


def test_qlDateYear():
    date = qlDate(2020, 1, 15)
    assert qlDateYear(date) == 2020


def test_qlDateWeekday():
    date = qlDate(2020, 1, 15)  # This is a Wednesday
    assert qlDateWeekday(date) == "WEDNESDAY"


def test_qlDateIsLeap():
    date = qlDate(2020, 1, 15)
    assert qlDateIsLeap(date.year()) == True
    date_non_leap = qlDate(2019, 1, 15)
    assert qlDateIsLeap(date_non_leap.year()) == False


def test_qlDateMinDate():
    min_date = qlDateMinDate()
    assert min_date == ql.Date(1, 1, 1901)


def test_qlDateMaxDate():
    max_date = qlDateMaxDate()
    assert max_date == ql.Date(31, 12, 2199)


def test_qlDateTodaysDate():
    today = qlDateTodaysDate()
    assert today == ql.Date.todaysDate()


def test_qlDateStartOfMonth():
    date = qlDate(2020, 1, 15)
    start_of_month = qlDateStartOfMonth(date)
    assert start_of_month == ql.Date(1, 1, 2020)


def test_qlDateEndOfMonth():
    date = qlDate(2020, 1, 15)
    end_of_month = qlDateEndOfMonth(date)
    assert end_of_month == ql.Date(31, 1, 2020)


def test_qlDateIsStartOfMonth():
    date = qlDate(2020, 1, 1)
    assert qlDateIsStartOfMonth(date) == True
    date_not_start = qlDate(2020, 1, 15)
    assert qlDateIsStartOfMonth(date_not_start) == False


def test_qlDateIsEndOfMonth():
    date = qlDate(2020, 1, 31)
    assert qlDateIsEndOfMonth(date) == True
    date_not_end = qlDate(2020, 1, 15)
    assert qlDateIsEndOfMonth(date_not_end) == False


def test_qlDateNextWeekday():
    date = qlDate(2020, 1, 15)  # Wednesday
    next_monday = qlDateNextWeekday(date, ql.Monday)
    assert next_monday == ql.Date(20, 1, 2020)
    next_wednesday = qlDateNextWeekday(date, ql.Wednesday)
    assert next_wednesday == ql.Date(15, 1, 2020)
    next_friday = qlDateNextWeekday(date, ql.Friday)
    assert next_friday == ql.Date(17, 1, 2020)


def test_qlDateNthWeekday():
    first_monday = qlDateNthWeekday(1, ql.Monday, 1, 2020)
    assert first_monday == ql.Date(6, 1, 2020)
    second_wednesday = qlDateNthWeekday(2, ql.Wednesday, 1, 2020)
    assert second_wednesday == ql.Date(8, 1, 2020)
    third_friday = qlDateNthWeekday(3, ql.Friday, 1, 2020)
    assert third_friday == ql.Date(17, 1, 2020)


def test_qlDateParserParseFormatted():
    date_str = "2020-01-15"
    date = qlDateParserParseFormatted(date_str, "%Y-%m-%d")
    assert date == ql.Date(15, 1, 2020)


def test_qlDateParserParseISO():
    date_str = "2020-01-15"
    date = qlDateParserParseISO(date_str)
    assert date == ql.Date(15, 1, 2020)


def test_qlECB_wrappers():
    ecb_date = qlECBDate(1, 2024)

    assert qlECBIsECBDate(ecb_date) is True

    code = qlECBCode(ecb_date)
    assert code == "JAN24"
    assert qlECBIsECBCode(code) is True

    from_code = qlECBDateFromCode("JUN24")
    assert from_code == ql.Date(12, 6, 2024)

    # Keep references in the known ECB schedule window to avoid runtime errors.
    next_date = qlECBNextDate(ql.Date(1, 1, 2024))
    assert qlECBIsECBDate(next_date) is True
    assert qlECBNextDateFromCode("JAN24") == ql.Date(13, 3, 2024)

    next_dates = qlECBNextDates(ql.Date(1, 1, 2024))
    next_dates_from_code = qlECBNextDatesFromCode("JAN24")
    assert len(next_dates) > 0
    assert len(next_dates_from_code) > 0

    assert qlECBNextCode(ql.Date(1, 1, 2024)) == "JAN24"
    assert qlECBNextCodeFromCode("JAN24") == "FEB24"
