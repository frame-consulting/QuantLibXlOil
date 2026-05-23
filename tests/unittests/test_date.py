
def test_qWeekday():
    from quantlibxloil.date import _qWeekday
    import QuantLib as ql
    assert _qWeekday("Monday") == ql.Monday

def test_qFrequency():
    from quantlibxloil.date import _qFrequency
    import QuantLib as ql
    assert _qFrequency("Annual") == ql.Annual

def test_qTimeUnit():
    from quantlibxloil.date import _qTimeUnit
    import QuantLib as ql
    assert _qTimeUnit("Months") == ql.Months

def test_qPeriod():
    from quantlibxloil.date import _qPeriod
    import QuantLib as ql
    period = _qPeriod("3M")
    assert isinstance(period, ql.Period)
    assert period.length() == 3
    assert period.units() == ql.Months

def test_qDate():
    from quantlibxloil.date import _qDate
    import QuantLib as ql
    date = _qDate(43845)  # Excel serial number for 2020-01-15
    assert date == ql.Date(15, 1, 2020)
    assert _qDate(date) == date  # If it's already a QuantLib Date, it should return the same date
    assert _qDate("invalid") == ql.Date()  # Invalid input should return default empty date value

def test_qlPeriod():
    from quantlibxloil import qlPeriod
    import QuantLib as ql
    period = qlPeriod(3, ql.Months)
    assert isinstance(period, ql.Period)

def test_qlPeriodLength():
    from quantlibxloil import qlPeriod, qlPeriodLength
    import QuantLib as ql
    period = qlPeriod(3, ql.Months)
    assert qlPeriodLength(period) == 3

def test_qlPeriodUnits():
    from quantlibxloil import qlPeriod, qlPeriodUnits
    import QuantLib as ql
    period = qlPeriod(3, ql.Months)
    assert qlPeriodUnits(period) == "MONTHS"

def test_qlPeriodFrequency():
    from quantlibxloil import qlPeriod, qlPeriodFrequency
    import QuantLib as ql
    period = qlPeriod(3, ql.Months)
    assert qlPeriodFrequency(period) == "QUARTERLY"

def test_qlPeriodNormalized():
    from quantlibxloil import qlPeriod, qlPeriodNormalized
    import QuantLib as ql
    period = qlPeriod(12, ql.Months)
    normalized_period = qlPeriodNormalized(period)
    assert normalized_period.length() == 1
    assert normalized_period.units() == ql.Years

def test_qlDate():
    from quantlibxloil import qlDate
    import QuantLib as ql
    date = qlDate(2020, 1, 15)
    assert isinstance(date, ql.Date)

def test_qlDateDayOfMonth():
    from quantlibxloil import qlDate, qlDateDayOfMonth
    import QuantLib as ql
    date = qlDate(2020, 1, 15)
    assert qlDateDayOfMonth(date) == 15

def test_qlDateDayOfYear():
    from quantlibxloil import qlDate, qlDateDayOfYear
    import QuantLib as ql
    date = qlDate(2020, 2, 15)
    assert qlDateDayOfYear(date) == 31 + 15

def test_qlDateMonth():
    from quantlibxloil import qlDate, qlDateMonth
    import QuantLib as ql
    date = qlDate(2020, 1, 15)
    assert qlDateMonth(date) == 1

def test_qlDateYear():
    from quantlibxloil import qlDate, qlDateYear
    import QuantLib as ql
    date = qlDate(2020, 1, 15)
    assert qlDateYear(date) == 2020

def test_qlDateWeekday():
    from quantlibxloil import qlDate, qlDateWeekday
    import QuantLib as ql
    date = qlDate(2020, 1, 15)  # This is a Wednesday
    assert qlDateWeekday(date) == "WEDNESDAY"

