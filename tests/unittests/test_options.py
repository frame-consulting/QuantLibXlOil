import QuantLib as ql
import pytest

from quantlib_xloil import (
    qlBachelierCalculator,
    qlBachelierCalculatorAlpha,
    qlBachelierCalculatorBeta,
    qlBachelierCalculatorDelta,
    qlBachelierCalculatorDeltaForward,
    qlBachelierCalculatorDividendRho,
    qlBachelierCalculatorElasticity,
    qlBachelierCalculatorElasticityForward,
    qlBachelierCalculatorGamma,
    qlBachelierCalculatorGammaForward,
    qlBachelierCalculatorITMAssetProbability,
    qlBachelierCalculatorITMCashProbability,
    qlBachelierCalculatorRho,
    qlBachelierCalculatorStrikeGamma,
    qlBachelierCalculatorStrikeSensitivity,
    qlBachelierCalculatorTheta,
    qlBachelierCalculatorThetaPerDay,
    qlBachelierCalculatorValue,
    qlBachelierCalculatorVanna,
    qlBachelierCalculatorVega,
    qlBachelierCalculatorVolga,
    qlBlackCalculator,
    qlBlackCalculatorAlpha,
    qlBlackCalculatorBeta,
    qlBlackCalculatorDelta,
    qlBlackCalculatorDeltaForward,
    qlBlackCalculatorDividendRho,
    qlBlackCalculatorElasticity,
    qlBlackCalculatorElasticityForward,
    qlBlackCalculatorGamma,
    qlBlackCalculatorGammaForward,
    qlBlackCalculatorITMAssetProbability,
    qlBlackCalculatorITMCashProbability,
    qlBlackCalculatorRho,
    qlBlackCalculatorStrikeGamma,
    qlBlackCalculatorStrikeSensitivity,
    qlBlackCalculatorTheta,
    qlBlackCalculatorThetaPerDay,
    qlBlackCalculatorValue,
    qlBlackCalculatorVanna,
    qlBlackCalculatorVega,
    qlBlackCalculatorVolga,
    qlDeltaVolQuote,
    qlDeltaVolQuoteAtm,
    qlDeltaVolQuoteAtmType,
    qlDeltaVolQuoteDelta,
    qlDeltaVolQuoteDeltaType,
    qlDeltaVolQuoteIsValid,
    qlDeltaVolQuoteMaturity,
    qlDeltaVolQuoteValue,
    qlAnalyticCEVEngine,
    qlAnalyticGJRGARCHEngine,
    qlAnalyticH1HWEngine,
    qlBatesEngine,
    qlBatesModel,
    qlFFTVarianceGammaEngine,
    qlGJRGARCHModel,
    qlAnalyticHestonEngine,
    qlAnalyticHestonEngineIntegrationAndersenPiterbargIntegrationLimit,
    qlAnalyticHestonEngineIntegrationGaussLaguerre,
    qlAnalyticHestonEngineIntegrationIsAdaptive,
    qlAnalyticHestonEngineIntegrationNumberOfEvaluations,
    qlAnalyticHestonEngineNumberOfEvaluations,
    qlAnalyticHestonHullWhiteEngine,
    qlAnalyticHestonEngineOptimalAlpha,
    qlAnalyticHestonEngineOptimalAlphaBounds,
    qlAnalyticHestonEngineOptimalAlphaValue,
    qlAnalyticHestonForwardEuropeanEngine,
    qlAnalyticPDFHestonEngine,
    qlAnalyticPTDHestonEngine,
    qlAnalyticDigitalAmericanEngine,
    qlAnalyticEuropeanMargrabeEngine,
    qlAnalyticEuropeanEngine,
    qlBaroneAdesiWhaleyApproximationEngine,
    qlBjerksundStenslandApproximationEngine,
    qlBinomialVanillaEngine,
    qlBlackConstantVol,
    qlCOSHestonEngine,
    qlComplexChooserOption,
    qlCompoundOption,
    qlDate,
    qlFdBatesVanillaEngine,
    qlFdBlackScholesShoutEngine,
    qlFdBlackScholesVanillaEngine,
    qlFdCEVVanillaEngine,
    qlFdHestonHullWhiteVanillaEngine,
    qlFdHestonVanillaEngine,
    qlFdOrnsteinUhlenbeckVanillaEngine,
    qlFdSabrVanillaEngine,
    qlFdmQuantoHelper,
    qlFdmSchemeDesc,
    qlEuropeanExercise,
    qlEuropeanOption,
    qlExponentialFittingHestonEngine,
    qlFlatForward,
    qlForwardVanillaOption,
    qlGeneralizedBlackScholesProcess,
    qlHestonModel,
    qlHestonModelHandle,
    qlHestonModelHandleCurrentLink,
    qlHestonModelKappa,
    qlHestonModelProcess,
    qlHestonModelRho,
    qlHestonModelSigma,
    qlHestonModelTheta,
    qlHestonModelV0,
    qlHolderExtensibleOption,
    qlInstrumentNPV,
    qlInstrumentSetPricingEngine,
    qlJuQuadraticApproximationEngine,
    qlMCAmericanEngine,
    qlMCDigitalEngine,
    qlMCEuropeanEngine,
    qlOneAssetOptionDelta,
    qlOneAssetOptionGamma,
    qlOneAssetOptionITMCashProbability,
    qlOptionExercise,
    qlOptionPayoff,
    qlPlainVanillaPayoff,
    qlPiecewiseTimeDependentHestonModel,
    qlPiecewiseTimeDependentHestonModelKappa,
    qlPiecewiseTimeDependentHestonModelRho,
    qlPiecewiseTimeDependentHestonModelS0,
    qlPiecewiseTimeDependentHestonModelSigma,
    qlPiecewiseTimeDependentHestonModelTheta,
    qlPiecewiseTimeDependentHestonModelV0,
    qlQuantoForwardVanillaOption,
    qlQuantoVanillaOption,
    qlSimpleChooserOption,
    qlTwoAssetCorrelationOption,
    qlVanillaOption,
    qlVanillaOptionImpliedVolatility,
    qlWriterExtensibleOption,
    qlQdFpAmericanEngine,
    qlQdFpAmericanEngineAccurateScheme,
    qlQdFpAmericanEngineFastScheme,
    qlQdFpAmericanEngineHighPrecisionScheme,
    qlQdFpLegendreScheme,
    qlQdFpLegendreTanhSinhScheme,
    qlQdFpTanhSinhIterationScheme,
    qlQdPlusAmericanEngine,
    qlVarianceGammaEngine,
)
from quantlib_xloil.options import (
    _qAnalyticHestonComplexLogFormula,
    _qAnalyticPTDHestonComplexLogFormula,
    _qAnalyticHestonEngineIntegration,
    _qBinomialEngineType,
    _qDeltaVolQuoteAtmType,
    _qDeltaVolQuoteDeltaType,
    _qFdBlackScholesCashDividendModel,
    _qFdmSchemeType,
    _qLsmBasisSystemPolynomialType,
    _qMCTraits,
    _qQdFpFixedPointEquation,
    _qQdPlusSolverType,
)
from quantlib_xloil.payoffs import (
    _qOptionType,
)


