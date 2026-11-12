import QuantLib as ql
import re
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .currencies import qCurrency
from .date import qDate
from .utilities import enum_value, first_key, UNKNOWN_VALUE

QL_EXCHANGE_RATE_TYPE = {
    "DIRECT": ql.ExchangeRate.Direct,
    "DERIVED": ql.ExchangeRate.Derived,
}


def _qExchangeRateType(s: str) -> int:
    return enum_value(s, QL_EXCHANGE_RATE_TYPE)


@xlo.converter()
def qExchangeRateType(s: str) -> int:
    return _qExchangeRateType(s)


@xlo.func(
    help="Create a QuantLib ExchangeRate object.",
    args={
        "source": "The source Currency.",
        "target": "The target Currency.",
        "rate": "The exchange rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExchangeRate(
    source: qCurrency,
    target: qCurrency,
    rate: float,
    trigger=None,
) -> ql.ExchangeRate:
    return ql.ExchangeRate(source, target, rate)


@xlo.func(
    help="Get the source currency of an ExchangeRate.",
    args={
        "exchange_rate": "The ExchangeRate object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExchangeRateSource(
    exchange_rate: ql.ExchangeRate,
    trigger=None,
) -> ql.Currency:
    return exchange_rate.source()


@xlo.func(
    help="Get the target currency of an ExchangeRate.",
    args={
        "exchange_rate": "The ExchangeRate object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExchangeRateTarget(
    exchange_rate: ql.ExchangeRate,
    trigger=None,
) -> ql.Currency:
    return exchange_rate.target()


@xlo.func(
    help="Get the type of an ExchangeRate (Direct or Derived).",
    args={
        "exchange_rate": "The ExchangeRate object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExchangeRateType(
    exchange_rate: ql.ExchangeRate,
    trigger=None,
) -> qExchangeRateType:
    return first_key(QL_EXCHANGE_RATE_TYPE, exchange_rate.type(), UNKNOWN_VALUE)


@xlo.func(
    help="Get the rate of an ExchangeRate.",
    args={
        "exchange_rate": "The ExchangeRate object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExchangeRateValue(
    exchange_rate: ql.ExchangeRate,
    trigger=None,
) -> float:
    return exchange_rate.rate()


@xlo.func(
    help="Exchange money using an ExchangeRate.",
    args={
        "exchange_rate": "The ExchangeRate object.",
        "money": "The Money object to exchange.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExchangeRateExchange(
    exchange_rate: ql.ExchangeRate,
    money: ql.Money,
    trigger=None,
) -> ql.Money:
    return exchange_rate.exchange(money)


@xlo.func(
    help="Chain two ExchangeRates to create a new one.",
    args={
        "rate1": "The first ExchangeRate object.",
        "rate2": "The second ExchangeRate object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExchangeRateChain(
    rate1: ql.ExchangeRate,
    rate2: ql.ExchangeRate,
    trigger=None,
) -> ql.ExchangeRate:
    return ql.ExchangeRate.chain(rate1, rate2)


@xlo.func(
    help="Get the ExchangeRateManager instance.",
    group=EXCEL_GROUP_NAME,
)
def qlExchangeRateManagerInstance(trigger=None) -> ql.ExchangeRateManager:
    return ql.ExchangeRateManager.instance()


@xlo.func(
    help="Add an ExchangeRate to the ExchangeRateManager.",
    args={
        "exchange_rate": "The ExchangeRate to add.",
        "start_date": "The start date (optional, defaults to min date).",
        "end_date": "The end date (optional, defaults to max date).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExchangeRateManagerAdd(
    exchange_rate: ql.ExchangeRate,
    start_date: qDate = ql.Date.minDate(),
    end_date: qDate = ql.Date.maxDate(),
    trigger=None,
) -> bool:
    manager = ql.ExchangeRateManager.instance()
    manager.add(exchange_rate, start_date, end_date)
    return True


@xlo.func(
    help="Add an ExchangeRate to the ExchangeRateManager using a currency pair string.",
    args={
        "currency_pair": "The currency pair in the format 'XXX/YYY' or 'XXX-YYY' or 'XXX_YYY' or 'XXX.YYY'.",
        "rate": "The exchange rate.",
        "start_date": "The start date (optional, defaults to min date).",
        "end_date": "The end date (optional, defaults to max date).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExchangeRateManagerAdd2(
    currency_pair: str,
    rate: float,
    start_date: qDate = ql.Date.minDate(),
    end_date: qDate = ql.Date.maxDate(),
    trigger=None,
) -> bool:
    # Validate the currency pair format
    if not re.match(r"^([A-Z]{3})(/|-|_|\.)*([A-Z]{3})$", currency_pair):
        raise ValueError(
            f"Invalid currency pair format: {currency_pair}. Expected format is 'XXX[/|-|_|.]YYY' where XXX and YYY are ISO 4217 currency codes."
        )
    # Parse the currency pair
    source_currency = qCurrency.__wrapped__(currency_pair[:3])
    target_currency = qCurrency.__wrapped__(currency_pair[-3:])

    # Create the exchange rate
    exchange_rate = ql.ExchangeRate(source_currency, target_currency, rate)

    # Add it to the manager
    return qlExchangeRateManagerAdd(exchange_rate, start_date, end_date, trigger)


@xlo.func(
    help="Look up an ExchangeRate in the ExchangeRateManager.",
    args={
        "source": "The source Currency.",
        "target": "The target Currency.",
        "date": "The date for the lookup.",
        "exchange_rate_type": "The exchange rate type (DIRECT or DERIVED, defaults to DERIVED).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExchangeRateManagerLookup(
    source: qCurrency,
    target: qCurrency,
    date: qDate,
    exchange_rate_type: qExchangeRateType = ql.ExchangeRate.Derived,
    trigger=None,
) -> ql.ExchangeRate:
    manager = ql.ExchangeRateManager.instance()
    return manager.lookup(source, target, date, exchange_rate_type)


@xlo.func(
    help="Clear all ExchangeRates from the ExchangeRateManager.",
    group=EXCEL_GROUP_NAME,
)
def qlExchangeRateManagerClear(trigger=None) -> bool:
    manager = ql.ExchangeRateManager.instance()
    manager.clear()
    return True
