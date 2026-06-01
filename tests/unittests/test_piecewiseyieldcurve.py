import numpy as np
import QuantLib as ql
import pytest

from quantlib_xloil import (
	qlCalendar,
	qlDate,
	qlDayCounter,
	qlDepositRateHelper,
	qlFlatForward,
	qlPiecewiseSpreadYieldCurve,
	qlPiecewiseSpreadYieldCurveAsYts,
	qlPiecewiseYieldCurve,
	qlPiecewiseYieldCurveAsYts,
	qlPiecewiseYieldCurveData,
	qlPiecewiseYieldCurveDates,
	qlPiecewiseYieldCurveTimes,
	qlPiecewiseYieldCurveWithJumps,
	qlPiecewiseYieldCurveWithJumpsAsYts,
	qlYieldTermStructureHandle,
)
from quantlib_xloil.calendars import _qBusinessDayConvention
from quantlib_xloil.date import _qFrequency
from quantlib_xloil.piecewiseyieldcurve import _to_ql_rate_helpers
from quantlib_xloil.termstructures import _qCompounding


def _set_eval_date() -> None:
	ql.Settings.instance().evaluationDate = qlDate(2024, 1, 2)


def _sample_rate_helpers() -> list[ql.RateHelper]:
	calendar = qlCalendar("TARGET")
	business_day_convention = _qBusinessDayConvention("MODIFIEDFOLLOWING")
	daycounter = qlDayCounter("ACTUAL360")
	return [
		qlDepositRateHelper(0.05, ql.Period("3M"), 2, calendar, business_day_convention, False, daycounter),
		qlDepositRateHelper(0.052, ql.Period("6M"), 2, calendar, business_day_convention, False, daycounter),
	]


def _base_curve_handle() -> ql.YieldTermStructureHandle:
	return qlFlatForward(
		qlDate(2024, 1, 2),
		0.02,
		qlDayCounter("ACTUAL365FIXED"),
		_qCompounding("COMPOUNDED"),
		_qFrequency("ANNUAL"),
		qlCalendar("TARGET"),
	)


def test_to_ql_rate_helpers_variants():
	_set_eval_date()
	helpers = _sample_rate_helpers()
	helper = helpers[0]

	assert _to_ql_rate_helpers(None) == ()
	assert _to_ql_rate_helpers(helper) == (helper,)
	assert _to_ql_rate_helpers(helpers) == tuple(helpers)
	assert _to_ql_rate_helpers(tuple(helpers)) == tuple(helpers)

	helpers_array = np.array(helpers, dtype=object).reshape(1, -1)
	assert _to_ql_rate_helpers(helpers_array) == tuple(helpers)

	with pytest.raises(ValueError, match="Cannot convert"):
		_to_ql_rate_helpers("not-a-rate-helper")


def test_qlPiecewiseYieldCurve_happy_path_and_accessors():
	_set_eval_date()
	reference_date = qlDate(2024, 1, 2)
	helpers = _sample_rate_helpers()
	daycounter = qlDayCounter("ACTUAL365FIXED")

	yts = qlPiecewiseYieldCurveAsYts(
		reference_date,
		helpers,
		daycounter,
		"  logdiscount  ",
		" linear ",
	)
	handle = qlPiecewiseYieldCurve(reference_date, helpers, daycounter, "LOGDISCOUNT", "LINEAR")
	converted_handle = qlYieldTermStructureHandle(yts)

	assert isinstance(yts, ql.YieldTermStructure)
	assert isinstance(handle, ql.YieldTermStructureHandle)
	assert isinstance(converted_handle, ql.YieldTermStructureHandle)
	assert handle.currentLink() is not None
	assert converted_handle.currentLink() is not None

	serial_dates = qlPiecewiseYieldCurveDates(yts)
	times = qlPiecewiseYieldCurveTimes(yts)
	data = qlPiecewiseYieldCurveData(yts)

	assert len(serial_dates) >= 2
	assert len(times) == len(serial_dates)
	assert len(data) == len(serial_dates)
	assert all(t2 >= t1 for t1, t2 in zip(times, times[1:]))
	assert yts.discount(qlDate(2024, 7, 2)) > 0.0


