import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate
from .daycounters import qDayCounter
from .ratehelpers import qQuoteHandle
from .stochasticprocess import _to_float_matrix
from .utilities import enum_value, first_key, UNKNOWN_KEY, UNKNOWN_VALUE


@xlo.func(
    help="Create a QuantLib LocalConstantVol object.",
    args={
        "reference_date": "Reference date for the local volatility surface.",
        "volatility": "Constant local volatility value.",
        "day_counter": "Day counter for time calculations.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLocalConstantVol(
    reference_date: qDate,
    volatility: float,
    day_counter: qDayCounter,
    trigger=None,
) -> ql.LocalVolTermStructureHandle:
    vol = ql.LocalConstantVol(reference_date, volatility, day_counter)
    return ql.LocalVolTermStructureHandle(vol)


@xlo.func(
    help="Create a QuantLib LocalVolSurface object.",
    args={
        "black_vol_tsh": "Handle to a BlackVolTermStructure object.",
        "risk_free_ytsh": "Handle to a risk-free YieldTermStructure object.",
        "dividend_ytsh": "Handle to a dividend YieldTermStructure object.",
        "underlying": "Handle to a Quote representing the underlying price.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlLocalVolSurface(
    black_vol_tsh: ql.BlackVolTermStructureHandle,
    risk_free_ytsh: ql.YieldTermStructureHandle,
    dividend_ytsh: ql.YieldTermStructureHandle,
    underlying: qQuoteHandle,
    trigger=None,
) -> ql.LocalVolTermStructureHandle:
    local_vol_surface = ql.LocalVolSurface(black_vol_tsh, risk_free_ytsh, dividend_ytsh, underlying)
    return ql.LocalVolTermStructureHandle(local_vol_surface)


@xlo.func(
    help="Create a QuantLib NoExceptLocalVolSurface object.",
    args={
        "black_vol_tsh": "Handle to a BlackVolTermStructure object.",
        "risk_free_ytsh": "Handle to a risk-free YieldTermStructure object.",
        "dividend_ytsh": "Handle to a dividend YieldTermStructure object.",
        "underlying": "Handle to a Quote representing the underlying price.",
        "illegal_local_vol_overwrite": "Value to overwrite illegal local volatilities with.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNoExceptLocalVolSurface(
    black_vol_tsh: ql.BlackVolTermStructureHandle,
    risk_free_ytsh: ql.YieldTermStructureHandle,
    dividend_ytsh: ql.YieldTermStructureHandle,
    underlying: qQuoteHandle,
    illegal_local_vol_overwrite: float,
    trigger=None,
) -> ql.LocalVolTermStructureHandle:
    local_vol_surface = ql.NoExceptLocalVolSurface(black_vol_tsh, risk_free_ytsh, dividend_ytsh, underlying, illegal_local_vol_overwrite)
    return ql.LocalVolTermStructureHandle(local_vol_surface)


QL_FIXEDLOCALVOL_SURFACE_EXTRAPOLATION = {
    'CONSTANT': ql.FixedLocalVolSurface.ConstantExtrapolation,
    'DEFAULT': ql.FixedLocalVolSurface.InterpolatorDefaultExtrapolation,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

def _qFixedLocalVolSurfaceExtrapolation(s: str) -> int:
    return enum_value(s, QL_FIXEDLOCALVOL_SURFACE_EXTRAPOLATION)

@xlo.converter()
def qFixedLocalVolSurfaceExtrapolation(s: str) -> int:
    return _qFixedLocalVolSurfaceExtrapolation(s)


@xlo.func(
    help="Create a QuantLib FixedLocalVolSurface object.",
    args={
        "reference_date": "Reference date for the local volatility surface.",
        "dates": "Array of expiry dates for the local volatility surface.",
        "strikes": "Array of strikes for the local volatility surface.",
        "local_vol_matrix": "Matrix of local volatilities with shape (#strikes, #dates).",
        "interpolation_str": "Interpolation method for the local volatility surface (LINEAR, CUBIC).",
        "lowerExtrapolation": "Extrapolation method for strikes below the minimum defined strike.",
        "upperExtrapolation": "Extrapolation method for strikes above the maximum defined strike.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFixedLocalVolSurface(
    reference_date: qDate,
    dates: xlo.Array(dims=1),
    strikes: xlo.Array(dims=1),
    local_vol_matrix: xlo.Array(dims=2),
    day_counter: qDayCounter,
    interpolation_str: str = "LINEAR",
    lowerExtrapolation: qFixedLocalVolSurfaceExtrapolation = ql.FixedLocalVolSurface.ConstantExtrapolation,
    upperExtrapolation: qFixedLocalVolSurfaceExtrapolation = ql.FixedLocalVolSurface.ConstantExtrapolation,
    trigger=None,
) -> ql.LocalVolTermStructureHandle:
    _dates = [ ql.Date(round(d)) for d in dates ]
    _strikes = [ float(s) for s in strikes ]
    _local_vol_matrix = ql.Matrix(_to_float_matrix(local_vol_matrix))
    local_vol_surface = ql.FixedLocalVolSurface(
        reference_date,
        _dates,
        _strikes,
        _local_vol_matrix,
        day_counter,
        lowerExtrapolation,
        upperExtrapolation,
    )
    local_vol_surface.setInterpolation(interpolation_str)
    return ql.LocalVolTermStructureHandle(local_vol_surface)
