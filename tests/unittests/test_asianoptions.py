import QuantLib as ql
import pytest

from quantlib_xloil.asianoptions import (
    qAverageType,
    qlAnalyticContinuousGeometricAveragePriceAsianEngine,
    qlAnalyticContinuousGeometricAveragePriceAsianHestonEngine,
    qlAnalyticDiscreteGeometricAveragePriceAsianEngine,
    qlAnalyticDiscreteGeometricAveragePriceAsianHestonEngine,
    qlAnalyticDiscreteGeometricAverageStrikeAsianEngine,
    qlChoiAsianEngine,
    qlContinuousAveragingAsianOption,
    qlContinuousAveragingAsianOptionWithStartDate,
    qlContinuousArithmeticAsianLevyEngine,
    qlContinuousArithmeticAsianLevyEngineWithStartDate,
    qlDiscreteAveragingAsianOption,
    qlDiscreteAveragingAsianOptionTimeGrid,
    qlFdBlackScholesAsianEngine,
    qlMCDiscreteArithmeticAPEngine,
    qlMCDiscreteArithmeticAPHestonEngine,
    qlMCDiscreteArithmeticASEngine,
    qlMCDiscreteGeometricAPEngine,
    qlMCDiscreteGeometricAPHestonEngine,
    qlTurnbullWakemanAsianEngine,
)
from quantlib_xloil.date import qlDate
from quantlib_xloil.exercise import qlEuropeanExercise
from quantlib_xloil.payoffs import qlPlainVanillaPayoff


def test_qAverageType_converter():
    assert qAverageType.__wrapped__("ARITHMETIC") == ql.Average.Arithmetic
    assert qAverageType.__wrapped__("arithmetic") == ql.Average.Arithmetic
    assert qAverageType.__wrapped__("GEOMETRIC") == ql.Average.Geometric
    assert qAverageType.__wrapped__("geometric") == ql.Average.Geometric
    assert qAverageType.__wrapped__(ql.Average.Arithmetic) == ql.Average.Arithmetic


def test_qlContinuousAveragingAsianOption_construction():
    # Set up basic objects
    option_type = ql.Option.Call
    strike = 100.0
    payoff = qlPlainVanillaPayoff(option_type, strike)
    exercise_date = qlDate(2025, 12, 31)
    exercise = qlEuropeanExercise(exercise_date)

    # Create Asian option
    asian_option = qlContinuousAveragingAsianOption(
        qAverageType.__wrapped__("ARITHMETIC"), payoff, exercise
    )

    assert isinstance(asian_option, ql.ContinuousAveragingAsianOption)


def test_qlContinuousAveragingAsianOption_with_geometric_average():
    # Set up basic objects
    payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    exercise = qlEuropeanExercise(qlDate(2025, 12, 31))

    # Create Asian option with geometric average
    asian_option = qlContinuousAveragingAsianOption(
        qAverageType.__wrapped__("GEOMETRIC"), payoff, exercise
    )

    assert isinstance(asian_option, ql.ContinuousAveragingAsianOption)


def test_qlContinuousAveragingAsianOptionWithStartDate_construction():
    # Set up basic objects
    payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    exercise = qlEuropeanExercise(qlDate(2025, 12, 31))
    start_date = qlDate(2025, 1, 1)

    # Create Asian option with start date
    asian_option = qlContinuousAveragingAsianOptionWithStartDate(
        qAverageType.__wrapped__("ARITHMETIC"), start_date, payoff, exercise
    )

    assert isinstance(asian_option, ql.ContinuousAveragingAsianOption)


def test_qlDiscreteAveragingAsianOptionWithPastFixings_construction():
    # Set up basic objects
    payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    exercise = qlEuropeanExercise(qlDate(2025, 12, 31))

    # Create fixing dates
    fixing_dates = [
        qlDate(2025, 1, 1).serialNumber(),
        qlDate(2025, 2, 1).serialNumber(),
        qlDate(2025, 3, 1).serialNumber(),
    ]

    # Create discrete Asian option with past fixings
    asian_option = qlDiscreteAveragingAsianOption(
        qAverageType.__wrapped__("GEOMETRIC"),
        fixing_dates,
        payoff,
        exercise,
        [100.0, 101.0, 102.0],  # past fixings
    )

    assert isinstance(asian_option, ql.DiscreteAveragingAsianOption)


def test_qlDiscreteAveragingAsianOptionTimeGrid():
    # Set up basic objects
    payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    exercise = qlEuropeanExercise(qlDate(2025, 12, 31))

    # Create fixing dates
    fixing_dates = [
        qlDate(2025, 1, 1).serialNumber(),
        qlDate(2025, 2, 1).serialNumber(),
        qlDate(2025, 3, 1).serialNumber(),
    ]

    # Create discrete Asian option
    asian_option = qlDiscreteAveragingAsianOption(
        qAverageType.__wrapped__("ARITHMETIC"),
        fixing_dates,
        payoff,
        exercise,
    )

    # Get time grid
    # time_grid = qlDiscreteAveragingAsianOptionTimeGrid(asian_option)
    # assert isinstance(time_grid, ql.TimeGrid)


# Test Analytic Engines


def test_qlAnalyticContinuousGeometricAveragePriceAsianEngine():
    # Set up process
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )

    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    engine = qlAnalyticContinuousGeometricAveragePriceAsianEngine(process)

    assert isinstance(engine, ql.AnalyticContinuousGeometricAveragePriceAsianEngine)