def test_qlPiecewiseYieldCurve_validation_errors():
	_set_eval_date()
	reference_date = qlDate(2024, 1, 2)
	helpers = _sample_rate_helpers()
	daycounter = qlDayCounter("ACTUAL365FIXED")

	with pytest.raises(ValueError, match="Invalid traits"):
		qlPiecewiseYieldCurveAsYts(reference_date, helpers, daycounter, "BADTRAIT", "LINEAR")

	with pytest.raises(ValueError, match="Invalid interpolator"):
		qlPiecewiseYieldCurveAsYts(reference_date, helpers, daycounter, "LOGDISCOUNT", "BADINTERP")

	with pytest.raises(ValueError, match="not implemented"):
		qlPiecewiseYieldCurveAsYts(reference_date, helpers, daycounter, "ZERORATE", "BACKWARDFLAT")

	with pytest.raises(ValueError, match="Mixed interpolation not implemented"):
		qlPiecewiseYieldCurveAsYts(
			reference_date,
			helpers,
			daycounter,
			"LOGDISCOUNT",
			"LINEAR",
			mixed_interpolation_behavior="SPLICE",
		)


def test_qlPiecewiseYieldCurveWithJumps_happy_path():
	_set_eval_date()
	reference_date = qlDate(2024, 1, 2)
	helpers = _sample_rate_helpers()
	daycounter = qlDayCounter("ACTUAL365FIXED")

	yts = qlPiecewiseYieldCurveWithJumpsAsYts(
		reference_date,
		helpers,
		daycounter,
		[0.999],
		[qlDate(2024, 3, 29)],
		"LOGDISCOUNT",
		"LINEAR",
	)
	handle = qlPiecewiseYieldCurveWithJumps(
		reference_date,
		helpers,
		daycounter,
		[0.999],
		[qlDate(2024, 3, 29)],
		"LOGDISCOUNT",
		"LINEAR",
	)

	assert isinstance(yts, ql.YieldTermStructure)
	assert isinstance(handle, ql.YieldTermStructureHandle)
	assert handle.currentLink() is not None
	assert yts.discount(qlDate(2024, 7, 2)) > 0.0


def test_qlPiecewiseYieldCurveWithJumps_mixed_interpolation_raises():
	_set_eval_date()
	reference_date = qlDate(2024, 1, 2)
	helpers = _sample_rate_helpers()
	daycounter = qlDayCounter("ACTUAL365FIXED")

	with pytest.raises(ValueError, match="Mixed interpolation not implemented"):
		qlPiecewiseYieldCurveWithJumpsAsYts(
			reference_date,
			helpers,
			daycounter,
			[0.999],
			[qlDate(2024, 3, 29)],
			"LOGDISCOUNT",
			"LINEAR",
			mixed_interpolation_n=1,
		)


def test_qlPiecewiseSpreadYieldCurve_happy_path():
	_set_eval_date()
	base_curve = _base_curve_handle()
	helpers = _sample_rate_helpers()

	yts = qlPiecewiseSpreadYieldCurveAsYts(base_curve, helpers, "  logdiscount ", " linear ")
	handle = qlPiecewiseSpreadYieldCurve(base_curve, helpers, "LOGDISCOUNT", "LINEAR")

	assert isinstance(yts, ql.YieldTermStructure)
	assert isinstance(handle, ql.YieldTermStructureHandle)
	assert handle.currentLink() is not None
	assert yts.discount(qlDate(2024, 7, 2)) > 0.0
	assert handle.discount(qlDate(2024, 7, 2)) > 0.0


def test_qlPiecewiseSpreadYieldCurve_validation_errors():
	base_curve = _base_curve_handle()

	with pytest.raises(ValueError, match="Invalid traits"):
		qlPiecewiseSpreadYieldCurveAsYts(base_curve, [], "BADTRAIT", "LINEAR")

	with pytest.raises(ValueError, match="Invalid interpolator"):
		qlPiecewiseSpreadYieldCurveAsYts(base_curve, [], "LOGDISCOUNT", "BADINTERP")

	with pytest.raises(ValueError, match="not implemented"):
		qlPiecewiseSpreadYieldCurveAsYts(base_curve, [], "ZERORATE", "LINEAR")

	with pytest.raises(ValueError, match="Mixed interpolation not implemented"):
		qlPiecewiseSpreadYieldCurveAsYts(
			base_curve,
			[],
			"LOGDISCOUNT",
			"LINEAR",
			mixed_interpolation_behavior="SPLICE",
		)
