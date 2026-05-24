import QuantLib as ql
import pytest

from quantlibxloil import qlRounding, qlRoundingApply
from quantlibxloil.rounding import _qRoundingMethod


def test_qRoundingMethod_case_insensitive_and_passthrough():
	assert _qRoundingMethod("up") == ql.UpRounding
	assert _qRoundingMethod("  Down  ") == ql.DownRounding
	assert _qRoundingMethod("closest") == ql.ClosestRounding
	assert _qRoundingMethod("CEILING") == ql.CeilingTruncation
	assert _qRoundingMethod("floor") == ql.FloorTruncation
	assert _qRoundingMethod(ql.UpRounding) == ql.UpRounding


def test_qRoundingMethod_invalid_raises():
	with pytest.raises(ValueError, match="Unknown rounding method"):
		_qRoundingMethod("bad-method")


@pytest.mark.parametrize(
	"method_name, value, expected",
	[
		("UP", 1.234, 1.24),
		("DOWN", 1.234, 1.23),
		("CLOSEST", 1.235, 1.24),
		("CEILING", 1.231, 1.23),
		("FLOOR", 1.239, 1.24),
	],
)
def test_qlRounding_and_apply(method_name, value, expected):
	rounding = qlRounding(_qRoundingMethod(method_name), 2)

	assert isinstance(rounding, ql.Rounding)
	assert qlRoundingApply(rounding, value) == pytest.approx(expected)


def test_qlRounding_custom_digit():
	rounding = qlRounding(_qRoundingMethod("CLOSEST"), 2, 3)

	assert isinstance(rounding, ql.Rounding)
	assert qlRoundingApply(rounding, 1.233) == pytest.approx(1.24)
