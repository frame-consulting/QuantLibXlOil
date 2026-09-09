import QuantLib as ql
import xloil as xlo

from .calendars import qBusinessDayConvention, qCalendar
from .config import EXCEL_GROUP_NAME
from .date import qDate, qFrequency, qPeriod
from .daycounters import qDayCounter
from .inflation import qCPIInterpolationType
from .ratehelpers import qQuoteHandle
from .termstructures import qCompounding
from .utilities import (
    enum_value,
    first_key,
    to_float_list,
    to_object_list,
)

QL_BOND_PRICE_TYPE = {
    "CLEAN": ql.BondPrice.Dirty,
    "DIRTY": ql.BondPrice.Clean,
}

QL_CALLABILITY_TYPE = {
    "CALL": ql.Callability.Call,
    "PUT": ql.Callability.Put,
}


def _qBondPriceType(bond_price_type: str) -> ql.BondPrice.Type:
    return enum_value(bond_price_type, QL_BOND_PRICE_TYPE)


def _qCallabilityType(callability_type: str) -> ql.Callability.Type:
    return enum_value(callability_type, QL_CALLABILITY_TYPE)


@xlo.converter()
def qBondPriceType(bond_price_type: str) -> ql.BondPrice.Type:
    return _qBondPriceType(bond_price_type)


@xlo.converter()
def qCallabilityType(callability_type: str) -> ql.Callability.Type:
    return _qCallabilityType(callability_type)


