import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .payoffs import qOptionType
from .options import qDeltaVolQuoteDeltaType, qDeltaVolQuoteAtmType


@xlo.func(
    help="Calculate the Black formula for a European option.",
    args={
        "option_type": "The type of the option (call or put).",
        "strike": "The strike price of the option.",
        "forward": "The forward price of the underlying asset.",
        "std_dev": "The standard deviation of the underlying asset's returns.",
        "discount": "The discount factor to apply to the option price (default is 1.0).",
        "displacement": "The displacement to apply to the forward price (default is 0.0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackFormula(
    option_type: qOptionType,
    strike: float,
    forward: float,
    std_dev: float,
    discount: float = 1.0,
    displacement: float = 0.0,
    trigger=None,
) -> float:
    return ql.blackFormula(
        option_type, strike, forward, std_dev, discount, displacement
    )


@xlo.func(
    help="Calculate the implied standard deviation using the Black formula.",
    args={
        "option_type": "The type of the option (call or put).",
        "strike": "The strike price of the option.",
        "forward": "The forward price of the underlying asset.",
        "price": "The market price of the option.",
        "discount": "The discount factor to apply to the option price (default is 1.0).",
        "displacement": "The displacement to apply to the forward price (default is 0.0).",
        "guess": "An initial guess for the implied standard deviation (default is null).",
        "accuracy": "The desired accuracy for the result (default is 1e-6).",
        "max_iterations": "The maximum number of iterations to perform (default is 100).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackFormulaImpliedStdDev(
    option_type: qOptionType,
    strike: float,
    forward: float,
    price: float,
    discount: float = 1.0,
    displacement: float = 0.0,
    guess: float = ql.nullDouble(),
    accuracy: float = 1e-6,
    max_iterations: int = 100,
    trigger=None,
) -> float:
    return ql.blackFormulaImpliedStdDev(
        option_type,
        strike,
        forward,
        price,
        discount,
        displacement,
        guess,
        accuracy,
        max_iterations,
    )


@xlo.func(
    help="Calculate the implied standard deviation using the Black formula with LiRS method.",
    args={
        "option_type": "The type of the option (call or put).",
        "strike": "The strike price of the option.",
        "forward": "The forward price of the underlying asset.",
        "price": "The market price of the option.",
        "discount": "The discount factor to apply to the option price (default is 1.0).",
        "displacement": "The displacement to apply to the forward price (default is 0.0).",
        "guess": "An initial guess for the implied standard deviation (default is null).",
        "omega": "The omega parameter for the LiRS method (default is 1.0).",
        "accuracy": "The desired accuracy for the result (default is 1e-6).",
        "max_iterations": "The maximum number of iterations to perform (default is 100).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackFormulaImpliedStdDevLiRS(
    option_type: qOptionType,
    strike: float,
    forward: float,
    price: float,
    discount: float = 1.0,
    displacement: float = 0.0,
    guess: float = ql.nullDouble(),
    omega: float = 1.0,
    accuracy: float = 1e-6,
    max_iterations: int = 100,
    trigger=None,
) -> float:
    return ql.blackFormulaImpliedStdDevLiRS(
        option_type,
        strike,
        forward,
        price,
        discount,
        displacement,
        guess,
        omega,
        accuracy,
        max_iterations,
    )


@xlo.func(
    help="Calculate the Bachelier formula for a European option.",
    args={
        "option_type": "The type of the option (call or put).",
        "strike": "The strike price of the option.",
        "forward": "The forward price of the underlying asset.",
        "std_dev": "The standard deviation of the underlying asset's returns.",
        "discount": "The discount factor to apply to the option price (default is 1.0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierBlackFormula(
    option_type: qOptionType,
    strike: float,
    forward: float,
    std_dev: float,
    discount: float = 1.0,
    trigger=None,
) -> float:
    return ql.bachelierBlackFormula(option_type, strike, forward, std_dev, discount)


@xlo.func(
    help="Calculate the implied volatility using the Bachelier formula.",
    args={
        "option_type": "The type of the option (call or put).",
        "strike": "The strike price of the option.",
        "forward": "The forward price of the underlying asset.",
        "time_to_expiry": "The time to expiry of the option in years.",
        "price": "The market price of the option.",
        "discount": "The discount factor to apply to the option price (default is 1.0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierBlackFormulaImpliedVol(
    option_type: qOptionType,
    strike: float,
    forward: float,
    time_to_expiry: float,
    price: float,
    discount: float = 1.0,
    trigger=None,
) -> float:
    return ql.bachelierBlackFormulaImpliedVol(
        option_type, strike, forward, time_to_expiry, price, discount
    )


@xlo.func(
    help="Calculate the implied volatility using the Bachelier formula with Choi's method.",
    args={
        "option_type": "The type of the option (call or put).",
        "strike": "The strike price of the option.",
        "forward": "The forward price of the underlying asset.",
        "time_to_expiry": "The time to expiry of the option in years.",
        "price": "The market price of the option.",
        "discount": "The discount factor to apply to the option price (default is 1.0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierBlackFormulaImpliedVolChoi(
    option_type: qOptionType,
    strike: float,
    forward: float,
    time_to_expiry: float,
    price: float,
    discount: float = 1.0,
    trigger=None,
) -> float:
    return ql.bachelierBlackFormulaImpliedVolChoi(
        option_type, strike, forward, time_to_expiry, price, discount
    )


@xlo.func(
    help="Create a BlackDeltaCalculator object.",
    args={
        "option_type": "The type of the option (call or put).",
        "delta_type": "The type of delta to calculate (e.g. spot, forward, etc.).",
        "spot": "The current price of the underlying asset.",
        "domestic_discount": "The discount factor for the domestic currency.",
        "foreign_discount": "The discount factor for the foreign currency.",
        "std_dev": "The standard deviation of the underlying asset's returns.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackDeltaCalculator(
    option_type: qOptionType,
    delta_type: qDeltaVolQuoteDeltaType,
    spot: float,
    domestic_discount: float,
    foreign_discount: float,
    std_dev: float,
    trigger=None,
) -> ql.BlackDeltaCalculator:
    return ql.BlackDeltaCalculator(
        option_type, delta_type, spot, domestic_discount, foreign_discount, std_dev
    )


@xlo.func(
    help="Calculate the strike price corresponding to a given delta using a BlackDeltaCalculator.",
    args={
        "calculator": "The BlackDeltaCalculator object to use for the calculation.",
        "delta": "The delta value for which to calculate the strike price.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackDeltaCalculatorDeltaFromStrike(
    calculator: ql.BlackDeltaCalculator,
    strike: float,
    trigger=None,
) -> float:
    return calculator.deltaFromStrike(strike)


@xlo.func(
    help="Calculate the strike price corresponding to a given delta using a BlackDeltaCalculator.",
    args={
        "calculator": "The BlackDeltaCalculator object to use for the calculation.",
        "delta": "The delta value for which to calculate the strike price.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackDeltaCalculatorStrikeFromDelta(
    calculator: ql.BlackDeltaCalculator,
    delta: float,
    trigger=None,
) -> float:
    return calculator.strikeFromDelta(delta)


@xlo.func(
    help="Calculate the at-the-money strike price using a BlackDeltaCalculator.",
    args={
        "calculator": "The BlackDeltaCalculator object to use for the calculation.",
        "atm_type": "The type of at-the-money strike to calculate (e.g. spot, forward, etc.).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackDeltaCalculatorAtmStrike(
    calculator: ql.BlackDeltaCalculator,
    atm_type: qDeltaVolQuoteAtmType,
    trigger=None,
) -> float:
    return calculator.atmStrike(atm_type)
