import QuantLib as ql
import xloil as xlo
from typing import Optional

from .config import EXCEL_GROUP_NAME
from .daycounters import qDayCounter
from .ratehelpers import qQuoteHandle
from .swap import QL_SWAP_TYPE
from .utilities import enum_value, first_key, UNKNOWN_KEY, UNKNOWN_VALUE
from .volatilities import qVolatilityType

# Settlement types

QL_SETTLEMENT_TYPE = {
    "CASH": ql.Settlement.Cash,
    "PHYSICAL": ql.Settlement.Physical,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_SETTLEMENT_METHOD = {
    "CASH": ql.Settlement.Cash,
    "COLLATERALIZEDCASHPRICE": ql.Settlement.CollateralizedCashPrice,
    "PARYIELDCURVE": ql.Settlement.ParYieldCurve,
    "PHYSICALCLEARED": ql.Settlement.PhysicalCleared,
    "PHYSICALOTC": ql.Settlement.PhysicalOTC,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_SWAPTION_PRICE_TYPE = {
    "FORWARD": ql.Swaption.Forward,
    "SPOT": ql.Swaption.Spot,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_CASH_ANNUITY_MODEL = {
    "DISCOUNTCURVE": ql.BlackSwaptionEngine.DiscountCurve,
    "SWAPRATE": ql.BlackSwaptionEngine.SwapRate,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


# Converter functions


def _qSettlementType(s: str) -> int:
    return enum_value(s, QL_SETTLEMENT_TYPE)


@xlo.converter()
def qSettlementType(s: str) -> int:
    return _qSettlementType(s)


def _qSettlementMethod(s: str) -> int:
    return enum_value(s, QL_SETTLEMENT_METHOD)


@xlo.converter()
def qSettlementMethod(s: str) -> int:
    return _qSettlementMethod(s)


def _qSwaptionPriceType(s: str) -> int:
    return enum_value(s, QL_SWAPTION_PRICE_TYPE)


@xlo.converter()
def qSwaptionPriceType(s: str) -> int:
    return _qSwaptionPriceType(s)


def _qCashAnnuityModel(s: str) -> int:
    return enum_value(s, QL_CASH_ANNUITY_MODEL)


@xlo.converter()
def qCashAnnuityModel(s: str) -> int:
    return _qCashAnnuityModel(s)


# Swaption interface


@xlo.func(
    help="Create a QuantLib Swaption object.",
    args={
        "swap": "QuantLib fixed vs floating swap.",
        "exercise": "QuantLib exercise.",
        "settlement_type": "Settlement type ('Physical' or 'Cash').",
        "settlement_method": "Settlement method ('PhysicalOTC', 'PhysicalCleared', 'CollateralizedCashPrice', 'ParYieldCurve').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaption(
    swap: ql.FixedVsFloatingSwap,
    exercise: ql.Exercise,
    settlement_type: qSettlementType = ql.Settlement.Physical,
    settlement_method: qSettlementMethod = ql.Settlement.PhysicalOTC,
    trigger=None,
) -> ql.Swaption:
    return ql.Swaption(swap, exercise, settlement_type, settlement_method)


@xlo.func(
    help="Return the settlement type of a swaption.",
    args={
        "swaption": "QuantLib Swaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionSettlementType(swaption: ql.Swaption, trigger=None) -> str:
    return first_key(QL_SETTLEMENT_TYPE, swaption.settlementType(), UNKNOWN_VALUE)


@xlo.func(
    help="Return the settlement method of a swaption.",
    args={
        "swaption": "QuantLib Swaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionSettlementMethod(swaption: ql.Swaption, trigger=None) -> str:
    return first_key(QL_SETTLEMENT_METHOD, swaption.settlementMethod(), UNKNOWN_VALUE)


@xlo.func(
    help="Return the underlying swap type of a swaption.",
    args={
        "swaption": "QuantLib Swaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionType(swaption: ql.Swaption, trigger=None) -> str:
    return first_key(QL_SWAP_TYPE, swaption.type(), UNKNOWN_VALUE)


@xlo.func(
    help="Return the underlying swap of a swaption.",
    args={
        "swaption": "QuantLib Swaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionUnderlying(swaption: ql.Swaption, trigger=None):
    return swaption.underlying()


@xlo.func(
    help="Calculate the implied volatility for a swaption.",
    args={
        "swaption": "QuantLib Swaption object.",
        "price": "The target price of the swaption.",
        "discount_curve": "Handle to the yield term structure for discounting.",
        "guess": "Initial guess for the volatility.",
        "accuracy": "Solver accuracy.",
        "max_evaluations": "Maximum number of evaluations.",
        "min_vol": "Minimum volatility bound.",
        "max_vol": "Maximum volatility bound.",
        "volatility_type": "Type of volatility (e.g., 'ShiftedLognormal' or 'Normal').",
        "displacement": "Displacement for shifted lognormal model.",
        "price_type": "Price type ('Spot' or 'Forward').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionImpliedVolatility(
    swaption: ql.Swaption,
    price: float,
    discount_curve: ql.YieldTermStructureHandle,
    guess: float,
    accuracy: float = 1.0e-4,
    max_evaluations: int = 100,
    min_vol: float = 1.0e-7,
    max_vol: float = 4.0,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    displacement: float = 0.0,
    price_type: qSwaptionPriceType = ql.Swaption.Spot,
    trigger=None,
) -> float:
    return swaption.impliedVolatility(
        price,
        discount_curve,
        guess,
        accuracy,
        max_evaluations,
        min_vol,
        max_vol,
        volatility_type,
        displacement,
        price_type,
    )


@xlo.func(
    help="Return the vega of a swaption.",
    args={
        "swaption": "QuantLib Swaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVega(swaption: ql.Swaption, trigger=None) -> float:
    return swaption.vega()


@xlo.func(
    help="Return the delta of a swaption.",
    args={
        "swaption": "QuantLib Swaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionDelta(swaption: ql.Swaption, trigger=None) -> float:
    return swaption.delta()


@xlo.func(
    help="Return the annuity of a swaption.",
    args={
        "swaption": "QuantLib Swaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionAnnuity(swaption: ql.Swaption, trigger=None) -> float:
    return swaption.annuity()


@xlo.func(
    help="Return the forward price of a swaption.",
    args={
        "swaption": "QuantLib Swaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionForwardPrice(swaption: ql.Swaption, trigger=None) -> float:
    return swaption.forwardPrice()


# NonstandardSwaption interface


@xlo.func(
    help="Create a QuantLib NonstandardSwaption object.",
    args={
        "swap": "QuantLib nonstandard swap.",
        "exercise": "QuantLib exercise.",
        "settlement_type": "Settlement type ('Physical' or 'Cash').",
        "settlement_method": "Settlement method ('PhysicalOTC', 'PhysicalCleared', 'CollateralizedCashPrice', 'ParYieldCurve').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwaption(
    swap: ql.NonstandardSwap,
    exercise: ql.Exercise,
    settlement_type: qSettlementType = ql.Settlement.Physical,
    settlement_method: qSettlementMethod = ql.Settlement.PhysicalOTC,
    trigger=None,
) -> ql.NonstandardSwaption:
    return ql.NonstandardSwaption(swap, exercise, settlement_type, settlement_method)


@xlo.func(
    help="Return the underlying nonstandard swap of a nonstandard swaption.",
    args={
        "swaption": "QuantLib NonstandardSwaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwaptionUnderlyingSwap(
    swaption: ql.NonstandardSwaption, trigger=None
) -> ql.NonstandardSwap:
    return swaption.underlyingSwap()


@xlo.func(
    help="Return the probabilities for a nonstandard swaption.",
    args={
        "swaption": "QuantLib NonstandardSwaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwaptionProbabilities(
    swaption: ql.NonstandardSwaption, trigger=None
) -> list[float]:
    return list(swaption.probabilities())


@xlo.func(
    help="Create a calibration basket for a nonstandard swaption.",
    args={
        "swaption": "QuantLib NonstandardSwaption object.",
        "swap_index": "Swap index for the calibration.",
        "swaption_volatility": "Swaption volatility structure for the calibration.",
        "type_str": "Calibration basket type ('Naive' or 'MaturityStrikeByDeltaGamma').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNonstandardSwaptionCalibrationBasket(
    swaption: ql.NonstandardSwaption,
    swap_index,
    swaption_volatility: ql.SwaptionVolatilityStructureHandle,
    type_str: str = "Naive",
    trigger=None,
) -> list:
    return swaption.calibrationBasket(swap_index, swaption_volatility, type_str)


# FloatFloatSwaption interface


@xlo.func(
    help="Create a QuantLib FloatFloatSwaption object.",
    args={
        "swap": "QuantLib float-float swap.",
        "exercise": "QuantLib exercise.",
        "delivery": "Settlement type ('Physical' or 'Cash').",
        "settlement_method": "Settlement method ('PhysicalOTC', 'PhysicalCleared', 'CollateralizedCashPrice', 'ParYieldCurve').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatFloatSwaption(
    swap,
    exercise,
    delivery: qSettlementType = ql.Settlement.Physical,
    settlement_method: qSettlementMethod = ql.Settlement.PhysicalOTC,
    trigger=None,
) -> ql.FloatFloatSwaption:
    return ql.FloatFloatSwaption(swap, exercise, delivery, settlement_method)


@xlo.func(
    help="Return the underlying float-float swap of a float-float swaption.",
    args={
        "swaption": "QuantLib FloatFloatSwaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatFloatSwaptionUnderlyingSwap(
    swaption: ql.FloatFloatSwaption, trigger=None
) -> ql.FloatFloatSwap:
    return swaption.underlyingSwap()


@xlo.func(
    help="Return the underlying value of a float-float swaption.",
    args={
        "swaption": "QuantLib FloatFloatSwaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatFloatSwaptionUnderlyingValue(
    swaption: ql.FloatFloatSwaption, trigger=None
) -> float:
    return swaption.underlyingValue()


@xlo.func(
    help="Return the probabilities for a float-float swaption.",
    args={
        "swaption": "QuantLib FloatFloatSwaption object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatFloatSwaptionProbabilities(
    swaption: ql.FloatFloatSwaption, trigger=None
) -> list[float]:
    return list(swaption.probabilities())


@xlo.func(
    help="Create a calibration basket for a float-float swaption.",
    args={
        "swaption": "QuantLib FloatFloatSwaption object.",
        "swap_index": "Swap index for the calibration.",
        "swaption_volatility": "Swaption volatility structure for the calibration.",
        "type_str": "Calibration basket type ('Naive' or 'MaturityStrikeByDeltaGamma').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFloatFloatSwaptionCalibrationBasket(
    swaption: ql.FloatFloatSwaption,
    swap_index,
    swaption_volatility: ql.SwaptionVolatilityStructureHandle,
    type_str: str = "Naive",
    trigger=None,
) -> list:
    return swaption.calibrationBasket(swap_index, swaption_volatility, type_str)


# Pricing engines


@xlo.func(
    help="Create a Black swaption pricing engine with volatility term structure.",
    args={
        "discount_curve": "Handle to the yield term structure for discounting.",
        "swaption_volatility": "Handle to the swaption volatility structure.",
        "model": "Cash annuity model ('DiscountCurve' or 'SwapRate').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackSwaptionEngine(
    discount_curve: ql.YieldTermStructureHandle,
    swaption_volatility: ql.SwaptionVolatilityStructureHandle,
    model: qCashAnnuityModel = ql.BlackSwaptionEngine.DiscountCurve,
    trigger=None,
) -> ql.BlackSwaptionEngine:
    return ql.BlackSwaptionEngine(discount_curve, swaption_volatility, model)


@xlo.func(
    help="Create a Black swaption pricing engine with constant volatility.",
    args={
        "discount_curve": "Handle to the yield term structure for discounting.",
        "volatility": "Handle to the volatility quote.",
        "day_counter": "Day count convention.",
        "displacement": "Displacement for shifted lognormal model.",
        "model": "Cash annuity model ('DiscountCurve' or 'SwapRate').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackSwaptionEngineFromQuote(
    discount_curve: ql.YieldTermStructureHandle,
    volatility: qQuoteHandle,
    day_counter: qDayCounter = ql.Actual365Fixed(),
    displacement: float = 0.0,
    model: qCashAnnuityModel = ql.BlackSwaptionEngine.DiscountCurve,
    trigger=None,
) -> ql.BlackSwaptionEngine:
    return ql.BlackSwaptionEngine(
        discount_curve, volatility, day_counter, displacement, model
    )


@xlo.func(
    help="Create a Bachelier swaption pricing engine with volatility term structure.",
    args={
        "discount_curve": "Handle to the yield term structure for discounting.",
        "swaption_volatility": "Handle to the swaption volatility structure.",
        "model": "Cash annuity model ('DiscountCurve' or 'SwapRate').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierSwaptionEngine(
    discount_curve: ql.YieldTermStructureHandle,
    swaption_volatility: ql.SwaptionVolatilityStructureHandle,
    model: qCashAnnuityModel = ql.BachelierSwaptionEngine.DiscountCurve,
    trigger=None,
) -> ql.BachelierSwaptionEngine:
    return ql.BachelierSwaptionEngine(discount_curve, swaption_volatility, model)


@xlo.func(
    help="Create a Bachelier swaption pricing engine with constant volatility.",
    args={
        "discount_curve": "Handle to the yield term structure for discounting.",
        "volatility": "Handle to the volatility quote.",
        "day_counter": "Day count convention.",
        "model": "Cash annuity model ('DiscountCurve' or 'SwapRate').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierSwaptionEngineFromQuote(
    discount_curve: ql.YieldTermStructureHandle,
    volatility: qQuoteHandle,
    day_counter: qDayCounter = ql.Actual365Fixed(),
    model: qCashAnnuityModel = ql.BachelierSwaptionEngine.DiscountCurve,
    trigger=None,
) -> ql.BachelierSwaptionEngine:
    return ql.BachelierSwaptionEngine(discount_curve, volatility, day_counter, model)


# TODO: add MakeSwaption helper
