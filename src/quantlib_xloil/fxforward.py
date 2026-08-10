import QuantLib as ql
import xloil as xlo

from .calendars import qCalendar
from .config import EXCEL_GROUP_NAME
from .currencies import qCurrency
from .date import qDate


@xlo.func(
    help="Create a QuantLib FxForward instrument from nominal amounts.",
    args={
        "source_nominal": "The nominal amount in the source currency.",
        "source_currency": "The source currency code (e.g., USD, EUR).",
        "target_nominal": "The nominal amount in the target currency.",
        "target_currency": "The target currency code (e.g., USD, EUR).",
        "maturity_date": "The maturity date of the forward contract.",
        "pay_source_currency": "Whether the source currency is paid (True) or received (False).",
        "settlement_days": "The number of settlement days.",
        "payment_calendar": "The calendar used for payment date adjustment.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForward(
    source_nominal: float,
    source_currency: qCurrency,
    target_nominal: float,
    target_currency: qCurrency,
    maturity_date: qDate,
    pay_source_currency: bool,
    settlement_days: int = 2,
    payment_calendar: qCalendar = None,
    trigger=None,
) -> ql.FxForward:
    if payment_calendar is None:
        payment_calendar = ql.NullCalendar()
    return ql.FxForward(
        source_nominal,
        source_currency,
        target_nominal,
        target_currency,
        maturity_date,
        pay_source_currency,
        settlement_days,
        payment_calendar,
    )


@xlo.func(
    help="Create a QuantLib FxForward instrument from a forward rate.",
    args={
        "source_nominal": "The nominal amount in the source currency.",
        "source_currency": "The source currency code (e.g., USD, EUR).",
        "target_currency": "The target currency code (e.g., USD, EUR).",
        "forward_rate": "The forward exchange rate.",
        "maturity_date": "The maturity date of the forward contract.",
        "pay_source_currency": "Whether the source currency is paid (True) or received (False).",
        "settlement_days": "The number of settlement days.",
        "payment_calendar": "The calendar used for payment date adjustment.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForward2(
    source_nominal: float,
    source_currency: qCurrency,
    target_currency: qCurrency,
    forward_rate: float,
    maturity_date: qDate,
    pay_source_currency: bool,
    settlement_days: int = 2,
    payment_calendar: qCalendar = None,
    trigger=None,
) -> ql.FxForward:
    if payment_calendar is None:
        payment_calendar = ql.NullCalendar()
    return ql.FxForward(
        source_nominal,
        source_currency,
        target_currency,
        forward_rate,
        maturity_date,
        pay_source_currency,
        settlement_days,
        payment_calendar,
    )


@xlo.func(
    help="Get the source nominal amount of a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardSourceNominal(fx_forward: ql.FxForward, trigger=None) -> float:
    return fx_forward.sourceNominal()


@xlo.func(
    help="Get the source currency of a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardSourceCurrency(fx_forward: ql.FxForward, trigger=None) -> ql.Currency:
    return fx_forward.sourceCurrency()


@xlo.func(
    help="Get the target nominal amount of a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardTargetNominal(fx_forward: ql.FxForward, trigger=None) -> float:
    return fx_forward.targetNominal()


@xlo.func(
    help="Get the target currency of a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardTargetCurrency(fx_forward: ql.FxForward, trigger=None) -> ql.Currency:
    return fx_forward.targetCurrency()


@xlo.func(
    help="Get the maturity date of a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardMaturityDate(fx_forward: ql.FxForward, trigger=None) -> ql.Date:
    return fx_forward.maturityDate()


@xlo.func(
    help="Get whether source currency is paid in a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardPaySourceCurrency(fx_forward: ql.FxForward, trigger=None) -> bool:
    return fx_forward.paySourceCurrency()


@xlo.func(
    help="Get the forward rate of a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardForwardRate(fx_forward: ql.FxForward, trigger=None) -> float:
    return fx_forward.forwardRate()


@xlo.func(
    help="Get the settlement days of a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardSettlementDays(fx_forward: ql.FxForward, trigger=None) -> int:
    return fx_forward.settlementDays()


@xlo.func(
    help="Get the settlement calendar of a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardSettlementCalendar(fx_forward: ql.FxForward, trigger=None) -> ql.Calendar:
    return fx_forward.settlementCalendar()


@xlo.func(
    help="Get the settlement date of a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardSettlementDate(fx_forward: ql.FxForward, trigger=None) -> ql.Date:
    return fx_forward.settlementDate()


@xlo.func(
    help="Get the fair forward rate of a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardFairForwardRate(fx_forward: ql.FxForward, trigger=None) -> float:
    return fx_forward.fairForwardRate()


@xlo.func(
    help="Get the NPV in source currency of a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardNpvSourceCurrency(fx_forward: ql.FxForward, trigger=None) -> float:
    return fx_forward.npvSourceCurrency()


@xlo.func(
    help="Get the NPV in target currency of a QuantLib FxForward.",
    args={
        "fx_forward": "The QuantLib FxForward object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFxForwardNpvTargetCurrency(fx_forward: ql.FxForward, trigger=None) -> float:
    return fx_forward.npvTargetCurrency()


@xlo.func(
    help="Create a QuantLib DiscountingFxForwardEngine.",
    args={
        "source_currency_discount_curve": "The yield term structure for the source currency.",
        "target_currency_discount_curve": "The yield term structure for the target currency.",
        "spot_fx": "The spot FX rate (source/target).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDiscountingFxForwardEngine(
    source_currency_discount_curve: ql.YieldTermStructureHandle,
    target_currency_discount_curve: ql.YieldTermStructureHandle,
    spot_fx: float,
    trigger=None,
) -> ql.DiscountingFxForwardEngine:
    spot_fx_quote = ql.SimpleQuote(spot_fx)
    spot_fx_handle = ql.QuoteHandle(spot_fx_quote)
    return ql.DiscountingFxForwardEngine(
        source_currency_discount_curve,
        target_currency_discount_curve,
        spot_fx_handle,
    )
