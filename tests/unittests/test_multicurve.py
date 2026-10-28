import QuantLib as ql
import pytest

from quantlib_xloil.multicurve import (
    qlMultiCurve,
    qlMultiCurveAddBootstrappedCurve,
    qlMultiCurveAddNonBootstrappedCurve,
    qlRelinkableYieldTermStructureHandle,
)


def test_qlMultiCurve_add_bootstrapped_curve():
    original_eval = ql.Settings.instance().evaluationDate
    today = ql.Date(2, ql.January, 2025)
    try:
        ql.Settings.instance().evaluationDate = today
        accuracy = 1.0e-10
        multi_curve = qlMultiCurve(accuracy)
        internal_handle = qlRelinkableYieldTermStructureHandle()
        helpers = [
            ql.DepositRateHelper(
                rate,
                ql.Period(months, ql.Months),
                2,
                ql.TARGET(),
                ql.Following,
                False,
                ql.Actual360(),
            )
            for months, rate in ((1, 0.02), (3, 0.025), (6, 0.03), (12, 0.035))
        ]
        curve = ql.GlobalPiecewiseLogLinearDiscount(
            today,
            helpers,
            ql.Actual360(),
            ql.GlobalBootstrap(accuracy),
        )

        external_handle = qlMultiCurveAddBootstrappedCurve(
            multi_curve,
            internal_handle,
            ql.YieldTermStructureHandle(curve),
        )

        assert isinstance(external_handle, ql.YieldTermStructureHandle)
        assert external_handle.discount(today + 365) > 0.0
        for helper in helpers:
            assert helper.quoteError() == pytest.approx(0.0, abs=accuracy)
    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_qlMultiCurve_add_non_bootstrapped_curve():
    original_eval = ql.Settings.instance().evaluationDate
    today = ql.Date(2, ql.January, 2025)
    try:
        ql.Settings.instance().evaluationDate = today
        multi_curve = qlMultiCurve(1.0e-10)
        internal_handle = qlRelinkableYieldTermStructureHandle()
        curve = ql.YieldTermStructureHandle(
            ql.FlatForward(today, 0.02, ql.Actual365Fixed())
        )

        external_handle = qlMultiCurveAddNonBootstrappedCurve(
            multi_curve, internal_handle, curve
        )

        assert isinstance(external_handle, ql.YieldTermStructureHandle)
        assert external_handle.discount(today + 365) > 0.0
    finally:
        ql.Settings.instance().evaluationDate = original_eval
