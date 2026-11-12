import QuantLib as ql
import pytest

from quantlib_xloil.currencies import qCurrency
from quantlib_xloil.exchangerates import (
    qExchangeRateType,
    qlExchangeRate,
    qlExchangeRateChain,
    qlExchangeRateExchange,
    qlExchangeRateManagerAdd,
    qlExchangeRateManagerAdd2,
    qlExchangeRateManagerClear,
    qlExchangeRateManagerInstance,
    qlExchangeRateManagerLookup,
    qlExchangeRateSource,
    qlExchangeRateTarget,
    qlExchangeRateType,
    qlExchangeRateValue,
)


def test_qlExchangeRate_constructor():
    usd = qCurrency.__wrapped__("USD")
    eur = qCurrency.__wrapped__("EUR")

    rate = qlExchangeRate(usd, eur, 0.92)

    assert isinstance(rate, ql.ExchangeRate)
    assert qlExchangeRateValue(rate) == 0.92


def test_qlExchangeRateSource():
    usd = qCurrency.__wrapped__("USD")
    eur = qCurrency.__wrapped__("EUR")

    rate = qlExchangeRate(usd, eur, 0.92)
    source = qlExchangeRateSource(rate)

    assert isinstance(source, ql.Currency)
    assert source.code() == "USD"


def test_qlExchangeRateTarget():
    usd = qCurrency.__wrapped__("USD")
    eur = qCurrency.__wrapped__("EUR")

    rate = qlExchangeRate(usd, eur, 0.92)
    target = qlExchangeRateTarget(rate)

    assert isinstance(target, ql.Currency)
    assert target.code() == "EUR"


def test_qlExchangeRateType_Direct():
    usd = qCurrency.__wrapped__("USD")
    eur = qCurrency.__wrapped__("EUR")

    rate = qlExchangeRate(usd, eur, 0.92)
    rate_type = qlExchangeRateType(rate)

    assert rate_type == "DIRECT"


def test_qExchangeRateType_converter():
    assert qExchangeRateType.__wrapped__("direct") == ql.ExchangeRate.Direct
    assert (
        qExchangeRateType.__wrapped__(ql.ExchangeRate.Derived)
        == ql.ExchangeRate.Derived
    )


def test_qlExchangeRateValue():
    usd = qCurrency.__wrapped__("USD")
    eur = qCurrency.__wrapped__("EUR")

    rate = qlExchangeRate(usd, eur, 0.92)
    value = qlExchangeRateValue(rate)

    assert value == 0.92


def test_qlExchangeRateExchange():
    usd = qCurrency.__wrapped__("USD")
    eur = qCurrency.__wrapped__("EUR")

    rate = qlExchangeRate(usd, eur, 0.92)
    money = ql.Money(100, usd)
    converted = qlExchangeRateExchange(rate, money)

    assert isinstance(converted, ql.Money)
    assert converted.currency().code() == "EUR"
    assert abs(converted.value() - 92.0) < 1e-10


def test_qlExchangeRateChain():
    usd = qCurrency.__wrapped__("USD")
    eur = qCurrency.__wrapped__("EUR")
    gbp = qCurrency.__wrapped__("GBP")

    rate1 = qlExchangeRate(usd, eur, 0.92)
    rate2 = qlExchangeRate(eur, gbp, 0.86)
    chained = qlExchangeRateChain(rate1, rate2)

    assert isinstance(chained, ql.ExchangeRate)
    assert chained.source().code() == "USD"
    assert chained.target().code() == "GBP"
    assert abs(chained.rate() - (0.92 * 0.86)) < 1e-10


def test_qlExchangeRateManagerInstance():
    manager = qlExchangeRateManagerInstance()

    assert isinstance(manager, ql.ExchangeRateManager)


def test_qlExchangeRateManagerAdd_and_Lookup():
    # Clear the manager first to ensure clean state
    qlExchangeRateManagerClear()

    usd = qCurrency.__wrapped__("USD")
    eur = qCurrency.__wrapped__("EUR")
    date = ql.Date(15, ql.December, 2023)

    rate = qlExchangeRate(usd, eur, 0.92)
    qlExchangeRateManagerAdd(rate, date, date)

    # Lookup the rate
    looked_up = qlExchangeRateManagerLookup(
        usd, eur, date, qExchangeRateType.__wrapped__("DIRECT")
    )

    assert isinstance(looked_up, ql.ExchangeRate)
    assert looked_up.source().code() == "USD"
    assert looked_up.target().code() == "EUR"
    assert abs(looked_up.rate() - 0.92) < 1e-10

    qlExchangeRateManagerClear()


def test_qlExchangeRateManagerAdd_with_default_dates():
    # Clear the manager first
    qlExchangeRateManagerClear()

    usd = qCurrency.__wrapped__("USD")
    gbp = qCurrency.__wrapped__("GBP")
    date = ql.Date(15, ql.December, 2023)

    rate = qlExchangeRate(usd, gbp, 0.79)
    qlExchangeRateManagerAdd(rate)

    # Lookup should work
    looked_up = qlExchangeRateManagerLookup(
        usd, gbp, date, qExchangeRateType.__wrapped__("DIRECT")
    )

    assert isinstance(looked_up, ql.ExchangeRate)
    assert abs(looked_up.rate() - 0.79) < 1e-10

    qlExchangeRateManagerClear()


def test_qlExchangeRateManagerAdd2():
    qlExchangeRateManagerClear()

    date = ql.Date(15, ql.December, 2023)
    assert qlExchangeRateManagerAdd2("USDEUR", 0.92, date, date)

    looked_up = qlExchangeRateManagerLookup(
        qCurrency.__wrapped__("USD"),
        qCurrency.__wrapped__("EUR"),
        date,
        qExchangeRateType.__wrapped__("DIRECT"),
    )

    assert looked_up.source().code() == "USD"
    assert looked_up.target().code() == "EUR"
    assert looked_up.rate() == pytest.approx(0.92)

    qlExchangeRateManagerClear()


def test_qlExchangeRateManagerLookup_with_derived_type():
    # Clear the manager first
    qlExchangeRateManagerClear()

    usd = qCurrency.__wrapped__("USD")
    eur = qCurrency.__wrapped__("EUR")
    jpy = qCurrency.__wrapped__("JPY")
    date = ql.Date(15, ql.December, 2023)

    rate1 = qlExchangeRate(usd, eur, 0.92)
    rate2 = qlExchangeRate(usd, jpy, 110.0)
    qlExchangeRateManagerAdd(rate1, date, date)
    qlExchangeRateManagerAdd(rate2, date, date)

    # Lookup derived rate from EUR to JPY
    looked_up = qlExchangeRateManagerLookup(
        eur, jpy, date, qExchangeRateType.__wrapped__("DERIVED")
    )

    assert isinstance(looked_up, ql.ExchangeRate)
    assert looked_up.source().code() == "EUR"
    assert looked_up.target().code() == "JPY"

    qlExchangeRateManagerClear()


def test_qlExchangeRateManagerClear():
    # Add a rate
    usd = qCurrency.__wrapped__("USD")
    eur = qCurrency.__wrapped__("EUR")
    date = ql.Date(15, ql.December, 2023)

    rate = qlExchangeRate(usd, eur, 0.92)
    qlExchangeRateManagerAdd(rate, date, date)

    # Clear should not raise
    qlExchangeRateManagerClear()

    # Lookup should fail after clear (unless rate is in cache or some other persistence)
    # This is expected behavior after clearing