def _set_eval_date() -> None:
    ql.Settings.instance().evaluationDate = qlDate(2024, 1, 2)


def _process(volatility: float = 0.20):
    reference_date = qlDate(2024, 1, 2)
    day_counter = ql.Actual365Fixed()

    spot = ql.QuoteHandle(ql.SimpleQuote(100.0))
    risk_free = qlFlatForward(reference_date, 0.03, day_counter)
    dividend = qlFlatForward(reference_date, 0.01, day_counter)
    black_vol = qlBlackConstantVol(reference_date, ql.TARGET(), volatility, day_counter)

    return qlGeneralizedBlackScholesProcess(spot, dividend, risk_free, black_vol)


def _heston_process_and_model():
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
    model = qlHestonModel(process)
    return process, model, spot, risk_free, dividend


def _vanilla_objects():
    payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    exercise = qlEuropeanExercise(qlDate(2025, 1, 2))
    option = qlEuropeanOption(payoff, exercise)
    return payoff, exercise, option


def test_option_engine_and_greeks_wrappers():
    _set_eval_date()
    payoff, exercise, option = _vanilla_objects()
    process = _process(0.20)

    engine = qlAnalyticEuropeanEngine(process)
    assert qlInstrumentSetPricingEngine(option, engine) is True

    npv = qlInstrumentNPV(option)
    assert npv > 0.0

    assert isinstance(qlOptionPayoff(option), ql.Payoff)
    assert qlOptionExercise(option).date(0) == exercise.date(0)
    assert qlOneAssetOptionDelta(option) > 0.0
    assert qlOneAssetOptionGamma(option) > 0.0
    assert 0.0 <= qlOneAssetOptionITMCashProbability(option) <= 1.0


def test_vanilla_option_implied_volatility_wrapper():
    _set_eval_date()
    _, _, option = _vanilla_objects()
    process = _process(0.25)

    engine = qlAnalyticEuropeanEngine(process)
    qlInstrumentSetPricingEngine(option, engine)
    target = option.NPV()

    implied = qlVanillaOptionImpliedVolatility(option, target, process)
    assert implied == pytest.approx(0.25, rel=1e-3)


