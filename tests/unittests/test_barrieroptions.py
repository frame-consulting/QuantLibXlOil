import QuantLib as ql
import pytest

from quantlib_xloil import (
    qlAnalyticBarrierEngine,
    qlAnalyticBinaryBarrierEngine,
    qlAnalyticDoubleBarrierBinaryEngine,
    qlAnalyticDoubleBarrierEngine,
    qlAnalyticPartialTimeBarrierOptionEngine,
    qlAnalyticSoftBarrierEngine,
    qlAnalyticTwoAssetBarrierEngine,
    qlBarrierOption,
    qlBarrierOptionImpliedVolatility,
    qlBinomialBarrierEngine,
    qlBinomialDoubleBarrierEngine,
    qlDate,
    qlDoubleBarrierOption,
    qlEuropeanExercise,
    qlFdBlackScholesBarrierEngine,
    qlFdBlackScholesRebateEngine,
    qlFdHestonBarrierEngine,
    qlFdHestonDoubleBarrierEngine,
    qlFdHestonRebateEngine,
    qlInstrumentNPV,
    qlInstrumentSetPricingEngine,
    qlMCBarrierEngine,
    qlPartialTimeBarrierOption,
    qlPlainVanillaPayoff,
    qlQuantoBarrierEngine,
    qlQuantoBarrierOption,
    qlQuantoDoubleBarrierOption,
    qlSoftBarrierOption,
    qlSoftBarrierOptionImpliedVolatility,
    qlSuoWangDoubleBarrierEngine,
    qlTwoAssetBarrierOption,
)
from quantlib_xloil.barrieroptions import (
    qBarrierType,
    qDoubleBarrierType,
    qPartialBarrierRange,
    qlBarrierTypeName,
    qlDoubleBarrierTypeName,
    qlPartialBarrierRangeName,
)
from quantlib_xloil.options import (
    qMCTraits,
    qBinomialEngineType,
)


def _set_eval_date() -> None:
    ql.Settings.instance().evaluationDate = qlDate(2024, 1, 2)


def _process(volatility: float = 0.20, spot_value: float = 100.0):
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


def _heston_model():
    reference_date = qlDate(2024, 1, 2)
    day_counter = ql.Actual365Fixed()
    spot = ql.QuoteHandle(ql.SimpleQuote(100.0))
    risk_free = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.03, day_counter)
    )
    dividend = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.01, day_counter)
    )
    process = ql.HestonProcess(risk_free, dividend, spot, 0.04, 1.50, 0.04, 0.25, -0.60)
    return ql.HestonModel(process)


def _plain_vanilla_objects():
    payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    exercise = qlEuropeanExercise(qlDate(2025, 1, 2))
    return payoff, exercise


def test_barrier_type_converters_and_names():
    assert qBarrierType.__wrapped__("downin") == ql.Barrier.DownIn
    assert qBarrierType.__wrapped__("UO") == ql.Barrier.UpOut
    assert qPartialBarrierRange.__wrapped__("start") == ql.PartialBarrier.Start
    assert qDoubleBarrierType.__wrapped__("koki") == ql.DoubleBarrier.KOKI

    assert qlBarrierTypeName(ql.Barrier.DownOut) == "DO"
    assert qlPartialBarrierRangeName(ql.PartialBarrier.EndB1) == "ENDB1"
    assert qlDoubleBarrierTypeName(ql.DoubleBarrier.KnockIn) == "KNOCKIN"


def test_barrier_option_construction_and_implied_volatility():
    _set_eval_date()
    payoff, exercise = _plain_vanilla_objects()
    process = _process(0.20)

    option = qlBarrierOption(ql.Barrier.DownOut, 90.0, 0.0, payoff, exercise)
    quanto_option = qlQuantoBarrierOption(
        ql.Barrier.UpOut, 120.0, 0.0, payoff, exercise
    )
    partial = qlPartialTimeBarrierOption(
        ql.Barrier.DownOut,
        ql.PartialBarrier.Start,
        90.0,
        0.0,
        qlDate(2024, 6, 30),
        payoff,
        exercise,
    )

    assert isinstance(option, ql.BarrierOption)
    assert isinstance(quanto_option, ql.QuantoBarrierOption)
    assert isinstance(partial, ql.PartialTimeBarrierOption)

    engine = qlAnalyticBarrierEngine(process)
    assert qlInstrumentSetPricingEngine(option, engine) is True

    npv = qlInstrumentNPV(option)
    assert npv > 0.0

    implied = qlBarrierOptionImpliedVolatility(option, npv, process)
    assert implied == pytest.approx(0.20, rel=1e-2)


