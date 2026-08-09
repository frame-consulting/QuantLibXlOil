import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate
from .options import qBinomialEngineType, qMCTraits
from .ratehelpers import qQuoteHandle
from .utilities import enum_value, first_key, to_object_list, UNKNOWN_KEY, UNKNOWN_VALUE

QL_BARRIER_TYPE = {
    "DI": ql.Barrier.DownIn,
    "DOWNIN": ql.Barrier.DownIn,
    "DO": ql.Barrier.DownOut,
    "DOWNOUT": ql.Barrier.DownOut,
    "UI": ql.Barrier.UpIn,
    "UPIN": ql.Barrier.UpIn,
    "UO": ql.Barrier.UpOut,
    "UPOUT": ql.Barrier.UpOut,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_PARTIAL_BARRIER_RANGE = {
    "START": ql.PartialBarrier.Start,
    "ENDB1": ql.PartialBarrier.EndB1,
    "ENDB2": ql.PartialBarrier.EndB2,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_DOUBLE_BARRIER_TYPE = {
    "KIKO": ql.DoubleBarrier.KIKO,
    "KNOCKIN": ql.DoubleBarrier.KnockIn,
    "KNOCKOUT": ql.DoubleBarrier.KnockOut,
    "KOKI": ql.DoubleBarrier.KOKI,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_VANNA_VOLGA_DOUBLE_BARRIER_ENGINE_TYPE = {
    "IK": ql.VannaVolgaIKDoubleBarrierEngine,
    "WO": ql.VannaVolgaWODoubleBarrierEngine,
}


def _qBarrierType(s: str) -> int:
    return enum_value(s, QL_BARRIER_TYPE)


@xlo.converter()
def qBarrierType(s: str) -> int:
    return _qBarrierType(s)


def _qPartialBarrierRange(s: str) -> int:
    return enum_value(s, QL_PARTIAL_BARRIER_RANGE)


@xlo.converter()
def qPartialBarrierRange(s: str) -> int:
    return _qPartialBarrierRange(s)


def _qDoubleBarrierType(s: str) -> int:
    return enum_value(s, QL_DOUBLE_BARRIER_TYPE)


@xlo.converter()
def qDoubleBarrierType(s: str) -> int:
    return _qDoubleBarrierType(s)


def _qVannaVolgaDoubleBarrierEngineType(name: str):
    return enum_value(name, QL_VANNA_VOLGA_DOUBLE_BARRIER_ENGINE_TYPE, type)


@xlo.converter()
def qVannaVolgaDoubleBarrierEngineType(name: str):
    return _qVannaVolgaDoubleBarrierEngineType(name)


@xlo.func(
    help="Create a QuantLib BarrierOption object.",
    args={
        "barrier_type": "Barrier type.",
        "barrier": "Barrier level.",
        "rebate": "Rebate amount.",
        "payoff": "Striked type payoff.",
        "exercise": "Exercise specification.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBarrierOption(
    barrier_type: qBarrierType,
    barrier: float,
    rebate: float,
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.BarrierOption:
    return ql.BarrierOption(barrier_type, barrier, rebate, payoff, exercise)


@xlo.func(
    help="Create a QuantLib QuantoBarrierOption object.",
    args={
        "barrier_type": "Barrier type.",
        "barrier": "Barrier level.",
        "rebate": "Rebate amount.",
        "payoff": "Striked type payoff.",
        "exercise": "Exercise specification.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoBarrierOption(
    barrier_type: qBarrierType,
    barrier: float,
    rebate: float,
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.QuantoBarrierOption:
    return ql.QuantoBarrierOption(barrier_type, barrier, rebate, payoff, exercise)


@xlo.func(
    help="Create a QuantLib PartialTimeBarrierOption object.",
    args={
        "barrier_type": "Barrier type.",
        "barrier_range": "Partial barrier range.",
        "barrier": "Barrier level.",
        "rebate": "Rebate amount.",
        "cover_event_date": "Cover event date.",
        "payoff": "Striked type payoff.",
        "exercise": "Exercise specification.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPartialTimeBarrierOption(
    barrier_type: qBarrierType,
    barrier_range: qPartialBarrierRange,
    barrier: float,
    rebate: float,
    cover_event_date: qDate,
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.PartialTimeBarrierOption:
    return ql.PartialTimeBarrierOption(
        barrier_type,
        barrier_range,
        barrier,
        rebate,
        cover_event_date,
        payoff,
        exercise,
    )


@xlo.func(
    help="Return BarrierOption implied volatility.",
    args={
        "option": "QuantLib BarrierOption.",
        "target_value": "Target option value.",
        "process": "Generalized Black-Scholes process.",
        "dividends": "Optional dividend schedule.",
        "accuracy": "Solver accuracy.",
        "max_evaluations": "Maximum evaluations.",
        "min_vol": "Minimum volatility.",
        "max_vol": "Maximum volatility.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBarrierOptionImpliedVolatility(
    option: ql.BarrierOption,
    target_value: float,
    process: ql.GeneralizedBlackScholesProcess,
    dividends: xlo.Array(dims=1) = None,
    accuracy: float = 1.0e-4,
    max_evaluations: int = 100,
    min_vol: float = 1.0e-4,
    max_vol: float = 4.0,
    trigger=None,
) -> float:
    dividends = to_object_list(dividends, ql.Dividend)
    if len(dividends) > 0:
        return option.impliedVolatility(
            target_value,
            process,
            dividends,
            accuracy,
            max_evaluations,
            min_vol,
            max_vol,
        )
    return option.impliedVolatility(
        target_value,
        process,
        accuracy,
        max_evaluations,
        min_vol,
        max_vol,
    )


@xlo.func(
    help="Create a QuantLib AnalyticPartialTimeBarrierOptionEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticPartialTimeBarrierOptionEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticPartialTimeBarrierOptionEngine:
    return ql.AnalyticPartialTimeBarrierOptionEngine(process)


@xlo.func(
    help="Create a QuantLib AnalyticBarrierEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticBarrierEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticBarrierEngine:
    return ql.AnalyticBarrierEngine(process)


@xlo.func(
    help="Create a QuantLib MCBarrierEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "traits": "Monte Carlo traits (PR or LD).",
        "time_steps": "Number of time steps (optional).",
        "time_steps_per_year": "Number of time steps per year (optional).",
        "brownian_bridge": "Use Brownian bridge.",
        "antithetic_variate": "Use antithetic variate.",
        "required_samples": "Required number of samples (optional).",
        "required_tolerance": "Required tolerance (optional).",
        "max_samples": "Maximum number of samples (optional).",
        "is_biased": "Use biased estimator.",
        "seed": "Random seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCBarrierEngine(
    process: ql.GeneralizedBlackScholesProcess,
    traits: qMCTraits,
    time_steps: int = ql.nullInt(),
    time_steps_per_year: int = ql.nullInt(),
    brownian_bridge: bool = False,
    antithetic_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    is_biased: bool = False,
    seed: int = 0,
    trigger=None,
) -> ql.PricingEngine:
    if traits == "pseudorandom":
        cls = ql.MCPRBarrierEngine
    elif traits == "lowdiscrepancy":
        cls = ql.MCLDBarrierEngine
    else:
        raise RuntimeError(f"unknown MC traits: {traits}")
    return cls(
        process,
        time_steps,
        time_steps_per_year,
        brownian_bridge,
        antithetic_variate,
        required_samples,
        required_tolerance,
        max_samples,
        is_biased,
        seed,
    )


@xlo.func(
    help="Create a QuantLib QuantoBarrierEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "foreign_risk_free_rate": "Foreign risk-free yield term structure handle.",
        "exchange_rate_volatility": "Exchange-rate volatility handle.",
        "correlation": "Correlation quote handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoBarrierEngine(
    process: ql.GeneralizedBlackScholesProcess,
    foreign_risk_free_rate: ql.YieldTermStructureHandle,
    exchange_rate_volatility: ql.BlackVolTermStructureHandle,
    correlation: qQuoteHandle,
    trigger=None,
) -> ql.QuantoBarrierEngine:
    return ql.QuantoBarrierEngine(
        process,
        foreign_risk_free_rate,
        exchange_rate_volatility,
        correlation,
    )


@xlo.func(
    help="Create a QuantLib FdBlackScholesBarrierEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "dividends": "Optional discrete dividends.",
        "t_grid": "Time grid size.",
        "x_grid": "Spatial grid size.",
        "damping_steps": "Damping steps.",
        "scheme_desc": "Finite-difference scheme description.",
        "local_vol": "Use local volatility if true.",
        "illegal_local_vol_overwrite": "Overwrite for illegal local vol values.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdBlackScholesBarrierEngine(
    process: ql.GeneralizedBlackScholesProcess,
    dividends: xlo.Array(dims=1) = None,
    t_grid: int = 100,
    x_grid: int = 100,
    damping_steps: int = 0,
    scheme_desc: ql.FdmSchemeDesc = None,
    local_vol: bool = False,
    illegal_local_vol_overwrite: float = -ql.nullDouble(),
    trigger=None,
) -> ql.FdBlackScholesBarrierEngine:
    scheme_desc = scheme_desc if scheme_desc is not None else ql.FdmSchemeDesc.Douglas()
    dividends = to_object_list(dividends, ql.Dividend)
    if len(dividends) > 0:
        return ql.FdBlackScholesBarrierEngine(
            process,
            dividends,
            t_grid,
            x_grid,
            damping_steps,
            scheme_desc,
            local_vol,
            illegal_local_vol_overwrite,
        )
    return ql.FdBlackScholesBarrierEngine(
        process,
        t_grid,
        x_grid,
        damping_steps,
        scheme_desc,
        local_vol,
        illegal_local_vol_overwrite,
    )


@xlo.func(
    help="Create a QuantLib FdBlackScholesRebateEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "dividends": "Optional discrete dividends.",
        "t_grid": "Time grid size.",
        "x_grid": "Spatial grid size.",
        "damping_steps": "Damping steps.",
        "scheme_desc": "Finite-difference scheme description.",
        "local_vol": "Use local volatility if true.",
        "illegal_local_vol_overwrite": "Overwrite for illegal local vol values.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdBlackScholesRebateEngine(
    process: ql.GeneralizedBlackScholesProcess,
    dividends: xlo.Array(dims=1) = None,
    t_grid: int = 100,
    x_grid: int = 100,
    damping_steps: int = 0,
    scheme_desc: ql.FdmSchemeDesc = None,
    local_vol: bool = False,
    illegal_local_vol_overwrite: float = -ql.nullDouble(),
    trigger=None,
) -> ql.FdBlackScholesRebateEngine:
    scheme_desc = scheme_desc if scheme_desc is not None else ql.FdmSchemeDesc.Douglas()
    dividends = to_object_list(dividends, ql.Dividend)
    if len(dividends) > 0:
        return ql.FdBlackScholesRebateEngine(
            process,
            dividends,
            t_grid,
            x_grid,
            damping_steps,
            scheme_desc,
            local_vol,
            illegal_local_vol_overwrite,
        )
    return ql.FdBlackScholesRebateEngine(
        process,
        t_grid,
        x_grid,
        damping_steps,
        scheme_desc,
        local_vol,
        illegal_local_vol_overwrite,
    )


@xlo.func(
    help="Create a QuantLib FdHestonBarrierEngine object.",
    args={
        "model": "Heston model.",
        "dividends": "Optional discrete dividends.",
        "t_grid": "Time grid size.",
        "x_grid": "Spatial grid size.",
        "v_grid": "Variance grid size.",
        "damping_steps": "Damping steps.",
        "scheme_desc": "Finite-difference scheme description.",
        "leverage_fct": "Optional leverage local volatility term structure.",
        "mixing_factor": "Mixing factor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdHestonBarrierEngine(
    model: ql.HestonModel,
    dividends: xlo.Array(dims=1) = None,
    t_grid: int = 100,
    x_grid: int = 100,
    v_grid: int = 50,
    damping_steps: int = 0,
    scheme_desc: ql.FdmSchemeDesc = None,
    leverage_fct: ql.LocalVolTermStructure = None,
    mixing_factor: float = 1.0,
    trigger=None,
) -> ql.FdHestonBarrierEngine:
    scheme_desc = (
        scheme_desc if scheme_desc is not None else ql.FdmSchemeDesc.Hundsdorfer()
    )
    dividends = to_object_list(dividends, ql.Dividend)

    if len(dividends) > 0:
        return ql.FdHestonBarrierEngine(
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
    return ql.FdHestonBarrierEngine(
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
    help="Create a QuantLib FdHestonRebateEngine object.",
    args={
        "model": "Heston model.",
        "dividends": "Optional discrete dividends.",
        "t_grid": "Time grid size.",
        "x_grid": "Spatial grid size.",
        "v_grid": "Variance grid size.",
        "damping_steps": "Damping steps.",
        "scheme_desc": "Finite-difference scheme description.",
        "leverage_fct": "Optional leverage local volatility term structure.",
        "mixing_factor": "Mixing factor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdHestonRebateEngine(
    model: ql.HestonModel,
    dividends: xlo.Array(dims=1) = None,
    t_grid: int = 100,
    x_grid: int = 100,
    v_grid: int = 50,
    damping_steps: int = 0,
    scheme_desc: ql.FdmSchemeDesc = None,
    leverage_fct: ql.LocalVolTermStructure = None,
    mixing_factor: float = 1.0,
    trigger=None,
) -> ql.FdHestonRebateEngine:
    scheme_desc = (
        scheme_desc if scheme_desc is not None else ql.FdmSchemeDesc.Hundsdorfer()
    )
    dividends = to_object_list(dividends, ql.Dividend)

    if len(dividends) > 0:
        return ql.FdHestonRebateEngine(
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
    return ql.FdHestonRebateEngine(
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
    help="Create a QuantLib AnalyticBinaryBarrierEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticBinaryBarrierEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticBinaryBarrierEngine:
    return ql.AnalyticBinaryBarrierEngine(process)


@xlo.func(
    help="Create a QuantLib binomial barrier engine.",
    args={
        "process": "Generalized Black-Scholes process.",
        "engine_type": "Binomial engine type.",
        "steps": "Number of time steps.",
        "max_steps": "Maximum number of time steps for Boyle-Lau adjustment.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBinomialBarrierEngine(
    process: ql.GeneralizedBlackScholesProcess,
    engine_type: qBinomialEngineType,
    steps: int,
    max_steps: int = 0,
    trigger=None,
) -> ql.PricingEngine:
    if engine_type == "coxrossrubinstein":
        cls = ql.BinomialCRRBarrierEngine
    elif engine_type == "jarrowrudd":
        cls = ql.BinomialJRBarrierEngine
    elif engine_type == "eqp":
        cls = ql.BinomialEQPBarrierEngine
    elif engine_type == "trigeorgis":
        cls = ql.BinomialTrigeorgisBarrierEngine
    elif engine_type == "tian":
        cls = ql.BinomialTianBarrierEngine
    elif engine_type == "leisenreimer":
        cls = ql.BinomialLRBarrierEngine
    elif engine_type == "joshi4":
        cls = ql.BinomialJ4BarrierEngine
    else:
        raise RuntimeError(f"unknown binomial engine type: {engine_type}")

    return cls(process, steps, max_steps)


@xlo.func(
    help="Create a QuantLib DoubleBarrierOption object.",
    args={
        "barrier_type": "Double barrier type.",
        "barrier_lo": "Lower barrier level.",
        "barrier_hi": "Upper barrier level.",
        "rebate": "Rebate amount.",
        "payoff": "Striked type payoff.",
        "exercise": "Exercise specification.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDoubleBarrierOption(
    barrier_type: qDoubleBarrierType,
    barrier_lo: float,
    barrier_hi: float,
    rebate: float,
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.DoubleBarrierOption:
    return ql.DoubleBarrierOption(
        barrier_type,
        barrier_lo,
        barrier_hi,
        rebate,
        payoff,
        exercise,
    )


@xlo.func(
    help="Create a QuantLib QuantoDoubleBarrierOption object.",
    args={
        "barrier_type": "Double barrier type.",
        "barrier_lo": "Lower barrier level.",
        "barrier_hi": "Upper barrier level.",
        "rebate": "Rebate amount.",
        "payoff": "Striked type payoff.",
        "exercise": "Exercise specification.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoDoubleBarrierOption(
    barrier_type: qDoubleBarrierType,
    barrier_lo: float,
    barrier_hi: float,
    rebate: float,
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.QuantoDoubleBarrierOption:
    return ql.QuantoDoubleBarrierOption(
        barrier_type,
        barrier_lo,
        barrier_hi,
        rebate,
        payoff,
        exercise,
    )


@xlo.func(
    help="Return QuantoDoubleBarrierOption qvega.",
    args={
        "option": "QuantLib QuantoDoubleBarrierOption.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoDoubleBarrierOptionQvega(
    option: ql.QuantoDoubleBarrierOption, trigger=None
) -> float:
    return option.qvega()


@xlo.func(
    help="Return QuantoDoubleBarrierOption qrho.",
    args={
        "option": "QuantLib QuantoDoubleBarrierOption.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoDoubleBarrierOptionQrho(
    option: ql.QuantoDoubleBarrierOption, trigger=None
) -> float:
    return option.qrho()


@xlo.func(
    help="Return QuantoDoubleBarrierOption qlambda.",
    args={
        "option": "QuantLib QuantoDoubleBarrierOption.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlQuantoDoubleBarrierOptionQlambda(
    option: ql.QuantoDoubleBarrierOption, trigger=None
) -> float:
    return option.qlambda()


@xlo.func(
    help="Create a QuantLib AnalyticDoubleBarrierEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "series": "Series expansion truncation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticDoubleBarrierEngine(
    process: ql.GeneralizedBlackScholesProcess,
    series: int = 5,
    trigger=None,
) -> ql.AnalyticDoubleBarrierEngine:
    return ql.AnalyticDoubleBarrierEngine(process, series)


@xlo.func(
    help="Create a QuantLib FdHestonDoubleBarrierEngine object.",
    args={
        "model": "Heston model.",
        "t_grid": "Time grid size.",
        "x_grid": "Spatial grid size.",
        "v_grid": "Variance grid size.",
        "damping_steps": "Damping steps.",
        "scheme_desc": "Finite-difference scheme description.",
        "leverage_fct": "Optional leverage local volatility term structure.",
        "mixing_factor": "Mixing factor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdHestonDoubleBarrierEngine(
    model: ql.HestonModel,
    t_grid: int = 100,
    x_grid: int = 100,
    v_grid: int = 50,
    damping_steps: int = 0,
    scheme_desc: ql.FdmSchemeDesc = None,
    leverage_fct: ql.LocalVolTermStructure = None,
    mixing_factor: float = 1.0,
    trigger=None,
) -> ql.FdHestonDoubleBarrierEngine:
    scheme_desc = (
        scheme_desc if scheme_desc is not None else ql.FdmSchemeDesc.Hundsdorfer()
    )
    return ql.FdHestonDoubleBarrierEngine(
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
    help="Create a QuantLib SuoWangDoubleBarrierEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "series": "Series expansion truncation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSuoWangDoubleBarrierEngine(
    process: ql.GeneralizedBlackScholesProcess,
    series: int = 5,
    trigger=None,
) -> ql.SuoWangDoubleBarrierEngine:
    return ql.SuoWangDoubleBarrierEngine(process, series)


@xlo.func(
    help="Create a QuantLib AnalyticDoubleBarrierBinaryEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticDoubleBarrierBinaryEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticDoubleBarrierBinaryEngine:
    return ql.AnalyticDoubleBarrierBinaryEngine(process)


@xlo.func(
    help="Create a QuantLib binomial double barrier engine.",
    args={
        "process": "Generalized Black-Scholes process.",
        "engine_type": "Binomial engine type.",
        "steps": "Number of time steps.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBinomialDoubleBarrierEngine(
    process: ql.GeneralizedBlackScholesProcess,
    engine_type: qBinomialEngineType,
    steps: int,
    trigger=None,
) -> ql.PricingEngine:
    if engine_type == "coxrossrubinstein":
        cls = ql.BinomialCRRDoubleBarrierEngine
    elif engine_type == "jarrowrudd":
        cls = ql.BinomialJRDoubleBarrierEngine
    elif engine_type == "eqp":
        cls = ql.BinomialEQPDoubleBarrierEngine
    elif engine_type == "trigeorgis":
        cls = ql.BinomialTrigeorgisDoubleBarrierEngine
    elif engine_type == "tian":
        cls = ql.BinomialTianDoubleBarrierEngine
    elif engine_type == "leisenreimer":
        cls = ql.BinomialLRDoubleBarrierEngine
    elif engine_type == "joshi4":
        cls = ql.BinomialJ4DoubleBarrierEngine
    else:
        raise RuntimeError(f"unknown binomial engine type: {engine_type}")

    return cls(process, steps)


@xlo.func(
    help="Create a QuantLib TwoAssetBarrierOption object.",
    args={
        "barrier_type": "Barrier type.",
        "barrier": "Barrier level.",
        "payoff": "Striked type payoff.",
        "exercise": "Exercise specification.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTwoAssetBarrierOption(
    barrier_type: qBarrierType,
    barrier: float,
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.TwoAssetBarrierOption:
    return ql.TwoAssetBarrierOption(barrier_type, barrier, payoff, exercise)


@xlo.func(
    help="Create a QuantLib AnalyticTwoAssetBarrierEngine object.",
    args={
        "process1": "First Generalized Black-Scholes process.",
        "process2": "Second Generalized Black-Scholes process.",
        "rho": "Correlation quote handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticTwoAssetBarrierEngine(
    process1: ql.GeneralizedBlackScholesProcess,
    process2: ql.GeneralizedBlackScholesProcess,
    rho: qQuoteHandle,
    trigger=None,
) -> ql.AnalyticTwoAssetBarrierEngine:
    return ql.AnalyticTwoAssetBarrierEngine(process1, process2, rho)


@xlo.func(
    help="Create a QuantLib SoftBarrierOption object.",
    args={
        "barrier_type": "Barrier type.",
        "barrier_lo": "Lower barrier level.",
        "barrier_hi": "Upper barrier level.",
        "payoff": "Striked type payoff.",
        "exercise": "Exercise specification.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSoftBarrierOption(
    barrier_type: qBarrierType,
    barrier_lo: float,
    barrier_hi: float,
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.SoftBarrierOption:
    return ql.SoftBarrierOption(barrier_type, barrier_lo, barrier_hi, payoff, exercise)


@xlo.func(
    help="Return SoftBarrierOption implied volatility.",
    args={
        "option": "QuantLib SoftBarrierOption.",
        "price": "Target option value.",
        "process": "Generalized Black-Scholes process.",
        "accuracy": "Solver accuracy.",
        "max_evaluations": "Maximum evaluations.",
        "min_vol": "Minimum volatility.",
        "max_vol": "Maximum volatility.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSoftBarrierOptionImpliedVolatility(
    option: ql.SoftBarrierOption,
    price: float,
    process: ql.GeneralizedBlackScholesProcess,
    accuracy: float = 1.0e-4,
    max_evaluations: int = 100,
    min_vol: float = 1.0e-6,
    max_vol: float = 4.0,
    trigger=None,
) -> float:
    return option.impliedVolatility(
        price,
        process,
        accuracy,
        max_evaluations,
        min_vol,
        max_vol,
    )


@xlo.func(
    help="Create a QuantLib AnalyticSoftBarrierEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticSoftBarrierEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticSoftBarrierEngine:
    return ql.AnalyticSoftBarrierEngine(process)


@xlo.func(
    help="Return Barrier type name.",
    args={
        "barrier_type": "QuantLib Barrier::Type value.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBarrierTypeName(barrier_type: int, trigger=None) -> str:
    return first_key(QL_BARRIER_TYPE, barrier_type, UNKNOWN_VALUE)


@xlo.func(
    help="Return PartialBarrier range name.",
    args={
        "barrier_range": "QuantLib PartialBarrier::Range value.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPartialBarrierRangeName(barrier_range: int, trigger=None) -> str:
    return first_key(QL_PARTIAL_BARRIER_RANGE, barrier_range, UNKNOWN_VALUE)


@xlo.func(
    help="Return DoubleBarrier type name.",
    args={
        "barrier_type": "QuantLib DoubleBarrier::Type value.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDoubleBarrierTypeName(barrier_type: int, trigger=None) -> str:
    return first_key(QL_DOUBLE_BARRIER_TYPE, barrier_type, UNKNOWN_VALUE)
