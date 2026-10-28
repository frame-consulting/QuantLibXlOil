import QuantLib as ql

from quantlib_xloil.varianceswaps import (
    qlMCVarianceSwapEngine,
    qlVarianceSwap,
    qlVarianceSwapVariance,
)
from quantlib_xloil.date import qlDate
from quantlib_xloil.fra import qPosition


def test_variance_swap_constructor_and_position_converter():
    start_date = qlDate(2025, 1, 2)
    maturity_date = qlDate(2025, 4, 2)

    variance_swap = qlVarianceSwap(
        qPosition.__wrapped__("long"),
        0.04,
        50000.0,
        start_date,
        maturity_date,
    )

    assert isinstance(variance_swap, ql.VarianceSwap)
    assert variance_swap.position() == ql.Position.Long
    assert variance_swap.strike() == 0.04
    assert variance_swap.notional() == 50000.0


def test_mc_variance_swap_engine_and_fair_variance():
    original_eval = ql.Settings.instance().evaluationDate
    today = qlDate(2025, 1, 2)
    try:
        maturity = today + 90
        ql.Settings.instance().evaluationDate = today
        day_counter = ql.Actual365Fixed()
        volatility = ql.BlackVarianceCurve(
            today, [today + 37, maturity], [0.1, 0.2], day_counter, True
        )
        process = ql.BlackScholesMertonProcess(
            ql.QuoteHandle(ql.SimpleQuote(100.0)),
            ql.YieldTermStructureHandle(ql.FlatForward(today, 0.0, day_counter)),
            ql.YieldTermStructureHandle(ql.FlatForward(today, 0.05, day_counter)),
            ql.BlackVolTermStructureHandle(volatility),
        )
        engine = qlMCVarianceSwapEngine(
            process,
            "pseudorandom",
            time_steps_per_year=250,
            required_samples=1023,
            seed=42,
        )
        variance_swap = qlVarianceSwap(ql.Position.Long, 0.04, 50000.0, today, maturity)
        variance_swap.setPricingEngine(engine)

        assert abs(qlVarianceSwapVariance(variance_swap) - 0.04) < 3.0e-4
    finally:
        ql.Settings.instance().evaluationDate = original_eval
