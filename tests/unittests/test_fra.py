import QuantLib as ql
import pytest

from quantlib_xloil.fra import (
    qPosition,
    qlForwardRateAgreement,
    qlForwardRateAgreement2,
    qlForwardRateAgreementAmount,
    qlForwardRateAgreementFixingDate,
    qlForwardRateAgreementForwardRate,
)


def _fra_context():
    evaluation_date = ql.Date(2, ql.January, 2024)
    ql.Settings.instance().evaluationDate = evaluation_date
    curve = ql.YieldTermStructureHandle(
        ql.FlatForward(evaluation_date, 0.03, ql.Actual365Fixed())
    )
    index = ql.USDLibor(ql.Period("3M"), curve)
    value_date = ql.Date(4, ql.April, 2024)
    maturity_date = index.maturityDate(value_date)
    return curve, index, value_date, maturity_date


def test_qFraPosition_converter():
    assert qPosition.__wrapped__("long") == ql.Position.Long
    assert qPosition.__wrapped__("SHORT") == ql.Position.Short
    assert qPosition.__wrapped__(ql.Position.Long) == ql.Position.Long


def test_qlForwardRateAgreement_constructor_and_accessors():
    original_evaluation_date = ql.Settings.instance().evaluationDate
    try:
        curve, index, value_date, _ = _fra_context()
        fra = qlForwardRateAgreement(
            index, value_date, ql.Position.Long, 0.04, 100000.0, curve
        )

        assert isinstance(fra, ql.ForwardRateAgreement)
        assert qlForwardRateAgreementFixingDate(fra) == index.fixingDate(value_date)
        forward_rate = qlForwardRateAgreementForwardRate(fra)
        assert isinstance(forward_rate, ql.InterestRate)
        assert forward_rate.rate() > 0.0
        assert qlForwardRateAgreementAmount(fra) == pytest.approx(fra.amount())
        assert fra.NPV() == pytest.approx(fra.amount() * curve.discount(value_date))
    finally:
        ql.Settings.instance().evaluationDate = original_evaluation_date


def test_qlForwardRateAgreement2_explicit_maturity_and_default_discount_curve():
    original_evaluation_date = ql.Settings.instance().evaluationDate
    try:
        _, index, value_date, maturity_date = _fra_context()
        fra = qlForwardRateAgreement2(
            index,
            value_date,
            maturity_date,
            qPosition.__wrapped__("SHORT"),
            0.04,
            100000.0,
        )

        assert isinstance(fra, ql.ForwardRateAgreement)
        assert qlForwardRateAgreementFixingDate(fra) == index.fixingDate(value_date)
        forward_rate = qlForwardRateAgreementForwardRate(fra)
        assert isinstance(forward_rate, ql.InterestRate)
        assert forward_rate.rate() > 0.0
        assert qlForwardRateAgreementAmount(fra) == pytest.approx(fra.amount())
    finally:
        ql.Settings.instance().evaluationDate = original_evaluation_date