@xlo.func(
    help="Create a QuantLib BondPrice object from an amount and price type.",
    args={
        "amount": "The bond price amount.",
        "price_type": 'The bond price type (e.g., "CLEAN" or "DIRTY").',
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondPrice(
    amount: float, price_type: qBondPriceType, trigger=None
) -> ql.BondPrice:
    return ql.BondPrice(amount, price_type)


@xlo.func(
    help="Create a QuantLib Callability object from a bond price, callability type, and date.",
    args={
        "price": "The bond price.",
        "callability_type": 'The callability type (e.g., "CALL" or "PUT").',
        "date": "The date of the callability.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCallability(
    price: ql.BondPrice, callability_type: qCallabilityType, date: qDate, trigger=None
) -> ql.Callability:
    return ql.Callability(price, callability_type, date)


@xlo.func(
    help="Create a QuantLib SoftCallability object from a bond price, date, and trigger value.",
    args={
        "price": "The bond price.",
        "date": "The date of the callability.",
        "trigger_callability": "The trigger value for soft callability (e.g., yield threshold).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSoftCallability(
    price: ql.BondPrice,
    date: qDate,
    trigger_callability: float,
    trigger=None,
) -> ql.SoftCallability:
    return ql.SoftCallability(price, date, trigger_callability)


@xlo.func(
    help="Convert a bond price type to its corresponding amount.",
    args={
        "price_type": 'The bond price type (e.g., "CLEAN" or "DIRTY").',
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondPriceAmount(bond_price: ql.BondPrice, trigger=None) -> float:
    return bond_price.amount()


@xlo.func(
    help="Get the type of a bond price.",
    args={
        "price_type": "The bond price object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondPriceType(bond_price: ql.BondPrice, trigger=None) -> str:
    return first_key(QL_BOND_PRICE_TYPE, bond_price.type())


@xlo.func(
    help="Check if a bond price type is valid.",
    args={
        "price_type": 'The bond price type (e.g., "CLEAN" or "DIRTY").',
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondPriceIsValid(bond_price: ql.BondPrice, trigger=None) -> bool:
    return bond_price.isValid()


@xlo.func(
    help="Get the price of a callability.",
    args={
        "callability": "The callability object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCallabilityPrice(callability: ql.Callability, trigger=None) -> ql.BondPrice:
    return callability.price()


@xlo.func(
    help="Get the type of a callability.",
    args={
        "callability": "The callability object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCallabilityType(callability: ql.Callability, trigger=None) -> str:
    return first_key(QL_CALLABILITY_TYPE, callability.type())


@xlo.func(
    help="Get the date of a callability.",
    args={
        "callability": "The callability object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCallabilityDate(callability: ql.Callability, trigger=None) -> ql.Date:
    return callability.date()


@xlo.func(
    help="Create a QuantLib Bond object with specified settlement days, calendar, and cashflows.",
    args={
        "settlement_days": "The number of settlement days after the trade date.",
        "calendar": "The calendar for business day conventions.",
        "face_amount": "The face amount (principal) of the bond.",
        "maturity_date": "The maturity date of the bond.",
        "issue_date": "The issue date of the bond (default: today).",
        "cashflows": "The leg containing the bond's cashflows (default: empty leg).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBond(
    settlement_days: int,
    calendar: qCalendar,
    face_amount: float,
    maturity_date: qDate,
    cashflows: ql.Leg,
    issue_date: qDate = ql.Date(),
    trigger=None,
) -> ql.Bond:
    return ql.Bond(
        settlement_days,
        calendar,
        face_amount,
        maturity_date,
        issue_date,
        to_object_list(cashflows, ql.CashFlow),
    )


@xlo.func(
    help="Create a QuantLib Bond object with specified settlement days, calendar, and coupons.",
    args={
        "settlement_days": "The number of settlement days after the trade date.",
        "calendar": "The calendar for business day conventions.",
        "issue_date": "The issue date of the bond (default: today).",
        "coupons": "The leg containing the bond's coupon cashflows (default: empty leg).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBond2(
    settlement_days: int,
    calendar: qCalendar,
    issue_date: qDate = ql.Date(),
    coupons=ql.Leg(),
    trigger=None,
) -> ql.Bond:
    return ql.Bond(settlement_days, calendar, issue_date, coupons)


@xlo.func(
    help="Get the next coupon rate of a bond as of a given date.",
    args={
        "bond": "The bond object.",
        "date": "The reference date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondNextCouponRate(bond: ql.Bond, date: qDate = ql.Date(), trigger=None) -> float:
    return bond.nextCouponRate(date)


@xlo.func(
    help="Get the previous coupon rate of a bond as of a given date.",
    args={
        "bond": "The bond object.",
        "date": "The reference date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondPreviousCouponRate(
    bond: ql.Bond, date: qDate = ql.Date(), trigger=None
) -> float:
    return bond.previousCouponRate(date)


@xlo.func(
    help="Get the next cash flow date of a bond as of a given date.",
    args={
        "bond": "The bond object.",
        "date": "The reference date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondNextCashFlowDate(
    bond: ql.Bond, date: qDate = ql.Date(), trigger=None
) -> ql.Date:
    return bond.nextCashFlowDate(date)


@xlo.func(
    help="Get the previous cash flow date of a bond as of a given date.",
    args={
        "bond": "The bond object.",
        "date": "The reference date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondPreviousCashFlowDate(
    bond: ql.Bond, date: qDate = ql.Date(), trigger=None
) -> ql.Date:
    return bond.previousCashFlowDate(date)


@xlo.func(
    help="Get the number of settlement days of a bond.",
    args={
        "bond": "The bond object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondSettlementDays(bond: ql.Bond, trigger=None) -> int:
    return bond.settlementDays()


@xlo.func(
    help="Get the settlement date of a bond for a given trade date.",
    args={
        "bond": "The bond object.",
        "date": "The trade date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondSettlementDate(
    bond: ql.Bond, date: qDate = ql.Date(), trigger=None
) -> ql.Date:
    return bond.settlementDate(date)


@xlo.func(
    help="Check if a bond is tradable as of a given date.",
    args={
        "bond": "The bond object.",
        "date": "The reference date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondIsTradable(bond: ql.Bond, date: qDate = ql.Date(), trigger=None) -> bool:
    return bond.isTradable(date)


@xlo.func(
    help="Get the start date (issue or accrual start date) of a bond.",
    args={
        "bond": "The bond object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondStartDate(bond: ql.Bond, trigger=None) -> ql.Date:
    return bond.startDate()


@xlo.func(
    help="Get the maturity date of a bond.",
    args={
        "bond": "The bond object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondMaturityDate(bond: ql.Bond, trigger=None) -> ql.Date:
    return bond.maturityDate()


@xlo.func(
    help="Get the issue date of a bond.",
    args={
        "bond": "The bond object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondIssueDate(bond: ql.Bond, trigger=None) -> ql.Date:
    return bond.issueDate()


@xlo.func(
    help="Get the cash flows of a bond.",
    args={
        "bond": "The bond object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondCashFlows(bond: ql.Bond, trigger=None):
    return bond.cashflows()


@xlo.func(
    help="Get the redemption amount of a bond.",
    args={
        "bond": "The bond object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondRedemption(bond: ql.Bond, trigger=None) -> ql.CashFlow:
    return bond.redemption()


@xlo.func(
    help="Get the redemption amounts of a bond.",
    args={
        "bond": "The bond object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondRedemptions(bond: ql.Bond, trigger=None):
    return bond.redemptions()


@xlo.func(
    help="Get the calendar of a bond.",
    args={
        "bond": "The bond object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondCalendar(bond: ql.Bond, trigger=None) -> ql.Calendar:
    return bond.calendar()


@xlo.func(
    help="Get the notional values of a bond.",
    args={
        "bond": "The bond object.",
        "date": "The reference date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondNotionals(bond: ql.Bond, trigger=None):
    return bond.notionals()


@xlo.func(
    help="Get the notional value of a bond at a specific date.",
    args={
        "bond": "The bond object.",
        "date": "The settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondNotional(bond: ql.Bond, date: qDate = ql.Date(), trigger=None) -> float:
    return bond.notional(date)


@xlo.func(
    help="Get the clean price of a bond.",
    args={
        "bond": "The bond object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondCleanPrice(bond: ql.Bond, trigger=None) -> float:
    return bond.cleanPrice()


@xlo.func(
    help="Get the clean price of a bond with detailed parameters.",
    args={
        "bond": "The bond object.",
        "yield_": "The yield as a quote handle.",
        "dc": "The day counter.",
        "compounding": "The compounding convention.",
        "frequency": "The compounding frequency.",
        "settlement": "The settlement date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondCleanPrice2(
    bond: ql.Bond,
    yield_: float,
    dc: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency = ql.Annual,
    settlement: qDate = ql.Date(),
    trigger=None,
) -> float:
    return bond.cleanPrice(yield_, dc, compounding, frequency)


@xlo.func(
    help="Get the dirty price of a bond.",
    args={
        "bond": "The bond object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondDirtyPrice(bond: ql.Bond, trigger=None) -> float:
    return bond.dirtyPrice()


@xlo.func(
    help="Get the dirty price of a bond with detailed parameters.",
    args={
        "bond": "The bond object.",
        "yield_": "The yield as a quote handle.",
        "dc": "The day counter.",
        "compounding": "The compounding convention.",
        "frequency": "The compounding frequency.",
        "settlement": "The settlement date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondDirtyPrice2(
    bond: ql.Bond,
    yield_: float,
    dc: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    settlement: qDate = ql.Date(),
    trigger=None,
) -> float:
    return bond.dirtyPrice(yield_, dc, compounding, frequency, settlement)


@xlo.func(
    help="Calculate the yield of a bond.",
    args={
        "bond": "The bond object.",
        "dc": "The day counter.",
        "compounding": "The compounding convention.",
        "freq": "The compounding frequency.",
        "accuracy": "Accuracy for yield calculation (default: 1e-8).",
        "max_evaluations": "Maximum iterations for yield calculation (default: 100).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondYield(
    bond: ql.Bond,
    dc: qDayCounter,
    compounding: qCompounding,
    freq: qFrequency,
    accuracy: float = 1.0e-8,
    max_evaluations: int = 100,
    trigger=None,
) -> float:
    return bond.bondYield(dc, compounding, freq, accuracy, max_evaluations)


@xlo.func(
    help="Calculate the yield of a bond given its price.",
    args={
        "bond": "The bond object.",
        "price": "The bond price.",
        "dc": "The day counter.",
        "compounding": "The compounding convention.",
        "freq": "The compounding frequency.",
        "settlement": "The settlement date (default: today).",
        "accuracy": "Accuracy for yield calculation (default: 1e-8).",
        "max_evaluations": "Maximum iterations for yield calculation (default: 100).",
        "guess": "Initial guess for yield (default: 0.05).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondYield2(
    bond: ql.Bond,
    price: ql.BondPrice,
    dc: qDayCounter,
    compounding: qCompounding,
    freq: qFrequency,
    settlement: qDate = ql.Date(),
    accuracy: float = 1.0e-8,
    max_evaluations: int = 100,
    guess: float = 0.05,
    trigger=None,
) -> float:
    return bond.bondYield(
        price, dc, compounding, freq, settlement, accuracy, max_evaluations, guess
    )


@xlo.func(
    help="Get the accrued amount of a bond.",
    args={
        "bond": "The bond object.",
        "settlement": "The settlement date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondAccruedAmount(
    bond: ql.Bond, settlement: qDate = ql.Date(), trigger=None
) -> float:
    return bond.accruedAmount(settlement)


@xlo.func(
    help="Get the settlement value of a bond.",
    args={
        "bond": "The bond object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondSettlementValue(bond: ql.Bond, trigger=None) -> float:
    return bond.settlementValue()


@xlo.func(
    help="Get the settlement value of a bond with a clean price.",
    args={
        "bond": "The bond object.",
        "clean_price": "The clean price of the bond.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondSettlementValue2(bond: ql.Bond, clean_price: float, trigger=None) -> float:
    return bond.settlementValue(clean_price)


@xlo.func(
    help="Calculate the clean price of a bond given a Z-spread.",
    args={
        "bond": "The bond object.",
        "discount_curve": "The discount curve (yield term structure handle).",
        "z_spread": "The Z-spread in decimal form (e.g., 0.01 for 1%).",
        "dc": "The day counter.",
        "compounding": "The compounding convention.",
        "freq": "The compounding frequency.",
        "settlement_date": "The settlement date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondCleanPriceFromZSpread(
    bond: ql.Bond,
    discount_curve: ql.YieldTermStructureHandle,
    z_spread: float,
    dc: qDayCounter,
    compounding: qCompounding,
    freq: qFrequency,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.cleanPriceFromZSpread(
        bond,
        discount_curve.currentLink(),
        z_spread,
        dc,
        compounding,
        freq,
        settlement_date,
    )


@xlo.func(
    help="Calculate the sinking schedule for a bond with periodic amortization.",
    args={
        "start_date": "The start date of the bond.",
        "bond_length": "The total length of the bond (e.g., '10Y' for 10 years).",
        "frequency": "The amortization frequency (e.g., 'Annual', 'Semiannual').",
        "payment_calendar": "The calendar for payment date adjustments (e.g., 'TARGET').",
        "trigger": "Optional trigger parameter (default: None).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondSinkingSchedule(
    start_date: qDate,
    bond_length: qPeriod,
    frequency: qFrequency,
    payment_calendar: qCalendar,
    trigger=None,
) -> ql.Schedule:
    return ql.sinkingSchedule(start_date, bond_length, frequency, payment_calendar)


@xlo.func(
    help="Calculate the notional amortization amounts for a sinking fund bond.",
    args={
        "bond_length": "The total length of the bond (e.g., '10Y' for 10 years).",
        "frequency": "The amortization frequency (e.g., 'Annual', 'Semiannual').",
        "coupon_rate": "The coupon rate in decimal form (e.g., 0.05 for 5%).",
        "initial_notional": "The initial notional amount (principal).",
        "trigger": "Optional trigger parameter (default: None).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondSinkingNotionals(
    bond_length: qPeriod,
    frequency: qFrequency,
    coupon_rate: float,
    initial_notional: float,
    trigger=None,
) -> tuple:
    return ql.sinkingNotionals(bond_length, frequency, coupon_rate, initial_notional)


@xlo.func(
    help="Create a QuantLib ZeroCouponBond object.",
    args={
        "settlement_days": "The number of days to settlement.",
        "calendar": "The calendar for date calculations.",
        "face_amount": "The face amount of the bond.",
        "maturity_date": "The maturity date of the bond.",
        "business_day_convention": "The business day convention.",
        "issue_date": "The issue date of the bond.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponBond(
    settlement_days: int,
    calendar: qCalendar,
    face_amount: float,
    maturity_date: qDate,
    business_day_convention: qBusinessDayConvention = ql.Following,
    redemption: float = 100.0,
    issue_date: qDate = ql.Date(),
    trigger=None,
) -> ql.ZeroCouponBond:
    return ql.ZeroCouponBond(
        settlement_days,
        calendar,
        face_amount,
        maturity_date,
        business_day_convention,
        redemption,
        issue_date,
    )


@xlo.func(
    help="Create a QuantLib FixedRateBond object with detailed parameters.",
    args={
        "settlement_days": "The number of days to settlement.",
        "face_amount": "The face amount of the bond.",
        "schedule": "The schedule for coupon payments.",
        "coupons": "The list of coupon rates.",
        "payment_day_counter": "The day counter for payment dates.",
        "business_day_convention": "The business day convention.",
        "redemption": "The redemption amount (default: 100.0).",
        "issue_date": "The issue date of the bond.",
        "payment_calendar": "The calendar for payment dates.",
        "ex_coupon_period": "The period for ex-coupon dates.",
        "ex_coupon_calendar": "The calendar for ex-coupon dates.",
        "ex_coupon_convention": "The business day convention for ex-coupon dates.",
        "ex_coupon_end_of_month": "Whether to adjust ex-coupon dates to the end of the month.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedRateBond(
    settlement_days: int,
    face_amount: float,
    schedule: ql.Schedule,
    coupons: xlo.Array(dims=1),
    payment_day_counter: qDayCounter,
    business_day_convention: qBusinessDayConvention = ql.Following,
    redemption: float = 100.0,
    issue_date: qDate = ql.Date(),
    payment_calendar=None,
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar=None,
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    trigger=None,
) -> ql.FixedRateBond:
    if payment_calendar is not None:
        payment_calendar = qCalendar.__wrapped__(payment_calendar)
    if ex_coupon_calendar is not None:
        ex_coupon_calendar = qCalendar.__wrapped__(ex_coupon_calendar)
    _BOND_KWARGS = {
        "payment_calendar": "paymentCalendar",
        "ex_coupon_period": "exCouponPeriod",
        "ex_coupon_calendar": "exCouponCalendar",
        "ex_coupon_convention": "exCouponConvention",
        "ex_coupon_end_of_month": "exCouponEndOfMonth",
    }
    kwargs = {}
    for param_name, kw_name in _BOND_KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.FixedRateBond(
        settlement_days,
        face_amount,
        schedule,
        to_float_list(coupons),
        payment_day_counter,
        business_day_convention,
        redemption,
        issue_date,
        **kwargs,
    )


@xlo.func(
    help="Create a QuantLib AmortizingFixedRateBond object .",
    args={
        "settlement_days": "The number of settlement days after the trade date.",
        "notionals": "The list of notional amounts for each period.",
        "schedule": "The schedule for coupon payments.",
        "coupons": "The list of coupon rates.",
        "accrual_day_counter": "The day counter for accrual calculations.",
        "payment_convention": "The business day convention for payment dates.",
        "issue_date": "The issue date of the bond.",
        "ex_coupon_period": "The period for ex-coupon dates.",
        "ex_coupon_calendar": "The calendar for ex-coupon dates.",
        "ex_coupon_convention": "The business day convention for ex-coupon dates.",
        "ex_coupon_end_of_month": "Whether to adjust ex-coupon dates to the end of the month.",
        "redemptions": "The list of redemption amounts (default: [100]).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAmortizingFixedRateBond(
    settlement_days: int,
    notionals: xlo.Array(dims=1),
    schedule: ql.Schedule,
    coupons: xlo.Array(dims=1),
    accrual_day_counter: qDayCounter,
    payment_convention: qBusinessDayConvention = ql.Following,
    issue_date: qDate = ql.Date(),
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar=None,
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    redemptions=100,
    trigger=None,
) -> ql.AmortizingFixedRateBond:

    if ex_coupon_calendar is not None:
        ex_coupon_calendar = qCalendar.__wrapped__(ex_coupon_calendar)
    redemptions = to_float_list(redemptions)
    _BOND_KWARGS = {
        "ex_coupon_calendar": "exCouponCalendar",
        "ex_coupon_convention": "exCouponConvention",
        "ex_coupon_end_of_month": "exCouponEndOfMonth",
        "redemptions": "redemptions",
    }
    kwargs = {}
    for param_name, kw_name in _BOND_KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.AmortizingFixedRateBond(
        settlement_days,
        to_float_list(notionals),
        schedule,
        to_float_list(coupons),
        accrual_day_counter,
        payment_convention,
        issue_date,
        ex_coupon_period,
        **kwargs,
    )


# TODO When the caps and floors are passed in, the error 'Pricer not set' appears, even though it has been set.
@xlo.func(
    help="Create a QuantLib AmortizingFloatingRateBond object.",
    args={
        "settlement_days": "The number of settlement days after the trade date.",
        "notional": "The list of notional amounts for each period.",
        "schedule": "The schedule for coupon payments.",
        "index": "The Ibor index for floating rate calculations.",
        "accrual_day_counter": "The day counter for accrual calculations.",
        "payment_convention": "The business day convention for payment dates.",
        "fixing_days": "The number of days for fixing the rate (default: 0).",
        "gearings": "The list of gearings for the floating rate (default: [1.0]).",
        "spreads": "The list of spreads for the floating rate (default: [0.0]).",
        "caps": "The list of cap rates for the floating rate (default: []).",
        "floors": "The list of floor rates for the floating rate (default: []).",
        "in_arrears": "Whether the floating rate is in arrears (default: False).",
        "issue_date": "The issue date of the bond.",
        "ex_coupon_period": "The period for ex-coupon dates.",
        "ex_coupon_calendar": "The calendar for ex-coupon dates.",
        "ex_coupon_convention": "The business day convention for ex-coupon dates.",
        "ex_coupon_end_of_month": "Whether to adjust ex-coupon dates to the end of the month.",
        "redemptions": "The list of redemption amounts (default: [100.0]).",
        "payment_lag": "The lag for payment dates (default: 0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAmortizingFloatingRateBond(
    settlement_days: int,
    notional: xlo.Array(dims=1),
    schedule: ql.Schedule,
    index: ql.IborIndex,
    accrual_day_counter: qDayCounter,
    payment_convention: qBusinessDayConvention = ql.Following,
    fixing_days: int = 0,
    gearings: xlo.Array(dims=1) = [1.0],
    spreads: xlo.Array(dims=1) = [0.0],
    caps=None,
    floors=None,
    in_arrears: bool = False,
    issue_date: qDate = ql.Date(),
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar=None,
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    redemptions=100.0,
    payment_lag: int = 0,
    trigger=None,
) -> ql.AmortizingFloatingRateBond:
    if ex_coupon_calendar is not None:
        ex_coupon_calendar = qCalendar.__wrapped__(ex_coupon_calendar)
    redemptions = to_float_list(redemptions)
    _BOND_KWARGS = {
        "ex_coupon_calendar": "exCouponCalendar",
        "ex_coupon_convention": "exCouponConvention",
        "ex_coupon_end_of_month": "exCouponEndOfMonth",
        "redemptions": "redemptions",
        "payment_lag": "paymentLag",
    }
    kwargs = {}
    for param_name, kw_name in _BOND_KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.AmortizingFloatingRateBond(
        settlement_days,
        to_float_list(notional),
        schedule,
        index,
        accrual_day_counter,
        payment_convention,
        fixing_days,
        to_float_list(gearings),
        to_float_list(spreads),
        to_float_list(caps),
        to_float_list(floors),
        in_arrears,
        issue_date,
        ex_coupon_period,
        **kwargs,
    )


# TODO When the caps and floors are passed in, the error 'Pricer not set' appears, even though it has been set.
@xlo.func(
    help="Create a QuantLib FloatingRateBond object.",
    args={
        "settlement_days": "The number of settlement days after the trade date.",
        "face_amount": "The face amount of the bond.",
        "schedule": "The schedule for coupon payments.",
        "index": "The Ibor index for floating rate calculations.",
        "payment_day_counter": "The day counter for payment dates.",
        "payment_convention": "The business day convention for payment dates.",
        "fixing_days": "The number of days for fixing the rate (default: 0).",
        "gearings": "The list of gearings for the floating rate (default: [1.0]).",
        "spreads": "The list of spreads for the floating rate (default: [0.0]).",
        "caps": "The list of cap rates for the floating rate (default: []).",
        "floors": "The list of floor rates for the floating rate (default: []).",
        "in_arrears": "Whether the floating rate is in arrears (default: False).",
        "redemption": "The redemption amount (default: 100.0).",
        "issue_date": "The issue date of the bond.",
        "ex_coupon_period": "The period for ex-coupon dates.",
        "ex_coupon_calendar": "The calendar for ex-coupon dates.",
        "ex_coupon_convention": "The business day convention for ex-coupon dates.",
        "ex_coupon_end_of_month": "Whether to adjust ex-coupon dates to the end of the month.",
        "fixing_convention": "The business day convention for fixing dates (default: Preceding).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatingRateBond(
    settlement_days: int,
    face_amount: float,
    schedule: ql.Schedule,
    index: ql.IborIndex,
    payment_day_counter: qDayCounter,
    payment_convention: qBusinessDayConvention = ql.Following,
    fixing_days: int = 0,
    gearings: xlo.Array(dims=1) = [1.0],
    spreads: xlo.Array(dims=1) = [0.0],
    caps=None,
    floors=None,
    in_arrears: bool = False,
    redemption: float = 100.0,
    issue_date: qDate = ql.Date(),
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar=None,
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    fixing_convention: qBusinessDayConvention = ql.Preceding,
    trigger=None,
) -> ql.FloatingRateBond:
    if ex_coupon_calendar is not None:
        ex_coupon_calendar = qCalendar.__wrapped__(ex_coupon_calendar)
    _BOND_KWARGS = {
        "ex_coupon_calendar": "exCouponCalendar",
        "ex_coupon_convention": "exCouponConvention",
        "ex_coupon_end_of_month": "exCouponEndOfMonth",
        "fixing_convention": "fixingConvention",
    }
    kwargs = {}
    for param_name, kw_name in _BOND_KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value
    return ql.FloatingRateBond(
        settlement_days,
        face_amount,
        schedule,
        index,
        payment_day_counter,
        payment_convention,
        fixing_days,
        to_float_list(gearings),
        to_float_list(spreads),
        to_float_list(caps),
        to_float_list(floors),
        in_arrears,
        redemption,
        issue_date,
        ex_coupon_period,
        **kwargs,
    )


# TODO When the gearings<>0 are passed, the error 'Pricer not set' appears, even though it has been set.
@xlo.func(
    help="Create a QuantLib CmsRateBond object.",
    args={
        "settlement_days": "The number of settlement days after the trade date.",
        "face_amount": "The face amount of the bond.",
        "schedule": "The schedule for coupon payments.",
        "index": "The swap index for CMS rate calculations.",
        "payment_day_counter": "The day counter for payment dates.",
        "payment_convention": "The business day convention for payment dates.",
        "fixing_days": "The number of days for fixing the rate.",
        "gearings": "The list of gearings for the CMS rate.",
        "spreads": "The list of spreads for the CMS rate.",
        "caps": "The list of cap rates for the CMS rate.",
        "floors": "The list of floor rates for the CMS rate.",
        "in_arrears": "Whether the CMS rate is in arrears (default: False).",
        "redemption": "The redemption amount (default: 100.0).",
        "issue_date": "The issue date of the bond.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCmsRateBond(
    settlement_days: int,
    face_amount: float,
    schedule: ql.Schedule,
    index: ql.SwapIndex,
    payment_day_counter: qDayCounter,
    payment_convention: qBusinessDayConvention,
    fixing_days: int,
    gearings: xlo.Array(dims=1),
    spreads: xlo.Array(dims=1),
    caps: xlo.Array(dims=1),
    floors: xlo.Array(dims=1),
    in_arrears: bool = False,
    redemption: float = 100.0,
    issue_date: qDate = ql.Date(),
    trigger=None,
) -> ql.CmsRateBond:
    return ql.CmsRateBond(
        settlement_days,
        face_amount,
        schedule,
        index,
        payment_day_counter,
        payment_convention,
        fixing_days,
        to_float_list(gearings),
        to_float_list(spreads),
        to_float_list(caps),
        to_float_list(floors),
        in_arrears,
        redemption,
        issue_date,
    )


# TODO When the gearings<>0 are passed, the error 'Pricer not set' appears, even though it has been set.
@xlo.func(
    help="Create a QuantLib AmortizingCmsRateBond object.",
    args={
        "settlement_days": "The number of settlement days after the trade date.",
        "notionals": "The list of notional amounts for each period.",
        "schedule": "The schedule for coupon payments.",
        "index": "The swap index for CMS rate calculations.",
        "payment_day_counter": "The day counter for payment dates.",
        "payment_convention": "The business day convention for payment dates.",
        "fixing_days": "The number of days for fixing the rate.",
        "gearings": "The list of gearings for the CMS rate (default: [1.0]).",
        "spreads": "The list of spreads for the CMS rate (default: [0.0]).",
        "caps": "The list of cap rates for the CMS rate (default: []).",
        "floors": "The list of floor rates for the CMS rate (default: []).",
        "in_arrears": "Whether the CMS rate is in arrears (default: False).",
        "issue_date": "The issue date of the bond.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAmortizingCmsRateBond(
    settlement_days: int,
    notionals: xlo.Array(dims=1),
    schedule: ql.Schedule,
    index: ql.SwapIndex,
    payment_day_counter: qDayCounter,
    payment_convention: qBusinessDayConvention = ql.Following,
    fixing_days: int = 0,
    gearings: xlo.Array(dims=1) = [0.0],
    spreads: xlo.Array(dims=1) = [0.0],
    caps: xlo.Array(dims=1) = None,
    floors: xlo.Array(dims=1) = None,
    in_arrears: bool = False,
    issue_date: qDate = ql.Date(),
    trigger=None,
) -> ql.AmortizingCmsRateBond:
    return ql.AmortizingCmsRateBond(
        settlement_days,
        to_float_list(notionals),
        schedule,
        index,
        payment_day_counter,
        payment_convention,
        fixing_days,
        to_float_list(gearings),
        to_float_list(spreads),
        to_float_list(caps),
        to_float_list(floors),
        in_arrears,
        issue_date,
    )


@xlo.func(
    help="Create a bond discounting pricing engine.",
    args={
        "discount_curve": "The discount curve (yield term structure handle).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDiscountingBondEngine(
    discount_curve: ql.YieldTermStructureHandle, trigger=None
) -> ql.DiscountingBondEngine:
    return ql.DiscountingBondEngine(discount_curve)


@xlo.func(
    help="Return the callability schedule of a CallableBond as a list of tuples (type, date, price).",
    args={"callable_bond": "The QuantLib CallableBond instance."},
    group=EXCEL_GROUP_NAME,
)
def qlCallableBondCallability(callable_bond: ql.CallableBond, Trigger=None):
    return callable_bond.callability()


@xlo.func(
    help="Calculate the implied volatility of a bond.",
    args={
        "target_price": "The target price of the bond.",
        "discount_curve": "The discount curve.",
        "accuracy": "The accuracy of the calculation.",
        "max_evaluations": "The maximum number of evaluations.",
        "min_vol": "The minimum volatility.",
        "max_vol": "The maximum volatility.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCallableBondImpliedVolatility(
    callable_bond: ql.CallableBond,
    target_price: ql.BondPrice,
    discount_curve: ql.YieldTermStructureHandle,
    accuracy: float,
    max_evaluations: int,
    min_vol: float,
    max_vol: float,
    trigger=None,
) -> float:
    return callable_bond.impliedVolatility(
        target_price,
        discount_curve,
        accuracy,
        max_evaluations,
        min_vol,
        max_vol,
    )


@xlo.func(
    help="Calculate the Option-Adjusted Spread (OAS) of a bond.",
    args={
        "clean_price": "The clean price of the bond.",
        "engine_ts": "The yield term structure.",
        "dc": "The day counter.",
        "compounding": "The compounding convention.",
        "freq": "The frequency of compounding.",
        "settlement_date": "The settlement date.",
        "accuracy": "The accuracy of the calculation.",
        "max_iterations": "The maximum number of iterations.",
        "guess": "The initial guess for the OAS.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCallableBondOAS(
    callable_bond: ql.CallableBond,
    clean_price: float,
    engine_ts: ql.YieldTermStructureHandle,
    dc: qDayCounter,
    compounding: qCompounding,
    freq: qFrequency,
    settlement_date: qDate = ql.Date(),
    accuracy: float = 1e-10,
    max_iterations: int = 100,
    guess: float = 0.0,
    trigger=None,
) -> float:
    return callable_bond.OAS(
        clean_price,
        engine_ts,
        dc,
        compounding,
        freq,
        settlement_date,
        accuracy,
        max_iterations,
        guess,
    )


@xlo.func(
    help="Calculate the clean price of a bond given the Option-Adjusted Spread (OAS).",
    args={
        "oas": "The Option-Adjusted Spread (OAS).",
        "engine_ts": "The yield term structure.",
        "day_counter": "The day counter.",
        "compounding": "The compounding convention.",
        "frequency": "The frequency of compounding.",
        "settlement_date": "The settlement date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCallableBondCleanPriceOAS(
    callable_bond: ql.CallableBond,
    oas: float,
    engine_ts: ql.YieldTermStructureHandle,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return callable_bond.cleanPriceOAS(
        oas,
        engine_ts,
        day_counter,
        compounding,
        frequency,
        settlement_date,
    )


@xlo.func(
    help="Calculate the effective duration of a bond.",
    args={
        "oas": "The Option-Adjusted Spread (OAS).",
        "engine_ts": "The yield term structure.",
        "day_counter": "The day counter.",
        "compounding": "The compounding convention.",
        "frequency": "The frequency of compounding.",
        "bump": "The bump size for the calculation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCallableBondEffectiveDuration(
    callable_bond: ql.CallableBond,
    oas: float,
    engine_ts: ql.YieldTermStructureHandle,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    bump: float = 2e-4,
    trigger=None,
) -> float:
    return callable_bond.effectiveDuration(
        oas,
        engine_ts,
        day_counter,
        compounding,
        frequency,
        bump,
    )


@xlo.func(
    help="Calculate the effective convexity of a bond.",
    args={
        "oas": "The Option-Adjusted Spread (OAS).",
        "engine_ts": "The yield term structure.",
        "day_counter": "The day counter.",
        "compounding": "The compounding convention.",
        "frequency": "The frequency of compounding.",
        "bump": "The bump size for the calculation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCallableBondEffectiveConvexity(
    callable_bond: ql.CallableBond,
    oas: float,
    engine_ts: ql.YieldTermStructureHandle,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    bump: float = 2e-4,
    trigger=None,
) -> float:
    return callable_bond.effectiveConvexity(
        oas,
        engine_ts,
        day_counter,
        compounding,
        frequency,
        bump,
    )


@xlo.func(
    help="Create a QuantLib CallableFixedRateBond object.",
    args={
        "settlement_days": "The number of settlement days after the trade date.",
        "face_amount": "The face amount of the bond.",
        "schedule": "The schedule for coupon payments.",
        "coupons": "The list of coupon rates.",
        "accrual_day_counter": "The day counter for accrual periods.",
        "payment_convention": "The business day convention for payment dates.",
        "redemption": "The redemption amount at maturity.",
        "issue_date": "The issue date of the bond.",
        "put_call_schedule": "The list of callability schedules.",
        "ex_coupon_period": "The period before the ex-coupon date.",
        "ex_coupon_calendar": "The calendar for ex-coupon dates.",
        "ex_coupon_convention": "The business day convention for ex-coupon dates.",
        "ex_coupon_end_of_month": "Whether the ex-coupon date is adjusted to the end of the month.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCallableFixedRateBond(
    settlement_days: int,
    face_amount: float,
    schedule: ql.Schedule,
    coupons: xlo.Array(dims=1),
    accrual_day_counter: qDayCounter,
    payment_convention: qBusinessDayConvention,
    redemption: float,
    issue_date: qDate,
    put_call_schedule: xlo.Array(dims=1),
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar=None,
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    trigger=None,
) -> ql.CallableFixedRateBond:
    if ex_coupon_calendar is not None:
        ex_coupon_calendar = qCalendar.__wrapped__(ex_coupon_calendar)
    _BOND_KWARGS = {
        "ex_coupon_calendar": "exCouponCalendar",
        "ex_coupon_convention": "exCouponConvention",
        "ex_coupon_end_of_month": "exCouponEndOfMonth",
    }
    kwargs = {}
    for param_name, kw_name in _BOND_KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value
    return ql.CallableFixedRateBond(
        settlement_days,
        face_amount,
        schedule,
        to_float_list(coupons),
        accrual_day_counter,
        payment_convention,
        redemption,
        issue_date,
        to_object_list(put_call_schedule, ql.Callability),
        ex_coupon_period,
        **kwargs,
    )


@xlo.func(
    help="Create a QuantLib CallableZeroCouponBond object.",
    args={
        "settlement_days": "The number of settlement days after the trade date.",
        "face_amount": "The face amount of the bond.",
        "calendar": "The calendar for payment dates.",
        "maturity_date": "The maturity date of the bond.",
        "day_counter": "The day counter for accrual periods.",
        "payment_convention": "The business day convention for payment dates.",
        "redemption": "The redemption amount at maturity.",
        "issue_date": "The issue date of the bond.",
        "put_call_schedule": "The list of callability schedules.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCallableZeroCouponBond(
    settlement_days: int,
    face_amount: float,
    calendar: qCalendar,
    maturity_date: qDate,
    day_counter: qDayCounter,
    payment_convention: qBusinessDayConvention = ql.Following,
    redemption: float = 100.0,
    issue_date: qDate = ql.Date(),
    put_call_schedule: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.CallableZeroCouponBond:
    return ql.CallableZeroCouponBond(
        settlement_days,
        face_amount,
        calendar,
        maturity_date,
        day_counter,
        payment_convention,
        redemption,
        issue_date,
        to_object_list(put_call_schedule, ql.Callability),
    )


@xlo.func(
    help="Create a QuantLib TreeCallableFixedRateBondEngine object with time steps.",
    args={
        "model": "The short rate model.",
        "time_steps": "The number of time steps.",
        "term_structure": "The yield term structure handle (default: empty handle).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTreeCallableFixedRateBondEngine(
    model: ql.ShortRateModel,
    time_steps: int,
    term_structure: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> ql.TreeCallableFixedRateBondEngine:
    return ql.TreeCallableFixedRateBondEngine(model, time_steps, term_structure)


@xlo.func(
    help="Create a QuantLib TreeCallableFixedRateBondEngine object with a time grid.",
    args={
        "model": "The short rate model.",
        "time_grid": "The time grid.",
        "term_structure": "The yield term structure handle (default: empty handle).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTreeCallableFixedRateBondEngine2(
    model: ql.ShortRateModel,
    time_grid: ql.TimeGrid,
    term_structure: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> ql.TreeCallableFixedRateBondEngine:
    return ql.TreeCallableFixedRateBondEngine(model, time_grid, term_structure)


@xlo.func(
    help="Create a QuantLib BlackCallableFixedRateBondEngine object.",
    args={
        "fwd_yield_vol": "The forward yield volatility.",
        "discount_curve": "The discount curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCallableFixedRateBondEngine(
    fwd_yield_vol: qQuoteHandle,
    discount_curve: ql.YieldTermStructureHandle,
    trigger=None,
) -> ql.BlackCallableFixedRateBondEngine:
    return ql.BlackCallableFixedRateBondEngine(
        fwd_yield_vol,
        discount_curve,
    )


@xlo.func(
    help="Create a QuantLib CPIBond object.",
    args={
        "settlement_days": "The number of settlement days after the trade date.",
        "face_amount": "The face amount of the bond.",
        "growth_only": "Whether the bond has growth-only CPI adjustments.",
        "base_cpi": "The base CPI index value.",
        "observation_lag": "The lag period for CPI observations.",
        "cpi_index": "The zero inflation index.",
        "observation_interpolation": 'The interpolation type for CPI observations (e.g., "LINEAR" or "FLAT").',
        "schedule": "The schedule for coupon payments.",
        "coupons": "The list of coupon rates.",
        "accrual_day_counter": "The day counter for accrual calculations.",
        "payment_convention": "The business day convention for payment dates (default: ModifiedFollowing).",
        "issue_date": "The issue date of the bond (default: today).",
        "payment_calendar": "The calendar for payment dates.",
        "ex_coupon_period": "The period for ex-coupon dates (default: empty period).",
        "ex_coupon_calendar": "The calendar for ex-coupon dates.",
        "ex_coupon_convention": "The business day convention for ex-coupon dates (default: Unadjusted).",
        "ex_coupon_end_of_month": "Whether to adjust ex-coupon dates to the end of the month (default: False).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPIBond(
    settlement_days: int,
    face_amount: float,
    growth_only: bool,
    base_cpi: float,
    observation_lag: qPeriod,
    cpi_index: ql.ZeroInflationIndex,
    observation_interpolation: qCPIInterpolationType,
    schedule: ql.Schedule,
    coupons: xlo.Array(dims=1),
    accrual_day_counter: qDayCounter,
    payment_convention: qBusinessDayConvention = ql.ModifiedFollowing,
    issue_date: qDate = ql.Date(),
    payment_calendar=None,
    ex_coupon_period: qPeriod = ql.Period(),
    ex_coupon_calendar=None,
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    trigger=None,
) -> ql.CPIBond:
    if payment_calendar is not None:
        payment_calendar = qCalendar.__wrapped__(payment_calendar)
    if ex_coupon_calendar is not None:
        ex_coupon_calendar = qCalendar.__wrapped__(ex_coupon_calendar)

    _BOND_KWARGS = {
        "payment_calendar": "paymentCalendar",
        "ex_coupon_period": "exCouponPeriod",
        "ex_coupon_calendar": "exCouponCalendar",
        "ex_coupon_convention": "exCouponConvention",
        "ex_coupon_end_of_month": "exCouponEndOfMonth",
    }
    kwargs = {}
    for param_name, kw_name in _BOND_KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.CPIBond(
        settlement_days,
        face_amount,
        growth_only,
        base_cpi,
        observation_lag,
        cpi_index,
        observation_interpolation,
        schedule,
        to_float_list(coupons),
        accrual_day_counter,
        payment_convention,
        issue_date,
        **kwargs,
    )