def test_option_constructor_family_wrappers():
    _set_eval_date()
    payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    payoff2 = qlPlainVanillaPayoff(ql.Option.Put, 95.0)

    exercise = qlEuropeanExercise(qlDate(2025, 1, 2))
    exercise2 = qlEuropeanExercise(qlDate(2026, 1, 2))

    assert isinstance(qlVanillaOption(payoff, exercise), ql.VanillaOption)
    assert isinstance(
        qlForwardVanillaOption(1.0, qlDate(2024, 7, 2), payoff, exercise),
        ql.ForwardVanillaOption,
    )
    assert isinstance(qlQuantoVanillaOption(payoff, exercise), ql.QuantoVanillaOption)
    assert isinstance(
        qlQuantoForwardVanillaOption(1.0, qlDate(2024, 7, 2), payoff, exercise),
        ql.QuantoForwardVanillaOption,
    )
    assert isinstance(
        qlCompoundOption(payoff, exercise, payoff2, exercise2), ql.CompoundOption
    )
    assert isinstance(
        qlSimpleChooserOption(qlDate(2024, 7, 2), 100.0, exercise),
        ql.SimpleChooserOption,
    )
    assert isinstance(
        qlComplexChooserOption(qlDate(2024, 7, 2), 100.0, 95.0, exercise, exercise2),
        ql.ComplexChooserOption,
    )
    assert isinstance(
        qlHolderExtensibleOption(
            _qOptionType("CALL"), 1.5, qlDate(2026, 1, 2), 105.0, payoff, exercise
        ),
        ql.HolderExtensibleOption,
    )
    assert isinstance(
        qlWriterExtensibleOption(payoff, exercise, payoff2, exercise2),
        ql.WriterExtensibleOption,
    )
    assert isinstance(
        qlTwoAssetCorrelationOption(_qOptionType("PUT"), 100.0, 95.0, exercise),
        ql.TwoAssetCorrelationOption,
    )


def test_mc_and_binomial_engine_factory_wrappers():
    _set_eval_date()
    process = _process(0.20)

    binomial = qlBinomialVanillaEngine(process, "crr", 100)
    mc_eur = qlMCEuropeanEngine(process, "pr", time_steps=10, required_samples=16)
    mc_amer = qlMCAmericanEngine(process, "ld", time_steps=10, required_samples=16)
    mc_dig = qlMCDigitalEngine(process, "pr", time_steps=10, required_samples=16)

    assert isinstance(binomial, ql.PricingEngine)
    assert isinstance(mc_eur, ql.PricingEngine)
    assert isinstance(mc_amer, ql.PricingEngine)
    assert isinstance(mc_dig, ql.PricingEngine)


def test_option_converters_and_margrabe_engine_wrapper():
    _set_eval_date()
    assert _qBinomialEngineType("TIAN") == "tian"
    assert _qMCTraits("ld") == "lowdiscrepancy"
    assert _qLsmBasisSystemPolynomialType("legendre") == ql.LsmBasisSystem.Legendre

    reference_date = qlDate(2024, 1, 2)
    exercise = qlEuropeanExercise(qlDate(2025, 1, 2))

    p1 = qlGeneralizedBlackScholesProcess(
        ql.QuoteHandle(ql.SimpleQuote(100.0)),
        qlFlatForward(reference_date, 0.01),
        qlFlatForward(reference_date, 0.03),
        qlBlackConstantVol(reference_date, ql.TARGET(), 0.20, ql.Actual365Fixed()),
    )
    p2 = qlGeneralizedBlackScholesProcess(
        ql.QuoteHandle(ql.SimpleQuote(90.0)),
        qlFlatForward(reference_date, 0.01),
        qlFlatForward(reference_date, 0.03),
        qlBlackConstantVol(reference_date, ql.TARGET(), 0.25, ql.Actual365Fixed()),
    )

    margrabe = ql.MargrabeOption(1, 1, exercise)
    margrabe_engine = qlAnalyticEuropeanMargrabeEngine(p1, p2, 0.3)
    qlInstrumentSetPricingEngine(margrabe, margrabe_engine)
    assert margrabe.NPV() >= 0.0


def test_analytic_american_engine_wrappers():
    _set_eval_date()
    reference_date = qlDate(2024, 1, 2)
    process = _process(0.20)

    american_exercise = ql.AmericanExercise(reference_date, qlDate(2025, 1, 2))
    vanilla_payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    vanilla_option = qlVanillaOption(vanilla_payoff, american_exercise)

    baw = qlBaroneAdesiWhaleyApproximationEngine(process)
    bjs = qlBjerksundStenslandApproximationEngine(process)
    ju = qlJuQuadraticApproximationEngine(process)

    for engine in (baw, bjs, ju):
        assert qlInstrumentSetPricingEngine(vanilla_option, engine) is True
        assert qlInstrumentNPV(vanilla_option) > 0.0

    digital_payoff = ql.CashOrNothingPayoff(ql.Option.Call, 100.0, 10.0)
    digital_option = qlVanillaOption(digital_payoff, american_exercise)
    digital_engine = qlAnalyticDigitalAmericanEngine(process)

    assert qlInstrumentSetPricingEngine(digital_option, digital_engine) is True
    assert qlInstrumentNPV(digital_option) >= 0.0


