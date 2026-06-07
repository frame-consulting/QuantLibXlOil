import QuantLib as ql
import pytest

from quantlib_xloil.calibrationhelpers import _qBlackCalibrationHelperErrorType
from quantlib_xloil.date import _qFrequency
from quantlib_xloil import (
	qlBlackCalibrationHelperBlackPrice,
	qlBlackCalibrationHelperCalibrationError,
	qlBlackCalibrationHelperImpliedVolatility,
	qlBlackCalibrationHelperMarketValue,
	qlBlackCalibrationHelperModelValue,
	qlBlackCalibrationHelperSetPricingEngine,
	qlBlackCalibrationHelperVolatility,
	qlBlackCalibrationHelperVolatilityType,
	qlCalendar,
	qlCapHelper,
	qlDayCounter,
	qlHestonModelHelper,
	qlSwaptionHelper,
	qlUSDLibor,
)


def _market_setup() -> tuple[ql.YieldTermStructureHandle, ql.IborIndex, ql.QuoteHandle]:
	reference_date = ql.Date(2, 1, 2024)
	curve = ql.YieldTermStructureHandle(ql.FlatForward(reference_date, 0.02, ql.Actual365Fixed()))
	index = qlUSDLibor(ql.Period("3M"), curve)
	volatility = ql.QuoteHandle(ql.SimpleQuote(0.20))
	return curve, index, volatility


def test_qBlackCalibrationHelperErrorType_converter():
	assert _qBlackCalibrationHelperErrorType("relativeprice") == ql.BlackCalibrationHelper.RelativePriceError
	assert _qBlackCalibrationHelperErrorType("PRICE") == ql.BlackCalibrationHelper.PriceError
	assert _qBlackCalibrationHelperErrorType("impliedvol") == ql.BlackCalibrationHelper.ImpliedVolError

	with pytest.raises(ValueError, match="Cannot convert"):
		_qBlackCalibrationHelperErrorType("invalid")


def test_qlSwaptionHelper_accepts_period_and_date_inputs():
	original_eval = ql.Settings.instance().evaluationDate
	try:
		ql.Settings.instance().evaluationDate = ql.Date(2, 1, 2024)
		curve, index, volatility = _market_setup()

		helper_period = qlSwaptionHelper(
			"1Y",
			"5Y",
			volatility,
			index,
			ql.Period("1Y"),
			qlDayCounter("ACTUAL365FIXED"),
			qlDayCounter("ACTUAL365FIXED"),
			curve,
		)

		helper_dates = qlSwaptionHelper(
			ql.Date(2, 1, 2025).serialNumber(),
			ql.Date(2, 1, 2030).serialNumber(),
			volatility,
			index,
			ql.Period("1Y"),
			qlDayCounter("ACTUAL365FIXED"),
			qlDayCounter("ACTUAL365FIXED"),
			curve,
		)

		assert isinstance(helper_period, ql.SwaptionHelper)
		assert isinstance(helper_dates, ql.SwaptionHelper)
		assert qlBlackCalibrationHelperMarketValue(helper_period) > 0.0
		assert qlBlackCalibrationHelperMarketValue(helper_dates) > 0.0
	finally:
		ql.Settings.instance().evaluationDate = original_eval


def test_qlCapHelper_black_calibration_interface_and_engine_dependent_values():
	original_eval = ql.Settings.instance().evaluationDate
	try:
		ql.Settings.instance().evaluationDate = ql.Date(2, 1, 2024)
		curve, index, volatility = _market_setup()

		helper = qlCapHelper(
			ql.Period("5Y"),
			volatility,
			index,
			_qFrequency("ANNUAL"),
			qlDayCounter("ACTUAL365FIXED"),
			False,
			curve,
		)

		market_value = qlBlackCalibrationHelperMarketValue(helper)
		assert isinstance(helper, ql.CapHelper)
		assert qlBlackCalibrationHelperVolatilityType(helper) == "SHIFTEDLOGNORMAL"
		assert isinstance(qlBlackCalibrationHelperVolatility(helper), ql.QuoteHandle)
		assert qlBlackCalibrationHelperVolatility(helper).value() == pytest.approx(0.20)
		assert market_value > 0.0
		assert qlBlackCalibrationHelperBlackPrice(helper, 0.20) == pytest.approx(market_value)
		assert qlBlackCalibrationHelperImpliedVolatility(helper, market_value) == pytest.approx(0.20)

		with pytest.raises(RuntimeError, match="null pricing engine"):
			qlBlackCalibrationHelperModelValue(helper)

		engine = ql.BlackCapFloorEngine(curve, volatility)
		qlBlackCalibrationHelperSetPricingEngine(helper, engine)

		assert qlBlackCalibrationHelperModelValue(helper) == pytest.approx(market_value)
		assert qlBlackCalibrationHelperCalibrationError(helper) == pytest.approx(0.0)
	finally:
		ql.Settings.instance().evaluationDate = original_eval


def test_qlHestonModelHelper_constructor_and_black_interface():
	original_eval = ql.Settings.instance().evaluationDate
	try:
		ql.Settings.instance().evaluationDate = ql.Date(2, 1, 2024)
		curve, _, volatility = _market_setup()

		helper = qlHestonModelHelper(
			ql.Period("1Y"),
			qlCalendar("NULLCALENDAR"),
			100.0,
			100.0,
			volatility,
			curve,
			curve,
		)

		market_value = qlBlackCalibrationHelperMarketValue(helper)
		assert isinstance(helper, ql.HestonModelHelper)
		assert qlBlackCalibrationHelperVolatilityType(helper) == "SHIFTEDLOGNORMAL"
		assert qlBlackCalibrationHelperBlackPrice(helper, 0.20) == pytest.approx(market_value)
		assert qlBlackCalibrationHelperImpliedVolatility(helper, market_value) == pytest.approx(0.20)

		with pytest.raises(RuntimeError, match="null pricing engine"):
			qlBlackCalibrationHelperModelValue(helper)
	finally:
		ql.Settings.instance().evaluationDate = original_eval
