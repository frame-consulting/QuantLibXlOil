import QuantLib as ql
import pytest

from quantlib_xloil import (
    qlBlackConstantVol,
    qlBlackScholesProcess,
    qlBlackScholesMertonProcess,
    qlBlackProcess,
    qlBatesProcess,
    qlExtendedOrnsteinUhlenbeckProcess,
    qlExtOUWithJumpsProcess,
    qlG2ForwardProcess,
    qlG2ForwardProcessSetForwardMeasureTime,
    qlG2Process,
    qlGJRGARCHProcess,
    qlGJRGARCHProcessDividendYield,
    qlGJRGARCHProcessRiskFreeRate,
    qlGJRGARCHProcessS0,
    qlGeometricBrownianMotionProcess,
    qlGeneralizedBlackScholesProcess,
    qlGeneralizedBlackScholesProcessBlackVolatility,
    qlGeneralizedBlackScholesProcessDividendYield,
    qlGeneralizedBlackScholesProcessLocalVolatility,
    qlGeneralizedBlackScholesProcessRiskFreeRate,
    qlGeneralizedBlackScholesProcessStateVariable,
    qlGarmanKohlagenProcess,
    qlGsrProcess,
    qlGsrProcessG,
    qlGsrProcessReversion,
    qlGsrProcessSigma,
    qlGsrProcessSetForwardMeasureTime,
    qlGsrProcessY,
    qlHestonProcess,
    qlHestonProcessDividendYield,
    qlHestonProcessRiskFreeRate,
    qlHestonProcessS0,
    qlHullWhiteForwardProcess,
    qlHullWhiteForwardProcessAlpha,
    qlHullWhiteForwardProcessB,
    qlHullWhiteForwardProcessMT,
    qlHullWhiteForwardProcessSetForwardMeasureTime,
    qlHullWhiteProcess,
    qlKlugeExtOUProcess,
    qlMerton76Process,
    qlOrnsteinUhlenbeckProcess,
    qlOrnsteinUhlenbeckProcessLevel,
    qlOrnsteinUhlenbeckProcessSpeed,
    qlOrnsteinUhlenbeckProcessVolatility,
    qlStochasticProcessArray,
    qlStochasticProcessCovariance,
    qlStochasticProcessDiffusion,
    qlStochasticProcessDrift,
    qlStochasticProcessEvolve,
    qlStochasticProcessExpectation,
    qlStochasticProcessFactors,
    qlStochasticProcessInitialValues,
    qlStochasticProcessSize,
    qlStochasticProcessStdDeviation,
    qlStochasticProcess1DApply,
    qlStochasticProcess1DDiffusion,
    qlStochasticProcess1DDrift,
    qlStochasticProcess1DEvolve,
    qlStochasticProcess1DExpectation,
    qlStochasticProcess1DStdDeviation,
    qlStochasticProcess1DVariance,
    qlStochasticProcess1DX0,
    qlVarianceGammaProcess,
    qlYieldTermStructureHandle,
)

from quantlib_xloil.stochasticprocess import (
    _qGJRGARCHProcessDiscretization,
    _qHestonProcessDiscretization,
)

from quantlib_xloil.daycounters import qDayCounter
from quantlib_xloil.calendars import qCalendar


def _curve(reference_date: ql.Date, rate: float = 0.05) -> ql.YieldTermStructureHandle:
    return qlYieldTermStructureHandle(ql.FlatForward(reference_date, rate, ql.Actual365Fixed()))


def _quote(value: float) -> ql.QuoteHandle:
    return ql.QuoteHandle(ql.SimpleQuote(value))


