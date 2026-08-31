import QuantLib as ql
import xloil as xlo

from .calendars import qBusinessDayConvention, qCalendar
from .config import EXCEL_GROUP_NAME
from .date import qDate, qFrequency, qPeriod, _to_date_list
from .daycounters import qDayCounter
from .ratehelpers import qQuoteHandle
from .utilities import (
    enum_value,
    UNKNOWN_KEY,
    UNKNOWN_VALUE,
    to_float_matrix,
    to_float_list,
)

# Volatility types

QL_VOLATILITY_TYPE = {
    "NORMAL": ql.Normal,
    "SHIFTEDLOGNORMAL": ql.ShiftedLognormal,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_BLACK_VOL_TIME_EXTRAPOLATION = {
    "FLATVOLATILITY": ql.BlackVolTimeExtrapolation.FlatVolatility,
    "USEINTERPOLATOR": ql.BlackVolTimeExtrapolation.UseInterpolator,
    "LINEARVARIANCE": ql.BlackVolTimeExtrapolation.LinearVariance,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


QL_BLACK_VARIANCE_SURFACE_EXTRAPOLATION = {
    "CONSTANT": ql.BlackVarianceSurface.ConstantExtrapolation,
    "DEFAULT": ql.BlackVarianceSurface.InterpolatorDefaultExtrapolation,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qVolatilityType(s: str) -> int:
    return enum_value(s, QL_VOLATILITY_TYPE)


@xlo.converter()
def qVolatilityType(s: str) -> int:
    return _qVolatilityType(s)


def _qBlackVolTimeExtrapolation(s: str) -> int:
    return enum_value(s, QL_BLACK_VOL_TIME_EXTRAPOLATION)


@xlo.converter()
def qBlackVolTimeExtrapolation(s: str) -> int:
    return _qBlackVolTimeExtrapolation(s)


def _qBlackVarianceSurfaceExtrapolation(s: str) -> int:
    return enum_value(s, QL_BLACK_VARIANCE_SURFACE_EXTRAPOLATION)


@xlo.converter()
def qBlackVarianceSurfaceExtrapolation(s: str) -> int:
    return _qBlackVarianceSurfaceExtrapolation(s)


# SABR volatility functions


@xlo.func(
    help="Returns the SABR volatility for a given strike and forward.",
    args={
        "strike": "Option strike price.",
        "forward": "Forward price.",
        "expiry_time": "Time to expiry.",
        "alpha": "SABR alpha parameter.",
        "beta": "SABR beta parameter.",
        "nu": "SABR nu parameter.",
        "rho": "SABR rho parameter.",
        "volatility_type": "Volatility type (e.g. 'NORMAL' or 'SHIFTEDLOGNORMAL').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSabrVolatility(
    strike: float,
    forward: float,
    expiry_time: float,
    alpha: float,
    beta: float,
    nu: float,
    rho: float,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    trigger=None,
) -> float:
    return ql.sabrVolatility(
        strike,
        forward,
        expiry_time,
        alpha,
        beta,
        nu,
        rho,
        _qVolatilityType(volatility_type),
    )


@xlo.func(
    help="Returns the shifted SABR volatility for a given strike and forward.",
    args={
        "strike": "Option strike price.",
        "forward": "Forward price.",
        "expiry_time": "Time to expiry.",
        "alpha": "SABR alpha parameter.",
        "beta": "SABR beta parameter.",
        "nu": "SABR nu parameter.",
        "rho": "SABR rho parameter.",
        "shift": "Shift applied to strike and forward.",
        "volatility_type": "Volatility type (e.g. 'NORMAL' or 'SHIFTEDLOGNORMAL').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlShiftedSabrVolatility(
    strike: float,
    forward: float,
    expiry_time: float,
    alpha: float,
    beta: float,
    nu: float,
    rho: float,
    shift: float,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    trigger=None,
) -> float:
    return ql.shiftedSabrVolatility(
        strike,
        forward,
        expiry_time,
        alpha,
        beta,
        nu,
        rho,
        shift,
        _qVolatilityType(volatility_type),
    )


@xlo.func(
    help="Returns the Floch-Kennedy SABR volatility approximation.",
    args={
        "strike": "Option strike price.",
        "forward": "Forward price.",
        "expiry_time": "Time to expiry.",
        "alpha": "SABR alpha parameter.",
        "beta": "SABR beta parameter.",
        "nu": "SABR nu parameter.",
        "rho": "SABR rho parameter.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSabrFlochKennedyVolatility(
    strike: float,
    forward: float,
    expiry_time: float,
    alpha: float,
    beta: float,
    nu: float,
    rho: float,
    trigger=None,
) -> float:
    return ql.sabrFlochKennedyVolatility(
        strike, forward, expiry_time, alpha, beta, nu, rho
    )


@xlo.func(
    help="Returns an initial SABR parameter guess from three volatility points.",
    args={
        "k_m": "Strike below the forward.",
        "vol_m": "Volatility at k_m.",
        "k_0": "At-the-money strike.",
        "vol_0": "Volatility at k_0.",
        "k_p": "Strike above the forward.",
        "vol_p": "Volatility at k_p.",
        "forward": "Forward price.",
        "expiry_time": "Time to expiry.",
        "beta": "SABR beta parameter.",
        "shift": "Shift applied to strike and forward.",
        "volatility_type": "Volatility type (e.g. 'NORMAL' or 'SHIFTEDLOGNORMAL').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSabrGuess(
    k_m: float,
    vol_m: float,
    k_0: float,
    vol_0: float,
    k_p: float,
    vol_p: float,
    forward: float,
    expiry_time: float,
    beta: float,
    shift: float,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    trigger=None,
) -> list[float]:
    return list(
        ql.sabrGuess(
            k_m,
            vol_m,
            k_0,
            vol_0,
            k_p,
            vol_p,
            forward,
            expiry_time,
            beta,
            shift,
            _qVolatilityType(volatility_type),
        )
    )


# SmileSection constructors


@xlo.func(
    help="Creates a SabrSmileSection object.",
    args={
        "expiry_date": "Option expiry date.",
        "forward": "Forward price.",
        "sabr_parameters": "Array containing alpha, beta, nu, and rho.",
        "reference_date": "Reference date for time calculations.",
        "day_counter": "Day count convention for time calculations.",
        "shift": "Shift applied to strike and forward.",
        "volatility_type": "Volatility type (e.g. 'NORMAL' or 'SHIFTEDLOGNORMAL').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSabrSmileSection(
    expiry_date: qDate,
    forward: float,
    sabr_parameters: xlo.Array(dims=1),
    reference_date: qDate = ql.Date(),
    day_counter: qDayCounter = ql.Actual365Fixed(),
    shift: float = 0.0,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    trigger=None,
) -> ql.SabrSmileSection:
    return ql.SabrSmileSection(
        expiry_date,
        forward,
        to_float_list(sabr_parameters),
        reference_date,
        day_counter,
        shift,
        _qVolatilityType(volatility_type),
    )


@xlo.func(
    help="Creates a SabrSmileSection object from an expiry time.",
    args={
        "expiry_time": "Time to option expiry.",
        "forward": "Forward price.",
        "sabr_parameters": "Array containing alpha, beta, nu, and rho.",
        "shift": "Shift applied to strike and forward.",
        "volatility_type": "Volatility type (e.g. 'NORMAL' or 'SHIFTEDLOGNORMAL').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSabrSmileSectionFromTime(
    expiry_time: float,
    forward: float,
    sabr_parameters: xlo.Array(dims=1),
    shift: float = 0.0,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    trigger=None,
) -> ql.SabrSmileSection:
    return ql.SabrSmileSection(
        expiry_time,
        forward,
        to_float_list(sabr_parameters),
        shift,
        _qVolatilityType(volatility_type),
    )


@xlo.func(
    help="Creates a SviSmileSection object.",
    args={
        "expiry_date": "Option expiry date.",
        "forward": "Forward price.",
        "svi_parameters": "Array containing a, b, sigma, rho, and m.",
        "day_counter": "Day count convention for time calculations.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSviSmileSection(
    expiry_date: qDate,
    forward: float,
    svi_parameters: xlo.Array(dims=1),
    day_counter: qDayCounter = ql.Actual365Fixed(),
    trigger=None,
) -> ql.SviSmileSection:
    return ql.SviSmileSection(
        expiry_date, forward, to_float_list(svi_parameters), day_counter
    )


@xlo.func(
    help="Creates a SviSmileSection object from an expiry time.",
    args={
        "expiry_time": "Time to option expiry.",
        "forward": "Forward price.",
        "svi_parameters": "Array containing a, b, sigma, rho, and m.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSviSmileSectionFromTime(
    expiry_time: float,
    forward: float,
    svi_parameters: xlo.Array(dims=1),
    trigger=None,
) -> ql.SviSmileSection:
    return ql.SviSmileSection(expiry_time, forward, to_float_list(svi_parameters))


@xlo.func(
    help="Creates a FlatSmileSection object.",
    args={
        "expiry_date": "Option expiry date.",
        "volatility": "Constant volatility value.",
        "day_counter": "Day count convention for time calculations.",
        "reference_date": "Reference date for time calculations.",
        "atm_level": "At-the-money level.",
        "volatility_type": "Volatility type (e.g. 'NORMAL' or 'SHIFTEDLOGNORMAL').",
        "shift": "Shift applied to strike and forward.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFlatSmileSection(
    expiry_date: qDate,
    volatility: float,
    day_counter: qDayCounter,
    reference_date: qDate = ql.Date(),
    atm_level: float = ql.nullDouble(),
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    trigger=None,
) -> ql.FlatSmileSection:
    return ql.FlatSmileSection(
        expiry_date,
        volatility,
        day_counter,
        reference_date,
        atm_level,
        _qVolatilityType(volatility_type),
        shift,
    )


@xlo.func(
    help="Creates a FlatSmileSection object from an expiry time.",
    args={
        "expiry_time": "Time to option expiry.",
        "volatility": "Constant volatility value.",
        "day_counter": "Day count convention for time calculations.",
        "atm_level": "At-the-money level.",
        "volatility_type": "Volatility type (e.g. 'NORMAL' or 'SHIFTEDLOGNORMAL').",
        "shift": "Shift applied to strike and forward.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFlatSmileSectionFromTime(
    expiry_time: float,
    volatility: float,
    day_counter: qDayCounter,
    atm_level: float = ql.nullDouble(),
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    shift: float = 0.0,
    trigger=None,
) -> ql.FlatSmileSection:
    return ql.FlatSmileSection(
        expiry_time,
        volatility,
        day_counter,
        atm_level,
        _qVolatilityType(volatility_type),
        shift,
    )


@xlo.func(
    help="Creates a NoArbSabrSmileSection object.",
    args={
        "expiry_date": "Option expiry date.",
        "forward": "Forward price.",
        "sabr_parameters": "Array containing alpha, beta, nu, and rho.",
        "day_counter": "Day count convention for time calculations.",
        "shift": "Shift applied to strike and forward.",
        "volatility_type": "Volatility type (e.g. 'NORMAL' or 'SHIFTEDLOGNORMAL').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNoArbSabrSmileSection(
    expiry_date: qDate,
    forward: float,
    sabr_parameters: xlo.Array(dims=1),
    day_counter: qDayCounter = ql.Actual365Fixed(),
    shift: float = 0.0,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    trigger=None,
) -> ql.NoArbSabrSmileSection:
    return ql.NoArbSabrSmileSection(
        expiry_date,
        forward,
        to_float_list(sabr_parameters),
        day_counter,
        shift,
        _qVolatilityType(volatility_type),
    )


@xlo.func(
    help="Creates a NoArbSabrSmileSection object from an expiry time.",
    args={
        "expiry_time": "Time to option expiry.",
        "forward": "Forward price.",
        "sabr_parameters": "Array containing alpha, beta, nu, and rho.",
        "shift": "Shift applied to strike and forward.",
        "volatility_type": "Volatility type (e.g. 'NORMAL' or 'SHIFTEDLOGNORMAL').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNoArbSabrSmileSectionFromTime(
    expiry_time: float,
    forward: float,
    sabr_parameters: xlo.Array(dims=1),
    shift: float = 0.0,
    volatility_type: qVolatilityType = ql.ShiftedLognormal,
    trigger=None,
) -> ql.NoArbSabrSmileSection:
    return ql.NoArbSabrSmileSection(
        expiry_time,
        forward,
        to_float_list(sabr_parameters),
        shift,
        _qVolatilityType(volatility_type),
    )


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


@xlo.func(
    help="Creates a BlackVarianceSurface object and returns a handle to it.",
    args={
        "reference_date": "Reference date for the volatility surface.",
        "calendar": "Calendar for the volatility surface.",
        "dates": "Array of option expiry dates.",
        "strikes": "Array of strikes.",
        "black_vols": "2D array of Black volatilities with shape (#strikes, #dates).",
        "day_counter": "Day count convention for the volatility surface.",
        "lower_extrapolation": "Extrapolation below the minimum strike (default: DEFAULT).",
        "upper_extrapolation": "Extrapolation above the maximum strike (default: DEFAULT).",
        "interpolator": "Optional interpolation method.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackVarianceSurface(
    reference_date: qDate,
    calendar: qCalendar,
    dates: xlo.Array(dims=1),
    strikes: xlo.Array(dims=1),
    black_vols: xlo.Array(dims=2),
    day_counter: qDayCounter,
    lower_extrapolation: qBlackVarianceSurfaceExtrapolation = ql.BlackVarianceSurface.InterpolatorDefaultExtrapolation,
    upper_extrapolation: qBlackVarianceSurfaceExtrapolation = ql.BlackVarianceSurface.InterpolatorDefaultExtrapolation,
    interpolator: str = "",
    trigger=None,
) -> ql.BlackVolTermStructureHandle:
    vol_ts = ql.BlackVarianceSurface(
        reference_date,
        calendar,
        _to_date_list(dates),
        to_float_list(strikes),
        ql.Matrix(to_float_matrix(black_vols)),
        day_counter,
        lower_extrapolation,
        upper_extrapolation,
        interpolator,
    )
    return ql.BlackVolTermStructureHandle(vol_ts)


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


@xlo.func(
    help="Creates a ConstantYoYOptionletVolatility object and returns a handle to it.",
    args={
        "volatility": "Constant volatility value.",
        "settlement_days": "Number of settlement days.",
        "calendar": "Calendar for the volatility surface.",
        "business_day_convention": "Business day convention for the volatility surface.",
        "day_counter": "Day count convention for the volatility surface.",
        "observation_lag": "Observation lag for the YoY index.",
        "frequency": "Frequency of the YoY index.",
        "index_is_interpolated": "Whether the YoY index is interpolated.",
        "min_strike": "Minimum strike for the surface.",
        "max_strike": "Maximum strike for the surface.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlConstantYoYOptionletVolatility(
    volatility: float,
    settlement_days: int,
    calendar: qCalendar,
    business_day_convention: qBusinessDayConvention,
    day_counter: qDayCounter,
    observation_lag: qPeriod,
    frequency: qFrequency,
    index_is_interpolated: bool,
    min_strike: float = -1.0,
    max_strike: float = 100.0,
    trigger=None,
) -> ql.YoYOptionletVolatilitySurfaceHandle:
    vol_ts = ql.ConstantYoYOptionletVolatility(
        volatility,
        settlement_days,
        calendar,
        business_day_convention,
        day_counter,
        observation_lag,
        frequency,
        index_is_interpolated,
        min_strike,
        max_strike,
    )
    return ql.YoYOptionletVolatilitySurfaceHandle(vol_ts)


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


@xlo.func(
    help="Creates a SpreadedSwaptionVolatility object and returns a handle to it.",
    args={
        "vol_tsh": "Handle to the base SwaptionVolatilityStructure object.",
        "spread": "Handle to the additive volatility spread quote.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSpreadedSwaptionVolatility(
    vol_tsh: ql.SwaptionVolatilityStructureHandle,
    spread: qQuoteHandle,
    trigger=None,
) -> ql.SwaptionVolatilityStructureHandle:
    vol_ts = ql.SpreadedSwaptionVolatility(vol_tsh, spread)
    return ql.SwaptionVolatilityStructureHandle(vol_ts)


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
    #
    dates_list = _to_date_list(expiry_dates)
    length_list = [qPeriod.__wrapped__(length) for length in lengths]
    vol_matrix = ql.Matrix(to_float_matrix(vols))
    shift_matrix = ql.Matrix(to_float_matrix(shifts))
    #
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
