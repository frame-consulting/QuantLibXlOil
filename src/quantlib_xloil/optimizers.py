import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import first_key, UNKNOWN_KEY, UNKNOWN_VALUE, enum_value
from .stochasticprocess import _to_float_list

# Constraints

@xlo.func(
    help='Create a QuantLib NoConstraint.',
    group=EXCEL_GROUP_NAME,
)
def qlNoConstraint(trigger=None) -> ql.NoConstraint:
    return ql.NoConstraint()


@xlo.func(
    help='Create a QuantLib PositiveConstraint.',
    group=EXCEL_GROUP_NAME,
)
def qlPositiveConstraint(trigger=None) -> ql.PositiveConstraint:
    return ql.PositiveConstraint()


@xlo.func(
    help='Create a QuantLib BoundaryConstraint.',
    args={
        'lower': 'The lower bound of the constraint.',
        'upper': 'The upper bound of the constraint.'
    },
    group=EXCEL_GROUP_NAME,
)
def qlBoundaryConstraint(lower: float, upper: float, trigger=None) -> ql.BoundaryConstraint:
    return ql.BoundaryConstraint(lower, upper)


@xlo.func(
    help='Create a QuantLib CompositeConstraint from two constraints.',
    args={
        'constraint_1': 'The first constraint.',
        'constraint_2': 'The second constraint.'
    },
    group=EXCEL_GROUP_NAME,
)
def qlCompositeConstraint(
    constraint_1: ql.Constraint,
    constraint_2: ql.Constraint,
    trigger=None
) -> ql.CompositeConstraint:
    return ql.CompositeConstraint(constraint_1, constraint_2)


@xlo.func(
    help='Create a QuantLib NonhomogeneousBoundaryConstraint from lower and upper arrays.',
    args={
        'lower': 'The lower bounds of the constraint.',
        'upper': 'The upper bounds of the constraint.'
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonhomogeneousBoundaryConstraint(
    lower: xlo.Array(dims=1),
    upper: xlo.Array(dims=1),
    trigger=None
) -> ql.NonhomogeneousBoundaryConstraint:
    lower_ = ql.Array(_to_float_list(lower))
    upper_ = ql.Array(_to_float_list(upper))
    return ql.NonhomogeneousBoundaryConstraint(lower_, upper_)


# EndCriteria

QL_END_CRITERIA_TYPE = {
    'NO_CRITERIA': ql.EndCriteria.NoCriteria,
    'MAX_ITERATIONS': ql.EndCriteria.MaxIterations,
    'STATIONARY_POINT': ql.EndCriteria.StationaryPoint,
    'STATIONARY_FUNCTION_VALUE': ql.EndCriteria.StationaryFunctionValue,
    'STATIONARY_FUNCTION_ACCURACY': ql.EndCriteria.StationaryFunctionAccuracy,
    'ZERO_GRADIENT_NORM': ql.EndCriteria.ZeroGradientNorm,
    'FUNCTION_EPSILON_TOO_SMALL': ql.EndCriteria.FunctionEpsilonTooSmall,
    UNKNOWN_KEY: ql.EndCriteria.Unknown,
}

def _qEndCriteriaType(s: str) -> int:
    return enum_value(s, QL_END_CRITERIA_TYPE)

@xlo.converter()
def qEndCriteriaType(s: str) -> int:
    return _qEndCriteriaType(s)

@xlo.func(
    help='Create a QuantLib EndCriteria.',
    args={
        'max_iterations': 'The maximum number of iterations.',
        'max_stationary_state_iterations': 'The maximum number of stationary state iterations.',
        'root_epsilon': 'The root epsilon.',
        'function_epsilon': 'The function epsilon.',
        'gradient_norm_epsilon': 'The gradient norm epsilon.'
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
        gradient_norm_epsilon
    )


@xlo.func(
    help='Check if a given end criteria type was succeeded.',
    args={
        'end_criteria': 'The end criteria to check.',
        'ec_type': 'The end criteria type to check for.'
    },
    group=EXCEL_GROUP_NAME,
)
def qlEndCriteriaSucceded(
    end_criteria: ql.EndCriteria,
    ec_type: qEndCriteriaType,
    trigger=None
) -> bool:
    return end_criteria.succeeded(ec_type)

@xlo.func(
    help='Create a QuantLib LevenbergMarquardt optimization method.',
    args={
        'epsfcn': 'The epsilon for the function value.',
        'xtol': 'The epsilon for the solution.',
        'gtol': 'The epsilon for the gradient norm.',
        'use_cost_functions_jacobian': 'Whether to use the cost functions Jacobian.'
    },
    group=EXCEL_GROUP_NAME,
)
def qlLevenbergMarquardt(
    epsfcn: float = 1.0e-8,
    xtol: float = 1.0e-8,
    gtol: float = 1.0e-8,
    use_cost_functions_jacobian: bool = False,
    trigger = None,
) -> ql.LevenbergMarquardt:
    return ql.LevenbergMarquardt(epsfcn, xtol, gtol, use_cost_functions_jacobian)
