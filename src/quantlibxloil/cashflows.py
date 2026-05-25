import numpy as np
import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .calendars import qBusinessDayConvention, qCalendar
from .date import qDate, qFrequency, qPeriod, _qDate
from .daycounters import qDayCounter
from .termstructures import qCompounding
from .utilities import enum_value, first_key, UNKNOWN_KEY, UNKNOWN_VALUE


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


def _to_float_list(values) -> list[float]:
    if values is None:
        return []
    if isinstance(values, (int, float)):
        return [float(values)]
    if isinstance(values, (list, tuple)):
        return [float(v) for v in values]
    if isinstance(values, np.ndarray):
        return values.astype(float).ravel().tolist()
    raise ValueError(f"Cannot convert {values} to list of floats.")

def _to_int_list(values) -> list[int]:
    if values is None:
        return []
    if isinstance(values, (int, float)):
        return [int(values)]
    if isinstance(values, (list, tuple)):
        return [int(v) for v in values]
    if isinstance(values, np.ndarray):
        return values.astype(int).ravel().tolist()
    raise ValueError(f"Cannot convert {values} to list of ints.")


def _to_date_list(values) -> list[ql.Date]:
	return [_qDate(v) for v in values]


def _to_ql_leg(cashflows) -> tuple[ql.CashFlow,...]:
    if cashflows is None:
        return ()
    if isinstance(cashflows, ql.CashFlow):
        return (cashflows,)
    if isinstance(cashflows, (list, tuple)):
        return tuple(cf for cf in cashflows)
    if isinstance(cashflows, np.ndarray):
        return tuple(cashflows.ravel().tolist())
    raise ValueError(f"Cannot convert {cashflows} to list of QuantLib CashFlows.")


def _qDurationType(duration_type: str) -> int:
	return enum_value(duration_type, QL_DURATION_TYPE)


def _qRateAveragingType(averaging_type: str) -> int:
	return enum_value(averaging_type, QL_RATE_AVERAGING_TYPE)


@xlo.converter()
def qDurationType(duration_type: str) -> int:
	return _qDurationType(duration_type)


@xlo.converter()
def qRateAveragingType(averaging_type: str) -> int:
	return _qRateAveragingType(averaging_type)


