

def test_qlDayCounter_Actual360():
    """Test creation of ACTUAL360 day counter."""
    from quantlib_xloil import qlDayCounter
    daycounter = qlDayCounter("ACTUAL360")
    assert daycounter is not None

def test_qlDayCounter_Actual365Fixed():
    """Test creation of ACTUAL365FIXED day counter."""
    from quantlib_xloil import qlDayCounter
    daycounter = qlDayCounter("ACTUAL365FIXED")
    assert daycounter is not None

def test_qlDayCounter_Actual364():
    """Test creation of ACTUAL364 day counter."""
    from quantlib_xloil import qlDayCounter
    daycounter = qlDayCounter("ACTUAL364")
    assert daycounter is not None

def test_qlDayCounter_Actual36525():
    """Test creation of ACTUAL36525 day counter."""
    from quantlib_xloil import qlDayCounter
    daycounter = qlDayCounter("ACTUAL36525")
    assert daycounter is not None

def test_qlDayCounter_Actual366():
    """Test creation of ACTUAL366 day counter."""
    from quantlib_xloil import qlDayCounter
    daycounter = qlDayCounter("ACTUAL366")
    assert daycounter is not None

def test_qlDayCounter_ActualActual():
    """Test creation of ACTUALACTUAL day counter."""
    from quantlib_xloil import qlDayCounter
    daycounter = qlDayCounter("ACTUALACTUAL")
    assert daycounter is not None

def test_qlDayCounter_Business252():
    """Test creation of BUSINESS252 day counter."""
    from quantlib_xloil import qlDayCounter
    daycounter = qlDayCounter("BUSINESS252")
    assert daycounter is not None

def test_qlDayCounter_OneDayCounter():
    """Test creation of ONEDAYCOUNTER day counter."""
    from quantlib_xloil import qlDayCounter
    daycounter = qlDayCounter("ONEDAYCOUNTER")
    assert daycounter is not None

def test_qlDayCounter_SimpleDayCounter():
    """Test creation of SIMPLEDAYCOUNTER day counter."""
    from quantlib_xloil import qlDayCounter
    daycounter = qlDayCounter("SIMPLEDAYCOUNTER")
    assert daycounter is not None

def test_qlDayCounter_Thirty360():
    """Test creation of THIRTY360 day counter."""
    from quantlib_xloil import qlDayCounter
    daycounter = qlDayCounter("THIRTY360")
    assert daycounter is not None

def test_qlDayCounter_Thirty365():
    """Test creation of THIRTY365 day counter."""
    from quantlib_xloil import qlDayCounter
    daycounter = qlDayCounter("THIRTY365")
    assert daycounter is not None

def test_qlDayCounter_CaseInsensitive():
    """Test that day counter names are case-insensitive."""
    from quantlib_xloil.daycounters import _qDayCounter
    dc1 = _qDayCounter("ACTUAL360")
    dc2 = _qDayCounter("actual360")
    dc3 = _qDayCounter("Actual360")
    assert dc1 is not None
    assert dc2 is not None
    assert dc3 is not None


def test_qlDayCounterDayCount_SameDate():
    """Test day count between same dates."""
    from quantlib_xloil import qDayCounter, qlDayCounterDayCount, qlDate
    daycounter = qDayCounter.__wrapped__("ACTUAL360")
    date = qlDate(2024, 1, 1)
    assert qlDayCounterDayCount(daycounter, date, date) == 0

def test_qlDayCounterDayCount_OneDay():
    """Test day count for one day."""
    from quantlib_xloil import qlDayCounter, qlDayCounterDayCount, qlDate
    daycounter = qlDayCounter("ACTUAL360")
    date1 = qlDate(2024, 1, 1)
    date2 = qlDate(2024, 1, 2)
    assert qlDayCounterDayCount(daycounter, date1, date2) == 1

def test_qlDayCounterDayCount_HalfYear():
    """Test day count between 2024-01-01 and 2024-07-01 (ACTUAL360)."""
    from quantlib_xloil import qlDayCounter, qlDayCounterDayCount, qlDate
    daycounter = qlDayCounter("ACTUAL360")
    date1 = qlDate(2024, 1, 1)
    date2 = qlDate(2024, 7, 1)
    assert qlDayCounterDayCount(daycounter, date1, date2) == 182

