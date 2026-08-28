import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import _to_date_list
from .options import qMCTraits
from .utilities import (
    UNKNOWN_KEY,
    UNKNOWN_VALUE,
    enum_value,
    to_float_matrix,
    to_object_list,
)


QL_OPERATOR_SPLITTING_SPREAD_ENGINE_ORDER = {
    "FIRST": ql.OperatorSplittingSpreadEngine.First,
    "SECOND": ql.OperatorSplittingSpreadEngine.Second,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qOperatorSplittingSpreadEngineOrder(s: str) -> int:
    return enum_value(s, QL_OPERATOR_SPLITTING_SPREAD_ENGINE_ORDER)


@xlo.converter()
def qOperatorSplittingSpreadEngineOrder(s: str) -> int:
    return _qOperatorSplittingSpreadEngineOrder(s)


@xlo.func(
    help="Create a QuantLib MinBasketPayoff object.",
    args={"payoff": "Payoff for each basket component."},
    group=EXCEL_GROUP_NAME,
)
def qlMinBasketPayoff(payoff: ql.Payoff, trigger=None) -> ql.MinBasketPayoff:
    return ql.MinBasketPayoff(payoff)


@xlo.func(
    help="Create a QuantLib MaxBasketPayoff object.",
    args={"payoff": "Payoff for each basket component."},
    group=EXCEL_GROUP_NAME,
)
def qlMaxBasketPayoff(payoff: ql.Payoff, trigger=None) -> ql.MaxBasketPayoff:
    return ql.MaxBasketPayoff(payoff)


@xlo.func(
    help="Create a QuantLib AverageBasketPayoff object.",
    args={
        "payoff": "Payoff for each basket component.",
        "weights": "Array of basket weights.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAverageBasketPayoff(
    payoff: ql.Payoff, weights: xlo.Array(dims=1), trigger=None
) -> ql.AverageBasketPayoff:
    return ql.AverageBasketPayoff(payoff, weights)


@xlo.func(
    help="Create a QuantLib SpreadBasketPayoff object.",
    args={"payoff": "Payoff for the spread."},
    group=EXCEL_GROUP_NAME,
)
def qlSpreadBasketPayoff(payoff: ql.Payoff, trigger=None) -> ql.SpreadBasketPayoff:
    return ql.SpreadBasketPayoff(payoff)


@xlo.func(
    help="Create a QuantLib BasketOption object.",
    args={
        "payoff": "Basket payoff.",
        "exercise": "Exercise specification.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBasketOption(
    payoff: ql.BasketPayoff, exercise: ql.Exercise, trigger=None
) -> ql.BasketOption:
    return ql.BasketOption(payoff, exercise)


@xlo.func(
    help="Create a QuantLib MCEuropeanBasketEngine object.",
    args={
        "process": "Stochastic process array.",
        "traits": "Monte Carlo traits (PR or LD).",
        "time_steps": "Number of time steps (optional).",
        "time_steps_per_year": "Number of time steps per year (optional).",
        "brownian_bridge": "Use Brownian bridge.",
        "antithetic_variate": "Use antithetic variate.",
        "required_samples": "Required number of samples (optional).",
        "required_tolerance": "Required tolerance (optional).",
        "max_samples": "Maximum number of samples (optional).",
        "seed": "Random seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCEuropeanBasketEngine(
    process: ql.StochasticProcessArray,
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
    if traits == "pseudorandom":
        cls = ql.MCPREuropeanBasketEngine
    elif traits == "lowdiscrepancy":
        cls = ql.MCLDEuropeanBasketEngine
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
        seed,
    )


@xlo.func(
    help="Create a QuantLib MCAmericanBasketEngine object.",
    args={
        "process": "Stochastic process array.",
        "traits": "Monte Carlo traits (PR or LD).",
        "time_steps": "Number of time steps (optional).",
        "time_steps_per_year": "Number of time steps per year (optional).",
        "brownian_bridge": "Use Brownian bridge.",
        "antithetic_variate": "Use antithetic variate.",
        "required_samples": "Required number of samples (optional).",
        "required_tolerance": "Required tolerance (optional).",
        "max_samples": "Maximum number of samples (optional).",
        "seed": "Random seed.",
        "n_calibration_samples": "Number of calibration samples.",
        "polynom_order": "Polynomial order.",
        "polynom_type": "Polynomial type.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCAmericanBasketEngine(
    process: ql.StochasticProcessArray,
    traits: qMCTraits,
    time_steps: int = ql.nullInt(),
    time_steps_per_year: int = ql.nullInt(),
    brownian_bridge: bool = False,
    antithetic_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    n_calibration_samples: int = 2048,
    polynom_order: int = 2,
    polynom_type: int = ql.LsmBasisSystem.Monomial,
    trigger=None,
) -> ql.PricingEngine:
    if traits == "pseudorandom":
        cls = ql.MCPRAmericanBasketEngine
    elif traits == "lowdiscrepancy":
        cls = ql.MCLDAmericanBasketEngine
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
        seed,
        n_calibration_samples,
        polynom_order,
        polynom_type,
    )


@xlo.func(
    help="Create a QuantLib StulzEngine object.",
    args={
        "process1": "First generalized Black-Scholes process.",
        "process2": "Second generalized Black-Scholes process.",
        "correlation": "Correlation between processes.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlStulzEngine(
    process1: ql.GeneralizedBlackScholesProcess,
    process2: ql.GeneralizedBlackScholesProcess,
    correlation: float,
    trigger=None,
) -> ql.StulzEngine:
    return ql.StulzEngine(process1, process2, correlation)


@xlo.func(
    help="Create a QuantLib KirkEngine object.",
    args={
        "process1": "First generalized Black-Scholes process.",
        "process2": "Second generalized Black-Scholes process.",
        "correlation": "Correlation between processes.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlKirkEngine(
    process1: ql.GeneralizedBlackScholesProcess,
    process2: ql.GeneralizedBlackScholesProcess,
    correlation: float,
    trigger=None,
) -> ql.KirkEngine:
    return ql.KirkEngine(process1, process2, correlation)


@xlo.func(
    help="Create a QuantLib BjerksundStenslandSpreadEngine object.",
    args={
        "process1": "First generalized Black-Scholes process.",
        "process2": "Second generalized Black-Scholes process.",
        "correlation": "Correlation between processes.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBjerksundStenslandSpreadEngine(
    process1: ql.GeneralizedBlackScholesProcess,
    process2: ql.GeneralizedBlackScholesProcess,
    correlation: float,
    trigger=None,
) -> ql.BjerksundStenslandSpreadEngine:
    return ql.BjerksundStenslandSpreadEngine(process1, process2, correlation)


@xlo.func(
    help="Create a QuantLib OperatorSplittingSpreadEngine object.",
    args={
        "process1": "First generalized Black-Scholes process.",
        "process2": "Second generalized Black-Scholes process.",
        "correlation": "Correlation between processes.",
        "order": "Operator splitting order (FIRST or SECOND).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOperatorSplittingSpreadEngine(
    process1: ql.GeneralizedBlackScholesProcess,
    process2: ql.GeneralizedBlackScholesProcess,
    correlation: float,
    order: qOperatorSplittingSpreadEngineOrder = ql.OperatorSplittingSpreadEngine.Second,
    trigger=None,
) -> ql.OperatorSplittingSpreadEngine:
    return ql.OperatorSplittingSpreadEngine(process1, process2, correlation, order)


@xlo.func(
    help="Create a QuantLib Fd2dBlackScholesVanillaEngine object.",
    args={
        "process1": "First generalized Black-Scholes process.",
        "process2": "Second generalized Black-Scholes process.",
        "correlation": "Correlation between processes.",
        "x_grid": "First spatial grid size.",
        "y_grid": "Second spatial grid size.",
        "t_grid": "Time grid size.",
        "damping_steps": "Damping steps.",
        "scheme_desc": "Finite-difference scheme description.",
        "local_vol": "Use local volatility if true.",
        "illegal_local_vol_overwrite": "Overwrite for illegal local vol values.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFd2dBlackScholesVanillaEngine(
    process1: ql.GeneralizedBlackScholesProcess,
    process2: ql.GeneralizedBlackScholesProcess,
    correlation: float,
    x_grid: int = 100,
    y_grid: int = 100,
    t_grid: int = 50,
    damping_steps: int = 0,
    scheme_desc: ql.FdmSchemeDesc = ql.FdmSchemeDesc.Hundsdorfer(),
    local_vol: bool = False,
    illegal_local_vol_overwrite: float = -ql.nullDouble(),
    trigger=None,
) -> ql.Fd2dBlackScholesVanillaEngine:
    return ql.Fd2dBlackScholesVanillaEngine(
        process1,
        process2,
        correlation,
        x_grid,
        y_grid,
        t_grid,
        damping_steps,
        scheme_desc,
        local_vol,
        illegal_local_vol_overwrite,
    )


def _processes_and_correlation(processes, correlation):
    return (
        to_object_list(processes, ql.GeneralizedBlackScholesProcess),
        ql.Matrix(to_float_matrix(correlation)),
    )


@xlo.func(
    help="Create a QuantLib ChoiBasketEngine object.",
    args={
        "processes": "Array of generalized Black-Scholes processes.",
        "correlation": "Correlation matrix.",
        "lambda_": "Integration parameter.",
        "max_nr_integration_steps": "Maximum integration steps.",
        "calc_fwd_delta": "Calculate forward delta.",
        "control_variate": "Use control variate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlChoiBasketEngine(
    processes: xlo.Array(dims=1),
    correlation: xlo.Array,
    lambda_: float = 10.0,
    max_nr_integration_steps: int = ql.nullInt(),
    calc_fwd_delta: bool = False,
    control_variate: bool = False,
    trigger=None,
) -> ql.ChoiBasketEngine:
    processes, correlation = _processes_and_correlation(processes, correlation)
    return ql.ChoiBasketEngine(
        processes,
        correlation,
        lambda_,
        max_nr_integration_steps,
        calc_fwd_delta,
        control_variate,
    )


@xlo.func(
    help="Create a QuantLib DengLiZhouBasketEngine object.",
    args={
        "processes": "Array of generalized Black-Scholes processes.",
        "correlation": "Correlation matrix.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDengLiZhouBasketEngine(
    processes: xlo.Array(dims=1), correlation: xlo.Array, trigger=None
) -> ql.DengLiZhouBasketEngine:
    processes, correlation = _processes_and_correlation(processes, correlation)
    return ql.DengLiZhouBasketEngine(processes, correlation)


@xlo.func(
    help="Create a QuantLib FdndimBlackScholesVanillaEngine object.",
    args={
        "processes": "Array of generalized Black-Scholes processes.",
        "correlation": "Correlation matrix.",
        "x_grid": "Spatial grid size.",
        "t_grid": "Time grid size.",
        "damping_steps": "Damping steps.",
        "scheme_desc": "Finite-difference scheme description.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdndimBlackScholesVanillaEngine(
    processes: xlo.Array(dims=1),
    correlation: xlo.Array,
    x_grid: int,
    t_grid: int = 50,
    damping_steps: int = 0,
    scheme_desc: ql.FdmSchemeDesc = ql.FdmSchemeDesc.Hundsdorfer(),
    trigger=None,
) -> ql.FdndimBlackScholesVanillaEngine:
    processes, correlation = _processes_and_correlation(processes, correlation)
    return ql.FdndimBlackScholesVanillaEngine(
        processes, correlation, x_grid, t_grid, damping_steps, scheme_desc
    )


@xlo.func(
    help="Create a QuantLib EverestOption object.",
    args={
        "notional": "Option notional.",
        "guarantee": "Guaranteed rate.",
        "exercise": "Exercise specification.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEverestOption(
    notional: float, guarantee: float, exercise: ql.Exercise, trigger=None
) -> ql.EverestOption:
    return ql.EverestOption(notional, guarantee, exercise)


@xlo.func(
    help="Create a QuantLib MCEverestEngine object.",
    args={
        "process": "Stochastic process array.",
        "traits": "Monte Carlo traits (PR or LD).",
        "time_steps": "Number of time steps (optional).",
        "time_steps_per_year": "Number of time steps per year (optional).",
        "brownian_bridge": "Use Brownian bridge.",
        "antithetic_variate": "Use antithetic variate.",
        "required_samples": "Required number of samples (optional).",
        "required_tolerance": "Required tolerance (optional).",
        "max_samples": "Maximum number of samples (optional).",
        "seed": "Random seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCEverestEngine(
    process: ql.StochasticProcessArray,
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
    if traits == "pseudorandom":
        cls = ql.MCPREverestEngine
    elif traits == "lowdiscrepancy":
        cls = ql.MCLDEverestEngine
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
        seed,
    )


@xlo.func(
    help="Create a QuantLib HimalayaOption object.",
    args={
        "fixing_dates": "Array of fixing dates.",
        "strike": "Option strike.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHimalayaOption(
    fixing_dates: xlo.Array(dims=1), strike: float, trigger=None
) -> ql.HimalayaOption:
    return ql.HimalayaOption(_to_date_list(fixing_dates), strike)


@xlo.func(
    help="Create a QuantLib MCHimalayaEngine object.",
    args={
        "process": "Stochastic process array.",
        "traits": "Monte Carlo traits (PR or LD).",
        "brownian_bridge": "Use Brownian bridge.",
        "antithetic_variate": "Use antithetic variate.",
        "required_samples": "Required number of samples (optional).",
        "required_tolerance": "Required tolerance (optional).",
        "max_samples": "Maximum number of samples (optional).",
        "seed": "Random seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCHimalayaEngine(
    process: ql.StochasticProcessArray,
    traits: qMCTraits,
    brownian_bridge: bool = False,
    antithetic_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    trigger=None,
) -> ql.PricingEngine:
    if traits == "pseudorandom":
        cls = ql.MCPRHimalayaEngine
    elif traits == "lowdiscrepancy":
        cls = ql.MCLDHimalayaEngine
    else:
        raise RuntimeError(f"unknown MC traits: {traits}")
    return cls(
        process,
        brownian_bridge,
        antithetic_variate,
        required_samples,
        required_tolerance,
        max_samples,
        seed,
    )