def test_heston_model_and_handle_wrappers():
    _set_eval_date()
    process, model, _, _, _ = _heston_process_and_model()

    model_handle = qlHestonModelHandle(model)
    linked = qlHestonModelHandleCurrentLink(model_handle)

    assert isinstance(model, ql.HestonModel)
    assert isinstance(model_handle, ql.HestonModelHandle)
    assert isinstance(linked, ql.HestonModel)
    assert qlHestonModelTheta(model) == pytest.approx(0.04)
    assert qlHestonModelKappa(model) == pytest.approx(1.50)
    assert qlHestonModelSigma(model) == pytest.approx(0.25)
    assert qlHestonModelRho(model) == pytest.approx(-0.60)
    assert qlHestonModelV0(model) == pytest.approx(0.04)
    assert isinstance(qlHestonModelProcess(model), ql.HestonProcess)
    assert isinstance(process, ql.HestonProcess)


def test_heston_analytic_engine_and_helpers_wrappers():
    _set_eval_date()
    process, model, _, _, _ = _heston_process_and_model()

    payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    exercise = qlEuropeanExercise(qlDate(2025, 1, 2))
    option = qlEuropeanOption(payoff, exercise)

    ap_limit = qlAnalyticHestonEngineIntegrationAndersenPiterbargIntegrationLimit(
        1.0, 1.0e-8, 0.04, 1.0
    )
    assert ap_limit > 0.0

    engine_default = qlAnalyticHestonEngine(model, integration_order=64)
    engine_tol = qlAnalyticHestonEngine(
        model, rel_tolerance=1.0e-4, max_evaluations=2000
    )
    engine_custom = qlAnalyticHestonEngine(
        model,
        complex_log_formula=_qAnalyticHestonComplexLogFormula("GATHERAL"),
        integration=_qAnalyticHestonEngineIntegration("GAUSS_LAGUERRE"),
        andersen_piterbarg_epsilon=1.0e-8,
    )

    alpha = qlAnalyticHestonEngineOptimalAlpha(1.0, engine_default)
    alpha_value = qlAnalyticHestonEngineOptimalAlphaValue(alpha, 100.0)
    alpha_bounds = qlAnalyticHestonEngineOptimalAlphaBounds(alpha, 100.0)

    assert isinstance(alpha, ql.AnalyticHestonEngine_OptimalAlpha)
    assert alpha_bounds[0] < alpha_bounds[1]
    assert alpha_bounds[0] <= alpha_value <= alpha_bounds[1]

    for engine in (
        engine_default,
        engine_tol,
        engine_custom,
        qlCOSHestonEngine(model, 16.0, 128),
        qlExponentialFittingHestonEngine(model),
        qlAnalyticPDFHestonEngine(model),
    ):
        assert qlInstrumentSetPricingEngine(option, engine) is True
        assert qlInstrumentNPV(option) > 0.0

    assert qlAnalyticHestonEngineNumberOfEvaluations(engine_default) >= 0


def test_heston_hull_white_engine_wrappers():
    _set_eval_date()
    _, model, _, risk_free, _ = _heston_process_and_model()

    hull_white_model = ql.HullWhite(risk_free, 0.03, 0.01)

    payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    exercise = qlEuropeanExercise(qlDate(2025, 1, 2))
    option = qlEuropeanOption(payoff, exercise)

    engine_order = qlAnalyticHestonHullWhiteEngine(
        model, hull_white_model, integration_order=96
    )
    engine_tol = qlAnalyticHestonHullWhiteEngine(
        model, hull_white_model, rel_tolerance=1.0e-4, max_evaluations=2000
    )

    h1_engine_order = qlAnalyticH1HWEngine(
        model, hull_white_model, rho_sr=0.20, integration_order=96
    )
    h1_engine_tol = qlAnalyticH1HWEngine(
        model,
        hull_white_model,
        rho_sr=0.20,
        rel_tolerance=1.0e-4,
        max_evaluations=2000,
    )

    for engine in (engine_order, engine_tol, h1_engine_order, h1_engine_tol):
        assert qlInstrumentSetPricingEngine(option, engine) is True
        assert qlInstrumentNPV(option) > 0.0


