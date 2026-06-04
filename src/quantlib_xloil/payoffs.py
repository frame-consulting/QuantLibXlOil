import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import enum_value, first_key, UNKNOWN_KEY, UNKNOWN_VALUE


QL_OPTION_TYPE = {
	"CALL": ql.Option.Call,
	"PUT": ql.Option.Put,
	UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qOptionType(option_type: str) -> int:
	return enum_value(option_type, QL_OPTION_TYPE)


@xlo.converter()
def qOptionType(option_type: str) -> int:
	return _qOptionType(option_type)


@xlo.func(
	help="Return payoff value for a given spot.",
	args={
		"payoff": "QuantLib payoff.",
		"price": "Underlying price.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlPayoffValue(payoff: ql.Payoff, price: float, trigger=None) -> float:
	return payoff(price)


@xlo.func(
	help="Return payoff option type.",
	args={
		"payoff": "QuantLib type payoff.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlTypePayoffOptionType(payoff: ql.TypePayoff, trigger=None) -> qOptionType:
	return first_key(QL_OPTION_TYPE, payoff.optionType(), UNKNOWN_VALUE)


@xlo.func(
	help="Return payoff strike.",
	args={
		"payoff": "QuantLib striked payoff.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStrikedTypePayoffStrike(payoff: ql.StrikedTypePayoff, trigger=None) -> float:
	return payoff.strike()


@xlo.func(
	help="Create a QuantLib PlainVanillaPayoff object.",
	args={
		"option_type": "Option type.",
		"strike": "Strike value.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlPlainVanillaPayoff(option_type: qOptionType, strike: float, trigger=None) -> ql.PlainVanillaPayoff:
	return ql.PlainVanillaPayoff(option_type, strike)


@xlo.func(
	help="Cast a Payoff to PlainVanillaPayoff if possible.",
	args={
		"payoff": "QuantLib payoff.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlAsPlainVanillaPayoff(payoff: ql.Payoff, trigger=None) -> ql.PlainVanillaPayoff:
	return ql.as_plain_vanilla_payoff(payoff)


@xlo.func(
	help="Create a QuantLib PercentageStrikePayoff object.",
	args={
		"option_type": "Option type.",
		"moneyness": "Moneyness value.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlPercentageStrikePayoff(option_type: qOptionType, moneyness: float, trigger=None) -> ql.PercentageStrikePayoff:
	return ql.PercentageStrikePayoff(option_type, moneyness)


@xlo.func(
	help="Create a QuantLib CashOrNothingPayoff object.",
	args={
		"option_type": "Option type.",
		"strike": "Strike value.",
		"cash_payoff": "Cash payoff value.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashOrNothingPayoff(
	option_type: qOptionType,
	strike: float,
	cash_payoff: float,
	trigger=None,
) -> ql.CashOrNothingPayoff:
	return ql.CashOrNothingPayoff(option_type, strike, cash_payoff)


@xlo.func(
	help="Create a QuantLib AssetOrNothingPayoff object.",
	args={
		"option_type": "Option type.",
		"strike": "Strike value.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlAssetOrNothingPayoff(option_type: qOptionType, strike: float, trigger=None) -> ql.AssetOrNothingPayoff:
	return ql.AssetOrNothingPayoff(option_type, strike)


@xlo.func(
	help="Create a QuantLib SuperSharePayoff object.",
	args={
		"option_type": "Option type.",
		"strike": "Strike value.",
		"increment": "Increment value.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlSuperSharePayoff(
	option_type: qOptionType,
	strike: float,
	increment: float,
	trigger=None,
) -> ql.SuperSharePayoff:
	return ql.SuperSharePayoff(option_type, strike, increment)


@xlo.func(
	help="Create a QuantLib GapPayoff object.",
	args={
		"option_type": "Option type.",
		"strike": "Strike value.",
		"strike_payoff": "Second strike payoff value.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGapPayoff(
	option_type: qOptionType,
	strike: float,
	strike_payoff: float,
	trigger=None,
) -> ql.GapPayoff:
	return ql.GapPayoff(option_type, strike, strike_payoff)


@xlo.func(
	help="Create a QuantLib VanillaForwardPayoff object.",
	args={
		"option_type": "Option type.",
		"strike": "Strike value.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlVanillaForwardPayoff(option_type: qOptionType, strike: float, trigger=None) -> ql.VanillaForwardPayoff:
	return ql.VanillaForwardPayoff(option_type, strike)
