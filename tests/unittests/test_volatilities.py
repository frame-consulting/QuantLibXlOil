import pytest
import QuantLib as ql

from quantlib_xloil.volatilities import (
    qlBlackConstantVol,
    qlBlackVolTermStructureBlackForwardVariance,
    qlBlackVolTermStructureBlackForwardVarianceFromTime,
    qlBlackVolTermStructureBlackForwardVol,
    qlBlackVolTermStructureBlackForwardVolFromTime,
    qlBlackVolTermStructureBlackVariance,
    qlBlackVolTermStructureBlackVarianceFromTime,
    qlBlackVolTermStructureBlackVol,
    qlBlackVolTermStructureBlackVolFromTime,
    qlBlackVolTermStructureMaxStrike,
    qlBlackVolTermStructureMinStrike,
    qlConstantOptionletVolatility,
    qlConstantSwaptionVolatility,
    qlLocalVolTermStructureLocalVol,
    qlLocalVolTermStructureLocalVolFromTime,
    qlOptionletVolatilityStructureBlackVariance,
    qlOptionletVolatilityStructureBlackVarianceFromTime,
    qlOptionletVolatilityStructureVolatility,
    qlOptionletVolatilityStructureVolatilityFromTime,
    qlSwaptionVolatilityStructureBlackVariance,
    qlSwaptionVolatilityStructureBlackVarianceFromTime,
    qlSwaptionVolatilityStructureOptionDateFromTenor,
    qlSwaptionVolatilityStructureShift,
    qlSwaptionVolatilityStructureShiftFromTime,
    qlSwaptionVolatilityStructureSmileSection,
    qlSwaptionVolatilityStructureSmileSectionFromTime,
    qlSwaptionVolatilityStructureVolatility,
    qlSwaptionVolatilityStructureVolatilityFromTime,
    qlSwaptionVolatilityMatrix,
    qVolatilityType,
)
from quantlib_xloil.calendars import qBusinessDayConvention, qlCalendar
from quantlib_xloil.date import qlDate, qlPeriod
from quantlib_xloil.daycounters import qlDayCounter, qlDayCounterYearFraction
from quantlib_xloil.ratehelpers import qQuoteHandle


def _constant_vol_handle(volatility: float = 0.20):
    return qlBlackConstantVol(
        qlDate(2024, 1, 2),
        qlCalendar("TARGET"),
        volatility,
        qlDayCounter("ACTUAL365FIXED"),
    )


def test_qlBlackConstantVol_creates_handle_with_valid_strike_range():
    handle = _constant_vol_handle()

    min_strike = qlBlackVolTermStructureMinStrike(handle)
    max_strike = qlBlackVolTermStructureMaxStrike(handle)

    assert min_strike < max_strike


def test_qlBlackVolTermStructure_black_vol_is_constant_for_date_and_time():
    volatility = 0.20
    strike = 100.0
    handle = _constant_vol_handle(volatility)

    by_date = qlBlackVolTermStructureBlackVol(handle, qlDate(2024, 7, 2), strike)
    by_time = qlBlackVolTermStructureBlackVolFromTime(handle, 0.5, strike)

    assert by_date == pytest.approx(volatility)
    assert by_time == pytest.approx(volatility)


def test_qlBlackVolTermStructure_black_variance_for_time_and_date():
    volatility = 0.20
    strike = 100.0
    handle = _constant_vol_handle(volatility)
    day_counter = qlDayCounter("ACTUAL365FIXED")
    reference_date = qlDate(2024, 1, 2)
    expiry_date = qlDate(2025, 1, 2)

    t = 2.0
    variance_by_time = qlBlackVolTermStructureBlackVarianceFromTime(handle, t, strike)
    variance_by_date = qlBlackVolTermStructureBlackVariance(handle, expiry_date, strike)
    expected_t_date = qlDayCounterYearFraction(day_counter, reference_date, expiry_date)

    assert variance_by_time == pytest.approx((volatility * volatility) * t)
    assert variance_by_date == pytest.approx(
        (volatility * volatility) * expected_t_date
    )


def test_qlBlackVolTermStructure_forward_vol_is_constant_for_date_and_time():
    volatility = 0.20
    strike = 100.0
    handle = _constant_vol_handle(volatility)

    forward_vol_by_date = qlBlackVolTermStructureBlackForwardVol(
        handle,
        qlDate(2024, 7, 2),
        qlDate(2025, 1, 2),
        strike,
    )
    forward_vol_by_time = qlBlackVolTermStructureBlackForwardVolFromTime(
        handle, 0.5, 1.0, strike
    )

    assert forward_vol_by_date == pytest.approx(volatility)
    assert forward_vol_by_time == pytest.approx(volatility)