def test_piecewise_time_dependent_heston_and_forward_engine_wrappers():
    _set_eval_date()
    process, model, spot, risk_free, dividend = _heston_process_and_model()

    time_grid = ql.TimeGrid([0.0, 2.0], 2)
    theta = ql.ConstantParameter(0.04, ql.PositiveConstraint())
    kappa = ql.ConstantParameter(1.50, ql.PositiveConstraint())
    sigma = ql.ConstantParameter(0.25, ql.PositiveConstraint())
    rho = ql.ConstantParameter(-0.60, ql.BoundaryConstraint(-1.0, 1.0))

    ptd_model = qlPiecewiseTimeDependentHestonModel(
        risk_free, dividend, spot, 0.04, theta, kappa, sigma, rho, time_grid
    )

    assert qlPiecewiseTimeDependentHestonModelTheta(ptd_model, 0.5) == pytest.approx(
        0.04
    )
    assert qlPiecewiseTimeDependentHestonModelKappa(ptd_model, 0.5) == pytest.approx(
        1.50
    )
    assert qlPiecewiseTimeDependentHestonModelSigma(ptd_model, 0.5) == pytest.approx(
        0.25
    )
    assert qlPiecewiseTimeDependentHestonModelRho(ptd_model, 0.5) == pytest.approx(
        -0.60
    )
    assert qlPiecewiseTimeDependentHestonModelV0(ptd_model) == pytest.approx(0.04)
    assert qlPiecewiseTimeDependentHestonModelS0(ptd_model) == pytest.approx(100.0)

    payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    exercise = qlEuropeanExercise(qlDate(2025, 1, 2))
    option = qlEuropeanOption(payoff, exercise)

    ptd_engine_default = qlAnalyticPTDHestonEngine(ptd_model, integration_order=64)
    ptd_engine_tol = qlAnalyticPTDHestonEngine(
        ptd_model, rel_tolerance=1.0e-6, max_evaluations=200
    )
    ptd_engine_custom = qlAnalyticPTDHestonEngine(
        ptd_model,
        complex_log_formula=_qAnalyticPTDHestonComplexLogFormula("GATHERAL"),
        integration=_qAnalyticHestonEngineIntegration("GAUSS_LAGUERRE"),
        andersen_piterbarg_epsilon=1.0e-8,
    )

    for engine in (ptd_engine_default, ptd_engine_tol, ptd_engine_custom):
        assert qlInstrumentSetPricingEngine(option, engine) is True
        assert qlInstrumentNPV(option) > 0.0

    forward_option = qlForwardVanillaOption(1.0, qlDate(2024, 7, 2), payoff, exercise)
    forward_engine = qlAnalyticHestonForwardEuropeanEngine(process, 64)
    assert qlInstrumentSetPricingEngine(forward_option, forward_engine) is True
    assert qlInstrumentNPV(forward_option) > 0.0


