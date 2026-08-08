import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate, _to_date_list
from .options import qMCTraits
from .ratehelpers import qQuoteHandle
from .utilities import (
    enum_value,
    UNKNOWN_KEY,
    UNKNOWN_VALUE,
    to_float_list,
)

# Enumerations

QL_AVERAGE_TYPE = {
    "ARITHMETIC": ql.Average.Arithmetic,
    "GEOMETRIC": ql.Average.Geometric,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qAverageType(s: str) -> int:
    return enum_value(s, QL_AVERAGE_TYPE)


@xlo.converter()
def qAverageType(s: str) -> int:
    return _qAverageType(s)


# Asian Option Classes


@xlo.func(
    help="Create a QuantLib ContinuousAveragingAsianOption object.",
    args={
        "average_type": "Average type (ARITHMETIC or GEOMETRIC).",
        "payoff": "Striked type payoff.",
        "exercise": "Exercise specification.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlContinuousAveragingAsianOption(
    average_type: qAverageType,
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.ContinuousAveragingAsianOption:
    return ql.ContinuousAveragingAsianOption(average_type, payoff, exercise)


@xlo.func(
    help="Create a QuantLib ContinuousAveragingAsianOption object with start date.",
    args={
        "average_type": "Average type (ARITHMETIC or GEOMETRIC).",
        "start_date": "Start date for averaging.",
        "payoff": "Striked type payoff.",
        "exercise": "Exercise specification.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlContinuousAveragingAsianOptionWithStartDate(
    average_type: qAverageType,
    start_date: qDate,
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    trigger=None,
) -> ql.ContinuousAveragingAsianOption:
    return ql.ContinuousAveragingAsianOption(average_type, start_date, payoff, exercise)


@xlo.func(
    help="Create a QuantLib DiscreteAveragingAsianOption object with past fixings.",
    args={
        "average_type": "Average type (ARITHMETIC or GEOMETRIC).",
        "fixing_dates": "Array of fixing dates.",
        "payoff": "Striked type payoff.",
        "exercise": "Exercise specification.",
        "all_past_fixings": "Array of all past fixings (optional).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDiscreteAveragingAsianOption(
    average_type: qAverageType,
    fixing_dates: xlo.Array(dims=1),
    payoff: ql.StrikedTypePayoff,
    exercise: ql.Exercise,
    all_past_fixings: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.DiscreteAveragingAsianOption:
    if all_past_fixings is None:
        return ql.DiscreteAveragingAsianOption(
            average_type,
            _to_date_list(fixing_dates),
            payoff,
            exercise,
        )
    return ql.DiscreteAveragingAsianOption(
        average_type,
        _to_date_list(fixing_dates),
        payoff,
        exercise,
        to_float_list(all_past_fixings),
    )


@xlo.func(
    help="Return the time grid for a DiscreteAveragingAsianOption.",
    args={
        "option": "QuantLib DiscreteAveragingAsianOption.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDiscreteAveragingAsianOptionTimeGrid(
    option: ql.DiscreteAveragingAsianOption, trigger=None
) -> ql.TimeGrid:
    return option.timeGrid()


# Analytic Engines


@xlo.func(
    help="Create a QuantLib AnalyticContinuousGeometricAveragePriceAsianEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticContinuousGeometricAveragePriceAsianEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticContinuousGeometricAveragePriceAsianEngine:
    return ql.AnalyticContinuousGeometricAveragePriceAsianEngine(process)


@xlo.func(
    help="Create a QuantLib AnalyticContinuousGeometricAveragePriceAsianHestonEngine object.",
    args={
        "process": "Heston process.",
        "summation_cutoff": "Summation cutoff (default 50).",
        "xi_right_limit": "Xi right limit (default 100.0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticContinuousGeometricAveragePriceAsianHestonEngine(
    process: ql.HestonProcess,
    summation_cutoff: int = 50,
    xi_right_limit: float = 100.0,
    trigger=None,
) -> ql.AnalyticContinuousGeometricAveragePriceAsianHestonEngine:
    return ql.AnalyticContinuousGeometricAveragePriceAsianHestonEngine(
        process, summation_cutoff, xi_right_limit
    )


@xlo.func(
    help="Create a QuantLib AnalyticDiscreteGeometricAveragePriceAsianEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticDiscreteGeometricAveragePriceAsianEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticDiscreteGeometricAveragePriceAsianEngine:
    return ql.AnalyticDiscreteGeometricAveragePriceAsianEngine(process)


@xlo.func(
    help="Create a QuantLib AnalyticDiscreteGeometricAveragePriceAsianHestonEngine object.",
    args={
        "process": "Heston process.",
        "xi_right_limit": "Xi right limit (default 100.0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticDiscreteGeometricAveragePriceAsianHestonEngine(
    process: ql.HestonProcess,
    xi_right_limit: float = 100.0,
    trigger=None,
) -> ql.AnalyticDiscreteGeometricAveragePriceAsianHestonEngine:
    return ql.AnalyticDiscreteGeometricAveragePriceAsianHestonEngine(
        process, xi_right_limit
    )


@xlo.func(
    help="Create a QuantLib AnalyticDiscreteGeometricAverageStrikeAsianEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticDiscreteGeometricAverageStrikeAsianEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticDiscreteGeometricAverageStrikeAsianEngine:
    return ql.AnalyticDiscreteGeometricAverageStrikeAsianEngine(process)


# Monte Carlo Engines


@xlo.func(
    help="Create a QuantLib MCDiscreteArithmeticAPEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "traits": "Monte Carlo traits (PR or LD).",
        "brownian_bridge": "Use Brownian bridge (default False).",
        "antithetic_variate": "Use antithetic variate (default False).",
        "control_variate": "Use control variate (default False).",
        "required_samples": "Required number of samples (optional).",
        "required_tolerance": "Required tolerance (optional).",
        "max_samples": "Maximum number of samples (optional).",
        "seed": "Random seed (default 0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCDiscreteArithmeticAPEngine(
    process: ql.GeneralizedBlackScholesProcess,
    traits: qMCTraits,
    brownian_bridge: bool = False,
    antithetic_variate: bool = False,
    control_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    trigger=None,
) -> ql.PricingEngine:
    traits = traits.lower()
    if traits == "pr" or traits == "pseudorandom":
        cls = ql.MCPRDiscreteArithmeticAPEngine
    elif traits == "ld" or traits == "lowdiscrepancy":
        cls = ql.MCLDDiscreteArithmeticAPEngine
    else:
        raise RuntimeError(f"unknown MC traits: {traits}")

    return cls(
        process,
        brownian_bridge,
        antithetic_variate,
        control_variate,
        required_samples,
        required_tolerance,
        max_samples,
        seed,
    )


@xlo.func(
    help="Create a QuantLib MCDiscreteArithmeticAPHestonEngine object.",
    args={
        "process": "Heston process.",
        "traits": "Monte Carlo traits (PR or LD).",
        "antithetic_variate": "Use antithetic variate (default False).",
        "required_samples": "Required number of samples (optional).",
        "required_tolerance": "Required tolerance (optional).",
        "max_samples": "Maximum number of samples (optional).",
        "seed": "Random seed (default 0).",
        "time_steps": "Number of time steps (optional).",
        "time_steps_per_year": "Number of time steps per year (optional).",
        "control_variate": "Use control variate (default False).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCDiscreteArithmeticAPHestonEngine(
    process: ql.HestonProcess,
    traits: qMCTraits,
    antithetic_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    time_steps: int = ql.nullInt(),
    time_steps_per_year: int = ql.nullInt(),
    control_variate: bool = False,
    trigger=None,
) -> ql.PricingEngine:
    traits = traits.lower()
    if traits == "pr" or traits == "pseudorandom":
        cls = ql.MCPRDiscreteArithmeticAPHestonEngine
    elif traits == "ld" or traits == "lowdiscrepancy":
        cls = ql.MCLDDiscreteArithmeticAPHestonEngine
    else:
        raise RuntimeError(f"unknown MC traits: {traits}")

    return cls(
        process,
        antithetic_variate,
        required_samples,
        required_tolerance,
        max_samples,
        seed,
        time_steps,
        time_steps_per_year,
        control_variate,
    )


@xlo.func(
    help="Create a QuantLib MCDiscreteArithmeticASEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "traits": "Monte Carlo traits (PR or LD).",
        "brownian_bridge": "Use Brownian bridge (default False).",
        "antithetic_variate": "Use antithetic variate (default False).",
        "required_samples": "Required number of samples (optional).",
        "required_tolerance": "Required tolerance (optional).",
        "max_samples": "Maximum number of samples (optional).",
        "seed": "Random seed (default 0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCDiscreteArithmeticASEngine(
    process: ql.GeneralizedBlackScholesProcess,
    traits: qMCTraits,
    brownian_bridge: bool = False,
    antithetic_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    trigger=None,
) -> ql.PricingEngine:
    traits = traits.lower()
    if traits == "pseudorandom":
        cls = ql.MCPRDiscreteArithmeticASEngine
    elif traits == "lowdiscrepancy":
        cls = ql.MCLDDiscreteArithmeticASEngine
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


@xlo.func(
    help="Create a QuantLib MCDiscreteGeometricAPEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "traits": "Monte Carlo traits (PR or LD).",
        "brownian_bridge": "Use Brownian bridge (default False).",
        "antithetic_variate": "Use antithetic variate (default False).",
        "required_samples": "Required number of samples (optional).",
        "required_tolerance": "Required tolerance (optional).",
        "max_samples": "Maximum number of samples (optional).",
        "seed": "Random seed (default 0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCDiscreteGeometricAPEngine(
    process: ql.GeneralizedBlackScholesProcess,
    traits: qMCTraits,
    brownian_bridge: bool = False,
    antithetic_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    trigger=None,
) -> ql.PricingEngine:
    traits = traits.lower()
    if traits == "pseudorandom":
        cls = ql.MCPRDiscreteGeometricAPEngine
    elif traits == "lowdiscrepancy":
        cls = ql.MCLDDiscreteGeometricAPEngine
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


@xlo.func(
    help="Create a QuantLib MCDiscreteGeometricAPHestonEngine object.",
    args={
        "process": "Heston process.",
        "traits": "Monte Carlo traits (PR or LD).",
        "antithetic_variate": "Use antithetic variate (default False).",
        "required_samples": "Required number of samples (optional).",
        "required_tolerance": "Required tolerance (optional).",
        "max_samples": "Maximum number of samples (optional).",
        "seed": "Random seed (default 0).",
        "time_steps": "Number of time steps (optional).",
        "time_steps_per_year": "Number of time steps per year (optional).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCDiscreteGeometricAPHestonEngine(
    process: ql.HestonProcess,
    traits: qMCTraits,
    antithetic_variate: bool = False,
    required_samples: int = ql.nullInt(),
    required_tolerance: float = ql.nullDouble(),
    max_samples: int = ql.nullInt(),
    seed: int = 0,
    time_steps: int = ql.nullInt(),
    time_steps_per_year: int = ql.nullInt(),
    trigger=None,
) -> ql.PricingEngine:
    traits = traits.lower()
    if traits == "pseudorandom":
        cls = ql.MCPRDiscreteGeometricAPHestonEngine
    elif traits == "lowdiscrepancy":
        cls = ql.MCLDDiscreteGeometricAPHestonEngine
    else:
        raise RuntimeError(f"unknown MC traits: {traits}")

    return cls(
        process,
        antithetic_variate,
        required_samples,
        required_tolerance,
        max_samples,
        seed,
        time_steps,
        time_steps_per_year,
    )


# Other Engines


@xlo.func(
    help="Create a QuantLib ContinuousArithmeticAsianLevyEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "running_average": "Running average quote handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlContinuousArithmeticAsianLevyEngine(
    process: ql.GeneralizedBlackScholesProcess,
    running_average: qQuoteHandle,
    trigger=None,
) -> ql.ContinuousArithmeticAsianLevyEngine:
    return ql.ContinuousArithmeticAsianLevyEngine(process, running_average)


@xlo.func(
    help="Create a QuantLib ContinuousArithmeticAsianLevyEngine object with start date.",
    args={
        "process": "Generalized Black-Scholes process.",
        "running_average": "Running average quote handle.",
        "start_date": "Start date for the engine.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlContinuousArithmeticAsianLevyEngineWithStartDate(
    process: ql.GeneralizedBlackScholesProcess,
    running_average: qQuoteHandle,
    start_date: qDate,
    trigger=None,
) -> ql.ContinuousArithmeticAsianLevyEngine:
    return ql.ContinuousArithmeticAsianLevyEngine(process, running_average, start_date)


@xlo.func(
    help="Create a QuantLib FdBlackScholesAsianEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "t_grid": "Time grid points.",
        "x_grid": "Asset grid points.",
        "a_grid": "Averaging grid points.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdBlackScholesAsianEngine(
    process: ql.GeneralizedBlackScholesProcess,
    t_grid: int,
    x_grid: int,
    a_grid: int,
    trigger=None,
) -> ql.FdBlackScholesAsianEngine:
    # for discrete arithmetic averaging only
    return ql.FdBlackScholesAsianEngine(process, t_grid, x_grid, a_grid)


@xlo.func(
    help="Create a QuantLib ChoiAsianEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "lambda": "Lambda parameter (default 15).",
        "max_nr_integration_steps": "Maximum number of integration steps (default 2^21).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlChoiAsianEngine(
    process: ql.GeneralizedBlackScholesProcess,
    lambda_: int = 15,
    max_nr_integration_steps: int = 2 << 21,
    trigger=None,
) -> ql.ChoiAsianEngine:
    return ql.ChoiAsianEngine(process, lambda_, max_nr_integration_steps)


@xlo.func(
    help="Create a QuantLib TurnbullWakemanAsianEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTurnbullWakemanAsianEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.TurnbullWakemanAsianEngine:
    return ql.TurnbullWakemanAsianEngine(process)