def test_qlBlackVolTermStructure_forward_variance_matches_elapsed_time():
    volatility = 0.20
    strike = 100.0
    handle = _constant_vol_handle(volatility)
    day_counter = qlDayCounter("ACTUAL365FIXED")
    start_date = qlDate(2024, 7, 2)
    end_date = qlDate(2025, 1, 2)

    forward_variance_by_time = qlBlackVolTermStructureBlackForwardVarianceFromTime(
        handle, 0.5, 1.5, strike
    )
    forward_variance_by_date = qlBlackVolTermStructureBlackForwardVariance(
        handle,
        start_date,
        end_date,
        strike,
    )
    expected_forward_t = qlDayCounterYearFraction(day_counter, start_date, end_date)

    assert forward_variance_by_time == pytest.approx((volatility * volatility) * 1.0)
    assert forward_variance_by_date == pytest.approx(
        (volatility * volatility) * expected_forward_t
    )


def test_qlLocalVolTermStructure_interface():
    lvol = ql.LocalConstantVol(qlDate(2024, 1, 2), 0.25, qlDayCounter("ACTUAL365FIXED"))
    lvol_handle = ql.LocalVolTermStructureHandle(lvol)

    assert qlLocalVolTermStructureLocalVol(
        lvol_handle, qlDate(2024, 7, 2), 100.0
    ) == pytest.approx(0.25)
    assert qlLocalVolTermStructureLocalVolFromTime(
        lvol_handle, 0.5, 100.0
    ) == pytest.approx(0.25)


# Helper functions for optionlet and swaption volatility tests


def _constant_optionlet_vol_handle(volatility: float = 0.20):
    return qlConstantOptionletVolatility(
        reference_date=qlDate(2024, 1, 2),
        calendar=qlCalendar("TARGET"),
        business_day_convention=qBusinessDayConvention.__wrapped__("FOLLOWING"),
        volatility=qQuoteHandle.__wrapped__(volatility),
        day_counter=qlDayCounter("ACTUAL365FIXED"),
        volatility_type=qVolatilityType.__wrapped__("SHIFTEDLOGNORMAL"),
        shift=0.0,
    )


def _constant_swaption_vol_handle(volatility: float = 0.20):
    return qlConstantSwaptionVolatility(
        reference_date=qlDate(2024, 1, 2),
        calendar=qlCalendar("TARGET"),
        business_day_convention=qBusinessDayConvention.__wrapped__("FOLLOWING"),
        volatility=qQuoteHandle.__wrapped__(volatility),
        day_counter=qlDayCounter("ACTUAL365FIXED"),
        volatility_type=qVolatilityType.__wrapped__("SHIFTEDLOGNORMAL"),
        shift=0.0,
    )


# OptionletVolatilityStructure tests


def test_qlConstantOptionletVolatility_creates_handle():
    handle = _constant_optionlet_vol_handle()
    assert isinstance(handle, ql.OptionletVolatilityStructureHandle)


def test_qlOptionletVolatilityStructure_volatility_constant_for_date_and_time():
    volatility = 0.20
    strike = 100.0
    handle = _constant_optionlet_vol_handle(volatility)

    vol_by_date = qlOptionletVolatilityStructureVolatility(
        handle, qlDate(2024, 7, 2), strike
    )
    vol_by_time = qlOptionletVolatilityStructureVolatilityFromTime(handle, 0.5, strike)

    assert vol_by_date == pytest.approx(volatility)
    assert vol_by_time == pytest.approx(volatility)


def test_qlOptionletVolatilityStructure_black_variance():
    volatility = 0.20
    strike = 100.0
    handle = _constant_optionlet_vol_handle(volatility)
    day_counter = qlDayCounter("ACTUAL365FIXED")
    reference_date = qlDate(2024, 1, 2)
    option_date = qlDate(2025, 1, 2)

    t = 1.0
    variance_by_time = qlOptionletVolatilityStructureBlackVarianceFromTime(
        handle, t, strike
    )
    variance_by_date = qlOptionletVolatilityStructureBlackVariance(
        handle, option_date, strike
    )
    expected_t_date = qlDayCounterYearFraction(day_counter, reference_date, option_date)

    assert variance_by_time == pytest.approx((volatility * volatility) * t)
    assert variance_by_date == pytest.approx(
        (volatility * volatility) * expected_t_date
    )


# SwaptionVolatilityStructure tests


def test_qlConstantSwaptionVolatility_creates_handle():
    handle = _constant_swaption_vol_handle()
    assert isinstance(handle, ql.SwaptionVolatilityStructureHandle)


def test_qlSwaptionVolatilityStructure_volatility_constant_for_date_and_time():
    volatility = 0.20
    strike = 100.0
    handle = _constant_swaption_vol_handle(volatility)

    vol_by_date = qlSwaptionVolatilityStructureVolatility(
        handle,
        option_date=qlDate(2024, 7, 2),
        swap_tenor=ql.Period("5Y"),
        strike=strike,
    )
    vol_by_time = qlSwaptionVolatilityStructureVolatilityFromTime(
        handle, option_time=0.5, swap_length=5.0, strike=strike
    )

    assert vol_by_date == pytest.approx(volatility)
    assert vol_by_time == pytest.approx(volatility)