def test_fdm_helpers_and_fd_engine_wrappers():
    _set_eval_date()
    reference_date = qlDate(2024, 1, 2)
    day_counter = ql.Actual365Fixed()

    assert _qFdmSchemeType("DOUGLAS") == ql.FdmSchemeDesc.DouglasType
    assert (
        _qFdBlackScholesCashDividendModel("SPOT") == ql.FdBlackScholesVanillaEngine.Spot
    )

    scheme_douglas = qlFdmSchemeDesc("DOUGLAS", theta=0.5, mu=0.0)
    scheme_hund = qlFdmSchemeDesc("HUNDSDORFER", theta=0.5, mu=0.0)

    assert isinstance(scheme_douglas, ql.FdmSchemeDesc)
    assert scheme_douglas.type == ql.FdmSchemeDesc.DouglasType
    assert scheme_hund.type == ql.FdmSchemeDesc.HundsdorferType

    spot = ql.QuoteHandle(ql.SimpleQuote(100.0))
    risk_free_handle = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.03, day_counter)
    )
    dividend_handle = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.01, day_counter)
    )
    fx_vol = ql.BlackConstantVol(reference_date, ql.TARGET(), 0.15, day_counter)
    fx_vol_handle = ql.BlackVolTermStructureHandle(fx_vol)
    black_vol = ql.BlackConstantVol(reference_date, ql.TARGET(), 0.20, day_counter)

    process = ql.GeneralizedBlackScholesProcess(
        spot,
        dividend_handle,
        risk_free_handle,
        ql.BlackVolTermStructureHandle(black_vol),
    )

    quanto = qlFdmQuantoHelper(
        risk_free_handle,
        dividend_handle,
        fx_vol_handle,
        0.25,
        1.10,
    )
    assert isinstance(quanto, ql.FdmQuantoHelper)

    option = qlEuropeanOption(
        qlPlainVanillaPayoff(ql.Option.Call, 100.0),
        qlEuropeanExercise(qlDate(2025, 1, 2)),
    )

    bs_fd = qlFdBlackScholesVanillaEngine(
        process,
        quanto_helper=quanto,
        t_grid=60,
        x_grid=80,
        scheme_desc=scheme_douglas,
        cash_dividend_model=_qFdBlackScholesCashDividendModel("SPOT"),
    )
    bs_shout_fd = qlFdBlackScholesShoutEngine(
        process, t_grid=60, x_grid=80, scheme_desc=scheme_douglas
    )

    ou_process = ql.OrnsteinUhlenbeckProcess(0.20, 0.10, 0.03)
    ou_fd = qlFdOrnsteinUhlenbeckVanillaEngine(
        ou_process,
        risk_free_handle,
        t_grid=40,
        x_grid=80,
        epsilon=1.0e-4,
        scheme_desc=scheme_douglas,
    )

    bates_process = ql.BatesProcess(
        risk_free_handle,
        dividend_handle,
        spot,
        0.04,
        1.50,
        0.04,
        0.25,
        -0.50,
        0.10,
        0.20,
        0.10,
    )
    bates_model = ql.BatesModel(bates_process)
    bates_fd = qlFdBatesVanillaEngine(
        bates_model, t_grid=30, x_grid=50, v_grid=25, scheme_desc=scheme_hund
    )

    heston_model = qlHestonModel(
        ql.HestonProcess(
            risk_free_handle, dividend_handle, spot, 0.04, 1.50, 0.04, 0.25, -0.50
        )
    )
    heston_fd = qlFdHestonVanillaEngine(
        heston_model,
        quanto_helper=quanto,
        t_grid=30,
        x_grid=50,
        v_grid=25,
        scheme_desc=scheme_hund,
    )

    cev_fd = qlFdCEVVanillaEngine(
        100.0,
        0.30,
        0.70,
        risk_free_handle,
        t_grid=30,
        x_grid=200,
        scheme_desc=scheme_douglas,
    )
    sabr_fd = qlFdSabrVanillaEngine(
        100.0,
        0.20,
        0.50,
        0.30,
        -0.20,
        risk_free_handle,
        t_grid=30,
        f_grid=120,
        x_grid=40,
        scheme_desc=scheme_hund,
    )

    hull_white_process = ql.HullWhiteProcess(risk_free_handle, 0.03, 0.01)
    heston_hw_fd = qlFdHestonHullWhiteVanillaEngine(
        heston_model,
        hull_white_process,
        corr_equity_short_rate=0.20,
        t_grid=20,
        x_grid=40,
        v_grid=20,
        r_grid=10,
        scheme_desc=scheme_hund,
    )

    for engine in (
        bs_fd,
        bs_shout_fd,
        bates_fd,
        heston_fd,
        cev_fd,
        sabr_fd,
        heston_hw_fd,
    ):
        assert qlInstrumentSetPricingEngine(option, engine) is True
        assert qlInstrumentNPV(option) == pytest.approx(option.NPV())

    assert qlInstrumentSetPricingEngine(option, ou_fd) is True
    assert qlInstrumentNPV(option) >= 0.0


def test_qd_american_engine_wrappers():
    _set_eval_date()
    process = _process(0.20)

    assert _qQdPlusSolverType("HALLEY") == ql.QdPlusAmericanEngine.Halley
    assert _qQdFpFixedPointEquation("FP_A") == ql.QdFpAmericanEngine.FP_A

    reference_date = qlDate(2024, 1, 2)
    exercise = ql.AmericanExercise(reference_date, qlDate(2025, 1, 2))
    option = qlVanillaOption(qlPlainVanillaPayoff(ql.Option.Put, 100.0), exercise)

    qd_plus = qlQdPlusAmericanEngine(
        process,
        interpolation_points=8,
        solver_type=_qQdPlusSolverType("HALLEY"),
        eps=1.0e-6,
        max_iter=100,
    )
    assert qlInstrumentSetPricingEngine(option, qd_plus) is True
    assert qlInstrumentNPV(option) > 0.0

    scheme_legendre = qlQdFpLegendreScheme(10, 10, 30, 10)
    scheme_legendre_tanh = qlQdFpLegendreTanhSinhScheme(10, 30, 40, 1.0e-8)
    scheme_tanh = qlQdFpTanhSinhIterationScheme(30, 40, 1.0e-8)

    assert isinstance(scheme_legendre, ql.QdFpLegendreScheme)
    assert isinstance(scheme_legendre_tanh, ql.QdFpLegendreTanhSinhScheme)
    assert isinstance(scheme_tanh, ql.QdFpTanhSinhIterationScheme)

    for scheme in (
        scheme_legendre,
        scheme_legendre_tanh,
        scheme_tanh,
        qlQdFpAmericanEngineFastScheme(),
        qlQdFpAmericanEngineAccurateScheme(),
        qlQdFpAmericanEngineHighPrecisionScheme(),
    ):
        qd_fp = qlQdFpAmericanEngine(process, scheme, _qQdFpFixedPointEquation("AUTO"))
        assert qlInstrumentSetPricingEngine(option, qd_fp) is True
        assert qlInstrumentNPV(option) > 0.0


