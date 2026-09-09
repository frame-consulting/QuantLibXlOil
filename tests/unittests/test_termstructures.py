import QuantLib as ql
import pytest

from quantlib_xloil.termstructures import (
    qCompounding,
    qlFlatForward,
    qlFlatForward2,
    qlForwardSpreadedTermStructure,
    qlImpliedTermStructure,
    qlCompositeZeroYieldStructure,
    qlTermStructureAllowsExtrapolation,
    qlTermStructureCalendar,
    qlTermStructureDayCounter,
    qlTermStructureDisableExrapolation,
    qlTermStructureEnableExrapolation,
    qlTermStructureMaxDate,
    qlTermStructureMaxTime,
    qlTermStructureReferenceDate,
    qlTermStructureTimeFromReference,
    qlUltimateForwardTermStructure,
    qlYieldTermStructureDiscount,
    qlYieldTermStructureDiscountFromTime,
    qlYieldTermStructureForwardRate,
    qlYieldTermStructureForwardRateFromTime,
    qlYieldTermStructureZeroRate,
    qlYieldTermStructureZeroRateFromTime,
    qlZeroSpreadedTermStructure,
    qlPiecewiseZeroSpreadedTermStructure,
    qlSpreadedLinearZeroInterpolatedTermStructure,
    qlSpreadedBackwardFlatZeroInterpolatedTermStructure,
    qlSpreadedCubicZeroInterpolatedTermStructure,
    qlSpreadedKrugerZeroInterpolatedTermStructure,
    qlSpreadedSplineCubicZeroInterpolatedTermStructure,
    qlSpreadedParabolicCubicZeroInterpolatedTermStructure,
    qlSpreadedMonotonicParabolicCubicZeroInterpolatedTermStructure,
    qlPiecewiseForwardSpreadedTermStructure,
    qlPiecewiseLinearForwardSpreadedTermStructure,
    qlQuantoTermStructure,
)
from quantlib_xloil.calendars import qlCalendar
from quantlib_xloil.date import qFrequency, qlDate, qlPeriod, qTimeUnit
from quantlib_xloil.daycounters import qlDayCounter


def _base_curve():
    reference_date = qlDate(2024, 1, 2)
    daycounter = qlDayCounter("ACTUAL365FIXED")
    calendar = qlCalendar("TARGET")
    return qlFlatForward(
        reference_date,
        0.05,
        daycounter,
        qCompounding.__wrapped__("COMPOUNDED"),
        qFrequency.__wrapped__("ANNUAL"),
        calendar,
    )


def _future_date(year: int, month: int, day: int):
    return qlDate(year, month, day)


def _black_vol_term_structure():
    """Helper function to create a simple BlackVolTermStructureHandle for testing."""
    reference_date = qlDate(2024, 1, 2)
    daycounter = qlDayCounter("ACTUAL365FIXED")
    calendar = qlCalendar("TARGET")
    
    # Create a flat volatility term structure using BlackVarianceCurve
    # Constructor: (Date, vector<Date>, vector<Volatility>, DayCounter)
    vol = 0.2  # 20% volatility
    
    # Create dates vector (1 day, 1 year, 2 years, 5 years, 10 years from reference)
    dates = [
        calendar.advance(reference_date, ql.Period(1, ql.Days)),
        calendar.advance(reference_date, ql.Period(1, ql.Years)),
        calendar.advance(reference_date, ql.Period(2, ql.Years)),
        calendar.advance(reference_date, ql.Period(5, ql.Years)),
        calendar.advance(reference_date, ql.Period(10, ql.Years)),
    ]
    
    # Flat volatility for all dates
    vols = [vol, vol, vol, vol, vol]
    
    vol_ts = ql.BlackVarianceCurve(
        reference_date,
        dates,
        vols,
        daycounter
    )
    return ql.BlackVolTermStructureHandle(vol_ts)


def test_qCompounding_case_insensitive():
    assert qCompounding.__wrapped__("simple") == ql.Simple
    assert qCompounding.__wrapped__("Compounded") == ql.Compounded
    assert qCompounding.__wrapped__("CONTINUOUS") == ql.Continuous


