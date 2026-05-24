import QuantLib as ql
import pytest

from quantlibxloil.rounding import _qRoundingMethod
from quantlibxloil.currencies import _qCurrency

from quantlibxloil import (
	qlCurrency,
	qlCurrencyCode,
	qlCurrencyFractionSymbol,
	qlCurrencyFractionsPerUnit,
	qlCurrencyName,
	qlCurrencyNumericalCode,
	qlCurrencyRounding,
	qlCurrencySymbol,
	qlCurrencyTriangulationCurrency,
	qlRounding,
)


def test__qCurrency_case_insensitive_and_passthrough():
	usd1 = _qCurrency("USD")
	usd2 = _qCurrency(" usd ")
	passthrough = _qCurrency(usd1)

	assert isinstance(usd1, ql.Currency)
	assert usd1.code() == "USD"
	assert usd2.code() == "USD"
	assert passthrough.code() == "USD"


def test__qCurrency_invalid_raises():
	with pytest.raises(ValueError, match="Unknown currency code"):
		_qCurrency("NOT_A_CCY")


def test_qlCurrency_constructor_and_accessors_with_builtin_currency():
	eur = _qCurrency("EUR")

	assert qlCurrencyCode(eur) == "EUR"
	assert isinstance(qlCurrencyName(eur), str)
	assert len(qlCurrencyName(eur)) > 0
	assert isinstance(qlCurrencyNumericalCode(eur), int)
	assert qlCurrencyNumericalCode(eur) > 0
	assert isinstance(qlCurrencySymbol(eur), str)
	assert isinstance(qlCurrencyFractionSymbol(eur), str)
	assert qlCurrencyFractionsPerUnit(eur) > 0
	assert isinstance(qlCurrencyRounding(eur), ql.Rounding)
	assert isinstance(qlCurrencyTriangulationCurrency(eur), ql.Currency)


def test_qlCurrency_create_custom_currency():
	rounding = qlRounding(_qRoundingMethod("CLOSEST"), 2)
	custom = qlCurrency(
		"Test Currency",
		"TST",
		999,
		"T$",
		"t",
		100,
		rounding,
	)

	assert isinstance(custom, ql.Currency)
	assert custom.code() == "TST"
	assert custom.numericCode() == 999
	assert custom.fractionsPerUnit() == 100
	assert isinstance(custom.rounding(), ql.Rounding)
