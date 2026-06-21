import numpy as np
import QuantLib as ql
import xloil as xlo
from typing import Optional

from .calendars import qBusinessDayConvention, qCalendar, QL_BUSINESSDAYCONVENTION
from .cashflows import qRateAveragingType, QL_RATE_AVERAGING_TYPE
from .config import EXCEL_GROUP_NAME
from .currencies import qCurrency
from .date import qDate, qFrequency, qPeriod, QL_FREQUENCY
from .daycounters import qDayCounter
from .scheduler import qDateGenerationRule
from .utilities import (
    enum_value,
    first_key,
    to_bool_list,
    to_float_list,
    to_object_list,
)

# The value mappings for payer and receiver correspond to those in QuantLib ( enum Type { Receiver = -1, Payer = 1 })
QL_SWAP_TYPE = {
    "PAYER": 1,
    "RECEIVER": -1,
    "1": 1,
    "-1": -1,
    "1.0": 1,
    "-1.0": -1,
}


def _qSwapType(swap_type: str | int | float) -> bool:
    if isinstance(swap_type, int):
        return enum_value(str(swap_type), QL_SWAP_TYPE)
    if isinstance(swap_type, float):
        return enum_value(str(swap_type), QL_SWAP_TYPE)
    return enum_value(swap_type, QL_SWAP_TYPE)


def _to_ql_legs(legs) -> tuple[ql.Leg, ...]:
    if legs is None:
        return ()
    if isinstance(legs, np.ndarray):
        if legs.ndim == 0:
            outer = [legs.item()]
        else:
            outer = [legs[i] for i in range(legs.shape[0])]
    elif isinstance(legs, (list, tuple)):
        outer = legs
    elif hasattr(legs, "__iter__") and not isinstance(legs, (str, bytes)):
        outer = legs
    else:
        outer = [legs]

    result: list[tuple[ql.CashFlow, ...]] = []
    for idx, maybe_leg in enumerate(outer):
        if isinstance(maybe_leg, np.ndarray) and maybe_leg.ndim == 0:
            maybe_leg = maybe_leg.item()
        try:
            normalized = to_object_list(maybe_leg, ql.CashFlow)
        except TypeError as e:
            raise TypeError(f"Element {idx} is not a valid ql.Leg: {e}") from e
        if len(normalized) == 0:
            continue
        result.append(tuple(normalized))
    return tuple(result)


@xlo.converter()
def qSwapType(swap_type: str | int | float):
    return _qSwapType(swap_type)


