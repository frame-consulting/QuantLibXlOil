import QuantLib as ql

from quantlib_xloil.cliquetoptions import (
    qlAnalyticCliquetEngine,
    qlAnalyticPerformanceEngine,
    qlCliquetOption,
    qlMCPerformanceEngine,
)
from quantlib_xloil.date import qlDate
from quantlib_xloil.exercise import qlEuropeanExercise
from quantlib_xloil.instruments import qlInstrumentNPV, qlInstrumentSetPricingEngine
from quantlib_xloil.options import qMCTraits
from quantlib_xloil.payoffs import qlPercentageStrikePayoff


def _process():
    reference_date = qlDate(2024, 1, 2)
    day_counter = ql.Actual365Fixed()
    spot = ql.QuoteHandle(ql.SimpleQuote(100.0))
    risk_free = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.03, day_counter)
    )
    dividend = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.01, day_counter)
    )
    black_vol = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(reference_date, ql.TARGET(), 0.20, day_counter)
    )
    return ql.BlackScholesMertonProcess(spot, dividend, risk_free, black_vol)


def _cliquet_option():
    payoff = qlPercentageStrikePayoff(ql.Option.Call, 1.0)
    maturity = qlEuropeanExercise(qlDate(2025, 1, 2))
    reset_dates = [qlDate(2024, 4, 2).serialNumber(), qlDate(2024, 7, 2).serialNumber()]
    return qlCliquetOption(payoff, maturity, reset_dates)


def test_qlCliquetOption_construction():
    assert isinstance(_cliquet_option(), ql.CliquetOption)


def test_qlAnalyticCliquetEngine_npv():
    ql.Settings.instance().evaluationDate = qlDate(2024, 1, 2)
    option = _cliquet_option()

    assert qlInstrumentSetPricingEngine(option, qlAnalyticCliquetEngine(_process()))
    assert qlInstrumentNPV(option) > 0.0


def test_qlAnalyticPerformanceEngine_npv():
    ql.Settings.instance().evaluationDate = qlDate(2024, 1, 2)
    option = _cliquet_option()

    assert qlInstrumentSetPricingEngine(option, qlAnalyticPerformanceEngine(_process()))
    assert qlInstrumentNPV(option) > 0.0


def test_qlMCPerformanceEngine_npv():
    ql.Settings.instance().evaluationDate = qlDate(2024, 1, 2)
    option = _cliquet_option()
    engine = qlMCPerformanceEngine(
        _process(),
        qMCTraits.__wrapped__("PR"),
        required_samples=1024,
        seed=42,
    )

    assert qlInstrumentSetPricingEngine(option, engine)
    assert qlInstrumentNPV(option) > 0.0
