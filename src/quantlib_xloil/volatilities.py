import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate
from .calendars import qCalendar
from .daycounters import qDayCounter
from .utilities import first_key, UNKNOWN_KEY, UNKNOWN_VALUE, enum_value


# Volatility types

QL_VOLATILITY_TYPE = {
    'NORMAL' : ql.Normal,
    'SHIFTEDLOGNORMAL' : ql.ShiftedLognormal,
    UNKNOWN_KEY : UNKNOWN_VALUE,
}

def _qVolatilityType(s: str) -> int:
    return enum_value(s, QL_VOLATILITY_TYPE)

@xlo.converter()
def qVolatilityType(s: str) -> int:
    return _qVolatilityType(s)


# VolatilityTermStructure/BlackVolTermStructure interface

@xlo.func(
    help="Returns the minimum strike for which the volatility is defined.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object."
    },
    group=EXCEL_GROUP_NAME
)
def qlBlackVolTermStructureMinStrike(
    vol_tsh : ql.BlackVolTermStructureHandle,
    trigger=None
    ) -> float:
    #
    return vol_tsh.minStrike()

@xlo.func(
    help="Returns the maximum strike for which the volatility is defined.",
    args={
        "vol_tsh": "Handle to a BlackVolTermStructure object."
    },
    group=EXCEL_GROUP_NAME
)
def qlBlackVolTermStructureMaxStrike(
    vol_tsh : ql.BlackVolTermStructureHandle,
    trigger=None
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
    group=EXCEL_GROUP_NAME
)
def qlBlackVolTermStructureBlackVol(
    vol_tsh : ql.BlackVolTermStructureHandle,
    expiry_date : qDate,
    strike : float,
    extrapolate : bool = False,
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
    group=EXCEL_GROUP_NAME
)
def qlBlackVolTermStructureBlackVolFromTime(
    vol_tsh : ql.BlackVolTermStructureHandle,
    expiry_time : float,
    strike : float,
    extrapolate : bool = False,
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
    group=EXCEL_GROUP_NAME
)
def qlBlackVolTermStructureBlackVariance(
    vol_tsh : ql.BlackVolTermStructureHandle,
    expiry_date : qDate,
    strike : float,
    extrapolate : bool = False,
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
    group=EXCEL_GROUP_NAME
)
def qlBlackVolTermStructureBlackVarianceFromTime(
    vol_tsh : ql.BlackVolTermStructureHandle,
    expiry_time : float,
    strike : float,
    extrapolate : bool = False,
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
    group=EXCEL_GROUP_NAME
)
def qlBlackVolTermStructureBlackForwardVol(
    vol_tsh : ql.BlackVolTermStructureHandle,
    date_start : qDate,
    date_end : qDate,
    strike : float,
    extrapolate : bool = False,
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
    group=EXCEL_GROUP_NAME
)
def qlBlackVolTermStructureBlackForwardVolFromTime(
    vol_tsh : ql.BlackVolTermStructureHandle,
    time_start : float,
    time_end : float,
    strike : float,
    extrapolate : bool = False,
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
    group=EXCEL_GROUP_NAME
)
def qlBlackVolTermStructureBlackForwardVariance(
    vol_tsh : ql.BlackVolTermStructureHandle,
    date_start : qDate,
    date_end : qDate,
    strike : float,
    extrapolate : bool = False,
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
    group=EXCEL_GROUP_NAME
)
def qlBlackVolTermStructureBlackForwardVarianceFromTime(
    vol_tsh : ql.BlackVolTermStructureHandle,
    time_start : float,
    time_end : float,
    strike : float,
    extrapolate : bool = False,
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
    group=EXCEL_GROUP_NAME
)
def qlBlackConstantVol(
    reference_date : qDate,
    calendar : qCalendar,
    volatility : float,
    day_counter : qDayCounter,
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
    group=EXCEL_GROUP_NAME
)
def qlLocalVolTermStructureLocalVol(
    vol_tsh : ql.LocalVolTermStructureHandle,
    expiry_date : qDate,
    strike : float,
    extrapolate : bool = False,
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
    group=EXCEL_GROUP_NAME
)
def qlLocalVolTermStructureLocalVolFromTime(
    vol_tsh : ql.LocalVolTermStructureHandle,
    expiry_time : float,
    strike : float,
    extrapolate : bool = False,
    trigger=None,
    ) -> float:
    #
    return vol_tsh.localVol(expiry_time, strike, extrapolate)