def test_qlTermStructure_accessors_and_extrapolation_flags():
    handle = _base_curve()
    reference_date = qlTermStructureReferenceDate(handle)
    daycounter = qlTermStructureDayCounter(handle)
    calendar = qlTermStructureCalendar(handle)
    max_date = qlTermStructureMaxDate(handle)
    max_time = qlTermStructureMaxTime(handle)

    assert reference_date == qlDate(2024, 1, 2)
    assert isinstance(daycounter, ql.DayCounter)
    assert isinstance(calendar, ql.Calendar)
    assert max_date > reference_date
    assert max_time > 0.0
    assert qlTermStructureTimeFromReference(handle, reference_date) == 0.0
    assert qlTermStructureAllowsExtrapolation(handle) is False
    assert qlTermStructureEnableExrapolation(handle) is True
    assert qlTermStructureAllowsExtrapolation(handle) is True
    assert qlTermStructureDisableExrapolation(handle) is True
    assert qlTermStructureAllowsExtrapolation(handle) is False


def test_qlYieldTermStructure_discount_zero_and_forward_rates():
    handle = _base_curve()
    daycounter = qlDayCounter("ACTUAL365FIXED")
    date1 = qlDate(2024, 7, 2)
    date2 = qlDate(2025, 1, 2)

    discount_by_date = qlYieldTermStructureDiscount(handle, date1)
    discount_by_time = qlYieldTermStructureDiscountFromTime(handle, 0.5)
    zero_rate = qlYieldTermStructureZeroRate(
        handle,
        date1,
        daycounter,
        qCompounding.__wrapped__("COMPOUNDED"),
        qFrequency.__wrapped__("ANNUAL"),
    )
    zero_rate_time = qlYieldTermStructureZeroRateFromTime(
        handle,
        0.5,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
    )
    forward_rate = qlYieldTermStructureForwardRate(
        handle,
        date1,
        date2,
        daycounter,
        qCompounding.__wrapped__("COMPOUNDED"),
        qFrequency.__wrapped__("ANNUAL"),
    )
    forward_rate_time = qlYieldTermStructureForwardRateFromTime(
        handle,
        0.5,
        1.0,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
    )

    assert 0.0 < discount_by_date < 1.0
    assert 0.0 < discount_by_time < 1.0
    assert zero_rate > 0.0
    assert zero_rate_time > 0.0
    assert forward_rate > 0.0
    assert forward_rate_time > 0.0


def test_qlFlatForward_and_implied_and_spreaded_term_structures():
    base = _base_curve()
    spreaded_zero = qlZeroSpreadedTermStructure(
        base,
        0.001,
        qCompounding.__wrapped__("COMPOUNDED"),
        qFrequency.__wrapped__("ANNUAL"),
        qlDayCounter("ACTUAL365FIXED"),
    )
    spreaded_forward = qlForwardSpreadedTermStructure(base, 0.001)
    implied = qlImpliedTermStructure(base, qlDate(2024, 7, 2))

    assert isinstance(spreaded_zero, ql.YieldTermStructureHandle)
    assert isinstance(spreaded_forward, ql.YieldTermStructureHandle)
    assert isinstance(implied, ql.YieldTermStructureHandle)
    assert spreaded_zero.currentLink() is not None
    assert spreaded_forward.currentLink() is not None
    assert implied.currentLink() is not None


def test_qlFlatForward2():
    settlement_days = 2
    calendar = qlCalendar("TARGET")
    forward_rate = 0.05
    daycounter = qlDayCounter("ACTUAL365FIXED")
    compounding = qCompounding.__wrapped__("COMPOUNDED")
    frequency = qFrequency.__wrapped__("ANNUAL")

    handle = qlFlatForward2(
        settlement_days,
        calendar,
        forward_rate,
        daycounter,
        compounding,
        frequency,
    )

    assert isinstance(handle, ql.YieldTermStructureHandle)
    assert handle.currentLink() is not None
    assert qlTermStructureCalendar(handle) == calendar
    assert qlTermStructureDayCounter(handle) == daycounter