def test_analytic_cev_bates_vg_and_gjrgarch_wrappers():
    _set_eval_date()
    reference_date = qlDate(2024, 1, 2)
    day_counter = ql.Actual365Fixed()

    spot = ql.QuoteHandle(ql.SimpleQuote(100.0))
    risk_free = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.03, day_counter)
    )
    dividend = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.01, day_counter)
    )

    option = qlEuropeanOption(
        qlPlainVanillaPayoff(ql.Option.Call, 100.0),
        qlEuropeanExercise(qlDate(2025, 1, 2)),
    )

    cev_engine = qlAnalyticCEVEngine(100.0, 0.30, 0.70, risk_free)
    assert qlInstrumentSetPricingEngine(option, cev_engine) is True
    assert qlInstrumentNPV(option) > 0.0

    bates_process = ql.BatesProcess(
        risk_free,
        dividend,
        spot,
        0.04,
        1.50,
        0.04,
        0.25,
        -0.50,
        0.10,
        0.20,
        0.10,
    )
    bates_model = qlBatesModel(bates_process)
    assert isinstance(bates_model, ql.BatesModel)

    bates_engine_order = qlBatesEngine(bates_model, integration_order=96)
    bates_engine_tol = qlBatesEngine(
        bates_model, rel_tolerance=1.0e-4, max_evaluations=2000
    )
    for engine in (bates_engine_order, bates_engine_tol):
        assert qlInstrumentSetPricingEngine(option, engine) is True
        assert qlInstrumentNPV(option) > 0.0

    vg_process = ql.VarianceGammaProcess(spot, dividend, risk_free, 0.20, 0.20, 0.0)
    vg_engine = qlVarianceGammaEngine(vg_process)
    vg_fft_engine = qlFFTVarianceGammaEngine(vg_process, 0.001)

    for engine in (vg_engine, vg_fft_engine):
        assert qlInstrumentSetPricingEngine(option, engine) is True
        assert qlInstrumentNPV(option) > 0.0

    gjr_process = ql.GJRGARCHProcess(
        risk_free,
        dividend,
        spot,
        0.04,
        0.01,
        0.10,
        0.80,
        0.05,
        0.0,
        252.0,
        ql.GJRGARCHProcess.FullTruncation,
    )
    gjr_model = qlGJRGARCHModel(gjr_process)
    assert isinstance(gjr_model, ql.GJRGARCHModel)

    gjr_engine = qlAnalyticGJRGARCHEngine(gjr_model)
    assert qlInstrumentSetPricingEngine(option, gjr_engine) is True
    assert qlInstrumentNPV(option) > 0.0


