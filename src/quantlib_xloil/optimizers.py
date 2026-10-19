import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import enum_value, to_float_list, UNKNOWN_KEY

QL_END_CRITERIA_TYPE = {
    "FUNCTION_EPSILON_TOO_SMALL": ql.EndCriteria.FunctionEpsilonTooSmall,
    "MAX_ITERATIONS": ql.EndCriteria.MaxIterations,
    "NO_CRITERIA": ql.EndCriteria.NoCriteria,
    "STATIONARY_POINT": ql.EndCriteria.StationaryPoint,
    "STATIONARY_FUNCTION_VALUE": ql.EndCriteria.StationaryFunctionValue,
    "STATIONARY_FUNCTION_ACCURACY": ql.EndCriteria.StationaryFunctionAccuracy,
    "ZERO_GRADIENT_NORM": ql.EndCriteria.ZeroGradientNorm,
    UNKNOWN_KEY: ql.EndCriteria.Unknown,
}


def _qEndCriteriaType(s: str) -> int:
    return enum_value(s, QL_END_CRITERIA_TYPE)


@xlo.converter()
def qEndCriteriaType(s: str) -> int:
    return _qEndCriteriaType(s)


# Constraints


@xlo.func(
    help="Create a QuantLib NoConstraint.",
    group=EXCEL_GROUP_NAME,
)
def qlNoConstraint(trigger=None) -> ql.NoConstraint:
    return ql.NoConstraint()


@xlo.func(
    help="Create a QuantLib PositiveConstraint.",
    group=EXCEL_GROUP_NAME,
)
def qlPositiveConstraint(trigger=None) -> ql.PositiveConstraint:
    return ql.PositiveConstraint()


