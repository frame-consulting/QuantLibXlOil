import QuantLib as ql
import xloil as xlo

from .cashflows import qRateAveragingType
from .config import EXCEL_GROUP_NAME
from .date import qPeriod, _qPeriod, _qDate, qFrequency
from .calendars import qCalendar
from .daycounters import qDayCounter
from .ratehelpers import qQuoteHandle
from .utilities import UNKNOWN_KEY, UNKNOWN_VALUE, enum_value, first_key
from .volatilities import QL_VOLATILITY_TYPE, qVolatilityType


# BlackCalibrationHelper interface

QL_BLACK_CALIBRATION_HELPER_ERROR_TYPE = {
    'RELATIVEPRICE' : ql.BlackCalibrationHelper.RelativePriceError,
    'PRICE' : ql.BlackCalibrationHelper.PriceError,
    'IMPLIEDVOL' : ql.BlackCalibrationHelper.ImpliedVolError,
    UNKNOWN_KEY : UNKNOWN_VALUE,
}


def _qBlackCalibrationHelperErrorType(s: str) -> int:
    return enum_value(s, QL_BLACK_CALIBRATION_HELPER_ERROR_TYPE)

@xlo.converter()
def qBlackCalibrationHelperErrorType(s: str) -> int:
    return _qBlackCalibrationHelperErrorType(s)