def test_barrier_engine_wrappers():
    _set_eval_date()
    process = _process(0.20)
    model = _heston_model()

    day_counter = ql.Actual365Fixed()
    reference_date = qlDate(2024, 1, 2)
    foreign_risk_free = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.02, day_counter)
    )
    fx_vol = ql.BlackVolTermStructureHandle(
        ql.BlackConstantVol(reference_date, ql.TARGET(), 0.15, day_counter)
    )
    corr = ql.QuoteHandle(ql.SimpleQuote(0.25))

    assert isinstance(
        qlAnalyticPartialTimeBarrierOptionEngine(process),
        ql.AnalyticPartialTimeBarrierOptionEngine,
    )
    assert isinstance(qlAnalyticBarrierEngine(process), ql.AnalyticBarrierEngine)
    assert isinstance(
        qlMCBarrierEngine(
            process, qMCTraits.__wrapped__("PR"), time_steps=25, required_samples=1024
        ),
        ql.PricingEngine,
    )
    assert isinstance(
        qlQuantoBarrierEngine(process, foreign_risk_free, fx_vol, corr),
        ql.QuantoBarrierEngine,
    )
    assert isinstance(
        qlFdBlackScholesBarrierEngine(process), ql.FdBlackScholesBarrierEngine
    )
    assert isinstance(
        qlFdBlackScholesRebateEngine(process), ql.FdBlackScholesRebateEngine
    )
    assert isinstance(qlFdHestonBarrierEngine(model), ql.FdHestonBarrierEngine)
    assert isinstance(qlFdHestonRebateEngine(model), ql.FdHestonRebateEngine)
    assert isinstance(
        qlAnalyticBinaryBarrierEngine(process), ql.AnalyticBinaryBarrierEngine
    )
    assert isinstance(
        qlBinomialBarrierEngine(process, qBinomialEngineType.__wrapped__("CRR"), 200),
        ql.PricingEngine,
    )


def test_double_barrier_and_soft_barrier_wrappers():
    _set_eval_date()
    payoff, exercise = _plain_vanilla_objects()
    process = _process(0.20)
    model = _heston_model()

    option = qlDoubleBarrierOption(
        ql.DoubleBarrier.KnockOut, 90.0, 120.0, 0.0, payoff, exercise
    )
    quanto_option = qlQuantoDoubleBarrierOption(
        ql.DoubleBarrier.KnockOut, 90.0, 120.0, 0.0, payoff, exercise
    )
    soft_option = qlSoftBarrierOption(ql.Barrier.DownOut, 90.0, 95.0, payoff, exercise)

    assert isinstance(option, ql.DoubleBarrierOption)
    assert isinstance(quanto_option, ql.QuantoDoubleBarrierOption)
    assert isinstance(soft_option, ql.SoftBarrierOption)

    assert isinstance(
        qlAnalyticDoubleBarrierEngine(process), ql.AnalyticDoubleBarrierEngine
    )
    assert isinstance(
        qlAnalyticDoubleBarrierBinaryEngine(process),
        ql.AnalyticDoubleBarrierBinaryEngine,
    )
    assert isinstance(
        qlSuoWangDoubleBarrierEngine(process), ql.SuoWangDoubleBarrierEngine
    )
    assert isinstance(
        qlFdHestonDoubleBarrierEngine(model), ql.FdHestonDoubleBarrierEngine
    )
    assert isinstance(
        qlBinomialDoubleBarrierEngine(
            process, qBinomialEngineType.__wrapped__("TIAN"), 200
        ),
        ql.PricingEngine,
    )

    soft_engine = qlAnalyticSoftBarrierEngine(process)
    assert qlInstrumentSetPricingEngine(soft_option, soft_engine) is True

    soft_npv = qlInstrumentNPV(soft_option)
    assert soft_npv > 0.0

    with pytest.raises(RuntimeError):
        qlSoftBarrierOptionImpliedVolatility(soft_option, soft_npv, process)


def test_two_asset_barrier_option_and_engine():
    _set_eval_date()
    payoff, exercise = _plain_vanilla_objects()

    option = qlTwoAssetBarrierOption(ql.Barrier.UpOut, 120.0, payoff, exercise)
    process1 = _process(0.20, 100.0)
    process2 = _process(0.25, 95.0)
    rho = ql.QuoteHandle(ql.SimpleQuote(0.30))

    engine = qlAnalyticTwoAssetBarrierEngine(process1, process2, rho)

    assert isinstance(option, ql.TwoAssetBarrierOption)
    assert isinstance(engine, ql.AnalyticTwoAssetBarrierEngine)
