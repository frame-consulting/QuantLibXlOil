import QuantLib as ql
import pytest
import quantlib_xloil as qlx

from quantlib_xloil.calendars import _qBusinessDayConvention
from quantlib_xloil.currencies import _qCurrency

from quantlib_xloil import (
	qlCalendar,
	qlDate,
	qlDayCounter,
	qlEquityIndex,
	qlIborIndex,
	qlIndexAddFixing,
	qlIndexAddFixings,
	qlIndexClearFixings,
	qlIndexFixing,
	qlIndexFixingCalendar,
	qlIndexHasHistoricalFixing,
	qlIndexIsValidFixingDate,
	qlIndexManagerClearHistories,
	qlIndexManagerHistories,
	qlIndexName,
	qlIndexPastFixing,
	qlIndexTimeSeries,
	qlInterestRateIndexCurrency,
	qlInterestRateIndexDayCounter,
	qlInterestRateIndexFamilyName,
	qlInterestRateIndexFixingDate,
	qlInterestRateIndexFixingDays,
	qlInterestRateIndexMaturityDate,
	qlInterestRateIndexTenor,
	qlInterestRateIndexValueDate,
)


def _ibor_index() -> ql.IborIndex:
	return qlIborIndex(
		"TEST-IBOR",
		ql.Period("3M"),
		2,
		_qCurrency("USD"),
		qlCalendar("TARGET"),
		_qBusinessDayConvention("MODIFIEDFOLLOWING"),
		False,
		qlDayCounter("ACTUAL360"),
	)


def test_qlIndexManagerHistories_and_clear():
	# Keep manager state deterministic across tests.
	assert qlIndexManagerClearHistories() is True
	histories = qlIndexManagerHistories()
	assert histories is not None


def test_qlIndex_interface_fixings_and_timeseries():
	index = _ibor_index()
	value_date_1 = qlDate(2024, 1, 10)
	value_date_2 = qlDate(2024, 1, 11)
	fixing_date_1 = qlInterestRateIndexFixingDate(index, value_date_1)
	fixing_date_2 = qlInterestRateIndexFixingDate(index, value_date_2)

	assert isinstance(qlIndexName(index), str)
	assert isinstance(qlIndexFixingCalendar(index), ql.Calendar)
	assert isinstance(qlIndexIsValidFixingDate(index, fixing_date_1), bool)

	assert qlIndexAddFixing(index, fixing_date_1, 0.031) is True
	assert qlIndexHasHistoricalFixing(index, fixing_date_1) is True
	assert qlIndexFixing(index, fixing_date_1) == 0.031
	assert qlIndexPastFixing(index, fixing_date_1) == 0.031

	assert qlIndexAddFixings(index, [fixing_date_1, fixing_date_2], [0.031, 0.032], True) is True
	series = qlIndexTimeSeries(index)
	assert series is not None

	assert qlIndexClearFixings(index) is True


def test_qlInterestRateIndex_accessors_and_dates():
	index = _ibor_index()
	value_date = qlDate(2024, 1, 10)
	fixing_date = qlInterestRateIndexFixingDate(index, value_date)
	computed_value_date = qlInterestRateIndexValueDate(index, fixing_date)
	maturity_date = qlInterestRateIndexMaturityDate(index, computed_value_date)

	assert qlInterestRateIndexFamilyName(index) == "TEST-IBOR"
	assert qlInterestRateIndexTenor(index) == ql.Period("3M")
	assert qlInterestRateIndexFixingDays(index) == 2
	assert qlInterestRateIndexCurrency(index).code() == "USD"
	assert isinstance(qlInterestRateIndexDayCounter(index), ql.DayCounter)
	assert fixing_date <= computed_value_date
	assert maturity_date > computed_value_date


@pytest.mark.parametrize(
	"ctor_name",
	[
		"qlCdor",
		"qlBbsw",
		"qlBkbm",
		"qlEuribor",
		"qlEuribor365",
		"qlJibar",
		"qlMosprime",
		"qlNZDLibor",
		"qlPribor",
		"qlRobor",
		"qlShibor",
		"qlTibor",
		"qlTHBFIX",
		"qlWibor",
		"qlZibor",
		"qlAUDLibor",
		"qlCADLibor",
		"qlCHFLibor",
		"qlDKKLibor",
		"qlEURLibor",
		"qlGBPLibor",
		"qlJPYLibor",
		"qlSEKLibor",
		"qlTRLibor",
		"qlUSDLibor",
	],
)
def test_predefined_ibor_index_constructors(ctor_name):
	ctor = getattr(qlx, ctor_name)
	index = ctor(ql.Period("3M"))
	assert isinstance(index, ql.IborIndex)


@pytest.mark.parametrize(
	"ctor_name",
	[
		"qlAonia",
		"qlCdi",
		"qlCorra",
		"qlDestr",
		"qlEonia",
		"qlEstr",
		"qlFedFunds",
		"qlKofr",
		"qlNzocr",
		"qlSaron",
		"qlSofr",
		"qlSonia",
		"qlSwestr",
		"qlTonar",
	],
)
def test_predefined_overnight_index_constructors(ctor_name):
	ctor = getattr(qlx, ctor_name)
	index = ctor()
	assert isinstance(index, ql.OvernightIndex)


@pytest.mark.parametrize(
	"ctor_name",
	[
		"qlEuriborSwapIsdaFixA",
		"qlEuriborSwapIsdaFixB",
		"qlEuriborSwapIfrFix",
		"qlEurLiborSwapIsdaFixA",
		"qlEurLiborSwapIsdaFixB",
		"qlEurLiborSwapIfrFix",
		"qlChfLiborSwapIsdaFix",
		"qlGbpLiborSwapIsdaFix",
		"qlJpyLiborSwapIsdaFixAm",
		"qlJpyLiborSwapIsdaFixPm",
		"qlUsdLiborSwapIsdaFixAm",
		"qlUsdLiborSwapIsdaFixPm",
	],
)
def test_predefined_swap_index_constructors(ctor_name):
	ctor = getattr(qlx, ctor_name)
	index = ctor(ql.Period("5Y"))
	assert isinstance(index, ql.SwapIndex)


def test_qlEquityIndex_constructor():
	index = qlEquityIndex(
		"TEST-EQUITY",
		qlCalendar("TARGET"),
		_qCurrency("USD"),
		100.0,
	)

	assert isinstance(index, ql.EquityIndex)
	assert qlIndexName(index) == "TEST-EQUITY"
	assert isinstance(qlIndexFixingCalendar(index), ql.Calendar)
	assert index.currency().code() == "USD"