def test_qlSwaptionVolatilityStructure_black_variance():
    volatility = 0.20
    strike = 100.0
    handle = _constant_swaption_vol_handle(volatility)

    option_date = qlDate(2024, 7, 2)
    option_time = handle.timeFromReference(option_date)
    swap_tenor = ql.Period("5Y")
    swap_length = 5.0

    variance_by_date = qlSwaptionVolatilityStructureBlackVariance(
        handle,
        option_date=option_date,
        swap_tenor=swap_tenor,
        strike=strike,
    )

    variance_by_time = qlSwaptionVolatilityStructureBlackVarianceFromTime(
        handle, option_time=option_time, swap_length=swap_length, strike=strike
    )

    # For constant volatility, variance = vol^2 * time
    # The time here is the option time (0.5 years)
    assert variance_by_time == pytest.approx((volatility * volatility) * option_time)
    assert variance_by_date == pytest.approx((volatility * volatility) * option_time)


def test_qlSwaptionVolatilityStructure_option_date_from_tenor():
    handle = _constant_swaption_vol_handle()
    reference_date = qlDate(2024, 1, 2)

    option_date = qlSwaptionVolatilityStructureOptionDateFromTenor(
        handle, option_tenor=ql.Period(6, ql.Months)
    )

    expected_date = reference_date + ql.Period(6, ql.Months)
    assert option_date == expected_date


def test_qlSwaptionVolatilityStructure_shift():
    shift = 0.01
    handle = qlConstantSwaptionVolatility(
        reference_date=qlDate(2024, 1, 2),
        calendar=qlCalendar("TARGET"),
        business_day_convention=qBusinessDayConvention.__wrapped__("FOLLOWING"),
        volatility=qQuoteHandle.__wrapped__(0.20),
        day_counter=qlDayCounter("ACTUAL365FIXED"),
        volatility_type=qVolatilityType.__wrapped__("SHIFTEDLOGNORMAL"),
        shift=shift,
    )

    shift_by_date = qlSwaptionVolatilityStructureShift(
        handle,
        option_date=qlDate(2024, 7, 2),
        swap_tenor=ql.Period("5Y"),
    )
    shift_by_time = qlSwaptionVolatilityStructureShiftFromTime(
        handle, option_time=0.5, swap_length=5.0
    )

    assert shift_by_date == pytest.approx(shift)
    assert shift_by_time == pytest.approx(shift)


def test_qlSwaptionVolatilityStructure_smile_section():
    handle = _constant_swaption_vol_handle(0.20)

    smile_by_date = qlSwaptionVolatilityStructureSmileSection(
        handle,
        option_date=qlDate(2024, 7, 2),
        swap_tenor=qlPeriod(5, ql.Years),
    )
    smile_by_time = qlSwaptionVolatilityStructureSmileSectionFromTime(
        handle, option_time=0.5, swap_length=5.0
    )

    assert isinstance(smile_by_date, ql.SmileSection)
    assert isinstance(smile_by_time, ql.SmileSection)


def test_qlVolatilityType_converter():
    assert qVolatilityType.__wrapped__("NORMAL") == ql.Normal
    assert qVolatilityType.__wrapped__("SHIFTEDLOGNORMAL") == ql.ShiftedLognormal


def test_qlSwaptionVolatilityMatrix_creates_handle_and_interpolates():
    import numpy as np

    reference_date = qlDate(2024, 1, 2)
    day_counter = qlDayCounter("ACTUAL365FIXED")

    # Define a 2x2 vol matrix: 2 expiries x 2 swap tenors
    expiry_dates = np.array(
        [
            qlDate(2025, 1, 2),
            qlDate(2026, 1, 2),
        ]
    )
    lengths = np.array([qlPeriod(2, ql.Years), qlPeriod(5, ql.Years)])
    vols = np.array([[0.20, 0.22], [0.18, 0.21]])

    handle = qlSwaptionVolatilityMatrix(
        reference_date=reference_date,
        expiry_dates=expiry_dates,
        lengths=lengths,
        vols=vols,
        day_counter=day_counter,
        flat_extrapolation=True,
        volatility_type=qVolatilityType.__wrapped__("SHIFTEDLOGNORMAL"),
        shifts=None,
    )

    assert isinstance(handle, ql.SwaptionVolatilityStructureHandle)

    # Volatility at grid nodes should match input
    vol_1y_2y = qlSwaptionVolatilityStructureVolatility(
        handle,
        option_date=expiry_dates[0],
        swap_tenor=lengths[0],
        strike=0.025,
    )
    vol_2y_5y = qlSwaptionVolatilityStructureVolatility(
        handle,
        option_date=expiry_dates[1],
        swap_tenor=lengths[1],
        strike=0.025,
    )

    assert vol_1y_2y == pytest.approx(vols[0, 0], rel=1e-4)
    assert vol_2y_5y == pytest.approx(vols[1, 1], rel=1e-4)
