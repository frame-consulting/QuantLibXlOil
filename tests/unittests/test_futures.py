import QuantLib as ql
import pytest

from quantlib_xloil.calendars import qlCalendar
from quantlib_xloil.currencies import qCurrency
from quantlib_xloil.futures import (
    qlDiscountingPerpetualFuturesEngine,
    qlOvernightIndexFuture,
    qlOvernightIndexFutureConvexityAdjustment,
    qlPerpetualFutures,
    qPerpetualFuturesFundingType,
    qPerpetualFuturesPayoffType,
    qDiscountingPerpetualFuturesEngineInterpolationType,
)
from quantlib_xloil.indexes import qlOvernightIndex
from quantlib_xloil.ratehelpers import qQuoteHandle


def test_qPerpetualFuturesPayoffType_linear():
    result = qPerpetualFuturesPayoffType.__wrapped__("LINEAR")
    assert result == ql.PerpetualFutures.Linear


def test_qPerpetualFuturesPayoffType_inverse():
    result = qPerpetualFuturesPayoffType.__wrapped__("INVERSE")
    assert result == ql.PerpetualFutures.Inverse


def test_qPerpetualFuturesPayoffType_invalid():
    with pytest.raises(ValueError):
        qPerpetualFuturesPayoffType.__wrapped__("INVALID")


def test_qPerpetualFuturesFundingType_funding_with_current_spot():
    result = qPerpetualFuturesFundingType.__wrapped__("FUNDINGWITHCURRENTSPOT")
    assert result == ql.PerpetualFutures.FundingWithCurrentSpot


def test_qPerpetualFuturesFundingType_funding_with_previous_spot():
    result = qPerpetualFuturesFundingType.__wrapped__("FUNDINGWITHPREVIOUSSPOT")
    assert result == ql.PerpetualFutures.FundingWithPreviousSpot


def test_qPerpetualFuturesFundingType_invalid():
    with pytest.raises(ValueError):
        qPerpetualFuturesFundingType.__wrapped__("INVALID")


def test_qDiscountingPerpetualFuturesEngineInterpolationType_piecewise_constant():
    result = qDiscountingPerpetualFuturesEngineInterpolationType.__wrapped__(
        "PIECEWISECONSTANT"
    )
    assert result == ql.DiscountingPerpetualFuturesEngine.PiecewiseConstant


def test_qDiscountingPerpetualFuturesEngineInterpolationType_linear():
    result = qDiscountingPerpetualFuturesEngineInterpolationType.__wrapped__("LINEAR")
    assert result == ql.DiscountingPerpetualFuturesEngine.Linear


def test_qDiscountingPerpetualFuturesEngineInterpolationType_cubic_spline():
    result = qDiscountingPerpetualFuturesEngineInterpolationType.__wrapped__(
        "CUBICSPLINE"
    )
    assert result == ql.DiscountingPerpetualFuturesEngine.CubicSpline


def test_qDiscountingPerpetualFuturesEngineInterpolationType_invalid():
    with pytest.raises(ValueError):
        qDiscountingPerpetualFuturesEngineInterpolationType.__wrapped__("INVALID")


def test_qlPerpetualFutures_default_parameters():
    perpetual = qlPerpetualFutures(ql.PerpetualFutures.Linear)
    assert isinstance(perpetual, ql.PerpetualFutures)


def test_qlPerpetualFutures_all_parameters():
    calendar = qlCalendar("UNITEDSTATES")
    day_counter = ql.ActualActual(ql.ActualActual.ISDA)
    funding_frequency = ql.Period(8, ql.Hours)

    perpetual = qlPerpetualFutures(
        payoff_type=qPerpetualFuturesPayoffType.__wrapped__("INVERSE"),
        funding_type=qPerpetualFuturesFundingType.__wrapped__(
            "FUNDINGWITHPREVIOUSSPOT"
        ),
        funding_frequency=funding_frequency,
        calendar=calendar,
        day_counter=day_counter,
    )
    assert isinstance(perpetual, ql.PerpetualFutures)


