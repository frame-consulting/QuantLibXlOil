import QuantLib as ql
import pytest

from quantlib_xloil.blackformula import (
    qlBachelierBlackFormula,
    qlBachelierBlackFormulaImpliedVol,
    qlBachelierBlackFormulaImpliedVolChoi,
    qlBlackDeltaCalculator,
    qlBlackDeltaCalculatorAtmStrike,
    qlBlackDeltaCalculatorDeltaFromStrike,
    qlBlackDeltaCalculatorStrikeFromDelta,
    qlBlackFormula,
    qlBlackFormulaImpliedStdDev,
    qlBlackFormulaImpliedStdDevLiRS,
)
from quantlib_xloil.options import qDeltaVolQuoteAtmType, qDeltaVolQuoteDeltaType
from quantlib_xloil.payoffs import qOptionType


def test_black_formula_wrappers_match_quantlib():
    option_type = qOptionType.__wrapped__("call")
    strike = 100.0
    forward = 102.0
    std_dev = 0.20
    discount = 0.97
    displacement = 0.01

    price = qlBlackFormula(
        option_type, strike, forward, std_dev, discount, displacement
    )

    assert price == pytest.approx(
        ql.blackFormula(option_type, strike, forward, std_dev, discount, displacement)
    )
    assert qlBlackFormulaImpliedStdDev(
        option_type, strike, forward, price, discount, displacement
    ) == pytest.approx(std_dev)
    assert qlBlackFormulaImpliedStdDevLiRS(
        option_type, strike, forward, price, discount, displacement
    ) == pytest.approx(std_dev)


def test_bachelier_formula_wrappers_match_quantlib():
    option_type = qOptionType.__wrapped__("put")
    strike = 100.0
    forward = 98.0
    time_to_expiry = 2.0
    volatility = 0.20
    std_dev = volatility * (time_to_expiry**0.5)
    discount = 0.96

    price = qlBachelierBlackFormula(option_type, strike, forward, std_dev, discount)

    assert price == pytest.approx(
        ql.bachelierBlackFormula(option_type, strike, forward, std_dev, discount)
    )
    implied_vol = qlBachelierBlackFormulaImpliedVol(
        option_type, strike, forward, time_to_expiry, price, discount
    )
    implied_vol_choi = qlBachelierBlackFormulaImpliedVolChoi(
        option_type, strike, forward, time_to_expiry, price, discount
    )

    assert implied_vol == pytest.approx(
        ql.bachelierBlackFormulaImpliedVol(
            option_type, strike, forward, time_to_expiry, price, discount
        )
    )
    assert implied_vol_choi == pytest.approx(
        ql.bachelierBlackFormulaImpliedVolChoi(
            option_type, strike, forward, time_to_expiry, price, discount
        )
    )
    assert implied_vol == pytest.approx(volatility, rel=1e-4)
    assert implied_vol_choi == pytest.approx(volatility, rel=1e-4)


def test_black_delta_calculator_wrappers_match_methods():
    option_type = qOptionType.__wrapped__("call")
    delta_type = qDeltaVolQuoteDeltaType.__wrapped__("spot")
    atm_type = qDeltaVolQuoteAtmType.__wrapped__("atmfwd")

    calculator = qlBlackDeltaCalculator(
        option_type,
        delta_type,
        100.0,
        0.98,
        0.99,
        0.20,
    )

    strike = 105.0
    delta = qlBlackDeltaCalculatorDeltaFromStrike(calculator, strike)

    assert isinstance(calculator, ql.BlackDeltaCalculator)
    assert delta == pytest.approx(calculator.deltaFromStrike(strike))
    assert qlBlackDeltaCalculatorStrikeFromDelta(calculator, delta) == pytest.approx(
        calculator.strikeFromDelta(delta)
    )
    assert qlBlackDeltaCalculatorStrikeFromDelta(calculator, delta) == pytest.approx(
        strike
    )
    assert qlBlackDeltaCalculatorAtmStrike(calculator, atm_type) == pytest.approx(
        calculator.atmStrike(atm_type)
    )
