import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .currencies import qCurrency
from .utilities import enum_value, first_key, UNKNOWN_VALUE

QL_MONEY_CONVERSION_TYPE = {
    "AUTOMATED_CONVERSION": ql.Money.AutomatedConversion,
    "BASE_CURRENCY_CONVERSION": ql.Money.BaseCurrencyConversion,
    "NO_CONVERSION": ql.Money.NoConversion,
}


def _qMoneyConversionType(conversion_type: str) -> int:
    return enum_value(conversion_type, QL_MONEY_CONVERSION_TYPE)


@xlo.converter()
def qMoneyConversionType(conversion_type: str) -> int:
    return _qMoneyConversionType(conversion_type)


@xlo.func(
    help="Create a QuantLib Money object.",
    args={
        "currency": "The currency of the money.",
        "value": "The amount of money.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMoney(currency: qCurrency, value: float, trigger=None) -> ql.Money:
    return ql.Money(currency, value)


@xlo.func(
    help="Get the currency of a QuantLib Money object.",
    args={"money": "The Money object."},
    group=EXCEL_GROUP_NAME,
)
def qlMoneyCurrency(money: ql.Money, trigger=None) -> ql.Currency:
    return money.currency()


@xlo.func(
    help="Get the amount of a QuantLib Money object.",
    args={"money": "The Money object."},
    group=EXCEL_GROUP_NAME,
)
def qlMoneyValue(money: ql.Money, trigger=None) -> float:
    return money.value()


@xlo.func(
    help="Round a QuantLib Money object according to its currency.",
    args={"money": "The Money object to round."},
    group=EXCEL_GROUP_NAME,
)
def qlMoneyRounded(money: ql.Money, trigger=None) -> ql.Money:
    return money.rounded()


@xlo.func(
    help="Add two QuantLib Money objects.",
    args={
        "money1": "The first Money object.",
        "money2": "The second Money object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMoneyAdd(money1: ql.Money, money2: ql.Money, trigger=None) -> ql.Money:
    return money1 + money2


@xlo.func(
    help="Subtract one QuantLib Money object from another.",
    args={
        "money1": "The Money object to subtract from.",
        "money2": "The Money object to subtract.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMoneySubtract(money1: ql.Money, money2: ql.Money, trigger=None) -> ql.Money:
    return money1 - money2


@xlo.func(
    help="Multiply a QuantLib Money object by a number.",
    args={
        "money": "The Money object.",
        "multiplier": "The number to multiply by.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMoneyMultiply(money: ql.Money, multiplier: float, trigger=None) -> ql.Money:
    return money * multiplier


@xlo.func(
    help="Divide a QuantLib Money object by a number.",
    args={
        "money": "The Money object.",
        "divisor": "The number to divide by.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMoneyDivide(money: ql.Money, divisor: float, trigger=None) -> ql.Money:
    return money / divisor


@xlo.func(
    help="Divide one QuantLib Money object by another.",
    args={
        "money1": "The numerator Money object.",
        "money2": "The denominator Money object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMoneyRatio(money1: ql.Money, money2: ql.Money, trigger=None) -> float:
    return money1 / money2


@xlo.func(
    help="Negate a QuantLib Money object.",
    args={"money": "The Money object to negate."},
    group=EXCEL_GROUP_NAME,
)
def qlMoneyNegate(money: ql.Money, trigger=None) -> ql.Money:
    return -money


@xlo.func(
    help="Compare two QuantLib Money objects for equality.",
    args={
        "money1": "The first Money object.",
        "money2": "The second Money object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMoneyEqual(money1: ql.Money, money2: ql.Money, trigger=None) -> bool:
    return money1 == money2


@xlo.func(
    help="Compare two QuantLib Money objects for inequality.",
    args={
        "money1": "The first Money object.",
        "money2": "The second Money object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMoneyNotEqual(money1: ql.Money, money2: ql.Money, trigger=None) -> bool:
    return money1 != money2


@xlo.func(
    help="Check whether one QuantLib Money object is less than another.",
    args={
        "money1": "The first Money object.",
        "money2": "The second Money object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMoneyLessThan(money1: ql.Money, money2: ql.Money, trigger=None) -> bool:
    return money1 < money2


@xlo.func(
    help="Check whether one QuantLib Money object is less than or equal to another.",
    args={
        "money1": "The first Money object.",
        "money2": "The second Money object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMoneyLessThanOrEqual(money1: ql.Money, money2: ql.Money, trigger=None) -> bool:
    return money1 <= money2


@xlo.func(
    help="Check whether one QuantLib Money object is greater than another.",
    args={
        "money1": "The first Money object.",
        "money2": "The second Money object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMoneyGreaterThan(money1: ql.Money, money2: ql.Money, trigger=None) -> bool:
    return money1 > money2


@xlo.func(
    help="Check whether one QuantLib Money object is greater than or equal to another.",
    args={
        "money1": "The first Money object.",
        "money2": "The second Money object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMoneyGreaterThanOrEqual(money1: ql.Money, money2: ql.Money, trigger=None) -> bool:
    return money1 >= money2


@xlo.func(
    help="Convert a QuantLib Money object to a string.",
    args={"money": "The Money object to convert."},
    group=EXCEL_GROUP_NAME,
)
def qlMoneyToString(money: ql.Money, trigger=None) -> str:
    return str(money)


@xlo.func(
    help="Set the QuantLib Money conversion type.",
    args={"conversion_type": "The Money conversion type."},
    group=EXCEL_GROUP_NAME,
)
def qlMoneySetConversionType(
    conversion_type: qMoneyConversionType, trigger=None
) -> bool:
    ql.Money.setConversionType(conversion_type)
    return True


@xlo.func(
    help="Set the base currency for QuantLib Money conversion.",
    args={"currency": "The base currency."},
    group=EXCEL_GROUP_NAME,
)
def qlMoneySetBaseCurrency(currency: qCurrency, trigger=None) -> bool:
    ql.Money.setBaseCurrency(currency)
    return True
