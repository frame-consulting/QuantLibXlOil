import QuantLib as ql
import numpy as np
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate
from .payoffs import QL_OPTION_TYPE, _qOptionType, qOptionType
from .ratehelpers import qQuoteHandle
from .utilities import enum_value, first_key, UNKNOWN_KEY, UNKNOWN_VALUE, first_key

QL_CASH_DIVIDEND_MODEL = {
    "SPOT": ql.CashDividendEuropeanEngine.Spot,
    "ESCROWED": ql.CashDividendEuropeanEngine.Escrowed,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_BINOMIAL_ENGINE_TYPE = {
    "COXROSSRUBINSTEIN": "coxrossrubinstein",
    "CRR": "coxrossrubinstein",
    "JARROWRUDD": "jarrowrudd",
    "JR": "jarrowrudd",
    "EQP": "eqp",
    "JOSHI4": "joshi4",
    "J4": "joshi4",
    "LEISENREIMER": "leisenreimer",
    "LR": "leisenreimer",
    "TIAN": "tian",
    "TRIGEORGIS": "trigeorgis",
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_MC_TRAITS = {
    "LD": "lowdiscrepancy",
    "LOWDISCREPANCY": "lowdiscrepancy",
    "PR": "pseudorandom",
    "PSEUDORANDOM": "pseudorandom",
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_LSM_BASIS_SYSTEM_POLYNOMIAL_TYPE = {
    "CHEBYSHEV": ql.LsmBasisSystem.Chebyshev,
    "CHEBYSHEV2ND": ql.LsmBasisSystem.Chebyshev2nd,
    "HERMITE": ql.LsmBasisSystem.Hermite,
    "HYPERBOLIC": ql.LsmBasisSystem.Hyperbolic,
    "LAGUERRE": ql.LsmBasisSystem.Laguerre,
    "LEGENDRE": ql.LsmBasisSystem.Legendre,
    "MONOMIAL": ql.LsmBasisSystem.Monomial,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_ANALYTIC_HESTON_COMPLEX_LOG_FORMULA = {
    "ANDERSENPITERBARG": ql.AnalyticHestonEngine.AndersenPiterbarg,
    "ANDERSENPITERBARGOPTCV": ql.AnalyticHestonEngine.AndersenPiterbargOptCV,
    "ANGLEDCONTOUR": ql.AnalyticHestonEngine.AngledContour,
    "ANGLEDCONTOURNOCV": ql.AnalyticHestonEngine.AngledContourNoCV,
    "ASYMPTOTICCHF": ql.AnalyticHestonEngine.AsymptoticChF,
    "BRANCHCORRECTION": ql.AnalyticHestonEngine.BranchCorrection,
    "GATHERAL": ql.AnalyticHestonEngine.Gatheral,
    "OPTIMALCV": ql.AnalyticHestonEngine.OptimalCV,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_ANALYTIC_PTD_HESTON_COMPLEX_LOG_FORMULA = {
    "ANDERSENPITERBARG": ql.AnalyticPTDHestonEngine.AndersenPiterbarg,
    "GATHERAL": ql.AnalyticPTDHestonEngine.Gatheral,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_ANALYTIC_HESTON_ENGINE_INTEGRATION = {
    "GAUSS_LAGUERRE": ql.AnalyticHestonEngine_Integration.gaussLaguerre,
    "GAUSS_LEGENDRE": ql.AnalyticHestonEngine_Integration.gaussLegendre,
    "GAUSS_CHEBYSHEV": ql.AnalyticHestonEngine_Integration.gaussChebyshev,
    "GAUSS_CHEBYSHEV_2ND": ql.AnalyticHestonEngine_Integration.gaussChebyshev2nd,
    "GAUSS_LOBATTO": ql.AnalyticHestonEngine_Integration.gaussLobatto,
    "GAUSS_KRONROD": ql.AnalyticHestonEngine_Integration.gaussKronrod,
    "SIMPSON": ql.AnalyticHestonEngine_Integration.simpson,
    "TRAPEZOID": ql.AnalyticHestonEngine_Integration.trapezoid,
    "DISCRETE_SIMPSON": ql.AnalyticHestonEngine_Integration.discreteSimpson,
    "DISCRETE_TRAPEZOID": ql.AnalyticHestonEngine_Integration.discreteTrapezoid,
    "EXP_SINH": ql.AnalyticHestonEngine_Integration.expSinh,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_FDM_SCHEME_TYPE = {
    "CRAIGSNEYD": ql.FdmSchemeDesc.CraigSneydType,
    "CRANKNICOLSON": ql.FdmSchemeDesc.CrankNicolsonType,
    "DOUGLAS": ql.FdmSchemeDesc.DouglasType,
    "EXPLICITEULER": ql.FdmSchemeDesc.ExplicitEulerType,
    "HUNDSDORFER": ql.FdmSchemeDesc.HundsdorferType,
    "IMPLICITEULER": ql.FdmSchemeDesc.ImplicitEulerType,
    "METHODOFLINES": ql.FdmSchemeDesc.MethodOfLinesType,
    "MODIFIEDCRAIGSNEYD": ql.FdmSchemeDesc.ModifiedCraigSneydType,
    "TRBDF2": ql.FdmSchemeDesc.TrBDF2Type,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_FDM_SCHEME_DESC = {
    "CRAIGSNEYD": ql.FdmSchemeDesc.CraigSneyd(),
    "CRANKNICOLSON": ql.FdmSchemeDesc.CrankNicolson(),
    "DOUGLAS": ql.FdmSchemeDesc.Douglas(),
    "EXPLICITEULER": ql.FdmSchemeDesc.ExplicitEuler(),
    "HUNDSDORFER": ql.FdmSchemeDesc.Hundsdorfer(),
    "IMPLICITEULER": ql.FdmSchemeDesc.ImplicitEuler(),
    "METHODOFLINES": ql.FdmSchemeDesc.MethodOfLines(),
    "MODIFIEDCRAIGSNEYD": ql.FdmSchemeDesc.ModifiedCraigSneyd(),
    "MODIFIEDHUNDSDORFER": ql.FdmSchemeDesc.ModifiedHundsdorfer(),
    "TRBDF2": ql.FdmSchemeDesc.TrBDF2(),
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_FD_BLACK_SCHOLES_CASH_DIVIDEND_MODEL = {
    "ESCROWED": ql.FdBlackScholesVanillaEngine.Escrowed,
    "SPOT": ql.FdBlackScholesVanillaEngine.Spot,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_QD_PLUS_SOLVER_TYPE = {
    "BRENT": ql.QdPlusAmericanEngine.Brent,
    "HALLEY": ql.QdPlusAmericanEngine.Halley,
    "NEWTON": ql.QdPlusAmericanEngine.Newton,
    "RIDDER": ql.QdPlusAmericanEngine.Ridder,
    "SUPERHALLEY": ql.QdPlusAmericanEngine.SuperHalley,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_QD_FP_FIXED_POINT_EQUATION = {
    "AUTO": ql.QdFpAmericanEngine.Auto,
    "FP_A": ql.QdFpAmericanEngine.FP_A,
    "FP_B": ql.QdFpAmericanEngine.FP_B,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_QD_FP_ITERATION_SCHEME = {
    "FAST": ql.QdFpAmericanEngine.fastScheme(),
    "ACCURATE": ql.QdFpAmericanEngine.accurateScheme(),
    "HIGH_PRECISION": ql.QdFpAmericanEngine.highPrecisionScheme(),
}


QL_DELTA_VOL_QUOTE_DELTA_TYPE = {
    "FWD": ql.DeltaVolQuote.Fwd,
    "PAFWD": ql.DeltaVolQuote.PaFwd,
    "PASPOT": ql.DeltaVolQuote.PaSpot,
    "SPOT": ql.DeltaVolQuote.Spot,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_DELTA_VOL_QUOTE_ATM_TYPE = {
    "ATMDELTANEUTRAL": ql.DeltaVolQuote.AtmDeltaNeutral,
    "ATMFWD": ql.DeltaVolQuote.AtmFwd,
    "ATMGAMMAMAX": ql.DeltaVolQuote.AtmGammaMax,
    "ATMNULL": ql.DeltaVolQuote.AtmNull,
    "ATMPUTCALL50": ql.DeltaVolQuote.AtmPutCall50,
    "ATMSPOT": ql.DeltaVolQuote.AtmSpot,
    "ATMVEGAMAX": ql.DeltaVolQuote.AtmVegaMax,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qCashDividendModel(s: str) -> int:
    return enum_value(s, QL_CASH_DIVIDEND_MODEL)


@xlo.converter()
def qCashDividendModel(s: str) -> int:
    return _qCashDividendModel(s)


def _qBinomialEngineType(s: str) -> str:
    return enum_value(s, QL_BINOMIAL_ENGINE_TYPE)


@xlo.converter()
def qBinomialEngineType(s: str) -> str:
    return _qBinomialEngineType(s)


def _qMCTraits(s: str) -> str:
    return enum_value(s, QL_MC_TRAITS)


@xlo.converter()
def qMCTraits(s: str) -> str:
    return _qMCTraits(s)


def _qLsmBasisSystemPolynomialType(s: str) -> int:
    return enum_value(s, QL_LSM_BASIS_SYSTEM_POLYNOMIAL_TYPE)


@xlo.converter()
def qLsmBasisSystemPolynomialType(s: str) -> int:
    return _qLsmBasisSystemPolynomialType(s)


def _qAnalyticHestonComplexLogFormula(s: str) -> int:
    return enum_value(s, QL_ANALYTIC_HESTON_COMPLEX_LOG_FORMULA)


@xlo.converter()
def qAnalyticHestonComplexLogFormula(s: str) -> int:
    return _qAnalyticHestonComplexLogFormula(s)


def _qAnalyticPTDHestonComplexLogFormula(s: str) -> int:
    return enum_value(s, QL_ANALYTIC_PTD_HESTON_COMPLEX_LOG_FORMULA)


@xlo.converter()
def qAnalyticPTDHestonComplexLogFormula(s: str) -> int:
    return _qAnalyticPTDHestonComplexLogFormula(s)


def _qAnalyticHestonEngineIntegration(name: str) -> ql.AnalyticHestonEngine_Integration:
    if name is None:
        # capture optional argument
        return None
    if isinstance(name, ql.AnalyticHestonEngine_Integration):
        # capture default argument values
        return name
    if isinstance(name, str):
        name = name.strip().upper()
        if name in QL_ANALYTIC_HESTON_ENGINE_INTEGRATION:
            return QL_ANALYTIC_HESTON_ENGINE_INTEGRATION[name]
    raise ValueError(f"Unknown AnalyticHestonEngineIntegration: {name}")


@xlo.converter()
def qAnalyticHestonEngineIntegration(name: str) -> ql.AnalyticHestonEngine_Integration:
    return _qAnalyticHestonEngineIntegration(name)


def _to_analytic_heston_engine_integration(
    integration_function,
    integration_order: int,
    rel_tolerance: float,
    abs_tolerance: float,
    max_evaluations: int,
) -> ql.AnalyticHestonEngine_Integration:
    if integration_function in (
        ql.AnalyticHestonEngine_Integration.gaussLaguerre,
        ql.AnalyticHestonEngine_Integration.gaussLegendre,
        ql.AnalyticHestonEngine_Integration.gaussChebyshev,
        ql.AnalyticHestonEngine_Integration.gaussChebyshev2nd,
        ql.AnalyticHestonEngine_Integration.discreteSimpson,
        ql.AnalyticHestonEngine_Integration.discreteTrapezoid,
    ):
        integration_ = integration_function(integration_order)
    elif integration_function in (
        ql.AnalyticHestonEngine_Integration.gaussKronrod,
        ql.AnalyticHestonEngine_Integration.simpson,
        ql.AnalyticHestonEngine_Integration.trapezoid,
    ):
        integration_ = integration_function(abs_tolerance, max_evaluations)
    elif integration_function in (ql.AnalyticHestonEngine_Integration.gaussLobatto,):
        integration_ = integration_function(
            rel_tolerance, abs_tolerance, max_evaluations
        )
    elif integration_function in (ql.AnalyticHestonEngine_Integration.expSinh,):
        integration_ = integration_function(rel_tolerance)
    else:
        raise ValueError("Cannot create integration object.")
    return integration_


def _qFdmSchemeType(s: str) -> int:
    return enum_value(s, QL_FDM_SCHEME_TYPE)


@xlo.converter()
def qFdmSchemeType(s: str) -> int:
    return _qFdmSchemeType(s)


def _qFdmSchemeDesc(s: str) -> int:
    return enum_value(s, QL_FDM_SCHEME_DESC)


@xlo.converter()
def qFdmSchemeDesc(s: str) -> int:
    return _qFdmSchemeDesc(s)


def _qFdBlackScholesCashDividendModel(s: str) -> int:
    return enum_value(s, QL_FD_BLACK_SCHOLES_CASH_DIVIDEND_MODEL)


@xlo.converter()
def qFdBlackScholesCashDividendModel(s: str) -> int:
    return _qFdBlackScholesCashDividendModel(s)


def _qQdPlusSolverType(s: str) -> int:
    return enum_value(s, QL_QD_PLUS_SOLVER_TYPE)


@xlo.converter()
def qQdPlusSolverType(s: str) -> int:
    return _qQdPlusSolverType(s)


def _qQdFpFixedPointEquation(s: str) -> int:
    return enum_value(s, QL_QD_FP_FIXED_POINT_EQUATION)


@xlo.converter()
def qQdFpFixedPointEquation(s: str) -> int:
    return _qQdFpFixedPointEquation(s)


def _qQdFpIterationScheme(s: str) -> int:
    return enum_value(
        s,
        QL_QD_FP_ITERATION_SCHEME,
        value_type=type(ql.QdFpAmericanEngine.accurateScheme()),
    )


@xlo.converter()
def qQdFpIterationScheme(s: str) -> int:
    return _qQdFpIterationScheme(s)


def _qDeltaVolQuoteDeltaType(s: str) -> int:
    return enum_value(s, QL_DELTA_VOL_QUOTE_DELTA_TYPE)


@xlo.converter()
def qDeltaVolQuoteDeltaType(s: str) -> int:
    return _qDeltaVolQuoteDeltaType(s)


def _qDeltaVolQuoteAtmType(s: str) -> int:
    return enum_value(s, QL_DELTA_VOL_QUOTE_ATM_TYPE)


@xlo.converter()
def qDeltaVolQuoteAtmType(s: str) -> int:
    return _qDeltaVolQuoteAtmType(s)


@xlo.func(
    help="Return option type as string.",
    args={
        "option_type": "QuantLib option type.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOptionTypeName(option_type: qOptionType, trigger=None) -> str:
    return first_key(QL_OPTION_TYPE, _qOptionType(option_type), UNKNOWN_VALUE)


def _to_dividend_schedule(dividends) -> tuple[ql.Dividend, ...]:
    if dividends is None:
        return ()
    if isinstance(dividends, ql.Dividend):
        return (dividends,)
    if isinstance(dividends, (list, tuple)):
        return tuple(cf for cf in dividends)
    if isinstance(dividends, np.ndarray):
        return tuple(dividends.ravel().tolist())
    raise ValueError(f"Cannot convert {dividends} to list of QuantLib CashFlows.")


# Options


@xlo.func(
    help="Return payoff of a QuantLib option.",
    args={
        "option": "QuantLib option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOptionPayoff(option: ql.Option, trigger=None) -> ql.Payoff:
    return option.payoff()


@xlo.func(
    help="Return exercise of a QuantLib option.",
    args={
        "option": "QuantLib option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOptionExercise(option: ql.Option, trigger=None) -> ql.Exercise:
    return option.exercise()


## One-asset option interface


@xlo.func(
    help="Return option delta.",
    args={
        "option": "QuantLib one-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneAssetOptionDelta(option: ql.OneAssetOption, trigger=None) -> float:
    return option.delta()


@xlo.func(
    help="Return option forward delta.",
    args={
        "option": "QuantLib one-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneAssetOptionDeltaForward(option: ql.OneAssetOption, trigger=None) -> float:
    return option.deltaForward()


@xlo.func(
    help="Return option elasticity.",
    args={
        "option": "QuantLib one-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneAssetOptionElasticity(option: ql.OneAssetOption, trigger=None) -> float:
    return option.elasticity()


@xlo.func(
    help="Return option gamma.",
    args={
        "option": "QuantLib one-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneAssetOptionGamma(option: ql.OneAssetOption, trigger=None) -> float:
    return option.gamma()


@xlo.func(
    help="Return option theta.",
    args={
        "option": "QuantLib one-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneAssetOptionTheta(option: ql.OneAssetOption, trigger=None) -> float:
    return option.theta()


@xlo.func(
    help="Return option theta per day.",
    args={
        "option": "QuantLib one-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneAssetOptionThetaPerDay(option: ql.OneAssetOption, trigger=None) -> float:
    return option.thetaPerDay()


@xlo.func(
    help="Return option vega.",
    args={
        "option": "QuantLib one-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneAssetOptionVega(option: ql.OneAssetOption, trigger=None) -> float:
    return option.vega()


@xlo.func(
    help="Return option rho.",
    args={
        "option": "QuantLib one-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneAssetOptionRho(option: ql.OneAssetOption, trigger=None) -> float:
    return option.rho()


@xlo.func(
    help="Return option dividend rho.",
    args={
        "option": "QuantLib one-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneAssetOptionDividendRho(option: ql.OneAssetOption, trigger=None) -> float:
    return option.dividendRho()


@xlo.func(
    help="Return option strike sensitivity.",
    args={
        "option": "QuantLib one-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneAssetOptionStrikeSensitivity(option: ql.OneAssetOption, trigger=None) -> float:
    return option.strikeSensitivity()


@xlo.func(
    help="Return in-the-money cash probability.",
    args={
        "option": "QuantLib one-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneAssetOptionITMCashProbability(
    option: ql.OneAssetOption, trigger=None
) -> float:
    return option.itmCashProbability()


## Vanilla option


@xlo.func(
    help="Create a QuantLib VanillaOption object.",
    args={
        "payoff": "QuantLib striked payoff.",
        "exercise": "QuantLib exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlVanillaOption(
    payoff: ql.StrikedTypePayoff, exercise: ql.Exercise, trigger=None
) -> ql.VanillaOption:
    return ql.VanillaOption(payoff, exercise)


@xlo.func(
    help="Return implied volatility for a vanilla option.",
    args={
        "option": "QuantLib vanilla option.",
        "target_value": "Target option value.",
        "process": "QuantLib generalized Black-Scholes process.",
        "dividends": "Optional dividend schedule.",
        "accuracy": "Solver accuracy.",
        "max_evaluations": "Maximum number of evaluations.",
        "min_vol": "Minimum volatility bound.",
        "max_vol": "Maximum volatility bound.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlVanillaOptionImpliedVolatility(
    option: ql.VanillaOption,
    target_value: float,
    process: ql.GeneralizedBlackScholesProcess,
    dividends: xlo.Array(dims=1) = None,
    accuracy: float = 1.0e-4,
    max_evaluations: int = 100,
    min_vol: float = 1.0e-4,
    max_vol: float = 4.0,
    trigger=None,
) -> float:
    dividends_ = _to_dividend_schedule(dividends)
    if len(dividends_) > 0:
        return option.impliedVolatility(
            target_value,
            process,
            dividends_,
            accuracy,
            max_evaluations,
            min_vol,
            max_vol,
        )
    return option.impliedVolatility(
        target_value, process, accuracy, max_evaluations, min_vol, max_vol
    )


@xlo.func(
    help="Create a QuantLib EuropeanOption object.",
    args={
        "payoff": "QuantLib striked payoff.",
        "exercise": "QuantLib exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEuropeanOption(
    payoff: ql.StrikedTypePayoff, exercise: ql.Exercise, trigger=None
) -> ql.EuropeanOption:
    return ql.EuropeanOption(payoff, exercise)


## Forward and Quanto Vanilla option


@xlo.func(
    help="Create a QuantLib ForwardVanillaOption object.",
    args={
        "moneyness": "Moneyness value.",
        "reset_date": "Reset date.",
        "payoff": "QuantLib striked payoff.",
        "exercise": "QuantLib exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlForwardVanillaOption(
    moneyness: float,
    reset_date: qDate,
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.ForwardVanillaOption:
    return ql.ForwardVanillaOption(moneyness, reset_date, payoff, exercise)


@xlo.func(
    help="Create a QuantLib QuantoVanillaOption object.",
    args={
        "payoff": "QuantLib striked payoff.",
        "exercise": "QuantLib exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoVanillaOption(
    payoff: ql.StrikedTypePayoff, exercise: ql.Exercise, trigger=None
) -> ql.QuantoVanillaOption:
    return ql.QuantoVanillaOption(payoff, exercise)


@xlo.func(
    help="Return quanto option qvega.",
    args={
        "option": "QuantLib quanto vanilla option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoVanillaOptionQVega(option: ql.QuantoVanillaOption, trigger=None) -> float:
    return option.qvega()


@xlo.func(
    help="Return quanto option qrho.",
    args={
        "option": "QuantLib quanto vanilla option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoVanillaOptionQRho(option: ql.QuantoVanillaOption, trigger=None) -> float:
    return option.qrho()


@xlo.func(
    help="Return quanto option qlambda.",
    args={
        "option": "QuantLib quanto vanilla option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoVanillaOptionQLambda(option: ql.QuantoVanillaOption, trigger=None) -> float:
    return option.qlambda()


@xlo.func(
    help="Create a QuantLib QuantoForwardVanillaOption object.",
    args={
        "moneyness": "Moneyness value.",
        "reset_date": "Reset date.",
        "payoff": "QuantLib striked payoff.",
        "exercise": "QuantLib exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoForwardVanillaOption(
    moneyness: float,
    reset_date: qDate,
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.QuantoForwardVanillaOption:
    return ql.QuantoForwardVanillaOption(moneyness, reset_date, payoff, exercise)


## Multi-asset option interface


@xlo.func(
    help="Return option delta as list.",
    args={
        "option": "QuantLib multi-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiAssetOptionDelta(option: ql.MultiAssetOption, trigger=None) -> list:
    return option.delta()


@xlo.func(
    help="Return option gamma as list.",
    args={
        "option": "QuantLib multi-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiAssetOptionGamma(option: ql.MultiAssetOption, trigger=None) -> list:
    return option.gamma()


@xlo.func(
    help="Return option theta as list.",
    args={
        "option": "QuantLib multi-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiAssetOptionTheta(option: ql.MultiAssetOption, trigger=None) -> list:
    return option.theta()


@xlo.func(
    help="Return option vega as list.",
    args={
        "option": "QuantLib multi-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiAssetOptionVega(option: ql.MultiAssetOption, trigger=None) -> list:
    return option.vega()


@xlo.func(
    help="Return option rho as list.",
    args={
        "option": "QuantLib multi-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiAssetOptionRho(option: ql.MultiAssetOption, trigger=None) -> list:
    return option.rho()


@xlo.func(
    help="Return option dividend rho as list.",
    args={
        "option": "QuantLib multi-asset option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiAssetOptionDividendRho(option: ql.MultiAssetOption, trigger=None) -> list:
    return option.dividendRho()


## Magrabe option


@xlo.func(
    help="Create a QuantLib MargrabeOption object.",
    args={
        "q1": "Quantity of first asset.",
        "q2": "Quantity of second asset.",
        "exercise": "QuantLib exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMargrabeOption(
    q1: int, q2: int, exercise: ql.Exercise, trigger=None
) -> ql.MargrabeOption:
    return ql.MargrabeOption(q1, q2, exercise)


@xlo.func(
    help="Return first Margrabe delta.",
    args={
        "option": "QuantLib Margrabe option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMargrabeOptionDelta1(option: ql.MargrabeOption, trigger=None) -> float:
    return option.delta1()


@xlo.func(
    help="Return second Margrabe delta.",
    args={
        "option": "QuantLib Margrabe option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMargrabeOptionDelta2(option: ql.MargrabeOption, trigger=None) -> float:
    return option.delta2()


@xlo.func(
    help="Return first Margrabe gamma.",
    args={
        "option": "QuantLib Margrabe option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMargrabeOptionGamma1(option: ql.MargrabeOption, trigger=None) -> float:
    return option.gamma1()


@xlo.func(
    help="Return second Margrabe gamma.",
    args={
        "option": "QuantLib Margrabe option.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMargrabeOptionGamma2(option: ql.MargrabeOption, trigger=None) -> float:
    return option.gamma2()


@xlo.func(
    help="Create a QuantLib TwoAssetCorrelationOption object.",
    args={
        "option_type": "Option type.",
        "strike1": "First strike value.",
        "strike2": "Second strike value.",
        "exercise": "QuantLib exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTwoAssetCorrelationOption(
    option_type: qOptionType,
    strike1: float,
    strike2: float,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.TwoAssetCorrelationOption:
    return ql.TwoAssetCorrelationOption(option_type, strike1, strike2, exercise)


## Other options


@xlo.func(
    help="Create a QuantLib CompoundOption object.",
    args={
        "mother_payoff": "Mother striked payoff.",
        "mother_exercise": "Mother exercise.",
        "daughter_payoff": "Daughter striked payoff.",
        "daughter_exercise": "Daughter exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCompoundOption(
    mother_payoff: ql.StrikedTypePayoff,
    mother_exercise: ql.Exercise,
    daughter_payoff: ql.StrikedTypePayoff,
    daughter_exercise: ql.Exercise,
    trigger=None,
) -> ql.CompoundOption:
    return ql.CompoundOption(
        mother_payoff, mother_exercise, daughter_payoff, daughter_exercise
    )


@xlo.func(
    help="Create a QuantLib SimpleChooserOption object.",
    args={
        "choosing_date": "Choosing date.",
        "strike": "Strike value.",
        "exercise": "QuantLib exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSimpleChooserOption(
    choosing_date: qDate, strike: float, exercise: ql.Exercise, trigger=None
) -> ql.SimpleChooserOption:
    return ql.SimpleChooserOption(choosing_date, strike, exercise)


@xlo.func(
    help="Create a QuantLib ComplexChooserOption object.",
    args={
        "choosing_date": "Choosing date.",
        "strike_call": "Call strike value.",
        "strike_put": "Put strike value.",
        "exercise_call": "Call exercise.",
        "exercise_put": "Put exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlComplexChooserOption(
    choosing_date: qDate,
    strike_call: float,
    strike_put: float,
    exercise_call: ql.Exercise,
    exercise_put: ql.Exercise,
    trigger=None,
) -> ql.ComplexChooserOption:
    return ql.ComplexChooserOption(
        choosing_date, strike_call, strike_put, exercise_call, exercise_put
    )


@xlo.func(
    help="Create a QuantLib HolderExtensibleOption object.",
    args={
        "option_type": "Option type.",
        "premium": "Extension premium.",
        "second_expiry_date": "Second expiry date.",
        "second_strike": "Second strike value.",
        "payoff": "Initial striked payoff.",
        "exercise": "Initial exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHolderExtensibleOption(
    option_type: qOptionType,
    premium: float,
    second_expiry_date: qDate,
    second_strike: float,
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.HolderExtensibleOption:
    return ql.HolderExtensibleOption(
        _qOptionType(option_type),
        premium,
        second_expiry_date,
        second_strike,
        payoff,
        exercise,
    )


@xlo.func(
    help="Create a QuantLib WriterExtensibleOption object.",
    args={
        "payoff1": "First plain vanilla payoff.",
        "exercise1": "First exercise.",
        "payoff2": "Second plain vanilla payoff.",
        "exercise2": "Second exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlWriterExtensibleOption(
    payoff1: ql.PlainVanillaPayoff,
    exercise1: ql.Exercise,
    payoff2: ql.PlainVanillaPayoff,
    exercise2: ql.Exercise,
    trigger=None,
) -> ql.WriterExtensibleOption:
    return ql.WriterExtensibleOption(payoff1, exercise1, payoff2, exercise2)


# Pricing engines

## Black-Scholes engines


@xlo.func(
    help="Create a QuantLib AnalyticEuropeanEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "discount_curve": "Optional discount curve handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticEuropeanEngine(
    process: ql.GeneralizedBlackScholesProcess,
    discount_curve: ql.YieldTermStructureHandle = None,
    trigger=None,
) -> ql.AnalyticEuropeanEngine:
    if discount_curve is None:
        return ql.AnalyticEuropeanEngine(process)
    return ql.AnalyticEuropeanEngine(process, discount_curve)


@xlo.func(
    help="Create a QuantLib AnalyticDividendEuropeanEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "dividends": "Dividend schedule.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticDividendEuropeanEngine(
    process: ql.GeneralizedBlackScholesProcess,
    dividends: xlo.Array(dims=1),
    trigger=None,
) -> ql.AnalyticDividendEuropeanEngine:
    return ql.AnalyticDividendEuropeanEngine(process, _to_dividend_schedule(dividends))


@xlo.func(
    help="Create a QuantLib CashDividendEuropeanEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "dividends": "Dividend schedule.",
        "cash_dividend_model": "Cash dividend model (spot or escrowed).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashDividendEuropeanEngine(
    process: ql.GeneralizedBlackScholesProcess,
    dividends: xlo.Array(dims=1),
    cash_dividend_model: qCashDividendModel = ql.CashDividendEuropeanEngine.Spot,
    trigger=None,
) -> ql.CashDividendEuropeanEngine:
    return ql.CashDividendEuropeanEngine(
        process, _to_dividend_schedule(dividends), cash_dividend_model
    )


@xlo.func(
    help="Create a QuantLib IntegralEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIntegralEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.IntegralEngine:
    return ql.IntegralEngine(process)


@xlo.func(
    help="Create a QuantLib ForwardEuropeanEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlForwardEuropeanEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.ForwardEuropeanEngine:
    return ql.ForwardEuropeanEngine(process)


@xlo.func(
    help="Create a QuantLib QuantoEuropeanEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "foreign_risk_free_rate": "Foreign risk-free yield term structure handle.",
        "exchange_rate_volatility": "FX volatility term structure handle.",
        "correlation": "Correlation quote handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoEuropeanEngine(
    process: ql.GeneralizedBlackScholesProcess,
    foreign_risk_free_rate: ql.YieldTermStructureHandle,
    exchange_rate_volatility: ql.BlackVolTermStructureHandle,
    correlation: qQuoteHandle,
    trigger=None,
) -> ql.QuantoEuropeanEngine:
    return ql.QuantoEuropeanEngine(
        process, foreign_risk_free_rate, exchange_rate_volatility, correlation
    )


@xlo.func(
    help="Create a QuantLib QuantoForwardEuropeanEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "foreign_risk_free_rate": "Foreign risk-free yield term structure handle.",
        "exchange_rate_volatility": "FX volatility term structure handle.",
        "correlation": "Correlation quote handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoForwardEuropeanEngine(
    process: ql.GeneralizedBlackScholesProcess,
    foreign_risk_free_rate: ql.YieldTermStructureHandle,
    exchange_rate_volatility: ql.BlackVolTermStructureHandle,
    correlation: qQuoteHandle,
    trigger=None,
) -> ql.QuantoForwardEuropeanEngine:
    # TODO: Check why engine does not work with qlQuantoForwardVanillaOption
    return ql.QuantoForwardEuropeanEngine(
        process, foreign_risk_free_rate, exchange_rate_volatility, correlation
    )


## Analytic American options engines


@xlo.func(
    help="Create a QuantLib BaroneAdesiWhaleyApproximationEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBaroneAdesiWhaleyApproximationEngine(
    process: ql.GeneralizedBlackScholesProcess,
    trigger=None,
) -> ql.BaroneAdesiWhaleyApproximationEngine:
    return ql.BaroneAdesiWhaleyApproximationEngine(process)


@xlo.func(
    help="Create a QuantLib BjerksundStenslandApproximationEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBjerksundStenslandApproximationEngine(
    process: ql.GeneralizedBlackScholesProcess,
    trigger=None,
) -> ql.BjerksundStenslandApproximationEngine:
    return ql.BjerksundStenslandApproximationEngine(process)


@xlo.func(
    help="Create a QuantLib JuQuadraticApproximationEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlJuQuadraticApproximationEngine(
    process: ql.GeneralizedBlackScholesProcess,
    trigger=None,
) -> ql.JuQuadraticApproximationEngine:
    return ql.JuQuadraticApproximationEngine(process)


@xlo.func(
    help="Create a QuantLib AnalyticDigitalAmericanEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticDigitalAmericanEngine(
    process: ql.GeneralizedBlackScholesProcess,
    trigger=None,
) -> ql.AnalyticDigitalAmericanEngine:
    return ql.AnalyticDigitalAmericanEngine(process)


## Other Analytic engines


@xlo.func(
    help="Create a QuantLib AnalyticEuropeanMargrabeEngine object.",
    args={
        "process1": "First generalized Black-Scholes process.",
        "process2": "Second generalized Black-Scholes process.",
        "correlation": "Correlation value.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticEuropeanMargrabeEngine(
    process1: ql.GeneralizedBlackScholesProcess,
    process2: ql.GeneralizedBlackScholesProcess,
    correlation: float,
    trigger=None,
) -> ql.AnalyticEuropeanMargrabeEngine:
    return ql.AnalyticEuropeanMargrabeEngine(process1, process2, correlation)


@xlo.func(
    help="Create a QuantLib AnalyticAmericanMargrabeEngine object.",
    args={
        "process1": "First generalized Black-Scholes process.",
        "process2": "Second generalized Black-Scholes process.",
        "correlation": "Correlation value.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticAmericanMargrabeEngine(
    process1: ql.GeneralizedBlackScholesProcess,
    process2: ql.GeneralizedBlackScholesProcess,
    correlation: float,
    trigger=None,
) -> ql.AnalyticAmericanMargrabeEngine:
    return ql.AnalyticAmericanMargrabeEngine(process1, process2, correlation)


@xlo.func(
    help="Create a QuantLib AnalyticCompoundOptionEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticCompoundOptionEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticCompoundOptionEngine:
    return ql.AnalyticCompoundOptionEngine(process)


@xlo.func(
    help="Create a QuantLib AnalyticSimpleChooserEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticSimpleChooserEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticSimpleChooserEngine:
    return ql.AnalyticSimpleChooserEngine(process)


@xlo.func(
    help="Create a QuantLib AnalyticComplexChooserEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticComplexChooserEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticComplexChooserEngine:
    return ql.AnalyticComplexChooserEngine(process)


@xlo.func(
    help="Create a QuantLib AnalyticHolderExtensibleOptionEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHolderExtensibleOptionEngine(
    process: ql.GeneralizedBlackScholesProcess,
    trigger=None,
) -> ql.AnalyticHolderExtensibleOptionEngine:
    return ql.AnalyticHolderExtensibleOptionEngine(process)


@xlo.func(
    help="Create a QuantLib AnalyticWriterExtensibleOptionEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticWriterExtensibleOptionEngine(
    process: ql.GeneralizedBlackScholesProcess,
    trigger=None,
) -> ql.AnalyticWriterExtensibleOptionEngine:
    return ql.AnalyticWriterExtensibleOptionEngine(process)


@xlo.func(
    help="Create a QuantLib AnalyticTwoAssetCorrelationEngine object.",
    args={
        "process1": "First generalized Black-Scholes process.",
        "process2": "Second generalized Black-Scholes process.",
        "correlation": "Correlation quote handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticTwoAssetCorrelationEngine(
    process1: ql.GeneralizedBlackScholesProcess,
    process2: ql.GeneralizedBlackScholesProcess,
    correlation: qQuoteHandle,
    trigger=None,
) -> ql.AnalyticTwoAssetCorrelationEngine:
    return ql.AnalyticTwoAssetCorrelationEngine(process1, process2, correlation)


## Heston models and Heston engines


@xlo.func(
    help="Create a QuantLib HestonModel object.",
    args={
        "process": "QuantLib Heston process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHestonModel(process: ql.HestonProcess, trigger=None) -> ql.HestonModel:
    return ql.HestonModel(process)


@xlo.func(
    help="Create a QuantLib HestonModelHandle object.",
    args={
        "model": "QuantLib Heston model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHestonModelHandle(model: ql.HestonModel, trigger=None) -> ql.HestonModelHandle:
    return ql.HestonModelHandle(model)


@xlo.func(
    help="Return current link of a QuantLib HestonModelHandle.",
    args={
        "model_handle": "QuantLib Heston model handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHestonModelHandleCurrentLink(
    model_handle: ql.HestonModelHandle, trigger=None
) -> ql.HestonModel:
    return model_handle.currentLink()


@xlo.func(
    help="Return theta of a QuantLib HestonModel.",
    args={
        "model": "QuantLib Heston model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHestonModelTheta(model: ql.HestonModel, trigger=None) -> float:
    return model.theta()


@xlo.func(
    help="Return kappa of a QuantLib HestonModel.",
    args={
        "model": "QuantLib Heston model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHestonModelKappa(model: ql.HestonModel, trigger=None) -> float:
    return model.kappa()


@xlo.func(
    help="Return sigma of a QuantLib HestonModel.",
    args={
        "model": "QuantLib Heston model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHestonModelSigma(model: ql.HestonModel, trigger=None) -> float:
    return model.sigma()


@xlo.func(
    help="Return rho of a QuantLib HestonModel.",
    args={
        "model": "QuantLib Heston model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHestonModelRho(model: ql.HestonModel, trigger=None) -> float:
    return model.rho()


@xlo.func(
    help="Return v0 of a QuantLib HestonModel.",
    args={
        "model": "QuantLib Heston model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHestonModelV0(model: ql.HestonModel, trigger=None) -> float:
    return model.v0()


@xlo.func(
    help="Return process of a QuantLib HestonModel.",
    args={
        "model": "QuantLib Heston model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHestonModelProcess(model: ql.HestonModel, trigger=None) -> ql.HestonProcess:
    return model.process()


@xlo.func(
    help="Create a QuantLib PiecewiseTimeDependentHestonModel object.",
    args={
        "risk_free_rate": "Risk-free yield term structure handle.",
        "dividend_yield": "Dividend yield term structure handle.",
        "s0": "Spot quote handle.",
        "v0": "Initial variance.",
        "theta": "Theta parameter.",
        "kappa": "Kappa parameter.",
        "sigma": "Sigma parameter.",
        "rho": "Rho parameter.",
        "time_grid": "Time grid.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseTimeDependentHestonModel(
    risk_free_rate: ql.YieldTermStructureHandle,
    dividend_yield: ql.YieldTermStructureHandle,
    s0: qQuoteHandle,
    v0: float,
    theta: ql.Parameter,
    kappa: ql.Parameter,
    sigma: ql.Parameter,
    rho: ql.Parameter,
    time_grid: ql.TimeGrid,
    trigger=None,
) -> ql.PiecewiseTimeDependentHestonModel:
    return ql.PiecewiseTimeDependentHestonModel(
        risk_free_rate, dividend_yield, s0, v0, theta, kappa, sigma, rho, time_grid
    )


@xlo.func(
    help="Return theta of a PiecewiseTimeDependentHestonModel.",
    args={
        "model": "QuantLib PiecewiseTimeDependentHestonModel.",
        "t": "Time.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseTimeDependentHestonModelTheta(
    model: ql.PiecewiseTimeDependentHestonModel, t: float, trigger=None
) -> float:
    return model.theta(t)


@xlo.func(
    help="Return kappa of a PiecewiseTimeDependentHestonModel.",
    args={
        "model": "QuantLib PiecewiseTimeDependentHestonModel.",
        "t": "Time.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseTimeDependentHestonModelKappa(
    model: ql.PiecewiseTimeDependentHestonModel, t: float, trigger=None
) -> float:
    return model.kappa(t)


@xlo.func(
    help="Return sigma of a PiecewiseTimeDependentHestonModel.",
    args={
        "model": "QuantLib PiecewiseTimeDependentHestonModel.",
        "t": "Time.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseTimeDependentHestonModelSigma(
    model: ql.PiecewiseTimeDependentHestonModel, t: float, trigger=None
) -> float:
    return model.sigma(t)


@xlo.func(
    help="Return rho of a PiecewiseTimeDependentHestonModel.",
    args={
        "model": "QuantLib PiecewiseTimeDependentHestonModel.",
        "t": "Time.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseTimeDependentHestonModelRho(
    model: ql.PiecewiseTimeDependentHestonModel, t: float, trigger=None
) -> float:
    return model.rho(t)


@xlo.func(
    help="Return v0 of a PiecewiseTimeDependentHestonModel.",
    args={
        "model": "QuantLib PiecewiseTimeDependentHestonModel.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseTimeDependentHestonModelV0(
    model: ql.PiecewiseTimeDependentHestonModel, trigger=None
) -> float:
    return model.v0()


@xlo.func(
    help="Return s0 of a PiecewiseTimeDependentHestonModel.",
    args={
        "model": "QuantLib PiecewiseTimeDependentHestonModel.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseTimeDependentHestonModelS0(
    model: ql.PiecewiseTimeDependentHestonModel, trigger=None
) -> float:
    return model.s0()


## Analytic Heston engine and helpers


@xlo.func(
    help="Create AnalyticHestonEngine integration object using Gauss-Laguerre quadrature.",
    args={
        "integration_order": "Integration order.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHestonEngineIntegrationGaussLaguerre(
    integration_order: int = 128,
    trigger=None,
) -> ql.AnalyticHestonEngine_Integration:
    return ql.AnalyticHestonEngine_Integration.gaussLaguerre(integration_order)


@xlo.func(
    help="Return number of evaluations for AnalyticHestonEngine integration object.",
    args={
        "integration": "AnalyticHestonEngine integration object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHestonEngineIntegrationNumberOfEvaluations(
    integration: ql.AnalyticHestonEngine_Integration,
    trigger=None,
) -> int:
    return integration.numberOfEvaluations()


@xlo.func(
    help="Return whether AnalyticHestonEngine integration is adaptive.",
    args={
        "integration": "AnalyticHestonEngine integration object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHestonEngineIntegrationIsAdaptive(
    integration: ql.AnalyticHestonEngine_Integration,
    trigger=None,
) -> bool:
    return integration.isAdaptiveIntegration()


@xlo.func(
    help="Return Andersen-Piterbarg integration limit for AnalyticHestonEngine.",
    args={
        "c_inf": "Asymptotic decay parameter.",
        "epsilon": "Target error.",
        "v0": "Initial variance.",
        "t": "Time.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHestonEngineIntegrationAndersenPiterbargIntegrationLimit(
    c_inf: float,
    epsilon: float,
    v0: float,
    t: float,
    trigger=None,
) -> float:
    return ql.AnalyticHestonEngine_Integration.andersenPiterbargIntegrationLimit(
        c_inf, epsilon, v0, t
    )


@xlo.func(
    help="Create AnalyticHestonEngine optimal alpha helper object.",
    args={
        "t": "Time.",
        "engine": "AnalyticHestonEngine.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHestonEngineOptimalAlpha(
    t: float,
    engine: ql.AnalyticHestonEngine,
    trigger=None,
) -> ql.AnalyticHestonEngine_OptimalAlpha:
    return ql.AnalyticHestonEngine_OptimalAlpha(t, engine)


@xlo.func(
    help="Evaluate AnalyticHestonEngine optimal alpha helper for a strike.",
    args={
        "optimal_alpha": "AnalyticHestonEngine optimal alpha helper.",
        "strike": "Strike.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHestonEngineOptimalAlphaValue(
    optimal_alpha: ql.AnalyticHestonEngine_OptimalAlpha,
    strike: float,
    trigger=None,
) -> float:
    return optimal_alpha(strike)


@xlo.func(
    help="Return alpha bounds for a strike from AnalyticHestonEngine optimal alpha helper.",
    args={
        "optimal_alpha": "AnalyticHestonEngine optimal alpha helper.",
        "strike": "Strike.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHestonEngineOptimalAlphaBounds(
    optimal_alpha: ql.AnalyticHestonEngine_OptimalAlpha,
    strike: float,
    trigger=None,
) -> list[float]:
    return [optimal_alpha.alphaMin(strike), optimal_alpha.alphaMax(strike)]


@xlo.func(
    help="Create a QuantLib AnalyticHestonEngine object.",
    args={
        "model": "QuantLib Heston model.",
        "integration_order": "Integration order for default constructor.",
        "rel_tolerance": "Relative tolerance for adaptive integration constructor.",
        "max_evaluations": "Maximum evaluations for adaptive integration constructor.",
        "complex_log_formula": "Complex-log formula.",
        "integration": "AnalyticHestonEngine integration object.",
        "andersen_piterbarg_epsilon": "Andersen-Piterbarg epsilon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHestonEngine(
    model: ql.HestonModel,
    integration_order: int = 144,
    rel_tolerance: float = None,
    abs_tolerance: float = None,
    max_evaluations: int = None,
    complex_log_formula: qAnalyticHestonComplexLogFormula = ql.AnalyticHestonEngine.Gatheral,
    integration: qAnalyticHestonEngineIntegration = None,
    andersen_piterbarg_epsilon: float = 1.0e-8,
    trigger=None,
) -> ql.AnalyticHestonEngine:
    if integration is not None:
        integration_ = _to_analytic_heston_engine_integration(
            integration,
            integration_order,
            rel_tolerance,
            abs_tolerance,
            max_evaluations,
        )
        #
        return ql.AnalyticHestonEngine(
            model,
            complex_log_formula,
            integration_,
            andersen_piterbarg_epsilon,
        )
    if rel_tolerance is not None and max_evaluations is not None:
        return ql.AnalyticHestonEngine(model, rel_tolerance, max_evaluations)
    return ql.AnalyticHestonEngine(model, integration_order)


@xlo.func(
    help="Return number of evaluations for a QuantLib AnalyticHestonEngine object.",
    args={
        "engine": "QuantLib AnalyticHestonEngine.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHestonEngineNumberOfEvaluations(
    engine: ql.AnalyticHestonEngine, trigger=None
) -> int:
    return engine.numberOfEvaluations()


@xlo.func(
    help="Create a QuantLib COSHestonEngine object.",
    args={
        "model": "QuantLib Heston model.",
        "l": "Truncation range parameter.",
        "n": "Number of expansion terms.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCOSHestonEngine(
    model: ql.HestonModel, l: float = 16.0, n: int = 200, trigger=None
) -> ql.COSHestonEngine:
    return ql.COSHestonEngine(model, l, n)


@xlo.func(
    help="Create a QuantLib ExponentialFittingHestonEngine object.",
    args={
        "model": "QuantLib Heston model.",
        "control_variate": "Control variate formula.",
        "scaling": "Optional scaling parameter.",
        "alpha": "Alpha parameter.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExponentialFittingHestonEngine(
    model: ql.HestonModel,
    control_variate: qAnalyticHestonComplexLogFormula = ql.AnalyticHestonEngine.OptimalCV,
    scaling: float = ql.nullDouble(),
    alpha: float = -0.5,
    trigger=None,
) -> ql.ExponentialFittingHestonEngine:
    return ql.ExponentialFittingHestonEngine(model, control_variate, scaling, alpha)


@xlo.func(
    help="Create a QuantLib AnalyticPDFHestonEngine object.",
    args={
        "model": "QuantLib Heston model.",
        "gauss_lobatto_eps": "Gauss-Lobatto tolerance.",
        "gauss_lobatto_integration_order": "Gauss-Lobatto integration order.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticPDFHestonEngine(
    model: ql.HestonModel,
    gauss_lobatto_eps: float = 1.0e-6,
    gauss_lobatto_integration_order: int = 10000,
    trigger=None,
) -> ql.AnalyticPDFHestonEngine:
    return ql.AnalyticPDFHestonEngine(
        model, gauss_lobatto_eps, gauss_lobatto_integration_order
    )


@xlo.func(
    help="Create a QuantLib AnalyticHestonForwardEuropeanEngine object.",
    args={
        "process": "QuantLib Heston process.",
        "integration_order": "Integration order.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHestonForwardEuropeanEngine(
    process: ql.HestonProcess,
    integration_order: int = 144,
    trigger=None,
) -> ql.AnalyticHestonForwardEuropeanEngine:
    return ql.AnalyticHestonForwardEuropeanEngine(process, integration_order)


@xlo.func(
    help="Create a QuantLib AnalyticPTDHestonEngine object.",
    args={
        "model": "QuantLib PiecewiseTimeDependentHestonModel.",
        "integration_order": "Integration order for default constructor.",
        "rel_tolerance": "Relative tolerance for adaptive integration constructor.",
        "max_evaluations": "Maximum evaluations for adaptive integration constructor.",
        "complex_log_formula": "Complex-log formula.",
        "integration": "AnalyticHestonEngine integration object.",
        "andersen_piterbarg_epsilon": "Andersen-Piterbarg epsilon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticPTDHestonEngine(
    model: ql.PiecewiseTimeDependentHestonModel,
    integration_order: int = 144,
    rel_tolerance: float = None,
    abs_tolerance: float = None,
    max_evaluations: int = None,
    complex_log_formula: qAnalyticPTDHestonComplexLogFormula = ql.AnalyticPTDHestonEngine.Gatheral,
    integration: qAnalyticHestonEngineIntegration = None,
    andersen_piterbarg_epsilon: float = 1.0e-8,
    trigger=None,
) -> ql.AnalyticPTDHestonEngine:
    if integration is not None:
        integration_ = _to_analytic_heston_engine_integration(
            integration,
            integration_order,
            rel_tolerance,
            abs_tolerance,
            max_evaluations,
        )
        return ql.AnalyticPTDHestonEngine(
            model,
            complex_log_formula,
            integration_,
            andersen_piterbarg_epsilon,
        )
    if rel_tolerance is not None and max_evaluations is not None:
        return ql.AnalyticPTDHestonEngine(model, rel_tolerance, max_evaluations)
    return ql.AnalyticPTDHestonEngine(model, integration_order)


## Analytic Heston-Hull-White engine


@xlo.func(
    help="Create a QuantLib AnalyticHestonHullWhiteEngine object.",
    args={
        "heston_model": "QuantLib Heston model.",
        "hull_white_model": "QuantLib Hull-White model.",
        "integration_order": "Integration order for default constructor.",
        "rel_tolerance": "Relative tolerance for adaptive integration constructor.",
        "max_evaluations": "Maximum evaluations for adaptive integration constructor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHestonHullWhiteEngine(
    heston_model: ql.HestonModel,
    hull_white_model: ql.HullWhite,
    integration_order: int = 144,
    rel_tolerance: float = None,
    max_evaluations: int = None,
    trigger=None,
) -> ql.AnalyticHestonHullWhiteEngine:
    if rel_tolerance is not None and max_evaluations is not None:
        return ql.AnalyticHestonHullWhiteEngine(
            heston_model, hull_white_model, rel_tolerance, max_evaluations
        )
    return ql.AnalyticHestonHullWhiteEngine(
        heston_model, hull_white_model, integration_order
    )


@xlo.func(
    help="Create a QuantLib AnalyticH1HWEngine object.",
    args={
        "heston_model": "QuantLib Heston model.",
        "hull_white_model": "QuantLib Hull-White model.",
        "rho_sr": "Equity-interest-rate correlation.",
        "integration_order": "Integration order for default constructor.",
        "rel_tolerance": "Relative tolerance for adaptive integration constructor.",
        "max_evaluations": "Maximum evaluations for adaptive integration constructor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticH1HWEngine(
    heston_model: ql.HestonModel,
    hull_white_model: ql.HullWhite,
    rho_sr: float,
    integration_order: int = 144,
    rel_tolerance: float = None,
    max_evaluations: int = None,
    trigger=None,
) -> ql.AnalyticH1HWEngine:
    if rel_tolerance is not None and max_evaluations is not None:
        return ql.AnalyticH1HWEngine(
            heston_model, hull_white_model, rho_sr, rel_tolerance, max_evaluations
        )
    return ql.AnalyticH1HWEngine(
        heston_model, hull_white_model, rho_sr, integration_order
    )


## Binomial tree engine


@xlo.func(
    help="Create a QuantLib binomial vanilla engine.",
    args={
        "process": "Generalized Black-Scholes process.",
        "engine_type": "Binomial engine type.",
        "steps": "Number of time steps.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBinomialVanillaEngine(
    process: ql.GeneralizedBlackScholesProcess,
    engine_type: qBinomialEngineType,
    steps: int,
    trigger=None,
) -> ql.PricingEngine:
    return ql.BinomialVanillaEngine(process, engine_type, steps)


## Finite differences engines


@xlo.func(
    help="Create a QuantLib FdmSchemeDesc object.",
    args={
        "scheme_type": "Finite-difference scheme type.",
        "theta": "Theta parameter.",
        "mu": "Mu parameter.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdmSchemeDesc(
    scheme_type: qFdmSchemeType = ql.FdmSchemeDesc.DouglasType,
    theta: float = 0.5,
    mu: float = 0.0,
    trigger=None,
) -> ql.FdmSchemeDesc:
    return ql.FdmSchemeDesc(_qFdmSchemeType(scheme_type), theta, mu)


@xlo.func(
    help="Create a QuantLib FdmSchemeDesc object from pre-defined name.",
    args={
        "scheme_desc": "Finite-difference scheme name.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdmSchemeDescByName(
    scheme_desc: qFdmSchemeDesc, trigger=None
) -> ql.FdmSchemeDesc:
    return scheme_desc


@xlo.func(
    help="Create a QuantLib FdmQuantoHelper object.",
    args={
        "domestic_ts": "Domestic yield term structure.",
        "foreign_ts": "Foreign yield term structure.",
        "fx_vol_ts": "FX Black volatility term structure.",
        "equity_fx_correlation": "Equity-FX correlation.",
        "exchange_rate_atm_level": "ATM exchange-rate level.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdmQuantoHelper(
    domestic_ts: ql.YieldTermStructureHandle,
    foreign_ts: ql.YieldTermStructureHandle,
    fx_vol_ts: ql.BlackVolTermStructureHandle,
    equity_fx_correlation: float,
    exchange_rate_atm_level: float,
    trigger=None,
) -> ql.FdmQuantoHelper:
    return ql.FdmQuantoHelper(
        domestic_ts.currentLink(),
        foreign_ts.currentLink(),
        fx_vol_ts.currentLink(),
        equity_fx_correlation,
        exchange_rate_atm_level,
    )


@xlo.func(
    help="Create a QuantLib FdBlackScholesVanillaEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "dividends": "Optional discrete dividends.",
        "quanto_helper": "Optional FdmQuantoHelper.",
        "t_grid": "Time grid size.",
        "x_grid": "Spatial grid size.",
        "damping_steps": "Damping steps.",
        "scheme_desc": "Finite-difference scheme description.",
        "local_vol": "Use local volatility if true.",
        "illegal_local_vol_overwrite": "Overwrite for illegal local vol values.",
        "cash_dividend_model": "Cash dividend model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdBlackScholesVanillaEngine(
    process: ql.GeneralizedBlackScholesProcess,
    dividends: xlo.Array(dims=1) = None,
    quanto_helper: ql.FdmQuantoHelper = None,
    t_grid: int = 100,
    x_grid: int = 100,
    damping_steps: int = 0,
    scheme_desc: ql.FdmSchemeDesc = None,
    local_vol: bool = False,
    illegal_local_vol_overwrite: float = -ql.nullDouble(),
    cash_dividend_model: qFdBlackScholesCashDividendModel = ql.FdBlackScholesVanillaEngine.Spot,
    trigger=None,
) -> ql.FdBlackScholesVanillaEngine:
    scheme_desc = scheme_desc if scheme_desc is not None else ql.FdmSchemeDesc.Douglas()
    dividends = _to_dividend_schedule(dividends)

    if quanto_helper is not None and len(dividends) > 0:
        return ql.FdBlackScholesVanillaEngine(
            process,
            dividends,
            quanto_helper,
            t_grid,
            x_grid,
            damping_steps,
            scheme_desc,
            local_vol,
            illegal_local_vol_overwrite,
            cash_dividend_model,
        )
    if quanto_helper is not None:
        return ql.FdBlackScholesVanillaEngine(
            process,
            quanto_helper,
            t_grid,
            x_grid,
            damping_steps,
            scheme_desc,
            local_vol,
            illegal_local_vol_overwrite,
            cash_dividend_model,
        )
    if len(dividends) > 0:
        return ql.FdBlackScholesVanillaEngine(
            process,
            dividends,
            t_grid,
            x_grid,
            damping_steps,
            scheme_desc,
            local_vol,
            illegal_local_vol_overwrite,
            cash_dividend_model,
        )
    return ql.FdBlackScholesVanillaEngine(
        process,
        t_grid,
        x_grid,
        damping_steps,
        scheme_desc,
        local_vol,
        illegal_local_vol_overwrite,
        cash_dividend_model,
    )


@xlo.func(
    help="Create a QuantLib FdBlackScholesShoutEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "dividends": "Optional discrete dividends.",
        "t_grid": "Time grid size.",
        "x_grid": "Spatial grid size.",
        "damping_steps": "Damping steps.",
        "scheme_desc": "Finite-difference scheme description.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdBlackScholesShoutEngine(
    process: ql.GeneralizedBlackScholesProcess,
    dividends: xlo.Array(dims=1) = None,
    t_grid: int = 100,
    x_grid: int = 100,
    damping_steps: int = 0,
    scheme_desc: ql.FdmSchemeDesc = None,
    trigger=None,
) -> ql.FdBlackScholesShoutEngine:
    scheme_desc = scheme_desc if scheme_desc is not None else ql.FdmSchemeDesc.Douglas()
    dividends = _to_dividend_schedule(dividends)
    if len(dividends) > 0:
        return ql.FdBlackScholesShoutEngine(
            process, dividends, t_grid, x_grid, damping_steps, scheme_desc
        )
    return ql.FdBlackScholesShoutEngine(
        process, t_grid, x_grid, damping_steps, scheme_desc
    )


@xlo.func(
    help="Create a QuantLib FdOrnsteinUhlenbeckVanillaEngine object.",
    args={
        "process": "Ornstein-Uhlenbeck process.",
        "discount_curve": "Discount yield term structure.",
        "dividends": "Optional discrete dividends.",
        "t_grid": "Time grid size.",
        "x_grid": "Spatial grid size.",
        "damping_steps": "Damping steps.",
        "epsilon": "Epsilon parameter.",
        "scheme_desc": "Finite-difference scheme description.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdOrnsteinUhlenbeckVanillaEngine(
    process: ql.OrnsteinUhlenbeckProcess,
    discount_curve: ql.YieldTermStructureHandle,
    dividends: xlo.Array(dims=1) = None,
    t_grid: int = 100,
    x_grid: int = 100,
    damping_steps: int = 0,
    epsilon: float = 1.0e-4,
    scheme_desc: ql.FdmSchemeDesc = None,
    trigger=None,
) -> ql.FdOrnsteinUhlenbeckVanillaEngine:
    scheme_desc = scheme_desc if scheme_desc is not None else ql.FdmSchemeDesc.Douglas()
    dividends = _to_dividend_schedule(dividends)
    if len(dividends) > 0:
        return ql.FdOrnsteinUhlenbeckVanillaEngine(
            process,
            discount_curve.currentLink(),
            dividends,
            t_grid,
            x_grid,
            damping_steps,
            epsilon,
            scheme_desc,
        )
    return ql.FdOrnsteinUhlenbeckVanillaEngine(
        process,
        discount_curve.currentLink(),
        t_grid,
        x_grid,
        damping_steps,
        epsilon,
        scheme_desc,
    )


@xlo.func(
    help="Create a QuantLib FdBatesVanillaEngine object.",
    args={
        "model": "Bates model.",
        "dividends": "Optional discrete dividends.",
        "t_grid": "Time grid size.",
        "x_grid": "Spatial grid size.",
        "v_grid": "Variance grid size.",
        "damping_steps": "Damping steps.",
        "scheme_desc": "Finite-difference scheme description.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdBatesVanillaEngine(
    model: ql.BatesModel,
    dividends: xlo.Array(dims=1) = None,
    t_grid: int = 100,
    x_grid: int = 100,
    v_grid: int = 50,
    damping_steps: int = 0,
    scheme_desc: ql.FdmSchemeDesc = None,
    trigger=None,
) -> ql.FdBatesVanillaEngine:
    scheme_desc = (
        scheme_desc if scheme_desc is not None else ql.FdmSchemeDesc.Hundsdorfer()
    )
    dividends = _to_dividend_schedule(dividends)
    if len(dividends) > 0:
        return ql.FdBatesVanillaEngine(
            model, dividends, t_grid, x_grid, v_grid, damping_steps, scheme_desc
        )
    return ql.FdBatesVanillaEngine(
        model, t_grid, x_grid, v_grid, damping_steps, scheme_desc
    )


@xlo.func(
    help="Create a QuantLib FdHestonVanillaEngine object.",
    args={
        "model": "Heston model.",
        "dividends": "Optional discrete dividends.",
        "quanto_helper": "Optional FdmQuantoHelper.",
        "t_grid": "Time grid size.",
        "x_grid": "Spatial grid size.",
        "v_grid": "Variance grid size.",
        "damping_steps": "Damping steps.",
        "scheme_desc": "Finite-difference scheme description.",
        "leverage_fct": "Optional leverage local-vol surface.",
        "mixing_factor": "Mixing factor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdHestonVanillaEngine(
    model: ql.HestonModel,
    dividends: xlo.Array(dims=1) = None,
    quanto_helper: ql.FdmQuantoHelper = None,
    t_grid: int = 100,
    x_grid: int = 100,
    v_grid: int = 50,
    damping_steps: int = 0,
    scheme_desc: ql.FdmSchemeDesc = ql.FdmSchemeDesc.Hundsdorfer(),
    leverage_fct: ql.LocalVolTermStructureHandle = None,
    mixing_factor: float = 1.0,
    trigger=None,
) -> ql.FdHestonVanillaEngine:
    dividends = _to_dividend_schedule(dividends)
    if leverage_fct is not None:
        leverage_fct = leverage_fct.currentLink()
    #
    if quanto_helper is not None and len(dividends) > 0:
        return ql.FdHestonVanillaEngine(
            model,
            dividends,
            quanto_helper,
            t_grid,
            x_grid,
            v_grid,
            damping_steps,
            scheme_desc,
            leverage_fct,
            mixing_factor,
        )
    if quanto_helper is not None:
        return ql.FdHestonVanillaEngine(
            model,
            quanto_helper,
            t_grid,
            x_grid,
            v_grid,
            damping_steps,
            scheme_desc,
            leverage_fct,
            mixing_factor,
        )
    if len(dividends) > 0:
        return ql.FdHestonVanillaEngine(
            model,
            dividends,
            t_grid,
            x_grid,
            v_grid,
            damping_steps,
            scheme_desc,
            leverage_fct,
            mixing_factor,
        )
    return ql.FdHestonVanillaEngine(
        model,
        t_grid,
        x_grid,
        v_grid,
        damping_steps,
        scheme_desc,
        leverage_fct,
        mixing_factor,
    )


@xlo.func(
    help="Create a QuantLib FdCEVVanillaEngine object.",
    args={
        "f0": "Initial forward level.",
        "alpha": "Alpha parameter.",
        "beta": "Beta parameter.",
        "discount_curve": "Discount yield term structure handle.",
        "t_grid": "Time grid size.",
        "x_grid": "Spatial grid size.",
        "damping_steps": "Damping steps.",
        "scaling_factor": "Scaling factor.",
        "eps": "Epsilon parameter.",
        "scheme_desc": "Finite-difference scheme description.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdCEVVanillaEngine(
    f0: float,
    alpha: float,
    beta: float,
    discount_curve: ql.YieldTermStructureHandle,
    t_grid: int = 50,
    x_grid: int = 400,
    damping_steps: int = 0,
    scaling_factor: float = 1.0,
    eps: float = 1.0e-4,
    scheme_desc: ql.FdmSchemeDesc = ql.FdmSchemeDesc.Douglas(),
    trigger=None,
) -> ql.FdCEVVanillaEngine:
    return ql.FdCEVVanillaEngine(
        f0,
        alpha,
        beta,
        discount_curve,
        t_grid,
        x_grid,
        damping_steps,
        scaling_factor,
        eps,
        scheme_desc,
    )


@xlo.func(
    help="Create a QuantLib FdSabrVanillaEngine object.",
    args={
        "f0": "Initial forward level.",
        "alpha": "Alpha parameter.",
        "beta": "Beta parameter.",
        "nu": "Nu parameter.",
        "rho": "Rho parameter.",
        "discount_curve": "Discount yield term structure handle.",
        "t_grid": "Time grid size.",
        "f_grid": "Forward grid size.",
        "x_grid": "Spatial grid size.",
        "damping_steps": "Damping steps.",
        "scaling_factor": "Scaling factor.",
        "eps": "Epsilon parameter.",
        "scheme_desc": "Finite-difference scheme description.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdSabrVanillaEngine(
    f0: float,
    alpha: float,
    beta: float,
    nu: float,
    rho: float,
    discount_curve: ql.YieldTermStructureHandle,
    t_grid: int = 50,
    f_grid: int = 400,
    x_grid: int = 50,
    damping_steps: int = 0,
    scaling_factor: float = 1.0,
    eps: float = 1.0e-4,
    scheme_desc: ql.FdmSchemeDesc = ql.FdmSchemeDesc.Hundsdorfer(),
    trigger=None,
) -> ql.FdSabrVanillaEngine:
    return ql.FdSabrVanillaEngine(
        f0,
        alpha,
        beta,
        nu,
        rho,
        discount_curve,
        t_grid,
        f_grid,
        x_grid,
        damping_steps,
        scaling_factor,
        eps,
        scheme_desc,
    )


@xlo.func(
    help="Create a QuantLib FdHestonHullWhiteVanillaEngine object.",
    args={
        "model": "Heston model.",
        "hull_white_process": "Hull-White process.",
        "corr_equity_short_rate": "Equity short-rate correlation.",
        "dividends": "Optional discrete dividends.",
        "t_grid": "Time grid size.",
        "x_grid": "Spatial grid size.",
        "v_grid": "Variance grid size.",
        "r_grid": "Rate grid size.",
        "damping_steps": "Damping steps.",
        "control_variate": "Use control variate if true.",
        "scheme_desc": "Finite-difference scheme description.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdHestonHullWhiteVanillaEngine(
    model: ql.HestonModel,
    hull_white_process: ql.HullWhiteProcess,
    corr_equity_short_rate: float,
    dividends: xlo.Array(dims=1) = None,
    t_grid: int = 50,
    x_grid: int = 100,
    v_grid: int = 40,
    r_grid: int = 20,
    damping_steps: int = 0,
    control_variate: bool = True,
    scheme_desc: ql.FdmSchemeDesc = ql.FdmSchemeDesc.Hundsdorfer(),
    trigger=None,
) -> ql.FdHestonHullWhiteVanillaEngine:
    dividends = _to_dividend_schedule(dividends)
    if len(dividends) > 0:
        return ql.FdHestonHullWhiteVanillaEngine(
            model,
            hull_white_process,
            dividends,
            corr_equity_short_rate,
            t_grid,
            x_grid,
            v_grid,
            r_grid,
            damping_steps,
            control_variate,
            scheme_desc,
        )
    return ql.FdHestonHullWhiteVanillaEngine(
        model,
        hull_white_process,
        corr_equity_short_rate,
        t_grid,
        x_grid,
        v_grid,
        r_grid,
        damping_steps,
        control_variate,
        scheme_desc,
    )


## Monte Carlo engines


@xlo.func(
    help="Create a QuantLib Monte Carlo European engine.",
    args={
        "process": "Generalized Black-Scholes process.",
        "traits": "Random number generator traits.",
        "time_steps": "Optional number of time steps.",
        "time_steps_per_year": "Optional number of time steps per year.",
        "brownian_bridge": "Use Brownian bridge if true.",
        "antithetic_variate": "Use antithetic variates if true.",
        "required_samples": "Optional required number of samples.",
        "required_tolerance": "Optional required tolerance.",
        "max_samples": "Optional maximum number of samples.",
        "seed": "Random seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCEuropeanEngine(
    process: ql.GeneralizedBlackScholesProcess,
    traits: qMCTraits,
    time_steps: int = ql.nullInt(),
    time_steps_per_year: int = ql.nullInt(),
    brownian_bridge: bool = False,
    antithetic_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    trigger=None,
) -> ql.PricingEngine:
    return ql.MCEuropeanEngine(
        process,
        traits,
        time_steps,
        time_steps_per_year,
        brownian_bridge,
        antithetic_variate,
        required_samples,
        required_tolerance,
        max_samples,
        seed,
    )


@xlo.func(
    help="Create a QuantLib Monte Carlo American engine.",
    args={
        "process": "Generalized Black-Scholes process.",
        "traits": "Random number generator traits.",
        "time_steps": "Optional number of time steps.",
        "time_steps_per_year": "Optional number of time steps per year.",
        "antithetic_variate": "Use antithetic variates if true.",
        "control_variate": "Use control variate if true.",
        "required_samples": "Optional required number of samples.",
        "required_tolerance": "Optional required tolerance.",
        "max_samples": "Optional maximum number of samples.",
        "seed": "Random seed.",
        "polynom_order": "Least-squares basis polynomial order.",
        "polynom_type": "Least-squares basis polynomial type.",
        "n_calibration_samples": "Number of calibration samples.",
        "antithetic_variate_calibration": "Optional antithetic variate flag for calibration.",
        "seed_calibration": "Optional calibration seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCAmericanEngine(
    process: ql.GeneralizedBlackScholesProcess,
    traits: qMCTraits,
    time_steps: int = ql.nullInt(),
    time_steps_per_year: int = ql.nullInt(),
    antithetic_variate: bool = False,
    control_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    polynom_order: int = 2,
    polynom_type: qLsmBasisSystemPolynomialType = ql.LsmBasisSystem.Monomial,
    n_calibration_samples: int = 2048,
    antithetic_variate_calibration: bool = None,
    seed_calibration: int = ql.nullInt(),
    trigger=None,
) -> ql.PricingEngine:
    return ql.MCAmericanEngine(
        process,
        traits,
        time_steps,
        time_steps_per_year,
        antithetic_variate,
        control_variate,
        required_samples,
        required_tolerance,
        max_samples,
        seed,
        polynom_order,
        polynom_type,
        n_calibration_samples,
        antithetic_variate_calibration,
        seed_calibration,
    )


@xlo.func(
    help="Create a QuantLib Monte Carlo digital engine.",
    args={
        "process": "Generalized Black-Scholes process.",
        "traits": "Random number generator traits.",
        "time_steps": "Optional number of time steps.",
        "time_steps_per_year": "Optional number of time steps per year.",
        "brownian_bridge": "Use Brownian bridge if true.",
        "antithetic_variate": "Use antithetic variates if true.",
        "required_samples": "Optional required number of samples.",
        "required_tolerance": "Optional required tolerance.",
        "max_samples": "Optional maximum number of samples.",
        "seed": "Random seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCDigitalEngine(
    process: ql.GeneralizedBlackScholesProcess,
    traits: qMCTraits,
    time_steps: int = ql.nullInt(),
    time_steps_per_year: int = ql.nullInt(),
    brownian_bridge: bool = False,
    antithetic_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    trigger=None,
) -> ql.PricingEngine:
    return ql.MCDigitalEngine(
        process,
        traits,
        time_steps,
        time_steps_per_year,
        brownian_bridge,
        antithetic_variate,
        required_samples,
        required_tolerance,
        max_samples,
        seed,
    )


@xlo.func(
    help="Create a QuantLib Monte Carlo European Heston engine.",
    args={
        "process": "Heston process.",
        "traits": "Random number generator traits.",
        "time_steps": "Optional number of time steps.",
        "time_steps_per_year": "Optional number of time steps per year.",
        "antithetic_variate": "Use antithetic variates if true.",
        "required_samples": "Optional required number of samples.",
        "required_tolerance": "Optional required tolerance.",
        "max_samples": "Optional maximum number of samples.",
        "seed": "Random seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCEuropeanHestonEngine(
    process: ql.HestonProcess,
    traits: qMCTraits,
    time_steps: int = ql.nullInt(),
    time_steps_per_year: int = ql.nullInt(),
    antithetic_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    trigger=None,
) -> ql.PricingEngine:
    return ql.MCEuropeanHestonEngine(
        process,
        traits,
        time_steps,
        time_steps_per_year,
        antithetic_variate,
        required_samples,
        required_tolerance,
        max_samples,
        seed,
    )


@xlo.func(
    help="Create a QuantLib Monte Carlo forward European Black-Scholes engine.",
    args={
        "process": "Generalized Black-Scholes process.",
        "traits": "Random number generator traits.",
        "time_steps": "Optional number of time steps.",
        "time_steps_per_year": "Optional number of time steps per year.",
        "brownian_bridge": "Use Brownian bridge if true.",
        "antithetic_variate": "Use antithetic variates if true.",
        "required_samples": "Optional required number of samples.",
        "required_tolerance": "Optional required tolerance.",
        "max_samples": "Optional maximum number of samples.",
        "seed": "Random seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCForwardEuropeanBSEngine(
    process: ql.GeneralizedBlackScholesProcess,
    traits: qMCTraits,
    time_steps: int = ql.nullInt(),
    time_steps_per_year: int = ql.nullInt(),
    brownian_bridge: bool = False,
    antithetic_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    trigger=None,
) -> ql.PricingEngine:
    return ql.MCForwardEuropeanBSEngine(
        process,
        traits,
        time_steps,
        time_steps_per_year,
        brownian_bridge,
        antithetic_variate,
        required_samples,
        required_tolerance,
        max_samples,
        seed,
    )


@xlo.func(
    help="Create a QuantLib Monte Carlo forward European Heston engine.",
    args={
        "process": "Heston process.",
        "traits": "Random number generator traits.",
        "time_steps": "Optional number of time steps.",
        "time_steps_per_year": "Optional number of time steps per year.",
        "antithetic_variate": "Use antithetic variates if true.",
        "required_samples": "Optional required number of samples.",
        "required_tolerance": "Optional required tolerance.",
        "max_samples": "Optional maximum number of samples.",
        "seed": "Random seed.",
        "control_variate": "Use control variate if true.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCForwardEuropeanHestonEngine(
    process: ql.HestonProcess,
    traits: qMCTraits,
    time_steps: int = ql.nullInt(),
    time_steps_per_year: int = ql.nullInt(),
    antithetic_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    control_variate: bool = False,
    trigger=None,
) -> ql.PricingEngine:
    return ql.MCForwardEuropeanHestonEngine(
        process,
        traits,
        time_steps,
        time_steps_per_year,
        antithetic_variate,
        required_samples,
        required_tolerance,
        max_samples,
        seed,
        control_variate,
    )


## QD+ and QD Fixed Point Engines


@xlo.func(
    help="Create a QuantLib QdPlusAmericanEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "interpolation_points": "Interpolation points.",
        "solver_type": "Solver type.",
        "eps": "Solver tolerance.",
        "max_iter": "Optional maximum iterations.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQdPlusAmericanEngine(
    process: ql.GeneralizedBlackScholesProcess,
    interpolation_points: int = 8,
    solver_type: qQdPlusSolverType = ql.QdPlusAmericanEngine.Halley,
    eps: float = 1.0e-6,
    max_iter: int = ql.nullInt(),
    trigger=None,
) -> ql.QdPlusAmericanEngine:
    return ql.QdPlusAmericanEngine(
        process, interpolation_points, solver_type, eps, max_iter
    )


@xlo.func(
    help="Create a QuantLib QdFpLegendreScheme object.",
    args={
        "l": "Outer-order parameter.",
        "m": "Inner-order parameter.",
        "n": "Quadrature parameter.",
        "p": "Polynomial parameter.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQdFpLegendreScheme(
    l: int, m: int, n: int, p: int, trigger=None
) -> ql.QdFpLegendreScheme:
    return ql.QdFpLegendreScheme(l, m, n, p)


@xlo.func(
    help="Create a QuantLib QdFpLegendreTanhSinhScheme object.",
    args={
        "l": "Outer-order parameter.",
        "m": "Inner-order parameter.",
        "n": "Quadrature parameter.",
        "eps": "Quadrature tolerance.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQdFpLegendreTanhSinhScheme(
    l: int, m: int, n: int, eps: float, trigger=None
) -> ql.QdFpLegendreTanhSinhScheme:
    return ql.QdFpLegendreTanhSinhScheme(l, m, n, eps)


@xlo.func(
    help="Create a QuantLib QdFpTanhSinhIterationScheme object.",
    args={
        "m": "Inner-order parameter.",
        "n": "Quadrature parameter.",
        "eps": "Quadrature tolerance.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQdFpTanhSinhIterationScheme(
    m: int, n: int, eps: float, trigger=None
) -> ql.QdFpTanhSinhIterationScheme:
    return ql.QdFpTanhSinhIterationScheme(m, n, eps)


@xlo.func(
    help="Return QdFpAmericanEngine fast iteration scheme.",
    group=EXCEL_GROUP_NAME,
)
def qlQdFpAmericanEngineFastScheme(trigger=None) -> ql.QdFpIterationScheme:
    return ql.QdFpAmericanEngine.fastScheme()


@xlo.func(
    help="Return QdFpAmericanEngine accurate iteration scheme.",
    group=EXCEL_GROUP_NAME,
)
def qlQdFpAmericanEngineAccurateScheme(trigger=None) -> ql.QdFpIterationScheme:
    return ql.QdFpAmericanEngine.accurateScheme()


@xlo.func(
    help="Return QdFpAmericanEngine high-precision iteration scheme.",
    group=EXCEL_GROUP_NAME,
)
def qlQdFpAmericanEngineHighPrecisionScheme(trigger=None) -> ql.QdFpIterationScheme:
    return ql.QdFpAmericanEngine.highPrecisionScheme()


@xlo.func(
    help="Create a QuantLib QdFpAmericanEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "iteration_scheme": "Optional fixed-point iteration scheme.",
        "fixed_point_equation": "Fixed-point equation type.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQdFpAmericanEngine(
    process: ql.GeneralizedBlackScholesProcess,
    iteration_scheme: qQdFpIterationScheme = ql.QdFpAmericanEngine.accurateScheme(),
    fixed_point_equation: qQdFpFixedPointEquation = ql.QdFpAmericanEngine.Auto,
    trigger=None,
) -> ql.QdFpAmericanEngine:
    return ql.QdFpAmericanEngine(process, iteration_scheme, fixed_point_equation)


## Other pricing engines


@xlo.func(
    help="Create a QuantLib AnalyticCEVEngine object.",
    args={
        "f0": "Initial forward level.",
        "alpha": "Alpha parameter.",
        "beta": "Beta parameter.",
        "discount_curve": "Discount yield term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticCEVEngine(
    f0: float,
    alpha: float,
    beta: float,
    discount_curve: ql.YieldTermStructureHandle,
    trigger=None,
) -> ql.AnalyticCEVEngine:
    return ql.AnalyticCEVEngine(f0, alpha, beta, discount_curve)


@xlo.func(
    help="Create a QuantLib BatesModel object.",
    args={
        "process": "Bates process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBatesModel(process: ql.BatesProcess, trigger=None) -> ql.BatesModel:
    return ql.BatesModel(process)


@xlo.func(
    help="Create a QuantLib BatesEngine object.",
    args={
        "model": "Bates model.",
        "integration_order": "Integration order for default constructor.",
        "rel_tolerance": "Relative tolerance for adaptive integration constructor.",
        "max_evaluations": "Maximum evaluations for adaptive integration constructor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBatesEngine(
    model: ql.BatesModel,
    integration_order: int = 144,
    rel_tolerance: float = None,
    max_evaluations: int = None,
    trigger=None,
) -> ql.BatesEngine:
    if rel_tolerance is not None and max_evaluations is not None:
        return ql.BatesEngine(model, rel_tolerance, max_evaluations)
    return ql.BatesEngine(model, integration_order)


@xlo.func(
    help="Create a QuantLib VarianceGammaEngine object.",
    args={
        "process": "Variance-Gamma process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlVarianceGammaEngine(
    process: ql.VarianceGammaProcess, trigger=None
) -> ql.VarianceGammaEngine:
    return ql.VarianceGammaEngine(process)


@xlo.func(
    help="Create a QuantLib FFTVarianceGammaEngine object.",
    args={
        "process": "Variance-Gamma process.",
        "log_strike_spacing": "Log-strike spacing.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFFTVarianceGammaEngine(
    process: ql.VarianceGammaProcess,
    log_strike_spacing: float = 0.001,
    trigger=None,
) -> ql.FFTVarianceGammaEngine:
    return ql.FFTVarianceGammaEngine(process, log_strike_spacing)


@xlo.func(
    help="Create a QuantLib GJRGARCHModel object.",
    args={
        "process": "GJR-GARCH process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGJRGARCHModel(process: ql.GJRGARCHProcess, trigger=None) -> ql.GJRGARCHModel:
    return ql.GJRGARCHModel(process)


@xlo.func(
    help="Create a QuantLib AnalyticGJRGARCHEngine object.",
    args={
        "model": "GJR-GARCH model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticGJRGARCHEngine(
    model: ql.GJRGARCHModel, trigger=None
) -> ql.AnalyticGJRGARCHEngine:
    return ql.AnalyticGJRGARCHEngine(model)


# Calculators

## BlackCalculator


@xlo.func(
    help="Create a QuantLib BlackCalculator object.",
    args={
        "payoff": "Striked payoff.",
        "forward": "Forward level.",
        "std_dev": "Standard deviation.",
        "discount": "Discount factor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculator(
    payoff: ql.StrikedTypePayoff,
    forward: float,
    std_dev: float,
    discount: float = 1.0,
    trigger=None,
) -> ql.BlackCalculator:
    return ql.BlackCalculator(payoff, forward, std_dev, discount)


@xlo.func(
    help="Return BlackCalculator value.",
    args={
        "calculator": "QuantLib BlackCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorValue(calculator: ql.BlackCalculator, trigger=None) -> float:
    return calculator.value()


@xlo.func(
    help="Return BlackCalculator delta.",
    args={
        "calculator": "QuantLib BlackCalculator.",
        "spot": "Spot level.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorDelta(
    calculator: ql.BlackCalculator, spot: float, trigger=None
) -> float:
    return calculator.delta(spot)


@xlo.func(
    help="Return BlackCalculator gamma.",
    args={
        "calculator": "QuantLib BlackCalculator.",
        "spot": "Spot level.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorGamma(
    calculator: ql.BlackCalculator, spot: float, trigger=None
) -> float:
    return calculator.gamma(spot)


@xlo.func(
    help="Return BlackCalculator vega.",
    args={
        "calculator": "QuantLib BlackCalculator.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorVega(
    calculator: ql.BlackCalculator, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.vega(maturity)


@xlo.func(
    help="Return BlackCalculator theta.",
    args={
        "calculator": "QuantLib BlackCalculator.",
        "spot": "Spot level.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorTheta(
    calculator: ql.BlackCalculator, spot: float, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.theta(spot, maturity)


@xlo.func(
    help="Return BlackCalculator theta per day.",
    args={
        "calculator": "QuantLib BlackCalculator.",
        "spot": "Spot level.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorThetaPerDay(
    calculator: ql.BlackCalculator, spot: float, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.thetaPerDay(spot, maturity)


@xlo.func(
    help="Return BlackCalculator rho.",
    args={
        "calculator": "QuantLib BlackCalculator.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorRho(
    calculator: ql.BlackCalculator, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.rho(maturity)


@xlo.func(
    help="Return BlackCalculator dividend rho.",
    args={
        "calculator": "QuantLib BlackCalculator.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorDividendRho(
    calculator: ql.BlackCalculator, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.dividendRho(maturity)


@xlo.func(
    help="Return BlackCalculator forward delta.",
    args={
        "calculator": "QuantLib BlackCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorDeltaForward(
    calculator: ql.BlackCalculator, trigger=None
) -> float:
    return calculator.deltaForward()


@xlo.func(
    help="Return BlackCalculator forward gamma.",
    args={
        "calculator": "QuantLib BlackCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorGammaForward(
    calculator: ql.BlackCalculator, trigger=None
) -> float:
    return calculator.gammaForward()


@xlo.func(
    help="Return BlackCalculator elasticity.",
    args={
        "calculator": "QuantLib BlackCalculator.",
        "spot": "Spot level.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorElasticity(
    calculator: ql.BlackCalculator, spot: float, trigger=None
) -> float:
    return calculator.elasticity(spot)


@xlo.func(
    help="Return BlackCalculator forward elasticity.",
    args={
        "calculator": "QuantLib BlackCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorElasticityForward(
    calculator: ql.BlackCalculator, trigger=None
) -> float:
    return calculator.elasticityForward()


@xlo.func(
    help="Return BlackCalculator in-the-money cash probability.",
    args={
        "calculator": "QuantLib BlackCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorITMCashProbability(
    calculator: ql.BlackCalculator, trigger=None
) -> float:
    return calculator.itmCashProbability()


@xlo.func(
    help="Return BlackCalculator in-the-money asset probability.",
    args={
        "calculator": "QuantLib BlackCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorITMAssetProbability(
    calculator: ql.BlackCalculator, trigger=None
) -> float:
    return calculator.itmAssetProbability()


@xlo.func(
    help="Return BlackCalculator strike sensitivity.",
    args={
        "calculator": "QuantLib BlackCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorStrikeSensitivity(
    calculator: ql.BlackCalculator, trigger=None
) -> float:
    return calculator.strikeSensitivity()


@xlo.func(
    help="Return BlackCalculator strike gamma.",
    args={
        "calculator": "QuantLib BlackCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorStrikeGamma(calculator: ql.BlackCalculator, trigger=None) -> float:
    return calculator.strikeGamma()


@xlo.func(
    help="Return BlackCalculator alpha.",
    args={
        "calculator": "QuantLib BlackCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorAlpha(calculator: ql.BlackCalculator, trigger=None) -> float:
    return calculator.alpha()


@xlo.func(
    help="Return BlackCalculator vanna.",
    args={
        "calculator": "QuantLib BlackCalculator.",
        "spot": "Spot level.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorVanna(
    calculator: ql.BlackCalculator, spot: float, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.vanna(spot, maturity)


@xlo.func(
    help="Return BlackCalculator volga.",
    args={
        "calculator": "QuantLib BlackCalculator.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorVolga(
    calculator: ql.BlackCalculator, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.volga(maturity)


@xlo.func(
    help="Return BlackCalculator beta.",
    args={
        "calculator": "QuantLib BlackCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalculatorBeta(calculator: ql.BlackCalculator, trigger=None) -> float:
    return calculator.beta()


## BachelierCalculator


@xlo.func(
    help="Create a QuantLib BachelierCalculator object.",
    args={
        "payoff": "Striked payoff.",
        "forward": "Forward level.",
        "std_dev": "Standard deviation.",
        "discount": "Discount factor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculator(
    payoff: ql.StrikedTypePayoff,
    forward: float,
    std_dev: float,
    discount: float = 1.0,
    trigger=None,
) -> ql.BachelierCalculator:
    return ql.BachelierCalculator(payoff, forward, std_dev, discount)


@xlo.func(
    help="Return BachelierCalculator value.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorValue(
    calculator: ql.BachelierCalculator, trigger=None
) -> float:
    return calculator.value()


@xlo.func(
    help="Return BachelierCalculator delta.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
        "spot": "Spot level.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorDelta(
    calculator: ql.BachelierCalculator, spot: float, trigger=None
) -> float:
    return calculator.delta(spot)


@xlo.func(
    help="Return BachelierCalculator gamma.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
        "spot": "Spot level.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorGamma(
    calculator: ql.BachelierCalculator, spot: float, trigger=None
) -> float:
    return calculator.gamma(spot)


@xlo.func(
    help="Return BachelierCalculator vega.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorVega(
    calculator: ql.BachelierCalculator, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.vega(maturity)


@xlo.func(
    help="Return BachelierCalculator theta.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
        "spot": "Spot level.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorTheta(
    calculator: ql.BachelierCalculator, spot: float, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.theta(spot, maturity)


@xlo.func(
    help="Return BachelierCalculator theta per day.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
        "spot": "Spot level.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorThetaPerDay(
    calculator: ql.BachelierCalculator, spot: float, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.thetaPerDay(spot, maturity)


@xlo.func(
    help="Return BachelierCalculator rho.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorRho(
    calculator: ql.BachelierCalculator, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.rho(maturity)


@xlo.func(
    help="Return BachelierCalculator dividend rho.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorDividendRho(
    calculator: ql.BachelierCalculator, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.dividendRho(maturity)


@xlo.func(
    help="Return BachelierCalculator forward delta.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorDeltaForward(
    calculator: ql.BachelierCalculator, trigger=None
) -> float:
    return calculator.deltaForward()


@xlo.func(
    help="Return BachelierCalculator forward gamma.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorGammaForward(
    calculator: ql.BachelierCalculator, trigger=None
) -> float:
    return calculator.gammaForward()


@xlo.func(
    help="Return BachelierCalculator elasticity.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
        "spot": "Spot level.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorElasticity(
    calculator: ql.BachelierCalculator, spot: float, trigger=None
) -> float:
    return calculator.elasticity(spot)


@xlo.func(
    help="Return BachelierCalculator forward elasticity.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorElasticityForward(
    calculator: ql.BachelierCalculator, trigger=None
) -> float:
    return calculator.elasticityForward()


@xlo.func(
    help="Return BachelierCalculator in-the-money cash probability.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorITMCashProbability(
    calculator: ql.BachelierCalculator, trigger=None
) -> float:
    return calculator.itmCashProbability()


@xlo.func(
    help="Return BachelierCalculator in-the-money asset probability.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorITMAssetProbability(
    calculator: ql.BachelierCalculator, trigger=None
) -> float:
    return calculator.itmAssetProbability()


@xlo.func(
    help="Return BachelierCalculator strike sensitivity.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorStrikeSensitivity(
    calculator: ql.BachelierCalculator, trigger=None
) -> float:
    return calculator.strikeSensitivity()


@xlo.func(
    help="Return BachelierCalculator strike gamma.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorStrikeGamma(
    calculator: ql.BachelierCalculator, trigger=None
) -> float:
    return calculator.strikeGamma()


@xlo.func(
    help="Return BachelierCalculator alpha.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorAlpha(
    calculator: ql.BachelierCalculator, trigger=None
) -> float:
    return calculator.alpha()


@xlo.func(
    help="Return BachelierCalculator vanna.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorVanna(
    calculator: ql.BachelierCalculator, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.vanna(maturity)


@xlo.func(
    help="Return BachelierCalculator volga.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
        "maturity": "Maturity in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorVolga(
    calculator: ql.BachelierCalculator, maturity: float = 1.0, trigger=None
) -> float:
    return calculator.volga(maturity)


@xlo.func(
    help="Return BachelierCalculator beta.",
    args={
        "calculator": "QuantLib BachelierCalculator.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCalculatorBeta(
    calculator: ql.BachelierCalculator, trigger=None
) -> float:
    return calculator.beta()


## DeltaVolQuote


@xlo.func(
    help="Create a QuantLib DeltaVolQuote object.",
    args={
        "delta": "Strike in delta quotation.",
        "vol": "Volatility quote handle.",
        "maturity": "Maturity in years.",
        "delta_type": "Delta convention.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDeltaVolQuote(
    delta: float,
    vol: qQuoteHandle,
    maturity: float,
    delta_type: qDeltaVolQuoteDeltaType,
    trigger=None,
) -> ql.DeltaVolQuote:
    return ql.DeltaVolQuote(
        delta,
        vol,
        maturity,
        delta_type,
    )


@xlo.func(
    help="Create a QuantLib DeltaVolQuote object for ATM strike.",
    args={
        "vol": "Volatility quote handle.",
        "maturity": "Maturity in years.",
        "delta_type": "Delta convention.",
        "atm_type": "ATM type.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDeltaVolQuoteAtm(
    vol: qQuoteHandle,
    delta_type: qDeltaVolQuoteDeltaType,
    maturity: float,
    atm_type: qDeltaVolQuoteAtmType,
) -> ql.DeltaVolQuote:
    return ql.DeltaVolQuote(
        vol,
        delta_type,
        maturity,
        atm_type,
    )


@xlo.func(
    help="Return DeltaVolQuote delta.",
    args={
        "quote": "QuantLib DeltaVolQuote.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDeltaVolQuoteDelta(quote: ql.DeltaVolQuote, trigger=None) -> float:
    return quote.delta()


@xlo.func(
    help="Return DeltaVolQuote maturity.",
    args={
        "quote": "QuantLib DeltaVolQuote.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDeltaVolQuoteMaturity(quote: ql.DeltaVolQuote, trigger=None) -> float:
    return quote.maturity()


@xlo.func(
    help="Return DeltaVolQuote delta type.",
    args={
        "quote": "QuantLib DeltaVolQuote.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDeltaVolQuoteDeltaType(quote: ql.DeltaVolQuote, trigger=None) -> str:
    return first_key(QL_DELTA_VOL_QUOTE_DELTA_TYPE, quote.deltaType())


@xlo.func(
    help="Return DeltaVolQuote ATM type.",
    args={
        "quote": "QuantLib DeltaVolQuote.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDeltaVolQuoteAtmType(quote: ql.DeltaVolQuote, trigger=None) -> str:
    return first_key(QL_DELTA_VOL_QUOTE_ATM_TYPE, quote.atmType())


@xlo.func(
    help="Return DeltaVolQuote value.",
    args={
        "quote": "QuantLib DeltaVolQuote.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDeltaVolQuoteValue(quote: ql.DeltaVolQuote, trigger=None) -> float:
    return quote.value()


@xlo.func(
    help="Return whether DeltaVolQuote is valid.",
    args={
        "quote": "QuantLib DeltaVolQuote.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDeltaVolQuoteIsValid(quote: ql.DeltaVolQuote, trigger=None) -> bool:
    return quote.isValid()
