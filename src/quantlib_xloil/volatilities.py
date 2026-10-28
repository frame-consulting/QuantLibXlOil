import QuantLib as ql
import xloil as xlo

from .calendars import (
    QL_BUSINESSDAYCONVENTION,
    qBusinessDayConvention,
    qCalendar,
)
from .config import EXCEL_GROUP_NAME
from .date import qDate, qPeriod, _to_date_list
from .daycounters import qDayCounter
from quantlib_xloil.payoffs import qOptionType
from .ratehelpers import qQuoteHandle
from .utilities import (
    enum_value,
    UNKNOWN_KEY,
    UNKNOWN_VALUE,
    first_key,
    to_bool_list,
    to_float_matrix,
    to_float_list,
)

QL_BLACK_VOL_TIME_EXTRAPOLATION = {
    "FLATVOLATILITY": ql.BlackVolTimeExtrapolation.FlatVolatility,
    "USEINTERPOLATOR": ql.BlackVolTimeExtrapolation.UseInterpolator,
    "LINEARVARIANCE": ql.BlackVolTimeExtrapolation.LinearVariance,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_VOLATILITY_TYPE = {
    "NORMAL": ql.Normal,
    "SHIFTEDLOGNORMAL": ql.ShiftedLognormal,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qBlackVolTimeExtrapolation(s: str) -> int:
    return enum_value(s, QL_BLACK_VOL_TIME_EXTRAPOLATION)


@xlo.converter()
def qBlackVolTimeExtrapolation(s: str) -> int:
    return _qBlackVolTimeExtrapolation(s)


def _qVolatilityType(s: str) -> int:
    return enum_value(s, QL_VOLATILITY_TYPE)


@xlo.converter()
def qVolatilityType(s: str) -> int:
    return _qVolatilityType(s)


def _to_quote_handle_matrix(values) -> list[list[ql.QuoteHandle]]:
    if values is None:
        return []
    rows = values.tolist() if hasattr(values, "tolist") else values
    result = []
    for row_index, row in enumerate(rows):
        converted_row = []
        for column_index, value in enumerate(row):
            try:
                converted_row.append(qQuoteHandle.__wrapped__(value))
            except (TypeError, ValueError) as error:
                raise ValueError(
                    f"Invalid quote at row {row_index}, column {column_index}: {value!r}"
                ) from error
        result.append(converted_row)
    return result


# TODO returner for qVolatilityType

# SmileSection functions (from SWIG SmileSection class)


@xlo.func(
    help="Return the minimum strike of a smile section.",
    args={"smile": "The smile section to query."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionMinStrike(smile: ql.SmileSection, trigger=None) -> float:
    return smile.minStrike()


@xlo.func(
    help="Return the maximum strike of a smile section.",
    args={"smile": "The smile section to query."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionMaxStrike(smile: ql.SmileSection, trigger=None) -> float:
    return smile.maxStrike()


@xlo.func(
    help="Return the ATM level of a smile section.",
    args={"smile": "The smile section to query."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionAtmLevel(smile: ql.SmileSection, trigger=None) -> float:
    return smile.atmLevel()


@xlo.func(
    help="Return the variance of a smile section at a strike.",
    args={"smile": "The smile section to query.", "strike": "The strike."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionVariance(
    smile: ql.SmileSection, strike: float, trigger=None
) -> float:
    return smile.variance(strike)


@xlo.func(
    help="Return the volatility of a smile section at a strike.",
    args={"smile": "The smile section to query.", "strike": "The strike."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionVolatility(
    smile: ql.SmileSection, strike: float, trigger=None
) -> float:
    return smile.volatility(strike)


@xlo.func(
    help="Return the volatility of a smile section at a strike for a specific volatility type.",
    args={
        "smile": "The smile section to query.",
        "strike": "The strike.",
        "volatility_type": "The volatility type.",
        "shift": "The shift for shifted-lognormal volatility.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionVolatility2(
    smile: ql.SmileSection,
    strike: float,
    volatility_type: qVolatilityType,
    shift: float = 0.0,
    trigger=None,
) -> float:
    return smile.volatility(strike)


@xlo.func(
    help="Return the exercise date of a smile section.",
    args={"smile": "The smile section to query."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionExerciseDate(smile: ql.SmileSection, trigger=None) -> ql.Date:
    return smile.exerciseDate()


@xlo.func(
    help="Return the volatility type of a smile section.",
    args={"smile": "The smile section to query."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionVolatilityType(smile: ql.SmileSection, trigger=None) -> int:
    return smile.volatilityType()


@xlo.func(
    help="Return the shift of a smile section.",
    args={"smile": "The smile section to query."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionShift(smile: ql.SmileSection, trigger=None) -> float:
    return smile.shift()


@xlo.func(
    help="Return the reference date of a smile section.",
    args={"smile": "The smile section to query."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionReferenceDate(smile: ql.SmileSection, trigger=None) -> ql.Date:
    return smile.referenceDate()


@xlo.func(
    help="Return the exercise time of a smile section.",
    args={"smile": "The smile section to query."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionExerciseTime(smile: ql.SmileSection, trigger=None) -> float:
    return smile.exerciseTime()


@xlo.func(
    help="Return the day counter of a smile section.",
    args={"smile": "The smile section to query."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionDayCounter(smile: ql.SmileSection, trigger=None) -> ql.DayCounter:
    return smile.dayCounter()


@xlo.func(
    help="Return the option price implied by a smile section.",
    args={
        "smile": "The smile section to query.",
        "strike": "The option strike.",
        "option_type": "The option type.",
        "discount": "The discount factor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionOptionPrice(
    smile: ql.SmileSection,
    strike: float,
    option_type: qOptionType = ql.Option.Call,
    discount: float = 1.0,
    trigger=None,
) -> float:
    return smile.optionPrice(strike, option_type, discount)


@xlo.func(
    help="Return the price of a digital option implied by a smile section.",
    args={
        "smile": "The smile section to query.",
        "strike": "The option strike.",
        "option_type": "The option type.",
        "discount": "The discount factor.",
        "gap": "The gap used for numerical differentiation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionDigitalOptionPrice(
    smile: ql.SmileSection,
    strike: float,
    option_type: int = ql.Option.Call,
    discount: float = 1.0,
    gap: float = 1e-4,
    trigger=None,
) -> float:
    return smile.digitalOptionPrice(strike, option_type, discount)


@xlo.func(
    help="Return the vega of a smile section at a strike.",
    args={
        "smile": "The smile section to query.",
        "strike": "The option strike.",
        "discount": "The discount factor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionVega(
    smile: ql.SmileSection,
    strike: float,
    discount: float = 1.0,
    trigger=None,
) -> float:
    return smile.vega(strike, discount)


@xlo.func(
    help="Return the density of a smile section at a strike.",
    args={"smile": "The smile section to query.", "strike": "The strike."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionDensity(smile: ql.SmileSection, strike: float, trigger=None) -> float:
    return smile.density(strike)


@xlo.func(
    help="Create a risk-neutral density calculator from a smile section.",
    args={
        "smile": "The smile section.",
        "n_strikes": "Number of strikes used for the calculation.",
        "n_std": "Number of standard deviations used for the calculation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionRNDCalculator(
    smile: ql.SmileSection, n_strikes: int = 200, n_std: float = 5.0, trigger=None
) -> ql.SmileSectionRNDCalculator:
    return ql.SmileSectionRNDCalculator(smile, n_strikes, n_std)


@xlo.func(
    help="Return the risk-neutral density at a value.",
    args={"calculator": "The density calculator.", "value": "The value."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionRNDCalculatorPDF(
    calculator: ql.SmileSectionRNDCalculator, value: float, trigger=None
) -> float:
    return calculator.pdf(value)


@xlo.func(
    help="Return the cumulative risk-neutral probability at a value.",
    args={"calculator": "The density calculator.", "value": "The value."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionRNDCalculatorCDF(
    calculator: ql.SmileSectionRNDCalculator, value: float, trigger=None
) -> float:
    return calculator.cdf(value)


@xlo.func(
    help="Return the inverse cumulative risk-neutral probability.",
    args={"calculator": "The density calculator.", "probability": "The probability."},
    group=EXCEL_GROUP_NAME,
)
def qlSmileSectionRNDCalculatorInverseCDF(
    calculator: ql.SmileSectionRNDCalculator, probability: float, trigger=None
) -> float:
    return calculator.invcdf(probability)


# VolatilityTermStructure class
# TODO add functions for VolatilityTermStructure class


# BlackVolTermStructure functions (from SWIG BlackVolTermStructure class)


@xlo.func(
    help="Returns the minimum strike for which the volatility is defined.",
    args={"vol_tsh": "Handle to a BlackVolTermStructure object."},
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureMinStrike(
    vol_tsh: ql.BlackVolTermStructureHandle, trigger=None
) -> float:
    return vol_tsh.minStrike()


@xlo.func(
    help="Returns the maximum strike for which the volatility is defined.",
    args={"vol_tsh": "Handle to a BlackVolTermStructure object."},
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureMaxStrike(
    vol_tsh: ql.BlackVolTermStructureHandle, trigger=None
) -> float:
    return vol_tsh.maxStrike()


@xlo.func(
    help="Returns the Black volatility for a given expiry and strike.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object.",
        "expiry_date": "Option expiry date.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureBlackVol(
    vol_tsh: ql.BlackVolTermStructureHandle,
    expiry_date: qDate,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.blackVol(expiry_date, strike, extrapolate)


@xlo.func(
    help="Returns the Black volatility for a given expiry time and strike.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object.",
        "expiry_time": "Option expiry time.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureBlackVolFromTime(
    vol_tsh: ql.BlackVolTermStructureHandle,
    expiry_time: float,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.blackVol(expiry_time, strike, extrapolate)


@xlo.func(
    help="Returns the Black variance for a given expiry and strike.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object.",
        "expiry_date": "Option expiry date.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureBlackVariance(
    vol_tsh: ql.BlackVolTermStructureHandle,
    expiry_date: qDate,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.blackVariance(expiry_date, strike, extrapolate)


@xlo.func(
    help="Returns the Black variance for a given expiry time and strike.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object.",
        "expiry_time": "Option expiry time.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureBlackVarianceFromTime(
    vol_tsh: ql.BlackVolTermStructureHandle,
    expiry_time: float,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.blackVariance(expiry_time, strike, extrapolate)


@xlo.func(
    help="Returns the Black forward volatility for a given start and end date and strike.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object.",
        "date_start": "Start date of the forward period.",
        "date_end": "End date of the forward period.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureBlackForwardVol(
    vol_tsh: ql.BlackVolTermStructureHandle,
    date_start: qDate,
    date_end: qDate,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.blackForwardVol(date_start, date_end, strike, extrapolate)


@xlo.func(
    help="Returns the Black forward volatility for a given start and end time and strike.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object.",
        "time_start": "Start time of the forward period.",
        "time_end": "End time of the forward period.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureBlackForwardVolFromTime(
    vol_tsh: ql.BlackVolTermStructureHandle,
    time_start: float,
    time_end: float,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.blackForwardVol(time_start, time_end, strike, extrapolate)


@xlo.func(
    help="Returns the Black forward variance for a given start and end date and strike.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object.",
        "date_start": "Start date of the forward period.",
        "date_end": "End date of the forward period.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureBlackForwardVariance(
    vol_tsh: ql.BlackVolTermStructureHandle,
    date_start: qDate,
    date_end: qDate,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.blackForwardVariance(date_start, date_end, strike, extrapolate)


@xlo.func(
    help="Returns the Black forward variance for a given start and end time and strike.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object.",
        "time_start": "Start time of the forward period.",
        "time_end": "End time of the forward period.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureBlackForwardVarianceFromTime(
    vol_tsh: ql.BlackVolTermStructureHandle,
    time_start: float,
    time_end: float,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.blackForwardVariance(time_start, time_end, strike, extrapolate)


@xlo.func(
    help="Return the smile section for a Black volatility term structure.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object.",
        "maturity": "The smile maturity date.",
        "extrapolate": "Whether to allow extrapolation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureSmileSection(
    vol_tsh: ql.BlackVolTermStructureHandle,
    maturity: qDate,
    extrapolate: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return vol_tsh.smileSection(maturity, extrapolate)


@xlo.func(
    help="Return the smile section for a Black volatility term structure at a time.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object.",
        "maturity": "The smile maturity time.",
        "extrapolate": "Whether to allow extrapolation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureSmileSectionFromTime(
    vol_tsh: ql.BlackVolTermStructureHandle,
    maturity: float,
    extrapolate: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return vol_tsh.smileSection(maturity, extrapolate)


@xlo.func(
    help="Return the ATM level for a Black volatility term structure.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object.",
        "time": "The maturity time.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureAtmLevel(
    vol_tsh: ql.BlackVolTermStructureHandle, time: float, trigger=None
) -> float:
    return vol_tsh.atmLevel(time)


# LocalVolTermStructure interface


@xlo.func(
    help="Returns the local volatility for a given expiry date and strike.",
    args={
        "vol_tsh": "Handle to a LocalVolTermStructure object.",
        "expiry_date": "Expiry date for the volatility.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLocalVolTermStructureLocalVol(
    vol_tsh: ql.LocalVolTermStructureHandle,
    expiry_date: qDate,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.localVol(expiry_date, strike, extrapolate)


@xlo.func(
    help="Returns the local volatility for a given expiry time and strike.",
    args={
        "vol_tsh": "Handle to a LocalVolTermStructure object.",
        "expiry_time": "Expiry time for the volatility.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLocalVolTermStructureLocalVolFromTime(
    vol_tsh: ql.LocalVolTermStructureHandle,
    expiry_time: float,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.localVol(expiry_time, strike, extrapolate)


# OptionletVolatilityStructure interface


@xlo.func(
    help="Returns the volatility for a given option date and strike.",
    args={
        "vol_tsh": "Handle to an OptionletVolatilityStructure object.",
        "option_date": "Option expiry date.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOptionletVolatilityStructureVolatility(
    vol_tsh: ql.OptionletVolatilityStructureHandle,
    option_date: qDate,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.volatility(option_date, strike, extrapolate)


@xlo.func(
    help="Returns the volatility for a given option time and strike.",
    args={
        "vol_tsh": "Handle to an OptionletVolatilityStructure object.",
        "option_time": "Option expiry time.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOptionletVolatilityStructureVolatilityFromTime(
    vol_tsh: ql.OptionletVolatilityStructureHandle,
    option_time: float,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.volatility(option_time, strike, extrapolate)


@xlo.func(
    help="Returns the Black variance for a given option date and strike.",
    args={
        "vol_tsh": "Handle to an OptionletVolatilityStructure object.",
        "option_date": "Option expiry date.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOptionletVolatilityStructureBlackVariance(
    vol_tsh: ql.OptionletVolatilityStructureHandle,
    option_date: qDate,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.blackVariance(option_date, strike, extrapolate)


@xlo.func(
    help="Returns the Black variance for a given option time and strike.",
    args={
        "vol_tsh": "Handle to an OptionletVolatilityStructure object.",
        "option_time": "Option expiry time.",
        "strike": "Option strike price.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOptionletVolatilityStructureBlackVarianceFromTime(
    vol_tsh: ql.OptionletVolatilityStructureHandle,
    option_time: float,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.blackVariance(option_time, strike, extrapolate)


# YoYOptionletVolatilitySurface interface


@xlo.func(
    help="Returns the observation lag for a given YoY optionlet volatility surface.",
    args={
        "vol_tsh": "Handle to a YoYOptionletVolatilitySurface object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletVolatilitySurfaceObservationLag(
    vol_tsh: ql.YoYOptionletVolatilitySurfaceHandle, trigger=None
) -> ql.Period:
    return vol_tsh.observationLag()


@xlo.func(
    help="Returns the frequency for a given YoY optionlet volatility surface.",
    args={
        "vol_tsh": "Handle to a YoYOptionletVolatilitySurface object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletVolatilitySurfaceFrequency(
    vol_tsh: ql.YoYOptionletVolatilitySurfaceHandle, trigger=None
) -> float:
    return vol_tsh.frequency()


@xlo.func(
    help="Returns whether the index is interpolated for a given YoY optionlet volatility surface.",
    args={
        "vol_tsh": "Handle to a YoYOptionletVolatilitySurface object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletVolatilitySurfaceIndexIsInterpolated(
    vol_tsh: ql.YoYOptionletVolatilitySurfaceHandle, trigger=None
) -> bool:
    return vol_tsh.indexIsInterpolated()


@xlo.func(
    help="Returns the base date for a given YoY optionlet volatility surface.",
    args={
        "vol_tsh": "Handle to a YoYOptionletVolatilitySurface object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletVolatilitySurfaceBaseDate(
    vol_tsh: ql.YoYOptionletVolatilitySurfaceHandle, trigger=None
) -> ql.Date:
    return vol_tsh.baseDate()


@xlo.func(
    help="Returns the time from base date for a given YoY optionlet volatility surface and date.",
    args={
        "vol_tsh": "Handle to a YoYOptionletVolatilitySurface object.",
        "date": "Date for which to calculate the time from base date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletVolatilitySurfaceTimeFromBaseDate(
    vol_tsh: ql.YoYOptionletVolatilitySurfaceHandle, date: ql.Date, trigger=None
) -> float:
    return vol_tsh.timeFromBaseDate(date)


@xlo.func(
    help="Returns the minimum strike for a given YoY optionlet volatility surface.",
    args={
        "vol_tsh": "Handle to a YoYOptionletVolatilitySurface object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletVolatilitySurfaceMinStrike(
    vol_tsh: ql.YoYOptionletVolatilitySurfaceHandle, trigger=None
) -> float:
    return vol_tsh.minStrike()


@xlo.func(
    help="Returns the maximum strike for a given YoY optionlet volatility surface.",
    args={
        "vol_tsh": "Handle to a YoYOptionletVolatilitySurface object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletVolatilitySurfaceMaxStrike(
    vol_tsh: ql.YoYOptionletVolatilitySurfaceHandle, trigger=None
) -> float:
    return vol_tsh.maxStrike()


@xlo.func(
    help="Returns the base level for a given YoY optionlet volatility surface.",
    args={
        "vol_tsh": "Handle to a YoYOptionletVolatilitySurface object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletVolatilitySurfaceBaseLevel(
    vol_tsh: ql.YoYOptionletVolatilitySurfaceHandle, trigger=None
) -> float:
    return vol_tsh.baseLevel()


@xlo.func(
    help="Returns the volatility for a given YoY optionlet volatility surface, maturity date, and strike.",
    args={
        "vol_tsh": "Handle to a YoYOptionletVolatilitySurface object.",
        "maturity_date": "Maturity date for which to calculate the volatility.",
        "strike": "Strike price for which to calculate the volatility.",
        "observation_lag": "Observation lag for the YoY optionlet volatility surface.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletVolatilitySurfaceVolatility(
    vol_tsh: ql.YoYOptionletVolatilitySurfaceHandle,
    maturity_date: qDate,
    strike: float,
    observation_lag: qPeriod = ql.Period(-1, ql.Days),
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.volatility(maturity_date, strike, observation_lag, extrapolate)


@xlo.func(
    help="Returns the volatility for a given YoY optionlet volatility surface, maturity time, and strike.",
    args={
        "vol_tsh": "Handle to a YoYOptionletVolatilitySurface object.",
        "maturity_time": "Maturity time for which to calculate the volatility.",
        "strike": "Strike price for which to calculate the volatility.",
        "observation_lag": "Observation lag for the YoY optionlet volatility surface.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletVolatilitySurfaceVolatilityFromTime(
    vol_tsh: ql.YoYOptionletVolatilitySurfaceHandle,
    maturity_time: float,
    strike: float,
    observation_lag: qPeriod = ql.Period(-1, ql.Days),
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.volatility(maturity_time, strike, observation_lag, extrapolate)


@xlo.func(
    help="Returns the total variance for a given YoY optionlet volatility surface, exercise date, and strike.",
    args={
        "vol_tsh": "Handle to a YoYOptionletVolatilitySurface object.",
        "exercise_date": "Exercise date for which to calculate the total variance.",
        "strike": "Strike price for which to calculate the total variance.",
        "observation_lag": "Observation lag for the YoY optionlet volatility surface.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletVolatilitySurfaceTotalVariance(
    vol_tsh: ql.YoYOptionletVolatilitySurfaceHandle,
    exercise_date: qDate,
    strike: float,
    observation_lag: qPeriod = ql.Period(-1, ql.Days),
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.totalVariance(exercise_date, strike, observation_lag, extrapolate)


@xlo.func(
    help="Returns the total variance for a given YoY optionlet volatility surface, exercise time, and strike.",
    args={
        "vol_tsh": "Handle to a YoYOptionletVolatilitySurface object.",
        "exercise_time": "Exercise time for which to calculate the total variance.",
        "strike": "Strike price for which to calculate the total variance.",
        "observation_lag": "Observation lag for the YoY optionlet volatility surface.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletVolatilitySurfaceTotalVarianceFromTime(
    vol_tsh: ql.YoYOptionletVolatilitySurfaceHandle,
    exercise_time: float,
    strike: float,
    observation_lag: qPeriod = ql.Period(-1, ql.Days),
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.totalVariance(exercise_time, strike, observation_lag, extrapolate)


# SwaptionVolatilityStructure interface


@xlo.func(
    help="Returns the volatility for a given swaption volatility structure, option date, swap tenor, and strike.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_date": "Option expiry date.",
        "swap_tenor": "Swap tenor for which to calculate the volatility.",
        "strike": "Strike price for which to calculate the volatility.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureVolatility(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_date: qDate,
    swap_tenor: qPeriod,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.volatility(option_date, swap_tenor, strike, extrapolate)


@xlo.func(
    help="Returns the volatility for a given swaption volatility structure, option time, swap length, and strike.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_time": "Option expiry time.",
        "swap_length": "Swap length for which to calculate the volatility.",
        "strike": "Strike price for which to calculate the volatility.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureVolatilityFromTime(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_time: float,
    swap_length: float,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.volatility(option_time, swap_length, strike, extrapolate)


@xlo.func(
    help="Returns the Black variance for a given swaption volatility structure, option date, swap tenor, and strike.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_date": "Option expiry date.",
        "swap_tenor": "Swap tenor for which to calculate the variance.",
        "strike": "Strike price for which to calculate the variance.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureBlackVariance(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_date: qDate,
    swap_tenor: qPeriod,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.blackVariance(option_date, swap_tenor, strike, extrapolate)


@xlo.func(
    help="Returns the Black variance for a given swaption volatility structure, option time, swap length, and strike.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_time": "Option expiry time.",
        "swap_length": "Swap length for which to calculate the variance.",
        "strike": "Strike price for which to calculate the variance.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureBlackVarianceFromTime(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_time: float,
    swap_length: float,
    strike: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.blackVariance(option_time, swap_length, strike, extrapolate)


@xlo.func(
    help="Returns the option date for a given swaption volatility structure and option tenor.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_tenor": "Option tenor for which to calculate the option date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureOptionDateFromTenor(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_tenor: qPeriod,
    trigger=None,
) -> ql.Date:
    return vol_tsh.optionDateFromTenor(option_tenor)


@xlo.func(
    help="Returns the volatility shift for a given swaption volatility structure, option tenor, and swap tenor.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_tenor": "Option tenor for which to calculate the shift.",
        "swap_tenor": "Swap tenor for which to calculate the shift.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureShiftFromTenor(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_tenor: qPeriod,
    swap_tenor: qPeriod,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.shift(
        vol_tsh.optionDateFromTenor(option_tenor), swap_tenor, extrapolate
    )


@xlo.func(
    help="Returns the volatility shift for a given swaption volatility structure.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_date": "Option expiry date.",
        "swap_tenor": "Swap tenor for which to calculate the shift.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureShift(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_date: qDate,
    swap_tenor: qPeriod,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.shift(option_date, swap_tenor, extrapolate)


@xlo.func(
    help="Returns the volatility shift for a given swaption volatility structure, option time, and swap tenor.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_time": "Option expiry time.",
        "swap_tenor": "Swap tenor for which to calculate the shift.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureShiftFromTime(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_time: float,
    swap_tenor: qPeriod,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.shift(option_time, swap_tenor, extrapolate)


@xlo.func(
    help="Returns the volatility shift for a given swaption volatility structure, option tenor, and swap length.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_tenor": "Option tenor for which to calculate the shift.",
        "swap_length": "Swap length for which to calculate the shift.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureShiftFromTenor2(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_tenor: qPeriod,
    swap_length: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.shift(
        vol_tsh.optionDateFromTenor(option_tenor), swap_length, extrapolate
    )


@xlo.func(
    help="Returns the volatility shift for a given swaption volatility structure.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_date": "Option expiry date.",
        "swap_length": "Swap length for which to calculate the shift.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureShift2(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_date: qDate,
    swap_length: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.shift(option_date, swap_length, extrapolate)


@xlo.func(
    help="Returns the volatility shift for a given swaption volatility structure, option time, and swap length.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_time": "Option expiry time.",
        "swap_length": "Swap length for which to calculate the shift.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureShiftFromTime2(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_time: float,
    swap_length: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return vol_tsh.shift(option_time, swap_length, extrapolate)


@xlo.func(
    help="Returns the smile section for a given swaption volatility structure, option tenor, and swap tenor.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_tenor": "Option tenor for which to calculate the smile section.",
        "swap_tenor": "Swap tenor for which to calculate the smile section.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureSmileSectionFromTenor(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_tenor: qPeriod,
    swap_tenor: qPeriod,
    extrapolate: bool = False,
    trigger=None,
) -> ql.SmileSection:
    option_date = vol_tsh.optionDateFromTenor(option_tenor)
    return vol_tsh.smileSection(option_date, swap_tenor, extrapolate)


@xlo.func(
    help="Returns the smile section for a given swaption volatility structure.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_date": "Option expiry date.",
        "swap_tenor": "Swap tenor for which to calculate the smile section.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureSmileSection(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_date: qDate,
    swap_tenor: qPeriod,
    extrapolate: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return vol_tsh.smileSection(option_date, swap_tenor, extrapolate)


@xlo.func(
    help="Returns the smile section for a given swaption volatility structure, option time, and swap tenor.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_time": "Option expiry time.",
        "swap_tenor": "Swap tenor for which to calculate the smile section.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureSmileSectionFromTime(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_time: float,
    swap_tenor: qPeriod,
    extrapolate: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return vol_tsh.smileSection(option_time, swap_tenor, extrapolate)


@xlo.func(
    help="Returns the smile section for a given swaption volatility structure, option tenor, and swap length.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_tenor": "Option tenor for which to calculate the smile section.",
        "swap_length": "Swap length for which to calculate the smile section.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureSmileSectionFromTenor2(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_tenor: qPeriod,
    swap_length: float,
    extrapolate: bool = False,
    trigger=None,
) -> ql.SmileSection:
    option_date = vol_tsh.optionDateFromTenor(option_tenor)
    return vol_tsh.smileSection(option_date, swap_length, extrapolate)


@xlo.func(
    help="Returns the smile section for a given swaption volatility structure.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_date": "Option expiry date.",
        "swap_length": "Swap length for which to calculate the smile section.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureSmileSection2(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_date: qDate,
    swap_length: float,
    extrapolate: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return vol_tsh.smileSection(option_date, swap_length, extrapolate)


@xlo.func(
    help="Returns the smile section for a given swaption volatility structure, option time, and swap length.",
    args={
        "vol_tsh": "Handle to a SwaptionVolatilityStructure object.",
        "option_time": "Option expiry time.",
        "swap_length": "Swap length for which to calculate the smile section.",
        "extrapolate": "Whether to extrapolate if the strike is outside the defined range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureSmileSectionFromTime2(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_time: float,
    swap_length: float,
    extrapolate: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return vol_tsh.smileSection(option_time, swap_length, extrapolate)


###
# ToDo Sabr
###

# BlackConstantVol creator


@xlo.func(
    help="Creates a BlackConstantVol object and returns a handle to it.",
    args={
        "reference_date": "Reference date for the volatility.",
        "calendar": "Calendar for the volatility.",
        "volatility": "Constant volatility value.",
        "day_counter": "Day count convention for the volatility.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackConstantVol(
    reference_date: qDate,
    calendar: qCalendar,
    volatility: float,
    day_counter: qDayCounter,
    trigger=None,
) -> ql.BlackVolTermStructureHandle:
    volts = ql.BlackConstantVol(reference_date, calendar, volatility, day_counter)
    return ql.BlackVolTermStructureHandle(volts)


@xlo.func(
    help="Creates a BlackConstantVol object and returns a handle to it.",
    args={
        "settlement_days": "Settlement days for the volatility.",
        "calendar": "Calendar for the volatility.",
        "volatility": "Constant volatility value.",
        "day_counter": "Day count convention for the volatility.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackConstantVol2(
    settlement_days: float,
    calendar: qCalendar,
    volatility: float,
    day_counter: qDayCounter,
    trigger=None,
) -> ql.BlackVolTermStructureHandle:
    volts = ql.BlackConstantVol(settlement_days, calendar, volatility, day_counter)
    return ql.BlackVolTermStructureHandle(volts)


# BlackVarianceCurve creator


@xlo.func(
    help="Create a QuantLib BlackVarianceCurve object from dates, volatilities, and day counter.",
    args={
        "reference_date": "Reference date for the variance curve.",
        "dates": "Vector of dates for the variance curve.",
        "volatilities": "Vector of volatilities corresponding to the dates.",
        "day_counter": "Day count convention for the variance curve.",
        "force_monotone_variance": "Whether to force monotone variance (default: True).",
        "time_extrapolation_type": "The time extrapolation type for the curve (default: FlatVolatility).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVarianceCurve(
    reference_date: qDate,
    dates: xlo.Array(dims=1),
    volatilities: xlo.Array(dims=1),
    day_counter: qDayCounter,
    force_monotone_variance: bool = True,
    time_extrapolation_type: qBlackVolTimeExtrapolation = ql.BlackVolTimeExtrapolation.FlatVolatility,
    trigger=None,
) -> ql.BlackVarianceCurve:
    return ql.BlackVarianceCurve(
        reference_date,
        _to_date_list(dates),
        to_float_list(volatilities),
        day_counter,
        force_monotone_variance,
        time_extrapolation_type,
    )


###
# TODO Black Variance Surface
# TODO PiecewiseBlackVarianceSurface
# TODO BlackVolatilitySurfaceDelta
###

# ConstantOptionletVolatility creator


@xlo.func(
    help="Creates a ConstantOptionletVolatility object and returns a handle to it.",
    args={
        "reference_date": "Reference date for the volatility.",
        "calendar": "Calendar for the volatility.",
        "business_day_convention": "Business day convention for the volatility.",
        "volatility": "Constant volatility value.",
        "day_counter": "Day count convention for the volatility.",
        "volatility_type": "Volatility type (e.g. 'NORMAL', 'SHIFTEDLOGNORMAL').",
        "shift": "Shift value for shifted lognormal volatility.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlConstantOptionletVolatility(
    reference_date: qDate,
    calendar: qCalendar,
    business_day_convention: qBusinessDayConvention,
    volatility: qQuoteHandle,
    day_counter: qDayCounter,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    trigger=None,
) -> ql.OptionletVolatilityStructureHandle:
    vol_ts = ql.ConstantOptionletVolatility(
        reference_date,
        calendar,
        business_day_convention,
        volatility,
        day_counter,
        volatility_type,
        shift,
    )
    return ql.OptionletVolatilityStructureHandle(vol_ts)


xlo.func(
    help="Creates a ConstantOptionletVolatility object and returns a handle to it.",
    args={
        "settlement_days": "Settlement days for the volatility.",
        "calendar": "Calendar for the volatility.",
        "business_day_convention": "Business day convention for the volatility.",
        "volatility": "Constant volatility value.",
        "day_counter": "Day count convention for the volatility.",
        "volatility_type": "Volatility type (e.g. 'NORMAL', 'SHIFTEDLOGNORMAL').",
        "shift": "Shift value for shifted lognormal volatility.",
    },
    group=EXCEL_GROUP_NAME,
)


def qlConstantOptionletVolatility2(
    settlement_days: float,
    calendar: qCalendar,
    business_day_convention: qBusinessDayConvention,
    volatility: qQuoteHandle,
    day_counter: qDayCounter,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    trigger=None,
) -> ql.OptionletVolatilityStructureHandle:
    vol_ts = ql.ConstantOptionletVolatility(
        settlement_days,
        calendar,
        business_day_convention,
        volatility,
        day_counter,
        volatility_type,
        shift,
    )
    return ql.OptionletVolatilityStructureHandle(vol_ts)


# ConstantSwaptionVolatility creator


@xlo.func(
    help="Creates a ConstantSwaptionVolatility object and returns a handle to it.",
    args={
        "reference_date": "Reference date for the volatility.",
        "calendar": "Calendar for the volatility.",
        "business_day_convention": "Business day convention for the volatility.",
        "volatility": "Constant volatility value.",
        "day_counter": "Day count convention for the volatility.",
        "volatility_type": "Volatility type (e.g. 'Normal' or 'ShiftedLognormal').",
        "shift": "Volatility shift (only used if volatility_type is 'ShiftedLognormal').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlConstantSwaptionVolatility(
    reference_date: qDate,
    calendar: qCalendar,
    business_day_convention: qBusinessDayConvention,
    volatility: qQuoteHandle,
    day_counter: qDayCounter,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    trigger=None,
) -> ql.SwaptionVolatilityStructureHandle:
    vol_ts = ql.ConstantSwaptionVolatility(
        reference_date,
        calendar,
        business_day_convention,
        volatility,
        day_counter,
        volatility_type,
        shift,
    )
    return ql.SwaptionVolatilityStructureHandle(vol_ts)


@xlo.func(
    help="Creates a ConstantSwaptionVolatility object and returns a handle to it.",
    args={
        "settlement_days": "Settlement days for the volatility.",
        "calendar": "Calendar for the volatility.",
        "business_day_convention": "Business day convention for the volatility.",
        "volatility": "Constant volatility value.",
        "day_counter": "Day count convention for the volatility.",
        "volatility_type": "Volatility type (e.g. 'Normal' or 'ShiftedLognormal').",
        "shift": "Volatility shift (only used if volatility_type is 'ShiftedLognormal').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlConstantSwaptionVolatility2(
    settlement_days: float,
    calendar: qCalendar,
    business_day_convention: qBusinessDayConvention,
    volatility: qQuoteHandle,
    day_counter: qDayCounter,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    trigger=None,
) -> ql.SwaptionVolatilityStructureHandle:
    vol_ts = ql.ConstantSwaptionVolatility(
        settlement_days,
        calendar,
        business_day_convention,
        volatility,
        day_counter,
        volatility_type,
        shift,
    )
    return ql.SwaptionVolatilityStructureHandle(vol_ts)


###
# TODO SwaptionVolatilityDiscrete
###

# SwaptionVolatilityMatrix creator


@xlo.func(
    help="Creates a SwaptionVolatilityMatrix object and returns a handle to it.",
    args={
        "reference_date": "Reference date for the volatility matrix.",
        "expiry_dates": "Array of option expiry dates.",
        "lengths": "Array of swap lengths corresponding to the expiry dates.",
        "vols": "2D array of volatilities corresponding to the expiry dates and lengths.",
        "day_counter": "Day count convention for the volatility matrix.",
        "flat_extrapolation": "Whether to use flat extrapolation for the volatility matrix.",
        "volatility_type": "Volatility type (e.g. 'Normal' or 'ShiftedLognormal').",
        "shifts": "2D array of shifts corresponding to the expiry dates and lengths (only used if volatility_type is 'ShiftedLognormal').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityMatrix(
    reference_date: qDate,
    expiry_dates: xlo.Array(dims=1),
    lengths: xlo.Array(dims=1),
    vols: xlo.Array(dims=2),
    day_counter: qDayCounter,
    flat_extrapolation: bool = False,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shifts: xlo.Array(dims=2) = None,
    trigger=None,
) -> ql.SwaptionVolatilityStructureHandle:
    dates_list = _to_date_list(expiry_dates)
    length_list = [qPeriod.__wrapped__(length) for length in lengths]
    vol_matrix = ql.Matrix(to_float_matrix(vols))
    shift_matrix = ql.Matrix(to_float_matrix(shifts))
    vol_ts = ql.SwaptionVolatilityMatrix(
        reference_date,
        dates_list,
        length_list,
        vol_matrix,
        day_counter,
        flat_extrapolation,
        volatility_type,
        shift_matrix,
    )
    return ql.SwaptionVolatilityStructureHandle(vol_ts)


@xlo.func(
    help="Create a QuantLib SwaptionVolatilityMatrix from option and swap tenors.",
    args={
        "reference_date": "The reference date for the matrix.",
        "calendar": "The calendar used for the matrix.",
        "business_day_convention": "The business-day convention.",
        "option_tenors": "The option expiry tenors.",
        "swap_tenors": "The underlying swap tenors.",
        "vols": "The volatility matrix.",
        "day_counter": "The day counter.",
        "flat_extrapolation": "Whether to use flat extrapolation.",
        "volatility_type": "The volatility type.",
        "shifts": "The displacement matrix, if applicable.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityMatrixForTenors(
    reference_date: qDate,
    calendar: qCalendar,
    business_day_convention: qBusinessDayConvention,
    option_tenors: xlo.Array(dims=1),
    swap_tenors: xlo.Array(dims=1),
    vols: xlo.Array(dims=2),
    day_counter: qDayCounter,
    flat_extrapolation: bool = False,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shifts: xlo.Array(dims=2) = None,
    trigger=None,
) -> ql.SwaptionVolatilityStructureHandle:
    vol_ts = ql.SwaptionVolatilityMatrix.forTenors(
        reference_date,
        calendar,
        business_day_convention,
        [qPeriod.__wrapped__(tenor) for tenor in option_tenors],
        [qPeriod.__wrapped__(tenor) for tenor in swap_tenors],
        ql.Matrix(to_float_matrix(vols)),
        day_counter,
        flat_extrapolation,
        volatility_type,
        ql.Matrix(to_float_matrix(shifts)),
    )
    return ql.SwaptionVolatilityStructureHandle(vol_ts)


# TODO to test
@xlo.func(
    help="Creates a SwaptionVolatilityMatrix from dates and lengths.",
    args={
        "reference_date": "Reference date for the volatility matrix.",
        "calendar": "Calendar for the volatility matrix.",
        "business_day_convention": "Business day convention.",
        "expiry_dates": "Array of option expiry dates.",
        "lengths": "Array of swap lengths corresponding to the expiry dates.",
        "vols": "2D array of volatilities.",
        "day_counter": "Day count convention.",
        "flat_extrapolation": "Whether to use flat extrapolation.",
        "volatility_type": "Volatility type (Normal or ShiftedLognormal).",
        "shifts": "2D array of shifts (optional).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityMatrix2(
    reference_date: qDate,
    calendar: qCalendar,
    business_day_convention: qBusinessDayConvention,
    expiry_dates: xlo.Array(dims=1),
    lengths: xlo.Array(dims=1),
    vols: xlo.Array(dims=2),
    day_counter: qDayCounter,
    flat_extrapolation: bool = False,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shifts: xlo.Array(dims=2) = None,
    trigger=None,
) -> ql.SwaptionVolatilityStructureHandle:
    dates_list = _to_date_list(expiry_dates)
    length_list = [qPeriod.__wrapped__(length) for length in lengths]
    vol_matrix = ql.Matrix(to_float_matrix(vols))
    shift_matrix = (
        ql.Matrix(to_float_matrix(shifts)) if shifts is not None else ql.Matrix()
    )
    vol_ts = ql.SwaptionVolatilityMatrix(
        reference_date,
        calendar,
        business_day_convention,
        dates_list,
        length_list,
        vol_matrix,
        day_counter,
        flat_extrapolation,
        volatility_type,
        shift_matrix,
    )
    return ql.SwaptionVolatilityStructureHandle(vol_ts)


# TODO to test
@xlo.func(
    help="Creates a SwaptionVolatilityMatrix from option and swap tenors with Quote handles.",
    args={
        "calendar": "Calendar for the volatility matrix.",
        "business_day_convention": "Business day convention.",
        "option_tenors": "Array of option tenors (Periods).",
        "swap_tenors": "Array of swap tenors (Periods).",
        "vols": "2D array of Quote handles for volatilities.",
        "day_counter": "Day count convention.",
        "flat_extrapolation": "Whether to use flat extrapolation.",
        "volatility_type": "Volatility type (Normal or ShiftedLognormal).",
        "shifts": "2D array of shifts as Real values (optional).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityMatrix3(
    calendar: qCalendar,
    business_day_convention: qBusinessDayConvention,
    option_tenors: xlo.Array(dims=1),
    swap_tenors: xlo.Array(dims=1),
    vols: xlo.Array(dims=2),
    day_counter: qDayCounter,
    flat_extrapolation: bool = False,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shifts: xlo.Array(dims=2) = None,
    trigger=None,
) -> ql.SwaptionVolatilityStructureHandle:
    option_tenors_list = [qPeriod.__wrapped__(t) for t in option_tenors]
    swap_tenors_list = [qPeriod.__wrapped__(t) for t in swap_tenors]
    vol_matrix = ql.Matrix(len(option_tenors_list), len(swap_tenors_list))
    shift_matrix = ql.Matrix(len(option_tenors_list), len(swap_tenors_list))

    vol_handles = []
    for i, row in enumerate(vols):
        vol_row = []
        for j, vol in enumerate(row):
            vol_row.append(qQuoteHandle(vol))
        vol_handles.append(vol_row)
    shift_values = []
    if shifts is not None:
        for i, row in enumerate(shifts):
            shift_row = []
            for j, shift_val in enumerate(row):
                shift_row.append(float(shift_val))
            shift_values.append(shift_row)

    vol_ts = ql.SwaptionVolatilityMatrix(
        calendar,
        business_day_convention,
        option_tenors_list,
        swap_tenors_list,
        vol_handles,
        day_counter,
        flat_extrapolation,
        volatility_type,
        shift_values,
    )
    return ql.SwaptionVolatilityStructureHandle(vol_ts)


# TODO to test
@xlo.func(
    help="Creates a SwaptionVolatilityMatrix from option and swap tenors with Matrix.",
    args={
        "calendar": "Calendar for the volatility matrix.",
        "business_day_convention": "Business day convention.",
        "option_tenors": "Array of option tenors (Periods).",
        "swap_tenors": "Array of swap tenors (Periods).",
        "vols": "2D array of volatilities as numeric values.",
        "day_counter": "Day count convention.",
        "flat_extrapolation": "Whether to use flat extrapolation.",
        "volatility_type": "Volatility type (Normal or ShiftedLognormal).",
        "shifts": "2D array of shifts (optional).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityMatrix4(
    calendar: qCalendar,
    business_day_convention: qBusinessDayConvention,
    option_tenors: xlo.Array(dims=1),
    swap_tenors: xlo.Array(dims=1),
    vols: xlo.Array(dims=2),
    day_counter: qDayCounter,
    flat_extrapolation: bool = False,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shifts: xlo.Array(dims=2) = None,
    trigger=None,
) -> ql.SwaptionVolatilityStructureHandle:
    option_tenors_list = [qPeriod.__wrapped__(t) for t in option_tenors]
    swap_tenors_list = [qPeriod.__wrapped__(t) for t in swap_tenors]
    vol_matrix = ql.Matrix(to_float_matrix(vols))
    shift_matrix = (
        ql.Matrix(to_float_matrix(shifts)) if shifts is not None else ql.Matrix()
    )

    vol_ts = ql.SwaptionVolatilityMatrix(
        calendar,
        business_day_convention,
        option_tenors_list,
        swap_tenors_list,
        vol_matrix,
        day_counter,
        flat_extrapolation,
        volatility_type,
        shift_matrix,
    )
    return ql.SwaptionVolatilityStructureHandle(vol_ts)


@xlo.func(
    help="Return the business day convention of a volatility term structure.",
    args={"volatility": "The volatility term structure."},
    group=EXCEL_GROUP_NAME,
)
def qlVolatilityTermStructureBusinessDayConvention(
    volatility: ql.VolatilityTermStructure, trigger=None
) -> str:
    return first_key(QL_BUSINESSDAYCONVENTION, volatility.businessDayConvention())


@xlo.func(
    help="Return the volatility type of an optionlet volatility structure.",
    args={"volatility": "The optionlet volatility structure."},
    group=EXCEL_GROUP_NAME,
)
def qlOptionletVolatilityStructureVolatilityType(
    volatility: ql.OptionletVolatilityStructure, trigger=None
) -> str:
    return first_key(QL_VOLATILITY_TYPE, volatility.volatilityType())


@xlo.func(
    help="Return the displacement of an optionlet volatility structure.",
    args={"volatility": "The optionlet volatility structure."},
    group=EXCEL_GROUP_NAME,
)
def qlOptionletVolatilityStructureDisplacement(
    volatility: ql.OptionletVolatilityStructure, trigger=None
) -> float:
    return volatility.displacement()


@xlo.func(
    help="Return the volatility type of a swaption volatility structure.",
    args={"volatility": "The swaption volatility structure."},
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityStructureVolatilityType(
    volatility: ql.SwaptionVolatilityStructure, trigger=None
) -> str:
    return first_key(QL_VOLATILITY_TYPE, volatility.volatilityType())


@xlo.func(
    help="Return the at-the-money strike of a swaption volatility cube.",
    args={
        "cube": "The swaption volatility cube.",
        "option_date": "The option expiry date.",
        "swap_tenor": "The underlying swap tenor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityCubeAtmStrike(
    cube: ql.SwaptionVolatilityCube,
    option_date: qDate,
    swap_tenor: qPeriod,
    trigger=None,
) -> float:
    return cube.atmStrike(option_date, swap_tenor)


@xlo.func(
    help="Return the at-the-money volatility structure of a swaption volatility cube.",
    args={"cube": "The swaption volatility cube."},
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityCubeAtmVol(
    cube: ql.SwaptionVolatilityCube, trigger=None
) -> ql.SwaptionVolatilityStructureHandle:
    return cube.atmVol()


@xlo.func(
    help="Return the strike spreads of a swaption volatility cube.",
    args={"cube": "The swaption volatility cube."},
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityCubeStrikeSpreads(
    cube: ql.SwaptionVolatilityCube, trigger=None
) -> list[float]:
    return cube.strikeSpreads()


@xlo.func(
    help="Return the volatility-spread quote matrix of a swaption volatility cube.",
    args={"cube": "The swaption volatility cube."},
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityCubeVolSpreads(
    cube: ql.SwaptionVolatilityCube, trigger=None
) -> list[list[ql.QuoteHandle]]:
    return ql.SwaptionVolatilityCube.volSpreads(cube)


@xlo.func(
    help="Return the base swap index of a swaption volatility cube.",
    args={"cube": "The swaption volatility cube."},
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityCubeSwapIndexBase(
    cube: ql.SwaptionVolatilityCube, trigger=None
) -> ql.SwapIndex:
    return cube.swapIndexBase()


@xlo.func(
    help="Return the short swap index of a swaption volatility cube.",
    args={"cube": "The swaption volatility cube."},
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityCubeShortSwapIndexBase(
    cube: ql.SwaptionVolatilityCube, trigger=None
) -> ql.SwapIndex:
    return cube.shortSwapIndexBase()


@xlo.func(
    help="Return whether the swaption volatility cube uses vega-weighted smile fitting.",
    args={"cube": "The swaption volatility cube."},
    group=EXCEL_GROUP_NAME,
)
def qlSwaptionVolatilityCubeVegaWeightedSmileFit(
    cube: ql.SwaptionVolatilityCube, trigger=None
) -> bool:
    return cube.vegaWeightedSmileFit()


@xlo.func(
    help="Create a QuantLib InterpolatedSwaptionVolatilityCube.",
    args={
        "atm_vol_structure": "The at-the-money swaption volatility structure.",
        "option_tenors": "Option expiry tenors.",
        "swap_tenors": "Underlying swap tenors.",
        "strike_spreads": "Strike spreads.",
        "vol_spreads": "Volatility spreads by option tenor and strike.",
        "swap_index": "The base swap index.",
        "short_swap_index": "The short swap index.",
        "vega_weighted_smile_fit": "Whether to use vega-weighted smile fitting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterpolatedSwaptionVolatilityCube(
    atm_vol_structure: ql.SwaptionVolatilityStructureHandle,
    option_tenors: xlo.Array(dims=1),
    swap_tenors: xlo.Array(dims=1),
    strike_spreads: xlo.Array(dims=1),
    vol_spreads: xlo.Array(dims=2),
    swap_index: ql.SwapIndex,
    short_swap_index: ql.SwapIndex,
    vega_weighted_smile_fit: bool = False,
    trigger=None,
) -> ql.InterpolatedSwaptionVolatilityCube:
    return ql.InterpolatedSwaptionVolatilityCube(
        atm_vol_structure,
        [qPeriod.__wrapped__(tenor) for tenor in option_tenors],
        [qPeriod.__wrapped__(tenor) for tenor in swap_tenors],
        to_float_list(strike_spreads),
        _to_quote_handle_matrix(vol_spreads),
        swap_index,
        short_swap_index,
        vega_weighted_smile_fit,
    )


@xlo.func(
    help=(
        "Return the volatility-spread matrix for a tenor in an interpolated "
        "swaption volatility cube."
    ),
    args={
        "cube": "The interpolated swaption volatility cube.",
        "i": "The option tenor index.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterpolatedSwaptionVolatilityCubeVolSpreads(
    cube: ql.InterpolatedSwaptionVolatilityCube, i: int, trigger=None
) -> ql.Matrix:
    return cube.volSpreads(i)


@xlo.func(
    help="Create a QuantLib SabrSwaptionVolatilityCube.",
    args={
        "atm_vol_structure": "The at-the-money swaption volatility structure.",
        "option_tenors": "Option expiry tenors.",
        "swap_tenors": "Underlying swap tenors.",
        "strike_spreads": "Strike spreads.",
        "vol_spreads": "Volatility spreads by option tenor and strike.",
        "swap_index": "The base swap index.",
        "short_swap_index": "The short swap index.",
        "vega_weighted_smile_fit": "Whether to use vega-weighted smile fitting.",
        "parameters_guess": "Initial SABR parameter guesses.",
        "is_parameter_fixed": "Flags indicating fixed SABR parameters.",
        "is_atm_calibrated": "Whether to calibrate the cube to ATM volatilities.",
        "end_criteria": "Calibration stopping criteria.",
        "max_error_tolerance": "Maximum calibration error tolerance.",
        "opt_method": "The optimization method.",
        "error_accept": "Accepted calibration error.",
        "use_max_error": "Whether to use maximum error in calibration.",
        "max_guesses": "Maximum parameter guesses.",
        "backward_flat": "Whether to use backward-flat interpolation.",
        "cutoff_strike": "Minimum absolute strike for calibration.",
        "single_pass_calibration": "Whether to calibrate in a single pass.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSabrSwaptionVolatilityCube(
    atm_vol_structure: ql.SwaptionVolatilityStructureHandle,
    option_tenors: xlo.Array(dims=1),
    swap_tenors: xlo.Array(dims=1),
    strike_spreads: xlo.Array(dims=1),
    vol_spreads: xlo.Array(dims=2),
    swap_index: ql.SwapIndex,
    short_swap_index: ql.SwapIndex,
    vega_weighted_smile_fit: bool,
    parameters_guess: xlo.Array(dims=2) = None,
    is_parameter_fixed: xlo.Array(dims=1) = None,
    is_atm_calibrated: bool = False,
    end_criteria: ql.EndCriteria = None,
    max_error_tolerance: float = ql.nullDouble(),
    opt_method: ql.OptimizationMethod = None,
    error_accept: float = ql.nullDouble(),
    use_max_error: bool = False,
    max_guesses: int = 50,
    backward_flat: bool = False,
    cutoff_strike: float = 0.0001,
    single_pass_calibration: bool = False,
    trigger=None,
) -> ql.SabrSwaptionVolatilityCube:
    return ql.SabrSwaptionVolatilityCube(
        atm_vol_structure,
        [qPeriod.__wrapped__(tenor) for tenor in option_tenors],
        [qPeriod.__wrapped__(tenor) for tenor in swap_tenors],
        to_float_list(strike_spreads),
        _to_quote_handle_matrix(vol_spreads),
        swap_index,
        short_swap_index,
        vega_weighted_smile_fit,
        _to_quote_handle_matrix(parameters_guess),
        to_bool_list(is_parameter_fixed),
        is_atm_calibrated,
        end_criteria,
        max_error_tolerance,
        opt_method,
        error_accept,
        use_max_error,
        max_guesses,
        backward_flat,
        cutoff_strike,
        single_pass_calibration,
    )


@xlo.func(
    help="Return the sparse SABR parameter matrix of a swaption volatility cube.",
    args={"cube": "The SABR swaption volatility cube."},
    group=EXCEL_GROUP_NAME,
)
def qlSabrSwaptionVolatilityCubeSparseSabrParameters(
    cube: ql.SabrSwaptionVolatilityCube, trigger=None
) -> ql.Matrix:
    return cube.sparseSabrParameters()


@xlo.func(
    help="Return the dense SABR parameter matrix of a swaption volatility cube.",
    args={"cube": "The SABR swaption volatility cube."},
    group=EXCEL_GROUP_NAME,
)
def qlSabrSwaptionVolatilityCubeDenseSabrParameters(
    cube: ql.SabrSwaptionVolatilityCube, trigger=None
) -> ql.Matrix:
    return cube.denseSabrParameters()


@xlo.func(
    help="Return the market volatility matrix of a SABR swaption volatility cube.",
    args={"cube": "The SABR swaption volatility cube."},
    group=EXCEL_GROUP_NAME,
)
def qlSabrSwaptionVolatilityCubeMarketVolCube(
    cube: ql.SabrSwaptionVolatilityCube, trigger=None
) -> ql.Matrix:
    return cube.marketVolCube()


@xlo.func(
    help="Return the ATM-calibrated volatility matrix of a SABR swaption volatility cube.",
    args={"cube": "The SABR swaption volatility cube."},
    group=EXCEL_GROUP_NAME,
)
def qlSabrSwaptionVolatilityCubeVolCubeAtmCalibrated(
    cube: ql.SabrSwaptionVolatilityCube, trigger=None
) -> ql.Matrix:
    return cube.volCubeAtmCalibrated()


@xlo.func(
    help="Return a SABR smile section from a SABR swaption volatility cube.",
    args={
        "cube": "The SABR swaption volatility cube.",
        "option_tenor": "Option expiry tenor.",
        "swap_tenor": "Underlying swap tenor.",
        "extrapolate": "Whether to extrapolate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSabrSwaptionVolatilityCubeSmileSection(
    cube: ql.SabrSwaptionVolatilityCube,
    option_tenor: qPeriod,
    swap_tenor: qPeriod,
    extrapolate: bool = False,
    trigger=None,
) -> ql.SabrSmileSection:
    return cube.smileSection(option_tenor, swap_tenor, extrapolate)


# Smile Section Creator functions


@xlo.func(
    help="Create a flat smile section.",
    args={
        "date": "The date for the smile section.",
        "volatility": "The volatility value.",
        "day_counter": "The day counter for the smile.",
        "reference_date": "The reference date for the smile.",
        "atm_level": "The at-the-money level.",
        "volatility_type": "The volatility type.",
        "shift": "The displacement for shifted-lognormal volatility.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFlatSmileSection(
    date: qDate,
    volatility: float,
    day_counter: qDayCounter,
    reference_date: qDate = ql.Date(),
    atm_level: float = ql.nullDouble(),
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
) -> ql.SmileSection:
    return ql.FlatSmileSection(
        date, volatility, day_counter, reference_date, atm_level, volatility_type, shift
    )


@xlo.func(
    help="Create a flat smile section.",
    args={
        "expiry_time": "The time to expiry.",
        "volatility": "The volatility value.",
        "day_counter": "The day counter for the smile.",
        "atm_level": "The at-the-money level.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFlatSmileSection2(
    expiry_time: float,
    volatility: float,
    day_counter: qDayCounter,
    atm_level: float = ql.nullDouble(),
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    trigger=None,
) -> ql.SmileSection:
    return ql.FlatSmileSection(
        expiry_time, volatility, day_counter, atm_level, volatility_type, shift
    )


@xlo.func(
    help="Create a linear interpolated smile section.",
    args={
        "expiry_time": "The time to expiry.",
        "strikes": "The smile strikes.",
        "standard_deviations": "The Black standard deviations at each strike.",
        "atm_level": "The at-the-money level.",
        "day_counter": "The day counter for the smile.",
        "volatility_type": "The volatility type.",
        "shift": "The displacement for shifted-lognormal volatility.",
        "flat_strike_extrapolation": "Whether to extrapolate flat in strike.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLinearInterpolatedSmileSection(
    expiry_time: float,
    strikes: xlo.Array(dims=1),
    standard_deviations: xlo.Array(dims=1),
    atm_level: float,
    day_counter: qDayCounter = ql.Actual365Fixed(),
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    flat_strike_extrapolation: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return ql.LinearInterpolatedSmileSection(
        expiry_time,
        to_float_list(strikes),
        to_float_list(standard_deviations),
        atm_level,
        ql.Linear(),
        day_counter,
        volatility_type,
        shift,
        flat_strike_extrapolation,
    )


@xlo.func(
    help="Create a linear interpolated smile section.",
    args={
        "date": "The date for the smile section.",
        "strikes": "The smile strikes.",
        "standard_deviations": "The Black standard deviations at each strike.",
        "atm_level": "The at-the-money level.",
        "day_counter": "The day counter for the smile.",
        "reference_date": "The reference date for the smile section.",
        "volatility_type": "The volatility type.",
        "shift": "The displacement for shifted-lognormal volatility.",
        "flat_strike_extrapolation": "Whether to extrapolate flat in strike.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLinearInterpolatedSmileSection2(
    date: qDate,
    strikes: xlo.Array(dims=1),
    standard_deviations: xlo.Array(dims=1),
    atm_level: float,
    day_counter: qDayCounter = ql.Actual365Fixed(),
    reference_date: qDate = ql.Date(),
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    flat_strike_extrapolation: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return ql.LinearInterpolatedSmileSection(
        date,
        to_float_list(strikes),
        to_float_list(standard_deviations),
        atm_level,
        day_counter,
        ql.Linear(),
        reference_date,
        volatility_type,
        shift,
        flat_strike_extrapolation,
    )


@xlo.func(
    help="Create a cubic interpolated smile section.",
    args={
        "expiry_time": "The time to expiry.",
        "strikes": "The smile strikes.",
        "standard_deviations": "The Black standard deviations at each strike.",
        "atm_level": "The at-the-money level.",
        "day_counter": "The day counter for the smile.",
        "volatility_type": "The volatility type.",
        "shift": "The displacement for shifted-lognormal volatility.",
        "flat_strike_extrapolation": "Whether to extrapolate flat in strike.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCubicInterpolatedSmileSection(
    expiry_time: float,
    strikes: xlo.Array(dims=1),
    standard_deviations: xlo.Array(dims=1),
    atm_level: float,
    day_counter: qDayCounter = ql.Actual365Fixed(),
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    flat_strike_extrapolation: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return ql.CubicInterpolatedSmileSection(
        expiry_time,
        to_float_list(strikes),
        to_float_list(standard_deviations),
        atm_level,
        ql.Cubic(),
        day_counter,
        volatility_type,
        shift,
        flat_strike_extrapolation,
    )


@xlo.func(
    help="Create a cubic interpolated smile section.",
    args={
        "date": "The date for the smile section.",
        "strikes": "The smile strikes.",
        "standard_deviations": "The Black standard deviations at each strike.",
        "atm_level": "The at-the-money level.",
        "day_counter": "The day counter for the smile.",
        "reference_date": "The reference date for the smile section.",
        "volatility_type": "The volatility type.",
        "shift": "The displacement for shifted-lognormal volatility.",
        "flat_strike_extrapolation": "Whether to extrapolate flat in strike.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCubicInterpolatedSmileSection2(
    date: qDate,
    strikes: xlo.Array(dims=1),
    standard_deviations: xlo.Array(dims=1),
    atm_level: float,
    day_counter: qDayCounter = ql.Actual365Fixed(),
    reference_date: qDate = ql.Date(),
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    flat_strike_extrapolation: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return ql.CubicInterpolatedSmileSection(
        date,
        to_float_list(strikes),
        to_float_list(standard_deviations),
        atm_level,
        day_counter,
        ql.Cubic(),
        reference_date,
        volatility_type,
        shift,
        flat_strike_extrapolation,
    )


@xlo.func(
    help="Create a monotonic cubic interpolated smile section.",
    args={
        "expiry_time": "The time to expiry.",
        "strikes": "The smile strikes.",
        "standard_deviations": "The Black standard deviations at each strike.",
        "atm_level": "The at-the-money level.",
        "day_counter": "The day counter for the smile.",
        "volatility_type": "The volatility type.",
        "shift": "The displacement for shifted-lognormal volatility.",
        "flat_strike_extrapolation": "Whether to extrapolate flat in strike.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMonotonicCubicInterpolatedSmileSection(
    expiry_time: float,
    strikes: xlo.Array(dims=1),
    standard_deviations: xlo.Array(dims=1),
    atm_level: float,
    day_counter: qDayCounter = ql.Actual365Fixed(),
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    flat_strike_extrapolation: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return ql.MonotonicCubicInterpolatedSmileSection(
        expiry_time,
        to_float_list(strikes),
        to_float_list(standard_deviations),
        atm_level,
        ql.MonotonicCubic(),
        day_counter,
        volatility_type,
        shift,
        flat_strike_extrapolation,
    )


@xlo.func(
    help="Create a monotonic cubic interpolated smile section.",
    args={
        "date": "The date for the smile section.",
        "strikes": "The smile strikes.",
        "standard_deviations": "The Black standard deviations at each strike.",
        "atm_level": "The at-the-money level.",
        "day_counter": "The day counter for the smile.",
        "reference_date": "The reference date for the smile section.",
        "volatility_type": "The volatility type.",
        "shift": "The displacement for shifted-lognormal volatility.",
        "flat_strike_extrapolation": "Whether to extrapolate flat in strike.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMonotonicCubicInterpolatedSmileSection2(
    date: qDate,
    strikes: xlo.Array(dims=1),
    standard_deviations: xlo.Array(dims=1),
    atm_level: float,
    day_counter: qDayCounter = ql.Actual365Fixed(),
    reference_date: qDate = ql.Date(),
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    flat_strike_extrapolation: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return ql.MonotonicCubicInterpolatedSmileSection(
        date,
        to_float_list(strikes),
        to_float_list(standard_deviations),
        atm_level,
        day_counter,
        ql.MonotonicCubic(),
        reference_date,
        volatility_type,
        shift,
        flat_strike_extrapolation,
    )


@xlo.func(
    help="Create a spline cubic interpolated smile section.",
    args={
        "expiry_time": "The time to expiry.",
        "strikes": "The smile strikes.",
        "standard_deviations": "The Black standard deviations at each strike.",
        "atm_level": "The at-the-money level.",
        "day_counter": "The day counter for the smile.",
        "volatility_type": "The volatility type.",
        "shift": "The displacement for shifted-lognormal volatility.",
        "flat_strike_extrapolation": "Whether to extrapolate flat in strike.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSplineCubicInterpolatedSmileSection(
    expiry_time: float,
    strikes: xlo.Array(dims=1),
    standard_deviations: xlo.Array(dims=1),
    atm_level: float,
    day_counter: qDayCounter = ql.Actual365Fixed(),
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    flat_strike_extrapolation: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return ql.SplineCubicInterpolatedSmileSection(
        expiry_time,
        to_float_list(strikes),
        to_float_list(standard_deviations),
        atm_level,
        ql.SplineCubic(),
        day_counter,
        volatility_type,
        shift,
        flat_strike_extrapolation,
    )


@xlo.func(
    help="Create a spline cubic interpolated smile section.",
    args={
        "date": "The date for the smile section.",
        "strikes": "The smile strikes.",
        "standard_deviations": "The Black standard deviations at each strike.",
        "atm_level": "The at-the-money level.",
        "day_counter": "The day counter for the smile.",
        "reference_date": "The reference date for the smile section.",
        "volatility_type": "The volatility type.",
        "shift": "The displacement for shifted-lognormal volatility.",
        "flat_strike_extrapolation": "Whether to extrapolate flat in strike.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSplineCubicInterpolatedSmileSection2(
    date: qDate,
    strikes: xlo.Array(dims=1),
    standard_deviations: xlo.Array(dims=1),
    atm_level: float,
    day_counter: qDayCounter = ql.Actual365Fixed(),
    reference_date: qDate = ql.Date(),
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    flat_strike_extrapolation: bool = False,
    trigger=None,
) -> ql.SmileSection:
    return ql.SplineCubicInterpolatedSmileSection(
        date,
        to_float_list(strikes),
        to_float_list(standard_deviations),
        atm_level,
        day_counter,
        ql.SplineCubic(),
        reference_date,
        volatility_type,
        shift,
        flat_strike_extrapolation,
    )


# TODO to test
@xlo.func(
    help="Creates a Kahale smile section from a source smile section.",
    args={
        "source": "Source smile section to process.",
        "atm": "ATM level (optional).",
        "interpolate": "Whether to interpolate (default: False).",
        "exponential_extrapolation": "Whether to use exponential extrapolation (default: False).",
        "delete_arbitrage_points": "Whether to delete arbitrage points (default: False).",
        "moneyness_grid": "Vector of moneyness values for the grid (optional).",
        "gap": "Gap for numerical differentiation (default: 1e-5).",
        "forced_left_index": "Forced left index for interpolation (default: -1).",
        "forced_right_index": "Forced right index for interpolation (default: QL_MAX_INTEGER).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlKahaleSmileSection(
    source: ql.SmileSection,
    atm: float = ql.nullDouble(),
    interpolate: bool = False,
    exponential_extrapolation: bool = False,
    delete_arbitrage_points: bool = False,
    moneyness_grid: xlo.Array(dims=1) = None,
    gap: float = 1e-5,
    forced_left_index: int = -1,
    forced_right_index: int = 2147483647,  # QL_MAX_INTEGER
    trigger=None,
) -> ql.SmileSection:
    moneyness_list = to_float_list(moneyness_grid) if moneyness_grid is not None else []
    return ql.KahaleSmileSection(
        source,
        atm,
        interpolate,
        exponential_extrapolation,
        delete_arbitrage_points,
        moneyness_list,
        gap,
        forced_left_index,
        forced_right_index,
    )


# TODO qlSwaptionVolatilityMatrixVolatilityType
#
# TODO Sabr Smile Section
# TODO SviSmileSection
# TODO SviInterpolatedSmileSection

# TODO ConstantYoYOptionletVolatility

#
# TODO ZABR
# TODO NoArbSabrSmileSection
# TODO AndreasenHugeVolatility
# TODO HestonBlackVolSurface
# TODO CmsMarket
#