def test_qlDayCounterDayCount_BackwardDates():
    """Test day count with end date before start date."""
    from quantlib_xloil import qlDayCounter, qlDayCounterDayCount, qlDate
    daycounter = qlDayCounter("ACTUAL360")
    date1 = qlDate(2024, 7, 1)
    date2 = qlDate(2024, 1, 1)
    assert qlDayCounterDayCount(daycounter, date1, date2) < 0

def test_qlDayCounterName_Actual360():
    """Test name of ACTUAL360 day counter."""
    from quantlib_xloil import qlDayCounter, qlDayCounterName
    daycounter = qlDayCounter("ACTUAL360")
    assert qlDayCounterName(daycounter) == "Actual/360"


def test_qlDayCounterEmpty_False():
    """Test that created day counters are not empty."""
    from quantlib_xloil import qlDayCounter, qlDayCounterEmpty
    daycounter = qlDayCounter("ACTUAL360")
    assert qlDayCounterEmpty(daycounter) is False


def test_qlDayCounterYearFraction_SameDate():
    """Test year fraction for same dates."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFraction, qlDate
    daycounter = qlDayCounter("ACTUAL360")
    date = qlDate(2024, 1, 1)
    assert qlDayCounterYearFraction(daycounter, date, date) == 0.0

def test_qlDayCounterYearFraction_HalfYear():
    """Test year fraction for half year."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFraction, qlDate
    daycounter = qlDayCounter("ACTUAL360")
    date1 = qlDate(2024, 1, 1)
    date2 = qlDate(2024, 7, 1)
    year_frac = qlDayCounterYearFraction(daycounter, date1, date2)
    assert 0.5 < year_frac < 0.51

def test_qlDayCounterYearFraction_OneYear():
    """Test year fraction for one year."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFraction, qlDate
    daycounter = qlDayCounter("ACTUAL365FIXED")
    date1 = qlDate(2024, 1, 1)
    date2 = qlDate(2025, 1, 1)
    year_frac = qlDayCounterYearFraction(daycounter, date1, date2)
    assert 0.99 < year_frac < 1.01

def test_qlDayCounterYearFraction_WithoutRefDates():
    """Test year fraction without reference dates."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFraction, qlDate
    daycounter = qlDayCounter("ACTUAL360")
    date1 = qlDate(2024, 1, 1)
    date2 = qlDate(2024, 7, 1)
    result = qlDayCounterYearFraction(daycounter, date1, date2)
    assert isinstance(result, float)
    assert result > 0

def test_qlDayCounterYearFraction_WithRefDates():
    """Test year fraction with reference dates."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFraction, qlDate
    daycounter = qlDayCounter("ACTUALACTUAL")
    date1 = qlDate(2024, 1, 1)
    date2 = qlDate(2024, 7, 1)
    ref_start = qlDate(2024, 1, 1)
    ref_end = qlDate(2025, 1, 1)
    result = qlDayCounterYearFraction(daycounter, date1, date2, ref_start, ref_end)
    assert isinstance(result, float)
    assert result > 0

def test_qlDayCounterYearFraction_BackwardDates():
    """Test year fraction with end date before start date."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFraction, qlDate
    daycounter = qlDayCounter("ACTUAL360")
    date1 = qlDate(2024, 7, 1)
    date2 = qlDate(2024, 1, 1)
    year_frac = qlDayCounterYearFraction(daycounter, date1, date2)
    assert year_frac < 0

def test_qlDayCounterYearFraction_Actual360Full():
    """Test year fraction calculation for ACTUAL360."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFraction, qlDate
    daycounter = qlDayCounter("ACTUAL360")
    date1 = qlDate(2024, 1, 1)
    date2 = qlDate(2024, 12, 31)
    year_frac = qlDayCounterYearFraction(daycounter, date1, date2)
    # 365 days / 360 = 1.01388...
    assert 1.01 < year_frac < 1.02

def test_qlDayCounterYearFraction_Actual365Full():
    """Test year fraction calculation for ACTUAL365FIXED."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFraction, qlDate
    daycounter = qlDayCounter("ACTUAL365FIXED")
    date1 = qlDate(2024, 1, 1)
    date2 = qlDate(2024, 12, 31)
    year_frac = qlDayCounterYearFraction(daycounter, date1, date2)
    # 365 days / 365 = 1.0
    assert 0.99 < year_frac < 1.01