@xlo.func(
    help="Create a QuantLib BoundaryConstraint.",
    args={
        "lower": "The lower bound of the constraint.",
        "upper": "The upper bound of the constraint.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBoundaryConstraint(
    lower: float, upper: float, trigger=None
) -> ql.BoundaryConstraint:
    return ql.BoundaryConstraint(lower, upper)


@xlo.func(
    help="Create a QuantLib CompositeConstraint from two constraints.",
    args={
        "constraint_1": "The first constraint.",
        "constraint_2": "The second constraint.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCompositeConstraint(
    constraint_1: ql.Constraint, constraint_2: ql.Constraint, trigger=None
) -> ql.CompositeConstraint:
    return ql.CompositeConstraint(constraint_1, constraint_2)


@xlo.func(
    help="Create a QuantLib NonhomogeneousBoundaryConstraint from lower and upper arrays.",
    args={
        "lower": "The lower bounds of the constraint.",
        "upper": "The upper bounds of the constraint.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonhomogeneousBoundaryConstraint(
    lower: xlo.Array(dims=1), upper: xlo.Array(dims=1), trigger=None
) -> ql.NonhomogeneousBoundaryConstraint:
    lower_ = ql.Array(to_float_list(lower))
    upper_ = ql.Array(to_float_list(upper))
    return ql.NonhomogeneousBoundaryConstraint(lower_, upper_)


# EndCriteria


@xlo.func(
    help="Create a QuantLib EndCriteria.",
    args={
        "max_iterations": "The maximum number of iterations.",
        "max_stationary_state_iterations": "The maximum number of stationary state iterations.",
        "root_epsilon": "The root epsilon.",
        "function_epsilon": "The function epsilon.",
        "gradient_norm_epsilon": "The gradient norm epsilon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEndCriteria(
    max_iterations: int,
    max_stationary_state_iterations: int,
    root_epsilon: float,
    function_epsilon: float,
    gradient_norm_epsilon: float,
    trigger=None,
) -> ql.EndCriteria:
    return ql.EndCriteria(
        max_iterations,
        max_stationary_state_iterations,
        root_epsilon,
        function_epsilon,
        gradient_norm_epsilon,
    )


@xlo.func(
    help="Check if a given end criteria type was succeeded.",
    args={
        "end_criteria": "The end criteria to check.",
        "ec_type": "The end criteria type to check for.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEndCriteriaSucceded(
    end_criteria: ql.EndCriteria, ec_type: qEndCriteriaType, trigger=None
) -> bool:
    return end_criteria.succeeded(ec_type)


@xlo.func(
    help="Create a QuantLib LBFGSB optimization method.",
    args={
        "memory": "Number of limited-memory corrections.",
        "pg_tol": "Projected-gradient convergence tolerance.",
        "f_tol": "Function-value convergence tolerance.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLBFGSB(
    memory: int = 10,
    pg_tol: float = 1.0e-8,
    f_tol: float = 2.220446049250313e-9,
    trigger=None,
) -> ql.LBFGSB:
    return ql.LBFGSB(memory, pg_tol, f_tol)


@xlo.func(
    help="Create a bounded QuantLib LBFGSB optimization method.",
    args={
        "lower_bound": "Array of lower bounds.",
        "upper_bound": "Array of upper bounds.",
        "memory": "Number of limited-memory corrections.",
        "pg_tol": "Projected-gradient convergence tolerance.",
        "f_tol": "Function-value convergence tolerance.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLBFGSBBounded(
    lower_bound: xlo.Array(dims=1),
    upper_bound: xlo.Array(dims=1),
    memory: int = 10,
    pg_tol: float = 1.0e-8,
    f_tol: float = 2.220446049250313e-9,
    trigger=None,
) -> ql.LBFGSB:
    return ql.LBFGSB(
        ql.Array(to_float_list(lower_bound)),
        ql.Array(to_float_list(upper_bound)),
        memory,
        pg_tol,
        f_tol,
    )


@xlo.func(
    help="Create a QuantLib LevenbergMarquardt optimization method.",
    args={
        "epsfcn": "The epsilon for the function value.",
        "xtol": "The epsilon for the solution.",
        "gtol": "The epsilon for the gradient norm.",
        "use_cost_functions_jacobian": "Whether to use the cost functions Jacobian.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLevenbergMarquardt(
    epsfcn: float = 1.0e-8,
    xtol: float = 1.0e-8,
    gtol: float = 1.0e-8,
    use_cost_functions_jacobian: bool = False,
    trigger=None,
) -> ql.LevenbergMarquardt:
    return ql.LevenbergMarquardt(epsfcn, xtol, gtol, use_cost_functions_jacobian)


# 1D Solvers

# TODO write excel tests


@xlo.func(
    help="Create a QuantLib Brent solver.",
    group=EXCEL_GROUP_NAME,
)
def qlBrent(trigger=None) -> ql.Brent:
    return ql.Brent()


@xlo.func(
    help="Create a QuantLib Bisection solver.",
    group=EXCEL_GROUP_NAME,
)
def qlBisection(trigger=None) -> ql.Bisection:
    return ql.Bisection()


@xlo.func(
    help="Create a QuantLib FalsePosition solver.",
    group=EXCEL_GROUP_NAME,
)
def qlFalsePosition(trigger=None) -> ql.FalsePosition:
    return ql.FalsePosition()


@xlo.func(
    help="Create a QuantLib Ridder solver.",
    group=EXCEL_GROUP_NAME,
)
def qlRidder(trigger=None) -> ql.Ridder:
    return ql.Ridder()


@xlo.func(
    help="Create a QuantLib Secant solver.",
    group=EXCEL_GROUP_NAME,
)
def qlSecant(trigger=None) -> ql.Secant:
    return ql.Secant()


@xlo.func(
    help="Create a QuantLib Newton solver.",
    group=EXCEL_GROUP_NAME,
)
def qlNewton(trigger=None) -> ql.Newton:
    return ql.Newton()


@xlo.func(
    help="Create a QuantLib NewtonSafe solver.",
    group=EXCEL_GROUP_NAME,
)
def qlNewtonSafe(trigger=None) -> ql.NewtonSafe:
    return ql.NewtonSafe()


# Additional Optimization Methods


@xlo.func(
    help="Create a QuantLib ConjugateGradient optimization method.",
    group=EXCEL_GROUP_NAME,
)
def qlConjugateGradient(trigger=None) -> ql.ConjugateGradient:
    return ql.ConjugateGradient()


@xlo.func(
    help="Create a QuantLib Simplex optimization method.",
    args={
        "lambda": "The reflection coefficient.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSimplex(lambda_: float = 0.5, trigger=None) -> ql.Simplex:
    return ql.Simplex(lambda_)


@xlo.func(
    help="Create a QuantLib SteepestDescent optimization method.",
    group=EXCEL_GROUP_NAME,
)
def qlSteepestDescent(trigger=None) -> ql.SteepestDescent:
    return ql.SteepestDescent()


@xlo.func(
    help="Create a QuantLib BFGS optimization method.",
    group=EXCEL_GROUP_NAME,
)
def qlBFGS(trigger=None) -> ql.BFGS:
    return ql.BFGS()


@xlo.func(
    help="Create a QuantLib DifferentialEvolution optimization method.",
    group=EXCEL_GROUP_NAME,
)
def qlDifferentialEvolution(trigger=None) -> ql.DifferentialEvolution:
    return ql.DifferentialEvolution()


# Simulated Annealing Helper Classes


@xlo.func(
    help="Create a QuantLib SamplerGaussian.",
    args={
        "seed": "The random seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSamplerGaussian(seed: int = 0, trigger=None) -> ql.SamplerGaussian:
    return ql.SamplerGaussian(seed)


@xlo.func(
    help="Create a QuantLib SamplerLogNormal.",
    args={
        "seed": "The random seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSamplerLogNormal(seed: int = 0, trigger=None) -> ql.SamplerLogNormal:
    return ql.SamplerLogNormal(seed)


@xlo.func(
    help="Create a QuantLib SamplerMirrorGaussian.",
    args={
        "lower": "Array of lower bounds.",
        "upper": "Array of upper bounds.",
        "seed": "The random seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSamplerMirrorGaussian(
    lower: xlo.Array(dims=1),
    upper: xlo.Array(dims=1),
    seed: int = 0,
    trigger=None,
) -> ql.SamplerMirrorGaussian:
    return ql.SamplerMirrorGaussian(
        ql.Array(to_float_list(lower)),
        ql.Array(to_float_list(upper)),
        seed,
    )


@xlo.func(
    help="Create a QuantLib ProbabilityBoltzmannDownhill.",
    args={
        "seed": "The random seed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlProbabilityBoltzmannDownhill(
    seed: int = 0, trigger=None
) -> ql.ProbabilityBoltzmannDownhill:
    return ql.ProbabilityBoltzmannDownhill(seed)


@xlo.func(
    help="Create a QuantLib TemperatureExponential.",
    args={
        "initial_temp": "The initial temperature.",
        "dimension": "The dimension.",
        "power": "The power factor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTemperatureExponential(
    initial_temp: float,
    dimension: int,
    power: float = 0.95,
    trigger=None,
) -> ql.TemperatureExponential:
    return ql.TemperatureExponential(initial_temp, dimension, power)


@xlo.func(
    help="Create a QuantLib ReannealingTrivial.",
    group=EXCEL_GROUP_NAME,
)
def qlReannealingTrivial(trigger=None) -> ql.ReannealingTrivial:
    return ql.ReannealingTrivial()


# Simulated Annealing ResetScheme Enum

QL_RESET_SCHEME = {
    "NO_RESET_SCHEME": ql.GaussianSimulatedAnnealing.NoResetScheme,
    "RESET_TO_BEST_POINT": ql.GaussianSimulatedAnnealing.ResetToBestPoint,
    "RESET_TO_ORIGIN": ql.GaussianSimulatedAnnealing.ResetToOrigin,
}


def _qResetScheme(s: str) -> int:
    return enum_value(s, QL_RESET_SCHEME)


@xlo.converter()
def qResetScheme(s: str) -> int:
    return _qResetScheme(s)


# Simulated Annealing Optimization Methods


@xlo.func(
    help="Create a QuantLib GaussianSimulatedAnnealing optimization method.",
    args={
        "sampler": "The Gaussian sampler.",
        "probability": "The probability function.",
        "temperature": "The temperature schedule.",
        "reannealing": "The reannealing strategy.",
        "start_temperature": "The starting temperature.",
        "end_temperature": "The ending temperature.",
        "re_anneal_steps": "The number of re-annealing steps.",
        "reset_scheme": "The reset scheme.",
        "reset_steps": "The number of reset steps.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussianSimulatedAnnealing(
    sampler: ql.SamplerGaussian,
    probability: ql.ProbabilityBoltzmannDownhill,
    temperature: ql.TemperatureExponential,
    reannealing: ql.ReannealingTrivial = None,
    start_temperature: float = 200.0,
    end_temperature: float = 0.01,
    re_anneal_steps: int = 50,
    reset_scheme: qResetScheme = ql.GaussianSimulatedAnnealing.ResetToBestPoint,
    reset_steps: int = 150,
    trigger=None,
) -> ql.GaussianSimulatedAnnealing:
    if reannealing is None:
        reannealing = ql.ReannealingTrivial()
    return ql.GaussianSimulatedAnnealing(
        sampler,
        probability,
        temperature,
        reannealing,
        start_temperature,
        end_temperature,
        re_anneal_steps,
        reset_scheme,
        reset_steps,
    )


@xlo.func(
    help="Create a QuantLib MirrorGaussianSimulatedAnnealing optimization method.",
    args={
        "sampler": "The mirror Gaussian sampler.",
        "probability": "The probability function.",
        "temperature": "The temperature schedule.",
        "reannealing": "The reannealing strategy.",
        "start_temperature": "The starting temperature.",
        "end_temperature": "The ending temperature.",
        "re_anneal_steps": "The number of re-annealing steps.",
        "reset_scheme": "The reset scheme.",
        "reset_steps": "The number of reset steps.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMirrorGaussianSimulatedAnnealing(
    sampler: ql.SamplerMirrorGaussian,
    probability: ql.ProbabilityBoltzmannDownhill,
    temperature: ql.TemperatureExponential,
    reannealing: ql.ReannealingTrivial = None,
    start_temperature: float = 200.0,
    end_temperature: float = 0.01,
    re_anneal_steps: int = 50,
    reset_scheme: qResetScheme = ql.MirrorGaussianSimulatedAnnealing.ResetToBestPoint,
    reset_steps: int = 150,
    trigger=None,
) -> ql.MirrorGaussianSimulatedAnnealing:
    if reannealing is None:
        reannealing = ql.ReannealingTrivial()
    return ql.MirrorGaussianSimulatedAnnealing(
        sampler,
        probability,
        temperature,
        reannealing,
        start_temperature,
        end_temperature,
        re_anneal_steps,
        reset_scheme,
        reset_steps,
    )


@xlo.func(
    help="Create a QuantLib LogNormalSimulatedAnnealing optimization method.",
    args={
        "sampler": "The log-normal sampler.",
        "probability": "The probability function.",
        "temperature": "The temperature schedule.",
        "reannealing": "The reannealing strategy.",
        "start_temperature": "The starting temperature.",
        "end_temperature": "The ending temperature.",
        "re_anneal_steps": "The number of re-annealing steps.",
        "reset_scheme": "The reset scheme.",
        "reset_steps": "The number of reset steps.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLogNormalSimulatedAnnealing(
    sampler: ql.SamplerLogNormal,
    probability: ql.ProbabilityBoltzmannDownhill,
    temperature: ql.TemperatureExponential,
    reannealing: ql.ReannealingTrivial = None,
    start_temperature: float = 10.0,
    end_temperature: float = 0.01,
    re_anneal_steps: int = 50,
    reset_scheme: qResetScheme = ql.LogNormalSimulatedAnnealing.ResetToBestPoint,
    reset_steps: int = 150,
    trigger=None,
) -> ql.LogNormalSimulatedAnnealing:
    if reannealing is None:
        reannealing = ql.ReannealingTrivial()
    return ql.LogNormalSimulatedAnnealing(
        sampler,
        probability,
        temperature,
        reannealing,
        start_temperature,
        end_temperature,
        re_anneal_steps,
        reset_scheme,
        reset_steps,
    )