def test_qlDateIsLeap():
    from quantlibxloil import qlDate, qlDateIsLeap
    import QuantLib as ql
    date = qlDate(2020, 1, 15)
    assert qlDateIsLeap(date.year()) == True
    date_non_leap = qlDate(2019, 1, 15)
    assert qlDateIsLeap(date_non_leap.year()) == False

def test_qlDateMinDate():
    from quantlibxloil import qlDateMinDate
    import QuantLib as ql
    min_date = qlDateMinDate()
    assert min_date == ql.Date(1, 1, 1901)

def test_qlDateMaxDate():
    from quantlibxloil import qlDateMaxDate
    import QuantLib as ql
    max_date = qlDateMaxDate()
    assert max_date == ql.Date(31, 12, 2199)

def test_qlDateTodaysDate():
    from quantlibxloil import qlDateTodaysDate
    import QuantLib as ql
    today = qlDateTodaysDate()
    assert today == ql.Date.todaysDate()

def test_qlDateStartOfMonth():
    from quantlibxloil import qlDate, qlDateStartOfMonth
    import QuantLib as ql
    date = qlDate(2020, 1, 15)
    start_of_month = qlDateStartOfMonth(date)
    assert start_of_month == ql.Date(1, 1, 2020)

def test_qlDateEndOfMonth():
    from quantlibxloil import qlDate, qlDateEndOfMonth
    import QuantLib as ql
    date = qlDate(2020, 1, 15)
    end_of_month = qlDateEndOfMonth(date)
    assert end_of_month == ql.Date(31, 1, 2020)

def test_qlDateIsStartOfMonth():
    from quantlibxloil import qlDate, qlDateIsStartOfMonth
    import QuantLib as ql
    date = qlDate(2020, 1, 1)
    assert qlDateIsStartOfMonth(date) == True
    date_not_start = qlDate(2020, 1, 15)
    assert qlDateIsStartOfMonth(date_not_start) == False

def test_qlDateIsEndOfMonth():
    from quantlibxloil import qlDate, qlDateIsEndOfMonth
    import QuantLib as ql
    date = qlDate(2020, 1, 31)
    assert qlDateIsEndOfMonth(date) == True
    date_not_end = qlDate(2020, 1, 15)
    assert qlDateIsEndOfMonth(date_not_end) == False

def test_qlDateNextWeekday():
    from quantlibxloil import qlDate, qlDateNextWeekday
    import QuantLib as ql
    date = qlDate(2020, 1, 15)  # Wednesday
    next_monday = qlDateNextWeekday(date, ql.Monday)
    assert next_monday == ql.Date(20, 1, 2020)
    next_wednesday = qlDateNextWeekday(date, ql.Wednesday)
    assert next_wednesday == ql.Date(15, 1, 2020)
    next_friday = qlDateNextWeekday(date, ql.Friday)
    assert next_friday == ql.Date(17, 1, 2020)

def test_qlDateNthWeekday():
    from quantlibxloil import qlDateNthWeekday
    import QuantLib as ql
    first_monday = qlDateNthWeekday(1, ql.Monday, 1, 2020)
    assert first_monday == ql.Date(6, 1, 2020)
    second_wednesday = qlDateNthWeekday(2, ql.Wednesday, 1, 2020)
    assert second_wednesday == ql.Date(8, 1, 2020)
    third_friday = qlDateNthWeekday(3, ql.Friday, 1, 2020)
    assert third_friday == ql.Date(17, 1, 2020)

def test_qlDateParserParseFormatted():
    from quantlibxloil import qlDateParserParseFormatted
    import QuantLib as ql
    date_str = "2020-01-15"
    date = qlDateParserParseFormatted(date_str, "%Y-%m-%d")
    assert date == ql.Date(15, 1, 2020)

def test_qlDateParserParseISO():
    from quantlibxloil import qlDateParserParseISO
    import QuantLib as ql
    date_str = "2020-01-15"
    date = qlDateParserParseISO(date_str)
    assert date == ql.Date(15, 1, 2020)