def test_stochastic_process_base_and_1d_wrappers():
    process = qlGeometricBrownianMotionProcess(100.0, 0.05, 0.20)

    assert qlStochasticProcess1DX0(process) == 100.0
    assert qlStochasticProcess1DDrift(process, 0.0, 100.0) == 5.0
    assert qlStochasticProcess1DDiffusion(process, 0.0, 100.0) == 20.0
    assert qlStochasticProcess1DExpectation(process, 0.0, 100.0, 1.0) == 105.0
    assert qlStochasticProcess1DStdDeviation(process, 0.0, 100.0, 1.0) == 20.0
    assert qlStochasticProcess1DVariance(process, 0.0, 100.0, 1.0) == 400.0
    assert qlStochasticProcess1DEvolve(process, 0.0, 100.0, 1.0, 0.1) == 107.0
    assert qlStochasticProcess1DApply(process, 100.0, 1.0) == 101.0

    assert qlStochasticProcessSize(process) == 1
    assert qlStochasticProcessFactors(process) == 1
    assert qlStochasticProcessInitialValues(process) == [100.0]


def test_stochastic_process_array_wrappers():
    process = qlGeometricBrownianMotionProcess(100.0, 0.05, 0.20)
    correlation = [[1.0, 0.2], [0.2, 1.0]]
    array_process = qlStochasticProcessArray([process, process], correlation)
    x0 = qlStochasticProcessInitialValues(array_process)

    assert qlStochasticProcessSize(array_process) == 2
    assert qlStochasticProcessFactors(array_process) == 2
    assert x0 == [100.0, 100.0]
    assert qlStochasticProcessDrift(array_process, 0.0, x0) == [5.0, 5.0]
    covariance = qlStochasticProcessCovariance(array_process, 0.0, x0, 1.0)
    assert covariance == [[400.0, 80.0], [80.0, 400.0]]
    evolved = qlStochasticProcessEvolve(array_process, 0.0, x0, 1.0, [0.1, 0.2])
    assert evolved[0] == pytest.approx(109.07901546661768)
    assert evolved[1] == pytest.approx(104.01937121034827)


def test_generalized_black_scholes_family_wrappers():
    reference_date = ql.Date(2, 1, 2024)
    calendar = ql.TARGET()
    day_counter = ql.Actual365Fixed()
    risk_free = _curve(reference_date, 0.03)
    dividend = _curve(reference_date, 0.01)
    vol = qlBlackConstantVol(reference_date, calendar, 0.20, day_counter)
    local_vol = ql.LocalVolTermStructureHandle(ql.LocalConstantVol(reference_date, 0.25, day_counter))
    s0 = _quote(100.0)

    gbsm = qlGeneralizedBlackScholesProcess(s0, dividend, risk_free, vol, local_vol)
    assert qlGeneralizedBlackScholesProcessStateVariable(gbsm).value() == 100.0
    assert qlGeneralizedBlackScholesProcessDividendYield(gbsm).discount(reference_date) == dividend.discount(reference_date)
    assert qlGeneralizedBlackScholesProcessRiskFreeRate(gbsm).discount(reference_date) == risk_free.discount(reference_date)
    assert qlGeneralizedBlackScholesProcessBlackVolatility(gbsm).blackVol(reference_date, 100.0) == 0.20
    assert qlGeneralizedBlackScholesProcessLocalVolatility(gbsm) is not None

    assert qlStochasticProcess1DX0(qlBlackScholesProcess(s0, risk_free, vol)) == 100.0
    assert qlStochasticProcess1DX0(qlBlackScholesMertonProcess(s0, dividend, risk_free, vol)) == 100.0
    assert qlStochasticProcess1DX0(qlBlackProcess(s0, risk_free, vol)) == 100.0
    assert qlStochasticProcess1DX0(qlGarmanKohlagenProcess(s0, dividend, risk_free, vol)) == 100.0
    assert qlStochasticProcess1DX0(qlVarianceGammaProcess(s0, dividend, risk_free, 0.2, 0.3, -0.1)) == 100.0
    assert qlStochasticProcess1DX0(qlMerton76Process(s0, dividend, risk_free, vol, _quote(0.1), _quote(-0.05), _quote(0.2))) == 100.0


