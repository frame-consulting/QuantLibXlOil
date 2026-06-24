import QuantLib as ql
import xloil as xlo

from .calendars import qBusinessDayConvention, qCalendar
from .config import EXCEL_GROUP_NAME
from .date import qDate, qPeriod
from .daycounters import qDayCounter
from .ratehelpers import qQuoteHandle
from .utilities import enum_value, UNKNOWN_KEY, UNKNOWN_VALUE

# Volatility types

QL_VOLATILITY_TYPE = {
    "NORMAL": ql.Normal,
    "SHIFTEDLOGNORMAL": ql.ShiftedLognormal,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qVolatilityType(s: str) -> int:
    return enum_value(s, QL_VOLATILITY_TYPE)


@xlo.converter()
def qVolatilityType(s: str) -> int:
    return _qVolatilityType(s)


# VolatilityTermStructure/BlackVolTermStructure interface


@xlo.func(
    help="Returns the minimum strike for which the volatility is defined.",
    args={"vol_tsh": "Handle to a BlackVolTermStructure object."},
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureMinStrike(
    vol_tsh: ql.BlackVolTermStructureHandle, trigger=None
) -> float:
    #
    return vol_tsh.minStrike()


@xlo.func(
    help="Returns the maximum strike for which the volatility is defined.",
    args={"vol_tsh": "Handle to a BlackVolTermStructure object."},
    group=EXCEL_GROUP_NAME,
)
def qlBlackVolTermStructureMaxStrike(
    vol_tsh: ql.BlackVolTermStructureHandle, trigger=None
) -> float:
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
    return vol_tsh.blackForwardVariance(time_start, time_end, strike, extrapolate)


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
    #
    volts = ql.BlackConstantVol(reference_date, calendar, volatility, day_counter)
    return ql.BlackVolTermStructureHandle(volts)


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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
    return vol_tsh.blackVariance(option_time, strike, extrapolate)


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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
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
    #
    return vol_tsh.optionDateFromTenor(option_tenor)


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
    #
    return vol_tsh.shift(option_date, swap_tenor, extrapolate)


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
def qlSwaptionVolatilityStructureShiftFromTime(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_time: float,
    swap_length: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    #
    return vol_tsh.shift(option_time, swap_length, extrapolate)


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
    #
    return vol_tsh.smileSection(option_date, swap_tenor, extrapolate)


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
def qlSwaptionVolatilityStructureSmileSectionFromTime(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    option_time: float,
    swap_length: float,
    extrapolate: bool = False,
    trigger=None,
) -> ql.SmileSection:
    #
    return vol_tsh.smileSection(option_time, swap_length, extrapolate)


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
    #
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