@xlo.func(
    help='Set the pricing engine for a BlackCalibrationHelper.',
    args={
        'helper': 'QuantLib BlackCalibrationHelper.',
        'engine': 'QuantLib PricingEngine to use for calibration.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalibrationHelperSetPricingEngine(
    helper: ql.BlackCalibrationHelper,
    engine: ql.PricingEngine,
    trigger=None,
) -> bool:
    helper.setPricingEngine(engine)
    return True

@xlo.func(
    help='Return the market value of a BlackCalibrationHelper.',
    args={
        'helper': 'QuantLib BlackCalibrationHelper.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalibrationHelperMarketValue(
    helper: ql.BlackCalibrationHelper,
    trigger=None,
) -> float:
    return helper.marketValue()

@xlo.func(
    help='Return the model value of a BlackCalibrationHelper.',
    args={
        'helper': 'QuantLib BlackCalibrationHelper.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalibrationHelperModelValue(
    helper: ql.BlackCalibrationHelper,
    trigger=None,
) -> float:
    return helper.modelValue()

@xlo.func(
    help='Return the implied volatility of a BlackCalibrationHelper.',
    args={
        'helper': 'QuantLib BlackCalibrationHelper.',
        'target_value': 'Target value for which to compute implied volatility.',
        'accuracy': 'Accuracy of the implied volatility computation.',
        'max_evaluations': 'Maximum number of evaluations for the implied volatility computation.',
        'min_volatility': 'Minimum allowed volatility.',
        'max_volatility': 'Maximum allowed volatility.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalibrationHelperImpliedVolatility(
    helper: ql.BlackCalibrationHelper,
    target_value: float,
    accuracy: float = 1.0e-8,
    max_evaluations: int = 100,
    min_volatility: float = 1.0e-8,
    max_volatility: float = 4.0,
    trigger=None,
) -> float:
    return helper.impliedVolatility(
        target_value,
        accuracy,
        max_evaluations,
        min_volatility,
        max_volatility
    )

@xlo.func(
    help='Return the black price of a BlackCalibrationHelper.',
    args={
        'helper': 'QuantLib BlackCalibrationHelper.',
        'volatility': 'Volatility for which to compute the black price.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalibrationHelperBlackPrice(
    helper: ql.BlackCalibrationHelper,
    volatility: float,
    trigger=None,
) -> float:
    return helper.blackPrice(volatility)

@xlo.func(
    help='Return the volatility of a BlackCalibrationHelper.',
    args={
        'helper': 'QuantLib BlackCalibrationHelper.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalibrationHelperVolatility(
    helper: ql.BlackCalibrationHelper,
    trigger=None,
) -> ql.QuoteHandle:
    return helper.volatility()

@xlo.func(
    help='Return the type of volatility of a BlackCalibrationHelper as a string.',
    args={
        'helper': 'QuantLib BlackCalibrationHelper.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalibrationHelperVolatilityType(
    helper: ql.BlackCalibrationHelper,
    trigger=None,
) -> str:
    return first_key(QL_VOLATILITY_TYPE, helper.volatilityType())


@xlo.func(
    help='Return the calibration error of a BlackCalibrationHelper.',
    args={
        'helper': 'QuantLib BlackCalibrationHelper.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCalibrationHelperCalibrationError(
    helper: ql.BlackCalibrationHelper,
    trigger=None,
) -> float:
    return helper.calibrationError()


# BlackCalibrationHelper constructors

@xlo.func(
    help='Construct a SwaptionHelper for swaption calibration.',
    args={
        'exercise': 'Exercise period of the swaption (e.g. "5Y").',
        'swap_length': 'Length of the underlying swap (e.g. "10Y").',
        'volatility': 'Volatility quote handle for the swaption.',
        'index': 'Ibor index for the underlying swap.',
        'fixed_leg_tenor': 'Tenor of the fixed leg of the underlying swap (e.g. "1Y").',
        'fixed_leg_day_counter': 'Day count convention for the fixed leg of the underlying swap.',
        'floating_leg_day_counter': 'Day count convention for the floating leg of the underlying swap.',
        'term_structure': 'Yield term structure handle for discounting.',
        'error_type': 'Type of error to use for calibration (e.g. "RelativePriceError").',
        'strike': 'Strike price of the swaption (optional, default is None).',
        'nominal': 'Nominal amount for the swaption (optional, default is 1.0).',
        'volatility_type': 'Type of volatility to use for the swaption (e.g. "ShiftedLognormal").',
        'shift': 'Shift to apply to the underlying rate for shifted volatilities (optional, default is 0.0).',
        'settlement_days': 'Number of settlement days for the swaption (optional, default is None).',
        'averaging_method': 'Averaging method for the swaption (e.g. "Compound").',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionHelper(
    exercise,
    swap_length,
    volatility: qQuoteHandle,
    index: ql.IborIndex,
    fixed_leg_tenor: qPeriod,
    fixed_leg_day_counter: qDayCounter,
    floating_leg_day_counter: qDayCounter,
    term_structure: ql.YieldTermStructureHandle,
    error_type: qBlackCalibrationHelperErrorType = ql.BlackCalibrationHelper.RelativePriceError,
    strike: float = ql.nullDouble(),
    nominal: float = 1.0,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    settlement_days: int = ql.nullInt(),
    averaging_method: qRateAveragingType = ql.RateAveraging.Compound,
    trigger = None,
) -> ql.SwaptionHelper:
    if isinstance(exercise, str):
        exercise = _qPeriod(exercise)
    else:
        exercise = _qDate(exercise)
    #
    if isinstance(swap_length, str):
        # (Period, Period) and (Date, Period)
        swap_length = _qPeriod(swap_length)
    if isinstance(exercise, ql.Date) and not isinstance(swap_length, ql.Period):
        # (Date, Date)
        swap_length = _qDate(swap_length)
    #
    return ql.SwaptionHelper(
        exercise,
        swap_length,
        volatility,
        index,
        fixed_leg_tenor,
        fixed_leg_day_counter,
        floating_leg_day_counter,
        term_structure,
        error_type,
        strike,
        nominal,
        volatility_type,
        shift,
        settlement_days,
        averaging_method,
    )


@xlo.func(
    help='Construct a CapHelper for ATM cap calibration.',
    args={
        'length': 'Length of the cap (e.g. "5Y").',
        'volatility': 'Volatility quote handle for the cap.',
        'index': 'Ibor index for the underlying cap.',
        'fixed_leg_frequency': 'Fair swap rate fixed leg frequency (e.g. "Annual").',
        'fixed_leg_day_counter': 'Fair swap rate fixed leg day count convention.',
        'include_first_swaplet': 'Whether to include the first swaplet in the calibration.',
        'term_structure': 'Yield term structure handle for discounting.',
        'error_type': 'Type of error to use for calibration (e.g. "RelativePriceError").',
        'volatility_type': 'Type of volatility to use for the cap (e.g. "ShiftedLognormal").',
        'shift': 'Shift to apply to the underlying rate for shifted volatilities (optional, default is 0.0).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCapHelper(
    length: qPeriod,
    volatility: qQuoteHandle,
    index: ql.IborIndex,
    fixed_leg_frequency: qFrequency,
    fixed_leg_day_counter: qDayCounter,
    include_first_swaplet: bool,
    term_structure: ql.YieldTermStructureHandle,
    error_type: qBlackCalibrationHelperErrorType = ql.BlackCalibrationHelper.RelativePriceError,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    trigger = None,
) -> ql.CapHelper:
    #
    return ql.CapHelper(
        length,
        volatility,
        index,
        fixed_leg_frequency,
        fixed_leg_day_counter,
        include_first_swaplet,
        term_structure,
        error_type,
        volatility_type,
        shift,
    )


@xlo.func(
    help='Construct a HestonModelHelper for Heston model calibration.',
    args={
        'maturity': 'Maturity of the option (e.g. "5Y").',
        'calendar': 'Calendar for the option maturity.',
        's0': 'Spot price of the underlying asset.',
        'strike_price': 'Strike price of the option.',
        'volatility': 'Volatility quote handle for the option.',
        'risk_free_rate': 'Yield term structure handle for discounting.',
        'dividend_yield': 'Yield term structure handle for dividends.',
        'error_type': 'Type of error to use for calibration (e.g. "RelativePriceError").',
    },
    group=EXCEL_GROUP_NAME,
)
def qlHestonModelHelper(
    maturity: qPeriod,
    calendar: qCalendar,
    s0: float,
    strike_price: float,
    volatility: qQuoteHandle,
    risk_free_rate: ql.YieldTermStructureHandle,
    dividend_yield: ql.YieldTermStructureHandle,
    error_type: qBlackCalibrationHelperErrorType = ql.BlackCalibrationHelper.RelativePriceError,
    trigger = None,
) -> ql.HestonModelHelper:
    return ql.HestonModelHelper(
        maturity,
        calendar,
        s0,
        strike_price,
        volatility,
        risk_free_rate,
        dividend_yield,
        error_type,
    )