def test_qlCompositeZeroYieldStructure_valid_and_invalid_operator():
    curve1 = _base_curve()
    curve2 = qlFlatForward(
        qlDate(2024, 1, 2),
        0.01,
        qlDayCounter("ACTUAL365FIXED"),
        qCompounding.__wrapped__("COMPOUNDED"),
        qFrequency.__wrapped__("ANNUAL"),
        qlCalendar("TARGET"),
    )

    combined_add = qlCompositeZeroYieldStructure(curve1, curve2, "+")
    combined_sub = qlCompositeZeroYieldStructure(curve1, curve2, "-")

    assert isinstance(combined_add, ql.YieldTermStructureHandle)
    assert isinstance(combined_sub, ql.YieldTermStructureHandle)
    assert combined_add.currentLink() is not None
    assert combined_sub.currentLink() is not None

    with pytest.raises(ValueError, match="Invalid operator"):
        qlCompositeZeroYieldStructure(curve1, curve2, "*")


def test_qlUltimateForwardTermStructure():
    base_curve = _base_curve()
    daycounter = qlDayCounter("ACTUAL365FIXED")

    # Create the UltimateForwardTermStructure
    first_smoothing_point = qlPeriod(5, qTimeUnit.__wrapped__("YEARS"))
    handle = qlUltimateForwardTermStructure(
        base_curve,
        last_liquid_forward=0.05,
        ultimate_forward=0.04,
        first_smoothing_point=first_smoothing_point,
        alpha=0.5,
        rounding_digits=None,
        compounding=qCompounding.__wrapped__("COMPOUNDED"),
        frequency=qFrequency.__wrapped__("ANNUAL"),
    )

    assert isinstance(handle, ql.YieldTermStructureHandle)
    assert handle.currentLink() is not None

    # Test basic term structure accessors
    assert qlTermStructureReferenceDate(handle) == qlDate(2024, 1, 2)
    assert qlTermStructureDayCounter(handle) == daycounter

    # Test that we can query rates from the structure
    date1 = qlDate(2024, 7, 2)
    date2 = qlDate(2029, 1, 2)  # Beyond the smoothing point

    discount = qlYieldTermStructureDiscount(handle, date1)
    forward_rate = qlYieldTermStructureForwardRate(
        handle,
        date1,
        date2,
        daycounter,
        qCompounding.__wrapped__("COMPOUNDED"),
        qFrequency.__wrapped__("ANNUAL"),
    )

    assert 0.0 < discount < 1.0
    assert forward_rate > 0.0


