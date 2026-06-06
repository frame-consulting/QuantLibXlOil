import QuantLib as ql
import pytest

from quantlib_xloil import (
	qlCompositeInstrument,
	qlInstrumentErrorEstimate,
	qlInstrumentIsExpired,
	qlInstrumentNPV,
	qlStock,
)
from quantlib_xloil.ratehelpers import qQuoteHandle


def test_qlStock_constructor_and_instrument_accessors():
	quote = qQuoteHandle.__wrapped__(123.45)
	stock = qlStock(quote)

	assert isinstance(stock, ql.Stock)
	assert qlInstrumentNPV(stock) == pytest.approx(123.45)
	assert qlInstrumentIsExpired(stock) is False
	with pytest.raises(RuntimeError, match="error estimate not provided"):
		qlInstrumentErrorEstimate(stock)


def test_qlCompositeInstrument_default_multipliers_are_one():
	stock1 = qlStock(qQuoteHandle.__wrapped__(100.0))
	stock2 = qlStock(qQuoteHandle.__wrapped__(50.0))

	composite = qlCompositeInstrument([stock1, stock2])

	assert isinstance(composite, ql.CompositeInstrument)
	assert qlInstrumentNPV(composite) == pytest.approx(150.0)
	assert qlInstrumentIsExpired(composite) is False


def test_qlCompositeInstrument_scalar_multiplier_broadcasts():
	stock1 = qlStock(qQuoteHandle.__wrapped__(100.0))
	stock2 = qlStock(qQuoteHandle.__wrapped__(50.0))

	composite = qlCompositeInstrument([stock1, stock2], [2.0])

	assert qlInstrumentNPV(composite) == pytest.approx(300.0)


def test_qlCompositeInstrument_explicit_multipliers():
	stock1 = qlStock(qQuoteHandle.__wrapped__(123.45))
	stock2 = qlStock(qQuoteHandle.__wrapped__(100.0))

	composite = qlCompositeInstrument([stock1, stock2], [2.0, -0.5])

	assert qlInstrumentNPV(composite) == pytest.approx(196.9)
	with pytest.raises(RuntimeError, match="error estimate not provided"):
		qlInstrumentErrorEstimate(composite)


def test_qlCompositeInstrument_invalid_multiplier_length_raises():
	stock1 = qlStock(qQuoteHandle.__wrapped__(100.0))
	stock2 = qlStock(qQuoteHandle.__wrapped__(50.0))

	with pytest.raises(ValueError, match="Length of multipliers"):
		qlCompositeInstrument([stock1, stock2], [1.0, 2.0, 3.0])