def test_qlDayCounterYearFractionToDate_ZeroFraction():
    """Test conversion of zero year fraction."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFractionToDate, qlDate
    daycounter = qlDayCounter("ACTUAL360")
    ref_date = qlDate(2024, 1, 1)
    result = qlDayCounterYearFractionToDate(daycounter, ref_date, 0.0)
    assert result.serialNumber() == ref_date.serialNumber()

def test_qlDayCounterYearFractionToDate_HalfYear():
    """Test conversion of half year fraction."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFractionToDate, qlDate
    daycounter = qlDayCounter("ACTUAL360")
    ref_date = qlDate(2024, 1, 1)
    result = qlDayCounterYearFractionToDate(daycounter, ref_date, 0.5)
    # Should be approximately 6 months later
    assert result.month() in (6, 7)

def test_qlDayCounterYearFractionToDate_OneYear():
    """Test conversion of one year fraction."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFractionToDate, qlDate
    daycounter = qlDayCounter("ACTUAL365FIXED")
    ref_date = qlDate(2025, 1, 1)
    result = qlDayCounterYearFractionToDate(daycounter, ref_date, 1.0)
    assert result.year() == 2026

def test_qlDayCounterYearFractionToDate_NegativeFraction():
    """Test conversion of negative year fraction."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFractionToDate, qlDate
    daycounter = qlDayCounter("ACTUAL360")
    ref_date = qlDate(2024, 7, 1)
    result = qlDayCounterYearFractionToDate(daycounter, ref_date, -0.5)
    # Should be approximately 6 months before
    assert result.month() in (1, 12)


def test_qlDayCounterDifferentCounters():
    """Test that different counters give different results."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFraction, qlDate
    date1 = qlDate(2024, 1, 1)
    date2 = qlDate(2024, 12, 31)
    dc_360 = qlDayCounter("ACTUAL360")
    dc_365 = qlDayCounter("ACTUAL365FIXED")

    yf_360 = qlDayCounterYearFraction(dc_360, date1, date2)
    yf_365 = qlDayCounterYearFraction(dc_365, date1, date2)

    assert yf_360 != yf_365
    assert yf_360 > yf_365  # 365 / 360 > 365 / 365


def test_qlDayCounterLeapYearHandling():
    """Test day counting across leap year boundary."""
    from quantlib_xloil import qlDayCounter, qlDayCounterDayCount, qlDate
    date1 = qlDate(2024, 2, 28)
    date2 = qlDate(2024, 3, 1)
    daycounter = qlDayCounter("ACTUAL360")
    day_count = qlDayCounterDayCount(daycounter, date1, date2)
    assert day_count == 2  # 2024 is a leap year


def test_qlDayCounterYearEndBoundary():
    """Test day counting at year end."""
    from quantlib_xloil import qlDayCounter, qlDayCounterDayCount, qlDate
    date1 = qlDate(2024, 12, 31)
    date2 = qlDate(2025, 1, 1)
    daycounter = qlDayCounter("ACTUAL360")
    day_count = qlDayCounterDayCount(daycounter, date1, date2)
    assert day_count == 1


def test_qlDayCounterCenturyBoundary():
    """Test day counting at century boundary."""
    from quantlib_xloil import qlDayCounter, qlDayCounterDayCount, qlDate
    date1 = qlDate(2000, 12, 31)
    date2 = qlDate(2001, 1, 1)
    daycounter = qlDayCounter("ACTUAL360")
    day_count = qlDayCounterDayCount(daycounter, date1, date2)
    assert day_count == 1


def test_qlDayCounterLongPeriod():
    """Test year fraction for long period."""
    from quantlib_xloil import qlDayCounter, qlDayCounterYearFraction, qlDate
    date1 = qlDate(2000, 1, 1)
    date2 = qlDate(2025, 1, 1)
    daycounter = qlDayCounter("ACTUAL360")
    year_frac = qlDayCounterYearFraction(daycounter, date1, date2)
    assert year_frac == 25.366666666666667
