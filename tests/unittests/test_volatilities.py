import pytest
import QuantLib as ql

from quantlib_xloil import (
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
    qlCalendar,
    qlDate,
    qlDayCounter,
    qlDayCounterYearFraction,
    qlLocalVolTermStructureLocalVol,
    qlLocalVolTermStructureLocalVolFromTime,
)


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
    assert variance_by_date == pytest.approx((volatility * volatility) * expected_t_date)


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
    forward_vol_by_time = qlBlackVolTermStructureBlackForwardVolFromTime(handle, 0.5, 1.0, strike)

    assert forward_vol_by_date == pytest.approx(volatility)
    assert forward_vol_by_time == pytest.approx(volatility)


def test_qlBlackVolTermStructure_forward_variance_matches_elapsed_time():
    volatility = 0.20
    strike = 100.0
    handle = _constant_vol_handle(volatility)
    day_counter = qlDayCounter("ACTUAL365FIXED")
    start_date = qlDate(2024, 7, 2)
    end_date = qlDate(2025, 1, 2)

    forward_variance_by_time = qlBlackVolTermStructureBlackForwardVarianceFromTime(handle, 0.5, 1.5, strike)
    forward_variance_by_date = qlBlackVolTermStructureBlackForwardVariance(
        handle,
        start_date,
        end_date,
        strike,
    )
    expected_forward_t = qlDayCounterYearFraction(day_counter, start_date, end_date)

    assert forward_variance_by_time == pytest.approx((volatility * volatility) * 1.0)
    assert forward_variance_by_date == pytest.approx((volatility * volatility) * expected_forward_t)


def test_qlLocalVolTermStructure_interface():
    lvol = ql.LocalConstantVol(qlDate(2024, 1, 2), 0.25, qlDayCounter("ACTUAL365FIXED"))
    lvol_handle = ql.LocalVolTermStructureHandle(lvol)

    assert qlLocalVolTermStructureLocalVol(lvol_handle, qlDate(2024, 7, 2), 100.0) == pytest.approx(0.25)
    assert qlLocalVolTermStructureLocalVolFromTime(lvol_handle, 0.5, 100.0) == pytest.approx(0.25)
