import QuantLib as ql
import pytest

from quantlibxloil import (
	qlCalendar,
	qlDayCounter,
	qlDate,
	qlDiscountCurve,
	qlForwardCurve,
	qlInterpolatedYieldCurve,
	qlZeroCurve,
)


def _sample_dates():
	return [
		qlDate(2025, 1, 2),
		qlDate(2025, 7, 2),
		qlDate(2026, 1, 2),
		qlDate(2027, 1, 4),
	]


def _sample_context():
	daycounter = qlDayCounter("ACTUAL365FIXED")
	calendar = qlCalendar("TARGET")
	return daycounter, calendar


def test_qlInterpolatedYieldCurve_LogDiscount_Linear():
	dates = _sample_dates()
	discounts = [1.0, 0.99, 0.975, 0.95]
	daycounter, calendar = _sample_context()

	handle = qlInterpolatedYieldCurve(
		dates,
		discounts,
		daycounter,
		calendar,
		"LOGDISCOUNT",
		"LINEAR",
	)

	assert isinstance(handle, ql.YieldTermStructureHandle)
	assert handle.currentLink() is not None
	assert handle.discount(dates[1]) > 0.0


def test_qlInterpolatedYieldCurve_ZeroRate_MonotonicCubic_CaseInsensitive():
	dates = _sample_dates()
	zerorates = [0.01, 0.0125, 0.015, 0.0175]
	daycounter, calendar = _sample_context()

	handle = qlInterpolatedYieldCurve(
		dates,
		zerorates,
		daycounter,
		calendar,
		"  zeroRate  ",
		"  monotoniccubic  ",
	)

	assert isinstance(handle, ql.YieldTermStructureHandle)
	assert handle.currentLink() is not None
	assert handle.discount(dates[2]) > 0.0


def test_qlInterpolatedYieldCurve_ForwardRate_ForwardFlat():
	dates = _sample_dates()
	forwards = [0.01, 0.011, 0.012, 0.013]
	daycounter, calendar = _sample_context()

	handle = qlInterpolatedYieldCurve(
		dates,
		forwards,
		daycounter,
		calendar,
		"FORWARDRATE",
		"FORWARDFLAT",
	)

	assert isinstance(handle, ql.YieldTermStructureHandle)
	assert handle.currentLink() is not None


def test_qlInterpolatedYieldCurve_InvalidTraits_raises():
	dates = _sample_dates()
	values = [1.0, 0.99, 0.975, 0.95]
	daycounter, calendar = _sample_context()

	with pytest.raises(ValueError, match="Invalid traits"):
		qlInterpolatedYieldCurve(
			dates,
			values,
			daycounter,
			calendar,
			"BADTRAIT",
			"LINEAR",
		)


def test_qlInterpolatedYieldCurve_InvalidInterpolator_raises():
	dates = _sample_dates()
	values = [1.0, 0.99, 0.975, 0.95]
	daycounter, calendar = _sample_context()

	with pytest.raises(ValueError, match="Invalid interpolator"):
		qlInterpolatedYieldCurve(
			dates,
			values,
			daycounter,
			calendar,
			"LOGDISCOUNT",
			"BADINTERP",
		)


def test_qlInterpolatedYieldCurve_NotImplementedCombination_raises():
	dates = _sample_dates()
	values = [1.0, 0.99, 0.975, 0.95]
	daycounter, calendar = _sample_context()

	with pytest.raises(ValueError, match="not implemented"):
		qlInterpolatedYieldCurve(
			dates,
			values,
			daycounter,
			calendar,
			"ZERORATE",
			"BACKWARDFLAT",
		)


def test_qlInterpolatedYieldCurve_MixedInterpolation_raises():
	dates = _sample_dates()
	values = [1.0, 0.99, 0.975, 0.95]
	daycounter, calendar = _sample_context()

	with pytest.raises(ValueError, match="Mixed interpolation not implemented"):
		qlInterpolatedYieldCurve(
			dates,
			values,
			daycounter,
			calendar,
			"LOGDISCOUNT",
			"LINEAR",
			mixed_interpolation_behavior="SPLICE",
		)


def test_qlDiscountCurve_constructor():
	dates = _sample_dates()
	discounts = [1.0, 0.99, 0.975, 0.95]
	daycounter, calendar = _sample_context()

	handle = qlDiscountCurve(dates, discounts, daycounter, calendar)

	assert isinstance(handle, ql.YieldTermStructureHandle)
	assert handle.currentLink() is not None


def test_qlForwardCurve_constructor():
	dates = _sample_dates()
	forwards = [0.01, 0.011, 0.012, 0.013]
	daycounter, calendar = _sample_context()

	handle = qlForwardCurve(dates, forwards, daycounter, calendar)

	assert isinstance(handle, ql.YieldTermStructureHandle)
	assert handle.currentLink() is not None


def test_qlZeroCurve_constructor():
	dates = _sample_dates()
	zerorates = [0.01, 0.0125, 0.015, 0.0175]
	daycounter, calendar = _sample_context()

	handle = qlZeroCurve(dates, zerorates, daycounter, calendar)

	assert isinstance(handle, ql.YieldTermStructureHandle)
	assert handle.currentLink() is not None
