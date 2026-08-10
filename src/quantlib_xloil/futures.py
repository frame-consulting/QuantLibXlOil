import QuantLib as ql
import xloil as xlo

from quantlib_xloil.calendars import qCalendar
from quantlib_xloil.daycounters import qDayCounter

from .cashflows import qRateAveragingType
from .config import EXCEL_GROUP_NAME
from .date import qDate, qPeriod
from .ratehelpers import qQuoteHandle
from .utilities import (
    enum_value,
    to_float_list,
    UNKNOWN_KEY,
    UNKNOWN_VALUE,
)

QL_PERPETUAL_FUTURES_PAYOFF_TYPE = {
    "INVERSE": ql.PerpetualFutures.Inverse,
    "LINEAR": ql.PerpetualFutures.Linear,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_PERPETUAL_FUTURES_FUNDING_TYPE = {
    "FUNDINGWITHCURRENTSPOT": ql.PerpetualFutures.FundingWithCurrentSpot,
    "FUNDINGWITHPREVIOUSSPOT": ql.PerpetualFutures.FundingWithPreviousSpot,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_DISCOUNTING_PERPETUAL_FUTURES_ENGINE_INTERPOLATION_TYPE = {
    "CUBICSPLINE": ql.DiscountingPerpetualFuturesEngine.CubicSpline,
    "LINEAR": ql.DiscountingPerpetualFuturesEngine.Linear,
    "PIECEWISECONSTANT": ql.DiscountingPerpetualFuturesEngine.PiecewiseConstant,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qPerpetualFuturesPayoffType(payoff_type: str) -> int:
    return enum_value(payoff_type, QL_PERPETUAL_FUTURES_PAYOFF_TYPE)


def _qPerpetualFuturesFundingType(funding_type: str) -> int:
    return enum_value(funding_type, QL_PERPETUAL_FUTURES_FUNDING_TYPE)


def _qDiscountingPerpetualFuturesEngineInterpolationType(
    interp_type: str,
) -> int:
    return enum_value(
        interp_type, QL_DISCOUNTING_PERPETUAL_FUTURES_ENGINE_INTERPOLATION_TYPE
    )


@xlo.converter()
def qPerpetualFuturesPayoffType(payoff_type: str | int | float):
    return _qPerpetualFuturesPayoffType(payoff_type)


@xlo.converter()
def qPerpetualFuturesFundingType(funding_type: str):
    return _qPerpetualFuturesFundingType(funding_type)


@xlo.converter()
def qDiscountingPerpetualFuturesEngineInterpolationType(interp_type: str):
    return _qDiscountingPerpetualFuturesEngineInterpolationType(interp_type)


@xlo.func(
    help="Create an OvernightIndexFuture object.",
    args={
        "overnight_index": "The overnight index.",
        "value_date": "The value date of the future.",
        "maturity_date": "The maturity date of the future.",
        "convexity_adjustment": "Optional convexity adjustment as a quote handle.",
        "averaging_method": "The rate averaging method.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexFuture(
    overnight_index: ql.OvernightIndex,
    value_date: qDate,
    maturity_date: qDate,
    convexity_adjustment: qQuoteHandle = ql.QuoteHandle(),
    averaging_method: qRateAveragingType = ql.RateAveraging.Compound,
    trigger=None,
) -> ql.OvernightIndexFuture:
    return ql.OvernightIndexFuture(
        overnight_index,
        value_date,
        maturity_date,
        convexity_adjustment,
        averaging_method,
    )


@xlo.func(
    help="Get the convexity adjustment of an OvernightIndexFuture.",
    args={
        "overnight_index_future": "The OvernightIndexFuture object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexFutureConvexityAdjustment(
    overnight_index_future: ql.OvernightIndexFuture, trigger=None
) -> float:
    return overnight_index_future.convexityAdjustment()


@xlo.func(
    help="Create a PerpetualFutures object.",
    args={
        "payoff_type": "The payoff type (Linear or Inverse).",
        "funding_type": "The funding type.",
        "funding_frequency": "The funding frequency.",
        "calendar": "The calendar for funding dates.",
        "day_counter": "The day counter for funding periods.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPerpetualFutures(
    payoff_type: qPerpetualFuturesPayoffType,
    funding_type: qPerpetualFuturesFundingType = ql.PerpetualFutures.FundingWithCurrentSpot,
    funding_frequency: qPeriod = ql.Period(8, ql.Hours),
    calendar: qCalendar = ql.NullCalendar(),
    day_counter: qDayCounter = ql.ActualActual(ql.ActualActual.ISDA),
    trigger=None,
) -> ql.PerpetualFutures:
    return ql.PerpetualFutures(
        payoff_type, funding_type, funding_frequency, calendar, day_counter
    )


@xlo.func(
    help="Create a DiscountingPerpetualFuturesEngine object.",
    args={
        "domestic_discount_curve": "The domestic discount curve.",
        "foreign_discount_curve": "The foreign discount curve.",
        "asset_spot": "The asset spot quote handle.",
        "funding_times": "The funding times as an array.",
        "funding_rates": "The funding rates as an array.",
        "interest_rate_diffs": "The interest rate differences as an array.",
        "funding_interp_type": "The interpolation type for funding.",
        "max_t": "The maximum time.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDiscountingPerpetualFuturesEngine(
    domestic_discount_curve: ql.YieldTermStructureHandle,
    foreign_discount_curve: ql.YieldTermStructureHandle,
    asset_spot: qQuoteHandle,
    funding_times: xlo.Array(dims=1),
    funding_rates: xlo.Array(dims=1),
    interest_rate_diffs: xlo.Array(dims=1),
    funding_interp_type: qDiscountingPerpetualFuturesEngineInterpolationType = ql.DiscountingPerpetualFuturesEngine.PiecewiseConstant,
    max_t: float = 60.0,
    trigger=None,
) -> ql.DiscountingPerpetualFuturesEngine:
    _funding_times = to_float_list(funding_times)
    _funding_rates = to_float_list(funding_rates)
    _interest_rate_diffs = to_float_list(interest_rate_diffs)
    return ql.DiscountingPerpetualFuturesEngine(
        domestic_discount_curve,
        foreign_discount_curve,
        asset_spot,
        _funding_times,
        _funding_rates,
        _interest_rate_diffs,
        funding_interp_type,
        max_t,
    )
