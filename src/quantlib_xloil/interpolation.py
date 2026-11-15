import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import enum_class, to_float_list, to_float_matrix

QL_INTERPOLATION_INTERPOLATORS = {
    "BACKWARDFLAT": ql.BackwardFlatInterpolation,
    "CONVEXMONOTONE": ql.ConvexMonotoneInterpolation,
    "CUBICNATURALSPLINE": ql.CubicNaturalSpline,
    "FORWARDFLAT": ql.ForwardFlatInterpolation,
    "FRITSCHBUTLANDCUBIC": ql.FritschButlandCubic,
    "FRITSCHBUTLANDLOGCUBIC": ql.FritschButlandLogCubic,
    "KRUGERCUBIC": ql.KrugerCubic,
    "KRUGERLOGCUBIC": ql.KrugerLogCubic,
    "LAGRANGE": ql.LagrangeInterpolation,
    "LINEAR": ql.LinearInterpolation,
    "LOGCUBICNATURALSPLINE": ql.LogCubicNaturalSpline,
    "LOGLINEAR": ql.LogLinearInterpolation,
    "LOGPARABOLIC": ql.LogParabolic,
    "MONOTONICCUBICNATURALSPLINE": ql.MonotonicCubicNaturalSpline,
    "MONOTONICLOGCUBICNATURALSPLINE": ql.MonotonicLogCubicNaturalSpline,
    "MONOTONICLOGPARABOLIC": ql.MonotonicLogParabolic,
    "MONOTONICPARABOLIC": ql.MonotonicParabolic,
    "PARABOLIC": ql.Parabolic,
}

QL_INTERPOLATION_INTERPOLATORS_2D = {
    "BICUBICSPLINE": ql.BicubicSpline,
    "BILINEAR": ql.BilinearInterpolation,
}

QL_INTERPOLATION_OPERATIONS = {
    "DERIVATIVE": "derivative",
    "PRIMITIVE": "primitive",
    "SECONDDERIVATIVE": "secondDerivative",
    "VALUE": None,
}


def _qInterpolator(interpolator: str):
    if isinstance(interpolator, type):
        return interpolator
    return enum_class(interpolator, QL_INTERPOLATION_INTERPOLATORS, type)


@xlo.converter()
def qInterpolator(interpolator: str):
    return _qInterpolator(interpolator)


def _qInterpolator2D(interpolator: str):
    if isinstance(interpolator, type):
        return interpolator
    return enum_class(interpolator, QL_INTERPOLATION_INTERPOLATORS_2D, type)


@xlo.converter()
def qInterpolator2D(interpolator: str):
    return _qInterpolator2D(interpolator)


@xlo.func(
    help="Construct a one-dimensional interpolation object.",
    args={
        "x_values": "The x coordinates of the data series.",
        "y_values": "The y values corresponding to the x coordinates.",
        "interpolator": "The interpolation method to use.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterpolation(
    x_values: xlo.Array(dims=1),
    y_values: xlo.Array(dims=1),
    interpolator: qInterpolator,
    trigger=None,
) -> object:
    return interpolator(to_float_list(x_values), to_float_list(y_values))


@xlo.func(
    help="Construct a two-dimensional interpolation object.",
    args={
        "x_values": "The x coordinates of the data series.",
        "y_values": "The y coordinates of the data series.",
        "values": "The matrix of values corresponding to the coordinates.",
        "interpolator": "The interpolation method to use: BILINEAR or BICUBICSPLINE.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterpolation2D(
    x_values: xlo.Array(dims=1),
    y_values: xlo.Array(dims=1),
    values: xlo.Array(dims=2),
    interpolator: qInterpolator2D,
    trigger=None,
) -> object:
    if values.shape != (len(x_values), len(y_values)):
        raise ValueError(
            f"The shape of 'values' must match the lengths of 'x_values' and 'y_values'. "
            f"Expected shape: ({len(x_values)}, {len(y_values)}), "
            f"but got: {values.shape}."
        )
    values = values.T  # Transpose to match QuantLib's expected layout
    return interpolator(
        to_float_list(x_values),
        to_float_list(y_values),
        ql.Matrix(to_float_matrix(values)),
    )


@xlo.func(
    help="Apply a one-dimensional interpolation to calculate a value or property.",
    args={
        "interpolation": "The interpolation object to apply.",
        "x_value": "The x coordinate at which to apply the interpolation.",
        "operation": "The operation to perform: VALUE, DERIVATIVE, SECONDDERIVATIVE, or PRIMITIVE.",
        "allow_extrapolation": "Whether to allow extrapolation outside the data range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterpolationApply(
    interpolation: object,
    x_value: float,
    operation: str = "VALUE",
    allow_extrapolation: bool = False,
    trigger=None,
) -> float:
    operation_key = str(operation).strip().upper()
    if operation_key not in QL_INTERPOLATION_OPERATIONS:
        valid_operations = ", ".join(QL_INTERPOLATION_OPERATIONS)
        raise ValueError(
            f"Unknown interpolation operation '{operation}'. "
            f"Valid values are: {valid_operations}."
        )
    method_name = QL_INTERPOLATION_OPERATIONS[operation_key]
    if method_name is None:
        # Directly call the interpolation object for the VALUE operation
        return interpolation(x_value, allow_extrapolation)
    if not hasattr(interpolation, method_name):
        raise ValueError(
            f"Operation '{operation_key}' is not supported by "
            f"'{type(interpolation).__name__}'."
        )
    # Call the appropriate method on the interpolation object for other operations
    return getattr(interpolation, method_name)(x_value, allow_extrapolation)


@xlo.func(
    help="Apply a two-dimensional interpolation to calculate a value.",
    args={
        "interpolation": "The two-dimensional interpolation object to apply.",
        "x_value": "The x coordinate at which to apply the interpolation.",
        "y_value": "The y coordinate at which to apply the interpolation.",
        "allow_extrapolation": "Whether to allow extrapolation outside the data range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterpolation2DApply(
    interpolation: object,
    x_value: float,
    y_value: float,
    allow_extrapolation: bool = False,
    trigger=None,
) -> float:
    # Directly call the interpolation object for the VALUE operation
    return interpolation(x_value, y_value, allow_extrapolation)