@xlo.func(
	help="Create a QuantLib SimpleCashFlow object.",
	args={
		"Amount": "Cash-flow amount.",
		"Date": "Payment date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlSimpleCashFlow(amount: float, date: qDate, Trigger=None) -> ql.SimpleCashFlow:
	return ql.SimpleCashFlow(amount, date)


@xlo.func(
	help="Create a QuantLib Redemption cash flow.",
	args={
		"Amount": "Cash-flow amount.",
		"Date": "Payment date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlRedemption(amount: float, date: qDate, Trigger=None) -> ql.Redemption:
	return ql.Redemption(amount, date)


@xlo.func(
	help="Create a QuantLib AmortizingPayment cash flow.",
	args={
		"Amount": "Cash-flow amount.",
		"Date": "Payment date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlAmortizingPayment(amount: float, date: qDate, Trigger=None) -> ql.AmortizingPayment:
	return ql.AmortizingPayment(amount, date)


@xlo.func(
	help="Create a QuantLib IndexedCashFlow object.",
	args={
		"Notional": "Notional amount.",
		"Index": "Index used for fixing.",
		"BaseDate": "Base fixing date.",
		"FixingDate": "Current fixing date.",
		"PaymentDate": "Payment date.",
		"GrowthOnly": "Whether to pay growth only.",
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
	Trigger=None,
) -> ql.IndexedCashFlow:
	return ql.IndexedCashFlow(notional, index, base_date, fixing_date, payment_date, growth_only)


@xlo.func(
	help="Return cash-flow amount.",
	args={
		"CashFlow": "QuantLib CashFlow.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowAmount(cashflow: ql.CashFlow, Trigger=None) -> float:
	return cashflow.amount()


@xlo.func(
	help="Return cash-flow payment date.",
	args={
		"CashFlow": "QuantLib CashFlow.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowDate(cashflow: ql.CashFlow, Trigger=None) -> qDate:
	return cashflow.date()


@xlo.func(
	help="Check whether the cash flow has occurred.",
	args={
		"CashFlow": "QuantLib CashFlow.",
		"RefDate": "Reference date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowHasOccurred(cashflow: ql.CashFlow, ref_date: qDate = ql.Date(), Trigger=None) -> bool:
	return cashflow.hasOccurred(ref_date)


@xlo.func(
	help="Cast a CashFlow to IndexedCashFlow if possible.",
	args={
		"CashFlow": "QuantLib CashFlow.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlAsIndexedCashFlow(cashflow: ql.CashFlow, Trigger=None) -> ql.IndexedCashFlow:
	return ql.as_indexed_cashflow(cashflow)


@xlo.func(
	help="Cast a CashFlow to Coupon if possible.",
	args={
		"CashFlow": "QuantLib CashFlow.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlAsCoupon(cashflow: ql.CashFlow, Trigger=None) -> ql.Coupon:
	return ql.as_coupon(cashflow)


@xlo.func(
	help="Return coupon nominal.",
	args={
		"Coupon": "QuantLib Coupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCouponNominal(coupon: ql.Coupon, Trigger=None) -> float:
	return coupon.nominal()


@xlo.func(
	help="Return coupon accrual start date.",
	args={
		"Coupon": "QuantLib Coupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCouponAccrualStartDate(coupon: ql.Coupon, Trigger=None) -> qDate:
	return coupon.accrualStartDate()


@xlo.func(
	help="Return coupon accrual end date.",
	args={
		"Coupon": "QuantLib Coupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCouponAccrualEndDate(coupon: ql.Coupon, Trigger=None) -> qDate:
	return coupon.accrualEndDate()


@xlo.func(
	help="Return coupon reference period start date.",
	args={
		"Coupon": "QuantLib Coupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCouponReferencePeriodStart(coupon: ql.Coupon, Trigger=None) -> qDate:
	return coupon.referencePeriodStart()


@xlo.func(
	help="Return coupon reference period end date.",
	args={
		"Coupon": "QuantLib Coupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCouponReferencePeriodEnd(coupon: ql.Coupon, Trigger=None) -> qDate:
	return coupon.referencePeriodEnd()


@xlo.func(
	help="Return coupon ex-coupon date.",
	args={
		"Coupon": "QuantLib Coupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCouponExCouponDate(coupon: ql.Coupon, Trigger=None) -> qDate:
	return coupon.exCouponDate()


@xlo.func(
	help="Return coupon rate.",
	args={
		"Coupon": "QuantLib Coupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCouponRate(coupon: ql.Coupon, Trigger=None) -> float:
	return coupon.rate()


@xlo.func(
	help="Return coupon accrual period.",
	args={
		"Coupon": "QuantLib Coupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCouponAccrualPeriod(coupon: ql.Coupon, Trigger=None) -> float:
	return coupon.accrualPeriod()


@xlo.func(
	help="Return coupon accrual days.",
	args={
		"Coupon": "QuantLib Coupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCouponAccrualDays(coupon: ql.Coupon, Trigger=None) -> int:
	return coupon.accrualDays()


@xlo.func(
	help="Return coupon day counter.",
	args={
		"Coupon": "QuantLib Coupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCouponDayCounter(coupon: ql.Coupon, Trigger=None) -> ql.DayCounter:
	return coupon.dayCounter()


@xlo.func(
	help="Return coupon accrued amount at a given date.",
	args={
		"Coupon": "QuantLib Coupon.",
		"Date": "Accrual date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCouponAccruedAmount(coupon: ql.Coupon, date: qDate, Trigger=None) -> float:
	return coupon.accruedAmount(date)


@xlo.func(
	help="Cast a CashFlow to FixedRateCoupon if possible.",
	args={
		"CashFlow": "QuantLib CashFlow.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlAsFixedRateCoupon(cashflow: ql.CashFlow, Trigger=None) -> ql.FixedRateCoupon:
	return ql.as_fixed_rate_coupon(cashflow)


@xlo.func(
	help="Cast a CashFlow to FloatingRateCoupon if possible.",
	args={
		"CashFlow": "QuantLib CashFlow.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlAsFloatingRateCoupon(cashflow: ql.CashFlow, Trigger=None) -> ql.FloatingRateCoupon:
	return ql.as_floating_rate_coupon(cashflow)


@xlo.func(
	help="Return floating-rate coupon fixing date.",
	args={
		"Coupon": "QuantLib FloatingRateCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponFixingDate(coupon: ql.FloatingRateCoupon, Trigger=None) -> qDate:
	return coupon.fixingDate()


@xlo.func(
	help="Return floating-rate coupon fixing days.",
	args={
		"Coupon": "QuantLib FloatingRateCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponFixingDays(coupon: ql.FloatingRateCoupon, Trigger=None) -> int:
	return coupon.fixingDays()


@xlo.func(
	help="Return whether the floating-rate coupon is in arrears.",
	args={
		"Coupon": "QuantLib FloatingRateCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponIsInArrears(coupon: ql.FloatingRateCoupon, Trigger=None) -> bool:
	return coupon.isInArrears()


@xlo.func(
	help="Return floating-rate coupon gearing.",
	args={
		"Coupon": "QuantLib FloatingRateCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponGearing(coupon: ql.FloatingRateCoupon, Trigger=None) -> float:
	return coupon.gearing()


@xlo.func(
	help="Return floating-rate coupon spread.",
	args={
		"Coupon": "QuantLib FloatingRateCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponSpread(coupon: ql.FloatingRateCoupon, Trigger=None) -> float:
	return coupon.spread()


@xlo.func(
	help="Return floating-rate coupon index fixing.",
	args={
		"Coupon": "QuantLib FloatingRateCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponIndexFixing(coupon: ql.FloatingRateCoupon, Trigger=None) -> float:
	return coupon.indexFixing()


@xlo.func(
	help="Return floating-rate coupon adjusted fixing.",
	args={
		"Coupon": "QuantLib FloatingRateCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponAdjustedFixing(coupon: ql.FloatingRateCoupon, Trigger=None) -> float:
	return coupon.adjustedFixing()


@xlo.func(
	help="Return floating-rate coupon convexity adjustment.",
	args={
		"Coupon": "QuantLib FloatingRateCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponConvexityAdjustment(coupon: ql.FloatingRateCoupon, Trigger=None) -> float:
	return coupon.convexityAdjustment()


@xlo.func(
	help="Return floating-rate coupon price from a discount curve handle.",
	args={
		"Coupon": "QuantLib FloatingRateCoupon.",
		"DiscountCurve": "Discount curve handle.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponPrice(
	coupon: ql.FloatingRateCoupon,
	discount_curve: ql.YieldTermStructureHandle,
	Trigger=None,
) -> float:
	return coupon.price(discount_curve)


@xlo.func(
	help="Return floating-rate coupon index.",
	args={
		"Coupon": "QuantLib FloatingRateCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponIndex(coupon: ql.FloatingRateCoupon, Trigger=None) -> ql.InterestRateIndex:
	return coupon.index()


@xlo.func(
	help="Set floating-rate coupon pricer.",
	args={
		"Coupon": "QuantLib FloatingRateCoupon.",
		"Pricer": "Floating-rate coupon pricer.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlFloatingRateCouponSetPricer(
	coupon: ql.FloatingRateCoupon,
	pricer: ql.FloatingRateCouponPricer,
	Trigger=None,
) -> bool:
	coupon.setPricer(pricer)
	return True


@xlo.func(
	help="Return whether the capped/floored coupon has a cap.",
	args={
		"Coupon": "QuantLib CappedFlooredCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCouponIsCapped(coupon: ql.CappedFlooredCoupon, Trigger=None) -> bool:
	return coupon.isCapped()


@xlo.func(
	help="Return whether the capped/floored coupon has a floor.",
	args={
		"Coupon": "QuantLib CappedFlooredCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCouponIsFloored(coupon: ql.CappedFlooredCoupon, Trigger=None) -> bool:
	return coupon.isFloored()


@xlo.func(
	help="Return capped/floored coupon cap.",
	args={
		"Coupon": "QuantLib CappedFlooredCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCouponCap(coupon: ql.CappedFlooredCoupon, Trigger=None) -> float:
	return coupon.cap()


@xlo.func(
	help="Return capped/floored coupon floor.",
	args={
		"Coupon": "QuantLib CappedFlooredCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCouponFloor(coupon: ql.CappedFlooredCoupon, Trigger=None) -> float:
	return coupon.floor()


@xlo.func(
	help="Return capped/floored coupon effective cap.",
	args={
		"Coupon": "QuantLib CappedFlooredCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCouponEffectiveCap(coupon: ql.CappedFlooredCoupon, Trigger=None) -> float:
	return coupon.effectiveCap()


@xlo.func(
	help="Return capped/floored coupon effective floor.",
	args={
		"Coupon": "QuantLib CappedFlooredCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredCouponEffectiveFloor(coupon: ql.CappedFlooredCoupon, Trigger=None) -> float:
	return coupon.effectiveFloor()


@xlo.func(
	help="Return overnight coupon averaging method.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponAveragingMethod(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> qRateAveragingType:
	return first_key(QL_RATE_AVERAGING_TYPE, coupon.averagingMethod(), UNKNOWN_KEY)


@xlo.func(
	help="Return whether telescopic formula can be applied.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponCanApplyTelescopicFormula(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> bool:
	return coupon.canApplyTelescopicFormula()


@xlo.func(
	help="Return whether observation shift is applied.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponApplyObservationShift(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> bool:
	return coupon.applyObservationShift()


@xlo.func(
	help="Return whether spread is compounded daily.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponCompoundSpreadDaily(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> bool:
	return coupon.compoundSpreadDaily()


@xlo.func(
	help="Return overnight coupon lockout days.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponLockoutDays(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> int:
	return coupon.lockoutDays()


@xlo.func(
	help="Return overnight coupon rate-computation start date.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponRateComputationStartDate(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> qDate:
	return coupon.rateComputationStartDate()


@xlo.func(
	help="Return overnight coupon rate-computation end date.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponRateComputationEndDate(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> qDate:
	return coupon.rateComputationEndDate()


@xlo.func(
	help="Return overnight coupon value dates.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponValueDates(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> tuple[ql.Date, ...]:
	return tuple(coupon.valueDates())


@xlo.func(
	help="Return overnight coupon fixing dates.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponFixingDates(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> tuple[ql.Date, ...]:
	return tuple(coupon.fixingDates())


@xlo.func(
	help="Return overnight coupon interest dates.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponInterestDates(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> tuple[ql.Date, ...]:
	return tuple(coupon.interestDates())


@xlo.func(
	help="Return overnight coupon day-fraction steps.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponDt(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> tuple[float, ...]:
	return tuple(coupon.dt())


@xlo.func(
	help="Return overnight coupon index fixings.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponIndexFixings(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> tuple[float, ...]:
	return tuple(coupon.indexFixings())


@xlo.func(
	help="Return overnight coupon effective index fixing.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponEffectiveIndexFixing(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> float:
	return coupon.effectiveIndexFixing()


@xlo.func(
	help="Return overnight coupon effective spread.",
	args={
		"Coupon": "QuantLib OvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedCouponEffectiveSpread(coupon: ql.OvernightIndexedCoupon, Trigger=None) -> float:
	return coupon.effectiveSpread()


@xlo.func(
	help="Return capped/floored overnight coupon underlying coupon.",
	args={
		"Coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponUnderlying(
	coupon: ql.CappedFlooredOvernightIndexedCoupon,
	Trigger=None,
) -> ql.OvernightIndexedCoupon:
	return coupon.underlying()


@xlo.func(
	help="Return whether capped/floored overnight coupon uses naked option payoff.",
	args={
		"Coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponNakedOption(
	coupon: ql.CappedFlooredOvernightIndexedCoupon,
	Trigger=None,
) -> bool:
	return coupon.nakedOption()


@xlo.func(
	help="Return whether cap/floor is applied daily for capped/floored overnight coupon.",
	args={
		"Coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponDailyCapFloor(
	coupon: ql.CappedFlooredOvernightIndexedCoupon,
	Trigger=None,
) -> bool:
	return coupon.dailyCapFloor()


@xlo.func(
	help="Return capped/floored overnight coupon averaging method label.",
	args={
		"Coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponAveragingMethod(
	coupon: ql.CappedFlooredOvernightIndexedCoupon,
	Trigger=None,
) -> str:
	return first_key(QL_RATE_AVERAGING_TYPE, coupon.averagingMethod(), UNKNOWN_KEY)


@xlo.func(
	help="Return whether spread is compounded daily for capped/floored overnight coupon.",
	args={
		"Coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponCompoundSpreadDaily(
	coupon: ql.CappedFlooredOvernightIndexedCoupon,
	Trigger=None,
) -> bool:
	return coupon.compoundSpreadDaily()


@xlo.func(
	help="Return capped/floored overnight coupon effective caplet volatility.",
	args={
		"Coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponEffectiveCapletVolatility(
	coupon: ql.CappedFlooredOvernightIndexedCoupon,
	Trigger=None,
) -> float:
	return coupon.effectiveCapletVolatility()


@xlo.func(
	help="Return capped/floored overnight coupon effective floorlet volatility.",
	args={
		"Coupon": "QuantLib CappedFlooredOvernightIndexedCoupon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCouponEffectiveFloorletVolatility(
	coupon: ql.CappedFlooredOvernightIndexedCoupon,
	Trigger=None,
) -> float:
	return coupon.effectiveFloorletVolatility()


@xlo.func(
	help="Cast a CashFlow to OvernightIndexedCoupon if possible.",
	args={
		"CashFlow": "QuantLib CashFlow.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlAsOvernightIndexedCoupon(cashflow: ql.CashFlow, Trigger=None) -> ql.OvernightIndexedCoupon:
	return ql.as_overnight_indexed_coupon(cashflow)


@xlo.func(
	help="Cast a CashFlow to CappedFlooredOvernightIndexedCoupon if possible.",
	args={
		"CashFlow": "QuantLib CashFlow.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlAsCappedFlooredOvernightIndexedCoupon(cashflow: ql.CashFlow, Trigger=None) -> ql.CappedFlooredOvernightIndexedCoupon:
	return ql.as_capped_floored_overnight_indexed_coupon(cashflow)


@xlo.func(
	help="Cast a CashFlow to SubPeriodsCoupon if possible.",
	args={
		"CashFlow": "QuantLib CashFlow.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlAsMultipleResetsCoupon(cashflow: ql.CashFlow, Trigger=None) -> ql.SubPeriodsCoupon:
	return ql.as_multiple_resets_coupon(cashflow)


@xlo.func(
	help="Create a QuantLib FixedRateCoupon object.",
	args={
		"PaymentDate": "Payment date.",
		"Nominal": "Nominal amount.",
		"Rate": "Coupon rate.",
		"DayCounter": "Day count convention.",
		"StartDate": "Accrual start date.",
		"EndDate": "Accrual end date.",
		"RefPeriodStart": "Reference period start date.",
		"RefPeriodEnd": "Reference period end date.",
		"ExCouponDate": "Ex-coupon date.",
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
	Trigger=None,
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
	help="Create a QuantLib IborCoupon object.",
	args={
		"PaymentDate": "Payment date.",
		"Nominal": "Nominal amount.",
		"StartDate": "Accrual start date.",
		"EndDate": "Accrual end date.",
		"FixingDays": "Fixing days.",
		"Index": "Ibor index.",
		"Gearing": "Coupon gearing.",
		"Spread": "Coupon spread.",
		"RefPeriodStart": "Reference period start date.",
		"RefPeriodEnd": "Reference period end date.",
		"DayCounter": "Day count convention.",
		"IsInArrears": "Whether fixing is in arrears.",
		"ExCouponDate": "Ex-coupon date.",
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
	day_counter: qDayCounter = ql.Actual365Fixed(),
	is_in_arrears: bool = False,
	ex_coupon_date: qDate = ql.Date(),
	Trigger=None,
) -> ql.IborCoupon:
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
		day_counter,
		is_in_arrears,
		ex_coupon_date,
	)
	cpn.setPricer(ql.BlackIborCouponPricer())
	return cpn


@xlo.func(
	help="Create a QuantLib CappedFlooredIborCoupon object.",
	args={
		"PaymentDate": "Payment date.",
		"Nominal": "Nominal amount.",
		"StartDate": "Accrual start date.",
		"EndDate": "Accrual end date.",
		"FixingDays": "Fixing days.",
		"Index": "Ibor index.",
		"Gearing": "Coupon gearing.",
		"Spread": "Coupon spread.",
		"Cap": "Cap rate.",
		"Floor": "Floor rate.",
		"RefPeriodStart": "Reference period start date.",
		"RefPeriodEnd": "Reference period end date.",
		"DayCounter": "Day count convention.",
		"IsInArrears": "Whether fixing is in arrears.",
		"ExCouponDate": "Ex-coupon date.",
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
	day_counter: qDayCounter = ql.Actual365Fixed(),
	is_in_arrears: bool = False,
	ex_coupon_date: qDate = ql.Date(),
	Trigger=None,
) -> ql.CappedFlooredIborCoupon:
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
		day_counter,
		is_in_arrears,
		ex_coupon_date,
	)


@xlo.func(
	help="Create a QuantLib OvernightIndexedCoupon object.",
	args={
		"PaymentDate": "Payment date.",
		"Nominal": "Nominal amount.",
		"StartDate": "Accrual start date.",
		"EndDate": "Accrual end date.",
		"OvernightIndex": "Overnight index.",
		"Gearing": "Coupon gearing.",
		"Spread": "Coupon spread.",
		"RefPeriodStart": "Reference period start date.",
		"RefPeriodEnd": "Reference period end date.",
		"DayCounter": "Day count convention.",
		"TelescopicValueDates": "Use telescopic dates.",
		"AveragingMethod": "Rate averaging method.",
		"LookbackDays": "Lookback days.",
		"LockoutDays": "Lockout days.",
		"ApplyObservationShift": "Apply observation shift.",
		"CompoundSpread": "Compound spread daily.",
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
	day_counter: qDayCounter = ql.Actual365Fixed(),
	telescopic_value_dates: bool = False,
	averaging_method: qRateAveragingType = ql.RateAveraging.Compound,
	lookback_days: int = ql.nullInt(),
	lockout_days: int = 0,
	apply_observation_shift: bool = False,
	compound_spread: bool = False,
	Trigger=None,
) -> ql.OvernightIndexedCoupon:
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
		day_counter,
		telescopic_value_dates,
		averaging_method,
		lookback_days,
		lockout_days,
		apply_observation_shift,
		compound_spread,
	)


@xlo.func(
	help="Create a QuantLib CappedFlooredOvernightIndexedCoupon object.",
	args={
		"Underlying": "Underlying overnight indexed coupon.",
		"Cap": "Cap rate.",
		"Floor": "Floor rate.",
		"NakedOption": "Whether to use naked option payoff.",
		"DailyCapFloor": "Whether cap/floor is applied daily.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredOvernightIndexedCoupon(
	underlying: ql.OvernightIndexedCoupon,
	cap: float = ql.nullDouble(),
	floor: float = ql.nullDouble(),
	naked_option: bool = False,
	daily_cap_floor: bool = False,
	Trigger=None,
) -> ql.CappedFlooredOvernightIndexedCoupon:
	return ql.CappedFlooredOvernightIndexedCoupon(underlying, cap, floor, naked_option, daily_cap_floor)


@xlo.func(
	help="Create a QuantLib CmsCoupon object.",
	args={
		"PaymentDate": "Payment date.",
		"Nominal": "Nominal amount.",
		"StartDate": "Accrual start date.",
		"EndDate": "Accrual end date.",
		"FixingDays": "Fixing days.",
		"Index": "Swap index.",
		"Gearing": "Coupon gearing.",
		"Spread": "Coupon spread.",
		"RefPeriodStart": "Reference period start date.",
		"RefPeriodEnd": "Reference period end date.",
		"DayCounter": "Day count convention.",
		"IsInArrears": "Whether fixing is in arrears.",
		"ExCouponDate": "Ex-coupon date.",
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
	day_counter: qDayCounter = ql.Actual365Fixed(),
	is_in_arrears: bool = False,
	ex_coupon_date: qDate = ql.Date(),
	Trigger=None,
) -> ql.CmsCoupon:
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
		day_counter,
		is_in_arrears,
		ex_coupon_date,
	)


@xlo.func(
	help="Create a QuantLib CmsSpreadCoupon object.",
	args={
		"PaymentDate": "Payment date.",
		"Nominal": "Nominal amount.",
		"StartDate": "Accrual start date.",
		"EndDate": "Accrual end date.",
		"FixingDays": "Fixing days.",
		"Index": "Swap spread index.",
		"Gearing": "Coupon gearing.",
		"Spread": "Coupon spread.",
		"RefPeriodStart": "Reference period start date.",
		"RefPeriodEnd": "Reference period end date.",
		"DayCounter": "Day count convention.",
		"IsInArrears": "Whether fixing is in arrears.",
		"ExCouponDate": "Ex-coupon date.",
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
	day_counter: qDayCounter = ql.Actual365Fixed(),
	is_in_arrears: bool = False,
	ex_coupon_date: qDate = ql.Date(),
	Trigger=None,
) -> ql.CmsSpreadCoupon:
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
		day_counter,
		is_in_arrears,
		ex_coupon_date,
	)


@xlo.func(
	help="Create a QuantLib RangeAccrualFloatersCoupon object.",
	args={
		"PaymentDate": "Payment date.",
		"Nominal": "Nominal amount.",
		"Index": "Ibor index.",
		"StartDate": "Accrual start date.",
		"EndDate": "Accrual end date.",
		"FixingDays": "Fixing days.",
		"DayCounter": "Day count convention.",
		"Gearing": "Coupon gearing.",
		"Spread": "Coupon spread.",
		"RefPeriodStart": "Reference period start date.",
		"RefPeriodEnd": "Reference period end date.",
		"ObservationsSchedule": "Observations schedule.",
		"LowerTrigger": "Lower trigger.",
		"UpperTrigger": "Upper trigger.",
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
	Trigger=None,
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


@xlo.func(
	help="Create a QuantLib MultipleResetsCoupon object.",
	args={
		"PaymentDate": "Payment date.",
		"Nominal": "Nominal amount.",
		"ResetSchedule": "Reset schedule.",
		"FixingDays": "Fixing days.",
		"Index": "Ibor index.",
		"Gearing": "Coupon gearing.",
		"CouponSpread": "Coupon spread.",
		"RateSpread": "Rate spread.",
		"RefPeriodStart": "Reference period start date.",
		"RefPeriodEnd": "Reference period end date.",
		"DayCounter": "Day count convention.",
		"ExCouponDate": "Ex-coupon date.",
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
	day_counter: qDayCounter = ql.Actual365Fixed(),
	ex_coupon_date: qDate = ql.Date(),
	Trigger=None,
) -> ql.MultipleResetsCoupon:
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
		day_counter,
		ex_coupon_date,
	)
	cpn.setPricer(ql.AveragingMultipleResetsPricer())
	return cpn


@xlo.func(
	help="Create a QuantLib BlackIborCouponPricer.",
	args={
		"Volatility": "Optionlet volatility handle.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlBlackIborCouponPricer(
	volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(),
	Trigger=None,
) -> ql.BlackIborCouponPricer:
	return ql.BlackIborCouponPricer(volatility)


@xlo.func(
	help="Create a QuantLib CompoundingOvernightIndexedCouponPricer.",
	group=EXCEL_GROUP_NAME,
)
def qlCompoundingOvernightIndexedCouponPricer(Trigger=None) -> ql.CompoundingOvernightIndexedCouponPricer:
	return ql.CompoundingOvernightIndexedCouponPricer()


@xlo.func(
	help="Create a QuantLib ArithmeticAveragedOvernightIndexedCouponPricer.",
	args={
		"MeanReversion": "Mean reversion parameter.",
		"Volatility": "Convexity-adjustment volatility.",
		"ByApprox": "Use approximation method.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlArithmeticAveragedOvernightIndexedCouponPricer(
	mean_reversion: float = 0.03,
	volatility: float = 0.0,
	by_approx: bool = False,
	Trigger=None,
) -> ql.ArithmeticAveragedOvernightIndexedCouponPricer:
	return ql.ArithmeticAveragedOvernightIndexedCouponPricer(mean_reversion, volatility, by_approx)


@xlo.func(
	help="Create a QuantLib BlackCompoundingOvernightIndexedCouponPricer.",
	args={
		"Volatility": "Optionlet volatility handle.",
		"EffectiveVolatilityInput": "Whether volatility input is effective volatility.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlBlackCompoundingOvernightIndexedCouponPricer(
	volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(),
	effective_volatility_input: bool = False,
	Trigger=None,
) -> ql.BlackCompoundingOvernightIndexedCouponPricer:
	return ql.BlackCompoundingOvernightIndexedCouponPricer(volatility, effective_volatility_input)


@xlo.func(
	help="Create a QuantLib BlackAveragingOvernightIndexedCouponPricer.",
	args={
		"Volatility": "Optionlet volatility handle.",
		"EffectiveVolatilityInput": "Whether volatility input is effective volatility.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlBlackAveragingOvernightIndexedCouponPricer(
	volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(),
	effective_volatility_input: bool = False,
	Trigger=None,
) -> ql.BlackAveragingOvernightIndexedCouponPricer:
	return ql.BlackAveragingOvernightIndexedCouponPricer(volatility, effective_volatility_input)


@xlo.func(
	help="Create a QuantLib CompoundingMultipleResetsPricer.",
	group=EXCEL_GROUP_NAME,
)
def qlCompoundingMultipleResetsPricer(Trigger=None) -> ql.CompoundingMultipleResetsPricer:
	return ql.CompoundingMultipleResetsPricer()


@xlo.func(
	help="Create a QuantLib AveragingMultipleResetsPricer.",
	group=EXCEL_GROUP_NAME,
)
def qlAveragingMultipleResetsPricer(Trigger=None) -> ql.AveragingMultipleResetsPricer:
	return ql.AveragingMultipleResetsPricer()


@xlo.func(
	help="Set the floating-rate coupon pricer for a leg.",
	args={
		"Leg": "Cash-flow leg.",
		"Pricer": "Floating-rate coupon pricer.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlSetCouponPricer(leg : xlo.Array(dims=1), pricer: ql.FloatingRateCouponPricer, Trigger=None) -> bool:
	ql.setCouponPricer(_to_ql_leg(leg), pricer)
	return True


@xlo.func(
	help="Build a fixed-rate leg.",
	args={
		"Schedule": "Payment schedule.",
		"DayCounter": "Day count convention.",
		"Nominals": "Nominal amounts.",
		"CouponRates": "Coupon rates.",
		"PaymentAdjustment": "Payment adjustment convention.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlFixedRateLeg(
	schedule: ql.Schedule,
	day_counter: qDayCounter,
	nominals,
	coupon_rates,
	payment_adjustment: qBusinessDayConvention = ql.Following,
	Trigger=None,
):
	return ql.FixedRateLeg(schedule, day_counter, _to_float_list(nominals), _to_float_list(coupon_rates), payment_adjustment)


@xlo.func(
	help="Build an Ibor leg.",
	args={
		"Nominals": "Nominal amounts.",
		"Schedule": "Payment schedule.",
		"Index": "Ibor index.",
		"PaymentDayCounter": "Payment day count convention.",
		"PaymentConvention": "Payment convention.",
		"FixingDays": "Fixing-day sequence.",
		"Gearings": "Coupon gearings.",
		"Spreads": "Coupon spreads.",
		"Caps": "Caps.",
		"Floors": "Floors.",
		"IsInArrears": "Whether coupons are in arrears.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlIborLeg(
	nominals,
	schedule: ql.Schedule,
	index: ql.IborIndex,
	payment_day_counter: qDayCounter = ql.Actual365Fixed(),
	payment_convention: qBusinessDayConvention = ql.Following,
	fixing_days=(),
	gearings=(),
	spreads=(),
	caps=(),
	floors=(),
	is_in_arrears: bool = False,
	Trigger=None,
):
	return ql.IborLeg(
		_to_float_list(nominals),
		schedule,
		index,
		payment_day_counter,
		payment_convention,
		_to_int_list(fixing_days),
		_to_float_list(gearings),
		_to_float_list(spreads),
		_to_float_list(caps),
		_to_float_list(floors),
		is_in_arrears,
	)


@xlo.func(
	help="Build an overnight leg.",
	args={
		"Nominals": "Nominal amounts.",
		"Schedule": "Payment schedule.",
		"Index": "Overnight index.",
		"PaymentDayCounter": "Payment day count convention.",
		"PaymentConvention": "Payment convention.",
		"Gearings": "Coupon gearings.",
		"Spreads": "Coupon spreads.",
		"TelescopicValueDates": "Use telescopic value dates.",
		"AveragingMethod": "Rate averaging method.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOvernightLeg(
	nominals,
	schedule: ql.Schedule,
	index: ql.OvernightIndex,
	payment_day_counter: qDayCounter = ql.Actual360(),
	payment_convention: qBusinessDayConvention = ql.Following,
	gearings=(),
	spreads=(),
	telescopic_value_dates: bool = False,
	averaging_method: qRateAveragingType = ql.RateAveraging.Compound,
	Trigger=None,
):
	return ql.OvernightLeg(
		_to_float_list(nominals),
		schedule,
		index,
		payment_day_counter,
		payment_convention,
		_to_float_list(gearings),
		_to_float_list(spreads),
		telescopic_value_dates,
		averaging_method,
	)


@xlo.func(
	help="Build a CMS leg.",
	args={
		"Nominals": "Nominal amounts.",
		"Schedule": "Payment schedule.",
		"Index": "Swap index.",
		"PaymentDayCounter": "Payment day count convention.",
		"PaymentConvention": "Payment convention.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCmsLeg(
	nominals,
	schedule: ql.Schedule,
	index: ql.SwapIndex,
	payment_day_counter: qDayCounter = ql.Actual365Fixed(),
	payment_convention: qBusinessDayConvention = ql.Following,
	Trigger=None,
):
	return ql.CmsLeg(_to_float_list(nominals), schedule, index, payment_day_counter, payment_convention)


@xlo.func(
	help="Build a CMS zero leg.",
	args={
		"Nominals": "Nominal amounts.",
		"Schedule": "Payment schedule.",
		"Index": "Swap index.",
		"PaymentDayCounter": "Payment day count convention.",
		"PaymentConvention": "Payment convention.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCmsZeroLeg(
	nominals,
	schedule: ql.Schedule,
	index: ql.SwapIndex,
	payment_day_counter: qDayCounter = ql.Actual365Fixed(),
	payment_convention: qBusinessDayConvention = ql.Following,
	Trigger=None,
):
	return ql.CmsZeroLeg(_to_float_list(nominals), schedule, index, payment_day_counter, payment_convention)


@xlo.func(
	help="Build a CMS spread leg.",
	args={
		"Nominals": "Nominal amounts.",
		"Schedule": "Payment schedule.",
		"Index": "Swap spread index.",
		"PaymentDayCounter": "Payment day count convention.",
		"PaymentConvention": "Payment convention.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCmsSpreadLeg(
	nominals,
	schedule: ql.Schedule,
	index: ql.SwapSpreadIndex,
	payment_day_counter: qDayCounter = ql.Actual365Fixed(),
	payment_convention: qBusinessDayConvention = ql.Following,
	Trigger=None,
):
	return ql.CmsSpreadLeg(_to_float_list(nominals), schedule, index, payment_day_counter, payment_convention)


@xlo.func(
	help="Build a multiple-resets leg.",
	args={
		"FullResetSchedule": "Full reset schedule.",
		"Index": "Ibor index.",
		"ResetsPerCoupon": "Number of resets per coupon.",
		"Nominals": "Nominal amounts.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlMultipleResetsLeg(
	full_reset_schedule: ql.Schedule,
	index: ql.IborIndex,
	resets_per_coupon: int,
	nominals,
	Trigger=None,
):
	return ql.MultipleResetsLeg(full_reset_schedule, index, resets_per_coupon, _to_float_list(nominals))


@xlo.func(
	help="Build a range-accrual leg.",
	args={
		"Nominals": "Nominal amounts.",
		"Schedule": "Payment schedule.",
		"Index": "Ibor index.",
		"PaymentDayCounter": "Payment day count convention.",
		"PaymentConvention": "Payment convention.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlRangeAccrualLeg(
	nominals,
	schedule: ql.Schedule,
	index: ql.IborIndex,
	payment_day_counter: qDayCounter = ql.Actual360(),
	payment_convention: qBusinessDayConvention = ql.Following,
	Trigger=None,
):
	return ql.RangeAccrualLeg(_to_float_list(nominals), schedule, index, payment_day_counter, payment_convention)


@xlo.func(
	help="Return the start date of a leg.",
	args={
		"Leg": "Cash-flow leg.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsStartDate(leg : xlo.Array(dims=1), Trigger=None) -> qDate:
	return ql.CashFlows.startDate(_to_ql_leg(leg))


@xlo.func(
	help="Return the maturity date of a leg.",
	args={
		"Leg": "Cash-flow leg.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsMaturityDate(leg : xlo.Array(dims=1), Trigger=None) -> qDate:
	return ql.CashFlows.maturityDate(_to_ql_leg(leg))


@xlo.func(
	help="Return the previous cash-flow date.",
	args={
		"Leg": "Cash-flow leg.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsPreviousCashFlowDate(
	leg : xlo.Array(dims=1),
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	Trigger=None,
) -> qDate:
	return ql.CashFlows.previousCashFlowDate(_to_ql_leg(leg), include_settlement_date_flows, settlement_date)


@xlo.func(
	help="Return the next cash-flow date.",
	args={
		"Leg": "Cash-flow leg.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNextCashFlowDate(
	leg : xlo.Array(dims=1),
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	Trigger=None,
) -> qDate:
	return ql.CashFlows.nextCashFlowDate(_to_ql_leg(leg), include_settlement_date_flows, settlement_date)


@xlo.func(
	help="Return the previous cash-flow amount.",
	args={
		"Leg": "Cash-flow leg.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsPreviousCashFlowAmount(
	leg : xlo.Array(dims=1),
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.previousCashFlowAmount(_to_ql_leg(leg), include_settlement_date_flows, settlement_date)


@xlo.func(
	help="Return the next cash-flow amount.",
	args={
		"Leg": "Cash-flow leg.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNextCashFlowAmount(
	leg : xlo.Array(dims=1),
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.nextCashFlowAmount(_to_ql_leg(leg), include_settlement_date_flows, settlement_date)


@xlo.func(
	help="Return the previous cash-flow object.",
	args={
		"Leg": "Cash-flow leg.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsPreviousCashFlow(
	leg : xlo.Array(dims=1),
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	Trigger=None,
) -> ql.CashFlow:
	return ql.CashFlows.previousCashFlow(_to_ql_leg(leg), include_settlement_date_flows, settlement_date)


@xlo.func(
	help="Return the next cash-flow object.",
	args={
		"Leg": "Cash-flow leg.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNextCashFlow(
	leg : xlo.Array(dims=1),
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	Trigger=None,
) -> ql.CashFlow:
	return ql.CashFlows.nextCashFlow(_to_ql_leg(leg), include_settlement_date_flows, settlement_date)


@xlo.func(
	help="Return the accrual period of the next cash flow.",
	args={
		"Leg": "Cash-flow leg.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsAccrualPeriod(
	leg : xlo.Array(dims=1),
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.accrualPeriod(_to_ql_leg(leg), include_settlement_date_flows, settlement_date)


@xlo.func(
	help="Return the accrual days of the next cash flow.",
	args={
		"Leg": "Cash-flow leg.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsAccrualDays(
	leg : xlo.Array(dims=1),
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	Trigger=None,
) -> int:
	return ql.CashFlows.accrualDays(_to_ql_leg(leg), include_settlement_date_flows, settlement_date)


@xlo.func(
	help="Return the accrued period at settlement.",
	args={
		"Leg": "Cash-flow leg.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsAccruedPeriod(
	leg : xlo.Array(dims=1),
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.accruedPeriod(_to_ql_leg(leg), include_settlement_date_flows, settlement_date)


@xlo.func(
	help="Return the accrued days at settlement.",
	args={
		"Leg": "Cash-flow leg.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsAccruedDays(
	leg : xlo.Array(dims=1),
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	Trigger=None,
) -> int:
	return ql.CashFlows.accruedDays(_to_ql_leg(leg), include_settlement_date_flows, settlement_date)


@xlo.func(
	help="Return the accrued amount at settlement.",
	args={
		"Leg": "Cash-flow leg.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsAccruedAmount(
	leg : xlo.Array(dims=1),
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.accruedAmount(_to_ql_leg(leg), include_settlement_date_flows, settlement_date)


@xlo.func(
	help="Return leg NPV.",
	args={
		"Leg": "Cash-flow leg.",
		"DiscountCurve": "Discount curve handle.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
		"NpvDate": "NPV date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNpv(
	leg : xlo.Array(dims=1),
	discount_curve: ql.YieldTermStructureHandle,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.npv(_to_ql_leg(leg), discount_curve, include_settlement_date_flows, settlement_date, npv_date)


@xlo.func(
	help="Return leg NPV from an interest rate.",
	args={
		"Leg": "Cash-flow leg.",
		"InterestRate": "Interest rate object.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
		"NpvDate": "NPV date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNpvFromInterestRate(
	leg : xlo.Array(dims=1),
	interest_rate: ql.InterestRate,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.npv(_to_ql_leg(leg), interest_rate, include_settlement_date_flows, settlement_date, npv_date)


@xlo.func(
	help="Return leg NPV from rate and compounding inputs.",
	args={
		"Leg": "Cash-flow leg.",
		"Yield": "Yield.",
		"DayCounter": "Day count convention.",
		"Compounding": "Compounding convention.",
		"Frequency": "Compounding frequency.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
		"NpvDate": "NPV date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNpvFromRate(
	leg : xlo.Array(dims=1),
	_yield: float,
	day_counter: qDayCounter,
	compounding: qCompounding,
	frequency: qFrequency,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.npv(
		_to_ql_leg(leg),
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
		"Leg": "Cash-flow leg.",
		"DiscountCurve": "Discount curve handle.",
		"ZSpread": "Z-spread.",
		"DayCounter": "Day count convention.",
		"Compounding": "Compounding convention.",
		"Frequency": "Compounding frequency.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
		"NpvDate": "NPV date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNpvFromZSpread(
	leg : xlo.Array(dims=1),
	discount_curve: ql.YieldTermStructureHandle,
	z_spread: float,
	day_counter: qDayCounter,
	compounding: qCompounding,
	frequency: qFrequency,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.npv(
		_to_ql_leg(leg),
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
		"Leg": "Cash-flow leg.",
		"DiscountCurve": "Discount curve handle.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
		"NpvDate": "NPV date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsBps(
	leg : xlo.Array(dims=1),
	discount_curve: ql.YieldTermStructureHandle,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.bps(_to_ql_leg(leg), discount_curve, include_settlement_date_flows, settlement_date, npv_date)

@xlo.func(
	help="Return leg BPS from an interest rate.",
	args={
		"Leg": "Cash-flow leg.",
		"InterestRate": "Interest rate object.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
		"NpvDate": "NPV date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsBpsFromInterestRate(
	leg : xlo.Array(dims=1),
	interest_rate: ql.InterestRate,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.bps(_to_ql_leg(leg), interest_rate, include_settlement_date_flows, settlement_date, npv_date)


@xlo.func(
	help="Return leg BPS from rate and compounding inputs.",
	args={
		"Leg": "Cash-flow leg.",
		"Yield": "Yield.",
		"DayCounter": "Day count convention.",
		"Compounding": "Compounding convention.",
		"Frequency": "Compounding frequency.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
		"NpvDate": "NPV date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsBpsFromRate(
	leg : xlo.Array(dims=1),
	_yield: float,
	day_counter: qDayCounter,
	compounding: qCompounding,
	frequency: qFrequency,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.bps(
		_to_ql_leg(leg),
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
		"Leg": "Cash-flow leg.",
		"DiscountCurve": "Discount curve handle.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
		"NpvDate": "NPV date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsNpvBps(
	leg : xlo.Array(dims=1),
	discount_curve: ql.YieldTermStructureHandle,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> tuple[float, float]:
	npv, bps = ql.CashFlows.npvbps(_to_ql_leg(leg), discount_curve, include_settlement_date_flows, settlement_date, npv_date)
	return float(npv), float(bps)


@xlo.func(
	help="Return leg ATM rate.",
	args={
		"Leg": "Cash-flow leg.",
		"DiscountCurve": "Discount curve handle.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
		"NpvDate": "NPV date.",
		"Npv": "Optional target NPV.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsAtmRate(
	leg : xlo.Array(dims=1),
	discount_curve: ql.YieldTermStructureHandle,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	npv: float = ql.nullDouble(),
	Trigger=None,
) -> float:
	return ql.CashFlows.atmRate(_to_ql_leg(leg), discount_curve.currentLink(), include_settlement_date_flows, settlement_date, npv_date, npv)


@xlo.func(
	help="Return leg yield from an NPV.",
	args={
		"Leg": "Cash-flow leg.",
		"Npv": "Present value.",
		"DayCounter": "Day count convention.",
		"Compounding": "Compounding convention.",
		"Frequency": "Compounding frequency.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
		"NpvDate": "NPV date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsYieldRate(
	leg : xlo.Array(dims=1),
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
	Trigger=None,
) -> float:
	return ql.CashFlows.yieldRate(
		_to_ql_leg(leg),
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
		"Leg": "Cash-flow leg.",
		"InterestRate": "Interest rate object.",
		"DurationType": "Duration type.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsDurationFromInterestRate(
	leg : xlo.Array(dims=1),
	interest_rate: ql.InterestRate,
	duration_type: qDurationType,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.duration(_to_ql_leg(leg), interest_rate, duration_type, include_settlement_date_flows, settlement_date)


@xlo.func(
	help="Return leg duration from rate and compounding inputs.",
	args={
		"Leg": "Cash-flow leg.",
		"Yield": "Yield.",
		"DayCounter": "Day count convention.",
		"Compounding": "Compounding convention.",
		"Frequency": "Compounding frequency.",
		"DurationType": "Duration type.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsDurationFromRate(
	leg : xlo.Array(dims=1),
	_yield: float,
	day_counter: qDayCounter,
	compounding: qCompounding,
	frequency: qFrequency,
	duration_type: qDurationType,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.duration(
		_to_ql_leg(leg),
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
		"Leg": "Cash-flow leg.",
		"Yield": "Yield.",
		"DayCounter": "Day count convention.",
		"Compounding": "Compounding convention.",
		"Frequency": "Compounding frequency.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsConvexityFromRate(
	leg : xlo.Array(dims=1),
	_yield: float,
	day_counter: qDayCounter,
	compounding: qCompounding,
	frequency: qFrequency,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.convexity(
		_to_ql_leg(leg),
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
		"Leg": "Cash-flow leg.",
		"InterestRate": "Interest rate object.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
		"NpvDate": "NPV date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsConvexityFromInterestRate(
	leg : xlo.Array(dims=1),
	interest_rate: ql.InterestRate,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.convexity(_to_ql_leg(leg), interest_rate, include_settlement_date_flows, settlement_date, npv_date)


@xlo.func(
	help="Return leg basis-point value from rate and compounding inputs.",
	args={
		"Leg": "Cash-flow leg.",
		"Yield": "Yield.",
		"DayCounter": "Day count convention.",
		"Compounding": "Compounding convention.",
		"Frequency": "Compounding frequency.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsBasisPointValueFromRate(
	leg : xlo.Array(dims=1),
	_yield: float,
	day_counter: qDayCounter,
	compounding: qCompounding,
	frequency: qFrequency,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.basisPointValue(
		_to_ql_leg(leg),
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
		"Leg": "Cash-flow leg.",
		"InterestRate": "Interest rate object.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
		"SettlementDate": "Settlement date.",
		"NpvDate": "NPV date.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsBasisPointValueFromInterestRate(
	leg : xlo.Array(dims=1),
	interest_rate: ql.InterestRate,
	include_settlement_date_flows: bool,
	settlement_date: qDate = ql.Date(),
	npv_date: qDate = ql.Date(),
	Trigger=None,
) -> float:
	return ql.CashFlows.basisPointValue(_to_ql_leg(leg), interest_rate, include_settlement_date_flows, settlement_date, npv_date)


@xlo.func(
	help="Return leg z-spread from NPV and discount curve.",
	args={
		"Leg": "Cash-flow leg.",
		"Npv": "Present value.",
		"DiscountCurve": "Discount curve.",
		"DayCounter": "Day count convention.",
		"Compounding": "Compounding convention.",
		"Frequency": "Compounding frequency.",
		"IncludeSettlementDateFlows": "Include settlement-date flows.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlCashFlowsZSpread(
	leg : xlo.Array(dims=1),
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
	Trigger=None,
) -> float:
	return ql.CashFlows.zSpread(
		_to_ql_leg(leg),
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
		"DurationType": "Duration type value.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlDurationTypeName(duration_type: qDurationType, Trigger=None) -> str:
	return first_key(QL_DURATION_TYPE, duration_type, UNKNOWN_VALUE)


@xlo.func(
	help="Return rate-averaging type label.",
	args={
		"RateAveragingType": "Rate averaging type value.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlRateAveragingTypeName(averaging_type: qRateAveragingType, Trigger=None) -> str:
	return first_key(QL_RATE_AVERAGING_TYPE, averaging_type, UNKNOWN_VALUE)