def test_qlAnalyticContinuousGeometricAveragePriceAsianHestonEngine():
    spot = ql.QuoteHandle(ql.SimpleQuote(100.0))
    risk_free = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    process = ql.HestonProcess(risk_free, dividend, spot, 0.04, 1.50, 0.04, 0.25, -0.60)

    engine = qlAnalyticContinuousGeometricAveragePriceAsianHestonEngine(process)

    assert isinstance(
        engine, ql.AnalyticContinuousGeometricAveragePriceAsianHestonEngine
    )


def test_qlAnalyticDiscreteGeometricAveragePriceAsianEngine():
    # Set up process
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )

    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    engine = qlAnalyticDiscreteGeometricAveragePriceAsianEngine(process)

    assert isinstance(engine, ql.AnalyticDiscreteGeometricAveragePriceAsianEngine)


def test_qlAnalyticDiscreteGeometricAveragePriceAsianHestonEngine():
    spot = ql.QuoteHandle(ql.SimpleQuote(100.0))
    risk_free = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    process = ql.HestonProcess(risk_free, dividend, spot, 0.04, 1.50, 0.04, 0.25, -0.60)

    engine = qlAnalyticDiscreteGeometricAveragePriceAsianHestonEngine(process)

    assert isinstance(engine, ql.AnalyticDiscreteGeometricAveragePriceAsianHestonEngine)


def test_qlAnalyticDiscreteGeometricAverageStrikeAsianEngine():
    # Set up process
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )

    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    engine = qlAnalyticDiscreteGeometricAverageStrikeAsianEngine(process)

    assert isinstance(engine, ql.AnalyticDiscreteGeometricAverageStrikeAsianEngine)


# Test Other Engines


def test_qlChoiAsianEngine():
    # Set up process
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )

    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    engine = qlChoiAsianEngine(process)

    assert isinstance(engine, ql.ChoiAsianEngine)


def test_qlChoiAsianEngine_with_parameters():
    # Set up process
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )

    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    engine = qlChoiAsianEngine(process, lambda_=20, max_nr_integration_steps=1000)

    assert isinstance(engine, ql.ChoiAsianEngine)


def test_qlTurnbullWakemanAsianEngine():
    # Set up process
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )

    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    engine = qlTurnbullWakemanAsianEngine(process)

    assert isinstance(engine, ql.TurnbullWakemanAsianEngine)


def test_qlFdBlackScholesAsianEngine():
    # Set up process
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )

    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    engine = qlFdBlackScholesAsianEngine(process, 50, 50, 50)

    assert isinstance(engine, ql.FdBlackScholesAsianEngine)


# Test Monte Carlo Engines


def test_qlMCDiscreteArithmeticAPEngine_pseudorandom():
    # Set up process
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )

    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    engine = qlMCDiscreteArithmeticAPEngine(
        process, "pseudorandom", brownian_bridge=True, seed=42
    )

    assert isinstance(engine, ql.PricingEngine)


def test_qlMCDiscreteArithmeticAPEngine_lowdiscrepancy():
    # Set up process
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )

    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    engine = qlMCDiscreteArithmeticAPEngine(
        process, "lowdiscrepancy", antithetic_variate=True
    )

    assert isinstance(engine, ql.PricingEngine)


def test_qlMCDiscreteArithmeticASEngine():
    # Set up process
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )

    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    engine = qlMCDiscreteArithmeticASEngine(
        process, "pseudorandom", required_samples=1000
    )

    assert isinstance(engine, ql.PricingEngine)


def test_qlMCDiscreteArithmeticAPHestonEngine():
    spot = ql.QuoteHandle(ql.SimpleQuote(100.0))
    risk_free = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    process = ql.HestonProcess(risk_free, dividend, spot, 0.04, 1.50, 0.04, 0.25, -0.60)

    engine = qlMCDiscreteArithmeticAPHestonEngine(
        process, "lowdiscrepancy", required_samples=128
    )

    assert isinstance(engine, ql.PricingEngine)


def test_qlMCDiscreteGeometricAPEngine():
    # Set up process
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )

    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    engine = qlMCDiscreteGeometricAPEngine(process, "lowdiscrepancy", max_samples=10000)

    assert isinstance(engine, ql.PricingEngine)


def test_qlMCDiscreteGeometricAPHestonEngine():
    spot = ql.QuoteHandle(ql.SimpleQuote(100.0))
    risk_free = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    process = ql.HestonProcess(risk_free, dividend, spot, 0.04, 1.50, 0.04, 0.25, -0.60)

    engine = qlMCDiscreteGeometricAPHestonEngine(
        process, "pseudorandom", required_samples=128
    )

    assert isinstance(engine, ql.PricingEngine)


def test_qlContinuousArithmeticAsianLevyEngineWithStartDate():
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )
    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    running_average = ql.QuoteHandle(ql.SimpleQuote(100.0))
    start_date = qlDate(2025, 1, 1)

    engine = qlContinuousArithmeticAsianLevyEngineWithStartDate(
        process, running_average, start_date
    )

    assert isinstance(engine, ql.ContinuousArithmeticAsianLevyEngine)


def test_qlMCDiscreteArithmeticAPEngine_invalid_traits():
    # Set up process
    spot = 100.0
    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.05, ql.Actual365Fixed())
    )
    dividend_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(ql.Date(), 0.01, ql.Actual365Fixed())
    )
    flat_vol_ts = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(ql.Date(), ql.NullCalendar(), 0.20, ql.Actual365Fixed())
    )

    process = ql.BlackScholesMertonProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        dividend_ts,
        flat_ts,
        flat_vol_ts,
    )

    with pytest.raises(RuntimeError, match="unknown MC traits"):
        qlMCDiscreteArithmeticAPEngine(process, "INVALID")