def test_calculators_and_delta_vol_quote_wrappers():
    _set_eval_date()

    payoff = qlPlainVanillaPayoff(ql.Option.Call, 100.0)
    black = qlBlackCalculator(payoff, 102.0, 0.20, 0.97)
    bachelier = qlBachelierCalculator(payoff, 102.0, 0.20, 0.97)

    assert qlBlackCalculatorValue(black) > 0.0
    assert qlBlackCalculatorDelta(black, 100.0) > 0.0
    assert qlBlackCalculatorGamma(black, 100.0) >= 0.0
    assert qlBlackCalculatorVega(black, 1.0) >= 0.0
    assert qlBlackCalculatorTheta(black, 100.0, 1.0) == pytest.approx(
        black.theta(100.0, 1.0)
    )
    assert qlBlackCalculatorThetaPerDay(black, 100.0, 1.0) == pytest.approx(
        black.thetaPerDay(100.0, 1.0)
    )
    assert qlBlackCalculatorRho(black, 1.0) == pytest.approx(black.rho(1.0))
    assert qlBlackCalculatorDividendRho(black, 1.0) == pytest.approx(
        black.dividendRho(1.0)
    )
    assert qlBlackCalculatorDeltaForward(black) == pytest.approx(black.deltaForward())
    assert qlBlackCalculatorGammaForward(black) == pytest.approx(black.gammaForward())
    assert qlBlackCalculatorElasticity(black, 100.0) == pytest.approx(
        black.elasticity(100.0)
    )
    assert qlBlackCalculatorElasticityForward(black) == pytest.approx(
        black.elasticityForward()
    )
    assert qlBlackCalculatorITMCashProbability(black) == pytest.approx(
        black.itmCashProbability()
    )
    assert qlBlackCalculatorITMAssetProbability(black) == pytest.approx(
        black.itmAssetProbability()
    )
    assert qlBlackCalculatorStrikeSensitivity(black) == pytest.approx(
        black.strikeSensitivity()
    )
    assert qlBlackCalculatorStrikeGamma(black) == pytest.approx(black.strikeGamma())
    assert qlBlackCalculatorAlpha(black) == pytest.approx(black.alpha())
    assert qlBlackCalculatorVanna(black, 100.0, 1.0) == pytest.approx(
        black.vanna(100.0, 1.0)
    )
    assert qlBlackCalculatorVolga(black, 1.0) == pytest.approx(black.volga(1.0))
    assert qlBlackCalculatorBeta(black) == pytest.approx(black.beta())

    assert qlBachelierCalculatorValue(bachelier) > 0.0
    assert qlBachelierCalculatorDelta(bachelier, 100.0) > 0.0
    assert qlBachelierCalculatorGamma(bachelier, 100.0) >= 0.0
    assert qlBachelierCalculatorVega(bachelier, 1.0) >= 0.0
    assert qlBachelierCalculatorTheta(bachelier, 100.0, 1.0) == pytest.approx(
        bachelier.theta(100.0, 1.0)
    )
    assert qlBachelierCalculatorThetaPerDay(bachelier, 100.0, 1.0) == pytest.approx(
        bachelier.thetaPerDay(100.0, 1.0)
    )
    assert qlBachelierCalculatorRho(bachelier, 1.0) == pytest.approx(bachelier.rho(1.0))
    assert qlBachelierCalculatorDividendRho(bachelier, 1.0) == pytest.approx(
        bachelier.dividendRho(1.0)
    )
    assert qlBachelierCalculatorDeltaForward(bachelier) == pytest.approx(
        bachelier.deltaForward()
    )
    assert qlBachelierCalculatorGammaForward(bachelier) == pytest.approx(
        bachelier.gammaForward()
    )
    assert qlBachelierCalculatorElasticity(bachelier, 100.0) == pytest.approx(
        bachelier.elasticity(100.0)
    )
    assert qlBachelierCalculatorElasticityForward(bachelier) == pytest.approx(
        bachelier.elasticityForward()
    )
    assert qlBachelierCalculatorITMCashProbability(bachelier) == pytest.approx(
        bachelier.itmCashProbability()
    )
    assert qlBachelierCalculatorITMAssetProbability(bachelier) == pytest.approx(
        bachelier.itmAssetProbability()
    )
    assert qlBachelierCalculatorStrikeSensitivity(bachelier) == pytest.approx(
        bachelier.strikeSensitivity()
    )
    assert qlBachelierCalculatorStrikeGamma(bachelier) == pytest.approx(
        bachelier.strikeGamma()
    )
    assert qlBachelierCalculatorAlpha(bachelier) == pytest.approx(bachelier.alpha())
    assert qlBachelierCalculatorVanna(bachelier, 1.0) == pytest.approx(
        bachelier.vanna(1.0)
    )
    assert qlBachelierCalculatorVolga(bachelier, 1.0) == pytest.approx(
        bachelier.volga(1.0)
    )
    assert qlBachelierCalculatorBeta(bachelier) == pytest.approx(bachelier.beta())

    assert _qDeltaVolQuoteDeltaType("SPOT") == ql.DeltaVolQuote.Spot
    assert _qDeltaVolQuoteAtmType("ATMSPOT") == ql.DeltaVolQuote.AtmSpot

    vol_handle = ql.QuoteHandle(ql.SimpleQuote(0.20))
    quote_by_delta = qlDeltaVolQuote(
        0.25,
        vol_handle,
        1.0,
        _qDeltaVolQuoteDeltaType("SPOT"),
    )
    quote_atm = qlDeltaVolQuoteAtm(
        vol_handle,
        _qDeltaVolQuoteDeltaType("FWD"),
        1.0,
        _qDeltaVolQuoteAtmType("ATMSPOT"),
    )

    for quote in (quote_by_delta, quote_atm):
        assert qlDeltaVolQuoteIsValid(quote) is True
        assert qlDeltaVolQuoteIsValid(quote) == quote.isValid()
        assert qlDeltaVolQuoteValue(quote) == pytest.approx(quote.value())
        assert qlDeltaVolQuoteMaturity(quote) == pytest.approx(quote.maturity())

    assert qlDeltaVolQuoteDelta(quote_by_delta) == pytest.approx(quote_by_delta.delta())
    assert qlDeltaVolQuoteDelta(quote_by_delta) == pytest.approx(0.25)
    assert qlDeltaVolQuoteDeltaType(quote_by_delta) == "SPOT"
    assert qlDeltaVolQuoteAtmType(quote_by_delta) == "ATMNULL"

    assert qlDeltaVolQuoteDeltaType(quote_atm) == "FWD"
    assert qlDeltaVolQuoteAtmType(quote_atm) == "ATMSPOT"
