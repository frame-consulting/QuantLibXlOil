import QuantLib as ql
import pytest

from quantlib_xloil.currencies import qCurrency
from quantlib_xloil.money import (
    qMoneyConversionType,
    qlMoney,
    qlMoneyAdd,
    qlMoneyCurrency,
    qlMoneyDivide,
    qlMoneyEqual,
    qlMoneyGreaterThan,
    qlMoneyGreaterThanOrEqual,
    qlMoneyLessThan,
    qlMoneyLessThanOrEqual,
    qlMoneyMultiply,
    qlMoneyNegate,
    qlMoneyNotEqual,
    qlMoneyRatio,
    qlMoneyRounded,
    qlMoneySetBaseCurrency,
    qlMoneySetConversionType,
    qlMoneySubtract,
    qlMoneyToString,
    qlMoneyValue,
)


def test_qlMoney_constructor_and_accessors():
    usd = qCurrency.__wrapped__("USD")
    money = qlMoney(usd, 123.456)

    assert isinstance(money, ql.Money)
    assert qlMoneyCurrency(money).code() == "USD"
    assert qlMoneyValue(money) == pytest.approx(123.456)
    rounded = qlMoneyRounded(money)
    assert isinstance(rounded, ql.Money)
    assert rounded.value() == pytest.approx(123.456)


def test_qlMoney_arithmetic():
    usd = qCurrency.__wrapped__("USD")
    money1 = qlMoney(usd, 100)
    money2 = qlMoney(usd, 40)

    assert qlMoneyAdd(money1, money2).value() == pytest.approx(140)
    assert qlMoneySubtract(money1, money2).value() == pytest.approx(60)
    assert qlMoneyMultiply(money1, 2).value() == pytest.approx(200)
    assert qlMoneyDivide(money1, 2).value() == pytest.approx(50)
    assert qlMoneyRatio(money1, money2) == pytest.approx(2.5)
    assert qlMoneyNegate(money1).value() == pytest.approx(-100)


def test_qlMoney_comparisons():
    usd = qCurrency.__wrapped__("USD")
    money1 = qlMoney(usd, 100)
    money2 = qlMoney(usd, 40)
    equal_money = qlMoney(usd, 100)

    assert qlMoneyEqual(money1, equal_money)
    assert qlMoneyNotEqual(money1, money2)
    assert qlMoneyLessThan(money2, money1)
    assert qlMoneyLessThanOrEqual(money1, equal_money)
    assert qlMoneyGreaterThan(money1, money2)
    assert qlMoneyGreaterThanOrEqual(money1, equal_money)


def test_qlMoneyToString():
    usd = qCurrency.__wrapped__("USD")
    assert qlMoneyToString(qlMoney(usd, 100)) == "100 USD"


def test_qlMoney_settings():
    usd = qCurrency.__wrapped__("USD")
    conversion_type = qMoneyConversionType.__wrapped__("NO_CONVERSION")

    assert qlMoneySetConversionType(conversion_type)
    assert qlMoneySetBaseCurrency(usd)