def test_qlOvernightIndexFuture_without_convexity_adjustment():
    calendar = qlCalendar("UNITEDSTATES")
    day_counter = ql.ActualActual(ql.ActualActual.ISDA)
    currency = qCurrency.__wrapped__("USD")

    overnight_index = qlOvernightIndex(
        family_name="SOFR",
        settlement_days=0,
        currency=currency,
        calendar=calendar,
        day_counter=day_counter,
    )

    value_date = ql.Date(
        1,
        1,
        2024,
    )
    maturity_date = ql.Date(1, 3, 2024)

    future = qlOvernightIndexFuture(
        overnight_index=overnight_index,
        value_date=value_date,
        maturity_date=maturity_date,
    )

    assert isinstance(future, ql.OvernightIndexFuture)


def test_qlOvernightIndexFuture_with_convexity_adjustment():
    calendar = qlCalendar("UNITEDSTATES")
    day_counter = ql.ActualActual(ql.ActualActual.ISDA)
    currency = qCurrency.__wrapped__("USD")

    overnight_index = qlOvernightIndex(
        family_name="SOFR",
        settlement_days=0,
        currency=currency,
        calendar=calendar,
        day_counter=day_counter,
    )

    value_date = ql.Date(1, 1, 2024)
    maturity_date = ql.Date(1, 3, 2024)
    convexity_adjustment = qQuoteHandle.__wrapped__(0.001)

    future = qlOvernightIndexFuture(
        overnight_index=overnight_index,
        value_date=value_date,
        maturity_date=maturity_date,
        convexity_adjustment=convexity_adjustment,
    )

    assert isinstance(future, ql.OvernightIndexFuture)


def test_qlOvernightIndexFutureConvexityAdjustment():
    calendar = qlCalendar("UNITEDSTATES")
    day_counter = ql.ActualActual(ql.ActualActual.ISDA)
    currency = qCurrency.__wrapped__("USD")

    overnight_index = qlOvernightIndex(
        family_name="SOFR",
        settlement_days=0,
        currency=currency,
        calendar=calendar,
        day_counter=day_counter,
    )

    value_date = ql.Date(1, 1, 2024)
    maturity_date = ql.Date(1, 3, 2024)
    convexity_value = 0.001
    convexity_adjustment = qQuoteHandle.__wrapped__(convexity_value)

    future = qlOvernightIndexFuture(
        overnight_index=overnight_index,
        value_date=value_date,
        maturity_date=maturity_date,
        convexity_adjustment=convexity_adjustment,
    )

    result = qlOvernightIndexFutureConvexityAdjustment(future)
    assert result == pytest.approx(convexity_value)


def test_qlDiscountingPerpetualFuturesEngine():
    day_counter = ql.ActualActual(ql.ActualActual.ISDA)
    reference_date = ql.Date(1, 1, 2024)

    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.05, day_counter)
    )

    asset_spot = qQuoteHandle.__wrapped__(100.0)

    funding_times = [0.25, 0.5, 0.75, 1.0]
    funding_rates = [0.01, 0.02, 0.03, 0.04]
    interest_rate_diffs = [0.001, 0.002, 0.003, 0.004]

    engine = qlDiscountingPerpetualFuturesEngine(
        domestic_discount_curve=flat_ts,
        foreign_discount_curve=flat_ts,
        asset_spot=asset_spot,
        funding_times=funding_times,
        funding_rates=funding_rates,
        interest_rate_diffs=interest_rate_diffs,
        funding_interp_type=qDiscountingPerpetualFuturesEngineInterpolationType.__wrapped__(
            "LINEAR"
        ),
        max_t=60.0,
    )

    assert isinstance(engine, ql.DiscountingPerpetualFuturesEngine)


def test_qlDiscountingPerpetualFuturesEngine_default_interp_type():
    day_counter = ql.ActualActual(ql.ActualActual.ISDA)
    reference_date = ql.Date(1, 1, 2024)

    flat_ts = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.05, day_counter)
    )

    asset_spot = qQuoteHandle.__wrapped__(100.0)

    funding_times = [0.25, 0.5]
    funding_rates = [0.01, 0.02]
    interest_rate_diffs = [0.001, 0.002]

    engine = qlDiscountingPerpetualFuturesEngine(
        domestic_discount_curve=flat_ts,
        foreign_discount_curve=flat_ts,
        asset_spot=asset_spot,
        funding_times=funding_times,
        funding_rates=funding_rates,
        interest_rate_diffs=interest_rate_diffs,
    )

    assert isinstance(engine, ql.DiscountingPerpetualFuturesEngine)
