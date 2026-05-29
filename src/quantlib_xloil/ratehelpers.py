import QuantLib as ql
import xloil as xlo

from .calendars import qBusinessDayConvention, qCalendar
from .cashflows import qRateAveragingType
from .date import qDate, qFrequency, qPeriod
from .daycounters import qDayCounter
from .scheduler import qDateGenerationRule
from .config import EXCEL_GROUP_NAME
from .utilities import UNKNOWN_KEY, UNKNOWN_VALUE, enum_value

QL_PILLAR_CHOICE = {
    "LASTRELEVANTDATE": ql.Pillar.LastRelevantDate,
    "MATURITYDATE": ql.Pillar.MaturityDate,
    "CUSTOMDATE": ql.Pillar.CustomDate,
}  

QL_FUTURES_TYPE = {
    "IMM": ql.Futures.IMM,
    "ASX": ql.Futures.ASX,
    "CUSTOM": ql.Futures.Custom,
}

def _qPillarChoice(s: str) -> ql.Pillar:
    return enum_value(s, QL_PILLAR_CHOICE)

@xlo.converter()
def qPillarChoice(s : str) -> ql.Pillar:
    return _qPillarChoice(s)

def _qFuturesType(s: str) -> ql.Futures:
    return enum_value(s, QL_FUTURES_TYPE)

@xlo.converter()
def qFuturesType(s : str) -> ql.Futures:
    return _qFuturesType(s)

@xlo.converter()
def qQuoteHandle(rate : str) -> ql.QuoteHandle:
    if isinstance(rate, ql.QuoteHandle):
        return rate
    if isinstance(rate, (int, float)):
        return ql.QuoteHandle(ql.SimpleQuote(float(rate)))
    raise ValueError(f"Cannot convert {rate} to QuoteHandle.")

@xlo.returner(target=ql.QuoteHandle, register=True)
def xQuoteHandle(quote_handle : ql.QuoteHandle):
    return quote_handle.value()

