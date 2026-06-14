import QuantLib as ql
import pytest

from quantlib_xloil.parameter import (
    qlConstantParameter,
    qlNullParameter,
    qlParameterAtTime,
    qlParameterConstraint,
    qlParameterParams,
    qlParameterSetParam,
    qlParameterSize,
    qlParameterTestParams,
    qlPiecewiseConstantParameter,
)
from quantlib_xloil.optimizers import (
    qlBoundaryConstraint,
    qlNoConstraint,
    qlPositiveConstraint,
)


def test_qlNullParameter_interface_methods():
    parameter = qlNullParameter()

    assert isinstance(parameter, ql.NullParameter)
    assert qlParameterSize(parameter) == 0
    assert qlParameterParams(parameter) == []
    assert qlParameterAtTime(parameter, 0.5) == pytest.approx(0.0)
    assert isinstance(qlParameterConstraint(parameter), ql.Constraint)


def test_qlConstantParameter_with_explicit_value_and_accessors():
    constraint = qlPositiveConstraint()
    parameter = qlConstantParameter(constraint, 0.2)

    assert isinstance(parameter, ql.ConstantParameter)
    assert qlParameterSize(parameter) == 1
    assert qlParameterParams(parameter) == pytest.approx([0.2])
    assert qlParameterAtTime(parameter, 0.0) == pytest.approx(0.2)
    assert qlParameterAtTime(parameter, 10.0) == pytest.approx(0.2)
    assert isinstance(qlParameterConstraint(parameter), ql.Constraint)


def test_qlConstantParameter_without_value_constructs_valid_parameter():
    parameter = qlConstantParameter(qlNoConstraint())

    assert isinstance(parameter, ql.ConstantParameter)
    assert qlParameterSize(parameter) == 1
    assert len(qlParameterParams(parameter)) == 1


def test_qlParameterSetParam_updates_value_and_checks_bounds():
    parameter = qlConstantParameter(qlNoConstraint(), 0.2)

    assert qlParameterSetParam(parameter, 0, 0.4) is True
    assert qlParameterParams(parameter) == pytest.approx([0.4])

    with pytest.raises(IndexError, match="out of bounds"):
        qlParameterSetParam(parameter, -1, 0.1)

    with pytest.raises(IndexError, match="out of bounds"):
        qlParameterSetParam(parameter, 1, 0.1)


def test_qlPiecewiseConstantParameter_and_test_params():
    times = [1.0, 2.0]
    values = [0.1, 0.2, 0.3]
    constraint = qlBoundaryConstraint(0.0, 10.0)
    parameter = qlPiecewiseConstantParameter(times, values, constraint)

    assert isinstance(parameter, ql.PiecewiseConstantParameter)
    assert qlParameterSize(parameter) == 3
    assert len(qlParameterParams(parameter)) == 3
    assert qlParameterTestParams(parameter, [0.1, 0.2, 0.3]) is True

    qlParameterSetParam(parameter, 0, 0.1)
    qlParameterSetParam(parameter, 1, 0.2)
    qlParameterSetParam(parameter, 2, 0.3)

    assert qlParameterAtTime(parameter, 0.5) == pytest.approx(0.1)
    assert qlParameterAtTime(parameter, 1.5) == pytest.approx(0.2)
    assert qlParameterAtTime(parameter, 2.5) == pytest.approx(0.3)
