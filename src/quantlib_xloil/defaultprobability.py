import QuantLib as ql
import numpy as np
import xloil as xlo

from .calendars import qCalendar, qBusinessDayConvention
from .config import EXCEL_GROUP_NAME
from .creditdefaultswap import qCreditDefaultSwapPricingModel
from .date import qDate, _to_date_list, qFrequency, qPeriod
from .daycounters import qDayCounter
from .ratehelpers import qQuoteHandle
from .scheduler import qDateGenerationRule
from .utilities import to_float_list


def _to_ql_default_probability_helpers(
    helpers,
) -> tuple[ql.DefaultProbabilityHelper, ...]:
    if helpers is None:
        return ()
    if isinstance(helpers, ql.DefaultProbabilityHelper):
        return (helpers,)
    if isinstance(helpers, (list, tuple)):
        return tuple(cf for cf in helpers)
    if isinstance(helpers, np.ndarray):
        return tuple(helpers.ravel().tolist())
    raise ValueError(
        f"Cannot convert {helpers} to list of QuantLib DefaultProbabilityHelper."
    )


# DefaultProbabilityTermStructure interface


@xlo.func(
    help="Returns the default probability from a DefaultProbabilityTermStructure at a given date.",
    args={
        "ts": "The DefaultProbabilityTermStructure object.",
        "date": "The date for which to calculate the default probability.",
        "extrapolate": "Whether to allow extrapolation beyond the range of the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityTermStructureDefaultProbability(
    ts: ql.DefaultProbabilityTermStructureHandle,
    date: qDate,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ts.defaultProbability(date, extrapolate)


@xlo.func(
    help="Returns the default probability from a DefaultProbabilityTermStructure at a given time.",
    args={
        "ts": "The DefaultProbabilityTermStructure object.",
        "time": "The time for which to calculate the default probability.",
        "extrapolate": "Whether to allow extrapolation beyond the range of the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityTermStructureDefaultProbabilityFromTime(
    ts: ql.DefaultProbabilityTermStructureHandle,
    time: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ts.defaultProbability(time, extrapolate)


@xlo.func(
    help="Returns the default probability from a DefaultProbabilityTermStructure between two dates.",
    args={
        "ts": "The DefaultProbabilityTermStructure object.",
        "date_one": "The first date for which to calculate the default probability.",
        "date_two": "The second date for which to calculate the default probability.",
        "extrapolate": "Whether to allow extrapolation beyond the range of the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityTermStructureDefaultProbability2(
    ts: ql.DefaultProbabilityTermStructureHandle,
    date_one: qDate,
    date_two: qDate,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ts.defaultProbability(date_one, date_two, extrapolate)


@xlo.func(
    help="Returns the default probability from a DefaultProbabilityTermStructure between two times.",
    args={
        "ts": "The DefaultProbabilityTermStructure object.",
        "time_one": "The first time for which to calculate the default probability.",
        "time_two": "The second time for which to calculate the default probability.",
        "extrapolate": "Whether to allow extrapolation beyond the range of the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityTermStructureDefaultProbabilityFromTime2(
    ts: ql.DefaultProbabilityTermStructureHandle,
    time_one: float,
    time_two: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ts.defaultProbability(time_one, time_two, extrapolate)


@xlo.func(
    help="Returns the survival probability from a DefaultProbabilityTermStructure at a given date.",
    args={
        "ts": "The DefaultProbabilityTermStructure object.",
        "date": "The date for which to calculate the survival probability.",
        "extrapolate": "Whether to allow extrapolation beyond the range of the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityTermStructureSurvivalProbability(
    ts: ql.DefaultProbabilityTermStructureHandle,
    date: qDate,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ts.survivalProbability(date, extrapolate)


@xlo.func(
    help="Returns the survival probability from a DefaultProbabilityTermStructure at a given time.",
    args={
        "ts": "The DefaultProbabilityTermStructure object.",
        "time": "The time for which to calculate the survival probability.",
        "extrapolate": "Whether to allow extrapolation beyond the range of the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityTermStructureSurvivalProbabilityFromTime(
    ts: ql.DefaultProbabilityTermStructureHandle,
    time: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ts.survivalProbability(time, extrapolate)


@xlo.func(
    help="Returns the default density from a DefaultProbabilityTermStructure at a given date.",
    args={
        "ts": "The DefaultProbabilityTermStructure object.",
        "date": "The date for which to calculate the default density.",
        "extrapolate": "Whether to allow extrapolation beyond the range of the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityTermStructureDefaultDensity(
    ts: ql.DefaultProbabilityTermStructureHandle,
    date: qDate,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ts.defaultDensity(date, extrapolate)


@xlo.func(
    help="Returns the default density from a DefaultProbabilityTermStructure at a given time.",
    args={
        "ts": "The DefaultProbabilityTermStructure object.",
        "time": "The time for which to calculate the default density.",
        "extrapolate": "Whether to allow extrapolation beyond the range of the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityTermStructureDefaultDensityFromTime(
    ts: ql.DefaultProbabilityTermStructureHandle,
    time: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ts.defaultDensity(time, extrapolate)


@xlo.func(
    help="Returns the hazard rate from a DefaultProbabilityTermStructure at a given date.",
    args={
        "ts": "The DefaultProbabilityTermStructure object.",
        "date": "The date for which to calculate the hazard rate.",
        "extrapolate": "Whether to allow extrapolation beyond the range of the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityTermStructureHazardRate(
    ts: ql.DefaultProbabilityTermStructureHandle,
    date: qDate,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ts.hazardRate(date, extrapolate)


@xlo.func(
    help="Returns the hazard rate from a DefaultProbabilityTermStructure at a given time.",
    args={
        "ts": "The DefaultProbabilityTermStructure object.",
        "time": "The time for which to calculate the hazard rate.",
        "extrapolate": "Whether to allow extrapolation beyond the range of the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityTermStructureHazardRateFromTime(
    ts: ql.DefaultProbabilityTermStructureHandle,
    time: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return ts.hazardRate(time, extrapolate)


# DefaultProbabilityTermStructures


@xlo.func(
    help="Returns a FlatHazardRate DefaultProbabilityTermStructure.",
    args={
        "reference_date": "The reference date for the term structure.",
        "hazard_rate": "The constant hazard rate.",
        "day_counter": "The day counter to use for the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFlatHazardRate(
    reference_date: qDate,
    hazard_rate: qQuoteHandle,
    day_counter: qDayCounter,
    trigger=None,
) -> ql.DefaultProbabilityTermStructureHandle:
    ts = ql.FlatHazardRate(reference_date, hazard_rate, day_counter)
    return ql.DefaultProbabilityTermStructureHandle(ts)


@xlo.func(
    help="Construct a hazard rate curve with linear interpolation.",
    args={
        "dates": "The dates corresponding to the hazard rates.",
        "hazard_rates": "The hazard rates corresponding to the dates.",
        "day_counter": "The day counter to use for the term structure.",
        "calendar": "The calendar to use for the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHazardRateCurve(
    dates: xlo.Array(dims=1),
    hazard_rates: xlo.Array(dims=1),
    day_counter: qDayCounter,
    calendar: qCalendar = ql.NullCalendar(),
    trigger=None,
) -> ql.DefaultProbabilityTermStructureHandle:
    ts = ql.HazardRateCurve(
        _to_date_list(dates), to_float_list(hazard_rates), day_counter, calendar
    )
    return ql.DefaultProbabilityTermStructureHandle(ts)


@xlo.func(
    help="Construct a default density curve with linear interpolation.",
    args={
        "dates": "The dates corresponding to the default densities.",
        "default_densities": "The default densities corresponding to the dates.",
        "day_counter": "The day counter to use for the term structure.",
        "calendar": "The calendar to use for the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultDensityCurve(
    dates: xlo.Array(dims=1),
    default_densities: xlo.Array(dims=1),
    day_counter: qDayCounter,
    calendar: qCalendar = ql.NullCalendar(),
    trigger=None,
) -> ql.DefaultProbabilityTermStructureHandle:
    ts = ql.DefaultDensityCurve(
        _to_date_list(dates), to_float_list(default_densities), day_counter, calendar
    )
    return ql.DefaultProbabilityTermStructureHandle(ts)


@xlo.func(
    help="Construct a survival probability curve with linear interpolation.",
    args={
        "dates": "The dates corresponding to the survival probabilities.",
        "survival_probabilities": "The survival probabilities corresponding to the dates.",
        "day_counter": "The day counter to use for the term structure.",
        "calendar": "The calendar to use for the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSurvivalProbabilityCurve(
    dates: xlo.Array(dims=1),
    survival_probabilities: xlo.Array(dims=1),
    day_counter: qDayCounter,
    calendar: qCalendar = ql.NullCalendar(),
    trigger=None,
) -> ql.DefaultProbabilityTermStructureHandle:
    ts = ql.SurvivalProbabilityCurve(
        _to_date_list(dates),
        to_float_list(survival_probabilities),
        day_counter,
        calendar,
    )
    return ql.DefaultProbabilityTermStructureHandle(ts)


# DefaultProbabilityHelper interface


@xlo.func(
    help="Returns the quote handle from a DefaultProbabilityHelper.",
    args={
        "helper": "The DefaultProbabilityHelper object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityHelperQuote(
    helper: ql.DefaultProbabilityHelper, trigger=None
) -> ql.QuoteHandle:
    return helper.quote()


@xlo.func(
    help="Returns the latest date from a DefaultProbabilityHelper.",
    args={
        "helper": "The DefaultProbabilityHelper object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityHelperLatestDate(
    helper: ql.DefaultProbabilityHelper, trigger=None
) -> ql.Date:
    return helper.latestDate()


@xlo.func(
    help="Returns the earliest date from a DefaultProbabilityHelper.",
    args={
        "helper": "The DefaultProbabilityHelper object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityHelperEarliestDate(
    helper: ql.DefaultProbabilityHelper, trigger=None
) -> ql.Date:
    return helper.earliestDate()


@xlo.func(
    help="Returns the maturity date from a DefaultProbabilityHelper.",
    args={
        "helper": "The DefaultProbabilityHelper object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityHelperMaturity(
    helper: ql.DefaultProbabilityHelper, trigger=None
) -> ql.Date:
    return helper.maturityDate()


@xlo.func(
    help="Returns the latest relevant date from a DefaultProbabilityHelper.",
    args={
        "helper": "The DefaultProbabilityHelper object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityHelperLatestRelevantDate(
    helper: ql.DefaultProbabilityHelper, trigger=None
) -> ql.Date:
    return helper.latestRelevantDate()


@xlo.func(
    help="Returns the pillar date from a DefaultProbabilityHelper.",
    args={
        "helper": "The DefaultProbabilityHelper object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityHelperPillarDate(
    helper: ql.DefaultProbabilityHelper, trigger=None
) -> ql.Date:
    return helper.pillarDate()


@xlo.func(
    help="Returns the implied quote from a DefaultProbabilityHelper.",
    args={
        "helper": "The DefaultProbabilityHelper object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityHelperImpliedQuote(
    helper: ql.DefaultProbabilityHelper,
    trigger=None,
) -> float:
    return helper.impliedQuote()


@xlo.func(
    help="Returns the quote error from a DefaultProbabilityHelper.",
    args={
        "helper": "The DefaultProbabilityHelper object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDefaultProbabilityHelperQuoteError(
    helper: ql.DefaultProbabilityHelper,
    trigger=None,
) -> float:
    return helper.quoteError()


@xlo.func(
    help="Creates a SpreadCdsHelper object.",
    args={
        "spread": "The spread quote handle.",
        "tenor": "The tenor of the CDS.",
        "settlement_days": "The number of settlement days.",
        "calendar": "The calendar for date calculations.",
        "frequency": "The frequency of payments.",
        "payment_convention": "The business day convention for payment dates.",
        "date_generation": "The date generation rule for the schedule.",
        "day_counter": "The day counter for the CDS.",
        "recovery_rate": "The recovery rate for the CDS.",
        "discount_curve": "The discount curve to use for pricing.",
        "settles_accrual": "Whether the CDS settles accrued interest.",
        "pays_at_default": "Whether the CDS pays at default.",
        "start_date": "The start date of the CDS.",
        "last_period_day_counter": "The day counter for the last period of the CDS.",
        "rebates_accrual": "Whether the CDS accrues rebates.",
        "model": "The pricing model to use for the CDS.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSpreadCdsHelper(
    spread: qQuoteHandle,
    tenor: qPeriod,
    settlement_days: int,
    calendar: qCalendar,
    frequency: qFrequency,
    payment_convention: qBusinessDayConvention,
    date_generation: qDateGenerationRule,  # ql.DateGeneration.TwentiethIMM
    day_counter: qDayCounter,
    recovery_rate: float,
    discount_curve: ql.YieldTermStructureHandle,
    settles_accrual: bool = True,
    pays_at_default: bool = True,
    start_date: qDate = ql.Date(),
    last_period_day_counter: str = None,  # cannot use ql.DayCounter(),
    rebates_accrual: bool = True,
    model: qCreditDefaultSwapPricingModel = ql.CreditDefaultSwap.Midpoint,
    trigger=None,
) -> ql.SpreadCdsHelper:
    if last_period_day_counter is None:
        last_period_day_counter = day_counter
    else:
        last_period_day_counter = qDayCounter.__wrapped__(last_period_day_counter)
    #
    return ql.SpreadCdsHelper(
        spread,
        tenor,
        settlement_days,
        calendar,
        frequency,
        payment_convention,
        date_generation,
        day_counter,
        recovery_rate,
        discount_curve,
        settles_accrual,
        pays_at_default,
        start_date,
        last_period_day_counter,
        rebates_accrual,
        model,
    )


@xlo.func(
    help="Creates an UpfrontCdsHelper object.",
    args={
        "upfront": "The upfront quote handle.",
        "spread": "The spread quote handle.",
        "tenor": "The tenor of the CDS.",
        "settlement_days": "The number of settlement days.",
        "calendar": "The calendar for date calculations.",
        "frequency": "The frequency of payments.",
        "payment_convention": "The business day convention for payment dates.",
        "date_generation": "The date generation rule for the schedule.",
        "day_counter": "The day counter for the CDS.",
        "recovery_rate": "The recovery rate for the CDS.",
        "discount_curve": "The discount curve to use for pricing.",
        "upfront_settlement_days": "The number of settlement days for the upfront payment.",
        "settles_accrual": "Whether the CDS settles accrued interest.",
        "pays_at_default": "Whether the CDS pays at default.",
        "start_date": "The start date of the CDS.",
        "last_period_day_counter": "The day counter for the last period of the CDS.",
        "rebates_accrual": "Whether the CDS accrues rebates.",
        "model": "The pricing model to use for the CDS.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlUpfrontCdsHelper(
    upfront: qQuoteHandle,
    spread: float,
    tenor: qPeriod,
    settlement_days: int,
    calendar: qCalendar,
    frequency: qFrequency,
    payment_convention: qBusinessDayConvention,
    date_generation: qDateGenerationRule,  # ql.DateGeneration.TwentiethIMM
    day_counter: qDayCounter,
    recovery_rate: float,
    discount_curve: ql.YieldTermStructureHandle,
    upfront_settlement_days: int = 0,
    settles_accrual: bool = True,
    pays_at_default: bool = True,
    start_date: qDate = ql.Date(),
    last_period_day_counter: str = None,  # cannot use ql.DayCounter(),
    rebates_accrual: bool = True,
    model: qCreditDefaultSwapPricingModel = ql.CreditDefaultSwap.Midpoint,
    trigger=None,
) -> ql.UpfrontCdsHelper:
    if last_period_day_counter is None:
        last_period_day_counter = day_counter
    else:
        last_period_day_counter = qDayCounter.__wrapped__(last_period_day_counter)
    #
    return ql.UpfrontCdsHelper(
        upfront,
        spread,
        tenor,
        settlement_days,
        calendar,
        frequency,
        payment_convention,
        date_generation,
        day_counter,
        recovery_rate,
        discount_curve,
        upfront_settlement_days,
        settles_accrual,
        pays_at_default,
        start_date,
        last_period_day_counter,
        rebates_accrual,
        model,
    )


@xlo.func(
    help="Construct a piecewise flat hazard rate curve from a set of DefaultProbabilityHelpers.",
    args={
        "reference_date": "The reference date for the term structure.",
        "helpers": "The DefaultProbabilityHelpers to use for bootstrapping the curve.",
        "day_counter": "The day counter to use for the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseFlatHazardRateAsDts(
    reference_date: qDate,
    helpers: xlo.Array(dims=1),
    day_counter: qDayCounter,
    trigger=None,
) -> ql.PiecewiseFlatHazardRate:
    return ql.PiecewiseFlatHazardRate(
        reference_date, _to_ql_default_probability_helpers(helpers), day_counter
    )


@xlo.func(
    help="Construct a piecewise flat hazard rate curve from a set of DefaultProbabilityHelpers and return it as a DefaultProbabilityTermStructureHandle.",
    args={
        "reference_date": "The reference date for the term structure.",
        "helpers": "The DefaultProbabilityHelpers to use for bootstrapping the curve.",
        "day_counter": "The day counter to use for the term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseFlatHazardRate(
    reference_date: qDate,
    helpers: xlo.Array(dims=1),
    day_counter: qDayCounter,
    trigger=None,
) -> ql.DefaultProbabilityTermStructureHandle:
    ts = ql.PiecewiseFlatHazardRate(
        reference_date, _to_ql_default_probability_helpers(helpers), day_counter
    )
    return ql.DefaultProbabilityTermStructureHandle(ts)


@xlo.func(
    help="Construct a risky bond engine using a default probability term structure, recovery rate, and discount curve.",
    args={
        "default_curve": "The default probability term structure to use for the engine.",
        "recovery_rate": "The recovery rate to use for the engine.",
        "discount_curve": "The discount curve to use for the engine.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRiskyBondEngine(
    default_curve: ql.DefaultProbabilityTermStructureHandle,
    recovery_rate: float,
    discount_curve: ql.YieldTermStructureHandle,
    trigger=None,
) -> ql.RiskyBondEngine:
    return ql.RiskyBondEngine(default_curve, recovery_rate, discount_curve)
