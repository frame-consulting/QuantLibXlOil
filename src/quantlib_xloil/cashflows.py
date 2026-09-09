import QuantLib as ql
import xloil as xlo

from .calendars import (
    qBusinessDayConvention,
    qCalendar,
    qPeriod,
    QL_BUSINESSDAYCONVENTION,
)
from .config import EXCEL_GROUP_NAME
from .date import _to_date_list, qDate, qFrequency, _qDate
from .daycounters import qDayCounter
from .termstructures import qCompounding
from .utilities import (
    enum_value,
    first_key,
    to_float_list,
    to_int_list,
    to_object_list,
    UNKNOWN_KEY,
    UNKNOWN_VALUE,
)

QL_DURATION_TYPE = {
    "MACAULAY": ql.Duration.Macaulay,
    "MODIFIED": ql.Duration.Modified,
    "SIMPLE": ql.Duration.Simple,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_RATE_AVERAGING_TYPE = {
    "COMPOUND": ql.RateAveraging.Compound,
    "SIMPLE": ql.RateAveraging.Simple,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_TIMING_ADJUSTMENT_TYPE = {
    "BLACK76": ql.BlackIborCouponPricer.Black76,
    "BIVARIATELOGNORMAL": ql.BlackIborCouponPricer.BivariateLognormal,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_YIELD_CURVE_MODEL = {
    "STANDARD": ql.GFunctionFactory.Standard,
    "EXACTYIELD": ql.GFunctionFactory.ExactYield,
    "PARALLELSHIFTS": ql.GFunctionFactory.ParallelShifts,
    "NONPARALLELSHIFTS": ql.GFunctionFactory.NonParallelShifts,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qDurationType(duration_type: str) -> int:
    return enum_value(duration_type, QL_DURATION_TYPE)


def _qRateAveragingType(averaging_type: str) -> int:
    return enum_value(averaging_type, QL_RATE_AVERAGING_TYPE)


def _qTimingAdjustmentType(timing_adjustment_type: str) -> int:
    return enum_value(timing_adjustment_type, QL_TIMING_ADJUSTMENT_TYPE)


def _qYieldCurveModel(yield_curve_model: str):
    return enum_value(yield_curve_model, QL_YIELD_CURVE_MODEL)


@xlo.converter()
def qDurationType(duration_type: str) -> int:
    return _qDurationType(duration_type)


@xlo.converter()
def qRateAveragingType(averaging_type: str) -> int:
    return _qRateAveragingType(averaging_type)


@xlo.converter()
def qTimingAdjustmentType(timing_adjustment_type: str) -> int:
    return _qTimingAdjustmentType(timing_adjustment_type)


@xlo.converter()
def qYieldCurveModel(yield_curve_model: str):
    return _qYieldCurveModel(yield_curve_model)


@xlo.converter()
def qQuoteHandle(rate) -> ql.QuoteHandle:
    if isinstance(rate, ql.QuoteHandle):
        return rate
    if isinstance(rate, (int, float)):
        return ql.QuoteHandle(ql.SimpleQuote(float(rate)))
    raise ValueError(f"Cannot convert {rate} to QuoteHandle.")


@xlo.func(
    help="Return cash-flow amount.",
    args={
        "cashflow": "QuantLib CashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowAmount(cashflow: ql.CashFlow, trigger=None) -> float:
    return cashflow.amount()


@xlo.func(
    help="Return cash-flow payment date.",
    args={
        "cashflow": "QuantLib CashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowDate(cashflow: ql.CashFlow, trigger=None) -> ql.Date:
    return cashflow.date()


@xlo.func(
    help="Check whether the cash flow has occurred.",
    args={
        "cashflow": "QuantLib CashFlow.",
        "ref_date": "Reference date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowHasOccurred(
    cashflow: ql.CashFlow, ref_date: qDate = ql.Date(), trigger=None
) -> bool:
    return cashflow.hasOccurred(ref_date)


@xlo.func(
    help="Create a QuantLib SimpleCashFlow object.",
    args={
        "amount": "Cash-flow amount.",
        "date": "Payment date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSimpleCashFlow(amount: float, date: qDate, trigger=None) -> ql.SimpleCashFlow:
    return ql.SimpleCashFlow(amount, date)


@xlo.func(
    help="Create a QuantLib Redemption cash flow.",
    args={
        "amount": "Cash-flow amount.",
        "date": "Payment date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRedemption(amount: float, date: qDate, trigger=None) -> ql.Redemption:
    return ql.Redemption(amount, date)


@xlo.func(
    help="Create a QuantLib AmortizingPayment cash flow.",
    args={
        "amount": "Cash-flow amount.",
        "date": "Payment date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAmortizingPayment(
    amount: float, date: qDate, trigger=None
) -> ql.AmortizingPayment:
    return ql.AmortizingPayment(amount, date)


@xlo.func(
    help="Create a QuantLib IndexedCashFlow object.",
    args={
        "notional": "Notional amount.",
        "index": "Index used for fixing.",
        "base_date": "Base fixing date.",
        "fixing_date": "Current fixing date.",
        "payment_date": "Payment date.",
        "growth_only": "Whether to pay growth only.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexedCashFlow(
    notional: float,
    index: ql.Index,
    base_date: qDate,
    fixing_date: qDate,
    payment_date: qDate,
    growth_only: bool = False,
    trigger=None,
) -> ql.IndexedCashFlow:
    return ql.IndexedCashFlow(
        notional, index, base_date, fixing_date, payment_date, growth_only
    )


@xlo.func(
    help="Return indexed cash flow notional amount.",
    args={
        "cashflow": "QuantLib IndexedCashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexedCashFlowNotional(cashflow: ql.IndexedCashFlow, trigger=None) -> float:
    return cashflow.notional()


@xlo.func(
    help="Return indexed cash flow base date.",
    args={
        "cashflow": "QuantLib IndexedCashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexedCashFlowBaseDate(cashflow: ql.IndexedCashFlow, trigger=None) -> ql.Date:
    return cashflow.baseDate()


@xlo.func(
    help="Return indexed cash flow fixing date.",
    args={
        "cashflow": "QuantLib IndexedCashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexedCashFlowFixingDate(cashflow: ql.IndexedCashFlow, trigger=None) -> ql.Date:
    return cashflow.fixingDate()


@xlo.func(
    help="Return indexed cash flow base fixing value.",
    args={
        "cashflow": "QuantLib IndexedCashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexedCashFlowBaseFixing(cashflow: ql.IndexedCashFlow, trigger=None) -> float:
    return cashflow.baseFixing()


@xlo.func(
    help="Return indexed cash flow index fixing value.",
    args={
        "cashflow": "QuantLib IndexedCashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexedCashFlowIndexFixing(cashflow: ql.IndexedCashFlow, trigger=None) -> float:
    return cashflow.indexFixing()


@xlo.func(
    help="Return indexed cash flow index.",
    args={
        "cashflow": "QuantLib IndexedCashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexedCashFlowIndex(cashflow: ql.IndexedCashFlow, trigger=None) -> ql.Index:
    return cashflow.index()


xlo.func(
    help="Return whether the indexed cash flow pays growth only.",
    args={
        "cashflow": "QuantLib IndexedCashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)


def qlIndexedCashFlowGrowthOnly(cashflow: ql.IndexedCashFlow, trigger=None) -> bool:
    return cashflow.growthOnly()


@xlo.func(
    help="Cast a CashFlow to IndexedCashFlow if possible.",
    args={
        "cashflow": "QuantLib CashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAsIndexedCashFlow(cashflow: ql.CashFlow, trigger=None) -> ql.IndexedCashFlow:
    return ql.as_indexed_cashflow(cashflow)


@xlo.func(
    help="Return coupon nominal.",
    args={
        "coupon": "QuantLib Coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCouponNominal(coupon: ql.Coupon, trigger=None) -> float:
    return coupon.nominal()


@xlo.func(
    help="Return coupon accrual start date.",
    args={
        "coupon": "QuantLib Coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCouponAccrualStartDate(coupon: ql.Coupon, trigger=None) -> ql.Date:
    return coupon.accrualStartDate()


@xlo.func(
    help="Return coupon accrual end date.",
    args={
        "coupon": "QuantLib Coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCouponAccrualEndDate(coupon: ql.Coupon, trigger=None) -> ql.Date:
    return coupon.accrualEndDate()


@xlo.func(
    help="Return coupon reference period start date.",
    args={
        "coupon": "QuantLib Coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCouponReferencePeriodStart(coupon: ql.Coupon, trigger=None) -> ql.Date:
    return coupon.referencePeriodStart()


@xlo.func(
    help="Return coupon reference period end date.",
    args={
        "coupon": "QuantLib Coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCouponReferencePeriodEnd(coupon: ql.Coupon, trigger=None) -> ql.Date:
    return coupon.referencePeriodEnd()


@xlo.func(
    help="Return coupon ex-coupon date.",
    args={
        "coupon": "QuantLib Coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCouponExCouponDate(coupon: ql.Coupon, trigger=None) -> ql.Date:
    return coupon.exCouponDate()


@xlo.func(
    help="Return coupon rate.",
    args={
        "coupon": "QuantLib Coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCouponRate(coupon: ql.Coupon, trigger=None) -> float:
    return coupon.rate()


@xlo.func(
    help="Return coupon accrual period.",
    args={
        "coupon": "QuantLib Coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCouponAccrualPeriod(coupon: ql.Coupon, trigger=None) -> float:
    return coupon.accrualPeriod()


@xlo.func(
    help="Return coupon accrual days.",
    args={
        "coupon": "QuantLib Coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCouponAccrualDays(coupon: ql.Coupon, trigger=None) -> int:
    return coupon.accrualDays()


@xlo.func(
    help="Return coupon day counter.",
    args={
        "coupon": "QuantLib Coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCouponDayCounter(coupon: ql.Coupon, trigger=None) -> ql.DayCounter:
    return coupon.dayCounter()


@xlo.func(
    help="Return coupon accrued amount at a given date.",
    args={
        "coupon": "QuantLib Coupon.",
        "date": "Accrual date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCouponAccruedAmount(coupon: ql.Coupon, date: qDate, trigger=None) -> float:
    return coupon.accruedAmount(date)


@xlo.func(
    help="Cast a CashFlow to Coupon if possible.",
    args={
        "cashflow": "QuantLib CashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAsCoupon(cashflow: ql.CashFlow, trigger=None) -> ql.Coupon:
    return ql.as_coupon(cashflow)


@xlo.func(
    help="Create a QuantLib FixedRateCoupon object.",
    args={
        "payment_date": "Payment date.",
        "nominal": "Nominal amount.",
        "rate": "Coupon rate.",
        "day_counter": "Day count convention.",
        "start_date": "Accrual start date.",
        "end_date": "Accrual end date.",
        "ref_period_start": "Reference period start date.",
        "ref_period_end": "Reference period end date.",
        "ex_coupon_date": "Ex-coupon date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedRateCoupon(
    payment_date: qDate,
    nominal: float,
    rate: float,
    day_counter: qDayCounter,
    start_date: qDate,
    end_date: qDate,
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    ex_coupon_date: qDate = ql.Date(),
    trigger=None,
) -> ql.FixedRateCoupon:
    return ql.FixedRateCoupon(
        payment_date,
        nominal,
        rate,
        day_counter,
        start_date,
        end_date,
        ref_period_start,
        ref_period_end,
        ex_coupon_date,
    )


@xlo.func(
    help="Return fixed-rate coupon interest rate.",
    args={
        "coupon": "QuantLib FixedRateCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedRateCouponInterestRate(
    coupon: ql.FixedRateCoupon, trigger=None
) -> ql.InterestRate:
    return coupon.interestRate()


@xlo.func(
    help="Cast a CashFlow to FixedRateCoupon if possible.",
    args={
        "cashflow": "QuantLib CashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAsFixedRateCoupon(cashflow: ql.CashFlow, trigger=None) -> ql.FixedRateCoupon:
    return ql.as_fixed_rate_coupon(cashflow)


@xlo.func(
    help="Return floating-rate coupon fixing date.",
    args={
        "coupon": "QuantLib FloatingRateCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponFixingDate(
    coupon: ql.FloatingRateCoupon, trigger=None
) -> ql.Date:
    return coupon.fixingDate()


@xlo.func(
    help="Return floating-rate coupon fixing days.",
    args={
        "coupon": "QuantLib FloatingRateCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponFixingDays(coupon: ql.FloatingRateCoupon, trigger=None) -> int:
    return coupon.fixingDays()


@xlo.func(
    help="Return floating-rate coupon fixing convention.",
    args={
        "coupon": "QuantLib FloatingRateCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponFixingConvention(
    coupon: ql.FloatingRateCoupon, trigger=None
) -> str:
    return first_key(QL_BUSINESSDAYCONVENTION, coupon.fixingConvention(), UNKNOWN_KEY)


@xlo.func(
    help="Return whether the floating-rate coupon is in arrears.",
    args={
        "coupon": "QuantLib FloatingRateCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponIsInArrears(
    coupon: ql.FloatingRateCoupon, trigger=None
) -> bool:
    return coupon.isInArrears()


@xlo.func(
    help="Return floating-rate coupon gearing.",
    args={
        "coupon": "QuantLib FloatingRateCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponGearing(coupon: ql.FloatingRateCoupon, trigger=None) -> float:
    return coupon.gearing()


@xlo.func(
    help="Return floating-rate coupon spread.",
    args={
        "coupon": "QuantLib FloatingRateCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponSpread(coupon: ql.FloatingRateCoupon, trigger=None) -> float:
    return coupon.spread()


@xlo.func(
    help="Return floating-rate coupon index fixing.",
    args={
        "coupon": "QuantLib FloatingRateCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponIndexFixing(
    coupon: ql.FloatingRateCoupon, trigger=None
) -> float:
    return coupon.indexFixing()


@xlo.func(
    help="Return floating-rate coupon adjusted fixing.",
    args={
        "coupon": "QuantLib FloatingRateCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponAdjustedFixing(
    coupon: ql.FloatingRateCoupon, trigger=None
) -> float:
    return coupon.adjustedFixing()


@xlo.func(
    help="Return floating-rate coupon convexity adjustment.",
    args={
        "coupon": "QuantLib FloatingRateCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponConvexityAdjustment(
    coupon: ql.FloatingRateCoupon, trigger=None
) -> float:
    return coupon.convexityAdjustment()


@xlo.func(
    help="Return floating-rate coupon price from a discount curve handle.",
    args={
        "coupon": "QuantLib FloatingRateCoupon.",
        "discount_curve": "Discount curve handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponPrice(
    coupon: ql.FloatingRateCoupon,
    discount_curve: ql.YieldTermStructureHandle,
    trigger=None,
) -> float:
    return coupon.price(discount_curve)


@xlo.func(
    help="Return floating-rate coupon index.",
    args={
        "coupon": "QuantLib FloatingRateCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponIndex(
    coupon: ql.FloatingRateCoupon, trigger=None
) -> ql.InterestRateIndex:
    return coupon.index()


@xlo.func(
    help="Set floating-rate coupon pricer.",
    args={
        "coupon": "QuantLib FloatingRateCoupon.",
        "pricer": "Floating-rate coupon pricer.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponSetPricer(
    coupon: ql.FloatingRateCoupon,
    pricer: ql.FloatingRateCouponPricer,
    trigger=None,
) -> bool:
    coupon.setPricer(pricer)
    return True


@xlo.func(
    help="Cast a CashFlow to FloatingRateCoupon if possible.",
    args={
        "cashflow": "QuantLib CashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAsFloatingRateCoupon(
    cashflow: ql.CashFlow, trigger=None
) -> ql.FloatingRateCoupon:
    return ql.as_floating_rate_coupon(cashflow)


@xlo.func(
    help="Create a QuantLib CappedFlooredCoupon object.",
    args={
        "underlying": "Underlying floating-rate coupon.",
        "cap": "Cap rate.",
        "floor": "Floor rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCoupon(
    underlying: ql.FloatingRateCoupon,
    cap: float = ql.nullDouble(),
    floor: float = ql.nullDouble(),
    trigger=None,
) -> ql.CappedFlooredCoupon:
    return ql.CappedFlooredCoupon(underlying, cap, floor)


@xlo.func(
    help="Return capped/floored coupon cap.",
    args={
        "coupon": "QuantLib CappedFlooredCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCouponCap(coupon: ql.CappedFlooredCoupon, trigger=None) -> float:
    return coupon.cap()


@xlo.func(
    help="Return capped/floored coupon floor.",
    args={
        "coupon": "QuantLib CappedFlooredCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCouponFloor(coupon: ql.CappedFlooredCoupon, trigger=None) -> float:
    return coupon.floor()


@xlo.func(
    help="Return capped/floored coupon effective cap.",
    args={
        "coupon": "QuantLib CappedFlooredCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCouponEffectiveCap(
    coupon: ql.CappedFlooredCoupon, trigger=None
) -> float:
    return coupon.effectiveCap()


@xlo.func(
    help="Return capped/floored coupon effective floor.",
    args={
        "coupon": "QuantLib CappedFlooredCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCouponEffectiveFloor(
    coupon: ql.CappedFlooredCoupon, trigger=None
) -> float:
    return coupon.effectiveFloor()


@xlo.func(
    help="Return whether the capped/floored coupon has a cap.",
    args={
        "coupon": "QuantLib CappedFlooredCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCouponIsCapped(coupon: ql.CappedFlooredCoupon, trigger=None) -> bool:
    return coupon.isCapped()


@xlo.func(
    help="Return whether the capped/floored coupon has a floor.",
    args={
        "coupon": "QuantLib CappedFlooredCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCouponIsFloored(
    coupon: ql.CappedFlooredCoupon, trigger=None
) -> bool:
    return coupon.isFloored()


@xlo.func(
    help="Create a QuantLib OvernightIndexedCoupon object.",
    args={
        "payment_date": "Payment date.",
        "nominal": "Nominal amount.",
        "start_date": "Accrual start date.",
        "end_date": "Accrual end date.",
        "overnight_index": "Overnight index.",
        "gearing": "Coupon gearing.",
        "spread": "Coupon spread.",
        "ref_period_start": "Reference period start date.",
        "ref_period_end": "Reference period end date.",
        "day_counter": "Day count convention.",
        "telescopic_value_dates": "Use telescopic dates.",
        "averaging_method": "Rate averaging method.",
        "lookback_days": "Lookback days.",
        "lockout_days": "Lockout days.",
        "apply_observation_shift": "Apply observation shift.",
        "compound_spread": "Compound spread daily.",
        "rate_computation_start_date": "Rate computation start date.",
        "rate_computation_end_date": "Rate computation end date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCoupon(
    payment_date: qDate,
    nominal: float,
    start_date: qDate,
    end_date: qDate,
    overnight_index: ql.OvernightIndex,
    gearing: float = 1.0,
    spread: float = 0.0,
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    day_counter=None,
    telescopic_value_dates: bool = False,
    averaging_method: qRateAveragingType = ql.RateAveraging.Compound,
    lookback_days: int = ql.nullInt(),
    lockout_days: int = 0,
    apply_observation_shift: bool = False,
    compound_spread: bool = False,
    rate_computation_start_date: qDate = ql.Date(),
    rate_computation_end_date: qDate = ql.Date(),
    trigger=None,
) -> ql.OvernightIndexedCoupon:
    if day_counter is not None:
        day_counter = qDayCounter.__wrapped__(day_counter)

    _KWARGS = {
        "day_counter": "dayCounter",
        "telescopic_value_dates": "telescopicValueDates",
        "averaging_method": "averagingMethod",
        "lookback_days": "lookbackDays",
        "lockout_days": "lockoutDays",
        "apply_observation_shift": "applyObservationShift",
        "compound_spread": "compoundSpread",
        "rate_computation_start_date": "rateComputationStartDate",
        "rate_computation_end_date": "rateComputationEndDate",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.OvernightIndexedCoupon(
        payment_date,
        nominal,
        start_date,
        end_date,
        overnight_index,
        gearing,
        spread,
        ref_period_start,
        ref_period_end,
        **kwargs,
    )


@xlo.func(
    help="Return overnight coupon fixing dates.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponFixingDates(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> tuple[ql.Date, ...]:
    return tuple(coupon.fixingDates())


@xlo.func(
    help="Return overnight coupon interest dates.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponInterestDates(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> tuple[ql.Date, ...]:
    return tuple(coupon.interestDates())


@xlo.func(
    help="Return overnight coupon day-fraction steps.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponDt(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> tuple[float, ...]:
    return tuple(coupon.dt())


@xlo.func(
    help="Return overnight coupon index fixings.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponIndexFixings(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> tuple[float, ...]:
    return tuple(coupon.indexFixings())


@xlo.func(
    help="Return overnight coupon value dates.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponValueDates(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> tuple[ql.Date, ...]:
    return tuple(coupon.valueDates())


@xlo.func(
    help="Return overnight coupon averaging method.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponAveragingMethod(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> qRateAveragingType:
    return first_key(QL_RATE_AVERAGING_TYPE, coupon.averagingMethod(), UNKNOWN_KEY)


@xlo.func(
    help="Return overnight coupon lockout days.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponLockoutDays(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> int:
    return coupon.lockoutDays()


@xlo.func(
    help="Return whether observation shift is applied.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponApplyObservationShift(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> bool:
    return coupon.applyObservationShift()


@xlo.func(
    help="Return whether spread is compounded daily.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponCompoundSpreadDaily(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> bool:
    return coupon.compoundSpreadDaily()


@xlo.func(
    help="Return whether telescopic formula can be applied.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponCanApplyTelescopicFormula(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> bool:
    return coupon.canApplyTelescopicFormula()


@xlo.func(
    help="Return overnight coupon effective spread.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponEffectiveSpread(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> float:
    return coupon.effectiveSpread()


@xlo.func(
    help="Return overnight coupon effective index fixing.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponEffectiveIndexFixing(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> float:
    return coupon.effectiveIndexFixing()


@xlo.func(
    help="Return overnight coupon rate-computation start date.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponRateComputationStartDate(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> ql.Date:
    return coupon.rateComputationStartDate()


@xlo.func(
    help="Return overnight coupon rate-computation end date.",
    args={
        "coupon": "QuantLib OvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponRateComputationEndDate(
    coupon: ql.OvernightIndexedCoupon, trigger=None
) -> ql.Date:
    return coupon.rateComputationEndDate()


@xlo.func(
    help="Create a QuantLib CappedFlooredOvernightIndexedCoupon object.",
    args={
        "underlying": "Underlying overnight indexed coupon.",
        "cap": "Cap rate.",
        "floor": "Floor rate.",
        "naked_option": "Whether to use naked option payoff.",
        "daily_cap_floor": "Whether cap/floor is applied daily.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCoupon(
    underlying: ql.OvernightIndexedCoupon,
    cap: float = ql.nullDouble(),
    floor: float = ql.nullDouble(),
    naked_option: bool = False,
    daily_cap_floor: bool = False,
    trigger=None,
) -> ql.CappedFlooredOvernightIndexedCoupon:
    return ql.CappedFlooredOvernightIndexedCoupon(
        underlying, cap, floor, naked_option, daily_cap_floor
    )


@xlo.func(
    help="Return capped/floored overnight coupon cap.",
    args={
        "coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponCap(
    coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger=None
) -> float:
    return coupon.cap()


@xlo.func(
    help="Return capped/floored overnight coupon floor.",
    args={
        "coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponFloor(
    coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger=None
) -> float:
    return coupon.floor()


@xlo.func(
    help="Return capped/floored overnight coupon effective caplet volatility.",
    args={
        "coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponEffectiveCapletVolatility(
    coupon: ql.CappedFlooredOvernightIndexedCoupon,
    trigger=None,
) -> float:
    return coupon.effectiveCapletVolatility()


@xlo.func(
    help="Return capped/floored overnight coupon effective floorlet volatility.",
    args={
        "coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponEffectiveFloorletVolatility(
    coupon: ql.CappedFlooredOvernightIndexedCoupon,
    trigger=None,
) -> float:
    return coupon.effectiveFloorletVolatility()


@xlo.func(
    help="Return whether the capped/floored overnight coupon has a cap.",
    args={
        "coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponIsCapped(
    coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger=None
) -> bool:
    return coupon.isCapped()


@xlo.func(
    help="Return whether the capped/floored overnight coupon has a floor.",
    args={
        "coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponIsFloored(
    coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger=None
) -> bool:
    return coupon.isFloored()


@xlo.func(
    help="Return capped/floored overnight coupon underlying coupon.",
    args={
        "coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponUnderlying(
    coupon: ql.CappedFlooredOvernightIndexedCoupon,
    trigger=None,
) -> ql.OvernightIndexedCoupon:
    return coupon.underlying()


@xlo.func(
    help="Return whether capped/floored overnight coupon uses naked option payoff.",
    args={
        "coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponNakedOption(
    coupon: ql.CappedFlooredOvernightIndexedCoupon,
    trigger=None,
) -> bool:
    return coupon.nakedOption()


@xlo.func(
    help="Return whether cap/floor is applied daily for capped/floored overnight coupon.",
    args={
        "coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponDailyCapFloor(
    coupon: ql.CappedFlooredOvernightIndexedCoupon,
    trigger=None,
) -> bool:
    return coupon.dailyCapFloor()


@xlo.func(
    help="Return whether spread is compounded daily for capped/floored overnight coupon.",
    args={
        "coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponCompoundSpreadDaily(
    coupon: ql.CappedFlooredOvernightIndexedCoupon,
    trigger=None,
) -> bool:
    return coupon.compoundSpreadDaily()


@xlo.func(
    help="Return capped/floored overnight coupon averaging method label.",
    args={
        "coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponAveragingMethod(
    coupon: ql.CappedFlooredOvernightIndexedCoupon,
    trigger=None,
) -> str:
    return first_key(QL_RATE_AVERAGING_TYPE, coupon.averagingMethod(), UNKNOWN_KEY)


@xlo.func(
    help="Cast a CashFlow to OvernightIndexedCoupon if possible.",
    args={
        "cashflow": "QuantLib CashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAsOvernightIndexedCoupon(
    cashflow: ql.CashFlow, trigger=None
) -> ql.OvernightIndexedCoupon:
    return ql.as_overnight_indexed_coupon(cashflow)


@xlo.func(
    help="Cast a CashFlow to CappedFlooredOvernightIndexedCoupon if possible.",
    args={
        "cashflow": "QuantLib CashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAsCappedFlooredOvernightIndexedCoupon(
    cashflow: ql.CashFlow, trigger=None
) -> ql.CappedFlooredOvernightIndexedCoupon:
    return ql.as_capped_floored_overnight_indexed_coupon(cashflow)


@xlo.func(
    help="Create a QuantLib IborCoupon object.",
    args={
        "payment_date": "Payment date.",
        "nominal": "Nominal amount.",
        "start_date": "Accrual start date.",
        "end_date": "Accrual end date.",
        "fixing_days": "Fixing days.",
        "index": "Ibor index.",
        "gearing": "Coupon gearing.",
        "spread": "Coupon spread.",
        "ref_period_start": "Reference period start date.",
        "ref_period_end": "Reference period end date.",
        "day_counter": "Day count convention.",
        "is_in_arrears": "Whether fixing is in arrears.",
        "ex_coupon_date": "Ex-coupon date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIborCoupon(
    payment_date: qDate,
    nominal: float,
    start_date: qDate,
    end_date: qDate,
    fixing_days: int,
    index: ql.IborIndex,
    gearing: float = 1.0,
    spread: float = 0.0,
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    day_counter=None,
    is_in_arrears: bool = False,
    ex_coupon_date: qDate = ql.Date(),
    fixing_convention: qBusinessDayConvention = ql.Preceding,
    trigger=None,
) -> ql.IborCoupon:
    if day_counter is not None:
        day_counter = qDayCounter.__wrapped__(day_counter)

    _KWARGS = {
        "day_counter": "dayCounter",
        "is_in_arrears": "isInArrears",
        "ex_coupon_date": "exCouponDate",
        "fixing_convention": "fixingConvention",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    cpn = ql.IborCoupon(
        payment_date,
        nominal,
        start_date,
        end_date,
        fixing_days,
        index,
        gearing,
        spread,
        ref_period_start,
        ref_period_end,
        **kwargs,
    )
    cpn.setPricer(ql.BlackIborCouponPricer())
    return cpn


@xlo.func(
    help="Return whether the Ibor coupon has been fixed.",
    args={
        "coupon": "QuantLib IborCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIborCouponHasFixed(coupon: ql.IborCoupon, trigger=None) -> bool:
    return coupon.hasFixed()


@xlo.func(
    help="Create a QuantLib CappedFlooredIborCoupon object.",
    args={
        "payment_date": "Payment date.",
        "nominal": "Nominal amount.",
        "start_date": "Accrual start date.",
        "end_date": "Accrual end date.",
        "fixing_days": "Fixing days.",
        "index": "Ibor index.",
        "gearing": "Coupon gearing.",
        "spread": "Coupon spread.",
        "cap": "Cap rate.",
        "floor": "Floor rate.",
        "ref_period_start": "Reference period start date.",
        "ref_period_end": "Reference period end date.",
        "day_counter": "Day count convention.",
        "is_in_arrears": "Whether fixing is in arrears.",
        "ex_coupon_date": "Ex-coupon date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredIborCoupon(
    payment_date: qDate,
    nominal: float,
    start_date: qDate,
    end_date: qDate,
    fixing_days: int,
    index: ql.IborIndex,
    gearing: float = 1.0,
    spread: float = 0.0,
    cap: float = ql.nullDouble(),
    floor: float = ql.nullDouble(),
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    day_counter=None,
    is_in_arrears: bool = False,
    ex_coupon_date: qDate = ql.Date(),
    trigger=None,
) -> ql.CappedFlooredIborCoupon:
    if day_counter is not None:
        day_counter = qDayCounter.__wrapped__(day_counter)

    _KWARGS = {
        "day_counter": "dayCounter",
        "is_in_arrears": "isInArrears",
        "ex_coupon_date": "exCouponDate",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.CappedFlooredIborCoupon(
        payment_date,
        nominal,
        start_date,
        end_date,
        fixing_days,
        index,
        gearing,
        spread,
        cap,
        floor,
        ref_period_start,
        ref_period_end,
        **kwargs,
    )


@xlo.func(
    help="Create a QuantLib MultipleResetsCoupon object.",
    args={
        "payment_date": "Payment date.",
        "nominal": "Nominal amount.",
        "reset_schedule": "Reset schedule.",
        "fixing_days": "Fixing days.",
        "index": "Ibor index.",
        "gearing": "Coupon gearing.",
        "coupon_spread": "Coupon spread.",
        "rate_spread": "Rate spread.",
        "ref_period_start": "Reference period start date.",
        "ref_period_end": "Reference period end date.",
        "day_counter": "Day count convention.",
        "ex_coupon_date": "Ex-coupon date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultipleResetsCoupon(
    payment_date: qDate,
    nominal: float,
    reset_schedule: ql.Schedule,
    fixing_days: int,
    index: ql.IborIndex,
    gearing: float = 1.0,
    coupon_spread: float = 0.0,
    rate_spread: float = 0.0,
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    day_counter=None,
    ex_coupon_date: qDate = ql.Date(),
    trigger=None,
) -> ql.MultipleResetsCoupon:
    if day_counter is not None:
        day_counter = qDayCounter.__wrapped__(day_counter)

    _KWARGS = {
        "day_counter": "dayCounter",
        "ex_coupon_date": "exCouponDate",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    cpn = ql.MultipleResetsCoupon(
        payment_date,
        nominal,
        reset_schedule,
        fixing_days,
        index,
        gearing,
        coupon_spread,
        rate_spread,
        ref_period_start,
        ref_period_end,
        **kwargs,
    )
    cpn.setPricer(ql.AveragingMultipleResetsPricer())
    return cpn


@xlo.func(
    help="Return the vector of fixing dates for an overnight indexed coupon.",
    args={
        "coupon": "QuantLib MultipleResetsCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultipleResetsCouponFixingDates(
    coupon: ql.MultipleResetsCoupon, trigger=None
) -> tuple[ql.Date, ...]:
    return tuple(coupon.fixingDates())


@xlo.func(
    help="Return the vector of day-fraction steps (dt) for an overnight indexed coupon.",
    args={
        "coupon": "QuantLib MultipleResetsCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultipleResetsCouponDt(
    coupon: ql.MultipleResetsCoupon, trigger=None
) -> tuple[float, ...]:
    return tuple(coupon.dt())


@xlo.func(
    help="Return the vector of value dates for an overnight indexed coupon.",
    args={
        "coupon": "QuantLib MultipleResetsCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultipleResetsCouponValueDates(
    coupon: ql.MultipleResetsCoupon, trigger=None
) -> tuple[ql.Date, ...]:
    return tuple(coupon.valueDates())


@xlo.func(
    help="Return the rate spread for an overnight indexed coupon.",
    args={
        "coupon": "QuantLib MultipleResetsCoupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultipleResetsCouponRateSpread(
    coupon: ql.MultipleResetsCoupon, trigger=None
) -> float:
    return coupon.rateSpread()


@xlo.func(
    help="Cast a CashFlow to MultipleResetsCoupon if possible.",
    args={
        "cashflow": "QuantLib CashFlow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAsMultipleResetsCoupon(
    cashflow: ql.CashFlow, trigger=None
) -> ql.MultipleResetsCoupon:
    return ql.as_multiple_resets_coupon(cashflow)


@xlo.func(
    help="Return the caplet volatility handle from an IborCouponPricer.",
    args={
        "pricer": "QuantLib IborCouponPricer.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIborCouponPricerCapletVolatility(
    pricer: ql.IborCouponPricer, trigger=None
) -> ql.OptionletVolatilityStructureHandle:
    return pricer.capletVolatility()


@xlo.func(
    help="Set the caplet volatility handle for an IborCouponPricer.",
    args={
        "pricer": "QuantLib IborCouponPricer.",
        "volatility": "Optionlet volatility handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIborCouponPricerSetCapletVolatility(
    pricer: ql.IborCouponPricer,
    volatility: ql.OptionletVolatilityStructureHandle,
    trigger=None,
) -> bool:
    pricer.setCapletVolatility(volatility)
    return True


@xlo.func(
    help="Create a QuantLib BlackIborCouponPricer.",
    args={
        "volatility": "Optionlet volatility handle.",
        "timing_adjustment": "Coupon pricer timing adjustment.",
        "correlation": "Correlation between the underlying index and the optionlet volatility.",
        "use_indexed_coupon": "Whether to use indexed coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackIborCouponPricer(
    volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(),
    timing_adjustment: qTimingAdjustmentType = ql.BlackIborCouponPricer.Black76,
    correlation: qQuoteHandle = ql.QuoteHandle(ql.SimpleQuote(1.0)),
    use_indexed_coupon: bool = None,
    trigger=None,
) -> ql.BlackIborCouponPricer:
    return ql.BlackIborCouponPricer(
        volatility, timing_adjustment, correlation, use_indexed_coupon
    )


@xlo.func(
    help="Create a QuantLib CompoundingOvernightIndexedCouponPricer.",
    group=EXCEL_GROUP_NAME,
)
def qlCompoundingOvernightIndexedCouponPricer(
    trigger=None,
) -> ql.CompoundingOvernightIndexedCouponPricer:
    return ql.CompoundingOvernightIndexedCouponPricer()


@xlo.func(
    help="Create a QuantLib BlackCompoundingOvernightIndexedCouponPricer.",
    args={
        "volatility": "Optionlet volatility handle.",
        "effective_volatility_input": "Whether volatility input is effective volatility.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCompoundingOvernightIndexedCouponPricer(
    volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(),
    effective_volatility_input: bool = False,
    trigger=None,
) -> ql.BlackCompoundingOvernightIndexedCouponPricer:
    return ql.BlackCompoundingOvernightIndexedCouponPricer(
        volatility, effective_volatility_input
    )


@xlo.func(
    help="Create a QuantLib ArithmeticAveragedOvernightIndexedCouponPricer.",
    args={
        "mean_reversion": "Mean reversion parameter.",
        "volatility": "Convexity-adjustment volatility.",
        "by_approx": "Use approximation method.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlArithmeticAveragedOvernightIndexedCouponPricer(
    mean_reversion: float = 0.03,
    volatility: float = 0.0,
    by_approx: bool = False,
    trigger=None,
) -> ql.ArithmeticAveragedOvernightIndexedCouponPricer:
    return ql.ArithmeticAveragedOvernightIndexedCouponPricer(
        mean_reversion, volatility, by_approx
    )


@xlo.func(
    help="Create a QuantLib BlackAveragingOvernightIndexedCouponPricer.",
    args={
        "volatility": "Optionlet volatility handle.",
        "effective_volatility_input": "Whether volatility input is effective volatility.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackAveragingOvernightIndexedCouponPricer(
    volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(),
    effective_volatility_input: bool = False,
    trigger=None,
) -> ql.BlackAveragingOvernightIndexedCouponPricer:
    return ql.BlackAveragingOvernightIndexedCouponPricer(
        volatility, effective_volatility_input
    )


@xlo.func(
    help="Create a QuantLib CompoundingMultipleResetsPricer.",
    group=EXCEL_GROUP_NAME,
)
def qlCompoundingMultipleResetsPricer(
    trigger=None,
) -> ql.CompoundingMultipleResetsPricer:
    return ql.CompoundingMultipleResetsPricer()


@xlo.func(
    help="Create a QuantLib AveragingMultipleResetsPricer.",
    group=EXCEL_GROUP_NAME,
)
def qlAveragingMultipleResetsPricer(trigger=None) -> ql.AveragingMultipleResetsPricer:
    return ql.AveragingMultipleResetsPricer()


@xlo.func(
    help="Create a QuantLib CmsCoupon object.",
    args={
        "payment_date": "Payment date.",
        "nominal": "Nominal amount.",
        "start_date": "Accrual start date.",
        "end_date": "Accrual end date.",
        "fixing_days": "Fixing days.",
        "index": "Swap index.",
        "gearing": "Coupon gearing.",
        "spread": "Coupon spread.",
        "ref_period_start": "Reference period start date.",
        "ref_period_end": "Reference period end date.",
        "day_counter": "Day count convention.",
        "is_in_arrears": "Whether fixing is in arrears.",
        "ex_coupon_date": "Ex-coupon date.",
        "fixing_convention": "Fixing convention.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCmsCoupon(
    payment_date: qDate,
    nominal: float,
    start_date: qDate,
    end_date: qDate,
    fixing_days: int,
    index: ql.SwapIndex,
    gearing: float = 1.0,
    spread: float = 0.0,
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    day_counter=None,
    is_in_arrears: bool = False,
    ex_coupon_date: qDate = ql.Date(),
    fixing_convention: qBusinessDayConvention = ql.Preceding,
    trigger=None,
) -> ql.CmsCoupon:
    if day_counter is not None:
        day_counter = qDayCounter.__wrapped__(day_counter)
    _KWARGS = {
        "day_counter": "dayCounter",
        "is_in_arrears": "isInArrears",
        "ex_coupon_date": "exCouponDate",
        "fixing_convention": "fixingConvention",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.CmsCoupon(
        payment_date,
        nominal,
        start_date,
        end_date,
        fixing_days,
        index,
        gearing,
        spread,
        ref_period_start,
        ref_period_end,
        **kwargs,
    )


@xlo.func(
    help="Create a QuantLib CmsSpreadCoupon object.",
    args={
        "payment_date": "Payment date.",
        "nominal": "Nominal amount.",
        "start_date": "Accrual start date.",
        "end_date": "Accrual end date.",
        "fixing_days": "Fixing days.",
        "index": "Swap spread index.",
        "gearing": "Coupon gearing.",
        "spread": "Coupon spread.",
        "ref_period_start": "Reference period start date.",
        "ref_period_end": "Reference period end date.",
        "day_counter": "Day count convention.",
        "is_in_arrears": "Whether fixing is in arrears.",
        "ex_coupon_date": "Ex-coupon date.",
        "fixing_convention": "Fixing convention.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCmsSpreadCoupon(
    payment_date: qDate,
    nominal: float,
    start_date: qDate,
    end_date: qDate,
    fixing_days: int,
    index: ql.SwapSpreadIndex,
    gearing: float = 1.0,
    spread: float = 0.0,
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    day_counter=None,
    is_in_arrears: bool = False,
    ex_coupon_date: qDate = ql.Date(),
    fixing_convention: qBusinessDayConvention = ql.Preceding,
    trigger=None,
) -> ql.CmsSpreadCoupon:
    if day_counter is not None:
        day_counter = qDayCounter.__wrapped__(day_counter)
    _KWARGS = {
        "day_counter": "dayCounter",
        "is_in_arrears": "isInArrears",
        "ex_coupon_date": "exCouponDate",
        "fixing_convention": "fixingConvention",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.CmsSpreadCoupon(
        payment_date,
        nominal,
        start_date,
        end_date,
        fixing_days,
        index,
        gearing,
        spread,
        ref_period_start,
        ref_period_end,
        **kwargs,
    )


@xlo.func(
    help="Return the swaption volatility handle from a CmsCouponPricer.",
    args={
        "pricer": "QuantLib CmsCouponPricer.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCmsCouponPricerSwaptionVolatility(
    pricer: ql.CmsCouponPricer, trigger=None
) -> ql.SwaptionVolatilityStructureHandle:
    return pricer.swaptionVolatility()


@xlo.func(
    help="Set the swaption volatility handle for a CmsCouponPricer.",
    args={
        "pricer": "QuantLib CmsCouponPricer.",
        "volatility": "Swaption volatility structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCmsCouponPricerSetSwaptionVolatility(
    pricer: ql.CmsCouponPricer,
    volatility: ql.SwaptionVolatilityStructureHandle,
    trigger=None,
) -> bool:
    pricer.setSwaptionVolatility(volatility)
    return True


@xlo.func(
    help="Create a QuantLib AnalyticHaganPricer for CMS coupon pricing.",
    args={
        "volatility": "Swaption volatility structure handle.",
        "model": "Yield curve model (e.g., HullWhite, BlackKarasinski).",
        "mean_reversion": "Mean reversion quote handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticHaganPricer(
    volatility: ql.SwaptionVolatilityStructureHandle,
    model: qYieldCurveModel,
    mean_reversion: qQuoteHandle,
    trigger=None,
) -> ql.AnalyticHaganPricer:
    return ql.AnalyticHaganPricer(volatility, model, mean_reversion)


@xlo.func(
    help="Create a QuantLib NumericHaganPricer for CMS coupon pricing.",
    args={
        "volatility": "Swaption volatility structure handle.",
        "model": "Yield curve model (e.g., HullWhite, BlackKarasinski).",
        "mean_reversion": "Mean reversion quote handle.",
        "lower_limit": "Lower integration limit for the rate.",
        "upper_limit": "Upper integration limit for the rate.",
        "precision": "Numerical integration precision.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNumericHaganPricer(
    volatility: ql.SwaptionVolatilityStructureHandle,
    model: qYieldCurveModel,
    mean_reversion: qQuoteHandle,
    lower_limit: float = 0.0,
    upper_limit: float = 1.0,
    precision: float = 1e-6,
    trigger=None,
) -> ql.NumericHaganPricer:
    return ql.NumericHaganPricer(
        volatility, model, mean_reversion, lower_limit, upper_limit, precision
    )


# TODO no kwargs available
@xlo.func(
    help="Create a QuantLib CappedFlooredCmsCoupon object.",
    args={
        "payment_date": "Payment date.",
        "nominal": "Nominal amount.",
        "start_date": "Accrual start date.",
        "end_date": "Accrual end date.",
        "fixing_days": "Fixing days.",
        "index": "Swap index.",
        "gearing": "Coupon gearing.",
        "spread": "Coupon spread.",
        "cap": "Cap rate.",
        "floor": "Floor rate.",
        "ref_period_start": "Reference period start date.",
        "ref_period_end": "Reference period end date.",
        "day_counter": "Day count convention.",
        "is_in_arrears": "Whether fixing is in arrears.",
        "ex_coupon_date": "Ex-coupon date.",
        "fixing_convention": "Fixing convention.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCmsCoupon(
    payment_date: qDate,
    nominal: float,
    start_date: qDate,
    end_date: qDate,
    fixing_days: int,
    index: ql.SwapIndex,
    gearing: float = 1.0,
    spread: float = 0.0,
    cap: float = ql.nullDouble(),
    floor: float = ql.nullDouble(),
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    day_counter=None,
    ex_coupon_date: qDate = ql.Date(),
    fixing_convention: qBusinessDayConvention = ql.Preceding,
    trigger=None,
) -> ql.CappedFlooredCmsCoupon:
    if day_counter is not None:
        day_counter = qDayCounter.__wrapped__(day_counter)

    _KWARGS = {
        "day_counter": "dayCounter",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.CappedFlooredCmsCoupon(
        payment_date,
        nominal,
        start_date,
        end_date,
        fixing_days,
        index,
        gearing,
        spread,
        cap,
        floor,
        ref_period_start,
        ref_period_end,
        **kwargs,
    )


# TODO no kwargs available
@xlo.func(
    help="Create a QuantLib CappedFlooredCmsSpreadCoupon object.",
    args={
        "payment_date": "Payment date.",
        "nominal": "Nominal amount.",
        "start_date": "Accrual start date.",
        "end_date": "Accrual end date.",
        "fixing_days": "Fixing days.",
        "index": "Swap spread index.",
        "gearing": "Coupon gearing.",
        "spread": "Coupon spread.",
        "cap": "Cap rate.",
        "floor": "Floor rate.",
        "ref_period_start": "Reference period start date.",
        "ref_period_end": "Reference period end date.",
        "day_counter": "Day count convention.",
        "is_in_arrears": "Whether fixing is in arrears.",
        "ex_coupon_date": "Ex-coupon date.",
        "fixing_convention": "Fixing convention.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCmsSpreadCoupon(
    payment_date: qDate,
    nominal: float,
    start_date: qDate,
    end_date: qDate,
    fixing_days: int,
    index: ql.SwapSpreadIndex,
    gearing: float = 1.0,
    spread: float = 0.0,
    cap: float = ql.nullDouble(),
    floor: float = ql.nullDouble(),
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    day_counter=None,
    ex_coupon_date: qDate = ql.Date(),
    fixing_convention: qBusinessDayConvention = ql.Preceding,
    trigger=None,
) -> ql.CappedFlooredCmsSpreadCoupon:
    if day_counter is not None:
        day_counter = qDayCounter.__wrapped__(day_counter)

    _KWARGS = {
        "day_counter": "dayCounter",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.CappedFlooredCmsSpreadCoupon(
        payment_date,
        nominal,
        start_date,
        end_date,
        fixing_days,
        index,
        gearing,
        spread,
        cap,
        floor,
        ref_period_start,
        ref_period_end,
        **kwargs,
    )


# TODO LinearTsrPricer


@xlo.func(
    help="Return the correlation quote handle from a CmsSpreadCouponPricer.",
    args={
        "pricer": "QuantLib CmsSpreadCouponPricer.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCmsSpreadCouponPricerCorrelation(
    pricer: ql.CmsSpreadCouponPricer, trigger=None
) -> ql.QuoteHandle:
    return pricer.correlation()


@xlo.func(
    help="Set the correlation quote handle for a CmsSpreadCouponPricer.",
    args={
        "pricer": "QuantLib CmsSpreadCouponPricer.",
        "correlation": "Correlation quote handle (optional).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCmsSpreadCouponPricerSetCorrelation(
    pricer: ql.CmsSpreadCouponPricer,
    correlation: qQuoteHandle = ql.QuoteHandle(),
    trigger=None,
) -> bool:
    pricer.setCorrelation(correlation)
    return True


# TODO to test
@xlo.func(
    help="Create a QuantLib LognormalCmsSpreadPricer.",
    args={
        "cms_pricer": "Underlying CMS coupon pricer.",
        "correlation": "Correlation quote handle.",
        "coupon_discount_curve": "Yield term structure handle for coupon discounting (optional).",
        "integration_points": "Number of integration points (default: 16).",
        "volatility_type": "Volatility type (optional, e.g., 'ShiftedLognormal').",
        "shift1": "First shift parameter (optional).",
        "shift2": "Second shift parameter (optional).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLognormalCmsSpreadPricer(
    cms_pricer: ql.CmsCouponPricer,
    correlation: qQuoteHandle,
    coupon_discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    integration_points: int = 16,
    volatility_type=None,
    shift1: float = ql.nullDouble(),
    shift2: float = ql.nullDouble(),
    trigger=None,
) -> ql.LognormalCmsSpreadPricer:

    if volatility_type is None:
        volatility_type_arg = ql.ShiftedLognormal
    else:
        volatility_type_arg = volatility_type

    return ql.LognormalCmsSpreadPricer(
        cms_pricer,
        correlation,
        coupon_discount_curve,
        integration_points,
        volatility_type_arg,
        shift1,
        shift2,
    )


# TODO to test
@xlo.func(
    help="Return swaplet price from a LognormalCmsSpreadPricer.",
    args={
        "pricer": "QuantLib LognormalCmsSpreadPricer.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLognormalCmsSpreadPricerSwapletPrice(
    pricer: ql.LognormalCmsSpreadPricer, trigger=None
) -> float:
    return pricer.swapletPrice()


@xlo.func(
    help="Return swaplet rate from a LognormalCmsSpreadPricer.",
    args={
        "pricer": "QuantLib LognormalCmsSpreadPricer.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLognormalCmsSpreadPricerSwapletRate(
    pricer: ql.LognormalCmsSpreadPricer, trigger=None
) -> float:
    return pricer.swapletRate()


@xlo.func(
    help="Return caplet price for a given effective cap from a LognormalCmsSpreadPricer.",
    args={
        "pricer": "QuantLib LognormalCmsSpreadPricer.",
        "effective_cap": "Effective cap rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLognormalCmsSpreadPricerCapletPrice(
    pricer: ql.LognormalCmsSpreadPricer, effective_cap: float, trigger=None
) -> float:
    return pricer.capletPrice(effective_cap)


@xlo.func(
    help="Return caplet rate for a given effective cap from a LognormalCmsSpreadPricer.",
    args={
        "pricer": "QuantLib LognormalCmsSpreadPricer.",
        "effective_cap": "Effective cap rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLognormalCmsSpreadPricerCapletRate(
    pricer: ql.LognormalCmsSpreadPricer, effective_cap: float, trigger=None
) -> float:
    return pricer.capletRate(effective_cap)


@xlo.func(
    help="Return floorlet price for a given effective floor from a LognormalCmsSpreadPricer.",
    args={
        "pricer": "QuantLib LognormalCmsSpreadPricer.",
        "effective_floor": "Effective floor rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLognormalCmsSpreadPricerFloorletPrice(
    pricer: ql.LognormalCmsSpreadPricer, effective_floor: float, trigger=None
) -> float:
    return pricer.floorletPrice(effective_floor)


@xlo.func(
    help="Return floorlet rate for a given effective floor from a LognormalCmsSpreadPricer.",
    args={
        "pricer": "QuantLib LognormalCmsSpreadPricer.",
        "effective_floor": "Effective floor rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLognormalCmsSpreadPricerFloorletRate(
    pricer: ql.LognormalCmsSpreadPricer, effective_floor: float, trigger=None
) -> float:
    return pricer.floorletRate(effective_floor)


# TODO to test
@xlo.func(
    help="Create a QuantLib EquityCashFlow object.",
    args={
        "notional": "Notional amount.",
        "index": "Equity index.",
        "base_date": "Base fixing date.",
        "fixing_date": "Current fixing date.",
        "payment_date": "Payment date.",
        "growth_only": "Whether to pay growth only (default: True).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityCashFlow(
    notional: float,
    index: ql.EquityIndex,
    base_date: qDate,
    fixing_date: qDate,
    payment_date: qDate,
    growth_only: bool = True,
    trigger=None,
) -> ql.EquityCashFlow:
    return ql.EquityCashFlow(
        notional, index, base_date, fixing_date, payment_date, growth_only
    )


@xlo.func(
    help="Set the pricer for an EquityCashFlow.",
    args={
        "cashflow": "QuantLib EquityCashFlow.",
        "pricer": "EquityCashFlowPricer.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityCashFlowSetPricer(
    cashflow: ql.EquityCashFlow,
    pricer: ql.EquityCashFlowPricer,
    trigger=None,
) -> bool:
    cashflow.setPricer(pricer)
    return True


@xlo.func(
    help="Set the equity cash flow pricer for a leg.",
    args={
        "leg": "Cash-flow leg.",
        "pricer": "EquityCashFlowPricer.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSetEquityCouponPricer(
    leg: xlo.Array(dims=1),
    pricer: ql.EquityCashFlowPricer,
    trigger=None,
) -> bool:
    ql.setCouponPricer(to_object_list(leg, ql.CashFlow), pricer)
    return True


@xlo.func(
    help="Create a QuantLib EquityQuantoCashFlowPricer.",
    args={
        "quanto_currency_term_structure": "Yield term structure handle for quanto currency.",
        "equity_volatility": "Black volatility term structure handle for equity.",
        "fx_volatility": "Black volatility term structure handle for FX.",
        "correlation": "Correlation quote handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityQuantoCashFlowPricer(
    quanto_currency_term_structure: ql.YieldTermStructureHandle,
    equity_volatility: ql.BlackVolTermStructureHandle,
    fx_volatility: ql.BlackVolTermStructureHandle,
    correlation: qQuoteHandle,
    trigger=None,
) -> ql.EquityQuantoCashFlowPricer:
    return ql.EquityQuantoCashFlowPricer(
        quanto_currency_term_structure,
        equity_volatility,
        fx_volatility,
        correlation,
    )


@xlo.func(
    help="Create a QuantLib RangeAccrualFloatersCoupon object.",
    args={
        "payment_date": "Payment date.",
        "nominal": "Nominal amount.",
        "index": "Ibor index.",
        "start_date": "Accrual start date.",
        "end_date": "Accrual end date.",
        "fixing_days": "Fixing days.",
        "day_counter": "Day count convention.",
        "gearing": "Coupon gearing.",
        "spread": "Coupon spread.",
        "ref_period_start": "Reference period start date.",
        "ref_period_end": "Reference period end date.",
        "observations_schedule": "Observations schedule.",
        "lower_trigger": "Lower trigger.",
        "upper_trigger": "Upper trigger.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRangeAccrualFloatersCoupon(
    payment_date: qDate,
    nominal: float,
    index: ql.IborIndex,
    start_date: qDate,
    end_date: qDate,
    fixing_days: int,
    day_counter: qDayCounter,
    gearing: float,
    spread: float,
    ref_period_start: qDate,
    ref_period_end: qDate,
    observations_schedule: ql.Schedule,
    lower_trigger: float,
    upper_trigger: float,
    trigger=None,
) -> ql.RangeAccrualFloatersCoupon:
    return ql.RangeAccrualFloatersCoupon(
        payment_date,
        nominal,
        index,
        start_date,
        end_date,
        fixing_days,
        day_counter,
        gearing,
        spread,
        ref_period_start,
        ref_period_end,
        observations_schedule,
        lower_trigger,
        upper_trigger,
    )


# TODO RangeAccrualPricerByBgm


@xlo.func(
    help="Set the floating-rate coupon pricer for a leg.",
    args={
        "leg": "Cash-flow leg.",
        "pricer": "Floating-rate coupon pricer.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSetCouponPricer(
    leg: xlo.Array(dims=1), pricer: ql.FloatingRateCouponPricer, trigger=None
) -> bool:
    ql.setCouponPricer(to_object_list(leg, ql.CashFlow), pricer)
    return True


@xlo.func(
    help="Build a fixed-rate leg.",
    args={
        "schedule": "Payment schedule.",
        "day_counter": "Day count convention.",
        "nominals": "Nominal amounts.",
        "coupon_rates": "Coupon rates.",
        "payment_adjustment": "Payment adjustment convention.",
        "first_period_day_count": "First period day count convention.",
        "ex_coupon_period": "Ex-coupon period.",
        "ex_coupon_calendar": "Ex-coupon calendar.",
        "ex_coupon_convention": "Ex-coupon convention.",
        "ex_coupon_end_of_month": "Ex-coupon end-of-month flag.",
        "payment_calendar": "Payment calendar.",
        "payment_lag": "Payment lag.",
        "compounding": "Compounding method.",
        "compounding_frequency": "Compounding frequency.",
        "interest_rates": "Interest rates for compounding.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedRateLeg(
    schedule: ql.Schedule,
    day_counter: qDayCounter,
    nominals: xlo.Array(dims=1),
    coupon_rates: xlo.Array(dims=1),
    payment_adjustment: qBusinessDayConvention = ql.Following,
    first_period_day_count=None,
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar=None,
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    payment_calendar=None,
    payment_lag: int = 0,
    compounding: qCompounding = ql.Simple,
    compounding_frequency: qFrequency = ql.Annual,
    interest_rates: xlo.Array(dims=1) = None,
    trigger=None,
):
    if first_period_day_count is not None:
        first_period_day_count = qDayCounter.__wrapped__(first_period_day_count)
    if ex_coupon_calendar is not None:
        ex_coupon_calendar = qCalendar.__wrapped__(ex_coupon_calendar)
    if payment_calendar is not None:
        payment_calendar = qCalendar.__wrapped__(payment_calendar)

    _KWARGS = {
        "payment_adjustment": "paymentAdjustment",
        "first_period_day_count": "firstPeriodDayCount",
        "ex_coupon_period": "exCouponPeriod",
        "ex_coupon_calendar": "exCouponCalendar",
        "ex_coupon_convention": "exCouponConvention",
        "ex_coupon_end_of_month": "exCouponEndOfMonth",
        "payment_calendar": "paymentCalendar",
        "payment_lag": "paymentLag",
        "compounding": "compounding",
        "compounding_frequency": "compoundingFrequency",
        "interest_rates": "interestRates",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.FixedRateLeg(
        schedule,
        day_counter,
        to_float_list(nominals),
        to_float_list(coupon_rates),
        **kwargs,
    )


@xlo.func(
    help="Build an Ibor leg.",
    args={
        "nominals": "Nominal amounts.",
        "schedule": "Payment schedule.",
        "index": "Ibor index.",
        "payment_day_counter": "Payment day count convention.",
        "payment_convention": "Payment convention.",
        "fixing_days": "Fixing-day sequence.",
        "gearings": "Coupon gearings.",
        "spreads": "Coupon spreads.",
        "caps": "Caps.",
        "floors": "Floors.",
        "is_in_arrears": "Whether coupons are in arrears.",
        "ex_coupon_period": "Ex-coupon period.",
        "ex_coupon_calendar": "Ex-coupon calendar.",
        "ex_coupon_convention": "Ex-coupon convention.",
        "ex_coupon_end_of_month": "Ex-coupon end-of-month flag.",
        "payment_calendar": "Payment calendar.",
        "payment_lag": "Payment lag.",
        "with_indexed_coupons": "Whether to use indexed coupons.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIborLeg(
    nominals: xlo.Array(dims=1),
    schedule: ql.Schedule,
    index: ql.IborIndex,
    payment_day_counter=None,
    payment_convention: qBusinessDayConvention = ql.Following,
    fixing_days=(),
    gearings: xlo.Array(dims=1) = None,
    spreads: xlo.Array(dims=1) = None,
    caps: xlo.Array(dims=1) = None,
    floors: xlo.Array(dims=1) = None,
    is_in_arrears: bool = False,
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar=None,
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    payment_calendar=None,
    payment_lag: int = 0,
    with_indexed_coupons: bool = False,
    trigger=None,
):
    if payment_day_counter is not None:
        payment_day_counter = qDayCounter.__wrapped__(payment_day_counter)
    if ex_coupon_calendar is not None:
        ex_coupon_calendar = qCalendar.__wrapped__(ex_coupon_calendar)
    if payment_calendar is not None:
        payment_calendar = qCalendar.__wrapped__(payment_calendar)
    gearings = to_float_list(gearings)
    spreads = to_float_list(spreads)
    caps = to_float_list(caps)
    floors = to_float_list(floors)
    fixing_days = to_int_list(fixing_days)

    _KWARGS = {
        "payment_day_counter": "paymentDayCounter",
        "payment_convention": "paymentConvention",
        "fixing_days": "fixingDays",
        "gearings": "gearings",
        "spreads": "spreads",
        "caps": "caps",
        "floors": "floors",
        "is_in_arrears": "isInArrears",
        "ex_coupon_period": "exCouponPeriod",
        "ex_coupon_calendar": "exCouponCalendar",
        "ex_coupon_convention": "exCouponConvention",
        "ex_coupon_end_of_month": "exCouponEndOfMonth",
        "payment_calendar": "paymentCalendar",
        "payment_lag": "paymentLag",
        "with_indexed_coupons": "withIndexedCoupons",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.IborLeg(
        to_float_list(nominals),
        schedule,
        index,
        **kwargs,
    )


@xlo.func(
    help="Build an overnight leg.",
    args={
        "nominals": "Nominal amounts.",
        "schedule": "Payment schedule.",
        "index": "Overnight index.",
        "payment_day_counter": "Payment day count convention.",
        "payment_convention": "Payment convention.",
        "gearings": "Coupon gearings.",
        "spreads": "Coupon spreads.",
        "telescopic_value_dates": "Use telescopic value dates.",
        "averaging_method": "Rate averaging method.",
        "payment_calendar": "Payment calendar.",
        "payment_lag": "Payment lag.",
        "lookback_days": "Lookback days.",
        "lockout_days": "Lockout days.",
        "apply_observation_shift": "Apply observation shift.",
        "compound_spread_daily": "Compound spread daily.",
        "caps": "Caps.",
        "floors": "Floors.",
        "daily_cap_floor": "Whether cap/floor is applied daily.",
        "in_arrears": "Whether coupons are in arrears.",
        "naked_option": "Whether to use naked option payoff.",
        "payment_dates": "Payment dates.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightLeg(
    nominals: xlo.Array(dims=1),
    schedule: ql.Schedule,
    index: ql.OvernightIndex,
    payment_day_counter=None,
    payment_convention: qBusinessDayConvention = ql.Following,
    gearings: xlo.Array(dims=1) = None,
    spreads: xlo.Array(dims=1) = None,
    telescopic_value_dates: bool = False,
    averaging_method: qRateAveragingType = ql.RateAveraging.Compound,
    payment_calendar=None,
    payment_lag: int = 0,
    lookback_days: int = ql.nullInt(),
    lockout_days: int = 0,
    apply_observation_shift: bool = False,
    compound_spread_daily: bool = False,
    caps: xlo.Array(dims=1) = None,
    floors: xlo.Array(dims=1) = None,
    daily_cap_floor: bool = False,
    in_arrears: bool = True,
    naked_option: bool = False,
    payment_dates: xlo.Array(dims=1) = None,
    trigger=None,
):
    if payment_day_counter is not None:
        payment_day_counter = qDayCounter.__wrapped__(payment_day_counter)
    if payment_calendar is not None:
        payment_calendar = qCalendar.__wrapped__(payment_calendar)
    gearings = to_float_list(gearings)
    spreads = to_float_list(spreads)
    caps = to_float_list(caps)
    floors = to_float_list(floors)
    if payment_dates is not None:
        payment_dates = _to_date_list(payment_dates)

    _KWARGS = {
        "payment_day_counter": "paymentDayCounter",
        "payment_convention": "paymentConvention",
        "gearings": "gearings",
        "spreads": "spreads",
        "telescopic_value_dates": "telescopicValueDates",
        "averaging_method": "averagingMethod",
        "payment_calendar": "paymentCalendar",
        "payment_lag": "paymentLag",
        "lookback_days": "lookbackDays",
        "lockout_days": "lockoutDays",
        "apply_observation_shift": "applyObservationShift",
        "compound_spread_daily": "compoundSpreadDaily",
        "caps": "caps",
        "floors": "floors",
        "daily_cap_floor": "dailyCapFloor",
        "in_arrears": "inArrears",
        "naked_option": "nakedOption",
        "payment_dates": "paymentDates",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.OvernightLeg(
        to_float_list(nominals),
        schedule,
        index,
        **kwargs,
    )


@xlo.func(
    help="Build a CMS leg.",
    args={
        "nominals": "Nominal amounts.",
        "schedule": "Payment schedule.",
        "index": "Swap index.",
        "payment_day_counter": "Payment day count convention.",
        "payment_convention": "Payment convention.",
        "fixing_days": "Fixing-day sequence.",
        "gearings": "Coupon gearings.",
        "spreads": "Coupon spreads.",
        "caps": "Caps.",
        "floors": "Floors.",
        "is_in_arrears": "Whether coupons are in arrears.",
        "ex_coupon_period": "Ex-coupon period.",
        "ex_coupon_calendar": "Ex-coupon calendar.",
        "ex_coupon_convention": "Ex-coupon convention.",
        "ex_coupon_end_of_month": "Ex-coupon end-of-month flag.",
        "fixing_convention": "Fixing convention.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCmsLeg(
    nominals: xlo.Array(dims=1),
    schedule: ql.Schedule,
    index: ql.SwapIndex,
    payment_day_counter=None,
    payment_convention: qBusinessDayConvention = ql.Following,
    fixing_days: xlo.Array(dims=1) = None,
    gearings: xlo.Array(dims=1) = None,
    spreads: xlo.Array(dims=1) = None,
    caps: xlo.Array(dims=1) = None,
    floors: xlo.Array(dims=1) = None,
    is_in_arrears: bool = False,
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar=None,
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    fixing_convention: qBusinessDayConvention = ql.Preceding,
    trigger=None,
):
    if payment_day_counter is not None:
        payment_day_counter = qDayCounter.__wrapped__(payment_day_counter)
    if ex_coupon_calendar is not None:
        ex_coupon_calendar = qCalendar.__wrapped__(ex_coupon_calendar)

    _KWARGS = {
        "payment_day_counter": "paymentDayCounter",
        "payment_convention": "paymentConvention",
        "fixing_days": "fixingDays",
        "gearings": "gearings",
        "spreads": "spreads",
        "caps": "caps",
        "floors": "floors",
        "is_in_arrears": "isInArrears",
        "ex_coupon_period": "exCouponPeriod",
        "ex_coupon_calendar": "exCouponCalendar",
        "ex_coupon_convention": "exCouponConvention",
        "ex_coupon_end_of_month": "exCouponEndOfMonth",
        "fixing_convention": "fixingConvention",
    }
    gearings = to_float_list(gearings)
    spreads = to_float_list(spreads)
    caps = to_float_list(caps)
    floors = to_float_list(floors)
    fixing_days = to_int_list(fixing_days)

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.CmsLeg(
        to_float_list(nominals),
        schedule,
        index,
        **kwargs,
    )


@xlo.func(
    help="Build a CMS zero leg.",
    args={
        "nominals": "Nominal amounts.",
        "schedule": "Payment schedule.",
        "index": "Swap index.",
        "payment_day_counter": "Payment day count convention.",
        "payment_convention": "Payment convention.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCmsZeroLeg(
    nominals: xlo.Array(dims=1),
    schedule: ql.Schedule,
    index: ql.SwapIndex,
    payment_day_counter=None,
    payment_convention: qBusinessDayConvention = ql.Following,
    fixing_days: xlo.Array(dims=1) = None,
    gearings: xlo.Array(dims=1) = None,
    spreads: xlo.Array(dims=1) = None,
    caps: xlo.Array(dims=1) = None,
    floors: xlo.Array(dims=1) = None,
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar: qCalendar = None,
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    trigger=None,
):
    if payment_day_counter is not None:
        payment_day_counter = qDayCounter.__wrapped__(payment_day_counter)
    if ex_coupon_calendar is not None:
        ex_coupon_calendar = qCalendar.__wrapped__(ex_coupon_calendar)

    _KWARGS = {
        "payment_day_counter": "paymentDayCounter",
        "payment_convention": "paymentConvention",
        "fixing_days": "fixingDays",
        "gearings": "gearings",
        "spreads": "spreads",
        "caps": "caps",
        "floors": "floors",
        "ex_coupon_period": "exCouponPeriod",
        "ex_coupon_calendar": "exCouponCalendar",
        "ex_coupon_convention": "exCouponConvention",
        "ex_coupon_end_of_month": "exCouponEndOfMonth",
    }
    gearings = to_float_list(gearings)
    spreads = to_float_list(spreads)
    caps = to_float_list(caps)
    floors = to_float_list(floors)
    fixing_days = to_int_list(fixing_days)

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.CmsZeroLeg(
        to_float_list(nominals),
        schedule,
        index,
        **kwargs,
    )


@xlo.func(
    help="Build a CMS spread leg.",
    args={
        "nominals": "Nominal amounts.",
        "schedule": "Payment schedule.",
        "index": "Swap spread index.",
        "payment_day_counter": "Payment day count convention.",
        "payment_convention": "Payment convention.",
        "fixing_days": "Fixing-day sequence.",
        "gearings": "Coupon gearings.",
        "spreads": "Coupon spreads.",
        "caps": "Caps.",
        "floors": "Floors.",
        "is_in_arrears": "Whether coupons are in arrears.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCmsSpreadLeg(
    nominals: xlo.Array(dims=1),
    schedule: ql.Schedule,
    index: ql.SwapSpreadIndex,
    payment_day_counter=None,
    payment_convention: qBusinessDayConvention = ql.Following,
    fixing_days: xlo.Array(dims=1) = None,
    gearings: xlo.Array(dims=1) = None,
    spreads: xlo.Array(dims=1) = None,
    caps: xlo.Array(dims=1) = None,
    floors: xlo.Array(dims=1) = None,
    is_in_arrears: bool = False,
    trigger=None,
):
    if payment_day_counter is not None:
        payment_day_counter = qDayCounter.__wrapped__(payment_day_counter)
    gearings = to_float_list(gearings)
    spreads = to_float_list(spreads)
    caps = to_float_list(caps)
    floors = to_float_list(floors)
    fixing_days = to_int_list(fixing_days)

    _KWARGS = {
        "payment_day_counter": "paymentDayCounter",
        "payment_convention": "paymentConvention",
        "fixing_days": "fixingDays",
        "gearings": "gearings",
        "spreads": "spreads",
        "caps": "caps",
        "floors": "floors",
        "is_in_arrears": "isInArrears",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.CmsSpreadLeg(
        to_float_list(nominals),
        schedule,
        index,
        **kwargs,
    )


@xlo.func(
    help="Build a multiple-resets leg.",
    args={
        "full_reset_schedule": "Full reset schedule.",
        "index": "Ibor index.",
        "resets_per_coupon": "Number of resets per coupon.",
        "nominals": "Nominal amounts.",
        "payment_day_counter": "Payment day count convention.",
        "payment_convention": "Payment convention.",
        "payment_calendar": "Payment calendar.",
        "payment_lag": "Payment lag.",
        "fixing_days": "Fixing-day sequence.",
        "gearings": "Coupon gearings.",
        "coupon_spreads": "Coupon spreads.",
        "rate_spreads": "Rate spreads.",
        "ex_coupon_period": "Ex-coupon period.",
        "ex_coupon_calendar": "Ex-coupon calendar.",
        "ex_coupon_convention": "Ex-coupon convention.",
        "ex_coupon_end_of_month": "Ex-coupon end-of-month flag.",
        "averaging_method": "Rate averaging method.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultipleResetsLeg(
    full_reset_schedule: ql.Schedule,
    index: ql.IborIndex,
    resets_per_coupon: int,
    nominals: xlo.Array(dims=1),
    payment_day_counter=None,
    payment_convention: qBusinessDayConvention = ql.Following,
    payment_calendar=None,
    payment_lag: int = 0,
    fixing_days: xlo.Array(dims=1) = None,
    gearings: xlo.Array(dims=1) = None,
    coupon_spreads: xlo.Array(dims=1) = None,
    rate_spreads: xlo.Array(dims=1) = None,
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar=None,
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    averaging_method: qRateAveragingType = ql.RateAveraging.Compound,
    trigger=None,
):
    if payment_day_counter is not None:
        payment_day_counter = qDayCounter.__wrapped__(payment_day_counter)
    if payment_calendar is not None:
        payment_calendar = qCalendar.__wrapped__(payment_calendar)
    if ex_coupon_calendar is not None:
        ex_coupon_calendar = qCalendar.__wrapped__(ex_coupon_calendar)
    gearings = to_float_list(gearings)
    coupon_spreads = to_float_list(coupon_spreads)
    rate_spreads = to_float_list(rate_spreads)
    fixing_days = to_int_list(fixing_days)

    _KWARGS = {
        "payment_day_counter": "paymentDayCounter",
        "payment_convention": "paymentConvention",
        "payment_calendar": "paymentCalendar",
        "payment_lag": "paymentLag",
        "fixing_days": "fixingDays",
        "gearings": "gearings",
        "coupon_spreads": "couponSpreads",
        "rate_spreads": "rateSpreads",
        "ex_coupon_period": "exCouponPeriod",
        "ex_coupon_calendar": "exCouponCalendar",
        "ex_coupon_convention": "exCouponConvention",
        "ex_coupon_end_of_month": "exCouponEndOfMonth",
        "averaging_method": "averagingMethod",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.MultipleResetsLeg(
        full_reset_schedule, index, resets_per_coupon, to_float_list(nominals), **kwargs
    )


@xlo.func(
    help="Build a range-accrual leg.",
    args={
        "nominals": "Nominal amounts.",
        "schedule": "Payment schedule.",
        "index": "Ibor index.",
        "payment_day_counter": "Payment day count convention.",
        "fixing_days": "Fixing-day sequence.",
        "gearings": "Coupon gearings.",
        "spreads": "Coupon spreads.",
        "lower_triggers": "Lower triggers.",
        "upper_triggers": "Upper triggers.",
        "observation_tenor": "Observation tenor.",
        "observation_convention": "Observation convention.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRangeAccrualLeg(
    nominals: xlo.Array(dims=1),
    schedule: ql.Schedule,
    index: ql.IborIndex,
    payment_day_counter=None,
    payment_convention: qBusinessDayConvention = ql.Following,
    fixing_days: xlo.Array(dims=1) = None,
    gearings: xlo.Array(dims=1) = None,
    spreads: xlo.Array(dims=1) = None,
    lower_triggers: xlo.Array(dims=1) = None,
    upper_triggers: xlo.Array(dims=1) = None,
    observation_tenor: qPeriod = ql.Period(),
    observation_convention: qBusinessDayConvention = ql.ModifiedFollowing,
    trigger=None,
):
    if payment_day_counter is not None:
        payment_day_counter = qDayCounter.__wrapped__(payment_day_counter)
    gearings = to_float_list(gearings)
    spreads = to_float_list(spreads)
    lower_triggers = to_float_list(lower_triggers)
    upper_triggers = to_float_list(upper_triggers)
    fixing_days = to_int_list(fixing_days)

    _KWARGS = {
        "payment_day_counter": "paymentDayCounter",
        "payment_convention": "paymentConvention",
        "fixing_days": "fixingDays",
        "gearings": "gearings",
        "spreads": "spreads",
        "lower_triggers": "lowerTriggers",
        "upper_triggers": "upperTriggers",
        "observation_tenor": "observationTenor",
        "observation_convention": "observationConvention",
    }

    kwargs = {}
    for param_name, kw_name in _KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.RangeAccrualLeg(
        to_float_list(nominals),
        schedule,
        index,
        **kwargs,
    )


@xlo.func(
    help="Return the start date of a leg.",
    args={
        "leg": "Cash-flow leg.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsStartDate(leg: xlo.Array(dims=1), trigger=None) -> ql.Date:
    return ql.CashFlows.startDate(to_object_list(leg, ql.CashFlow))


@xlo.func(
    help="Return the maturity date of a leg.",
    args={
        "leg": "Cash-flow leg.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsMaturityDate(leg: xlo.Array(dims=1), trigger=None) -> ql.Date:
    return ql.CashFlows.maturityDate(to_object_list(leg, ql.CashFlow))


@xlo.func(
    help="Return the previous cash-flow date.",
    args={
        "leg": "Cash-flow leg.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsPreviousCashFlowDate(
    leg: xlo.Array(dims=1),
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> ql.Date:
    return ql.CashFlows.previousCashFlowDate(
        to_object_list(leg, ql.CashFlow), include_settlement_date_flows, settlement_date
    )


@xlo.func(
    help="Return the next cash-flow date.",
    args={
        "leg": "Cash-flow leg.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNextCashFlowDate(
    leg: xlo.Array(dims=1),
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> ql.Date:
    return ql.CashFlows.nextCashFlowDate(
        to_object_list(leg, ql.CashFlow), include_settlement_date_flows, settlement_date
    )


@xlo.func(
    help="Return the previous cash-flow amount.",
    args={
        "leg": "Cash-flow leg.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsPreviousCashFlowAmount(
    leg: xlo.Array(dims=1),
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.previousCashFlowAmount(
        to_object_list(leg, ql.CashFlow), include_settlement_date_flows, settlement_date
    )


@xlo.func(
    help="Return the next cash-flow amount.",
    args={
        "leg": "Cash-flow leg.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNextCashFlowAmount(
    leg: xlo.Array(dims=1),
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.nextCashFlowAmount(
        to_object_list(leg, ql.CashFlow), include_settlement_date_flows, settlement_date
    )


@xlo.func(
    help="Return the accrual period of the next cash flow.",
    args={
        "leg": "Cash-flow leg.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsAccrualPeriod(
    leg: xlo.Array(dims=1),
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.accrualPeriod(
        to_object_list(leg, ql.CashFlow), include_settlement_date_flows, settlement_date
    )


@xlo.func(
    help="Return the accrual days of the next cash flow.",
    args={
        "leg": "Cash-flow leg.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsAccrualDays(
    leg: xlo.Array(dims=1),
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> int:
    return ql.CashFlows.accrualDays(
        to_object_list(leg, ql.CashFlow), include_settlement_date_flows, settlement_date
    )


@xlo.func(
    help="Return the accrued period at settlement.",
    args={
        "leg": "Cash-flow leg.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsAccruedPeriod(
    leg: xlo.Array(dims=1),
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.accruedPeriod(
        to_object_list(leg, ql.CashFlow), include_settlement_date_flows, settlement_date
    )


@xlo.func(
    help="Return the accrued days at settlement.",
    args={
        "leg": "Cash-flow leg.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsAccruedDays(
    leg: xlo.Array(dims=1),
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> int:
    return ql.CashFlows.accruedDays(
        to_object_list(leg, ql.CashFlow), include_settlement_date_flows, settlement_date
    )


@xlo.func(
    help="Return the accrued amount at settlement.",
    args={
        "leg": "Cash-flow leg.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsAccruedAmount(
    leg: xlo.Array(dims=1),
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.accruedAmount(
        to_object_list(leg, ql.CashFlow), include_settlement_date_flows, settlement_date
    )


@xlo.func(
    help="Return the previous cash-flow object.",
    args={
        "leg": "Cash-flow leg.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsPreviousCashFlow(
    leg: xlo.Array(dims=1),
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> ql.CashFlow:
    return ql.CashFlows.previousCashFlow(
        to_object_list(leg, ql.CashFlow), include_settlement_date_flows, settlement_date
    )


@xlo.func(
    help="Return the next cash-flow object.",
    args={
        "leg": "Cash-flow leg.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNextCashFlow(
    leg: xlo.Array(dims=1),
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> ql.CashFlow:
    return ql.CashFlows.nextCashFlow(
        to_object_list(leg, ql.CashFlow), include_settlement_date_flows, settlement_date
    )


@xlo.func(
    help="Return leg NPV.",
    args={
        "leg": "Cash-flow leg.",
        "discount_curve": "Discount curve handle.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
        "npv_date": "NPV date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNpv(
    leg: xlo.Array(dims=1),
    discount_curve: ql.YieldTermStructureHandle,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.npv(
        to_object_list(leg, ql.CashFlow),
        discount_curve,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Return leg NPV from an interest rate.",
    args={
        "leg": "Cash-flow leg.",
        "interest_rate": "Interest rate object.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
        "npv_date": "NPV date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNpvFromInterestRate(
    leg: xlo.Array(dims=1),
    interest_rate: ql.InterestRate,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.npv(
        to_object_list(leg, ql.CashFlow),
        interest_rate,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Return leg NPV from rate and compounding inputs.",
    args={
        "leg": "Cash-flow leg.",
        "_yield": "Yield.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
        "npv_date": "NPV date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNpvFromRate(
    leg: xlo.Array(dims=1),
    _yield: float,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.npv(
        to_object_list(leg, ql.CashFlow),
        _yield,
        day_counter,
        compounding,
        frequency,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Return leg NPV from discount curve and z-spread.",
    args={
        "leg": "Cash-flow leg.",
        "discount_curve": "Discount curve handle.",
        "z_spread": "Z-spread.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
        "npv_date": "NPV date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNpvFromZSpread(
    leg: xlo.Array(dims=1),
    discount_curve: ql.YieldTermStructureHandle,
    z_spread: float,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.npv(
        to_object_list(leg, ql.CashFlow),
        discount_curve.currentLink(),
        z_spread,
        day_counter,
        compounding,
        frequency,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Return leg BPS.",
    args={
        "leg": "Cash-flow leg.",
        "discount_curve": "Discount curve handle.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
        "npv_date": "NPV date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsBps(
    leg: xlo.Array(dims=1),
    discount_curve: ql.YieldTermStructureHandle,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.bps(
        to_object_list(leg, ql.CashFlow),
        discount_curve,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Return leg BPS from an interest rate.",
    args={
        "leg": "Cash-flow leg.",
        "interest_rate": "Interest rate object.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
        "npv_date": "NPV date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsBpsFromInterestRate(
    leg: xlo.Array(dims=1),
    interest_rate: ql.InterestRate,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.bps(
        to_object_list(leg, ql.CashFlow),
        interest_rate,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Return leg BPS from rate and compounding inputs.",
    args={
        "leg": "Cash-flow leg.",
        "_yield": "Yield.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
        "npv_date": "NPV date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsBpsFromRate(
    leg: xlo.Array(dims=1),
    _yield: float,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.bps(
        to_object_list(leg, ql.CashFlow),
        _yield,
        day_counter,
        compounding,
        frequency,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Return leg NPV and BPS.",
    args={
        "leg": "Cash-flow leg.",
        "discount_curve": "Discount curve handle.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
        "npv_date": "NPV date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNpvBps(
    leg: xlo.Array(dims=1),
    discount_curve: ql.YieldTermStructureHandle,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> tuple[float, float]:
    npv, bps = ql.CashFlows.npvbps(
        to_object_list(leg, ql.CashFlow),
        discount_curve,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )
    return float(npv), float(bps)


@xlo.func(
    help="Return leg ATM rate.",
    args={
        "leg": "Cash-flow leg.",
        "discount_curve": "Discount curve handle.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
        "npv_date": "NPV date.",
        "npv": "Optional target NPV.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsAtmRate(
    leg: xlo.Array(dims=1),
    discount_curve: ql.YieldTermStructureHandle,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    npv: float = ql.nullDouble(),
    trigger=None,
) -> float:
    return ql.CashFlows.atmRate(
        to_object_list(leg, ql.CashFlow),
        discount_curve.currentLink(),
        include_settlement_date_flows,
        settlement_date,
        npv_date,
        npv,
    )


@xlo.func(
    help="Return leg yield from an NPV.",
    args={
        "leg": "Cash-flow leg.",
        "npv": "Present value.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
        "npv_date": "NPV date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsYieldRate(
    leg: xlo.Array(dims=1),
    npv: float,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    accuracy: float = 1.0e-10,
    max_iterations: int = 10000,
    guess: float = 0.05,
    trigger=None,
) -> float:
    return ql.CashFlows.yieldRate(
        to_object_list(leg, ql.CashFlow),
        npv,
        day_counter,
        compounding,
        frequency,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
        accuracy,
        max_iterations,
        guess,
    )


@xlo.func(
    help="Return leg duration from an interest rate.",
    args={
        "leg": "Cash-flow leg.",
        "interest_rate": "Interest rate object.",
        "duration_type": "Duration type.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsDurationFromInterestRate(
    leg: xlo.Array(dims=1),
    interest_rate: ql.InterestRate,
    duration_type: qDurationType,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.duration(
        to_object_list(leg, ql.CashFlow),
        interest_rate,
        duration_type,
        include_settlement_date_flows,
        settlement_date,
    )


@xlo.func(
    help="Return leg duration from rate and compounding inputs.",
    args={
        "leg": "Cash-flow leg.",
        "_yield": "Yield.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "duration_type": "Duration type.",
        "include_settlement_date_flows": "Include settlement-date flows.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsDurationFromRate(
    leg: xlo.Array(dims=1),
    _yield: float,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    duration_type: qDurationType,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.duration(
        to_object_list(leg, ql.CashFlow),
        _yield,
        day_counter,
        compounding,
        frequency,
        duration_type,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Return leg convexity from rate and compounding inputs.",
    args={
        "leg": "Cash-flow leg.",
        "_yield": "Yield.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "include_settlement_date_flows": "Include settlement-date flows.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsConvexityFromRate(
    leg: xlo.Array(dims=1),
    _yield: float,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.convexity(
        to_object_list(leg, ql.CashFlow),
        _yield,
        day_counter,
        compounding,
        frequency,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Return leg convexity from an interest rate.",
    args={
        "leg": "Cash-flow leg.",
        "interest_rate": "Interest rate object.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
        "npv_date": "NPV date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsConvexityFromInterestRate(
    leg: xlo.Array(dims=1),
    interest_rate: ql.InterestRate,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.convexity(
        to_object_list(leg, ql.CashFlow),
        interest_rate,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Return leg basis-point value from rate and compounding inputs.",
    args={
        "leg": "Cash-flow leg.",
        "_yield": "Yield.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "include_settlement_date_flows": "Include settlement-date flows.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsBasisPointValueFromRate(
    leg: xlo.Array(dims=1),
    _yield: float,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.basisPointValue(
        to_object_list(leg, ql.CashFlow),
        _yield,
        day_counter,
        compounding,
        frequency,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Return leg basis-point value from an interest rate.",
    args={
        "leg": "Cash-flow leg.",
        "interest_rate": "Interest rate object.",
        "include_settlement_date_flows": "Include settlement-date flows.",
        "settlement_date": "Settlement date.",
        "npv_date": "NPV date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsBasisPointValueFromInterestRate(
    leg: xlo.Array(dims=1),
    interest_rate: ql.InterestRate,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.CashFlows.basisPointValue(
        to_object_list(leg, ql.CashFlow),
        interest_rate,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Return leg z-spread from NPV and discount curve.",
    args={
        "leg": "Cash-flow leg.",
        "npv": "Present value.",
        "discount_curve": "Discount curve.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "include_settlement_date_flows": "Include settlement-date flows.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCashFlowsZSpread(
    leg: xlo.Array(dims=1),
    npv: float,
    discount_curve: ql.YieldTermStructure,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    include_settlement_date_flows: bool,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    accuracy: float = 1.0e-10,
    max_iterations: int = 100,
    guess: float = 0.0,
    trigger=None,
) -> float:
    return ql.CashFlows.zSpread(
        to_object_list(leg, ql.CashFlow),
        npv,
        discount_curve,
        day_counter,
        compounding,
        frequency,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
        accuracy,
        max_iterations,
        guess,
    )


@xlo.func(
    help="Return duration type label.",
    args={
        "duration_type": "Duration type value.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDurationTypeName(duration_type: qDurationType, trigger=None) -> str:
    return first_key(QL_DURATION_TYPE, duration_type, UNKNOWN_VALUE)


@xlo.func(
    help="Return rate-averaging type label.",
    args={
        "averaging_type": "Rate averaging type value.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRateAveragingTypeName(averaging_type: qRateAveragingType, trigger=None) -> str:
    return first_key(QL_RATE_AVERAGING_TYPE, averaging_type, UNKNOWN_VALUE)
