import QuantLib as ql
import pytest

from quantlib_xloil.optimizers import _qEndCriteriaType
from quantlib_xloil import (
	qlBoundaryConstraint,
	qlCompositeConstraint,
	qlEndCriteria,
	qlEndCriteriaSucceded,
	qlNoConstraint,
	qlNonhomogeneousBoundaryConstraint,
	qlPositiveConstraint,
)


def test_constraint_constructors_return_expected_types():
	no_constraint = qlNoConstraint()
	positive_constraint = qlPositiveConstraint()
	boundary_constraint = qlBoundaryConstraint(0.0, 2.0)
	composite_constraint = qlCompositeConstraint(positive_constraint, boundary_constraint)

	assert isinstance(no_constraint, ql.NoConstraint)
	assert isinstance(positive_constraint, ql.PositiveConstraint)
	assert isinstance(boundary_constraint, ql.BoundaryConstraint)
	assert isinstance(composite_constraint, ql.CompositeConstraint)


def test_qlNonhomogeneousBoundaryConstraint_converts_inputs_and_constructs():
	constraint = qlNonhomogeneousBoundaryConstraint(["0.0", 1], [1.5, "2.0"])

	assert isinstance(constraint, ql.NonhomogeneousBoundaryConstraint)


def test_qlNonhomogeneousBoundaryConstraint_size_mismatch_raises():
	with pytest.raises(RuntimeError, match="boundaries sizes are inconsistent"):
		qlNonhomogeneousBoundaryConstraint([0.0], [1.0, 2.0])


def test_qEndCriteriaType_case_insensitive_and_passthrough():
	assert _qEndCriteriaType("max_iterations") == ql.EndCriteria.MaxIterations
	assert _qEndCriteriaType("ZERO_GRADIENT_NORM") == ql.EndCriteria.ZeroGradientNorm
	assert _qEndCriteriaType(ql.EndCriteria.Unknown) == ql.EndCriteria.Unknown


def test_qEndCriteriaType_invalid_raises():
	with pytest.raises(ValueError, match="Cannot convert"):
		_qEndCriteriaType("bad-end-criteria")


def test_qlEndCriteria_constructor_and_succeeded_wrapper():
	end_criteria = qlEndCriteria(100, 10, 1.0e-8, 1.0e-8, 1.0e-8)

	assert isinstance(end_criteria, ql.EndCriteria)
	assert qlEndCriteriaSucceded(end_criteria, _qEndCriteriaType("MAX_ITERATIONS")) is False
	assert qlEndCriteriaSucceded(end_criteria, _qEndCriteriaType("UNKNOWN")) is False
