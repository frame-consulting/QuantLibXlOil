import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import _to_date_list
from .options import qMCTraits


@xlo.func(
    help="Create a QuantLib CliquetOption object.",
    args={
        "payoff": "Percentage strike payoff.",
        "maturity": "European exercise specification.",
        "reset_dates": "Array of reset dates.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCliquetOption(
    payoff: ql.PercentageStrikePayoff,
    maturity: ql.EuropeanExercise,
    reset_dates: xlo.Array(dims=1),
    trigger=None,
) -> ql.CliquetOption:
    return ql.CliquetOption(payoff, maturity, _to_date_list(reset_dates))


@xlo.func(
    help="Create a QuantLib AnalyticCliquetEngine object.",
    args={"process": "Generalized Black-Scholes process."},
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticCliquetEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticCliquetEngine:
    return ql.AnalyticCliquetEngine(process)


@xlo.func(
    help="Create a QuantLib AnalyticPerformanceEngine object.",
    args={"process": "Generalized Black-Scholes process."},
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticPerformanceEngine(
    process: ql.GeneralizedBlackScholesProcess, trigger=None
) -> ql.AnalyticPerformanceEngine:
    return ql.AnalyticPerformanceEngine(process)


@xlo.func(
    help="Create a QuantLib MCPerformanceEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
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
def qlMCPerformanceEngine(
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
    return ql.MCPerformanceEngine(
        process,
        traits,
        brownian_bridge,
        antithetic_variate,
        required_samples,
        required_tolerance,
        max_samples,
        seed,
    )
