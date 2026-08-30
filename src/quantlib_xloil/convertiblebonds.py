import QuantLib as ql
import xloil as xlo

from .calendars import qBusinessDayConvention, qCalendar
from .config import EXCEL_GROUP_NAME
from .date import qDate, qPeriod
from .daycounters import qDayCounter
from .options import qBinomialEngineType
from .ratehelpers import qQuoteHandle
from .utilities import to_float_list, to_object_list


@xlo.func(
    help="Create a QuantLib ConvertibleZeroCouponBond object.",
    args={
        "exercise": "Exercise specification.",
        "conversion_ratio": "Conversion ratio.",
        "issue_date": "Bond issue date.",
        "settlement_days": "Settlement days.",
        "day_counter": "Day count convention.",
        "schedule": "Bond schedule.",
        "redemption": "Redemption amount.",
        "callability": "Array of callability specifications.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlConvertibleZeroCouponBond(
    exercise: ql.Exercise,
    conversion_ratio: float,
    issue_date: qDate,
    settlement_days: int,
    day_counter: qDayCounter,
    schedule: ql.Schedule,
    redemption: float = 100.0,
    callability: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.ConvertibleZeroCouponBond:
    return ql.ConvertibleZeroCouponBond(
        exercise,
        conversion_ratio,
        to_object_list(callability, ql.Callability),
        issue_date,
        settlement_days,
        day_counter,
        schedule,
        redemption,
    )


@xlo.func(
    help="Create a QuantLib ConvertibleFixedCouponBond object.",
    args={
        "exercise": "Exercise specification.",
        "conversion_ratio": "Conversion ratio.",
        "issue_date": "Bond issue date.",
        "settlement_days": "Settlement days.",
        "coupons": "Array of coupon rates.",
        "day_counter": "Day count convention.",
        "schedule": "Bond schedule.",
        "redemption": "Redemption amount.",
        "ex_coupon_period": "Ex-coupon period.",
        "ex_coupon_calendar": "Ex-coupon calendar.",
        "ex_coupon_convention": "Ex-coupon business day convention.",
        "ex_coupon_end_of_month": "Use end-of-month adjustment for ex-coupon dates.",
        "callability": "Array of callability specifications.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlConvertibleFixedCouponBond(
    exercise: ql.Exercise,
    conversion_ratio: float,
    issue_date: qDate,
    settlement_days: int,
    coupons: xlo.Array(dims=1),
    day_counter: qDayCounter,
    schedule: ql.Schedule,
    redemption: float = 100.0,
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar: qCalendar = ql.NullCalendar(),
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    callability: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.ConvertibleFixedCouponBond:
    return ql.ConvertibleFixedCouponBond(
        exercise,
        conversion_ratio,
        to_object_list(callability, ql.Callability),
        issue_date,
        settlement_days,
        to_float_list(coupons),
        day_counter,
        schedule,
        redemption,
        ex_coupon_period,
        ex_coupon_calendar,
        ex_coupon_convention,
        ex_coupon_end_of_month,
    )


@xlo.func(
    help="Create a QuantLib ConvertibleFloatingRateBond object.",
    args={
        "exercise": "Exercise specification.",
        "conversion_ratio": "Conversion ratio.",
        "issue_date": "Bond issue date.",
        "settlement_days": "Settlement days.",
        "index": "Ibor index.",
        "fixing_days": "Fixing days.",
        "spreads": "Array of coupon spreads.",
        "day_counter": "Day count convention.",
        "schedule": "Bond schedule.",
        "redemption": "Redemption amount.",
        "ex_coupon_period": "Ex-coupon period.",
        "ex_coupon_calendar": "Ex-coupon calendar.",
        "ex_coupon_convention": "Ex-coupon business day convention.",
        "ex_coupon_end_of_month": "Use end-of-month adjustment for ex-coupon dates.",
        "callability": "Array of callability specifications.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlConvertibleFloatingRateBond(
    exercise: ql.Exercise,
    conversion_ratio: float,
    issue_date: qDate,
    settlement_days: int,
    index: ql.IborIndex,
    fixing_days: int,
    spreads: xlo.Array(dims=1),
    day_counter: qDayCounter,
    schedule: ql.Schedule,
    redemption: float = 100.0,
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar: qCalendar = ql.NullCalendar(),
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    callability: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.ConvertibleFloatingRateBond:
    return ql.ConvertibleFloatingRateBond(
        exercise,
        conversion_ratio,
        to_object_list(callability, ql.Callability),
        issue_date,
        settlement_days,
        index,
        fixing_days,
        to_float_list(spreads),
        day_counter,
        schedule,
        redemption,
        ex_coupon_period,
        ex_coupon_calendar,
        ex_coupon_convention,
        ex_coupon_end_of_month,
    )


@xlo.func(
    help="Create a QuantLib BinomialConvertibleEngine object.",
    args={
        "process": "Generalized Black-Scholes process.",
        "engine_type": "Binomial engine type.",
        "steps": "Number of binomial steps.",
        "credit_spread": "Credit spread quote handle.",
        "dividends": "Optional array of dividends.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBinomialConvertibleEngine(
    process: ql.GeneralizedBlackScholesProcess,
    engine_type: qBinomialEngineType,
    steps: int,
    credit_spread: qQuoteHandle,
    dividends: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.PricingEngine:
    return ql.BinomialConvertibleEngine(
        process,
        engine_type,
        steps,
        credit_spread,
        to_object_list(dividends, ql.Dividend),
    )
