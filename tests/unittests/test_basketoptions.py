import QuantLib as ql

from quantlib_xloil.basketoptions import (
    qOperatorSplittingSpreadEngineOrder,
    qlAverageBasketPayoff,
    qlBasketOption,
    qlBjerksundStenslandSpreadEngine,
    qlChoiBasketEngine,
    qlDengLiZhouBasketEngine,
    qlEverestOption,
    qlFd2dBlackScholesVanillaEngine,
    qlFdndimBlackScholesVanillaEngine,
    qlHimalayaOption,
    qlKirkEngine,
    qlMCAmericanBasketEngine,
    qlMCEuropeanBasketEngine,
    qlMCEverestEngine,
    qlMCHimalayaEngine,
    qlMaxBasketPayoff,
    qlMinBasketPayoff,
    qlOperatorSplittingSpreadEngine,
    qlSpreadBasketPayoff,
    qlStulzEngine,
)
from quantlib_xloil.date import qlDate
from quantlib_xloil.exercise import qlAmericanExercise, qlEuropeanExercise
from quantlib_xloil.instruments import qlInstrumentNPV, qlInstrumentSetPricingEngine
from quantlib_xloil.options import qMCTraits
from quantlib_xloil.payoffs import qlPlainVanillaPayoff
from quantlib_xloil.stochasticprocess import qlStochasticProcessArray


def _process(spot_value: float, volatility: float = 0.20):
    reference_date = qlDate(2024, 1, 2)
    day_counter = ql.Actual365Fixed()
    spot = ql.QuoteHandle(ql.SimpleQuote(spot_value))
    risk_free = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.03, day_counter)
    )
    dividend = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.01, day_counter)
    )
    black_vol = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(reference_date, ql.TARGET(), volatility, day_counter)
    )
    return ql.BlackScholesMertonProcess(spot, dividend, risk_free, black_vol)


def _process_array():
    processes = [_process(100.0), _process(95.0, 0.25)]
    correlation = [[1.0, 0.30], [0.30, 1.0]]
    return processes, correlation, qlStochasticProcessArray(processes, correlation)


def test_qlOperatorSplittingSpreadEngineOrder_converter():
    assert (
        qOperatorSplittingSpreadEngineOrder.__wrapped__("first")
        == ql.OperatorSplittingSpreadEngine.First
    )
    assert (
        qOperatorSplittingSpreadEngineOrder.__wrapped__("SECOND")
        == ql.OperatorSplittingSpreadEngine.Second
    )


def test_basket_payoff_and_option_construction():
    payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    exercise = qlEuropeanExercise(qlDate(2025, 1, 2))

    assert isinstance(qlMinBasketPayoff(payoff), ql.MinBasketPayoff)
    assert isinstance(qlMaxBasketPayoff(payoff), ql.MaxBasketPayoff)
    average_payoff = qlAverageBasketPayoff(payoff, [0.5, 0.5])
    assert isinstance(average_payoff, ql.AverageBasketPayoff)
    assert isinstance(qlSpreadBasketPayoff(payoff), ql.SpreadBasketPayoff)
    assert isinstance(qlBasketOption(average_payoff, exercise), ql.BasketOption)


def test_two_asset_basket_engine_wrappers():
    process1 = _process(100.0)
    process2 = _process(95.0, 0.25)

    assert isinstance(qlStulzEngine(process1, process2, 0.30), ql.StulzEngine)
    assert isinstance(qlKirkEngine(process1, process2, 0.30), ql.KirkEngine)
    assert isinstance(
        qlBjerksundStenslandSpreadEngine(process1, process2, 0.30),
        ql.BjerksundStenslandSpreadEngine,
    )
    assert isinstance(
        qlOperatorSplittingSpreadEngine(
            process1,
            process2,
            0.30,
            qOperatorSplittingSpreadEngineOrder.__wrapped__("FIRST"),
        ),
        ql.OperatorSplittingSpreadEngine,
    )
    assert isinstance(
        qlFd2dBlackScholesVanillaEngine(process1, process2, 0.30, 25, 25, 25),
        ql.Fd2dBlackScholesVanillaEngine,
    )


def test_multi_asset_basket_engine_wrappers():
    processes, correlation, process_array = _process_array()

    assert isinstance(
        qlChoiBasketEngine(processes, correlation, max_nr_integration_steps=100),
        ql.ChoiBasketEngine,
    )
    assert isinstance(
        qlDengLiZhouBasketEngine(processes, correlation), ql.DengLiZhouBasketEngine
    )
    assert isinstance(
        qlFdndimBlackScholesVanillaEngine(processes, correlation, 10, 25),
        ql.FdndimBlackScholesVanillaEngine,
    )
    assert isinstance(
        qlMCEuropeanBasketEngine(
            process_array,
            qMCTraits.__wrapped__("PR"),
            time_steps=10,
            required_samples=64,
        ),
        ql.PricingEngine,
    )
    assert isinstance(
        qlMCAmericanBasketEngine(
            process_array,
            qMCTraits.__wrapped__("LD"),
            time_steps=10,
            required_samples=64,
            n_calibration_samples=64,
        ),
        ql.PricingEngine,
    )


def test_basket_option_pricing_with_kirk_engine():
    ql.Settings.instance().evaluationDate = qlDate(2024, 1, 2)
    payoff = qlSpreadBasketPayoff(qlPlainVanillaPayoff(ql.Option.Call, 5.0))
    option = qlBasketOption(payoff, qlEuropeanExercise(qlDate(2025, 1, 2)))
    engine = qlKirkEngine(_process(100.0), _process(95.0, 0.25), 0.30)

    assert qlInstrumentSetPricingEngine(option, engine) is True
    assert qlInstrumentNPV(option) > 0.0


def test_everest_and_himalaya_option_wrappers():
    _, _, process_array = _process_array()
    european_exercise = qlEuropeanExercise(qlDate(2025, 1, 2))
    american_exercise = qlAmericanExercise(qlDate(2024, 6, 1), qlDate(2025, 1, 2))

    assert isinstance(qlEverestOption(100.0, 0.05, european_exercise), ql.EverestOption)
    assert isinstance(
        qlMCEverestEngine(
            process_array,
            qMCTraits.__wrapped__("PR"),
            time_steps=10,
            required_samples=64,
        ),
        ql.PricingEngine,
    )
    assert isinstance(
        qlHimalayaOption(
            [qlDate(2024, 7, 2).serialNumber(), qlDate(2025, 1, 2).serialNumber()],
            100.0,
        ),
        ql.HimalayaOption,
    )
    assert isinstance(american_exercise, ql.AmericanExercise)
    assert isinstance(
        qlMCHimalayaEngine(
            process_array, qMCTraits.__wrapped__("LD"), required_samples=64
        ),
        ql.PricingEngine,
    )
