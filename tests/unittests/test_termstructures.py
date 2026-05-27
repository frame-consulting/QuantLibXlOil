import QuantLib as ql
import pytest

from quantlib_xloil.date import _qFrequency
from quantlib_xloil.termstructures import _qCompounding

from quantlib_xloil import (
	qlCalendar,
	qlDate,
	qlDayCounter,
	qlFlatForward,
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
	qlYieldTermStructureDiscount,
	qlYieldTermStructureDiscountFromTime,
	qlYieldTermStructureForwardRate,
	qlYieldTermStructureForwardRateFromTime,
	qlYieldTermStructureZeroRate,
	qlYieldTermStructureZeroRateFromTime,
	qlZeroSpreadedTermStructure,
)


def _base_curve():
	reference_date = qlDate(2024, 1, 2)
	daycounter = qlDayCounter("ACTUAL365FIXED")
	calendar = qlCalendar("TARGET")
	return qlFlatForward(reference_date, 0.05, daycounter, _qCompounding("COMPOUNDED"), _qFrequency("ANNUAL"), calendar)


def _future_date(year: int, month: int, day: int):
	return qlDate(year, month, day)


def test_qCompounding_case_insensitive():
	assert _qCompounding("simple") == ql.Simple
	assert _qCompounding("Compounded") == ql.Compounded
	assert _qCompounding("CONTINUOUS") == ql.Continuous


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
	zero_rate = qlYieldTermStructureZeroRate(handle, date1, daycounter, _qCompounding("COMPOUNDED"), _qFrequency("ANNUAL"))
	zero_rate_time = qlYieldTermStructureZeroRateFromTime(handle, 0.5, _qCompounding("CONTINUOUS"), _qFrequency("NOFREQUENCY"))
	forward_rate = qlYieldTermStructureForwardRate(handle, date1, date2, daycounter, _qCompounding("COMPOUNDED"), _qFrequency("ANNUAL"))
	forward_rate_time = qlYieldTermStructureForwardRateFromTime(handle, 0.5, 1.0, _qCompounding("CONTINUOUS"), _qFrequency("NOFREQUENCY"))

	assert 0.0 < discount_by_date < 1.0
	assert 0.0 < discount_by_time < 1.0
	assert zero_rate > 0.0
	assert zero_rate_time > 0.0
	assert forward_rate > 0.0
	assert forward_rate_time > 0.0


def test_qlFlatForward_and_implied_and_spreaded_term_structures():
	base = _base_curve()
	spreaded_zero = qlZeroSpreadedTermStructure(base, 0.001, _qCompounding("COMPOUNDED"), _qFrequency("ANNUAL"), qlDayCounter("ACTUAL365FIXED"))
	spreaded_forward = qlForwardSpreadedTermStructure(base, 0.001)
	implied = qlImpliedTermStructure(base, qlDate(2024, 7, 2))

	assert isinstance(spreaded_zero, ql.YieldTermStructureHandle)
	assert isinstance(spreaded_forward, ql.YieldTermStructureHandle)
	assert isinstance(implied, ql.YieldTermStructureHandle)
	assert spreaded_zero.currentLink() is not None
	assert spreaded_forward.currentLink() is not None
	assert implied.currentLink() is not None


def test_qlCompositeZeroYieldStructure_valid_and_invalid_operator():
	curve1 = _base_curve()
	curve2 = qlFlatForward(qlDate(2024, 1, 2), 0.01, qlDayCounter("ACTUAL365FIXED"), _qCompounding("COMPOUNDED"), _qFrequency("ANNUAL"), qlCalendar("TARGET"))

	combined_add = qlCompositeZeroYieldStructure(curve1, curve2, "+")
	combined_sub = qlCompositeZeroYieldStructure(curve1, curve2, "-")

	assert isinstance(combined_add, ql.YieldTermStructureHandle)
	assert isinstance(combined_sub, ql.YieldTermStructureHandle)
	assert combined_add.currentLink() is not None
	assert combined_sub.currentLink() is not None

	with pytest.raises(ValueError, match="Invalid operator"):
		qlCompositeZeroYieldStructure(curve1, curve2, "*")
