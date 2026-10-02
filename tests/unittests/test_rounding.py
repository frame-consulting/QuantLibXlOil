import QuantLib as ql
import pytest

from quantlib_xloil.rounding import qRoundingMethod, qlRounding, qlRoundingApply


def test_qRoundingMethod_case_insensitive_and_passthrough():
    assert qRoundingMethod.__wrapped__("up") == ql.UpRounding
    assert qRoundingMethod.__wrapped__("  Down  ") == ql.DownRounding
    assert qRoundingMethod.__wrapped__("closest") == ql.ClosestRounding
    assert qRoundingMethod.__wrapped__("CEILING") == ql.CeilingTruncation
    assert qRoundingMethod.__wrapped__("floor") == ql.FloorTruncation
    assert qRoundingMethod.__wrapped__(ql.UpRounding) == ql.UpRounding


def test_qRoundingMethod_invalid_raises():
    with pytest.raises(ValueError, match="Unknown type: BAD-METHOD"):
        qRoundingMethod.__wrapped__("bad-method")


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
    rounding = qlRounding(qRoundingMethod.__wrapped__(method_name), 2)

    assert isinstance(rounding, ql.Rounding)
    assert qlRoundingApply(rounding, value) == pytest.approx(expected)


def test_qlRounding_custom_digit():
    rounding = qlRounding(qRoundingMethod.__wrapped__("CLOSEST"), 2, 3)

    assert isinstance(rounding, ql.Rounding)
    assert qlRoundingApply(rounding, 1.233) == pytest.approx(1.24)