@xlo.func(
    help="Create a QuantLib Swap object from two legs of cash flows.",
    args={
        "first_leg": "The first leg of the swap as a list of cash flows.",
        "second_leg": "The second leg of the swap as a list of cash flows.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwap(
    first_leg: xlo.Array(dims=1),
    second_leg: xlo.Array(dims=1),
    trigger=None,
) -> ql.Swap:
    first_leg = to_object_list(first_leg, ql.CashFlow)
    second_leg = to_object_list(second_leg, ql.CashFlow)
    return ql.Swap(first_leg, second_leg)


@xlo.func(
    help="Create a QuantLib Swap object from multiple legs and payer information.",
    args={
        "legs": "The legs of the swap as a list of legs.",
        "payer": "A list indicating which leg is the payer (True for payer, False for receiver).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwap2(
    legs: xlo.Array(dims=1),
    payer: xlo.Array(dims=1),
    trigger=None,
) -> ql.Swap:
    legs = _to_ql_legs(legs)
    payer = to_bool_list(payer)
    return ql.Swap(legs, payer)


@xlo.func(
    help="Get the number of legs in a swap.",
    args={
        "swap": "The swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapNumberOfLegs(swap: ql.Swap, trigger=None) -> int:
    return swap.numberOfLegs()


@xlo.func(
    help="Get the start date of a swap.",
    args={
        "swap": "The swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapStartDate(swap: ql.Swap, trigger=None) -> ql.Date:
    return swap.startDate()


@xlo.func(
    help="Get the maturity date of a swap.",
    args={
        "swap": "The swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapMaturityDate(swap: ql.Swap, trigger=None) -> ql.Date:
    return swap.maturityDate()


@xlo.func(
    help="Get a specific leg of a swap.",
    args={
        "swap": "The swap object.",
        "i": "The index of the leg.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapLeg(swap: ql.Swap, i: int, trigger=None) -> ql.Leg:
    return swap.leg(i)


@xlo.func(
    help="Get the NPV of a specific leg of a swap.",
    args={
        "swap": "The swap object.",
        "j": "The index of the leg.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapLegNPV(swap: ql.Swap, j: int, trigger=None) -> float:
    return swap.legNPV(j)


@xlo.func(
    help="Get the basis point value (BPS) of a specific leg of a swap.",
    args={
        "swap": "The swap object.",
        "k": "The index of the leg.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapLegBPS(swap: ql.Swap, k: int, trigger=None) -> float:
    return swap.legBPS(k)


@xlo.func(
    help="Get the start discounts of a specific leg of a swap.",
    args={
        "swap": "The swap object.",
        "j": "The index of the leg.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapStartDiscounts(swap: ql.Swap, j: int, trigger=None) -> float:
    return swap.startDiscounts(j)


@xlo.func(
    help="Get the end discounts of a specific leg of a swap.",
    args={
        "swap": "The swap object.",
        "j": "The index of the leg.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapEndDiscounts(swap: ql.Swap, j: int, trigger=None) -> float:
    return swap.endDiscounts(j)


@xlo.func(
    help="Get the NPV date discount of a swap.",
    args={
        "swap": "The swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapNpvDateDiscount(swap: ql.Swap, trigger=None) -> float:
    return swap.npvDateDiscount()


@xlo.func(
    help="Check if a specific leg of a swap is a payer.",
    args={
        "swap": "The swap object.",
        "j": "The index of the leg.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapPayer(swap: ql.Swap, j: int, trigger=None) -> bool:
    return swap.payer(j)


@xlo.func(
    help="Get the type of the swap (Payer or Receiver).",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapType(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
):
    return first_key(QL_SWAP_TYPE, swap.type())


@xlo.func(
    help="Get the nominal amount.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapNominal(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> float:
    return swap.nominal()


@xlo.func(
    help="Get the nominal amounts.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapNominals(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> list:
    return swap.nominals()


@xlo.func(
    help="Get the fixed nominal amounts.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFixedNominals(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> list:
    return swap.fixedNominals()


@xlo.func(
    help="Get the fixed schedule.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFixedSchedule(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> ql.Schedule:
    return swap.fixedSchedule()


@xlo.func(
    help="Get the fixed rate.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFixedRate(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> float:
    return swap.fixedRate()


@xlo.func(
    help="Get the fixed day count.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFixedDayCount(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> ql.DayCounter:
    return swap.fixedDayCount()


@xlo.func(
    help="Get the floating nominal amounts.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFloatingNominals(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> list:
    return swap.floatingNominals()


@xlo.func(
    help="Get the floating schedule.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFloatingSchedule(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> ql.Schedule:
    return swap.floatingSchedule()


@xlo.func(
    help="Get the Ibor index.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapIborIndex(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> ql.IborIndex:
    return swap.iborIndex()


@xlo.func(
    help="Get the spread.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapSpread(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> float:
    return swap.spread()


@xlo.func(
    help="Get the floating day count.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFloatingDayCount(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> ql.DayCounter:
    return swap.floatingDayCount()


@xlo.func(
    help="Get the payment convention.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapPaymentConvention(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
):
    return first_key(QL_BUSINESSDAYCONVENTION, swap.paymentConvention())


@xlo.func(
    help="Get the fixed leg.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFixedLeg(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> ql.Leg:
    return swap.fixedLeg()


@xlo.func(
    help="Get the floating leg.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFloatingLeg(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> ql.Leg:
    return swap.floatingLeg()


@xlo.func(
    help="Get the fixed leg basis point value (BPS).",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFixedLegBPS(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> float:
    return swap.fixedLegBPS()


@xlo.func(
    help="Get the fixed leg net present value (NPV).",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFixedLegNPV(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> float:
    return swap.fixedLegNPV()


@xlo.func(
    help="Get the fair rate.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFairRate(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> float:
    return swap.fairRate()


@xlo.func(
    help="Get the floating leg basis point value (BPS).",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFloatingLegBPS(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> float:
    return swap.floatingLegBPS()


@xlo.func(
    help="Get the floating leg net present value (NPV).",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFloatingLegNPV(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> float:
    return swap.floatingLegNPV()


@xlo.func(
    help="Get the fair spread.",
    args={
        "swap": "The FixedVsFloatingSwap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedVsFloatingSwapFairSpread(
    swap: ql.FixedVsFloatingSwap,
    trigger=None,
) -> float:
    return swap.fairSpread()


@xlo.func(
    help="Create a QuantLib VanillaSwap object.",
    args={
        "type": "The type of the swap (Payer or Receiver).",
        "nominal": "The nominal amount of the swap.",
        "fixed_schedule": "The schedule for fixed leg payments.",
        "fixed_rate": "The fixed rate for the fixed leg.",
        "fixed_day_count": "The day counter for the fixed leg.",
        "float_schedule": "The schedule for floating leg payments.",
        "index": "The index for the floating leg.",
        "spread": "The spread for the floating leg.",
        "floating_day_count": "The day counter for the floating leg.",
        "payment_convention": "The business day convention for payments (default: Following).",
        "with_indexed_coupons": "Whether to use indexed coupons (default: None).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlVanillaSwap(
    type: qSwapType,
    nominal: float,
    fixed_schedule: ql.Schedule,
    fixed_rate: float,
    fixed_day_count: qDayCounter,
    float_schedule: ql.Schedule,
    index: ql.IborIndex,
    spread: float,
    floating_day_count: qDayCounter,
    payment_convention: qBusinessDayConvention = ql.Following,  # TODO default value
    with_indexed_coupons: Optional[bool] = None,
    trigger=None,
) -> ql.VanillaSwap:
    return ql.VanillaSwap(
        type,
        nominal,
        fixed_schedule,
        fixed_rate,
        fixed_day_count,
        float_schedule,
        index,
        spread,
        floating_day_count,
        payment_convention,
        with_indexed_coupons,
    )


@xlo.func(
    help="Create a QuantLib VanillaSwap object using the MakeVanillaSwap function.",
    args={
        "swap_tenor": "The tenor of the swap.",
        "ibor_index": "The Ibor index.",
        "fixed_rate": "The fixed rate (default: None).",
        "forward_start": "The forward start period (default: 0 Days).",
        "receive_fixed": "Whether to receive fixed (default: None).",
        "swap_type": "The swap type (default: None).",
        "nominal": "The nominal amount (default: None).",
        "settlement_days": "The number of settlement days (default: None).",
        "effective_date": "The effective date (default: None).",
        "termination_date": "The termination date (default: None).",
        "date_generation_rule": "The date generation rule (default: None).",
        "payment_convention": "The payment convention (default: None).",
        "fixed_leg_tenor": "The fixed leg tenor (default: None).",
        "fixed_leg_calendar": "The fixed leg calendar (default: None).",
        "fixed_leg_convention": "The fixed leg convention (default: None).",
        "fixed_leg_termination_date_convention": "The fixed leg termination date convention (default: None).",
        "fixed_leg_date_gen_rule": "The fixed leg date generation rule (default: None).",
        "fixed_leg_end_of_month": "Whether the fixed leg end of month (default: None).",
        "fixed_leg_first_date": "The fixed leg first date (default: None).",
        "fixed_leg_next_to_last_date": "The fixed leg next to last date (default: None).",
        "fixed_leg_day_count": "The fixed leg day count (default: None).",
        "floating_leg_tenor": "The floating leg tenor (default: None).",
        "floating_leg_calendar": "The floating leg calendar (default: None).",
        "floating_leg_convention": "The floating leg convention (default: None).",
        "floating_leg_termination_date_convention": "The floating leg termination date convention (default: None).",
        "floating_leg_date_gen_rule": "The floating leg date generation rule (default: None).",
        "floating_leg_end_of_month": "Whether the floating leg end of month (default: None).",
        "floating_leg_first_date": "The floating leg first date (default: None).",
        "floating_leg_next_to_last_date": "The floating leg next to last date (default: None).",
        "floating_leg_day_count": "The floating leg day count (default: None).",
        "floating_leg_spread": "The floating leg spread (default: None).",
        "discounting_term_structure": "The discounting term structure (default: None).",
        "pricing_engine": "The pricing engine (default: None).",
        "indexed_coupons": "Whether to use indexed coupons (default: None).",
        "at_par_coupons": "Whether to use at par coupons (default: None).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMakeVanillaSwap(
    swap_tenor: qPeriod,
    ibor_index: ql.IborIndex,
    fixed_rate=None,
    forward_start: qPeriod = ql.Period(0, ql.Days),
    receive_fixed=None,
    swap_type=None,
    nominal=None,
    settlement_days=None,
    effective_date=None,
    termination_date=None,
    date_generation_rule=None,
    payment_convention=None,
    fixed_leg_tenor=None,
    fixed_leg_calendar=None,
    fixed_leg_convention=None,
    fixed_leg_termination_date_convention=None,
    fixed_leg_date_gen_rule=None,
    fixed_leg_end_of_month=None,
    fixed_leg_first_date=None,
    fixed_leg_next_to_last_date=None,
    fixed_leg_day_count=None,
    floating_leg_tenor=None,
    floating_leg_calendar=None,
    floating_leg_convention=None,
    floating_leg_termination_date_convention=None,
    floating_leg_date_gen_rule=None,
    floating_leg_end_of_month=None,
    floating_leg_first_date=None,
    floating_leg_next_to_last_date=None,
    floating_leg_day_count=None,
    floating_leg_spread=None,
    discounting_term_structure=None,
    pricing_engine=None,
    indexed_coupons=None,
    at_par_coupons=None,
    trigger=None,
):

    if fixed_rate is not None:
        fixed_rate = float(fixed_rate)
    if receive_fixed:
        receive_fixed = bool(receive_fixed)
    if swap_type is not None:
        swap_type = qSwapType.__wrapped__(swap_type)
    if nominal is not None:
        nominal = float(nominal)
    if settlement_days is not None:
        settlement_days = int(settlement_days)
    if effective_date is not None:
        effective_date = qDate.__wrapped__(effective_date)
    if termination_date is not None:
        termination_date = qDate.__wrapped__(termination_date)
    if date_generation_rule is not None:
        date_generation_rule = qDateGenerationRule.__wrapped__(date_generation_rule)
    if payment_convention is not None:
        payment_convention = qBusinessDayConvention.__wrapped__(payment_convention)
    if fixed_leg_tenor is not None:
        fixed_leg_tenor = qPeriod.__wrapped__(fixed_leg_tenor)
    if fixed_leg_calendar is not None:
        fixed_leg_calendar = qCalendar.__wrapped__(fixed_leg_calendar)
    if fixed_leg_convention is not None:
        fixed_leg_convention = qBusinessDayConvention.__wrapped__(fixed_leg_convention)
    if fixed_leg_termination_date_convention is not None:
        fixed_leg_termination_date_convention = qBusinessDayConvention.__wrapped__(
            fixed_leg_termination_date_convention
        )
    if fixed_leg_date_gen_rule is not None:
        fixed_leg_date_gen_rule = qDateGenerationRule.__wrapped__(
            fixed_leg_date_gen_rule
        )
    if fixed_leg_end_of_month is not None:
        fixed_leg_end_of_month = bool(fixed_leg_end_of_month)
    if fixed_leg_first_date is not None:
        fixed_leg_first_date = qDate.__wrapped__(fixed_leg_first_date)
    if fixed_leg_next_to_last_date is not None:
        fixed_leg_next_to_last_date = qDate.__wrapped__(fixed_leg_next_to_last_date)
    if fixed_leg_day_count is not None:
        fixed_leg_day_count = qDayCounter.__wrapped__(fixed_leg_day_count)
    if floating_leg_tenor is not None:
        floating_leg_tenor = qPeriod.__wrapped__(floating_leg_tenor)
    if floating_leg_calendar is not None:
        floating_leg_calendar = qCalendar.__wrapped__(floating_leg_calendar)
    if floating_leg_convention is not None:
        floating_leg_convention = qBusinessDayConvention.__wrapped__(
            floating_leg_convention
        )
    if floating_leg_termination_date_convention is not None:
        floating_leg_termination_date_convention = qBusinessDayConvention.__wrapped__(
            floating_leg_termination_date_convention
        )
    if floating_leg_date_gen_rule is not None:
        floating_leg_date_gen_rule = qDateGenerationRule.__wrapped__(
            floating_leg_date_gen_rule
        )
    if floating_leg_end_of_month is not None:
        floating_leg_end_of_month = bool(floating_leg_end_of_month)
    if floating_leg_first_date is not None:
        floating_leg_first_date = qDate.__wrapped__(floating_leg_first_date)
    if floating_leg_next_to_last_date is not None:
        floating_leg_next_to_last_date = qDate.__wrapped__(
            floating_leg_next_to_last_date
        )
    if floating_leg_day_count is not None:
        floating_leg_day_count = qDayCounter.__wrapped__(floating_leg_day_count)
    if floating_leg_spread is not None:
        floating_leg_spread = float(floating_leg_spread)
    if discounting_term_structure is not None:
        discounting_term_structure = discounting_term_structure
    if pricing_engine is not None:
        pricing_engine = pricing_engine
    if indexed_coupons is not None:
        indexed_coupons = bool(indexed_coupons)
    if at_par_coupons is not None:
        at_par_coupons = bool(at_par_coupons)

    _MAKEVANILLA_KWARGS = {
        "receive_fixed": "receiveFixed",
        "swap_type": "swapType",
        "nominal": "nominal",
        "settlement_days": "settlementDays",
        "effective_date": "effectiveDate",
        "termination_date": "terminationDate",
        "date_generation_rule": "dateGenerationRule",
        "payment_convention": "paymentConvention",
        "fixed_leg_tenor": "fixedLegTenor",
        "fixed_leg_calendar": "fixedLegCalendar",
        "fixed_leg_convention": "fixedLegConvention",
        "fixed_leg_termination_date_convention": "fixedLegTerminationDateConvention",
        "fixed_leg_end_of_month": "fixedLegEndOfMonth",
        "fixed_leg_first_date": "fixedLegFirstDate",
        "fixed_leg_next_to_last_date": "fixedLegNextToLastDate",
        "fixed_leg_day_count": "fixedLegDayCount",
        "floating_leg_tenor": "floatingLegTenor",
        "floating_leg_calendar": "floatingLegCalendar",
        "floating_leg_convention": "floatingLegConvention",
        "floating_leg_termination_date_convention": "floatingLegTerminationDateConvention",
        "floating_leg_end_of_month": "floatingLegEndOfMonth",
        "floating_leg_first_date": "floatingLegFirstDate",
        "floating_leg_next_to_last_date": "floatingLegNextToLastDate",
        "floating_leg_day_count": "floatingLegDayCount",
        "floating_leg_spread": "floatingLegSpread",
        "discounting_term_structure": "discountingTermStructure",
        "pricing_engine": "pricingEngine",
        "at_par_coupons": "atParCoupons",
    }

    kwargs = {}
    for param_name, kw_name in _MAKEVANILLA_KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.MakeVanillaSwap(
        swap_tenor, ibor_index, fixed_rate, forward_start, **kwargs
    )


@xlo.func(
    help="Create a QuantLib NonstandardSwap object.",
    args={
        "type": "The type of the swap (Payer or Receiver).",
        "fixed_nominal": "The list of fixed nominal amounts.",
        "floating_nominal": "The list of floating nominal amounts.",
        "fixed_schedule": "The schedule for fixed leg payments.",
        "fixed_rate": "The list of fixed rates.",
        "fixed_day_count": "The day counter for the fixed leg.",
        "float_schedule": "The schedule for floating leg payments.",
        "index": "The index for the floating leg.",
        "gearing": "The list of gearings for the floating leg.",
        "spread": "The list of spreads for the floating leg.",
        "float_day_count": "The day counter for the floating leg.",
        "intermediate_capital_exchange": "Whether to include intermediate capital exchange (default: False).",
        "final_capital_exchange": "Whether to include final capital exchange (default: False).",
        "payment_convention": "The business day convention for payments (default: Following).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwap(
    type: qSwapType,
    fixed_nominal: xlo.Array(dims=1),
    floating_nominal: xlo.Array(dims=1),
    fixed_schedule: ql.Schedule,
    fixed_rate: xlo.Array(dims=1),
    fixed_day_count: qDayCounter,
    float_schedule: ql.Schedule,
    index: ql.IborIndex,
    gearing: xlo.Array(dims=1),
    spread: xlo.Array(dims=1),
    float_day_count: qDayCounter,
    intermediate_capital_exchange: bool = False,
    final_capital_exchange: bool = False,
    payment_convention: qBusinessDayConvention = ql.Following,
    trigger=None,
) -> ql.NonstandardSwap:
    return ql.NonstandardSwap(
        type,
        to_float_list(fixed_nominal),
        to_float_list(floating_nominal),
        fixed_schedule,
        to_float_list(fixed_rate),
        fixed_day_count,
        float_schedule,
        index,
        to_float_list(gearing),
        to_float_list(spread),
        float_day_count,
        intermediate_capital_exchange,
        final_capital_exchange,
        payment_convention,
    )


@xlo.func(
    help="Get the type of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapType(swap: ql.NonstandardSwap, trigger=None):
    return first_key(QL_SWAP_TYPE, swap.type())


@xlo.func(
    help="Get the fixed nominal amounts of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapFixedNominal(swap: ql.NonstandardSwap, trigger=None) -> list:
    return swap.fixedNominal()


@xlo.func(
    help="Get the floating nominal amounts of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapFloatingNominal(swap: ql.NonstandardSwap, trigger=None) -> list:
    return swap.floatingNominal()


@xlo.func(
    help="Get the fixed schedule of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapFixedSchedule(
    swap: ql.NonstandardSwap, trigger=None
) -> ql.Schedule:
    return swap.fixedSchedule()


@xlo.func(
    help="Get the fixed rates of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapFixedRate(swap: ql.NonstandardSwap, trigger=None) -> list:
    return swap.fixedRate()


@xlo.func(
    help="Get the fixed day count of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapFixedDayCount(
    swap: ql.NonstandardSwap, trigger=None
) -> qDayCounter:
    return swap.fixedDayCount()


@xlo.func(
    help="Get the floating schedule of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapFloatingSchedule(
    swap: ql.NonstandardSwap, trigger=None
) -> ql.Schedule:
    return swap.floatingSchedule()


@xlo.func(
    help="Get the Ibor index of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapIborIndex(swap: ql.NonstandardSwap, trigger=None) -> ql.IborIndex:
    return swap.iborIndex()


@xlo.func(
    help="Get the spread of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapSpread(swap: ql.NonstandardSwap, trigger=None) -> float:
    return swap.spread()


@xlo.func(
    help="Get the gearing of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapGearing(swap: ql.NonstandardSwap, trigger=None) -> float:
    return swap.gearing()


@xlo.func(
    help="Get the spreads of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapSpreads(swap: ql.NonstandardSwap, trigger=None) -> list:
    return swap.spreads()


@xlo.func(
    help="Get the gearings of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapGearings(swap: ql.NonstandardSwap, trigger=None) -> list:
    return swap.gearings()


@xlo.func(
    help="Get the floating day count of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapFloatingDayCount(
    swap: ql.NonstandardSwap, trigger=None
) -> ql.DayCounter:
    return swap.floatingDayCount()


@xlo.func(
    help="Get the payment convention of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapPaymentConvention(swap: ql.NonstandardSwap, trigger=None):
    return first_key(QL_BUSINESSDAYCONVENTION, swap.paymentConvention())


@xlo.func(
    help="Get the fixed leg of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapFixedLeg(swap: ql.NonstandardSwap, trigger=None) -> ql.Leg:
    return swap.fixedLeg()


@xlo.func(
    help="Get the floating leg of a nonstandard swap.",
    args={
        "swap": "The nonstandard swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwapFloatingLeg(swap: ql.NonstandardSwap, trigger=None) -> ql.Leg:
    return swap.floatingLeg()


@xlo.func(
    help="Create a QuantLib DiscountingSwapEngine object.",
    args={
        "discount_curve": "The yield term structure for discounting.",
        "include_settlement_date_flows": "Whether to include settlement date flows (default: False).",
        "settlement_date": "The settlement date (default: today).",
        "npv_date": "The NPV date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDiscountingSwapEngine(
    discount_curve: ql.YieldTermStructureHandle,
    include_settlement_date_flows: bool = False,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> ql.DiscountingSwapEngine:
    return ql.DiscountingSwapEngine(
        discount_curve,
        include_settlement_date_flows,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Create a QuantLib DiscountingSwapEngine object.",
    args={
        "discount_curve": "The yield term structure for discounting.",
        "settlement_date": "The settlement date (default: today).",
        "npv_date": "The NPV date (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDiscountingSwapEngine2(
    discount_curve: ql.YieldTermStructureHandle,
    settlement_date: qDate = ql.Date(),
    npv_date: qDate = ql.Date(),
    trigger=None,
) -> ql.DiscountingSwapEngine:
    return ql.DiscountingSwapEngine(
        discount_curve,
        None,
        settlement_date,
        npv_date,
    )


@xlo.func(
    help="Create a QuantLib AssetSwap object.",
    args={
        "pay_fixed_rate": "Whether the fixed rate is paid.",
        "bond": "The bond object.",
        "bond_clean_price": "The clean price of the bond.",
        "index": "The index for the floating leg.",
        "spread": "The spread for the floating leg.",
        "float_schedule": "The schedule for floating leg payments (default: empty schedule).",
        "floating_day_count": "The day counter for the floating leg (default: act/360).",
        "par_asset_swap": "Whether the asset swap is par (default: True).",
        "gearing": "The gearing for the floating leg (default: 1.0).",
        "non_par_repayment": "The non-par repayment amount (default: 0).",
        "deal_maturity": "The maturity date of the deal (default: today).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAssetSwap(
    pay_fixed_rate: bool,
    bond: ql.Bond,
    bond_clean_price: float,
    index: ql.IborIndex,
    spread: float,
    float_schedule: ql.Schedule = ql.Schedule(),
    floating_day_count: qDayCounter = ql.Actual360(),  # TODO default value
    par_asset_swap: bool = True,
    gearing: float = 1.0,
    non_par_repayment: float = 0,  # TODO default value
    deal_maturity: qDate = ql.Date(),
    trigger=None,
) -> ql.AssetSwap:
    return ql.AssetSwap(
        pay_fixed_rate,
        bond,
        bond_clean_price,
        index,
        spread,
        float_schedule,
        floating_day_count,
        par_asset_swap,
        gearing,
        non_par_repayment,
        deal_maturity,
    )


@xlo.func(
    help="Get the fair clean price of an asset swap.",
    args={
        "swap": "The asset swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAssetSwapFairCleanPrice(swap: ql.AssetSwap, trigger=None) -> float:
    return swap.fairCleanPrice()


@xlo.func(
    help="Get the fair spread of an asset swap.",
    args={
        "swap": "The asset swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAssetSwapFairSpread(swap: ql.AssetSwap, trigger=None) -> float:
    return swap.fairSpread()


# TODO to test when optional fields gaps and floors are passed
@xlo.func(
    help="Create a QuantLib FloatFloatSwap object.",
    args={
        "type": "The type of the swap (Payer or Receiver).",
        "nominal1": "The list of nominal amounts for the first leg.",
        "nominal2": "The list of nominal amounts for the second leg.",
        "schedule1": "The schedule for the first leg payments.",
        "index1": "The index for the first leg.",
        "day_count1": "The day counter for the first leg.",
        "schedule2": "The schedule for the second leg payments.",
        "index2": "The index for the second leg.",
        "day_count2": "The day counter for the second leg.",
        "intermediate_capital_exchange": "Whether to include intermediate capital exchange (default: False).",
        "final_capital_exchange": "Whether to include final capital exchange (default: False).",
        "gearing1": "The list of gearings for the first leg (default: None).",
        "spread1": "The list of spreads for the first leg (default: None).",
        "capped_rate1": "The list of capped rates for the first leg (default: None).",
        "floored_rate1": "The list of floored rates for the first leg (default: None).",
        "gearing2": "The list of gearings for the second leg (default: None).",
        "spread2": "The list of spreads for the second leg (default: None).",
        "capped_rate2": "The list of capped rates for the second leg (default: None).",
        "floored_rate2": "The list of floored rates for the second leg (default: None).",
        "payment_convention1": "The business day convention for the first leg payments (default: Following).",
        "payment_convention2": "The business day convention for the second leg payments (default: Following).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatFloatSwap(
    type: qSwapType,
    nominal1: xlo.Array(dims=1),
    nominal2: xlo.Array(dims=1),
    schedule1: ql.Schedule,
    index1: ql.InterestRateIndex,
    day_count1: qDayCounter,
    schedule2: ql.Schedule,
    index2: ql.InterestRateIndex,
    day_count2: qDayCounter,
    intermediate_capital_exchange: bool = False,
    final_capital_exchange: bool = False,
    gearing1: xlo.Array(dims=1) = None,
    spread1: xlo.Array(dims=1) = None,
    capped_rate1: xlo.Array(dims=1) = None,
    floored_rate1: xlo.Array(dims=1) = None,
    gearing2: xlo.Array(dims=1) = None,
    spread2: xlo.Array(dims=1) = None,
    capped_rate2: xlo.Array(dims=1) = None,
    floored_rate2: xlo.Array(dims=1) = None,
    payment_convention1: qBusinessDayConvention = ql.Following,
    payment_convention2: qBusinessDayConvention = ql.Following,
    trigger=None,
) -> ql.FloatFloatSwap:
    return ql.FloatFloatSwap(
        type,
        to_float_list(nominal1),
        to_float_list(nominal2),
        schedule1,
        index1,
        day_count1,
        schedule2,
        index2,
        day_count2,
        intermediate_capital_exchange,
        final_capital_exchange,
        to_float_list(gearing1),
        to_float_list(spread1),
        to_float_list(capped_rate1),
        to_float_list(floored_rate1),
        to_float_list(gearing2),
        to_float_list(spread2),
        to_float_list(capped_rate2),
        to_float_list(floored_rate2),
        payment_convention1,
        payment_convention2,
    )


@xlo.func(
    help="Create a QuantLib OvernightIndexedSwap object.",
    args={
        "type": "The type of the swap (Payer or Receiver).",
        "nominal": "The nominal amount of the swap.",
        "schedule": "The schedule for payments.",
        "fixed_rate": "The fixed rate.",
        "fixed_dc": "The day counter for the fixed leg.",
        "index": "The overnight index.",
        "spread": "The spread for the floating leg (default: 0.0).",
        "payment_lag": "The payment lag (default: 0).",
        "payment_adjustment": "The business day convention for payments (default: Following).",
        "payment_calendar": "The calendar for payments (default: null calendar).",
        "telescopic_value_dates": "Whether to use telescopic value dates (default: False).",
        "averaging_method": "The averaging method for the floating leg (default: Compound).",
        "lookback_days": "The number of lookback days (default: 0).",
        "lockout_days": "The number of lockout days (default: 0).",
        "apply_observation_shift": "Whether to apply observation shift (default: False).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwap(
    type: qSwapType,
    nominal: float,
    schedule: ql.Schedule,
    fixed_rate: float,
    fixed_dc: qDayCounter,
    index: ql.OvernightIndex,
    spread: float = 0.0,
    payment_lag: int = 0,
    payment_adjustment: qBusinessDayConvention = ql.Following,
    payment_calendar: qCalendar = ql.NullCalendar(),  # TODO default value
    telescopic_value_dates: bool = False,
    averaging_method: qRateAveragingType = ql.RateAveraging.Compound,
    lookback_days: int = 0,  # TODO default value,
    lockout_days: int = 0,
    apply_observation_shift: bool = False,
    trigger=None,
) -> ql.OvernightIndexedSwap:
    return ql.OvernightIndexedSwap(
        type,
        nominal,
        schedule,
        fixed_rate,
        fixed_dc,
        index,
        spread,
        payment_lag,
        payment_adjustment,
        payment_calendar,
        telescopic_value_dates,
        averaging_method,
        lookback_days,
        lockout_days,
        apply_observation_shift,
    )


@xlo.func(
    help="Create a QuantLib OvernightIndexedSwap object.",
    args={
        "type": "The type of the swap (Payer or Receiver).",
        "fixed_nominals": "The list of fixed nominal amounts.",
        "fixed_schedule": "The schedule for fixed leg payments.",
        "fixed_rate": "The fixed rate.",
        "fixed_dc": "The day counter for the fixed leg.",
        "overnight_nominals": "The list of overnight nominal amounts.",
        "overnight_schedule": "The schedule for overnight leg payments.",
        "overnight_index": "The overnight index.",
        "spread": "The spread for the overnight leg (default: 0.0).",
        "payment_lag": "The payment lag (default: 0).",
        "payment_adjustment": "The business day convention for payments (default: Following).",
        "payment_calendar": "The calendar for payments (default: null calendar).",
        "telescopic_value_dates": "Whether to use telescopic value dates (default: False).",
        "averaging_method": "The averaging method for the overnight leg (default: Compound).",
        "lookback_days": "The number of lookback days (default: 0).",
        "lockout_days": "The number of lockout days (default: 0).",
        "apply_observation_shift": "Whether to apply observation shift (default: False).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwap2(
    type: qSwapType,
    fixed_nominals: xlo.Array(dims=1),
    fixed_schedule: ql.Schedule,
    fixed_rate: float,
    fixed_dc: qDayCounter,
    overnight_nominals: xlo.Array(dims=1),
    overnight_schedule: ql.Schedule,
    overnight_index: ql.OvernightIndex,
    spread: float = 0.0,
    payment_lag: int = 0,
    payment_adjustment: qBusinessDayConvention = ql.Following,
    payment_calendar: qCalendar = ql.NullCalendar(),  # TODO default value
    telescopic_value_dates: bool = False,
    averaging_method: qRateAveragingType = ql.RateAveraging.Compound,
    lookback_days: int = 0,  # TODO default value
    lockout_days: int = 0,
    apply_observation_shift: bool = False,
    trigger=None,
) -> ql.OvernightIndexedSwap:
    return ql.OvernightIndexedSwap(
        type,
        to_float_list(fixed_nominals),
        fixed_schedule,
        fixed_rate,
        fixed_dc,
        to_float_list(overnight_nominals),
        overnight_schedule,
        overnight_index,
        spread,
        payment_lag,
        payment_adjustment,
        payment_calendar,
        telescopic_value_dates,
        averaging_method,
        lookback_days,
        lockout_days,
        apply_observation_shift,
    )


@xlo.func(
    help="Get the overnight leg BPS of an overnight indexed swap.",
    args={
        "swap": "The overnight indexed swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwapOvernightLegBPS(
    swap: ql.OvernightIndexedSwap, trigger=None
) -> float:
    return swap.overnightLegBPS()


@xlo.func(
    help="Get the overnight leg NPV of an overnight indexed swap.",
    args={
        "swap": "The overnight indexed swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwapOvernightLegNPV(
    swap: ql.OvernightIndexedSwap, trigger=None
) -> float:
    return swap.overnightLegNPV()


@xlo.func(
    help="Get the payment frequency of an overnight indexed swap.",
    args={
        "swap": "The overnight indexed swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwapPaymentFrequency(swap: ql.OvernightIndexedSwap, trigger=None):
    return first_key(QL_FREQUENCY, swap.paymentFrequency())


@xlo.func(
    help="Get the overnight index of an overnight indexed swap.",
    args={
        "swap": "The overnight indexed swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwapOvernightIndex(
    swap: ql.OvernightIndexedSwap, trigger=None
) -> ql.OvernightIndex:
    return swap.overnightIndex()


@xlo.func(
    help="Get the overnight leg of an overnight indexed swap.",
    args={
        "swap": "The overnight indexed swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwapOvernightLeg(
    swap: ql.OvernightIndexedSwap, trigger=None
) -> ql.Leg:
    return swap.overnightLeg()


@xlo.func(
    help="Get the averaging method of an overnight indexed swap.",
    args={
        "swap": "The overnight indexed swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwapAveragingMethod(swap: ql.OvernightIndexedSwap, trigger=None):
    return first_key(QL_RATE_AVERAGING_TYPE, swap.averagingMethod())


@xlo.func(
    help="Get the lookback days of an overnight indexed swap.",
    args={
        "swap": "The overnight indexed swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwapLookbackDays(
    swap: ql.OvernightIndexedSwap, trigger=None
) -> int:
    return swap.lookbackDays()


@xlo.func(
    help="Get the lockout days of an overnight indexed swap.",
    args={
        "swap": "The overnight indexed swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwapLockoutDays(
    swap: ql.OvernightIndexedSwap, trigger=None
) -> int:
    return swap.lockoutDays()


@xlo.func(
    help="Check if observation shift is applied in an overnight indexed swap.",
    args={
        "swap": "The overnight indexed swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwapApplyObservationShift(
    swap: ql.OvernightIndexedSwap, trigger=None
) -> bool:
    return swap.applyObservationShift()


@xlo.func(
    help="Create a QuantLib OvernightIndexedSwap object using the MakeOIS function.",
    args={
        "swap_tenor": "The tenor of the swap.",
        "overnight_index": "The overnight index.",
        "fixed_rate": "The fixed rate (default: None).",
        "fwd_start": "The forward start period (default: 0 days).",
        "receive_fixed": "Whether to receive fixed (default: None).",
        "swap_type": "The swap type (default: None).",
        "nominal": "The nominal amount (default: None).",
        "settlement_days": "The number of settlement days (default: None).",
        "effective_date": "The effective date (default: None).",
        "termination_date": "The termination date (default: None).",
        "date_generation_rule": "The date generation rule (default: None).",
        "fixed_leg_rule": "The fixed leg date generation rule (default: None).",
        "overnight_leg_rule": "The overnight leg date generation rule (default: None).",
        "payment_frequency": "The payment frequency (default: None).",
        "fixed_leg_payment_frequency": "The fixed leg payment frequency (default: None).",
        "overnight_leg_payment_frequency": "The overnight leg payment frequency (default: None).",
        "payment_adjustment_convention": "The payment adjustment convention (default: None).",
        "payment_lag": "The payment lag (default: None).",
        "payment_calendar": "The payment calendar (default: None).",
        "calendar": "The calendar (default: None).",
        "fixed_leg_calendar": "The fixed leg calendar (default: None).",
        "overnight_leg_calendar": "The overnight leg calendar (default: None).",
        "convention": "The business day convention (default: None).",
        "fixed_leg_convention": "The fixed leg business day convention (default: None).",
        "overnight_leg_convention": "The overnight leg business day convention (default: None).",
        "termination_date_convention": "The termination date convention (default: None).",
        "fixed_leg_termination_date_convention": "The fixed leg termination date convention (default: None).",
        "overnight_leg_termination_date_convention": "The overnight leg termination date convention (default: None).",
        "end_of_month": "Whether to end of month (default: None).",
        "fixed_leg_end_of_month": "Whether the fixed leg end of month (default: None).",
        "overnight_leg_end_of_month": "Whether the overnight leg end of month (default: None).",
        "fixed_leg_day_count": "The fixed leg day count (default: None).",
        "overnight_leg_spread": "The overnight leg spread (default: None).",
        "discounting_term_structure": "The discounting term structure (default: None).",
        "telescopic_value_dates": "Whether to use telescopic value dates (default: None).",
        "averaging_method": "The averaging method (default: None).",
        "lookback_days": "The number of lookback days (default: None).",
        "lockout_days": "The number of lockout days (default: None).",
        "apply_observation_shift": "Whether to apply observation shift (default: None).",
        "pricing_engine": "The pricing engine (default: None).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMakeOIS(
    swap_tenor: qPeriod,
    overnight_index: ql.OvernightIndex,
    fixed_rate: float = None,
    fwd_start: qPeriod = ql.Period(0, ql.Days),
    receive_fixed=None,  # default TRUE
    swap_type=None,
    nominal=None,
    settlement_days=None,
    effective_date=None,
    termination_date=None,
    date_generation_rule=None,
    fixed_leg_rule=None,
    overnight_leg_rule=None,
    payment_frequency=None,
    fixed_leg_payment_frequency=None,
    overnight_leg_payment_frequency=None,
    payment_adjustment_convention=None,
    payment_lag=None,
    payment_calendar=None,
    calendar=None,
    fixed_leg_calendar=None,
    overnight_leg_calendar=None,
    convention=None,
    fixed_leg_convention=None,
    overnight_leg_convention=None,
    termination_date_convention=None,
    fixed_leg_termination_date_convention=None,
    overnight_leg_termination_date_convention=None,
    end_of_month=None,  # default TRUE
    fixed_leg_end_of_month=None,  # default TRUE
    overnight_leg_end_of_month=None,  # default TRUE
    fixed_leg_day_count=None,
    overnight_leg_spread=None,
    discounting_term_structure=None,
    telescopic_value_dates=None,
    averaging_method=None,
    lookback_days=None,
    lockout_days=None,
    # apply_observation_shift=None, not supported
    pricing_engine=None,
    trigger=None,
):
    if fixed_rate is not None:
        fixed_rate = float(fixed_rate)
    if receive_fixed is not None:
        receive_fixed = bool(receive_fixed)
    if swap_type is not None:
        swap_type = qSwapType.__wrapped__(swap_type)
    if nominal is not None:
        nominal = float(nominal)
    if settlement_days is not None:
        settlement_days = int(settlement_days)
    if effective_date is not None:
        effective_date = qDate.__wrapped__(effective_date)
    if termination_date is not None:
        termination_date = qDate.__wrapped__(termination_date)
    if date_generation_rule is not None:
        date_generation_rule = qDateGenerationRule.__wrapped__(date_generation_rule)
    if fixed_leg_rule is not None:
        fixed_leg_rule = qDateGenerationRule.__wrapped__(fixed_leg_rule)
    if overnight_leg_rule is not None:
        overnight_leg_rule = qDateGenerationRule.__wrapped__(overnight_leg_rule)
    if payment_frequency is not None:
        payment_frequency = qFrequency.__wrapped__(payment_frequency)
    if fixed_leg_payment_frequency is not None:
        fixed_leg_payment_frequency = qFrequency.__wrapped__(
            fixed_leg_payment_frequency
        )
    if overnight_leg_payment_frequency is not None:
        overnight_leg_payment_frequency = qFrequency.__wrapped__(
            overnight_leg_payment_frequency
        )
    if payment_adjustment_convention is not None:
        payment_adjustment_convention = qBusinessDayConvention.__wrapped__(
            payment_adjustment_convention
        )
    if payment_lag is not None:
        payment_lag = int(payment_lag)
    if payment_calendar is not None:
        payment_calendar = qCalendar.__wrapped__(payment_calendar)
    if calendar is not None:
        calendar = qCalendar.__wrapped__(calendar)
    if fixed_leg_calendar is not None:
        fixed_leg_calendar = qCalendar.__wrapped__(fixed_leg_calendar)
    if overnight_leg_calendar is not None:
        overnight_leg_calendar = qCalendar.__wrapped__(overnight_leg_calendar)
    if convention is not None:
        convention = qBusinessDayConvention.__wrapped__(convention)
    if fixed_leg_convention is not None:
        fixed_leg_convention = qBusinessDayConvention.__wrapped__(fixed_leg_convention)
    if overnight_leg_convention is not None:
        overnight_leg_convention = qBusinessDayConvention.__wrapped__(
            overnight_leg_convention
        )
    if termination_date_convention is not None:
        termination_date_convention = qBusinessDayConvention.__wrapped__(
            termination_date_convention
        )
    if fixed_leg_termination_date_convention is not None:
        fixed_leg_termination_date_convention = qBusinessDayConvention.__wrapped__(
            fixed_leg_termination_date_convention
        )
    if overnight_leg_termination_date_convention is not None:
        overnight_leg_termination_date_convention = qBusinessDayConvention.__wrapped__(
            overnight_leg_termination_date_convention
        )
    if end_of_month is not None:
        end_of_month = bool(end_of_month)
    if fixed_leg_end_of_month is not None:
        fixed_leg_end_of_month = bool(fixed_leg_end_of_month)
    if overnight_leg_end_of_month is not None:
        overnight_leg_end_of_month = bool(overnight_leg_end_of_month)
    if fixed_leg_day_count is not None:
        fixed_leg_day_count = qDayCounter.__wrapped__(fixed_leg_day_count)
    if overnight_leg_spread is not None:
        overnight_leg_spread = float(overnight_leg_spread)
    if telescopic_value_dates is not None:
        telescopic_value_dates = bool(telescopic_value_dates)
    if averaging_method is not None:
        averaging_method = qRateAveragingType.__wrapped__(averaging_method)
    if lookback_days is not None:
        lookback_days = int(lookback_days)
    if lockout_days is not None:
        lockout_days = int(lockout_days)

    # Map kwargs for MakeOIS. Note: QuantLib.MakeOIS does not accept a
    # top-level `paymentConvention` keyword in this QuantLib version, so
    # we do NOT forward `payment_adjustment_convention` directly. Instead,
    # if the user provided a payment adjustment, apply it to the fixed
    # and overnight leg conventions below.
    _MAKEOIS_KWARGS = {
        "receive_fixed": "receiveFixed",
        "swap_type": "swapType",
        "nominal": "nominal",
        "settlement_days": "settlementDays",
        "effective_date": "effectiveDate",
        "termination_date": "terminationDate",
        "date_generation_rule": "dateGenerationRule",
        "fixed_leg_rule": "fixedLegRule",
        "overnight_leg_rule": "overnightLegRule",
        "payment_frequency": "paymentFrequency",
        "fixed_leg_payment_frequency": "fixedLegPaymentFrequency",
        "overnight_leg_payment_frequency": "overnightLegPaymentFrequency",
        "payment_lag": "paymentLag",
        "payment_calendar": "paymentCalendar",
        "calendar": "calendar",
        "fixed_leg_calendar": "fixedLegCalendar",
        "overnight_leg_calendar": "overnightLegCalendar",
        "convention": "convention",
        "fixed_leg_convention": "fixedLegConvention",
        "overnight_leg_convention": "overnightLegConvention",
        "termination_date_convention": "terminationDateConvention",
        "fixed_leg_termination_date_convention": "fixedLegTerminationDateConvention",
        "overnight_leg_termination_date_convention": "overnightLegTerminationDateConvention",
        "end_of_month": "endOfMonth",
        "fixed_leg_end_of_month": "fixedLegEndOfMonth",
        "overnight_leg_end_of_month": "overnightLegEndOfMonth",
        "fixed_leg_day_count": "fixedLegDayCount",
        "overnight_leg_spread": "overnightLegSpread",
        "discounting_term_structure": "discountingTermStructure",
        "telescopic_value_dates": "telescopicValueDates",
        "averaging_method": "averagingMethod",
        "lookback_days": "lookbackDays",
        "lockout_days": "lockoutDays",
        # do not forward "apply_observation_shift" ->  "observationShift" not supported
        "pricing_engine": "pricingEngine",
    }

    kwargs = {}
    for param_name, kw_name in _MAKEOIS_KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    # If a payment adjustment convention was provided, but per-leg conventions
    # were not, apply it to both legs so the user's intent is respected

    if payment_adjustment_convention is not None:
        if fixed_leg_convention is None:
            fixed_leg_convention = payment_adjustment_convention
            kwargs["fixedLegConvention"] = fixed_leg_convention
        if overnight_leg_convention is None:
            overnight_leg_convention = payment_adjustment_convention
            kwargs["overnightLegConvention"] = overnight_leg_convention

    return ql.MakeOIS(swap_tenor, overnight_index, fixed_rate, fwd_start, **kwargs)


@xlo.func(
    help="Create a QuantLib OvernightIndexedSwapIndex object.",
    args={
        "family_name": "The family name of the index.",
        "tenor": "The tenor of the index.",
        "settlement_days": "The number of settlement days.",
        "currency": "The currency of the index.",
        "overnight_index": "The overnight index.",
        "telescopic_value_dates": "Whether to use telescopic value dates (default: False).",
        "averaging_method": "The averaging method (default: Compound).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwapIndex(
    family_name: str,
    tenor: qPeriod,
    settlement_days: int,
    currency: qCurrency,
    overnight_index: ql.OvernightIndex,
    telescopic_value_dates: bool = False,
    averaging_method: qRateAveragingType = ql.RateAveraging.Compound,
    trigger=None,
) -> ql.OvernightIndexedSwapIndex:
    return ql.OvernightIndexedSwapIndex(
        family_name,
        tenor,
        settlement_days,
        currency,
        overnight_index,
        telescopic_value_dates,
        averaging_method,
    )


@xlo.func(
    help="Get the overnight index of an overnight indexed swap index.",
    args={
        "index": "The overnight indexed swap index object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwapIndexOvernightIndex(
    index: ql.OvernightIndexedSwapIndex, trigger=None
) -> ql.OvernightIndex:
    return index.overnightIndex()


@xlo.func(
    help="Get the underlying swap of an overnight indexed swap index.",
    args={
        "index": "The overnight indexed swap index object.",
        "fixing_date": "The fixing date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexedSwapIndexUnderlyingSwap(
    index: ql.OvernightIndexedSwapIndex, fixing_date: qDate, trigger=None
) -> ql.OvernightIndexedSwap:
    return index.underlyingSwap(fixing_date)


# TODO to test qlAsOvernightSwapIndex
@xlo.func(
    help="Convert an interest rate index to an overnight indexed swap index.",
    args={
        "index": "The interest rate index object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAsOvernightSwapIndex(
    index: ql.InterestRateIndex, trigger=None
) -> ql.OvernightIndexedSwap:
    return ql.as_overnight_swap_index(index)


@xlo.func(
    help="Create a QuantLib ZeroCouponSwap object with fixed payment.",
    args={
        "type": "The type of the swap (Payer or Receiver).",
        "base_nominal": "The base nominal amount.",
        "start_date": "The start date of the swap.",
        "maturity_date": "The maturity date of the swap.",
        "fixed_payment": "The fixed payment amount.",
        "ibor_index": "The Ibor index.",
        "payment_calendar": "The payment calendar.",
        "payment_convention": "The business day convention for payments (default: Following).",
        "payment_delay": "The payment delay (default: 0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponSwap(
    type: qSwapType,
    base_nominal: float,
    start_date: qDate,
    maturity_date: qDate,
    fixed_payment: float,
    ibor_index: ql.IborIndex,
    payment_calendar: qCalendar,
    payment_convention: qBusinessDayConvention = ql.Following,
    payment_delay: int = 0,
    trigger=None,
) -> ql.ZeroCouponSwap:
    return ql.ZeroCouponSwap(
        type,
        base_nominal,
        start_date,
        maturity_date,
        fixed_payment,
        ibor_index,
        payment_calendar,
        payment_convention,
        payment_delay,
    )


@xlo.func(
    help="Create a QuantLib ZeroCouponSwap object with fixed rate.",
    args={
        "type": "The type of the swap (Payer or Receiver).",
        "base_nominal": "The base nominal amount.",
        "start_date": "The start date of the swap.",
        "maturity_date": "The maturity date of the swap.",
        "fixed_rate": "The fixed rate.",
        "fixed_day_counter": "The day counter for the fixed leg.",
        "ibor_index": "The Ibor index.",
        "payment_calendar": "The payment calendar.",
        "payment_convention": "The business day convention for payments (default: Following).",
        "payment_delay": "The payment delay (default: 0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponSwap2(
    type: qSwapType,
    base_nominal: float,
    start_date: qDate,
    maturity_date: qDate,
    fixed_rate: float,
    fixed_day_counter: qDayCounter,
    ibor_index: ql.IborIndex,
    payment_calendar: qCalendar,
    payment_convention: qBusinessDayConvention = ql.Following,
    payment_delay: int = 0,
    trigger=None,
) -> ql.ZeroCouponSwap:
    return ql.ZeroCouponSwap(
        type,
        base_nominal,
        start_date,
        maturity_date,
        fixed_rate,
        fixed_day_counter,
        ibor_index,
        payment_calendar,
        payment_convention,
        payment_delay,
    )


@xlo.func(
    help="Get the type of a zero coupon swap.",
    args={
        "swap": "The zero coupon swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponSwapType(swap: ql.ZeroCouponSwap, trigger=None):
    return first_key(QL_SWAP_TYPE, swap.type())


@xlo.func(
    help="Get the base nominal of a zero coupon swap.",
    args={
        "swap": "The zero coupon swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponSwapBaseNominal(swap: ql.ZeroCouponSwap, trigger=None) -> float:
    return swap.baseNominal()


@xlo.func(
    help="Get the Ibor index of a zero coupon swap.",
    args={
        "swap": "The zero coupon swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponSwapIborIndex(swap: ql.ZeroCouponSwap, trigger=None) -> ql.IborIndex:
    return swap.iborIndex()


@xlo.func(
    help="Get the fixed leg of a zero coupon swap.",
    args={
        "swap": "The zero coupon swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponSwapFixedLeg(swap: ql.ZeroCouponSwap, trigger=None) -> ql.Leg:
    return swap.fixedLeg()


@xlo.func(
    help="Get the floating leg of a zero coupon swap.",
    args={
        "swap": "The zero coupon swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponSwapFloatingLeg(swap: ql.ZeroCouponSwap, trigger=None) -> ql.Leg:
    return swap.floatingLeg()


@xlo.func(
    help="Get the fixed payment of a zero coupon swap.",
    args={
        "swap": "The zero coupon swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponSwapFixedPayment(swap: ql.ZeroCouponSwap, trigger=None) -> float:
    return swap.fixedPayment()


@xlo.func(
    help="Get the fixed leg NPV of a zero coupon swap.",
    args={
        "swap": "The zero coupon swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponSwapFixedLegNPV(swap: ql.ZeroCouponSwap, trigger=None) -> float:
    return swap.fixedLegNPV()


@xlo.func(
    help="Get the floating leg NPV of a zero coupon swap.",
    args={
        "swap": "The zero coupon swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponSwapFloatingLegNPV(swap: ql.ZeroCouponSwap, trigger=None) -> float:
    return swap.floatingLegNPV()


@xlo.func(
    help="Get the fair fixed payment of a zero coupon swap.",
    args={
        "swap": "The zero coupon swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponSwapFairFixedPayment(swap: ql.ZeroCouponSwap, trigger=None) -> float:
    return swap.fairFixedPayment()


@xlo.func(
    help="Get the fair fixed rate of a zero coupon swap.",
    args={
        "swap": "The zero coupon swap object.",
        "day_counter": "The day counter for the fixed leg.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponSwapFairFixedRate(
    swap: ql.ZeroCouponSwap, day_counter: qDayCounter, trigger=None
) -> float:
    return swap.fairFixedRate(day_counter)


@xlo.func(
    help="Create a QuantLib EquityTotalReturnSwap object with Ibor index.",
    args={
        "type": "The type of the swap (Payer or Receiver).",
        "nominal": "The nominal amount.",
        "schedule": "The schedule for payments.",
        "equity_index": "The equity index.",
        "interest_rate_index": "The ibor interest rate index.",
        "day_counter": "The day counter.",
        "margin": "The margin.",
        "gearing": "The gearing (default: 1.0).",
        "payment_calendar": "The payment calendar (default: null calendar).",
        "payment_convention": "The business day convention for payments (default: Unadjusted).",
        "payment_delay": "The payment delay (default: 0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwap(
    type: qSwapType,
    nominal: float,
    schedule: ql.Schedule,
    equity_index: ql.EquityIndex,
    interest_rate_index: ql.IborIndex,
    day_counter: qDayCounter,
    margin: float,
    gearing: float = 1.0,
    payment_calendar: qCalendar = ql.NullCalendar(),  # TODO default value
    payment_convention: qBusinessDayConvention = ql.Unadjusted,
    payment_delay: int = 0,
    trigger=None,
) -> ql.EquityTotalReturnSwap:
    return ql.EquityTotalReturnSwap(
        type,
        nominal,
        schedule,
        equity_index,
        interest_rate_index,
        day_counter,
        margin,
        gearing,
        payment_calendar,
        payment_convention,
        payment_delay,
    )


@xlo.func(
    help="Create a QuantLib EquityTotalReturnSwap object with Overnight index.",
    args={
        "type": "The type of the swap (Payer or Receiver).",
        "nominal": "The nominal amount.",
        "schedule": "The schedule for payments.",
        "equity_index": "The equity index.",
        "interest_rate_index": "The overnight index.",
        "day_counter": "The day counter.",
        "margin": "The margin.",
        "gearing": "The gearing (default: 1.0).",
        "payment_calendar": "The payment calendar (default: null calendar).",
        "payment_convention": "The business day convention for payments (default: Unadjusted).",
        "payment_delay": "The payment delay (default: 0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwap2(
    type: qSwapType,
    nominal: float,
    schedule: ql.Schedule,
    equity_index: ql.EquityIndex,
    interest_rate_index: ql.OvernightIndex,
    day_counter: qDayCounter,
    margin: float,
    gearing: float = 1.0,
    payment_calendar: qCalendar = ql.NullCalendar(),  # TODO default value
    payment_convention: qBusinessDayConvention = ql.Unadjusted,
    payment_delay: int = 0,
    trigger=None,
) -> ql.EquityTotalReturnSwap:
    return ql.EquityTotalReturnSwap(
        type,
        nominal,
        schedule,
        equity_index,
        interest_rate_index,
        day_counter,
        margin,
        gearing,
        payment_calendar,
        payment_convention,
        payment_delay,
    )


@xlo.func(
    help="Get the type of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapType(swap: ql.EquityTotalReturnSwap, trigger=None):
    return first_key(QL_SWAP_TYPE, swap.type())


@xlo.func(
    help="Get the nominal of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapNominal(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> float:
    return swap.nominal()


@xlo.func(
    help="Get the equity index of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapEquityIndex(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> ql.EquityIndex:
    return swap.equityIndex()


@xlo.func(
    help="Get the interest rate index of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapInterestRateIndex(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> ql.InterestRateIndex:
    return swap.interestRateIndex()


@xlo.func(
    help="Get the schedule of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapSchedule(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> ql.Schedule:
    return swap.schedule()


@xlo.func(
    help="Get the day counter of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapDayCounter(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> qDayCounter:
    return swap.dayCounter()


@xlo.func(
    help="Get the margin of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapMargin(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> float:
    return swap.margin()


@xlo.func(
    help="Get the gearing of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapGearing(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> float:
    return swap.gearing()


@xlo.func(
    help="Get the payment calendar of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapPaymentCalendar(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> ql.Calendar:
    return swap.paymentCalendar()


@xlo.func(
    help="Get the payment convention of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapPaymentConvention(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> qBusinessDayConvention:
    return first_key(QL_BUSINESSDAYCONVENTION, swap.paymentConvention())


@xlo.func(
    help="Get the payment delay of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapPaymentDelay(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> int:
    return swap.paymentDelay()


@xlo.func(
    help="Get the equity leg of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapEquityLeg(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> ql.Leg:
    return swap.equityLeg()


@xlo.func(
    help="Get the interest rate leg of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapInterestRateLeg(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> ql.Leg:
    return swap.interestRateLeg()


@xlo.func(
    help="Get the equity leg NPV of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapEquityLegNPV(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> float:
    return swap.equityLegNPV()


@xlo.func(
    help="Get the interest rate leg NPV of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapInterestRateLegNPV(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> float:
    return swap.interestRateLegNPV()


@xlo.func(
    help="Get the fair margin of an equity total return swap.",
    args={
        "swap": "The equity total return swap object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityTotalReturnSwapFairMargin(
    swap: ql.EquityTotalReturnSwap, trigger=None
) -> float:
    return swap.fairMargin()
