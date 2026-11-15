import numpy as np
import QuantLib as ql
import pytest

from quantlib_xloil.interpolation import (
    qInterpolator,
    qInterpolator2D,
    qlInterpolation,
    qlInterpolation2D,
    qlInterpolation2DApply,
    qlInterpolationApply,
)


def test_qInterpolator_conversion_and_passthrough():
    assert qInterpolator.__wrapped__("linear") is ql.LinearInterpolation
    assert qInterpolator.__wrapped__(ql.LinearInterpolation) is ql.LinearInterpolation


def test_qInterpolator2D_conversion_and_passthrough():
    assert qInterpolator2D.__wrapped__("bilinear") is ql.BilinearInterpolation
    assert (
        qInterpolator2D.__wrapped__(ql.BilinearInterpolation)
        is ql.BilinearInterpolation
    )


def test_qlInterpolation_value_and_derivative():
    x_values = [0.0, 1.0, 2.0, 3.0]
    y_values = [0.0, 1.0, 4.0, 9.0]
    linear = qlInterpolation(x_values, y_values, qInterpolator.__wrapped__("linear"))
    cubic = qlInterpolation(
        x_values, y_values, qInterpolator.__wrapped__("CUBICNATURALSPLINE")
    )

    assert qlInterpolationApply(linear, 1.5) == pytest.approx(2.5)
    assert qlInterpolationApply(cubic, 1.5, operation="DERIVATIVE") == pytest.approx(
        3.0
    )


def test_qlInterpolation_operation_and_extrapolation():
    x_values = [0.0, 1.0, 2.0]
    y_values = [0.0, 1.0, 4.0]

    linear = qlInterpolation(x_values, y_values, qInterpolator.__wrapped__("LINEAR"))

    assert qlInterpolationApply(linear, 2.0, operation="PRIMITIVE") == pytest.approx(
        3.0
    )
    assert qlInterpolationApply(linear, 3.0, allow_extrapolation=True) == pytest.approx(
        7.0
    )


def test_qlInterpolation_raises_for_unknown_interpolator_or_operation():
    x_values = [0.0, 1.0]
    y_values = [0.0, 1.0]

    with pytest.raises(ValueError, match="Unknown type"):
        qInterpolator.__wrapped__("UNKNOWN")
    with pytest.raises(ValueError, match="Unknown interpolation operation"):
        qlInterpolationApply(
            qlInterpolation(x_values, y_values, qInterpolator.__wrapped__("LINEAR")),
            0.5,
            operation="UNKNOWN",
        )
    with pytest.raises(ValueError, match="not supported"):
        qlInterpolationApply(
            qlInterpolation(
                x_values, y_values, qInterpolator.__wrapped__("CONVEXMONOTONE")
            ),
            0.5,
            operation="DERIVATIVE",
        )


def test_qlInterpolation_two_dimensional_bilinear_and_bicubic():
    x_values = [0.0, 1.0, 2.0, 3.0]
    y_values = [0.0, 1.0, 2.0]
    values = [[0.0, 0.0, 0.0], [1.0, 1.0, 1.0], [4.0, 4.0, 4.0], [4.0, 4.0, 4.0]]
    values = np.array(values)  # Convert to numpy array for shape checking

    bilinear = qlInterpolation2D(
        x_values, y_values, values, qInterpolator2D.__wrapped__("BILINEAR")
    )
    bicubic = qlInterpolation2D(
        x_values, y_values, values, qInterpolator2D.__wrapped__("BICUBICSPLINE")
    )

    assert qlInterpolation2DApply(bilinear, 1.0, 1.0) == pytest.approx(1.0)
    assert qlInterpolation2DApply(bicubic, 1.0, 1.0) == pytest.approx(1.0)


def test_qlInterpolation_two_dimensional_raises_for_unknown_interpolator():
    with pytest.raises(ValueError, match="Unknown type"):
        qInterpolator2D.__wrapped__("UNKNOWN")