def test_qlInterpolatedPiecewiseZeroSpreadedTermStructure_all_interpolators():
    """Test all 8 interpolated piecewise zero spreaded term structure functions."""
    base = _base_curve()
    reference_date = qlDate(2024, 1, 2)
    daycounter = qlDayCounter("ACTUAL365FIXED")

    # Define spreads and dates for interpolation
    spreads = [0.01, 0.015, 0.02, 0.025]
    dates = [
        qlDate(2024, 1, 2),
        qlDate(2025, 1, 2),
        qlDate(2026, 1, 2),
        qlDate(2027, 1, 2),
    ]

    # Test 1: PiecewiseZeroSpreadedTermStructure (Linear)
    handle1 = qlPiecewiseZeroSpreadedTermStructure(
        base,
        spreads,
        dates,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
        daycounter,
    )
    assert isinstance(handle1, ql.YieldTermStructureHandle)
    assert handle1.currentLink() is not None
    assert qlTermStructureReferenceDate(handle1) == reference_date

    # Test 2: SpreadedLinearZeroInterpolatedTermStructure
    handle2 = qlSpreadedLinearZeroInterpolatedTermStructure(
        base,
        spreads,
        dates,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
        daycounter,
    )
    assert isinstance(handle2, ql.YieldTermStructureHandle)
    assert handle2.currentLink() is not None
    assert qlTermStructureReferenceDate(handle2) == reference_date

    # Test 3: SpreadedBackwardFlatZeroInterpolatedTermStructure
    handle3 = qlSpreadedBackwardFlatZeroInterpolatedTermStructure(
        base,
        spreads,
        dates,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
        daycounter,
    )
    assert isinstance(handle3, ql.YieldTermStructureHandle)
    assert handle3.currentLink() is not None
    assert qlTermStructureReferenceDate(handle3) == reference_date

    # Test 4: SpreadedCubicZeroInterpolatedTermStructure
    handle4 = qlSpreadedCubicZeroInterpolatedTermStructure(
        base,
        spreads,
        dates,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
        daycounter,
    )
    assert isinstance(handle4, ql.YieldTermStructureHandle)
    assert handle4.currentLink() is not None
    assert qlTermStructureReferenceDate(handle4) == reference_date

    # Test 5: SpreadedKrugerZeroInterpolatedTermStructure
    handle5 = qlSpreadedKrugerZeroInterpolatedTermStructure(
        base,
        spreads,
        dates,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
        daycounter,
    )
    assert isinstance(handle5, ql.YieldTermStructureHandle)
    assert handle5.currentLink() is not None
    assert qlTermStructureReferenceDate(handle5) == reference_date

    # Test 6: SpreadedSplineCubicZeroInterpolatedTermStructure
    handle6 = qlSpreadedSplineCubicZeroInterpolatedTermStructure(
        base,
        spreads,
        dates,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
        daycounter,
    )
    assert isinstance(handle6, ql.YieldTermStructureHandle)
    assert handle6.currentLink() is not None
    assert qlTermStructureReferenceDate(handle6) == reference_date

    # Test 7: SpreadedParabolicCubicZeroInterpolatedTermStructure
    handle7 = qlSpreadedParabolicCubicZeroInterpolatedTermStructure(
        base,
        spreads,
        dates,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
        daycounter,
    )
    assert isinstance(handle7, ql.YieldTermStructureHandle)
    assert handle7.currentLink() is not None
    assert qlTermStructureReferenceDate(handle7) == reference_date

    # Test 8: SpreadedMonotonicParabolicCubicZeroInterpolatedTermStructure
    handle8 = qlSpreadedMonotonicParabolicCubicZeroInterpolatedTermStructure(
        base,
        spreads,
        dates,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
        daycounter,
    )
    assert isinstance(handle8, ql.YieldTermStructureHandle)
    assert handle8.currentLink() is not None
    assert qlTermStructureReferenceDate(handle8) == reference_date


def test_qlInterpolatedPiecewiseZeroSpreadedTermStructure_rates():
    """Test that we can query rates from interpolated piecewise zero spreaded term structures."""
    base = _base_curve()
    daycounter = qlDayCounter("ACTUAL365FIXED")

    spreads = [0.01, 0.015, 0.02]
    dates = [
        qlDate(2024, 1, 2),
        qlDate(2025, 1, 2),
        qlDate(2026, 1, 2),
    ]

    # Test with Linear interpolator
    handle = qlSpreadedLinearZeroInterpolatedTermStructure(
        base,
        spreads,
        dates,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
        daycounter,
    )

    # Query discount factors and rates at various points
    test_date = qlDate(2024, 7, 2)
    discount = qlYieldTermStructureDiscount(handle, test_date)
    zero_rate = qlYieldTermStructureZeroRate(
        handle,
        test_date,
        daycounter,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
    )

    assert 0.0 < discount < 1.0
    assert zero_rate > 0.0

    # Test with Cubic interpolator
    handle_cubic = qlSpreadedCubicZeroInterpolatedTermStructure(
        base,
        spreads,
        dates,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
        daycounter,
    )

    discount_cubic = qlYieldTermStructureDiscount(handle_cubic, test_date)
    zero_rate_cubic = qlYieldTermStructureZeroRate(
        handle_cubic,
        test_date,
        daycounter,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
    )

    assert 0.0 < discount_cubic < 1.0
    assert zero_rate_cubic > 0.0


