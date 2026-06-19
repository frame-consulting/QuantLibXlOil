import QuantLib as ql
import xloil as xlo


from .calendars import qCalendar, qBusinessDayConvention
from .credit import qProtectionSide, QL_PROTECTION_SIDE
from .config import EXCEL_GROUP_NAME
from .date import qDate, qPeriod
from .daycounters import qDayCounter
from .ratehelpers import qQuoteHandle
from .scheduler import qDateGenerationRule
from .utilities import enum_value, first_key, UNKNOWN_KEY, UNKNOWN_VALUE

QL_CREDIT_DEFAULT_SWAP_PRICING_MODEL = {
    "MIDPOINT": ql.CreditDefaultSwap.Midpoint,
    "ISDA": ql.CreditDefaultSwap.ISDA,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_ISDA_CDS_ENGINE_NUMERICAL_FIX = {
    "NO_FIX": ql.IsdaCdsEngine.NoFix,
    "TAYLOR": ql.IsdaCdsEngine.Taylor,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_ISDA_CDS_ENGINE_ACCRUAL_BIAS = {
    "HALF_DAY_BIAS": ql.IsdaCdsEngine.HalfDayBias,
    "NO_BIAS": ql.IsdaCdsEngine.NoBias,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_ISDA_CDS_ENGINE_FORWARDS_IN_COUPON_PERIOD = {
    "FLAT": ql.IsdaCdsEngine.Flat,
    "PIECEWISE": ql.IsdaCdsEngine.Piecewise,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qCreditDefaultSwapPricingModel(s: str) -> int:
    return enum_value(s, QL_CREDIT_DEFAULT_SWAP_PRICING_MODEL)


@xlo.converter()
def qCreditDefaultSwapPricingModel(s: str) -> int:
    return _qCreditDefaultSwapPricingModel(s)


def _qIsdaCdsEngineNumericalFix(s: str) -> int:
    return enum_value(s, QL_ISDA_CDS_ENGINE_NUMERICAL_FIX)


@xlo.converter()
def qIsdaCdsEngineNumericalFix(s: str) -> int:
    return _qIsdaCdsEngineNumericalFix(s)


def _qIsdaCdsEngineAccrualBias(s: str) -> int:
    return enum_value(s, QL_ISDA_CDS_ENGINE_ACCRUAL_BIAS)


@xlo.converter()
def qIsdaCdsEngineAccrualBias(s: str) -> int:
    return _qIsdaCdsEngineAccrualBias(s)


def _qIsdaCdsEngineForwardsInCouponPeriod(s: str) -> int:
    return enum_value(s, QL_ISDA_CDS_ENGINE_FORWARDS_IN_COUPON_PERIOD)


@xlo.converter()
def qIsdaCdsEngineForwardsInCouponPeriod(s: str) -> int:
    return _qIsdaCdsEngineForwardsInCouponPeriod(s)


# Claim (for defaulted names)


@xlo.func(
    help="Calculates the claim amount for a given default date, notional, and recovery rate.",
    args={
        "claim": "The claim object.",
        "default_date": "The date of default (as a qDate).",
        "notional": "The notional amount of the claim.",
        "recovery_rate": "The recovery rate (between 0 and 1).",
        "trigger": "Optional trigger for certain claim types (e.g., 'AtDefault').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlClaimAmount(
    claim: ql.Claim,
    default_date: qDate,
    notional: float,
    recovery_rate: float,
    trigger=None,
) -> float:
    return claim.amount(default_date, notional, recovery_rate, trigger)


@xlo.func(
    help="Creates a FaceValueClaim object, which pays the face value of the claim upon default.",
    group=EXCEL_GROUP_NAME,
)
def qlFaceValueClaim(
    trigger=None,
) -> ql.FaceValueClaim:
    return ql.FaceValueClaim()


@xlo.func(
    help="Creates a FaceValueAccrualClaim object, which pays the face value plus accrued interest upon default.",
    args={
        "bond": "The bond associated with the claim.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFaceValueAccrualClaim(
    bond: ql.Bond,
    trigger=None,
) -> ql.FaceValueAccrualClaim:
    return ql.FaceValueAccrualClaim(bond)


@xlo.func(
    help="Creates an AtDefaultClaim object, which pays the value of the claim at the time of default.",
    args={
        "protection_side": "The side of the protection (BUY/SELL).",
        "notional": "The notional amount of the claim.",
        "spread": "The spread of the CDS.",
        "schedule": "The payment schedule of the CDS.",
        "payment_convention": "The payment convention for the CDS.",
        "day_counter": "The day counter for the CDS.",
        "settles_accrual": "Whether the CDS settles accrued interest.",
        "pays_at_default": "Whether the CDS pays at default.",
        "protection_start_date": "The start date of the CDS.",
        "claim": "The claim object to use.",
        "last_period_day_counter": "The day counter for the last period of the CDS.",
        "rebates_accrual": "Whether the CDS accrues rebates.",
        "trade_date": "The trade date of the CDS.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwap(
    protection_side: qProtectionSide,
    notional: float,
    spread: float,
    schedule: ql.Schedule,
    payment_convention: qBusinessDayConvention,
    day_counter: qDayCounter,
    settles_accrual: bool = True,
    pays_at_default: bool = True,
    protection_start_date: qDate = ql.Date(),
    claim: ql.Claim = None,
    last_period_day_counter: str = None,  # cannot use ql.DayCounter(),
    rebates_accrual: bool = True,
    trade_date: qDate = ql.Date(),
    trigger=None,
) -> ql.CreditDefaultSwap:
    if last_period_day_counter is None:
        last_period_day_counter = day_counter
    else:
        last_period_day_counter = qDayCounter.__wrapped__(last_period_day_counter)
    #
    return ql.CreditDefaultSwap(
        protection_side,
        notional,
        spread,
        schedule,
        payment_convention,
        day_counter,
        settles_accrual,
        pays_at_default,
        protection_start_date,
        claim,
        last_period_day_counter,
        rebates_accrual,
        trade_date,
    )


@xlo.func(
    help="Creates a CreditDefaultSwap object with an upfront payment.",
    args={
        "protection_side": "The side of the protection (BUY/SELL).",
        "notional": "The notional amount of the CDS.",
        "upfront": "The upfront fee to be paid at the start of the CDS.",
        "spread": "The spread of the CDS.",
        "schedule": "The payment schedule of the CDS.",
        "payment_convention": "The payment convention for the CDS.",
        "day_counter": "The day counter for the CDS.",
        "settles_accrual": "Whether the CDS settles accrued interest.",
        "pays_at_default": "Whether the CDS pays at default.",
        "protection_start_date": "The start date of the CDS.",
        "upfront_date": "The date on which the upfront payment is made.",
        "claim": "The claim object to use.",
        "last_period_day_counter": "The day counter for the last period of the CDS.",
        "rebates_accrual": "Whether the CDS accrues rebates.",
        "trade_date": "The trade date of the CDS.",
        "cash_settlement_days": "The number of days for cash settlement after the trade date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapWithUpfront(
    protection_side: qProtectionSide,
    notional: float,
    upfront: float,
    spread: float,
    schedule: ql.Schedule,
    payment_convention: qBusinessDayConvention,
    day_counter: qDayCounter,
    settles_accrual: bool = True,
    pays_at_default: bool = True,
    protection_start_date: qDate = ql.Date(),
    upfront_date: qDate = ql.Date(),
    claim: ql.Claim = None,
    last_period_day_counter: str = None,  # cannot use ql.DayCounter(),
    rebates_accrual: bool = True,
    trade_date: qDate = ql.Date(),
    cash_settlement_days: int = 3,
    trigger=None,
) -> ql.CreditDefaultSwap:
    if last_period_day_counter is None:
        last_period_day_counter = day_counter
    else:
        last_period_day_counter = qDayCounter.__wrapped__(last_period_day_counter)
    #
    return ql.CreditDefaultSwap(
        protection_side,
        notional,
        upfront,
        spread,
        schedule,
        payment_convention,
        day_counter,
        settles_accrual,
        pays_at_default,
        protection_start_date,
        upfront_date,
        claim,
        last_period_day_counter,
        rebates_accrual,
        trade_date,
        cash_settlement_days,
    )


@xlo.func(
    help="Returns the protection side of a given CreditDefaultSwap as a string (BUY/SELL).",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditdefaultswapSide(cds: ql.CreditDefaultSwap, trigger=None) -> str:
    return first_key(QL_PROTECTION_SIDE, cds.side())


@xlo.func(
    help="Returns the notional amount of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapNotional(cds: ql.CreditDefaultSwap, trigger=None) -> float:
    return cds.notional()


@xlo.func(
    help="Returns the spread of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapRunningSpread(cds: ql.CreditDefaultSwap, trigger=None) -> float:
    return cds.runningSpread()


@xlo.func(
    help="Returns the upfront payment of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapUpfront(cds: ql.CreditDefaultSwap, trigger=None) -> float:
    return cds.upfront()


@xlo.func(
    help="Returns whether a given CreditDefaultSwap settles accrued interest.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditdefaultSwapSettlesAccrual(cds: ql.CreditDefaultSwap, trigger=None) -> bool:
    return cds.settlesAccrual()


@xlo.func(
    help="Returns whether a given CreditDefaultSwap pays at default time.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditdefaultswapPaysAtDefaultTime(
    cds: ql.CreditDefaultSwap, trigger=None
) -> bool:
    return cds.paysAtDefaultTime()


@xlo.func(
    help="Returns the coupons of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapCoupons(
    cds: ql.CreditDefaultSwap, trigger=None
) -> list[ql.CashFlow]:
    return cds.coupons()


@xlo.func(
    help="Returns the protection start date of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapProtectionStartDate(
    cds: ql.CreditDefaultSwap, trigger=None
) -> ql.Date:
    return cds.protectionStartDate()


@xlo.func(
    help="Returns the protection end date of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapProtectionEndDate(
    cds: ql.CreditDefaultSwap, trigger=None
) -> ql.Date:
    return cds.protectionEndDate()


@xlo.func(
    help="Returns whether a given CreditDefaultSwap rebates accrued interest.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapRebatesAccrual(cds: ql.CreditDefaultSwap, trigger=None) -> bool:
    return cds.rebatesAccrual()


@xlo.func(
    help="Returns the upfront payment as CashFlow of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultswapUpfrontPayment(
    cds: ql.CreditDefaultSwap, trigger=None
) -> ql.CashFlow:
    return cds.upfrontPayment()


@xlo.func(
    help="Returns the accrual rebate as CashFlow of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapAccrualRebate(
    cds: ql.CreditDefaultSwap, trigger=None
) -> ql.CashFlow:
    return cds.accrualRebate()


@xlo.func(
    help="Returns the trade date of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapTradeDate(cds: ql.CreditDefaultSwap, trigger=None) -> ql.Date:
    return cds.tradeDate()


@xlo.func(
    help="Returns the cash settlement days of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapCashSettlementDays(
    cds: ql.CreditDefaultSwap, trigger=None
) -> int:
    return cds.cashSettlementDays()


@xlo.func(
    help="Returns the fair upfront payment of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapFairUpfront(cds: ql.CreditDefaultSwap, trigger=None) -> float:
    return cds.fairUpfront()


@xlo.func(
    help="Returns the fair spread of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapFairSpread(cds: ql.CreditDefaultSwap, trigger=None) -> float:
    return cds.fairSpread()


@xlo.func(
    help="Returns the coupon leg BPS of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapCouponLegBPS(cds: ql.CreditDefaultSwap, trigger=None) -> float:
    return cds.couponLegBPS()


@xlo.func(
    help="Returns the upfront BPS of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapUpfrontBPS(cds: ql.CreditDefaultSwap, trigger=None) -> float:
    return cds.upfrontBPS()


@xlo.func(
    help="Returns the coupon leg NPV of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapCouponLegNPV(cds: ql.CreditDefaultSwap, trigger=None) -> float:
    return cds.couponLegNPV()


@xlo.func(
    help="Returns the default leg NPV of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapDefaultLegNPV(cds: ql.CreditDefaultSwap, trigger=None) -> float:
    return cds.defaultLegNPV()


@xlo.func(
    help="Returns the upfront NPV of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapUpfrontNPV(cds: ql.CreditDefaultSwap, trigger=None) -> float:
    return cds.upfrontNPV()


@xlo.func(
    help="Returns the accrual rebate NPV of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapAccrualRebateNPV(
    cds: ql.CreditDefaultSwap, trigger=None
) -> float:
    return cds.accrualRebateNPV()


@xlo.func(
    help="Returns the implied hazard rate of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
        "target_npv": "The target NPV to match when calculating the implied hazard rate.",
        "discount_curve": "The discount curve to use for the calculation.",
        "day_counter": "The day counter to use for the calculation.",
        "recovery_rate": "The recovery rate to use for the calculation.",
        "accuracy": "The desired accuracy.",
        "model": "The pricing model to use for the calculation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapImpliedHazardRate(
    cds: ql.CreditDefaultSwap,
    target_npv: float,
    discount_curve: ql.YieldTermStructureHandle,
    day_counter: qDayCounter,
    recovery_rate: float = 0.40,
    accuracy: float = 1e-6,
    model: qCreditDefaultSwapPricingModel = ql.CreditDefaultSwap.Midpoint,
    trigger=None,
) -> float:
    return cds.impliedHazardRate(
        target_npv, discount_curve, day_counter, recovery_rate, accuracy, model
    )


@xlo.func(
    help="Returns the conventional spread of a given CreditDefaultSwap.",
    args={
        "cds": "The CreditDefaultSwap object to query.",
        "conventional_recovery": "The conventional recovery rate to use for the calculation.",
        "discount_curve": "The discount curve to use for the calculation.",
        "day_counter": "The day counter to use for the calculation.",
        "model": "The pricing model to use for the calculation. Default is ISDA.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCreditDefaultSwapConventionalSpread(
    cds: ql.CreditDefaultSwap,
    conventional_recovery: float,
    discount_curve: ql.YieldTermStructureHandle,
    day_counter: qDayCounter,
    model: qCreditDefaultSwapPricingModel = ql.CreditDefaultSwap.ISDA,
    trigger=None,
) -> float:
    return cds.conventionalSpread(
        conventional_recovery, discount_curve, day_counter, model
    )


if ql.__version__ >= "1.42":

    def qlMakeCreditDefaultSwap(
        maturity: str | float,
        running_spread: float,
        upfront_rate=None,
        side=None,
        notional=None,
        coupon_tenor=None,
        day_counter=None,
        last_period_day_counter=None,
        date_generation_rule=None,
        cash_settlement_days=None,
        pricing_engine=None,
        trade_date=None,
        trigger=None,
    ) -> ql.CreditDefaultSwap:
        if isinstance(maturity, str):
            maturity = qPeriod.__wrapped__(maturity)
        else:
            maturity = qDate.__wrapped__(maturity)
        #
        kwargs = {}
        if upfront_rate is not None:
            kwargs["upfrontRate"] = upfront_rate
        if side is not None:
            kwargs["protectionSide"] = qProtectionSide.__wrapped__(side)
        if coupon_tenor is not None:
            kwargs["couponTenor"] = qPeriod.__wrapped__(coupon_tenor)
        if day_counter is not None:
            kwargs["dayCounter"] = qDayCounter.__wrapped__(day_counter)
        if last_period_day_counter is not None:
            kwargs["lastPeriodDayCounter"] = qDayCounter.__wrapped__(
                last_period_day_counter
            )
        if date_generation_rule is not None:
            kwargs["dateGenerationRule"] = qDateGenerationRule.__wrapped__(
                date_generation_rule
            )
        if cash_settlement_days is not None:
            kwargs["cashSettlementDays"] = cash_settlement_days
        if pricing_engine is not None:
            kwargs["pricingEngine"] = pricing_engine
        if trade_date is not None:
            kwargs["tradeDate"] = qDate.__wrapped__(trade_date)
        return ql.MakeCreditDefaultSwap(maturity, running_spread, **kwargs)


@xlo.func(
    help="Calculates the maturity date of a Credit Default Swap based on the trade date.",
    args={
        "trade_date": "The trade date of the CDS (as a qDate).",
        "tenor": "The tenor of the CDS (as a qPeriod).",
        "date_generation_rule": "The date generation rule to use for calculating the maturity date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCdsMaturity(
    trade_date: qDate,
    tenor: qPeriod,
    date_generation_rule: qDateGenerationRule,
    trigger=None,
) -> ql.Date:
    return ql.cdsMaturity(trade_date, tenor, date_generation_rule)


@xlo.func(
    help="Creates a MidPointCdsEngine for pricing Credit Default Swaps.",
    args={
        "default_curve": "The default probability term structure to use for the engine.",
        "recovery_rate": "The recovery rate to use for the engine (between 0 and 1).",
        "discount_curve": "The discount curve to use for the engine.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMidPointCdsEngine(
    default_curve: ql.DefaultProbabilityTermStructureHandle,
    recovery_rate: float,
    discount_curve: ql.YieldTermStructureHandle,
    trigger=None,
) -> ql.MidPointCdsEngine:
    return ql.MidPointCdsEngine(default_curve, recovery_rate, discount_curve)


@xlo.func(
    help="Creates an IntegralCdsEngine for pricing Credit Default Swaps.",
    args={
        "integration_step": "The integration step to use for the engine (as a qPeriod).",
        "default_curve": "The default probability term structure to use for the engine.",
        "recovery_rate": "The recovery rate to use for the engine (between 0 and 1).",
        "discount_curve": "The discount curve to use for the engine.",
        "include_settlement_date_flows": "Whether to include settlement date flows in the calculation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIntegralCdsEngine(
    integration_step: qPeriod,
    default_curve: ql.DefaultProbabilityTermStructureHandle,
    recovery_rate: float,
    discount_curve: ql.YieldTermStructureHandle,
    include_settlement_date_flows: bool = False,
    trigger=None,
) -> ql.IntegralCdsEngine:
    return ql.IntegralCdsEngine(
        integration_step,
        default_curve,
        recovery_rate,
        discount_curve,
        include_settlement_date_flows,
    )


@xlo.func(
    help="Creates an IsdaCdsEngine for pricing Credit Default Swaps using ISDA model.",
    args={
        "default_curve": "The default probability term structure to use for the engine.",
        "recovery_rate": "The recovery rate to use for the engine (between 0 and 1).",
        "discount_curve": "The discount curve to use for the engine.",
        "include_settlement_date_flows": "Whether to include settlement date flows in the calculation.",
        "numerical_fix": "The numerical fix to use for the engine (e.g., 'No_Fix', 'Taylor').",
        "accrual_bias": "The accrual bias to use for the engine (e.g., 'Half_Day_Bias', 'No_Bias').",
        "forwards_in_coupon_period": "Whether to include forwards in coupon period calculations (e.g., 'Flat', 'Piecewise').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIsdaCdsEngine(
    default_curve: ql.DefaultProbabilityTermStructureHandle,
    recovery_rate: float,
    discount_curve: ql.YieldTermStructureHandle,
    include_settlement_date_flows: bool = False,
    numerical_fix: qIsdaCdsEngineNumericalFix = ql.IsdaCdsEngine.Taylor,
    accrual_bias: qIsdaCdsEngineAccrualBias = ql.IsdaCdsEngine.HalfDayBias,
    forwards_in_coupon_period: qIsdaCdsEngineForwardsInCouponPeriod = ql.IsdaCdsEngine.Piecewise,
    trigger=None,
) -> ql.IsdaCdsEngine:
    return ql.IsdaCdsEngine(
        default_curve,
        recovery_rate,
        discount_curve,
        include_settlement_date_flows,
        numerical_fix,
        accrual_bias,
        forwards_in_coupon_period,
    )


@xlo.func(
    help="Creates a CdsOption for a given Credit Default Swap and exercise.",
    args={
        "cds": "The Credit Default Swap to use for the option.",
        "exercise": "The exercise to use for the option.",
        "knocks_out": "Whether the option knocks out upon exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCdsOption(
    cds: ql.CreditDefaultSwap,
    exercise: ql.Exercise,
    knocks_out: bool = True,
    trigger=None,
) -> ql.CdsOption:
    return ql.CdsOption(cds, exercise, knocks_out)


@xlo.func(
    help="Creates a BlackCdsOptionEngine for pricing Credit Default Swap options using the Black model.",
    args={
        "default_curve": "The default probability term structure to use for the engine.",
        "recovery_rate": "The recovery rate to use for the engine (between 0 and 1).",
        "discount_curve": "The discount curve to use for the engine.",
        "vol": "The volatility to use for the engine (as a qQuoteHandle).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCdsOptionEngine(
    default_curve: ql.DefaultProbabilityTermStructureHandle,
    recovery_rate: float,
    discount_curve: ql.YieldTermStructureHandle,
    vol: qQuoteHandle,
    trigger=None,
) -> ql.BlackCdsOptionEngine:
    return ql.BlackCdsOptionEngine(default_curve, recovery_rate, discount_curve, vol)
