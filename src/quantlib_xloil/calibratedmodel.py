import QuantLib as ql
import numpy as np
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import to_float_list, to_object_list

# CalibratedModel interface


@xlo.func(
    help="Calibrate a QuantLib CalibratedModel to a set of calibration helpers.",
    args={
        "model": "The QuantLib CalibratedModel to calibrate.",
        "calibration_helpers": "The calibration helpers to calibrate to.",
        "optimization_method": "The optimization method to use for calibration.",
        "end_criteria": "The end criteria to use for calibration.",
        "constraint": "The constraint to use for calibration.",
        "weights": "The weights to use for calibration.",
        "fix_parameters": "Whether to fix parameters during calibration.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalibratedModelCalibrate(
    model: ql.CalibratedModel,
    calibration_helpers: xlo.Array(dims=1),
    optimization_method: ql.OptimizationMethod,
    end_criteria: ql.EndCriteria,
    constraint: ql.Constraint = ql.NoConstraint(),
    weights: xlo.Array(dims=1) = [],
    fix_parameters: xlo.Array(dims=1) = [],
    trigger=None,
) -> bool:
    helpers_ = to_object_list(calibration_helpers, ql.CalibrationHelper)
    weights_ = [float(w) for w in weights]
    fix_parameters_ = [bool(p) for p in fix_parameters]
    model.calibrate(
        helpers_,
        optimization_method,
        end_criteria,
        constraint,
        weights_,
        fix_parameters_,
    )
    return True


@xlo.func(
    help="Return the parameters of a QuantLib CalibratedModel as a list.",
    args={"model": "The QuantLib CalibratedModel to get parameters from."},
    group=EXCEL_GROUP_NAME,
)
def qlCalibratedModelParams(
    model: ql.CalibratedModel,
    trigger=None,
) -> list[float]:
    return list(model.params())


@xlo.func(
    help="Set the parameters of a QuantLib CalibratedModel.",
    args={
        "model": "The QuantLib CalibratedModel to set parameters for.",
        "params": "The parameters to set.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalibratedModelSetParams(
    model: ql.CalibratedModel,
    params: xlo.Array(dims=1),
    trigger=None,
) -> bool:
    p_array = ql.Array(to_float_list(params))
    model.setParams(p_array)
    return True


@xlo.func(
    help="Return the value of a QuantLib CalibratedModel for a given set of parameters and calibration helpers.",
    args={
        "model": "The QuantLib CalibratedModel to evaluate.",
        "params": "The parameters to evaluate the model with.",
        "calibration_helpers": "The calibration helpers to evaluate the model with.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCalibratedModelValue(
    model: ql.CalibratedModel,
    params: xlo.Array(dims=1),
    calibration_helpers: xlo.Array(dims=1),
    trigger=None,
) -> float:
    p_array = ql.Array(to_float_list(params))
    helpers_ = to_object_list(calibration_helpers, ql.CalibrationHelper)
    return model.value(p_array, helpers_)


@xlo.func(
    help="Return the constraint of a QuantLib CalibratedModel.",
    args={"model": "The QuantLib CalibratedModel to get the constraint for."},
    group=EXCEL_GROUP_NAME,
)
def qlCalibratedModelConstraint(
    model: ql.CalibratedModel,
    trigger=None,
) -> ql.Constraint:
    return model.constraint()


@xlo.func(
    help="Return the end criteria of a QuantLib CalibratedModel.",
    args={"model": "The QuantLib CalibratedModel to get the end criteria for."},
    group=EXCEL_GROUP_NAME,
)
def qlCalibratedModelEndCriteria(
    model: ql.CalibratedModel,
    trigger=None,
) -> ql.EndCriteria:
    return model.endCriteria()


@xlo.func(
    help="Return the problem values of a QuantLib CalibratedModel.",
    args={"model": "The QuantLib CalibratedModel to get the problem values for."},
    group=EXCEL_GROUP_NAME,
)
def qlCalibratedModelProblemValues(
    model: ql.CalibratedModel,
    trigger=None,
) -> list[float]:
    return list(model.problemValues())


@xlo.func(
    help="Return the number of function evaluations of a QuantLib CalibratedModel.",
    args={"model": "The QuantLib CalibratedModel to get the function evaluations for."},
    group=EXCEL_GROUP_NAME,
)
def qlCalibratedModelProblemValuesFunctionEvaluation(
    model: ql.CalibratedModel,
    trigger=None,
) -> int:
    return model.functionEvaluation()


@xlo.func(
    help="Create a handle for a QuantLib CalibratedModel.",
    args={"model": "The QuantLib CalibratedModel to create a handle for."},
    group=EXCEL_GROUP_NAME,
)
def qlCalibratedModelHandle(
    model: ql.CalibratedModel,
    trigger=None,
) -> ql.CalibratedModelHandle:
    return ql.CalibratedModelHandle(model)