def test_qlPiecewiseForwardSpreadedTermStructure():
    """Test construction and basic functionality of piecewise forward spreaded term structures."""
    base = _base_curve()
    reference_date = qlDate(2024, 1, 2)
    daycounter = qlDayCounter("ACTUAL365FIXED")

    spreads = [0.01, 0.015, 0.02, 0.025]
    dates = [
        qlDate(2024, 1, 2),
        qlDate(2025, 1, 2),
        qlDate(2026, 1, 2),
        qlDate(2027, 1, 2),
    ]

    # Test PiecewiseForwardSpreadedTermStructure (BackwardFlat)
    handle_forward = qlPiecewiseForwardSpreadedTermStructure(
        base, spreads, dates, daycounter
    )
    assert isinstance(handle_forward, ql.YieldTermStructureHandle)
    assert handle_forward.currentLink() is not None
    assert qlTermStructureReferenceDate(handle_forward) == reference_date

    # Test PiecewiseLinearForwardSpreadedTermStructure (Linear)
    handle_linear = qlPiecewiseLinearForwardSpreadedTermStructure(
        base, spreads, dates, daycounter
    )
    assert isinstance(handle_linear, ql.YieldTermStructureHandle)
    assert handle_linear.currentLink() is not None
    assert qlTermStructureReferenceDate(handle_linear) == reference_date


def test_qlPiecewiseForwardSpreadedTermStructure_rates():
    """Test that we can query rates from piecewise forward spreaded term structures."""
    base = _base_curve()
    daycounter = qlDayCounter("ACTUAL365FIXED")

    spreads = [0.01, 0.015, 0.02]
    dates = [
        qlDate(2024, 1, 2),
        qlDate(2025, 1, 2),
        qlDate(2026, 1, 2),
    ]

    # Test with BackwardFlat interpolator
    handle_forward = qlPiecewiseForwardSpreadedTermStructure(
        base, spreads, dates, daycounter
    )

    test_date = qlDate(2024, 7, 2)
    discount_forward = qlYieldTermStructureDiscount(handle_forward, test_date)
    forward_rate_forward = qlYieldTermStructureForwardRate(
        handle_forward,
        test_date,
        qlDate(2025, 1, 2),
        daycounter,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
    )

    assert 0.0 < discount_forward < 1.0
    assert forward_rate_forward > 0.0

    # Test with Linear interpolator
    handle_linear = qlPiecewiseLinearForwardSpreadedTermStructure(
        base, spreads, dates, daycounter
    )

    discount_linear = qlYieldTermStructureDiscount(handle_linear, test_date)
    forward_rate_linear = qlYieldTermStructureForwardRate(
        handle_linear,
        test_date,
        qlDate(2025, 1, 2),
        daycounter,
        qCompounding.__wrapped__("CONTINUOUS"),
        qFrequency.__wrapped__("NOFREQUENCY"),
    )

    assert 0.0 < discount_linear < 1.0
    assert forward_rate_linear > 0.0


def test_qlQuantoTermStructure():
    """Test construction of QuantoTermStructure for cross-currency derivatives pricing."""
    # Create base curves
    underlying_dividend_ts = _base_curve()
    risk_free_ts = _base_curve()
    foreign_risk_free_ts = qlFlatForward(
        qlDate(2024, 1, 2),
        0.03,  # Different rate for foreign
        qlDayCounter("ACTUAL365FIXED"),
        qCompounding.__wrapped__("COMPOUNDED"),
        qFrequency.__wrapped__("ANNUAL"),
        qlCalendar("TARGET"),
    )
    
    # Create volatility term structures
    underlying_black_vol_ts = _black_vol_term_structure()
    exch_rate_black_vol_ts = _black_vol_term_structure()
    
    # Quanto parameters
    strike = 100.0
    exch_rate_atm_level = 1.1
    underlying_exch_rate_correlation = 0.7
    
    # Create the QuantoTermStructure
    handle = qlQuantoTermStructure(
        underlying_dividend_ts,
        risk_free_ts,
        foreign_risk_free_ts,
        underlying_black_vol_ts,
        strike,
        exch_rate_black_vol_ts,
        exch_rate_atm_level,
        underlying_exch_rate_correlation,
    )
    
    # Verify the handle is created correctly
    assert isinstance(handle, ql.YieldTermStructureHandle)
    assert handle.currentLink() is not None
    
    # Test basic term structure accessors
    reference_date = qlDate(2024, 1, 2)
    assert qlTermStructureReferenceDate(handle) == reference_date
    
    # Test that we can query discount factors
    test_date = qlDate(2024, 7, 2)
    discount = qlYieldTermStructureDiscount(handle, test_date)
    
    assert 0.0 < discount < 1.0
