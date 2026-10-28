import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate
from .fra import qPosition
from .utilities import enum_value, to_float_list


@xlo.func(
    help="Create a QuantLib VarianceSwap.",
    args={
        "position": "The position ('Long' or 'Short').",
        "strike": "The variance strike.",
        "notional": "The swap notional.",
        "start_date": "The start date.",
        "maturity_date": "The maturity date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlVarianceSwap(
    position: qPosition,
    strike: float,
    notional: float,
    start_date: qDate,
    maturity_date: qDate,
    trigger=None,
) -> ql.VarianceSwap:
    return ql.VarianceSwap(position, strike, notional, start_date, maturity_date)


@xlo.func(
    help="Create a replication-based VarianceSwap pricing engine.",
    args={
        "process": "The generalized Black-Scholes process.",
        "dk": "The log-strike spacing used for replication.",
        "call_strikes": "The call strikes used for replication.",
        "put_strikes": "The put strikes used for replication.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlReplicatingVarianceSwapEngine(
    process: ql.GeneralizedBlackScholesProcess,
    dk: float = 5.0,
    call_strikes: xlo.Array(dims=1) = None,
    put_strikes: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.ReplicatingVarianceSwapEngine:
    call_strikes_ = to_float_list([] if call_strikes is None else call_strikes)
    put_strikes_ = to_float_list([] if put_strikes is None else put_strikes)
    return ql.ReplicatingVarianceSwapEngine(process, dk, call_strikes_, put_strikes_)


@xlo.func(
    help="Create a Monte Carlo VarianceSwap pricing engine.",
    args={
        "process": "The generalized Black-Scholes process.",
        "traits": "The random-number traits ('PseudoRandom' or 'LowDiscrepancy').",
        "time_steps": "The number of time steps.",
        "time_steps_per_year": "The number of time steps per year.",
        "brownian_bridge": "Whether to use a Brownian bridge.",
        "antithetic_variate": "Whether to use antithetic variates.",
        "required_samples": "The required number of samples.",
        "required_tolerance": "The required tolerance.",
        "max_samples": "The maximum number of samples.",
        "seed": "The random-number generator seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMCVarianceSwapEngine(
    process: ql.GeneralizedBlackScholesProcess,
    traits: str,
    time_steps: int = None,
    time_steps_per_year: int = None,
    brownian_bridge: bool = False,
    antithetic_variate: bool = False,
    required_samples: int = None,
    required_tolerance: float = None,
    max_samples: int = None,
    seed: int = 0,
    trigger=None,
) -> ql.PricingEngine:
    return ql.MCVarianceSwapEngine(
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
    help="Get the fair variance of a VarianceSwap.",
    args={"variance_swap": "The VarianceSwap object."},
    group=EXCEL_GROUP_NAME,
)
def qlVarianceSwapVariance(variance_swap: ql.VarianceSwap, trigger=None) -> float:
    return variance_swap.variance()
