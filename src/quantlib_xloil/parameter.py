import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import to_float_list

# Parameter interface


@xlo.func(
    help="Return the parameters of a QuantLib Parameter as a list.",
    args={"parameter": "The QuantLib Parameter to get parameters from."},
    group=EXCEL_GROUP_NAME,
)
def qlParameterParams(parameter: ql.Parameter, trigger=None) -> list[float]:
    return list(parameter.params())


@xlo.func(
    help="Set a parameter of a QuantLib Parameter.",
    args={
        "parameter": "The QuantLib Parameter to set the parameter for.",
        "idx": "The index of the parameter to set.",
        "x": "The value to set the parameter to.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlParameterSetParam(
    parameter: ql.Parameter, idx: int, x: float, trigger=None
) -> bool:
    # setPatam is unsafe; we need to catch index out of bounds
    if idx < 0 or idx >= parameter.size():
        raise IndexError(
            f"Parameter index {idx} out of bounds for parameter of size {parameter.size()}"
        )
    parameter.setParam(idx, x)
    return True


@xlo.func(
    help="Test if the parameters of a QuantLib Parameter are valid.",
    args={
        "parameter": "The QuantLib Parameter to test.",
        "params": "The parameters to test.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlParameterTestParams(
    parameter: ql.Parameter, params: xlo.Array(dims=1), trigger=None
) -> bool:
    p_array = ql.Array(to_float_list(params))
    return parameter.testParams(p_array)


@xlo.func(
    help="Return the size of a QuantLib Parameter.",
    args={"parameter": "The QuantLib Parameter to get the size of."},
    group=EXCEL_GROUP_NAME,
)
def qlParameterSize(parameter: ql.Parameter, trigger=None) -> int:
    return parameter.size()


@xlo.func(
    help="Return the value of a QuantLib Parameter at a specific time.",
    args={
        "parameter": "The QuantLib Parameter to evaluate.",
        "t": "The time at which to evaluate the parameter.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlParameterAtTime(parameter: ql.Parameter, t: float, trigger=None) -> float:
    return parameter(t)


@xlo.func(
    help="Return the constraint of a QuantLib Parameter.",
    args={"parameter": "The QuantLib Parameter to get the constraint for."},
    group=EXCEL_GROUP_NAME,
)
def qlParameterConstraint(parameter: ql.Parameter, trigger=None) -> ql.Constraint:
    return parameter.constraint()


# Parameters


@xlo.func(
    help="Create a QuantLib NullParameter.",
    args={},
    group=EXCEL_GROUP_NAME,
)
def qlNullParameter(trigger=None) -> ql.NullParameter:
    return ql.NullParameter()


@xlo.func(
    help="Create a QuantLib ConstantParameter.",
    args={"constraint": "The constraint for the parameter."},
    group=EXCEL_GROUP_NAME,
)
def qlConstantParameter(
    constraint: ql.Constraint,
    value: float = None,
    trigger=None,
) -> ql.ConstantParameter:
    # We need to switch order of parameters to handle optional value
    if value is not None:
        return ql.ConstantParameter(value, constraint)
    else:
        return ql.ConstantParameter(constraint)


@xlo.func(
    help="Create a QuantLib PiecewiseConstantParameter.",
    args={
        "times": "The times for the parameter.",
        "values": "The values for the parameter.",
        "constraint": "The constraint for the parameter.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseConstantParameter(
    times: xlo.Array(dims=1),
    values: xlo.Array(dims=1),
    constraint: ql.Constraint = ql.NoConstraint(),
    trigger=None,
) -> ql.PiecewiseConstantParameter:
    if len(times) + 1 != len(values):
        raise ValueError(
            f"There must be one more value than times. Got {len(times)} times and {len(values)} values."
        )
    p = ql.PiecewiseConstantParameter(to_float_list(times), constraint)
    for i, value in enumerate(to_float_list(values)):
        p.setParam(i, value)
    return p
