import QuantLib as ql

from quantlib_xloil.convertiblebonds import (
    qlBinomialConvertibleEngine,
    qlConvertibleFixedCouponBond,
    qlConvertibleFloatingRateBond,
    qlConvertibleZeroCouponBond,
)
from quantlib_xloil.date import qlDate
from quantlib_xloil.exercise import qlAmericanExercise
from quantlib_xloil.instruments import qlInstrumentNPV, qlInstrumentSetPricingEngine
from quantlib_xloil.options import qBinomialEngineType


def _schedule():
    return ql.Schedule(
        qlDate(2024, 1, 2),
        qlDate(2026, 1, 2),
        ql.Period(ql.Annual),
        ql.TARGET(),
        ql.Unadjusted,
        ql.Unadjusted,
        ql.DateGeneration.Forward,
        False,
    )


def _exercise():
    return qlAmericanExercise(qlDate(2024, 1, 2), qlDate(2026, 1, 2))


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


def test_convertible_bond_constructors():
    exercise = _exercise()
    schedule = _schedule()
    issue_date = qlDate(2024, 1, 2)
    day_counter = ql.Actual365Fixed()

    assert isinstance(
        qlConvertibleZeroCouponBond(
            exercise, 1.0, [], issue_date, 0, day_counter, schedule
        ),
        ql.ConvertibleZeroCouponBond,
    )
    assert isinstance(
        qlConvertibleFixedCouponBond(
            exercise, 1.0, [], issue_date, 0, [0.03], day_counter, schedule
        ),
        ql.ConvertibleFixedCouponBond,
    )
    assert isinstance(
        qlConvertibleFloatingRateBond(
            exercise,
            1.0,
            [],
            issue_date,
            0,
            ql.Euribor6M(),
            0,
            [0.01],
            day_counter,
            schedule,
        ),
        ql.ConvertibleFloatingRateBond,
    )


def test_qlBinomialConvertibleEngine_npv():
    ql.Settings.instance().evaluationDate = qlDate(2024, 1, 2)
    bond = qlConvertibleZeroCouponBond(
        _exercise(),
        1.0,
        [],
        qlDate(2024, 1, 2),
        0,
        ql.Actual365Fixed(),
        _schedule(),
    )
    engine = qlBinomialConvertibleEngine(
        _process(),
        qBinomialEngineType.__wrapped__("CRR"),
        200,
        ql.QuoteHandle(ql.SimpleQuote(0.01)),
    )

    assert qlInstrumentSetPricingEngine(bond, engine) is True
    assert qlInstrumentNPV(bond) > 0.0
