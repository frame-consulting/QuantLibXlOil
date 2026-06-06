import QuantLib as ql
import pytest

from quantlib_xloil import (
	qlDate,
	qlDividendVector,
	qlFixedDividend,
	qlFractionalDividend,
)


def test_qlFixedDividend_constructor_and_accessors():
	payment_date = qlDate(2025, 1, 15)
	dividend = qlFixedDividend(1.25, payment_date)

	assert isinstance(dividend, ql.FixedDividend)
	assert dividend.date() == payment_date
	assert dividend.amount() == pytest.approx(1.25)


def test_qlFractionalDividend_constructor_and_amount_requires_nominal():
	payment_date = qlDate(2025, 1, 15)
	dividend = qlFractionalDividend(0.02, payment_date)

	assert isinstance(dividend, ql.FractionalDividend)
	assert dividend.date() == payment_date
	with pytest.raises(RuntimeError, match="no nominal given"):
		dividend.amount()


def test_qlDividendVector_from_quantlib_dates_and_amounts():
	dates = [qlDate(2025, 1, 15), qlDate(2025, 7, 15)]
	amounts = [1.0, 2.5]

	dividend_vector = qlDividendVector(dates, amounts)

	assert isinstance(dividend_vector, tuple)
	assert len(dividend_vector) == 2
	assert dividend_vector[0].date() == dates[0]
	assert dividend_vector[0].amount() == pytest.approx(1.0)
	assert dividend_vector[1].date() == dates[1]
	assert dividend_vector[1].amount() == pytest.approx(2.5)


def test_qlDividendVector_converts_excel_serial_dates_and_numeric_amounts():
	base_date_1 = qlDate(2025, 1, 15)
	base_date_2 = qlDate(2025, 7, 15)
	serial_dates = [base_date_1.serialNumber() + 0.4, base_date_2.serialNumber() + 0.6]
	amounts = ["1.0", 2]

	dividend_vector = qlDividendVector(serial_dates, amounts)

	assert len(dividend_vector) == 2
	assert dividend_vector[0].date() == ql.Date(round(serial_dates[0]))
	assert dividend_vector[1].date() == ql.Date(round(serial_dates[1]))
	assert dividend_vector[0].amount() == pytest.approx(1.0)
	assert dividend_vector[1].amount() == pytest.approx(2.0)


def test_qlDividendVector_size_mismatch_raises():
	dates = [qlDate(2025, 1, 15)]
	amounts = [1.0, 2.0]

	with pytest.raises(RuntimeError, match="size mismatch"):
		qlDividendVector(dates, amounts)