def test_heston_bates_and_gjrgarch_wrappers():
    reference_date = ql.Date(2, 1, 2024)
    risk_free = _curve(reference_date, 0.03)
    dividend = _curve(reference_date, 0.01)
    s0 = _quote(100.0)

    heston = qlHestonProcess(
        risk_free,
        dividend,
        s0,
        0.04,
        1.5,
        0.04,
        0.30,
        -0.7,
        _qHestonProcessDiscretization("quadraticexponentialmartingale"),
    )
    assert qlHestonProcessS0(heston).value() == 100.0
    assert qlHestonProcessDividendYield(heston).discount(reference_date) == dividend.discount(reference_date)
    assert qlHestonProcessRiskFreeRate(heston).discount(reference_date) == risk_free.discount(reference_date)
    assert qlStochasticProcessSize(heston) == 2

    bates = qlBatesProcess(risk_free, dividend, s0, 0.04, 1.5, 0.04, 0.30, -0.7, 0.10, -0.05, 0.20)
    assert qlHestonProcessS0(bates).value() == 100.0

    gjr = qlGJRGARCHProcess(
        risk_free,
        dividend,
        s0,
        0.04,
        0.10,
        0.05,
        0.90,
        0.10,
        0.20,
    )
    assert qlGJRGARCHProcessS0(gjr).value() == 100.0
    assert qlGJRGARCHProcessDividendYield(gjr).discount(reference_date) == dividend.discount(reference_date)
    assert qlGJRGARCHProcessRiskFreeRate(gjr).discount(reference_date) == risk_free.discount(reference_date)
    assert _qGJRGARCHProcessDiscretization("fulltruncation") == ql.GJRGARCHProcess.FullTruncation


def test_forward_and_gsr_process_wrappers():
    reference_date = ql.Date(2, 1, 2024)
    risk_free = _curve(reference_date, 0.03)

    hwf = qlHullWhiteForwardProcess(risk_free, 0.10, 0.01)
    assert qlHullWhiteForwardProcessAlpha(hwf, 0.5) > 0.0
    assert qlHullWhiteForwardProcessMT(hwf, 0.0, 0.5, 1.0) > 0.0
    assert qlHullWhiteForwardProcessB(hwf, 0.0, 1.0) > 0.0
    assert qlHullWhiteForwardProcessSetForwardMeasureTime(hwf, 1.0) is True

    g2f = qlG2ForwardProcess(0.10, 0.01, 0.20, 0.02, -0.3)
    assert qlG2ForwardProcessSetForwardMeasureTime(g2f, 1.0) is True
    assert qlStochasticProcessSize(g2f) == 2

    g2 = qlG2Process(0.10, 0.01, 0.20, 0.02, -0.3)
    assert qlStochasticProcessSize(g2) == 2

    # GsrProcess::setForwardMeasureTime(Time t) errors and kills Python process occasionally.
    # gsr = qlGsrProcess([0.0, 1.0], [0.01, 0.02, 0.03], [0.03, 0.04, 0.05], 10.0)
    # assert qlGsrProcessSetForwardMeasureTime(gsr, 1.0) is True

    ou = qlOrnsteinUhlenbeckProcess(0.10, 0.20, 1.5, 2.0)
    assert qlOrnsteinUhlenbeckProcessSpeed(ou) == 0.10
    assert qlOrnsteinUhlenbeckProcessVolatility(ou) == 0.20
    assert qlOrnsteinUhlenbeckProcessLevel(ou) == 2.0

    ext_ou = qlExtendedOrnsteinUhlenbeckProcess(0.10, 0.20, 1.5, lambda x: x * x)
    ext_jumps = qlExtOUWithJumpsProcess(ext_ou, 1.0, 0.5, 0.1, 0.2)
    assert qlStochasticProcessSize(ext_ou) == 1
    assert qlStochasticProcessSize(ext_jumps) == 2

    kluge = qlKlugeExtOUProcess(0.30, ext_jumps, ext_ou)
    assert qlStochasticProcessSize(kluge) == 3