@xlo.func(
    help='Get the quote associated with a QuantLib RateHelper.',
    args={
        'rate_helper': 'The QuantLib RateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlRateHelperQuote(rate_helper: ql.RateHelper, trigger = None) -> ql.Quote:
    return rate_helper.quote()

@xlo.func(
    help='Get the latest date associated with a QuantLib RateHelper.',
    args={
        'rate_helper': 'The QuantLib RateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlRateHelperLatestDate(rate_helper: ql.RateHelper, trigger = None) -> ql.Date:
    return rate_helper.latestDate()

@xlo.func(
    help='Get the earliest date associated with a QuantLib RateHelper.',
    args={
        'rate_helper': 'The QuantLib RateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlRateHelperEarliestDate(rate_helper: ql.RateHelper, trigger = None) -> ql.Date:
    return rate_helper.earliestDate()

@xlo.func(
    help='Get the maturity date associated with a QuantLib RateHelper.',
    args={
        'rate_helper': 'The QuantLib RateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlRateHelperMaturityDate(rate_helper: ql.RateHelper, trigger = None) -> ql.Date:
    return rate_helper.maturityDate()

@xlo.func(
    help='Get the latest relevant date associated with a QuantLib RateHelper.',
    args={
        'rate_helper': 'The QuantLib RateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlRateHelperLatestRelevantDate(rate_helper: ql.RateHelper, trigger = None) -> ql.Date:
    return rate_helper.latestRelevantDate()

@xlo.func(
    help='Get the pillar date associated with a QuantLib RateHelper.',
    args={
        'rate_helper': 'The QuantLib RateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlRateHelperPillarDate(rate_helper: ql.RateHelper, trigger = None) -> ql.Date:
    return rate_helper.pillarDate()

# \ToDo test cases
@xlo.func(
    help='Get the earliest relevant date associated with a QuantLib RateHelper.',
    args={
        'rate_helper': 'The QuantLib RateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlRateHelperImpliedQuote(rate_helper: ql.RateHelper, trigger = None) -> float:
    return rate_helper.impliedQuote()

# \ToDo test cases
@xlo.func(
    help='Get the quote error associated with a QuantLib RateHelper.',
    args={
        'rate_helper': 'The QuantLib RateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlRateHelperQuoteError(rate_helper: ql.RateHelper, trigger = None) -> float:
    return rate_helper.quoteError()

@xlo.func(
    help='Create a QuantLib DepositRateHelper object from a type and arguments.',
    args={
        'rate': 'The rate for the deposit.',
        'tenor': 'The tenor of the deposit (e.g. "3M", "6M").',
        'fixing_days': 'The number of fixing days for the deposit.',
        'calendar': 'The calendar for the deposit.',
        'business_day_convention': 'The business day convention for the deposit.',
        'end_of_month': 'Whether to use the end of month convention for the deposit.',
        'day_counter': 'The day counter for the deposit.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDepositRateHelper(
    rate: qQuoteHandle, 
    tenor: qPeriod, 
    fixing_days: int, 
    calendar: qCalendar, 
    business_day_convention: qBusinessDayConvention, 
    end_of_month: bool, 
    daycounter: qDayCounter, 
    trigger = None
    ) -> ql.DepositRateHelper:
    return ql.DepositRateHelper(
        rate, 
        tenor, 
        fixing_days, 
        calendar, 
        business_day_convention, 
        end_of_month, 
        daycounter
    )

@xlo.func(
    help='Create a QuantLib DepositRateHelper object from a type and arguments.',
    args={
        'rate': 'The rate for the deposit.',
        'index': 'The IborIndex for the deposit.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDepositRateHelper2(
    rate: qQuoteHandle, 
    index: ql.IborIndex, 
    trigger = None
    ) -> ql.DepositRateHelper:
    return ql.DepositRateHelper(
        rate, 
        index
    )

@xlo.func(
    help='Create a QuantLib DepositRateHelper object from a type and arguments.',
    args={
        'rate': 'The rate for the deposit.',
        'fixing_date': 'The date on which the deposit is fixed.',
        'index': 'The IborIndex for the deposit.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlDepositRateHelper3(
    rate: qQuoteHandle, 
    fixing_date: qDate, 
    index: ql.IborIndex, 
    trigger = None
    ) -> ql.DepositRateHelper:
    return ql.DepositRateHelper(
        rate, 
        fixing_date, 
        index
    )

@xlo.func(
    help='Create a QuantLib FRARateHelper object from a type and arguments.',
    args={
        'rate': 'The rate for the FRA.',
        'month_to_start': 'The number of months to start for the FRA.',
        'month_to_end': 'The number of months to end for the FRA.',
        'fixing_days': 'The number of fixing days for the FRA.',
        'calendar': 'The calendar for the FRA.',    
        'business_day_convention': 'The business day convention for the FRA.',
        'end_of_month': 'Whether to use the end of month convention for the FRA.',
        'day_counter': 'The day counter for the FRA.',
        'pillar': 'The pillar choice for the FRA. (lastrelevantdate, maturitydate, customdate)',
        'custom_pillar_date': 'The custom pillar date for the FRA (if pillar choice is CustomDate).',
        'use_indexed_coupon': 'Whether to use indexed coupons for the FRA.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFRARateHelper(
    rate: qQuoteHandle, 
    month_to_start: int, 
    month_to_end: int, 
    fixing_days: int, 
    calendar: qCalendar, 
    business_day_convention: qBusinessDayConvention, 
    end_of_month: bool, 
    day_counter: qDayCounter, 
    pillar: qPillarChoice = ql.Pillar.LastRelevantDate, 
    custom_pillar_date: qDate = ql.Date(), 
    use_indexed_coupon: bool = True, 
    trigger = None
    ) -> ql.FraRateHelper:
    return ql.FraRateHelper(
        rate, 
        month_to_start, 
        month_to_end, 
        fixing_days, 
        calendar, 
        business_day_convention, 
        end_of_month, 
        day_counter, 
        pillar, 
        custom_pillar_date, 
        use_indexed_coupon
    )

@xlo.func(
    help='Create a QuantLib FRARateHelper object from a type and arguments.',
    args={
        'rate': 'The rate for the FRA.',
        'month_to_start': 'The number of months to start for the FRA.',
        'index': 'The IborIndex for the FRA.',
        'pillar': 'The pillar choice for the FRA. (lastrelevantdate, maturitydate, customdate)',
        'custom_pillar_date': 'The custom pillar date for the FRA (if pillar choice is CustomDate).',
        'use_indexed_coupon': 'Whether to use indexed coupons for the FRA.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFRARateHelper2(
    rate: qQuoteHandle, 
    month_to_start: int, 
    index: ql.IborIndex, 
    pillar: qPillarChoice = ql.Pillar.LastRelevantDate, 
    custom_pillar_date: qDate = ql.Date(), 
    use_indexed_coupon: bool = True, 
    trigger = None
    ) -> ql.FraRateHelper:
    return ql.FraRateHelper(
        rate, 
        month_to_start, 
        index, 
        pillar, 
        custom_pillar_date, 
        use_indexed_coupon
    )

@xlo.func(
    help='Create a QuantLib FRARateHelper object from a type and arguments.',
    args={
        'rate': 'The rate for the FRA.',
        'imm_offset_start': 'The IMM offset for the start of the FRA.',
        'imm_offset_end': 'The IMM offset for the end of the FRA.',
        'index': 'The IborIndex for the FRA.',
        'pillar': 'The pillar choice for the FRA. (lastrelevantdate, maturitydate, customdate)',
        'custom_pillar_date': 'The custom pillar date for the FRA (if pillar choice is CustomDate).',
        'use_indexed_coupon': 'Whether to use indexed coupons for the FRA.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFRARateHelper3(
    rate: qQuoteHandle,
    imm_offset_start: int, 
    imm_offset_end: int, 
    index: ql.IborIndex, 
    pillar: qPillarChoice = ql.Pillar.LastRelevantDate, 
    custom_pillar_date: qDate = ql.Date(), 
    use_indexed_coupon: bool = True, 
    trigger = None
    ) -> ql.FraRateHelper:
    return ql.FraRateHelper(
        rate, 
        imm_offset_start, 
        imm_offset_end, 
        index, 
        pillar, 
        custom_pillar_date, 
        use_indexed_coupon
    )

@xlo.func(
    help='Create a QuantLib FRARateHelper object from a type and arguments.',
    args={
        'rate': 'The rate for the FRA.',
        'period_to_start': 'The period to start for the FRA.',
        'index': 'The IborIndex for the FRA.',
        'pillar': 'The pillar choice for the FRA. (lastrelevantdate, maturitydate, customdate)',
        'custom_pillar_date': 'The custom pillar date for the FRA (if pillar choice is CustomDate).',
        'use_indexed_coupon': 'Whether to use indexed coupons for the FRA.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFRARateHelper4(
    rate: qQuoteHandle, 
    period_to_start: qPeriod, 
    index: ql.IborIndex, 
    pillar: qPillarChoice = ql.Pillar.LastRelevantDate,  
    custom_pillar_date: qDate = ql.Date(), 
    use_indexed_coupon: bool = True, 
    trigger = None
    ) -> ql.FraRateHelper:
    return ql.FraRateHelper(
        rate, 
        period_to_start, 
        index, 
        pillar, 
        custom_pillar_date, 
        use_indexed_coupon
    )

# \ToDo constructor not available in this version of quantlib
@xlo.func(
    help='Create a QuantLib FRARateHelper object from a type and arguments.',
    args={
        'rate': 'The rate for the FRA.',
        'start_date': 'The start date for the FRA.',
        'end_date': 'The end date for the FRA.',
        'index': 'The IborIndex for the FRA.',
        'pillar': 'The pillar choice for the FRA. (lastrelevantdate, maturitydate, customdate)',
        'custom_pillar_date': 'The custom pillar date for the FRA (if pillar choice is CustomDate).',
        'use_indexed_coupon': 'Whether to use indexed coupons for the FRA.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFRARateHelperForDates(
    rate: qQuoteHandle, 
    start_date: qDate, 
    end_date: qDate, 
    index: ql.IborIndex, 
    pillar: qPillarChoice = ql.Pillar.LastRelevantDate, 
    custom_pillar_date: qDate=ql.Date(), 
    use_indexed_coupon: bool = True, 
    trigger = None
    ) -> ql.FraRateHelper:
    return ql.FraRateHelper(
        rate, 
        start_date, 
        end_date, 
        index, 
        pillar, 
        custom_pillar_date, 
        use_indexed_coupon
    )

@xlo.func(
    help='Create a QuantLib FutureRateHelper object from a type and arguments.',
    args={
        'price': 'The price of the future.',
        'ibor_start_date': 'The start date of the underlying Ibor index.',
        'n_months': 'The number of months for the future.',
        'calendar': 'The calendar for the future.',
        'business_day_convention': 'The business day convention for the future.',
        'end_of_month': 'Whether to use the end of month convention for the future.',
        'day_counter': 'The day counter for the future.',
        'convexity_adjustment': 'The convexity adjustment for the future.',
        'type': 'The type of the future (e.g. IMM, Eurodollar).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFuturesRateHelper(
    price: qQuoteHandle, 
    ibor_start_date: qDate, 
    n_months: int, 
    calendar: qCalendar, 
    business_day_convention: qBusinessDayConvention, 
    end_of_month: bool, 
    day_counter: qDayCounter, 
    convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), 
    type: qFuturesType = ql.IMM,
    trigger = None
    ) -> ql.FuturesRateHelper:
    return ql.FuturesRateHelper(
        price, 
        ibor_start_date, 
        n_months, 
        calendar, 
        business_day_convention, 
        end_of_month, 
        day_counter, 
        convexity_adjustment, 
        type
    )

@xlo.func(
    help='Create a QuantLib FutureRateHelper object from a type and arguments.',
    args={
        'price': 'The price of the future.',
        'ibor_start_date': 'The start date of the underlying Ibor index.',
        'ibor_end_date': 'The end date of the underlying Ibor index.',
        'day_counter': 'The day counter for the future.',
        'convexity_adjustment': 'The convexity adjustment for the future.',
        'type': 'The type of the future (e.g. IMM, Eurodollar).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFuturesRateHelper2(
    price: qQuoteHandle, 
    ibor_start_date: qDate, 
    ibor_end_date: qDate, 
    day_counter: qDayCounter, 
    convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), 
    type: qFuturesType = ql.IMM,
    trigger = None
    ) -> ql.FuturesRateHelper:
    return ql.FuturesRateHelper(
        price, 
        ibor_start_date, 
        ibor_end_date, 
        day_counter, 
        convexity_adjustment, 
        type
    )

@xlo.func(
    help='Create a QuantLib FutureRateHelper object from a type and arguments.',
    args={
        'price': 'The price of the future.',
        'ibor_start_date': 'The start date of the underlying Ibor index.',
        'index': 'The IborIndex for the future.',
        'convexity_adjustment': 'The convexity adjustment for the future.',
        'type': 'The type of the future (e.g. IMM, Eurodollar).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFuturesRateHelper3(
    price: qQuoteHandle, 
    ibor_start_date: qDate, 
    index: ql.IborIndex, 
    convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), 
    type: qFuturesType = ql.IMM,
    trigger = None
    ) -> ql.FuturesRateHelper:
    return ql.FuturesRateHelper(
        price, 
        ibor_start_date, 
        index, 
        convexity_adjustment, 
        type
    )

@xlo.func(
    help='Get the convexity adjustement of a FuturesRateHelper.',
    args={
        'futures_rate_helper': 'The QuantLib FutureRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFuturesRateConvexityAdjustment(futures_rate_helper: ql.FuturesRateHelper, trigger = None) -> float:
    return futures_rate_helper.convexityAdjustment()

@xlo.func(
    help='Create a QuantLib SwapRateHelper object from a type and arguments.',
    args={
        'rate': 'The rate for the swap.',
        'tenor': 'The tenor of the swap (e.g. "5Y").',
        'calendar': 'The calendar for the swap.',
        'fixed_frequency': 'The frequency of the fixed leg (e.g. "Annual").',
        'fixed_convention': 'The business day convention for the fixed leg.',
        'fixed_day_ount': 'The day count convention for the fixed leg.',
        'ibor_index': 'The IborIndex for the floating leg.',
        'spread': 'The spread on the floating leg (optional).',
        'fwd_start': 'The forward start period for the swap (optional).',
        'discounting_curve': 'The discounting curve to use for the swap (optional).',
        'settlement_days': 'The number of settlement days for the swap (optional).',
        'pillar': 'The pillar choice for the swap (optional). (lastrelevantdate, maturitydate, customdate)' ,
        'custom_pillar_date': 'The custom pillar date for the swap (if pillar choice is CustomDate, optional).',
        'end_of_month': 'Whether to use end of month convention for the swap (optional).',
        'with_indexed_coupons': 'Whether to use indexed coupons for the swap (optional).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapRateHelper(
    rate: qQuoteHandle, 
    tenor: qPeriod, 
    calendar: qCalendar, 
    fixed_frequency: qFrequency, 
    fixed_convention: qBusinessDayConvention, 
    fixed_daycount: qDayCounter, 
    ibor_index: ql.IborIndex, 
    spread: float = 0.0,
    fwd_start: qPeriod = ql.Period(0, ql.Days), 
    discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    settlement_days: int = 0,
    pillar: qPillarChoice = ql.Pillar.LastRelevantDate, 
    custom_pillar_date: qDate = ql.Date(),
    end_of_month: bool = False,
    with_indexed_coupons: bool = False,
    trigger = None
    ) -> ql.SwapRateHelper:
    spread_handle = ql.QuoteHandle(ql.SimpleQuote(spread))
    return ql.SwapRateHelper(
        rate, 
        tenor, 
        calendar, 
        fixed_frequency, 
        fixed_convention, 
        fixed_daycount, 
        ibor_index, 
        spread_handle, 
        fwd_start, 
        discounting_curve,
        settlement_days,
        pillar,
        custom_pillar_date,
        end_of_month,
        with_indexed_coupons
    )

@xlo.func(
    help='Create a QuantLib SwapRateHelper object from a type and arguments.',
    args={
        'rate': 'The rate for the swap.',
        'index': 'The swap index.',
        'spread': 'The spread on the floating leg (optional).',
        'fwd_start': 'The forward start period for the swap (optional).',
        'discounting_curve': 'The discounting curve to use for the swap (optional).',
        'pillar': 'The pillar choice for the swap (optional). (lastrelevantdate, maturitydate, customdate)',
        'custom_pillar_date': 'The custom pillar date for the swap (if pillar choice is CustomDate, optional).',
        'end_of_month': 'Whether to use end of month convention for the swap (optional).',
        'with_indexed_coupons': 'Whether to use indexed coupons for the swap (optional).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapRateHelper2(
    rate: qQuoteHandle, 
    index: ql.SwapIndex, 
    spread: float = 0.0, 
    fwd_start: qPeriod = ql.Period(0, ql.Days), 
    discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), 
    pillar: qPillarChoice = ql.Pillar.LastRelevantDate, 
    custom_pillar_date: qDate = ql.Date(), 
    end_of_month: bool = False, 
    with_indexed_coupons: bool = False, 
    trigger = None
    ) -> ql.SwapRateHelper:
    spread_handle = ql.QuoteHandle(ql.SimpleQuote(spread))
    return ql.SwapRateHelper(
        rate, 
        index, 
        spread_handle, 
        fwd_start, 
        discounting_curve, 
        pillar, 
        custom_pillar_date, 
        end_of_month, 
        with_indexed_coupons
    )

# \ToDo constructor not available in this version of quantlib
@xlo.func(
    local=False,
    help='Create a QuantLib SwapRateHelper object from a type and arguments.',
    args={
        'rate': 'The swap rate quote handle.',
        'start_date': 'The start date of the swap.',
        'end_date': 'The end date of the swap.',
        'calendar': 'The calendar for the swap.',
        'fixed_frequencies': 'The frequency of fixed rate payments.',
        'business_day_convention': 'The business day convention for the swap.',
        'day_counter': 'The day counter for the swap.',
        'index': 'The IBOR index for the floating leg (e.g., EURIBOR, LIBOR).',
        'spread': 'The spread over the index (default: 0.0).',
        'discounting_curve': 'The yield term structure for discounting (optional).',
        'pillar': 'The pillar choice for the swap (default: LastRelevantDate).',
        'custom_pillar_date': 'The custom pillar date if pillar choice is Custom (optional).',
        'end_of_month': 'Whether to use the end of month convention (default: False).',
        'with_indexed_coupons': 'Whether to use indexed coupons (default: False).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapRateForDates(
    rate: qQuoteHandle, 
    start_date: qDate,
    end_date: qDate,
    calendar: qCalendar,
    fixed_frequencies: qFrequency,
    business_day_convention: qBusinessDayConvention,
    day_counter: qDayCounter,
    index: ql.IborIndex,
    spread: float = 0.0,
    discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), 
    pillar: ql.Pillar = ql.Pillar.LastRelevantDate, 
    custom_pillar_date: qDate = ql.Date(), 
    end_of_month: bool = False, 
    with_indexed_coupons: bool = False, 
    trigger = None
    ) -> ql.SwapRateHelper:
    return ql.SwapRateHelper(
        rate, 
        start_date,
        end_date,
        calendar,
        fixed_frequencies,
        business_day_convention,
        day_counter,
        index,
        spread,
        discounting_curve,
        pillar,
        custom_pillar_date,
        end_of_month,
        with_indexed_coupons
    )

@xlo.func(
    help='Get the spread associated with a QuantLib SwapRateHelper.',
    args={
        'swap_rate_helper': 'The QuantLib SwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapRateHelperSpread(swap_rate_helper: ql.SwapRateHelper, trigger = None) -> float:
    return swap_rate_helper.spread()

@xlo.func(
    help='Get the swap associated with a QuantLib SwapRateHelper.',
    args={
        'swap_rate_helper': 'The QuantLib SwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapRateHelperSwap(swap_rate_helper: ql.SwapRateHelper, trigger = None) -> ql.VanillaSwap:
    return swap_rate_helper.swap()

# /ToDo: bond.py needs to be implemented
"""
@xlo.func(
    help='Create a QuantLib BondHelper object.',
    args={
        'Quote': 'The quote for the bond.',
        'Bond': 'The QuantLib Bond object.',
        'PriceType': 'The price type for the bond (optional).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondHelper(quote: float, bond: ql.Bond, price_type: ql.BondHelper.PriceType = ql.Bond.Price.Clean, trigger = None) -> ql.BondHelper:
    quote_handle = ql.QuoteHandle(ql.SimpleQuote(quote))
    return ql.BondHelper(quote_handle, bond, price_type)

@xlo.func(
    help='Create a QuantLib FixedRateBondHelper object.',
    args={
        'clean_price': 'The clean price of the bond.',
        'settlement_days': 'The number of settlement days for the bond.',
        'face_amount': 'The face amount of the bond.',
        'schedule': 'The schedule for the bond.',
        'coupons': 'The list of coupon rates for the bond.',
        'day_counter': 'The day counter for the bond.',
        'business_day_convention': 'The business day convention for the bond.',
        'redemption': 'The redemption value of the bond (optional).',
        'issue_date': 'The issue date of the bond (optional).',
        'payment_calendar': 'The payment calendar for the bond (optional).',
        'ex_coupon_period': 'The ex-coupon period for the bond (optional).',
        'ex_coupon_calendar': 'The ex-coupon calendar for the bond (optional).',
        'ex_coupon_convention': 'The ex-coupon business day convention for the bond (optional).',
        'ex_coupon_end_of_month': 'Whether to use end of month convention for ex-coupon dates (optional).',
        'price_type': 'The price type for the bond helper (optional).',
    },
        group=EXCEL_GROUP_NAME,
)
def qlFixedRateBondHelper(
        clean_price: float, 
        settlement_days: int, 
        face_amount: float, 
        schedule: ql.Schedule, 
        coupons: list[float], 
        day_counter: qDayCounter, 
        business_day_convention: qBusinessDayConvention = "Following", 
        redemption: float = 100.0, 
        issue_date: qDate = ql.Date(), 
        payment_calendar: qCalendar = "NullCalendar",
        ex_coupon_period: qPeriod = ql.Period(0, ql.Days),
        ex_coupon_calendar: qCalendar = "NullCalendar",
        ex_coupon_convention: qBusinessDayConvention = "UnAdjusted",
        ex_coupon_end_of_month: bool = False,
        price_type: ql.BondHelper.PriceType = ql.BondHelper.Clean, 
        trigger = None) -> ql.BondHelper:
    quote_handle = ql.QuoteHandle(ql.SimpleQuote(clean_price))
    return ql.FixedRateBondHelper(
        quote_handle, 
        settlement_days, 
        face_amount, 
        schedule, 
        coupons, 
        day_counter, 
        business_day_convention, 
        redemption, 
        issue_date, 
        payment_calendar, 
        ex_coupon_period, 
        ex_coupon_calendar, 
        ex_coupon_convention, 
        ex_coupon_end_of_month, 
        price_type
        )
"""

# \ToDo pricer test case
@xlo.func(
    help="Create an OIS Rate Helper object.",
    args={
        "settlement_days": "The number of settlement days",
        "tenor": "The tenor of the OIS swap (e.g., '1Y', '5Y')",
        "fixed_rate": "The fixed rate quote for the OIS swap",
        "overnight_index": "The overnight index (e.g., SOFR, EONIA)",
        "discounting_curve": "The YieldTermStructure for discounting (optional)",
        "telescopic_value_dates": "The indicator to use telescopic value dates (True/False)",
        "payment_lag": "The days between accrual end and payment",
        "payment_convention": "The business day convention for payments",
        "payment_frequency": "The payment frequency (Annual, Semi-Annual, etc.)",
        "payment_calendar": "The calendar for payment dates",
        "forward_start": "The forward start period (e.g., '1M')",
        "overnight_spread": "The additional spread on overnight index",
        "pillar": "The pillar definition (LastRelevantDate, MaturityDate, etc.)",
        "custom_pillar_date": "The custom pillar date if needed",
        "averaging_method": "The averaging method (Compound, Simple, etc.)",
        "end_of_month": "The end-of-month adjustment flag (True/False)",
        "fixed_payment_frequency": "The payment frequency for the fixed leg",
        "fixed_calendar": "The calendar for the fixed leg",
        "look_back_days": "The look-back period in days",
        "lock_out_days": "The lock-out period in days",
        "apply_observation_shift": "The flag to apply observation shift (True/False)",
        "pricer": "The FloatingRateCouponPricer object",
        "rule": "The DateGeneration rule (Backward, Forward, etc.)",
        "overnight_calendar": "The calendar for the overnight index",
        "convention": "The business day convention (Modified Following, etc.)",
    },
        group=EXCEL_GROUP_NAME,
)

def qlOISRateHelper(
    settlement_days: int, 
    tenor: qPeriod, 
    fixed_rate: qQuoteHandle, 
    overnight_index: ql.OvernightIndex, 
    discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    telescopic_value_dates: bool = False,
    payment_lag: int = 0,
    payment_convention: qBusinessDayConvention = ql.Following,
    payment_frequency: qFrequency = ql.Annual,
    payment_calendar: qCalendar = ql.NullCalendar,
    forward_start: qPeriod = ql.Period(0, ql.Days),
    overnight_spread: float = 0.0, 
    pillar: qPillarChoice = ql.Pillar.LastRelevantDate, 
    custom_pillar_date: qDate = ql.Date(),
    averaging_method: qRateAveragingType = ql.RateAveraging.Compound,
    end_of_month: bool = None, 
    fixed_payment_frequency: qFrequency = ql.NoFrequency,
    fixed_calendar: qCalendar = ql.NullCalendar,
    look_back_days: int = 0,
    lock_out_days: int = 0,
    apply_observation_shift: bool = False,
    pricer: ql.FloatingRateCouponPricer = None,
    rule: qDateGenerationRule = ql.DateGeneration.Backward,
    overnight_calendar: qCalendar = ql.NullCalendar,
    convention: qBusinessDayConvention = ql.ModifiedFollowing,
    trigger = None
    ) -> ql.OISRateHelper:
    return ql.OISRateHelper(
        settlement_days, 
        tenor, 
        fixed_rate, 
        overnight_index, 
        discounting_curve, 
        telescopic_value_dates,
        payment_lag,
        payment_convention,
        payment_frequency,
        payment_calendar,
        forward_start,
        overnight_spread, 
        pillar, 
        custom_pillar_date,
        averaging_method, 
        end_of_month, 
        fixed_payment_frequency,
        fixed_calendar,
        look_back_days,
        lock_out_days,
        apply_observation_shift,
        pricer,
        rule,
        overnight_calendar,
        convention,
    )

# \ToDo constructor not available in this version of quantlib
"""
@xlo.func(
    help="The OIS Rate Helper creates a rate helper using start and end dates instead of settlement days",
    args={
        "start_date": "The start date of the OIS swap",
        "end_date": "The end date of the OIS swap",
        "fixed_rate": "The fixed rate quote for the OIS swap",
        "overnight_index": "The overnight index (e.g., SOFR, EONIA)",
        "discounting_curve": "The YieldTermStructure for discounting (optional)",
        "telescopic_value_dates": "The indicator to use telescopic value dates (True/False)",
        "payment_lag": "The days between accrual end and payment",
        "payment_convention": "The business day convention for payments",
        "payment_frequency": "The payment frequency (Annual, Semi-Annual, etc.)",
        "payment_calendar": "The calendar for payment dates",
        "overnight_spread": "The additional spread on overnight index",
        "pillar": "The pillar definition (LastRelevantDate, MaturityDate, etc.)",
        "custom_pillar_date": "The custom pillar date if needed",
        "averaging_method": "The averaging method (Compound, Simple, etc.)",
        "end_of_month": "The end-of-month adjustment flag (True/False)",
        "fixed_payment_frequency": "The payment frequency for the fixed leg",
        "fixed_calendar": "The calendar for the fixed leg",
        "look_back_days": "The look-back period in days",
        "lock_out_days": "The lock-out period in days",
        "apply_observation_shift": "The flag to apply observation shift (True/False)",
        "pricer": "The FloatingRateCouponPricer object",
        "rule": "The DateGeneration rule (Backward, Forward, etc.)",
        "overnight_calendar": "The calendar for the overnight index",
        "convention": "The business day convention (Modified Following, etc.)",
    }
)
def qlOISRateHelperForDates(
        start_date: qDate,
        end_date: qDate,
        fixed_rate: float,
        overnight_index: ql.OvernightIndex,
        discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
        telescopic_value_dates: bool = False,
        payment_lag: int = 0,
        payment_convention: qBusinessDayConvention = "Following",
        payment_frequency: qFrequency = "Annual",
        payment_calendar: qCalendar = "NullCalendar",
        overnight_spread: float = 0.0,
        pillar: ql.Pillar = ql.Pillar.LastRelevantDate,
        custom_pillar_date: qDate = ql.Date(),
        averaging_method: ql.RateAveraging = ql.RateAveraging.Compound,
        end_of_month: bool = False,
        fixed_payment_frequency: qFrequency = "monthly",
        fixed_calendar: qCalendar = "NullCalendar",
        look_back_days: int = 0,
        lock_out_days: int = 0,
        apply_observation_shift: bool = False,
        pricer: ql.FloatingRateCouponPricer = {},
        rule: ql.DateGeneration = ql.DateGeneration.Backward,
        overnight_calendar: qCalendar = "NullCalendar",
        convention: qBusinessDayConvention = "Modified Following",
        trigger = None
        ) -> ql.OISRateHelper:
    quote_handle = ql.QuoteHandle(ql.SimpleQuote(fixed_rate))
    return ql.OISRateHelper(
        start_date,
        end_date,
        quote_handle,
        overnight_index,
        discounting_curve,
        telescopic_value_dates,
        payment_lag,
        payment_convention,
        payment_frequency,
        payment_calendar,
        overnight_spread,
        pillar,
        custom_pillar_date,
        averaging_method,
        end_of_month,
        fixed_payment_frequency,
        fixed_calendar,
        look_back_days,
        lock_out_days,
        apply_observation_shift,
        pricer,
        rule,
        overnight_calendar,
        convention,
    )
"""

@xlo.func(
    help='Get the swap associated with a QuantLib OISRateHelper.',
    args={
        'ois_rate_helper': 'The QuantLib OISRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlOISRateHelperSwap(ois_rate_helper: ql.OISRateHelper, trigger = None) -> ql.VanillaSwap:
    return ois_rate_helper.swap()

@xlo.func(
    local=False,
    help='Create a QuantLib FxSwapRateHelper object for FX swap rate curve building.',
    args={
        'fwd_point': 'The forward points quote for the FX swap.',
        'spot_fx': 'The spot FX rate quote.',
        'tenor': 'The tenor period of the FX swap.',
        'fixing_days': 'The number of fixing days for the FX swap.',
        'calendar': 'The calendar for the FX swap.',
        'business_day_convention': 'The business day convention for the FX swap.',
        'end_of_month': 'Whether to use the end of month convention.',
        'is_fx_base_currency_collateral_currency': 'Flag indicating if the FX base currency is the collateral currency.',
        'collateral_curve': 'The yield term structure for collateral discounting.',
        'trading_calendar': 'The trading calendar for the FX swap.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxSwapRateHelper(
    fwd_point: qQuoteHandle,
    spot_fx: qQuoteHandle,
    tenor: qPeriod,
    fixing_days: int,
    calendar: qCalendar,
    business_day_convention: qBusinessDayConvention,
    end_of_month: bool,
    is_fx_base_currency_collateral_currency: bool,
    collateral_curve: ql.YieldTermStructureHandle,
    trading_calendar: qCalendar = ql.NullCalendar,
    trigger = None
    ) -> ql.FxSwapRateHelper:
    return ql.FxSwapRateHelper(
        fwd_point,
        spot_fx,
        tenor,
        fixing_days,
        calendar,
        business_day_convention,
        end_of_month,
        is_fx_base_currency_collateral_currency,
        collateral_curve,
        trading_calendar,
    )

# \ToDo constructor not available in this version of quantlib
@xlo.func(
    help='Create a QuantLib FxSwapRateHelper object from dates for FX swap rate curve building.',
    args={
        'fwd_point': 'The forward points quote handle for the FX swap.',
        'spot_fx': 'The spot FX rate quote handle.',
        'start_date': 'The start date of the FX swap.',
        'end_date': 'The end date of the FX swap.',
        'is_fx_base_currency_collateral_currency': 'Flag indicating if the FX base currency is the collateral currency.',
        'collateral_curve': 'The yield term structure for collateral discounting (optional).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxSwapRateHelperForDates(
    fwd_point: qQuoteHandle,
    spot_fx: qQuoteHandle,
    start_date: qDate,
    end_date: qDate,
    is_fx_base_currency_collateral_currency: bool,
    collateral_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger = None
    ) -> ql.FxSwapRateHelper:
    return ql.FxSwapRateHelper(
        fwd_point,
        spot_fx,
        start_date,
        end_date,
        is_fx_base_currency_collateral_currency,
        collateral_curve,
    )

@xlo.func(
    help='Get the spot FX rate from a FxSwapRateHelper object.',
    args={
        'fx_swap_rate_helper': 'The FxSwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxSwapRateHelperSpot(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None) -> float:
    return fx_swap_rate_helper.spot()

@xlo.func(
    help='Get the tenor period from a FxSwapRateHelper object.',
    args={
        'fx_swap_rate_helper': 'The FxSwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxSwapRateHelperTenor(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None) -> ql.Period:
    return fx_swap_rate_helper.tenor()

@xlo.func(
    help='Get the number of fixing days from a FxSwapRateHelper object.',
    args={
        'fx_swap_rate_helper': 'The FxSwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxSwapRateHelperFixingDays(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None) -> int:
    return fx_swap_rate_helper.fixingDays()

@xlo.func(
    help='Get the calendar from a FxSwapRateHelper object.',
    args={
        'fx_swap_rate_helper': 'The FxSwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxSwapRateHelperCalendar(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None) -> ql.Calendar:
    return fx_swap_rate_helper.calendar()

# \ToDo Implementation of a returner for BDC
@xlo.func(
    help='Get the business day convention from a FxSwapRateHelper object.',
    args={
        'fx_swap_rate_helper': 'The FxSwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxSwapRateHelperBusinessDayConvention(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None) -> qBusinessDayConvention:
    return fx_swap_rate_helper.businessDayConvention()

@xlo.func(
    help='Check if the end of month convention is used in a FxSwapRateHelper object.',
    args={
        'fx_swap_rate_helper': 'The FxSwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxSwapRateHelperEndOfMonth(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None) -> bool:
    return fx_swap_rate_helper.endOfMonth()

@xlo.func(
    help='Check if the FX base currency is the collateral currency in a FxSwapRateHelper object.',
    args={
        'fx_swap_rate_helper': 'The FxSwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxSwapRateHelperIsFxBaseCurrencyCollateralCurrency(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None) -> bool:
    return fx_swap_rate_helper.isFxBaseCurrencyCollateralCurrency()

@xlo.func(
    help='Get the trading calendar from a FxSwapRateHelper object.',
    args={
        'fx_swap_rate_helper': 'The FxSwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxSwapRateHelperTradingCalendar(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None) -> ql.Calendar:
    return fx_swap_rate_helper.tradingCalendar()

@xlo.func(
    help='Get the adjustment calendar from a FxSwapRateHelper object.',
    args={
        'fx_swap_rate_helper': 'The FxSwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxSwapRateHelperAdjustmentCalendar(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None) -> ql.Calendar:
    return fx_swap_rate_helper.adjustmentCalendar()

@xlo.func(
    help='Create a QuantLib OvernightIndexFutureRateHelper object for overnight rate curve building.',
    args={
        'price': 'The price quote handle of the overnight index future.',
        'value_date': 'The value date of the future.',
        'maturity_date': 'The maturity date of the future.',
        'index': 'The overnight index (e.g., SOFR, SONIA, EONIA).',
        'convexity_adjustment': 'The convexity adjustment for the future (default: 0.0).',
        'averaging_method': 'The rate averaging method (default: Compound).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexFutureRateHelper(
    price: qQuoteHandle,
    value_date: qDate,
    maturity_date: qDate,
    index: ql.OvernightIndex,
    convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), 
    averaging_method: qRateAveragingType = ql.RateAveraging.Compound,
    trigger = None,
    ) -> ql.OvernightIndexFutureRateHelper:
    return ql.OvernightIndexFutureRateHelper(
        price,
        value_date,
        maturity_date,
        index,
        convexity_adjustment,
        averaging_method
    )

@xlo.func(
    help='Get the convexity adjustement of a FOvernightIndexFutureRateHelper.',
    args={
        'overnight_index_future_rate_helper': 'The QuantLib OvernightIndexFutureRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndexFutureRateHelperConvexityAdjustment(overnight_index_future_rate_helper: ql.OvernightIndexFutureRateHelper, trigger = None) -> float:
    return overnight_index_future_rate_helper.convexityAdjustment()

@xlo.func(
    help='Create a QuantLib SofrFutureRateHelper object for SOFR future rate curve building.',
    args={
        'price': 'The price quote handle of the SOFR future.',
        'reference_month': 'The reference month for the SOFR future.',
        'reference_year': 'The reference year for the SOFR future.',
        'frequency': 'The frequency of the SOFR future (e.g., Monthly, Quarterly).',
        'convexity_adjustment': 'The convexity adjustment quote handle (optional).',
        'pillar': 'The pillar choice for the helper (default: LastRelevantDate).',
        'custom_pillar_date': 'The custom pillar date if pillar choice is Custom (optional).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSofrFutureRateHelper(
    price: qQuoteHandle,
    reference_month: int,
    reference_year: int,
    frequency: qFrequency,
    convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), 
    trigger = None,
    ) -> ql.SofrFutureRateHelper:
    return ql.SofrFutureRateHelper(
            price,
            reference_month,
            reference_year,
            frequency,
            convexity_adjustment, 
    )

@xlo.func(
    help='Create a QuantLib ConstNotionalCrossCurrencySwapRateHelper object for cross-currency swap rate curve building.',
    args={
        'fixed_rate': 'The fixed rate quote handle for the cross-currency swap.',
        'tenor': 'The tenor period of the cross-currency swap.',
        'fixing_days': 'The number of fixing days.',
        'calendar': 'The calendar for the swap.',
        'convention': 'The business day convention for the swap.',
        'endOfMonth': 'Whether to use the end of month convention.',
        'fixed_frequency': 'The frequency of fixed leg payments.',
        'fixedDayCount': 'The day counter for the fixed leg.',
        'float_index': 'The IBOR index for the floating leg.',
        'collateral_curve': 'The yield term structure for collateral discounting.',
        'collateral_on_fixed_leg': 'Flag indicating if collateral is on the fixed leg.',
        'paymentLag': 'The payment lag in days (default: 0).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlConstNotionalCrossCurrencySwapRateHelper(
    fixed_rate: qQuoteHandle,
    tenor: qPeriod,
    fixing_days: int,
    calendar: qCalendar,
    convention: qBusinessDayConvention,
    end_of_month: bool,
    fixed_frequency: qFrequency,
    fixed_day_count: qDayCounter,
    float_index: ql.IborIndex,
    collateral_curve: ql.YieldTermStructureHandle,
    collateral_on_fixed_leg: bool,
    payment_lag: int = 0, 
    trigger = None,
    ) -> ql.ConstNotionalCrossCurrencySwapRateHelper:
    return ql.ConstNotionalCrossCurrencySwapRateHelper(
        fixed_rate,
        tenor,
        fixing_days,
        calendar,
        convention,
        end_of_month,
        fixed_frequency,
        fixed_day_count,
        float_index,
        collateral_curve,
        collateral_on_fixed_leg,
        payment_lag
    )

@xlo.func(
    help='Create a QuantLib ConstNotionalCrossCurrencyBasisSwapRateHelper object for cross-currency basis swap rate curve building.',
    args={
        'basis': 'The basis spread quote handle for the cross-currency basis swap.',
        'tenor': 'The tenor period of the cross-currency basis swap.',
        'fixing_days': 'The number of fixing days.',
        'calendar': 'The calendar for the swap.',
        'convention': 'The business day convention for the swap.',
        'end_of_month': 'Whether to use the end of month convention.',
        'base_currency_index': 'The IBOR index for the base currency leg.',
        'quote_currency_index': 'The IBOR index for the quote currency leg.',
        'collateral_curve': 'The yield term structure for collateral discounting.',
        'is_fx_base_currency_collateral_currency': 'Flag indicating if the FX base currency is the collateral currency.',
        'is_basis_on_fx_base_currency_leg': 'Flag indicating if the basis is on the FX base currency leg.',
        'payment_frequency': 'The payment frequency (default: NoFrequency).',
        'payment_lag': 'The payment lag in days (default: 0).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlConstNotionalCrossCurrencyBasisSwapRateHelper(
    basis: qQuoteHandle,
    tenor: qPeriod,
    fixing_days: int,
    calendar: qCalendar,
    convention: qBusinessDayConvention,
    end_of_month: bool,
    base_currency_index: ql.IborIndex,
    quote_currency_index: ql.IborIndex,
    collateral_curve: ql.YieldTermStructureHandle,
    is_fx_base_currency_collateral_currency: bool,
    is_basis_on_fx_base_currency_leg: bool,
    payment_frequency: qFrequency = ql.NoFrequency,
    payment_lag: int = 0,
    trigger = None,
    ) -> ql.ConstNotionalCrossCurrencyBasisSwapRateHelper:
    return ql.ConstNotionalCrossCurrencyBasisSwapRateHelper(
        basis,
        tenor,
        fixing_days,
        calendar,
        convention,
        end_of_month,
        base_currency_index,
        quote_currency_index,
        collateral_curve,
        is_fx_base_currency_collateral_currency,
        is_basis_on_fx_base_currency_leg,
        payment_frequency, 
        payment_lag
    ) 

@xlo.func(
help='Create a QuantLib MtMCrossCurrencyBasisSwapRateHelper object.',
args={
    'basis': 'The basis-swap spread.',
    'tenor': 'The tenor period of the cross-currency basis swap.',
    'fixing_days': 'The number of fixing days.',
    'calendar': 'The calendar for the swap.',
    'convention': 'The business day convention for the swap.',
    'end_of_month': 'Whether to use the end-of-month convention.',
    'base_currency_index': 'The IBOR index for the base currency leg.',
    'quote_currency_index': 'The IBOR index for the quote currency leg.',
    'collateral_curve': 'The yield term structure handle used for collateral discounting.',
    'is_fx_base_currency_collateral_currency': 'Flag indicating if the FX base currency is the collateral currency.',
    'is_basis_on_fx_base_currency_leg': 'Flag indicating if the basis is on the FX base-currency leg.',
    'is_fx_base_currency_leg_resettable': 'Flag indicating if the FX base-currency leg is resettable.',
    'payment_frequency': 'The payment frequency.',
    'payment_lag': 'The payment lag in days (default: 0).',
},
    group=EXCEL_GROUP_NAME,
)
def qlMtMCrossCurrencyBasisSwapRateHelper(
    basis: qQuoteHandle,
    tenor: qPeriod,
    fixing_days: int,
    calendar: qCalendar,
    convention: qBusinessDayConvention,
    end_of_month: bool,
    base_currency_index: ql.IborIndex,
    quote_currency_index: ql.IborIndex,
    collateral_curve: ql.YieldTermStructureHandle,
    is_fx_base_currency_collateral_currency: bool,
    is_basis_on_fx_base_currency_leg: bool,
    is_fx_base_currency_leg_resettable: bool,
    payment_frequency: qFrequency = ql.NoFrequency,
    payment_lag: int = 0,
    trigger = None,
    ) -> ql.MtMCrossCurrencyBasisSwapRateHelper:
    return ql.MtMCrossCurrencyBasisSwapRateHelper(
        basis,
        tenor,
        fixing_days,
        calendar,
        convention,
        end_of_month,
        base_currency_index,
        quote_currency_index,
        collateral_curve,
        is_fx_base_currency_collateral_currency,
        is_basis_on_fx_base_currency_leg,
        is_fx_base_currency_leg_resettable,
        payment_frequency, 
        payment_lag
    )

@xlo.func(
    help='Create a QuantLib IborIborBasisSwapRateHelper object.',
    args={
        'basis': 'The basis-swap spread quote handle between the two IBOR indices.',
        'tenor': 'The tenor period of the IBOR-IBOR basis swap.',
        'settlement_days': 'The number of settlement days after the trade date.',
        'calendar': 'The calendar for business day conventions.',
        'convention': 'The business day convention for the swap.',
        'end_of_month': 'Whether to use the end-of-month convention.',
        'base_index': 'The IBOR index for the base leg.',
        'other_index': 'The IBOR index for the other leg (e.g., EURIBOR).',
        'discount_handle': 'The yield term structure handle used for discounting.',
        'bootstrap_base_curve': 'Flag indicating if the base curve should be bootstrapped.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlIborIborBasisSwapRateHelper(
    basis: qQuoteHandle,
    tenor: qPeriod,
    settlement_days: int,
    calendar: qCalendar,
    convention: qBusinessDayConvention,
    end_of_month: bool,
    base_index: ql.IborIndex,
    other_index: ql.IborIndex,
    discount_handle: ql.YieldTermStructureHandle,
    bootstrap_base_curve: bool,
    trigger = None,
    ) -> ql.IborIborBasisSwapRateHelper:
    return ql.IborIborBasisSwapRateHelper(
        basis,
        tenor,
        settlement_days,
        calendar,
        convention,
        end_of_month,
        base_index,
        other_index,
        discount_handle,
        bootstrap_base_curve,
    )

@xlo.func(
    help='Get the swap associated with a QuantLib IborIborBasisSwapRateHelper.',
    args={
        'ibor_ibor_basis_swap_rate_helper': 'The QuantLib IborIborBasisSwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlIborIborBasisSwapRateHelperSwap(ibor_ibor_basis_swap_rate_helper: ql.IborIborBasisSwapRateHelper, trigger = None) -> ql.VanillaSwap:
    return ibor_ibor_basis_swap_rate_helper.swap()

@xlo.func(
    help='Create a QuantLib OvernightIborBasisSwapRateHelper object.',
    args={
        'basis': 'The basis-swap spread quote handle between the Overnight and IBOR indices.',
        'tenor': 'The tenor period of the Overnight-IBOR basis swap.',
        'settlement_days': 'The number of settlement days after the trade date.',
        'calendar': 'The calendar for business day conventions.',
        'convention': 'The business day convention for the swap.',
        'end_of_month': 'Whether to use the end-of-month convention.',
        'base_index': 'The Overnight index for the base leg (e.g., SOFR, SONIA).',
        'other_index': 'The IBOR index for the other leg (e.g., USD-LIBOR, GBP-LIBOR).',
        'discount_handle': 'The yield term structure handle used for discounting.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIborBasisSwapRateHelper(
    basis: qQuoteHandle,
    tenor: qPeriod,
    settlement_days: int,
    calendar: qCalendar,
    convention: qBusinessDayConvention,
    end_of_month: bool,
    base_index: ql.IborIndex,
    other_index: ql.IborIndex,
    discount_handle: ql.YieldTermStructureHandle,
    trigger = None,
    ) -> ql.OvernightIborBasisSwapRateHelper:
    return ql.OvernightIborBasisSwapRateHelper(
        basis,
        tenor,
        settlement_days,
        calendar,
        convention,
        end_of_month,
        base_index,
        other_index,
        discount_handle,
    )

@xlo.func(
    help='Get the swap associated with a QuantLib OvernightIborBasisSwapRateHelper.',
    args={
        'overnight_ibor_basis_swap_rate_helper': 'The QuantLib OvernightIborBasisSwapRateHelper object.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIborBasisSwapRateHelperSwap(overnight_ibor_basis_swap_rate_helper: ql.OvernightIborBasisSwapRateHelper, trigger = None) -> ql.VanillaSwap:
    return overnight_ibor_basis_swap_rate_helper.swap()

# \ToDo constructor not available in this version of quantlib
'''
@xlo.func(
    help='Create a QuantLib MultipleResetsSwapRateHelper object for calibrating swaps with multiple resets per coupon.',
    args={
        'settlement_days': 'The number of settlement days after the trade date.',
        'tenor': 'The tenor period of the multiple resets swap.',
        'fixed_rate': 'The quote handle for the fixed rate leg.',
        'ibor_index': 'The IBOR index for the floating rate leg.',
        'resets_per_coupon': 'The number of resets per coupon period.',
        'discounting_curve': 'The yield term structure handle used for discounting (optional, default: empty handle).',
        'averaging_method': 'The rate averaging method (e.g., "Compound", "Simple", default: "Compound").',
        'spread': 'The spread added to the IBOR rate (default: 0.0).',
        'fixed_frequency': 'The payment frequency of the fixed leg (e.g., "Monthly", "Quarterly", default: "Monthly").',
        'fixed_day_count': 'The day count convention for the fixed leg (e.g., "ACTUAL360", "ACTUAL365", default: "ACTUAL360").',
        'fixed_convention': 'The business day convention for the fixed leg (e.g., "ModifiedFollowing", default: "ModifiedFollowing").',
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultipleResetsSwapRateHelper(
        settlement_days: int,
        tenor: qPeriod,
        fixed_rate: qQuoteHandle,
        ibor_index: ql.IborIndex,
        resets_per_coupon: int, #Size resetsPerCoupon,
        discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
        averaging_method: qRateAveragingType = "Compound", 
        spread: float = 0.0, #Spread spread = 0.0,
        fixed_frequency: qFrequency = "Monthly",   # \ToDo default = NoFrequency,
        fixed_day_count: qDayCounter = "ACTUAL360",# \toDo default = DayCounter(),
        fixed_convention: qBusinessDayConvention = "ModifiedFollowing",
        trigger = None,
        ) -> ql.MultipleResetsSwapRateHelper:
        return  ql.MultipleResetsSwapRateHelper(
            settlement_days,
            tenor,
            fixed_rate,
            ibor_index,
            resets_per_coupon,
            discounting_curve,
            averaging_method, 
            spread,
            fixed_frequency,
            fixed_day_count,
            fixed_convention       
        )
'''