import QuantLib as ql
import xloil as xlo

from .calendars import qBusinessDayConvention, qCalendar, QL_BUSINESSDAYCONVENTION
from .config import EXCEL_GROUP_NAME
from .currencies import qCurrency
from .date import qDate, qFrequency, qPeriod, _to_date_list, QL_FREQUENCY
from .daycounters import qDayCounter
from .ratehelpers import qQuoteHandle, qPillarChoice
from .swap import qSwapType, QL_SWAP_TYPE
from .utilities import (
    enum_value,
    first_key,
    to_float_list,
    to_float_matrix,
    to_object_list,
    UNKNOWN_KEY,
    UNKNOWN_VALUE,
)

## CPI Interpolation Type

QL_CPI_INTERPOLATION_TYPE = {
    "ASINDEX": ql.CPI.AsIndex,
    "FLAT": ql.CPI.Flat,
    "LINEAR": ql.CPI.Linear,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_YOY_INFLATION_CAPFLOOR_TYPE = {
    "CAP": ql.YoYInflationCapFloor.Cap,
    "FLOOR": ql.YoYInflationCapFloor.Floor,
    "COLLAR": ql.YoYInflationCapFloor.Collar,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qCPIInterpolationType(interpolation_type: str) -> int:
    return enum_value(interpolation_type, QL_CPI_INTERPOLATION_TYPE)


def _qYoYInflationCapFloorType(capfloor_type: str) -> int:
    return enum_value(capfloor_type, QL_YOY_INFLATION_CAPFLOOR_TYPE)


@xlo.converter()
def qCPIInterpolationType(interpolation_type: str) -> int:
    return _qCPIInterpolationType(interpolation_type)


@xlo.converter()
def qYoYInflationCapFloorType(capfloor_type: str) -> int:
    return _qYoYInflationCapFloorType(capfloor_type)


## Seasonality


# TODO
@xlo.func(
    help="Correct zero rate for seasonality.",
    args={
        "seasonality": "The seasonality object.",
        "date": "The date for the rate.",
        "r": "The rate to correct.",
        "its": "The inflation term structure or handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSeasonalityCorrectZeroRate(
    seasonality: ql.Seasonality,
    date: qDate,
    r: float,
    its: ql.InflationTermStructure,
    trigger=None,
) -> float:
    return seasonality.correctZeroRate(date, r, its)


# TODO
@xlo.func(
    help="Correct YoY rate for seasonality.",
    args={
        "seasonality": "The seasonality object.",
        "date": "The date for the rate.",
        "r": "The rate to correct.",
        "its": "The inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSeasonalityCorrectYoYRate(
    seasonality: ql.Seasonality,
    date: qDate,
    r: float,
    its: ql.InflationTermStructure,
    trigger=None,
) -> float:
    return seasonality.correctYoYRate(date, r, its)


# TODO
@xlo.func(
    help="Check if seasonality is consistent with inflation term structure.",
    args={
        "seasonality": "The seasonality object.",
        "its": "The inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSeasonalityIsConsistent(
    seasonality: ql.Seasonality, its: ql.InflationTermStructure, trigger=None
) -> bool:
    return seasonality.isConsistent(its)


@xlo.func(
    help="Create a QuantLib MultiplicativePriceSeasonality object.",
    args={
        "seasonality_base_date": "The base date for seasonality.",
        "frequency": "The frequency of seasonality adjustments.",
        "seasonality_factors": "The seasonality factors as a list.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiplicativePriceSeasonality(
    seasonality_base_date: qDate,
    frequency: qFrequency,
    seasonality_factors: xlo.Array(dims=1),
    trigger=None,
) -> ql.MultiplicativePriceSeasonality:
    factors = to_float_list(seasonality_factors)
    return ql.MultiplicativePriceSeasonality(seasonality_base_date, frequency, factors)


@xlo.func(
    help="Get the seasonality base date.",
    args={
        "seasonality": "The seasonality object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiplicativePriceSeasonalitySeasonalityBaseDate(
    seasonality: ql.Seasonality, trigger=None
) -> ql.Date:
    return seasonality.seasonalityBaseDate()


@xlo.func(
    help="Get the seasonality frequency.",
    args={
        "seasonality": "The seasonality object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiplicativePriceSeasonalityFrequency(
    seasonality: ql.Seasonality, trigger=None
):
    return first_key(QL_FREQUENCY, seasonality.frequency())


@xlo.func(
    help="Get the seasonality factors.",
    args={
        "seasonality": "The MultiplicativePriceSeasonality object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiplicativePriceSeasonalityFactors(
    seasonality: ql.MultiplicativePriceSeasonality, trigger=None
) -> list[float]:
    return seasonality.seasonalityFactors()


@xlo.func(
    help="Get the seasonality factor for a specific date.",
    args={
        "seasonality": "The MultiplicativePriceSeasonality object.",
        "date": "The date for which to get the seasonality factor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiplicativePriceSeasonalityFactor(
    seasonality: ql.MultiplicativePriceSeasonality, date: qDate, trigger=None
) -> float:
    return seasonality.seasonalityFactor(date)


@xlo.func(
    help="Create a QuantLib KerkhofSeasonality object.",
    args={
        "seasonality_base_date": "The base date for seasonality.",
        "seasonality_factors": "The seasonality factors as a list.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlKerkhofSeasonality(
    seasonality_base_date: qDate,
    seasonality_factors: xlo.Array(dims=1),
    trigger=None,
) -> ql.KerkhofSeasonality:
    factors = to_float_list(seasonality_factors)
    return ql.KerkhofSeasonality(seasonality_base_date, factors)


## Inflation Term Structure


@xlo.func(
    help="Get the observation lag of an inflation term structure.",
    args={
        "inflation_term_structure": "The inflation term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationTermStructureObservationLag(
    inflation_term_structure: ql.InflationTermStructure, trigger=None
) -> ql.Period:
    return inflation_term_structure.observationLag()


@xlo.func(
    help="Get the frequency of an inflation term structure.",
    args={
        "inflation_term_structure": "The inflation term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationTermStructureFrequency(
    inflation_term_structure: ql.InflationTermStructure, trigger=None
):
    return first_key(QL_FREQUENCY, inflation_term_structure.frequency())


@xlo.func(
    help="Get the base rate of an inflation term structure.",
    args={
        "inflation_term_structure": "The inflation term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationTermStructureBaseRate(
    inflation_term_structure: ql.InflationTermStructure, trigger=None
) -> float:
    return inflation_term_structure.baseRate()


@xlo.func(
    help="Get the base date of an inflation term structure.",
    args={
        "inflation_term_structure": "The inflation term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationTermStructureBaseDate(
    inflation_term_structure: ql.InflationTermStructure, trigger=None
) -> ql.Date:
    return inflation_term_structure.baseDate()


@xlo.func(
    help="Check if an inflation term structure has an explicit base date.",
    args={
        "inflation_term_structure": "The inflation term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationTermStructureHasExplicitBaseDate(
    inflation_term_structure: ql.InflationTermStructure, trigger=None
) -> bool:
    return inflation_term_structure.hasExplicitBaseDate()


@xlo.func(
    help="Set the seasonality for an inflation term structure.",
    args={
        "inflation_term_structure": "The inflation term structure.",
        "seasonality": "The seasonality object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationTermStructureSetSeasonality(
    inflation_term_structure: ql.InflationTermStructure,
    seasonality: ql.Seasonality,
    trigger=None,
) -> bool:
    inflation_term_structure.setSeasonality(seasonality)
    return True


@xlo.func(
    help="Get the seasonality of an inflation term structure.",
    args={
        "inflation_term_structure": "The inflation term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationTermStructureSeasonality(
    inflation_term_structure: ql.InflationTermStructure, trigger=None
) -> ql.Seasonality:
    return inflation_term_structure.seasonality()


@xlo.func(
    help="Check if an inflation term structure has seasonality.",
    args={
        "inflation_term_structure": "The inflation term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationTermStructureHasSeasonality(
    inflation_term_structure: ql.InflationTermStructure, trigger=None
) -> bool:
    return inflation_term_structure.hasSeasonality()


## YoY Inflation Term Structure


@xlo.func(
    help="Get the YoY rate for a YoY inflation term structure at a specific date.",
    args={
        "yoy_inflation_term_structure": "The YoY inflation term structure.",
        "date": "The date for which to get the YoY rate.",
        "extrapolate": "Whether to extrapolate if the date is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationTermStructureYoYRate(
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle,
    date: qDate,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return yoy_inflation_term_structure.currentLink().yoyRate(date, extrapolate)


@xlo.func(
    help="Get the YoY rate for a YoY inflation term structure with observation lag.",
    args={
        "yoy_inflation_term_structure": "The YoY inflation term structure.",
        "date": "The date for which to get the YoY rate.",
        "observation_lag": "The observation lag.",
        "force_linear_interpolation": "Whether to force linear interpolation.",
        "extrapolate": "Whether to extrapolate if the date is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationTermStructureYoYRate2(
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle,
    date: qDate,
    observation_lag: qPeriod,
    force_linear_interpolation: bool = False,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return yoy_inflation_term_structure.currentLink().yoyRate(
        date, observation_lag, force_linear_interpolation, extrapolate
    )


@xlo.func(
    help="Get the YoY rate for a YoY inflation term structure at a specific time.",
    args={
        "yoy_inflation_term_structure": "The YoY inflation term structure.",
        "time": "The time for which to get the YoY rate.",
        "extrapolate": "Whether to extrapolate if the time is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationTermStructureYoYRate3(
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle,
    time: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return yoy_inflation_term_structure.currentLink().yoyRate(time, extrapolate)


## Zero Inflation Term Structure


@xlo.func(
    help="Get the zero rate for a zero inflation term structure at a specific date.",
    args={
        "zero_inflation_term_structure": "The zero inflation term structure.",
        "date": "The date for which to get the zero rate.",
        "extrapolate": "Whether to extrapolate if the date is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationTermStructureZeroRate(
    zero_inflation_term_structure: ql.ZeroInflationTermStructureHandle,
    date: qDate,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return zero_inflation_term_structure.currentLink().zeroRate(date, extrapolate)


@xlo.func(
    help="Get the zero rate for a zero inflation term structure with observation lag.",
    args={
        "zero_inflation_term_structure": "The zero inflation term structure.",
        "date": "The date for which to get the zero rate.",
        "observation_lag": "The observation lag.",
        "force_linear_interpolation": "Whether to force linear interpolation.",
        "extrapolate": "Whether to extrapolate if the date is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationTermStructureZeroRate2(
    zero_inflation_term_structure: ql.ZeroInflationTermStructureHandle,
    date: qDate,
    observation_lag: qPeriod,
    force_linear_interpolation: bool = False,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return zero_inflation_term_structure.currentLink().zeroRate(
        date, observation_lag, force_linear_interpolation, extrapolate
    )


@xlo.func(
    help="Get the zero rate for a zero inflation term structure at a specific time.",
    args={
        "zero_inflation_term_structure": "The zero inflation term structure.",
        "time": "The time for which to get the zero rate.",
        "extrapolate": "Whether to extrapolate if the time is outside the term structure range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationTermStructureZeroRate3(
    zero_inflation_term_structure: ql.ZeroInflationTermStructureHandle,
    time: float,
    extrapolate: bool = False,
    trigger=None,
) -> float:
    return zero_inflation_term_structure.currentLink().zeroRate(time, extrapolate)


## Region


@xlo.func(
    help="Create a QuantLib CustomRegion object.",
    args={
        "name": "The name of the region.",
        "code": "The code of the region.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCustomRegion(name: str, code: str, trigger=None) -> ql.CustomRegion:
    return ql.CustomRegion(name, code)


@xlo.func(
    help="Get the name of a region.",
    args={
        "region": "The region object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRegionName(region: ql.Region, trigger=None) -> str:
    return region.name()


@xlo.func(
    help="Get the code of a region.",
    args={
        "region": "The region object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRegionCode(region: ql.Region, trigger=None) -> str:
    return region.code()


## Inflation Index


@xlo.func(
    help="Get the family name of an inflation index.",
    args={
        "index": "The inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationIndexFamilyName(index: ql.InflationIndex, trigger=None) -> str:
    return index.familyName()


@xlo.func(
    help="Get the region of an inflation index.",
    args={
        "index": "The inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationIndexRegion(index: ql.InflationIndex, trigger=None) -> ql.Region:
    return index.region()


@xlo.func(
    help="Check if an inflation index is revised.",
    args={
        "index": "The inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationIndexRevised(index: ql.InflationIndex, trigger=None) -> bool:
    return index.revised()


@xlo.func(
    help="Get the frequency of an inflation index.",
    args={
        "index": "The inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationIndexFrequency(index: ql.InflationIndex, trigger=None):
    return first_key(QL_FREQUENCY, index.frequency())


@xlo.func(
    help="Get the availability lag of an inflation index.",
    args={
        "index": "The inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationIndexAvailabilityLag(
    index: ql.InflationIndex, trigger=None
) -> ql.Period:
    return index.availabilityLag()


@xlo.func(
    help="Get the currency of an inflation index.",
    args={
        "index": "The inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationIndexCurrency(index: ql.InflationIndex, trigger=None) -> ql.Currency:
    return index.currency()


## Zero Inflation Index


@xlo.func(
    help="Create a QuantLib ZeroInflationIndex object.",
    args={
        "family_name": "The family name of the index.",
        "region": "The region of the index.",
        "revised": "Whether the index is revised.",
        "frequency": "The frequency of the index.",
        "availability_lag": "The availability lag of the index.",
        "currency": "The currency of the index.",
        "zero_inflation_term_structure": "The zero inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationIndex(
    family_name: str,
    region: ql.Region,
    revised: bool,
    frequency: qFrequency,
    availability_lag: qPeriod,
    currency: qCurrency,
    zero_inflation_term_structure: ql.ZeroInflationTermStructure = ql.ZeroInflationTermStructureHandle(),
    trigger=None,
) -> ql.ZeroInflationIndex:
    return ql.ZeroInflationIndex(
        family_name,
        region,
        revised,
        frequency,
        availability_lag,
        currency,
        zero_inflation_term_structure,
    )


@xlo.func(
    help="Get the last fixing date of a zero inflation index.",
    args={
        "index": "The zero inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationIndexLastFixingDate(
    index: ql.ZeroInflationIndex, trigger=None
) -> ql.Date:
    return index.lastFixingDate()


@xlo.func(
    help="Get the zero inflation term structure of a zero inflation index.",
    args={
        "index": "The zero inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationIndexZeroInflationTermStructure(
    index: ql.ZeroInflationIndex, trigger=None
) -> ql.ZeroInflationTermStructureHandle:
    return index.zeroInflationTermStructure()


@xlo.func(
    help="Clone a zero inflation index with a different term structure.",
    args={
        "index": "The zero inflation index to clone.",
        "zero_inflation_term_structure": "The new zero inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationIndexClone(
    index: ql.ZeroInflationIndex,
    zero_inflation_term_structure: ql.ZeroInflationTermStructureHandle,
    trigger=None,
) -> ql.ZeroInflationIndex:
    return index.clone(zero_inflation_term_structure)


@xlo.func(
    help="Check if a zero inflation index needs forecast for a given fixing date.",
    args={
        "index": "The zero inflation index to query.",
        "fixing_date": "The fixing date to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationIndexNeedsForecast(
    index: ql.ZeroInflationIndex, fixing_date: qDate, trigger=None
) -> bool:
    return index.needsForecast(fixing_date)


## YoY Inflation Index


@xlo.func(
    help="Create a QuantLib YoYInflationIndex object from an underlying zero inflation index.",
    args={
        "underlying_index": "The underlying zero inflation index.",
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
        "interpolated": "Whether the index is interpolated.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationIndex(
    underlying_index: ql.ZeroInflationIndex,
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    interpolated: bool = False,
    trigger=None,
) -> ql.YoYInflationIndex:
    return ql.YoYInflationIndex(
        underlying_index, interpolated, yoy_inflation_term_structure
    )


@xlo.func(
    help="Create a QuantLib YoYInflationIndex object from parameters.",
    args={
        "family_name": "The family name of the index.",
        "region": "The region of the index.",
        "revised": "Whether the index is revised.",
        "frequency": "The frequency of the index.",
        "availability_lag": "The availability lag of the index.",
        "currency": "The currency of the index.",
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
        "interpolated": "Whether the index is interpolated.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationIndex2(
    family_name: str,
    region: ql.Region,
    revised: bool,
    frequency: qFrequency,
    availability_lag: qPeriod,
    currency: qCurrency,
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    interpolated: bool = False,
    trigger=None,
) -> ql.YoYInflationIndex:
    return ql.YoYInflationIndex(
        family_name,
        region,
        revised,
        interpolated,
        frequency,
        availability_lag,
        currency,
        yoy_inflation_term_structure,
    )


@xlo.func(
    help="Get the last fixing date of a YoY inflation index.",
    args={
        "index": "The YoY inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationIndexLastFixingDate(
    index: ql.YoYInflationIndex, trigger=None
) -> ql.Date:
    return index.lastFixingDate()


@xlo.func(
    help="Check if a YoY inflation index is a ratio.",
    args={
        "index": "The YoY inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationIndexRatio(index: ql.YoYInflationIndex, trigger=None) -> bool:
    return index.ratio()


@xlo.func(
    help="Check if a YoY inflation index is interpolated.",
    args={
        "index": "The YoY inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationIndexInterpolated(index: ql.YoYInflationIndex, trigger=None) -> bool:
    return index.interpolated()


# ToDo
@xlo.func(
    help="Get the underlying zero inflation index of a YoY inflation index.",
    args={
        "index": "The YoY inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationIndexUnderlyingIndex(
    index: ql.YoYInflationIndex, trigger=None
) -> ql.ZeroInflationIndex:
    return index.underlyingIndex()


@xlo.func(
    help="Get the YoY inflation term structure of a YoY inflation index.",
    args={
        "index": "The YoY inflation index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationIndexYoYInflationTermStructure(
    index: ql.YoYInflationIndex, trigger=None
) -> ql.YoYInflationTermStructureHandle:
    return index.yoyInflationTermStructure()


@xlo.func(
    help="Clone a YoY inflation index with a different term structure.",
    args={
        "index": "The YoY inflation index to clone.",
        "yoy_inflation_term_structure": "The new YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationIndexClone(
    index: ql.YoYInflationIndex,
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle,
    trigger=None,
) -> ql.YoYInflationIndex:
    return index.clone(yoy_inflation_term_structure)


@xlo.func(
    help="Check if a YoY inflation index needs forecast for a given fixing date.",
    args={
        "index": "The YoY inflation index to query.",
        "fixing_date": "The fixing date to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationIndexNeedsForecast(
    index: ql.YoYInflationIndex, fixing_date: qDate, trigger=None
) -> bool:
    return index.needsForecast(fixing_date)


# Zero Inflation Index instances


@xlo.func(
    help="Create a QuantLib AUCPI (Australian CPI) index.",
    args={
        "frequency": "The frequency of the index.",
        "revised": "Whether the index is revised.",
        "zero_inflation_term_structure": "The zero inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAUCPI(
    frequency: qFrequency,
    revised: bool,
    zero_inflation_term_structure: ql.ZeroInflationTermStructureHandle = ql.ZeroInflationTermStructureHandle(),
    trigger=None,
) -> ql.AUCPI:
    return ql.AUCPI(frequency, revised, zero_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib EUHICP index.",
    args={
        "zero_inflation_term_structure": "The zero inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEUHICP(
    zero_inflation_term_structure: ql.ZeroInflationTermStructureHandle = ql.ZeroInflationTermStructureHandle(),
    trigger=None,
) -> ql.EUHICP:
    return ql.EUHICP(zero_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib EUHICPXT index.",
    args={
        "zero_inflation_term_structure": "The zero inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEUHICPXT(
    zero_inflation_term_structure: ql.ZeroInflationTermStructureHandle = ql.ZeroInflationTermStructureHandle(),
    trigger=None,
) -> ql.EUHICPXT:
    return ql.EUHICPXT(zero_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib FRHICP index.",
    args={
        "zero_inflation_term_structure": "The zero inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFRHICP(
    zero_inflation_term_structure: ql.ZeroInflationTermStructureHandle = ql.ZeroInflationTermStructureHandle(),
    trigger=None,
) -> ql.FRHICP:
    return ql.FRHICP(zero_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib UKRPI index.",
    args={
        "zero_inflation_term_structure": "The zero inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlUKRPI(
    zero_inflation_term_structure: ql.ZeroInflationTermStructureHandle = ql.ZeroInflationTermStructureHandle(),
    trigger=None,
) -> ql.UKRPI:
    return ql.UKRPI(zero_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib UKHICP index.",
    args={
        "zero_inflation_term_structure": "The zero inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlUKHICP(
    zero_inflation_term_structure: ql.ZeroInflationTermStructureHandle = ql.ZeroInflationTermStructureHandle(),
    trigger=None,
) -> ql.UKHICP:
    return ql.UKHICP(zero_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib USCPI index.",
    args={
        "zero_inflation_term_structure": "The zero inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlUSCPI(
    zero_inflation_term_structure: ql.ZeroInflationTermStructureHandle = ql.ZeroInflationTermStructureHandle(),
    trigger=None,
) -> ql.USCPI:
    return ql.USCPI(zero_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib ZACPI index.",
    args={
        "zero_inflation_term_structure": "The zero inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZACPI(
    zero_inflation_term_structure: ql.ZeroInflationTermStructureHandle = ql.ZeroInflationTermStructureHandle(),
    trigger=None,
) -> ql.ZACPI:
    return ql.ZACPI(zero_inflation_term_structure)


# YoY Inflation Index instances


@xlo.func(
    help="Create a QuantLib YYEUHICP index.",
    args={
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYYEUHICP(
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    trigger=None,
) -> ql.YYEUHICP:
    return ql.YYEUHICP(yoy_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib YYEUHICP index.",
    args={
        "interpolated": "Whether the index is interpolated.",
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYYEUHICP2(
    interpolated: bool,
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    trigger=None,
) -> ql.YYEUHICP:
    return ql.YYEUHICP(interpolated, yoy_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib YYEUHICPXT index.",
    args={
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYYEUHICPXT(
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    trigger=None,
) -> ql.YYEUHICPXT:
    return ql.YYEUHICPXT(yoy_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib YYEUHICPXT index.",
    args={
        "interpolated": "Whether the index is interpolated.",
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYYEUHICPXT2(
    interpolated: bool,
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    trigger=None,
) -> ql.YYEUHICPXT:
    return ql.YYEUHICPXT(interpolated, yoy_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib YYFRHICP index.",
    args={
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYYFRHICP(
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    trigger=None,
) -> ql.YYFRHICP:
    return ql.YYFRHICP(yoy_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib YYFRHICP index.",
    args={
        "interpolated": "Whether the index is interpolated.",
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYYFRHICP2(
    interpolated: bool,
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    trigger=None,
) -> ql.YYFRHICP:
    return ql.YYFRHICP(interpolated, yoy_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib YYUKRPI index.",
    args={
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYYUKRPI(
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    trigger=None,
) -> ql.YYUKRPI:
    return ql.YYUKRPI(yoy_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib YYUKRPI index.",
    args={
        "interpolated": "Whether the index is interpolated.",
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYYUKRPI2(
    interpolated: bool,
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    trigger=None,
) -> ql.YYUKRPI:
    return ql.YYUKRPI(interpolated, yoy_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib YYUSCPI index.",
    args={
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYYUSCPI(
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    trigger=None,
) -> ql.YYUSCPI:
    return ql.YYUSCPI(yoy_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib YYUSCPI index.",
    args={
        "interpolated": "Whether the index is interpolated.",
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYYUSCPI2(
    interpolated: bool,
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    trigger=None,
) -> ql.YYUSCPI:
    return ql.YYUSCPI(interpolated, yoy_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib YYZACPI index.",
    args={
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYYZACPI(
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    trigger=None,
) -> ql.YYZACPI:
    return ql.YYZACPI(yoy_inflation_term_structure)


@xlo.func(
    help="Create a QuantLib YYZACPI index.",
    args={
        "interpolated": "Whether the index is interpolated.",
        "yoy_inflation_term_structure": "The YoY inflation term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYYZACPI2(
    interpolated: bool,
    yoy_inflation_term_structure: ql.YoYInflationTermStructureHandle = ql.YoYInflationTermStructureHandle(),
    trigger=None,
) -> ql.YYZACPI:
    return ql.YYZACPI(interpolated, yoy_inflation_term_structure)


## CPI Utilities


@xlo.func(
    help="Calculate the lagged fixing for a zero inflation index.",
    args={
        "index": "The zero inflation index.",
        "date": "The date for which to calculate the lagged fixing.",
        "observation_lag": "The observation lag.",
        "interpolation_type": "The interpolation type (ASINDEX, FLAT, LINEAR).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPILaggedFixing(
    index: ql.ZeroInflationIndex,
    date: qDate,
    observation_lag: qPeriod,
    interpolation_type: qCPIInterpolationType,
    trigger=None,
) -> float:
    return ql.CPI.laggedFixing(index, date, observation_lag, interpolation_type)


@xlo.func(
    help="Calculate the lagged YoY rate for a YoY inflation index.",
    args={
        "index": "The YoY inflation index.",
        "date": "The date for which to calculate the lagged YoY rate.",
        "observation_lag": "The observation lag.",
        "interpolation_type": "The interpolation type (ASINDEX, FLAT, LINEAR).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPILaggedYoYRate(
    index: ql.YoYInflationIndex,
    date: qDate,
    observation_lag: qPeriod,
    interpolation_type: qCPIInterpolationType,
    trigger=None,
) -> float:
    return ql.CPI.laggedYoYRate(index, date, observation_lag, interpolation_type)


## Inflation Cash Flows


@xlo.func(
    help="Get the fixing date of an inflation coupon.",
    args={
        "inflation_coupon": "The inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationCouponFixingDate(
    inflation_coupon: ql.InflationCoupon, trigger=None
) -> ql.Date:
    return inflation_coupon.fixingDate()


@xlo.func(
    help="Get the fixing days of an inflation coupon.",
    args={
        "inflation_coupon": "The inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationCouponFixingDays(
    inflation_coupon: ql.InflationCoupon, trigger=None
) -> int:
    return inflation_coupon.fixingDays()


@xlo.func(
    help="Get the observation lag of an inflation coupon.",
    args={
        "inflation_coupon": "The inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationCouponObservationLag(
    inflation_coupon: ql.InflationCoupon, trigger=None
) -> ql.Period:
    return inflation_coupon.observationLag()


@xlo.func(
    help="Get the index fixing of an inflation coupon.",
    args={
        "inflation_coupon": "The inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationCouponIndexFixing(
    inflation_coupon: ql.InflationCoupon, trigger=None
) -> float:
    return inflation_coupon.indexFixing()


@xlo.func(
    help="Get the index of an inflation coupon.",
    args={
        "inflation_coupon": "The inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationCouponIndex(
    inflation_coupon: ql.InflationCoupon, trigger=None
) -> ql.InflationIndex:
    return inflation_coupon.index()


## CPI Coupon


@xlo.func(
    help="Create a QuantLib CPICouponPricer object.",
    args={},
    group=EXCEL_GROUP_NAME,
)
def qlCPICouponPricer(
    trigger=None,
) -> ql.CPICouponPricer:
    return ql.CPICouponPricer()


@xlo.func(
    help="Create a QuantLib CPICoupon object.",
    args={
        "base_cpi": "The base CPI value.",
        "payment_date": "The payment date.",
        "nominal": "The nominal amount.",
        "start_date": "The start date.",
        "end_date": "The end date.",
        "index": "The zero inflation index.",
        "observation_lag": "The observation lag.",
        "observation_interpolation": "The observation interpolation type (ASINDEX, FLAT, LINEAR).",
        "day_counter": "The day counter.",
        "fixed_rate": "The fixed rate.",
        "ref_period_start": "The reference period start date.",
        "ref_period_end": "The reference period end date.",
        "ex_coupon_date": "The ex-coupon date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICoupon(
    base_cpi: float,
    payment_date: qDate,
    nominal: float,
    start_date: qDate,
    end_date: qDate,
    index: ql.ZeroInflationIndex,
    observation_lag: qPeriod,
    observation_interpolation: qCPIInterpolationType,
    day_counter: qDayCounter,
    fixed_rate: float,
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    ex_coupon_date: qDate = ql.Date(),
    trigger=None,
) -> ql.CPICoupon:
    return ql.CPICoupon(
        base_cpi,
        payment_date,
        nominal,
        start_date,
        end_date,
        index,
        observation_lag,
        observation_interpolation,
        day_counter,
        fixed_rate,
        ref_period_start,
        ref_period_end,
        ex_coupon_date,
    )


@xlo.func(
    help="Create a QuantLib CPICoupon object from base date.",
    args={
        "base_date": "The base date.",
        "payment_date": "The payment date.",
        "nominal": "The nominal amount.",
        "start_date": "The start date.",
        "end_date": "The end date.",
        "index": "The zero inflation index.",
        "observation_lag": "The observation lag.",
        "observation_interpolation": "The observation interpolation type (ASINDEX, FLAT, LINEAR).",
        "day_counter": "The day counter.",
        "fixed_rate": "The fixed rate.",
        "ref_period_start": "The reference period start date.",
        "ref_period_end": "The reference period end date.",
        "ex_coupon_date": "The ex-coupon date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICoupon2(
    base_date: qDate,
    payment_date: qDate,
    nominal: float,
    start_date: qDate,
    end_date: qDate,
    index: ql.ZeroInflationIndex,
    observation_lag: qPeriod,
    observation_interpolation: qCPIInterpolationType,
    day_counter: qDayCounter,
    fixed_rate: float,
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    ex_coupon_date: qDate = ql.Date(),
    trigger=None,
) -> ql.CPICoupon:
    return ql.CPICoupon(
        base_date,
        payment_date,
        nominal,
        start_date,
        end_date,
        index,
        observation_lag,
        observation_interpolation,
        day_counter,
        fixed_rate,
        ref_period_start,
        ref_period_end,
        ex_coupon_date,
    )


@xlo.func(
    help="Create a QuantLib CPICoupon object from base CPI and base date.",
    args={
        "base_cpi": "The base CPI value.",
        "base_date": "The base date.",
        "payment_date": "The payment date.",
        "nominal": "The nominal amount.",
        "start_date": "The start date.",
        "end_date": "The end date.",
        "index": "The zero inflation index.",
        "observation_lag": "The observation lag.",
        "observation_interpolation": "The observation interpolation type (ASINDEX, FLAT, LINEAR).",
        "day_counter": "The day counter.",
        "fixed_rate": "The fixed rate.",
        "ref_period_start": "The reference period start date.",
        "ref_period_end": "The reference period end date.",
        "ex_coupon_date": "The ex-coupon date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICoupon3(
    base_cpi: float,
    base_date: qDate,
    payment_date: qDate,
    nominal: float,
    start_date: qDate,
    end_date: qDate,
    index: ql.ZeroInflationIndex,
    observation_lag: qPeriod,
    observation_interpolation: qCPIInterpolationType,
    day_counter: qDayCounter,
    fixed_rate: float,
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    ex_coupon_date: qDate = ql.Date(),
    trigger=None,
) -> ql.CPICoupon:
    return ql.CPICoupon(
        base_cpi,
        base_date,
        payment_date,
        nominal,
        start_date,
        end_date,
        index,
        observation_lag,
        observation_interpolation,
        day_counter,
        fixed_rate,
        ref_period_start,
        ref_period_end,
        ex_coupon_date,
    )


@xlo.func(
    help="Get the fixed rate of a CPI coupon.",
    args={
        "cpi_coupon": "The CPI coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICouponFixedRate(cpi_coupon: ql.CPICoupon, trigger=None) -> float:
    return cpi_coupon.fixedRate()


@xlo.func(
    help="Get the adjusted index growth of a CPI coupon.",
    args={
        "cpi_coupon": "The CPI coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICouponAdjustedIndexGrowth(cpi_coupon: ql.CPICoupon, trigger=None) -> float:
    return cpi_coupon.adjustedIndexGrowth()


@xlo.func(
    help="Get the index fixing of a CPI coupon.",
    args={
        "cpi_coupon": "The CPI coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICouponIndexFixing(cpi_coupon: ql.CPICoupon, trigger=None) -> float:
    return cpi_coupon.indexFixing()


@xlo.func(
    help="Get the index ratio of a CPI coupon at a specific date.",
    args={
        "cpi_coupon": "The CPI coupon.",
        "date": "The date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICouponIndexRatio(cpi_coupon: ql.CPICoupon, date: qDate, trigger=None) -> float:
    return cpi_coupon.indexRatio(date)


@xlo.func(
    help="Get the base CPI of a CPI coupon.",
    args={
        "cpi_coupon": "The CPI coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICouponBaseCPI(cpi_coupon: ql.CPICoupon, trigger=None) -> float:
    return cpi_coupon.baseCPI()


@xlo.func(
    help="Get the base date of a CPI coupon.",
    args={
        "cpi_coupon": "The CPI coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICouponBaseDate(cpi_coupon: ql.CPICoupon, trigger=None) -> ql.Date:
    return cpi_coupon.baseDate()


@xlo.func(
    help="Get the observation interpolation of a CPI coupon.",
    args={
        "cpi_coupon": "The CPI coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICouponObservationInterpolation(cpi_coupon: ql.CPICoupon, trigger=None):
    return first_key(QL_CPI_INTERPOLATION_TYPE, cpi_coupon.observationInterpolation())


@xlo.func(
    help="Get the CPI index of a CPI coupon.",
    args={
        "cpi_coupon": "The CPI coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICouponCPIIndex(
    cpi_coupon: ql.CPICoupon, trigger=None
) -> ql.ZeroInflationIndex:
    return cpi_coupon.cpiIndex()


@xlo.func(
    help="Set the pricer for a CPI coupon.",
    args={
        "coupon": "The CPI coupon to set the pricer for.",
        "pricer": "The CPI coupon pricer.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICouponSetPricer(
    coupon: ql.CPICoupon,
    pricer: ql.CPICouponPricer,
    trigger=None,
) -> bool:
    coupon.setPricer(pricer)
    return True


## CPI Cash Flow


@xlo.func(
    help="Create a QuantLib CPICashFlow object.",
    args={
        "notional": "The notional amount.",
        "index": "The zero inflation index.",
        "base_date": "The base date.",
        "base_fixing": "The base fixing.",
        "observation_date": "The observation date.",
        "observation_lag": "The observation lag.",
        "interpolation": "The interpolation type (ASINDEX, FLAT, LINEAR).",
        "payment_date": "The payment date.",
        "growth_only": "Whether to pay growth only.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICashFlow(
    notional: float,
    index: ql.ZeroInflationIndex,
    base_date: qDate,
    base_fixing: float,
    observation_date: qDate,
    observation_lag: qPeriod,
    interpolation: qCPIInterpolationType,
    payment_date: qDate,
    growth_only: bool = False,
    trigger=None,
) -> ql.CPICashFlow:
    return ql.CPICashFlow(
        notional,
        index,
        base_date,
        base_fixing,
        observation_date,
        observation_lag,
        interpolation,
        payment_date,
        growth_only,
    )


@xlo.func(
    help="Get the interpolation of a CPI cash flow.",
    args={
        "cpi_cash_flow": "The CPI cash flow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICashFlowInterpolation(cpi_cash_flow: ql.CPICashFlow, trigger=None):
    return first_key(QL_CPI_INTERPOLATION_TYPE, cpi_cash_flow.interpolation())


@xlo.func(
    help="Get the frequency of a CPI cash flow.",
    args={
        "cpi_cash_flow": "The CPI cash flow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPICashFlowFrequency(cpi_cash_flow: ql.CPICashFlow, trigger=None):
    return first_key(QL_FREQUENCY, cpi_cash_flow.frequency())


## CPI Leg


# caps/floors on CPI coupons not implemented
@xlo.func(
    help="Create a QuantLib CPILeg object.",
    args={
        "nominals": "The nominal amounts for the CPI leg.",
        "schedule": "The schedule for the CPI leg.",
        "index": "The zero inflation index.",
        "base_cpi": "The base CPI value.",
        "observation_lag": "The observation lag period.",
        "payment_day_counter": "The day counter for payments (default: None).",
        "payment_convention": "The business day convention for payments (default: Following).",
        "fixed_rates": "The fixed rates (default: None).",
        "caps": "The cap rates (default: None).",
        "floors": "The floor rates (default: None).",
        "ex_coupon_period": "The ex-coupon period (default: None).",
        "ex_coupon_calendar": "The ex-coupon calendar (default: None).",
        "ex_coupon_convention": "The ex-coupon business day convention (default: Unadjusted).",
        "ex_coupon_end_of_month": "Whether ex-coupon end of month (default: False).",
        "payment_calendar": "The payment calendar (default: None).",
        "growth_only": "Whether to use growth only (default: True).",
        "observation_interpolation": "The observation interpolation type (ASINDEX, FLAT, LINEAR; default: ASINDEX).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPILeg(
    nominals: xlo.Array(dims=1),
    schedule: ql.Schedule,
    index: ql.ZeroInflationIndex,
    base_cpi: float,
    observation_lag: qPeriod,
    payment_day_counter=None,
    payment_convention: qBusinessDayConvention = ql.Following,
    fixed_rates: xlo.Array(dims=1) = [ql.nullDouble()],
    caps: xlo.Array(dims=1) = None,
    floors: xlo.Array(dims=1) = None,
    ex_coupon_period=None,
    ex_coupon_calendar=None,
    ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted,
    ex_coupon_end_of_month: bool = False,
    payment_calendar=None,
    growth_only: bool = True,
    observation_interpolation: qCPIInterpolationType = ql.CPI.AsIndex,
    trigger=None,
):
    nominals = to_float_list(nominals)
    base_cpi = float(base_cpi)
    observation_lag = qPeriod.__wrapped__(observation_lag)

    if payment_day_counter is not None:
        payment_day_counter = qDayCounter.__wrapped__(payment_day_counter)
    fixed_rates = to_float_list(fixed_rates)
    caps = to_float_list(caps)
    floors = to_float_list(floors)
    if ex_coupon_period is not None:
        ex_coupon_period = qPeriod.__wrapped__(ex_coupon_period)
    if ex_coupon_calendar is not None:
        ex_coupon_calendar = qCalendar.__wrapped__(ex_coupon_calendar)
    if payment_calendar is not None:
        payment_calendar = qCalendar.__wrapped__(payment_calendar)

    _CPILEG_KWARGS = {
        "payment_day_counter": "paymentDayCounter",
        "payment_convention": "paymentConvention",
        "fixed_rates": "fixedRates",
        "caps": "caps",
        "floors": "floors",
        "ex_coupon_period": "exCouponPeriod",
        "ex_coupon_calendar": "exCouponCalendar",
        "ex_coupon_convention": "exCouponConvention",
        "ex_coupon_end_of_month": "exCouponEndOfMonth",
        "payment_calendar": "paymentCalendar",
        "growth_only": "growthOnly",
        "observation_interpolation": "observationInterpolation",
    }

    kwargs = {}
    for param_name, kw_name in _CPILEG_KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.CPILeg(nominals, schedule, index, base_cpi, observation_lag, **kwargs)


## Zero Inflation Cash Flow


@xlo.func(
    help="Create a QuantLib ZeroInflationCashFlow object.",
    args={
        "notional": "The notional amount.",
        "index": "The zero inflation index.",
        "observation_interpolation": "The observation interpolation type (ASINDEX, FLAT, LINEAR).",
        "start_date": "The start date.",
        "end_date": "The end date.",
        "observation_lag": "The observation lag.",
        "payment_date": "The payment date.",
        "growth_only": "Whether to pay growth only.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCashFlow(
    notional: float,
    index: ql.ZeroInflationIndex,
    observation_interpolation: qCPIInterpolationType,
    start_date: qDate,
    end_date: qDate,
    observation_lag: qPeriod,
    payment_date: qDate,
    growth_only: bool = False,
    trigger=None,
) -> ql.ZeroInflationCashFlow:
    return ql.ZeroInflationCashFlow(
        notional,
        index,
        observation_interpolation,
        start_date,
        end_date,
        observation_lag,
        payment_date,
        growth_only,
    )


@xlo.func(
    help="Get the notional of a zero inflation cash flow.",
    args={
        "zero_inflation_cash_flow": "The zero inflation cash flow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCashFlowNotional(
    zero_inflation_cash_flow: ql.ZeroInflationCashFlow, trigger=None
) -> float:
    return zero_inflation_cash_flow.notional()


@xlo.func(
    help="Get the base date of a zero inflation cash flow.",
    args={
        "zero_inflation_cash_flow": "The zero inflation cash flow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCashFlowBaseDate(
    zero_inflation_cash_flow: ql.ZeroInflationCashFlow, trigger=None
) -> ql.Date:
    return zero_inflation_cash_flow.baseDate()


@xlo.func(
    help="Get the fixing date of a zero inflation cash flow.",
    args={
        "zero_inflation_cash_flow": "The zero inflation cash flow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCashFlowFixingDate(
    zero_inflation_cash_flow: ql.ZeroInflationCashFlow, trigger=None
) -> ql.Date:
    return zero_inflation_cash_flow.fixingDate()


@xlo.func(
    help="Check if a zero inflation cash flow is growth only.",
    args={
        "zero_inflation_cash_flow": "The zero inflation cash flow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCashFlowGrowthOnly(
    zero_inflation_cash_flow: ql.ZeroInflationCashFlow, trigger=None
) -> bool:
    return zero_inflation_cash_flow.growthOnly()


@xlo.func(
    help="Get the observation interpolation of a zero inflation cash flow.",
    args={
        "zero_inflation_cash_flow": "The zero inflation cash flow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCashFlowObservationInterpolation(
    zero_inflation_cash_flow: ql.ZeroInflationCashFlow, trigger=None
):
    return first_key(
        QL_CPI_INTERPOLATION_TYPE, zero_inflation_cash_flow.observationInterpolation()
    )


@xlo.func(
    help="Get the zero inflation index of a zero inflation cash flow.",
    args={
        "zero_inflation_cash_flow": "The zero inflation cash flow.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCashFlowZeroInflationIndex(
    zero_inflation_cash_flow: ql.ZeroInflationCashFlow, trigger=None
) -> ql.ZeroInflationIndex:
    return zero_inflation_cash_flow.zeroInflationIndex()


## Bootstrap Helpers


@xlo.func(
    help="Get the quote from a bootstrap helper.",
    args={
        "bootstrap_helper": "The bootstrap helper.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBootstrapHelperQuote(bootstrap_helper, trigger=None) -> ql.QuoteHandle:
    return bootstrap_helper.quote()


@xlo.func(
    help="Get the latest date from a bootstrap helper.",
    args={
        "bootstrap_helper": "The bootstrap helper.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBootstrapHelperLatestDate(bootstrap_helper, trigger=None) -> ql.Date:
    return bootstrap_helper.latestDate()


@xlo.func(
    help="Get the earliest date from a bootstrap helper.",
    args={
        "bootstrap_helper": "The bootstrap helper.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBootstrapHelperEarliestDate(bootstrap_helper, trigger=None) -> ql.Date:
    return bootstrap_helper.earliestDate()


@xlo.func(
    help="Get the maturity date from a bootstrap helper.",
    args={
        "bootstrap_helper": "The bootstrap helper.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBootstrapHelperMaturityDate(bootstrap_helper, trigger=None) -> ql.Date:
    return bootstrap_helper.maturityDate()


@xlo.func(
    help="Get the latest relevant date from a bootstrap helper.",
    args={
        "bootstrap_helper": "The bootstrap helper.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBootstrapHelperLatestRelevantDate(bootstrap_helper, trigger=None) -> ql.Date:
    return bootstrap_helper.latestRelevantDate()


@xlo.func(
    help="Get the pillar date from a bootstrap helper.",
    args={
        "bootstrap_helper": "The bootstrap helper.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBootstrapHelperPillarDate(bootstrap_helper, trigger=None) -> ql.Date:
    return bootstrap_helper.pillarDate()


@xlo.func(
    help="Get the implied quote from a bootstrap helper.",
    args={
        "bootstrap_helper": "The bootstrap helper.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBootstrapHelperImpliedQuote(bootstrap_helper, trigger=None) -> float:
    return bootstrap_helper.impliedQuote()


@xlo.func(
    help="Get the quote error from a bootstrap helper.",
    args={
        "bootstrap_helper": "The bootstrap helper.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBootstrapHelperQuoteError(bootstrap_helper, trigger=None):
    return bootstrap_helper.quoteError()


## Zero Coupon Inflation Swap Helper


@xlo.func(
    help="Create a ZeroCouponInflationSwapHelper.",
    args={
        "quote": "The quote handle.",
        "lag": "The lag period.",
        "maturity": "The maturity date.",
        "calendar": "The calendar.",
        "bdc": "The business day convention.",
        "day_counter": "The day counter.",
        "index": "The zero inflation index.",
        "observation_interpolation": "The observation interpolation type.",
        "nominal_its": "The nominal yield term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponInflationSwapHelper(
    quote: qQuoteHandle,
    lag: qPeriod,
    maturity: qDate,
    calendar: qCalendar,
    bdc: qBusinessDayConvention,
    day_counter: qDayCounter,
    index: ql.ZeroInflationIndex,
    observation_interpolation: qCPIInterpolationType,
    nominal_its: ql.YieldTermStructureHandle = None,
    trigger=None,
) -> ql.ZeroCouponInflationSwapHelper:
    return ql.ZeroCouponInflationSwapHelper(
        quote,
        lag,
        maturity,
        calendar,
        bdc,
        day_counter,
        index,
        observation_interpolation,
        nominal_its,
    )


@xlo.func(
    help="Get the swap from a ZeroCouponInflationSwapHelper.",
    args={
        "helper": "The ZeroCouponInflationSwapHelper.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponInflationSwapHelperSwap(
    helper: ql.ZeroCouponInflationSwapHelper, trigger=None
) -> ql.ZeroCouponInflationSwap:
    return helper.swap()


## Year On Year Inflation Swap Helper


@xlo.func(
    help="Create a YearOnYearInflationSwapHelper.",
    args={
        "quote": "The quote handle.",
        "lag": "The lag period.",
        "maturity": "The maturity date.",
        "calendar": "The calendar.",
        "bdc": "The business day convention.",
        "day_counter": "The day counter.",
        "index": "The YoY inflation index.",
        "interpolation": "The interpolation type.",
        "nominal_term_structure": "The nominal term structure handle.",
        "pillar": "The pillar choice.",
        "custom_pillar_date": "The custom pillar date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYearOnYearInflationSwapHelper(
    quote: qQuoteHandle,
    lag: qPeriod,
    maturity: qDate,
    calendar: qCalendar,
    bdc: qBusinessDayConvention,
    day_counter: qDayCounter,
    index: ql.YoYInflationIndex,
    interpolation: qCPIInterpolationType,
    nominal_term_structure: ql.YieldTermStructureHandle,
    pillar: qPillarChoice = ql.Pillar.LastRelevantDate,
    custom_pillar_date: qDate = ql.Date(),
    trigger=None,
) -> ql.YearOnYearInflationSwapHelper:
    return ql.YearOnYearInflationSwapHelper(
        quote,
        lag,
        maturity,
        calendar,
        bdc,
        day_counter,
        index,
        interpolation,
        nominal_term_structure,
        pillar,
        custom_pillar_date,
    )


@xlo.func(
    help="Get the swap from a YearOnYearInflationSwapHelper.",
    args={
        "helper": "The YearOnYearInflationSwapHelper.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYearOnYearInflationSwapHelperSwap(
    helper: ql.YearOnYearInflationSwapHelper, trigger=None
) -> ql.YearOnYearInflationSwap:
    return helper.swap()


## Piecewise Inflation Curves


# uses Linear interpolator internally
@xlo.func(
    help="Create a PiecewiseZeroInflation curve.",
    args={
        "reference_date": "The reference date.",
        "base_date": "The base date.",
        "frequency": "The frequency.",
        "day_counter": "The day counter.",
        "instruments": "The list of bootstrap instruments.",
        "seasonality": "The seasonality object (optional).",
        "accuracy": "The accuracy for curve construction.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseZeroInflation(
    reference_date: qDate,
    base_date: qDate,
    frequency: qFrequency,
    day_counter: qDayCounter,
    instruments: xlo.Array(dims=1),
    seasonality: ql.Seasonality = None,
    accuracy: float = 1.0e-12,
    trigger=None,
) -> ql.ZeroInflationTermStructureHandle:
    _instruments = to_object_list(instruments, ql.ZeroCouponInflationSwapHelper)
    return ql.ZeroInflationTermStructureHandle(
        ql.PiecewiseZeroInflation(
            reference_date,
            base_date,
            frequency,
            day_counter,
            _instruments,
            seasonality,
            accuracy,
        )
    )


# To access class methods, we add constructors for YieldTermStructures '*AsIts'.
# We want to also allow conversion into a Handle to use the curve as input to
# other functions.
@xlo.func(
    help="Create a PiecewiseZeroInflation curve.",
    args={
        "reference_date": "The reference date.",
        "base_date": "The base date.",
        "frequency": "The frequency.",
        "day_counter": "The day counter.",
        "instruments": "The list of bootstrap instruments.",
        "seasonality": "The seasonality object (optional).",
        "accuracy": "The accuracy for curve construction.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseZeroInflationAsIts(
    reference_date: qDate,
    base_date: qDate,
    frequency: qFrequency,
    day_counter: qDayCounter,
    instruments: xlo.Array(dims=1),
    seasonality: ql.Seasonality = None,
    accuracy: float = 1.0e-12,
    trigger=None,
) -> ql.PiecewiseZeroInflation:
    _instruments = to_object_list(instruments, ql.ZeroCouponInflationSwapHelper)
    return ql.PiecewiseZeroInflation(
        reference_date,
        base_date,
        frequency,
        day_counter,
        _instruments,
        seasonality,
        accuracy,
    )


@xlo.func(
    help="Get the dates from a piecewise inflation curve.",
    args={
        "curve": "The piecewise inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseZeroInflationCurveDates(curve, trigger=None) -> list:
    return curve.dates()


@xlo.func(
    help="Get the times from a piecewise inflation curve.",
    args={
        "curve": "The piecewise inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseZeroInflationCurveTimes(curve, trigger=None) -> list[float]:
    return curve.times()


@xlo.func(
    help="Get the data from a piecewise inflation curve.",
    args={
        "curve": "The piecewise inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseZeroInflationCurveData(
    curve: ql.ZeroInflationTermStructure, trigger=None
) -> list[float]:
    return curve.data()


@xlo.func(
    help="Get the nodes (dates and rates) from an piecewise zero inflation curve.",
    args={
        "curve": "The piecewise zero inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseZeroInflationCurveNodes(curve, trigger=None) -> list:
    return curve.nodes()


# uses Linear interpolator internally
@xlo.func(
    help="Create a PiecewiseYoYInflation curve.",
    args={
        "reference_date": "The reference date.",
        "base_date": "The base date.",
        "base_yoy_rate": "The base YoY rate.",
        "frequency": "The frequency.",
        "day_counter": "The day counter.",
        "instruments": "The list of bootstrap instruments.",
        "seasonality": "The seasonality object (optional).",
        "accuracy": "The accuracy for curve construction.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYoYInflation(
    reference_date: qDate,
    base_date: qDate,
    base_yoy_rate: float,
    frequency: qFrequency,
    day_counter: qDayCounter,
    instruments: xlo.Array(dims=1),
    seasonality: ql.Seasonality = None,
    accuracy: float = 1.0e-12,
    trigger=None,
) -> ql.YoYInflationTermStructureHandle:
    _instruments = to_object_list(instruments, ql.YoYHelper)
    return ql.YoYInflationTermStructureHandle(
        ql.PiecewiseYoYInflation(
            reference_date,
            base_date,
            base_yoy_rate,
            frequency,
            day_counter,
            _instruments,
            seasonality,
            accuracy,
        )
    )


# To access class methods, we add constructors for YieldTermStructures '*AsIts'.
# We want to also allow conversion into a Handle to use the curve as input to
# other functions.
# uses Linear interpolator internally
@xlo.func(
    help="Create a PiecewiseYoYInflation curve.",
    args={
        "reference_date": "The reference date.",
        "base_date": "The base date.",
        "base_yoy_rate": "The base YoY rate.",
        "frequency": "The frequency.",
        "day_counter": "The day counter.",
        "instruments": "The list of bootstrap instruments.",
        "seasonality": "The seasonality object (optional).",
        "accuracy": "The accuracy for curve construction.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYoYInflationAsIts(
    reference_date: qDate,
    base_date: qDate,
    base_yoy_rate: float,
    frequency: qFrequency,
    day_counter: qDayCounter,
    instruments: xlo.Array(dims=1),
    seasonality: ql.Seasonality = None,
    accuracy: float = 1.0e-12,
    trigger=None,
) -> ql.PiecewiseYoYInflation:
    _instruments = to_object_list(instruments, ql.YoYHelper)
    return ql.PiecewiseYoYInflation(
        reference_date,
        base_date,
        base_yoy_rate,
        frequency,
        day_counter,
        _instruments,
        seasonality,
        accuracy,
    )


@xlo.func(
    help="Get the dates from a piecewise inflation curve.",
    args={
        "curve": "The piecewise inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYoYInflationCurveDates(curve, trigger=None) -> tuple:
    return curve.dates()


@xlo.func(
    help="Get the times from a piecewise inflation curve.",
    args={
        "curve": "The piecewise inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYoYInflationCurveTimes(curve, trigger=None) -> tuple:
    return curve.times()


@xlo.func(
    help="Get the data from a piecewise inflation curve.",
    args={
        "curve": "The piecewise inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYoYInflationCurveData(curve, trigger=None) -> tuple:
    return curve.data()


@xlo.func(
    help="Get the nodes (dates and rates) from an piecewise YoY inflation curve.",
    args={
        "curve": "The piecewise yoy inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPiecewiseYoYInflationCurveNodes(curve, trigger=None) -> tuple:
    return curve.nodes()


## Inflation Utilities


@xlo.func(
    help="Calculate the inflation period for a date and frequency.",
    args={
        "date": "The date.",
        "frequency": "The frequency.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationPeriod(
    date: qDate, frequency: qFrequency, trigger=None
) -> tuple[ql.Date, ql.Date]:
    return ql.inflationPeriod(date, frequency)


@xlo.func(
    help="Calculate the inflation year fraction.",
    args={
        "frequency": "The frequency.",
        "index_is_interpolated": "Whether the index is interpolated.",
        "day_count": "The day counter.",
        "date1": "The first date.",
        "date2": "The second date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationYearFraction(
    frequency: qFrequency,
    index_is_interpolated: bool,
    day_count: qDayCounter,
    date1: qDate,
    date2: qDate,
    trigger=None,
) -> float:
    return ql.inflationYearFraction(
        frequency, index_is_interpolated, day_count, date1, date2
    )


@xlo.func(
    help="Calculate the inflation base date.",
    args={
        "reference_date": "The reference date.",
        "observation_lag": "The observation lag.",
        "frequency": "The frequency.",
        "index_is_interpolated": "Whether the index is interpolated.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInflationBaseDate(
    reference_date: qDate,
    observation_lag: qPeriod,
    frequency: qFrequency,
    index_is_interpolated: bool,
    trigger=None,
) -> ql.Date:
    return ql.inflationBaseDate(
        reference_date, observation_lag, frequency, index_is_interpolated
    )


## YoY Inflation Coupon


@xlo.func(
    help="Set the pricer for a YoY inflation coupon or leg.",
    args={
        "coupon_or_leg": "The YoY inflation coupon or leg to set the pricer for.",
        "pricer": "The YoY inflation coupon pricer.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCouponSetPricer(
    coupon_or_leg,
    pricer: ql.YoYInflationCouponPricer,
    trigger=None,
) -> bool:
    if isinstance(coupon_or_leg, ql.YoYInflationCoupon):
        ql.setCouponPricer(to_object_list([coupon_or_leg], ql.CashFlow), pricer)
    elif isinstance(coupon_or_leg, ql.Leg):
        coupon_or_leg.setCouponPricer(pricer)
    else:
        raise TypeError("Expected YoYInflationCoupon or Leg")
    return True


@xlo.func(
    help="Create a QuantLib YoYInflationCoupon object.",
    args={
        "payment_date": "The payment date.",
        "nominal": "The nominal amount.",
        "start_date": "The start date.",
        "end_date": "The end date.",
        "fixing_days": "The number of fixing days.",
        "index": "The YoY inflation index.",
        "observation_lag": "The observation lag.",
        "interpolation": "The interpolation type (ASINDEX, FLAT, LINEAR).",
        "day_counter": "The day counter.",
        "gearing": "The gearing.",
        "spread": "The spread.",
        "ref_period_start": "The reference period start date.",
        "ref_period_end": "The reference period end date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCoupon(
    payment_date: qDate,
    nominal: float,
    start_date: qDate,
    end_date: qDate,
    fixing_days: int,
    index: ql.YoYInflationIndex,
    observation_lag: qPeriod,
    interpolation: qCPIInterpolationType,
    day_counter: qDayCounter,
    gearing: float = 1.0,
    spread: float = 0.0,
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    trigger=None,
) -> ql.YoYInflationCoupon:
    return ql.YoYInflationCoupon(
        payment_date,
        nominal,
        start_date,
        end_date,
        fixing_days,
        index,
        observation_lag,
        interpolation,
        day_counter,
        gearing,
        spread,
        ref_period_start,
        ref_period_end,
    )


@xlo.func(
    help="Get the gearing of a YoY inflation coupon.",
    args={
        "yoy_inflation_coupon": "The YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCouponGearing(
    yoy_inflation_coupon: ql.YoYInflationCoupon, trigger=None
) -> float:
    return yoy_inflation_coupon.gearing()


@xlo.func(
    help="Get the spread of a YoY inflation coupon.",
    args={
        "yoy_inflation_coupon": "The YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCouponSpread(
    yoy_inflation_coupon: ql.YoYInflationCoupon, trigger=None
) -> float:
    return yoy_inflation_coupon.spread()


@xlo.func(
    help="Get the adjusted fixing of a YoY inflation coupon.",
    args={
        "yoy_inflation_coupon": "The YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCouponAdjustedFixing(
    yoy_inflation_coupon: ql.YoYInflationCoupon, trigger=None
) -> float:
    return yoy_inflation_coupon.adjustedFixing()


@xlo.func(
    help="Get the YoY inflation index of a YoY inflation coupon.",
    args={
        "yoy_inflation_coupon": "The YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCouponYoYIndex(
    yoy_inflation_coupon: ql.YoYInflationCoupon, trigger=None
) -> ql.YoYInflationIndex:
    return yoy_inflation_coupon.yoyIndex()


@xlo.func(
    help="Get the interpolation of a YoY inflation coupon.",
    args={
        "yoy_inflation_coupon": "The YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCouponInterpolation(
    yoy_inflation_coupon: ql.YoYInflationCoupon, trigger=None
):
    return first_key(QL_CPI_INTERPOLATION_TYPE, yoy_inflation_coupon.interpolation())


## Capped Floored YoY Inflation Coupon


@xlo.func(
    help="Create a QuantLib CappedFlooredYoYInflationCoupon object.",
    args={
        "payment_date": "The payment date.",
        "nominal": "The nominal amount.",
        "start_date": "The start date.",
        "end_date": "The end date.",
        "fixing_days": "The number of fixing days.",
        "index": "The YoY inflation index.",
        "observation_lag": "The observation lag.",
        "interpolation": "The interpolation type (ASINDEX, FLAT, LINEAR).",
        "day_counter": "The day counter.",
        "gearing": "The gearing.",
        "spread": "The spread.",
        "cap": "The cap rate.",
        "floor": "The floor rate.",
        "ref_period_start": "The reference period start date.",
        "ref_period_end": "The reference period end date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredYoYInflationCoupon(
    payment_date: qDate,
    nominal: float,
    start_date: qDate,
    end_date: qDate,
    fixing_days: int,
    index: ql.YoYInflationIndex,
    observation_lag: qPeriod,
    interpolation: qCPIInterpolationType,
    day_counter: qDayCounter,
    gearing: float = 1.0,
    spread: float = 0.0,
    cap: float = ql.nullDouble(),
    floor: float = ql.nullDouble(),
    ref_period_start: qDate = ql.Date(),
    ref_period_end: qDate = ql.Date(),
    trigger=None,
) -> ql.CappedFlooredYoYInflationCoupon:
    return ql.CappedFlooredYoYInflationCoupon(
        payment_date,
        nominal,
        start_date,
        end_date,
        fixing_days,
        index,
        observation_lag,
        interpolation,
        day_counter,
        gearing,
        spread,
        cap,
        floor,
        ref_period_start,
        ref_period_end,
    )


@xlo.func(
    help="Get the rate of a capped floored YoY inflation coupon.",
    args={
        "coupon": "The capped floored YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredYoYInflationCouponRate(
    coupon: ql.CappedFlooredYoYInflationCoupon, trigger=None
) -> float:
    return coupon.rate()


@xlo.func(
    help="Get the cap of a capped floored YoY inflation coupon.",
    args={
        "coupon": "The capped floored YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredYoYInflationCouponCap(
    coupon: ql.CappedFlooredYoYInflationCoupon, trigger=None
) -> float:
    return coupon.cap()


@xlo.func(
    help="Get the floor of a capped floored YoY inflation coupon.",
    args={
        "coupon": "The capped floored YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredYoYInflationCouponFloor(
    coupon: ql.CappedFlooredYoYInflationCoupon, trigger=None
) -> float:
    return coupon.floor()


@xlo.func(
    help="Get the effective cap of a capped floored YoY inflation coupon.",
    args={
        "coupon": "The capped floored YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredYoYInflationCouponEffectiveCap(
    coupon: ql.CappedFlooredYoYInflationCoupon, trigger=None
) -> float:
    return coupon.effectiveCap()


@xlo.func(
    help="Get the effective floor of a capped floored YoY inflation coupon.",
    args={
        "coupon": "The capped floored YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredYoYInflationCouponEffectiveFloor(
    coupon: ql.CappedFlooredYoYInflationCoupon, trigger=None
) -> float:
    return coupon.effectiveFloor()


@xlo.func(
    help="Get the underlying rate of a capped floored YoY inflation coupon.",
    args={
        "coupon": "The capped floored YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredYoYInflationCouponUnderlyingRate(
    coupon: ql.CappedFlooredYoYInflationCoupon, trigger=None
) -> float:
    return coupon.underlyingRate()


@xlo.func(
    help="Check if a capped floored YoY inflation coupon is capped.",
    args={
        "coupon": "The capped floored YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredYoYInflationCouponIsCapped(
    coupon: ql.CappedFlooredYoYInflationCoupon, trigger=None
) -> bool:
    return coupon.isCapped()


@xlo.func(
    help="Check if a capped floored YoY inflation coupon is floored.",
    args={
        "coupon": "The capped floored YoY inflation coupon.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCappedFlooredYoYInflationCouponIsFloored(
    coupon: ql.CappedFlooredYoYInflationCoupon, trigger=None
) -> bool:
    return coupon.isFloored()


## YoY Inflation Leg


@xlo.func(
    help="Create a YoY inflation leg.",
    args={
        "schedule": "The schedule.",
        "calendar": "The calendar.",
        "index": "The YoY inflation index.",
        "observation_lag": "The observation lag.",
        "interpolation": "The interpolation type (ASINDEX, FLAT, LINEAR).",
        "notionals": "The notionals as a list.",
        "payment_day_counter": "The payment day counter.",
        "payment_convention": "The payment business day convention.",
        "fixing_days": "The number of fixing days.",
        "gearings": "The gearings as a list.",
        "spreads": "The spreads as a list.",
        "caps": "The caps as a list.",
        "floors": "The floors as a list.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationLeg(
    schedule: ql.Schedule,
    calendar: qCalendar,
    index: ql.YoYInflationIndex,
    observation_lag: qPeriod,
    interpolation: qCPIInterpolationType,
    notionals: xlo.Array(dims=1),
    payment_day_counter: qDayCounter,
    payment_convention: qBusinessDayConvention = ql.Following,
    fixing_days: int = 0,
    gearings: xlo.Array(dims=1) = None,
    spreads: xlo.Array(dims=1) = None,
    caps: xlo.Array(dims=1) = None,
    floors: xlo.Array(dims=1) = None,
    trigger=None,
) -> ql.Leg:
    _notionals = to_float_list(notionals)
    _gearings = to_float_list(gearings)
    _spreads = to_float_list(spreads)
    _caps = to_float_list(caps)
    _floors = to_float_list(floors)

    return ql.yoyInflationLeg(
        schedule,
        calendar,
        index,
        observation_lag,
        interpolation,
        _notionals,
        payment_day_counter,
        payment_convention,
        fixing_days,
        _gearings,
        _spreads,
        _caps,
        _floors,
    )


## YoY Inflation Coupon Pricers


@xlo.func(
    help="Create a QuantLib BlackYoYInflationCouponPricer object.",
    args={
        "caplet_vol": "The YoY optionlet volatility surface handle.",
        "nominal_term_structure": "The nominal term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackYoYInflationCouponPricer(
    caplet_vol: ql.YoYOptionletVolatilitySurfaceHandle,
    nominal_term_structure: ql.YieldTermStructureHandle,
    trigger=None,
) -> ql.BlackYoYInflationCouponPricer:
    return ql.BlackYoYInflationCouponPricer(caplet_vol, nominal_term_structure)


@xlo.func(
    help="Create a QuantLib UnitDisplacedBlackYoYInflationCouponPricer object.",
    args={
        "caplet_vol": "The YoY optionlet volatility surface handle.",
        "nominal_term_structure": "The nominal term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlUnitDisplacedBlackYoYInflationCouponPricer(
    caplet_vol: ql.YoYOptionletVolatilitySurfaceHandle,
    nominal_term_structure: ql.YieldTermStructureHandle,
    trigger=None,
) -> ql.UnitDisplacedBlackYoYInflationCouponPricer:
    return ql.UnitDisplacedBlackYoYInflationCouponPricer(
        caplet_vol, nominal_term_structure
    )


@xlo.func(
    help="Create a QuantLib BachelierYoYInflationCouponPricer object.",
    args={
        "caplet_vol": "The YoY optionlet volatility surface handle.",
        "nominal_term_structure": "The nominal term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierYoYInflationCouponPricer(
    caplet_vol: ql.YoYOptionletVolatilitySurfaceHandle,
    nominal_term_structure: ql.YieldTermStructureHandle,
    trigger=None,
) -> ql.BachelierYoYInflationCouponPricer:
    return ql.BachelierYoYInflationCouponPricer(caplet_vol, nominal_term_structure)


## Zero Coupon Inflation Swap


@xlo.func(
    help="Create a QuantLib ZeroCouponInflationSwap object.",
    args={
        "swap_type": "The swap type (PAYER or RECEIVER).",
        "nominal": "The nominal amount.",
        "start": "The start date.",
        "maturity": "The maturity date.",
        "calendar": "The calendar.",
        "convention": "The business day convention.",
        "day_counter": "The day counter.",
        "fixed_rate": "The fixed rate.",
        "index": "The zero inflation index.",
        "lag": "The observation lag.",
        "observation_interpolation": "The observation interpolation type (ASINDEX, FLAT, LINEAR).",
        "adjust_inf_obs_dates": "Whether to adjust inflation observation dates.",
        "inf_calendar": "The inflation calendar.",
        "inf_convention": "The inflation business day convention.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponInflationSwap(
    swap_type: qSwapType,
    nominal: float,
    start: qDate,
    maturity: qDate,
    calendar: qCalendar,
    convention: qBusinessDayConvention,
    day_counter: qDayCounter,
    fixed_rate: float,
    index: ql.ZeroInflationIndex,
    lag: qPeriod,
    observation_interpolation: qCPIInterpolationType,
    adjust_inf_obs_dates: bool = False,
    inf_calendar=None,
    inf_convention=None,
    trigger=None,
) -> ql.ZeroCouponInflationSwap:
    if inf_calendar is not None:
        inf_calendar = qCalendar.__wrapped__(inf_calendar)
    if inf_convention is not None:
        inf_convention = qBusinessDayConvention.__wrapped__(inf_convention)

    _SWAP_KWARGS = {
        "inf_calendar": "infCalendar",
        "inf_convention": "infConvention",
    }
    kwargs = {}
    for param_name, kw_name in _SWAP_KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value
    return ql.ZeroCouponInflationSwap(
        swap_type,
        nominal,
        start,
        maturity,
        calendar,
        convention,
        day_counter,
        fixed_rate,
        index,
        lag,
        observation_interpolation,
        adjust_inf_obs_dates,
        **kwargs,
    )


@xlo.func(
    help="Get the fair rate of a zero coupon inflation swap.",
    args={
        "swap": "The zero coupon inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponInflationSwapFairRate(
    swap: ql.ZeroCouponInflationSwap, trigger=None
) -> float:
    return swap.fairRate()


@xlo.func(
    help="Get the fixed leg NPV of a zero coupon inflation swap.",
    args={
        "swap": "The zero coupon inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponInflationSwapFixedLegNPV(
    swap: ql.ZeroCouponInflationSwap, trigger=None
) -> float:
    return swap.fixedLegNPV()


@xlo.func(
    help="Get the fixed leg BPS of a zero coupon inflation swap.",
    args={
        "swap": "The zero coupon inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponInflationSwapFixedLegBPS(
    swap: ql.ZeroCouponInflationSwap, trigger=None
) -> float:
    return swap.fixedLegBPS()


@xlo.func(
    help="Get the inflation leg NPV of a zero coupon inflation swap.",
    args={
        "swap": "The zero coupon inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponInflationSwapInflationLegNPV(
    swap: ql.ZeroCouponInflationSwap, trigger=None
) -> float:
    return swap.inflationLegNPV()


@xlo.func(
    help="Get the fixed leg of a zero coupon inflation swap.",
    args={
        "swap": "The zero coupon inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponInflationSwapFixedLeg(
    swap: ql.ZeroCouponInflationSwap, trigger=None
) -> ql.Leg:
    return swap.fixedLeg()


@xlo.func(
    help="Get the inflation leg of a zero coupon inflation swap.",
    args={
        "swap": "The zero coupon inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponInflationSwapInflationLeg(
    swap: ql.ZeroCouponInflationSwap, trigger=None
) -> ql.Leg:
    return swap.inflationLeg()


@xlo.func(
    help="Get the type of a zero coupon inflation swap.",
    args={
        "swap": "The zero coupon inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroCouponInflationSwapType(
    swap: ql.ZeroCouponInflationSwap, trigger=None
) -> str:
    return first_key(QL_SWAP_TYPE, swap.type())


## Year On Year Inflation Swap


@xlo.func(
    help="Create a QuantLib YearOnYearInflationSwap object.",
    args={
        "swap_type": "The swap type (PAYER or RECEIVER).",
        "nominal": "The nominal amount.",
        "fixed_schedule": "The fixed leg schedule.",
        "fixed_rate": "The fixed rate.",
        "fixed_day_counter": "The fixed leg day counter.",
        "yoy_schedule": "The YoY leg schedule.",
        "index": "The YoY inflation index.",
        "lag": "The observation lag.",
        "interpolation": "The interpolation type (ASINDEX, FLAT, LINEAR).",
        "spread": "The spread.",
        "yoy_day_counter": "The YoY leg day counter.",
        "payment_calendar": "The payment calendar.",
        "payment_convention": "The payment business day convention.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYearOnYearInflationSwap(
    swap_type: qSwapType,
    nominal: float,
    fixed_schedule: ql.Schedule,
    fixed_rate: float,
    fixed_day_counter: qDayCounter,
    yoy_schedule: ql.Schedule,
    index: ql.YoYInflationIndex,
    lag: qPeriod,
    interpolation: qCPIInterpolationType,
    spread: float,
    yoy_day_counter: qDayCounter,
    payment_calendar: qCalendar,
    payment_convention: qBusinessDayConvention = ql.Following,
    trigger=None,
) -> ql.YearOnYearInflationSwap:
    return ql.YearOnYearInflationSwap(
        swap_type,
        nominal,
        fixed_schedule,
        fixed_rate,
        fixed_day_counter,
        yoy_schedule,
        index,
        lag,
        interpolation,
        spread,
        yoy_day_counter,
        payment_calendar,
        payment_convention,
    )


@xlo.func(
    help="Get the fair rate of a year-on-year inflation swap.",
    args={
        "swap": "The year-on-year inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYearOnYearInflationSwapFairRate(
    swap: ql.YearOnYearInflationSwap, trigger=None
) -> float:
    return swap.fairRate()


@xlo.func(
    help="Get the fixed leg NPV of a year-on-year inflation swap.",
    args={
        "swap": "The year-on-year inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYearOnYearInflationSwapFixedLegNPV(
    swap: ql.YearOnYearInflationSwap, trigger=None
) -> float:
    return swap.fixedLegNPV()


@xlo.func(
    help="Get the YoY leg NPV of a year-on-year inflation swap.",
    args={
        "swap": "The year-on-year inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYearOnYearInflationSwapYoYLegNPV(
    swap: ql.YearOnYearInflationSwap, trigger=None
) -> float:
    return swap.yoyLegNPV()


@xlo.func(
    help="Get the fair spread of a year-on-year inflation swap.",
    args={
        "swap": "The year-on-year inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYearOnYearInflationSwapFairSpread(
    swap: ql.YearOnYearInflationSwap, trigger=None
) -> float:
    return swap.fairSpread()


@xlo.func(
    help="Get the fixed leg of a year-on-year inflation swap.",
    args={
        "swap": "The year-on-year inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYearOnYearInflationSwapFixedLeg(
    swap: ql.YearOnYearInflationSwap, trigger=None
) -> ql.Leg:
    return swap.fixedLeg()


@xlo.func(
    help="Get the YoY leg of a year-on-year inflation swap.",
    args={
        "swap": "The year-on-year inflation swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYearOnYearInflationSwapYoYLeg(
    swap: ql.YearOnYearInflationSwap, trigger=None
) -> ql.Leg:
    return swap.yoyLeg()


## CPI Swap


@xlo.func(
    help="Create a QuantLib CPISwap object.",
    args={
        "swap_type": "The swap type (PAYER or RECEIVER).",
        "nominal": "The nominal amount.",
        "subtract_inflation_nominal": "Whether to subtract inflation nominal.",
        "spread": "The spread.",
        "float_day_count": "The float leg day counter.",
        "float_schedule": "The float leg schedule.",
        "float_roll": "The float leg roll convention.",
        "fixing_days": "The number of fixing days.",
        "float_index": "The float rate index.",
        "fixed_rate": "The fixed rate.",
        "base_cpi": "The base CPI value.",
        "fixed_day_count": "The fixed leg day counter.",
        "fixed_schedule": "The fixed leg schedule.",
        "fixed_roll": "The fixed leg roll convention.",
        "observation_lag": "The observation lag.",
        "fixed_index": "The fixed inflation index.",
        "observation_interpolation": "The observation interpolation type (ASINDEX, FLAT, LINEAR).",
        "inflation_nominal": "The inflation nominal.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPISwap(
    swap_type: qSwapType,
    nominal: float,
    subtract_inflation_nominal: bool,
    spread: float,
    float_day_count: qDayCounter,
    float_schedule: ql.Schedule,
    float_roll: qBusinessDayConvention,
    fixing_days: int,
    float_index: ql.IborIndex,
    fixed_rate: float,
    base_cpi: float,
    fixed_day_count: qDayCounter,
    fixed_schedule: ql.Schedule,
    fixed_roll: qBusinessDayConvention,
    observation_lag: qPeriod,
    fixed_index: ql.ZeroInflationIndex,
    observation_interpolation: qCPIInterpolationType = ql.CPI.AsIndex,
    inflation_nominal: float = ql.nullDouble(),
    trigger=None,
) -> ql.CPISwap:
    return ql.CPISwap(
        swap_type,
        nominal,
        subtract_inflation_nominal,
        spread,
        float_day_count,
        float_schedule,
        float_roll,
        fixing_days,
        float_index,
        fixed_rate,
        base_cpi,
        fixed_day_count,
        fixed_schedule,
        fixed_roll,
        observation_lag,
        fixed_index,
        observation_interpolation,
        inflation_nominal,
    )


@xlo.func(
    help="Get the fair rate of a CPI swap.",
    args={
        "swap": "The CPI swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPISwapFairRate(swap: ql.CPISwap, trigger=None) -> float:
    return swap.fairRate()


@xlo.func(
    help="Get the float leg NPV of a CPI swap.",
    args={
        "swap": "The CPI swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPISwapFloatLegNPV(swap: ql.CPISwap, trigger=None) -> float:
    return swap.floatLegNPV()


@xlo.func(
    help="Get the fair spread of a CPI swap.",
    args={
        "swap": "The CPI swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPISwapFairSpread(swap: ql.CPISwap, trigger=None) -> float:
    return swap.fairSpread()


@xlo.func(
    help="Get the fixed leg NPV of a CPI swap.",
    args={
        "swap": "The CPI swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPISwapFixedLegNPV(swap: ql.CPISwap, trigger=None) -> float:
    return swap.fixedLegNPV()


@xlo.func(
    help="Get the CPI leg of a CPI swap.",
    args={
        "swap": "The CPI swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPISwapCPILeg(swap: ql.CPISwap, trigger=None) -> ql.Leg:
    return swap.cpiLeg()


@xlo.func(
    help="Get the float leg of a CPI swap.",
    args={
        "swap": "The CPI swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCPISwapFloatLeg(swap: ql.CPISwap, trigger=None) -> ql.Leg:
    return swap.floatLeg()


## YoY Inflation Cap Floor


@xlo.func(
    help="Create a QuantLib YoYInflationCapFloor object.",
    args={
        "capfloor_type": "The type (CAP, FLOOR, COLLAR).",
        "yoy_leg": "The YoY leg.",
        "strikes": "The list of strike rates.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCapFloor(
    capfloor_type: qYoYInflationCapFloorType,
    yoy_leg: ql.Leg,
    strikes: xlo.Array(dims=1),
    trigger=None,
) -> ql.YoYInflationCapFloor:
    _strikes = to_float_list(strikes)
    _yoy_leg = to_object_list(yoy_leg, ql.CashFlow)
    return ql.YoYInflationCapFloor(capfloor_type, _yoy_leg, _strikes)


# Remark: Not implemented in QuantLib 1.42.1 ("not implemented yet").
@xlo.func(
    help="Get the implied volatility from a YoY inflation cap/floor.",
    args={
        "capfloor": "The YoY inflation cap/floor.",
        "price": "The price.",
        "curve": "The YoY inflation term structure handle.",
        "guess": "The initial volatility guess.",
        "accuracy": "The accuracy for the calculation.",
        "max_evaluations": "The maximum number of evaluations.",
        "min_vol": "The minimum volatility.",
        "max_vol": "The maximum volatility.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCapFloorImpliedVolatility(
    capfloor: ql.YoYInflationCapFloor,
    price: float,
    curve: ql.YoYInflationTermStructureHandle,
    guess: float,
    accuracy: float = 1.0e-4,
    max_evaluations: int = 100,
    min_vol: float = 1.0e-7,
    max_vol: float = 4.0,
    trigger=None,
) -> float:
    return capfloor.impliedVolatility(
        price, curve, guess, accuracy, max_evaluations, min_vol, max_vol
    )


@xlo.func(
    help="Get the optionlet prices from a YoY inflation cap/floor.",
    args={
        "capfloor": "The YoY inflation cap/floor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCapFloorOptionletPrices(
    capfloor: ql.YoYInflationCapFloor, trigger=None
) -> tuple:
    return capfloor.optionletPrices()


## YoY Inflation Cap


@xlo.func(
    help="Create a QuantLib YoYInflationCap object.",
    args={
        "leg": "The leg of cash flows.",
        "cap_rates": "The list of cap rates.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCap(
    leg: xlo.Array(dims=1),
    cap_rates: xlo.Array(dims=1),
    trigger=None,
) -> ql.YoYInflationCap:
    _leg = to_object_list(leg, ql.CashFlow)
    _cap_rates = to_float_list(cap_rates)
    return ql.YoYInflationCap(_leg, _cap_rates)


## YoY Inflation Floor


@xlo.func(
    help="Create a QuantLib YoYInflationFloor object.",
    args={
        "leg": "The leg of cash flows.",
        "floor_rates": "The list of floor rates.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationFloor(
    leg: xlo.Array(dims=1),
    floor_rates: xlo.Array(dims=1),
    trigger=None,
) -> ql.YoYInflationFloor:
    _leg = to_object_list(leg, ql.CashFlow)
    _floor_rates = to_float_list(floor_rates)
    return ql.YoYInflationFloor(_leg, _floor_rates)


## YoY Inflation Collar


@xlo.func(
    help="Create a QuantLib YoYInflationCollar object.",
    args={
        "leg": "The leg of cash flows.",
        "cap_rates": "The list of cap rates.",
        "floor_rates": "The list of floor rates.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCollar(
    leg: xlo.Array(dims=1),
    cap_rates: xlo.Array(dims=1),
    floor_rates: xlo.Array(dims=1),
    trigger=None,
) -> ql.YoYInflationCollar:
    _leg = to_object_list(leg, ql.CashFlow)
    _cap_rates = to_float_list(cap_rates)
    _floor_rates = to_float_list(floor_rates)
    return ql.YoYInflationCollar(_leg, _cap_rates, _floor_rates)


## Interpolated Zero Inflation Curve


@xlo.func(
    help="Create an InterpolatedZeroInflationCurve as Handle.",
    args={
        "reference_date": "The reference date.",
        "dates": "The list of dates.",
        "rates": "The list of rates.",
        "frequency": "The frequency.",
        "day_counter": "The day counter.",
        "seasonality": "The seasonality object (optional).",
        "interpolator": "The interpolator (optional, default is Linear).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCurve(
    reference_date: qDate,
    dates: xlo.Array(dims=1),
    rates: xlo.Array(dims=1),
    frequency: qFrequency,
    day_counter: qDayCounter,
    seasonality: ql.Seasonality = None,
    trigger=None,
) -> ql.ZeroInflationTermStructureHandle:
    _dates = _to_date_list(dates)
    _rates = to_float_list(rates)
    return ql.ZeroInflationTermStructureHandle(
        ql.ZeroInflationCurve(
            reference_date, _dates, _rates, frequency, day_counter, seasonality
        )
    )


# To access class methods, we add constructors for YieldTermStructures '*AsIts'.
# We want to also allow conversion into a Handle to use the curve as input to
# other functions.
@xlo.func(
    help="Create an InterpolatedZeroInflationCurve.",
    args={
        "reference_date": "The reference date.",
        "dates": "The list of dates.",
        "rates": "The list of rates.",
        "frequency": "The frequency.",
        "day_counter": "The day counter.",
        "seasonality": "The seasonality object (optional).",
        "interpolator": "The interpolator (optional, default is Linear).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCurveAsIts(
    reference_date: qDate,
    dates: xlo.Array(dims=1),
    rates: xlo.Array(dims=1),
    frequency: qFrequency,
    day_counter: qDayCounter,
    seasonality: ql.Seasonality = None,
    trigger=None,
) -> ql.ZeroInflationTermStructure:
    _dates = _to_date_list(dates)
    _rates = to_float_list(rates)
    return ql.ZeroInflationCurve(
        reference_date, _dates, _rates, frequency, day_counter, seasonality
    )


@xlo.func(
    help="Get the dates from an interpolated zero inflation curve.",
    args={
        "curve": "The interpolated zero inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCurveDates(
    curve: ql.ZeroInflationTermStructure, trigger=None
) -> tuple:
    return curve.dates()


@xlo.func(
    help="Get the times from an interpolated zero inflation curve.",
    args={
        "curve": "The interpolated zero inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCurveTimes(
    curve: ql.ZeroInflationTermStructure, trigger=None
) -> tuple:
    return curve.times()


@xlo.func(
    help="Get the data from an interpolated zero inflation curve.",
    args={
        "curve": "The interpolated zero inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCurveData(
    curve: ql.ZeroInflationTermStructure, trigger=None
) -> tuple:
    return curve.data()


@xlo.func(
    help="Get the rates from an interpolated zero inflation curve.",
    args={
        "curve": "The interpolated zero inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCurveRates(
    curve: ql.ZeroInflationTermStructure, trigger=None
) -> tuple:
    return curve.rates()


@xlo.func(
    help="Get the nodes (dates and rates) from an interpolated zero inflation curve.",
    args={
        "curve": "The interpolated zero inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationCurveNodes(
    curve: ql.ZeroInflationTermStructure, trigger=None
) -> tuple:
    return curve.nodes()


## Handle Converter Functions Zero and YoY Inflation Structures


@xlo.func(
    help="Convert a ZeroInflationTermStructure to a ZeroInflationTermStructureHandle.",
    args={
        "curve": "The ZeroInflationTermStructure to convert.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZeroInflationTermStructureHandle(
    curve: ql.ZeroInflationTermStructure,
    trigger=None,
) -> ql.ZeroInflationTermStructureHandle:
    return ql.ZeroInflationTermStructureHandle(curve)


@xlo.func(
    help="Convert a YoYInflationTermStructure to a ZeroInflationTermStructureHandle.",
    args={
        "curve": "The YoYInflationTermStructure to convert.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationTermStructureHandle(
    curve: ql.YoYInflationTermStructure,
    trigger=None,
) -> ql.YoYInflationTermStructureHandle:
    return ql.YoYInflationTermStructureHandle(curve)


## Interpolated YoY Inflation Curve


# uses Linear interpolator internally
@xlo.func(
    help="Create an InterpolatedYoYInflationCurve.",
    args={
        "reference_date": "The reference date.",
        "dates": "The list of dates.",
        "rates": "The list of rates.",
        "frequency": "The frequency.",
        "day_counter": "The day counter.",
        "seasonality": "The seasonality object (optional).",
        "interpolator": "The interpolator (optional, default is Linear).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCurve(
    reference_date: qDate,
    dates: xlo.Array(dims=1),
    rates: xlo.Array(dims=1),
    frequency: qFrequency,
    day_counter: qDayCounter,
    seasonality: ql.Seasonality = None,
    trigger=None,
) -> ql.YoYInflationTermStructureHandle:
    _dates = _to_date_list(dates)
    _rates = to_float_list(rates)
    return ql.YoYInflationTermStructureHandle(
        ql.YoYInflationCurve(
            reference_date,
            _dates,
            _rates,
            frequency,
            day_counter,
            seasonality,
        )
    )


# To access class methods, we add constructors for YieldTermStructures '*AsIts'.
# We want to also allow conversion into a Handle to use the curve as input to
# other functions.
@xlo.func(
    help="Create an InterpolatedYoYInflationCurve.",
    args={
        "reference_date": "The reference date.",
        "dates": "The list of dates.",
        "rates": "The list of rates.",
        "frequency": "The frequency.",
        "day_counter": "The day counter.",
        "seasonality": "The seasonality object (optional).",
        "interpolator": "The interpolator (optional, default is Linear).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCurveAsIts(
    reference_date: qDate,
    dates: xlo.Array(dims=1),
    rates: xlo.Array(dims=1),
    frequency: qFrequency,
    day_counter: qDayCounter,
    seasonality: ql.Seasonality = None,
    trigger=None,
) -> ql.YoYInflationTermStructure:
    _dates = _to_date_list(dates)
    _rates = to_float_list(rates)
    return ql.YoYInflationCurve(
        reference_date,
        _dates,
        _rates,
        frequency,
        day_counter,
        seasonality,
    )


@xlo.func(
    help="Get the dates from an interpolated YoY inflation curve.",
    args={
        "curve": "The interpolated YoY inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCurveDates(
    curve: ql.YoYInflationTermStructure, trigger=None
) -> tuple:
    return curve.dates()


@xlo.func(
    help="Get the times from an interpolated YoY inflation curve.",
    args={
        "curve": "The interpolated YoY inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCurveTimes(
    curve: ql.YoYInflationTermStructure, trigger=None
) -> tuple:
    return curve.times()


@xlo.func(
    help="Get the rates from an interpolated YoY inflation curve.",
    args={
        "curve": "The interpolated YoY inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCurveRates(
    curve: ql.YoYInflationTermStructure, trigger=None
) -> tuple:
    return curve.rates()


@xlo.func(
    help="Get the data from an interpolated YoY inflation curve.",
    args={
        "curve": "The interpolated YoY inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCurveData(curve: ql.YoYInflationTermStructure, trigger=None) -> tuple:
    return curve.data()


@xlo.func(
    help="Get the nodes (dates and rates) from an interpolated YoY inflation curve.",
    args={
        "curve": "The interpolated YoY inflation curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCurveNodes(
    curve: ql.YoYInflationTermStructure, trigger=None
) -> tuple:
    return curve.nodes()


## YoY Cap/Floor Term Price Surface Member Functions


@xlo.func(
    help="Get the ATM YoY swap time rates from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceAtmYoYSwapTimeRates(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> tuple[list[float], list[float]]:
    return surface.atmYoYSwapTimeRates()


@xlo.func(
    help="Get the ATM YoY swap date rates from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceAtmYoYSwapDateRates(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> tuple[list[ql.Date], list[float]]:
    return surface.atmYoYSwapDateRates()


@xlo.func(
    help="Get the YoY term structure from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceYoYTS(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> ql.YoYInflationTermStructureHandle:
    return surface.YoYTS()


@xlo.func(
    help="Get the YoY inflation index from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceYoYIndex(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> ql.YoYInflationIndex:
    return surface.yoyIndex()


@xlo.func(
    help="Get the business day convention from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceBusinessDayConvention(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
):
    return first_key(QL_BUSINESSDAYCONVENTION, surface.businessDayConvention())


@xlo.func(
    help="Get the observation lag from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceObservationLag(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> ql.Period:
    return surface.observationLag()


@xlo.func(
    help="Get the frequency from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceFrequency(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
):
    return first_key(QL_FREQUENCY, surface.frequency())


@xlo.func(
    help="Get the fixing days from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceFixingDays(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> int:
    return surface.fixingDays()


@xlo.func(
    help="Get the cap price for a YoY cap/floor term price surface at a specific date and strike.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
        "date": "The date.",
        "strike": "The strike rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceCapPrice(
    surface: ql.YoYCapFloorTermPriceSurface,
    date: qDate,
    strike: float,
    trigger=None,
) -> float:
    return surface.capPrice(date, strike)


@xlo.func(
    help="Get the cap price for a YoY cap/floor term price surface at a specific period and strike.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
        "period": "The period.",
        "strike": "The strike rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceCapPrice2(
    surface: ql.YoYCapFloorTermPriceSurface,
    period: qPeriod,
    strike: float,
    trigger=None,
) -> float:
    return surface.capPrice(period, strike)


@xlo.func(
    help="Get the floor price for a YoY cap/floor term price surface at a specific date and strike.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
        "date": "The date.",
        "strike": "The strike rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceFloorPrice(
    surface: ql.YoYCapFloorTermPriceSurface,
    date: qDate,
    strike: float,
    trigger=None,
) -> float:
    return surface.floorPrice(date, strike)


@xlo.func(
    help="Get the floor price for a YoY cap/floor term price surface at a specific period and strike.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
        "period": "The period.",
        "strike": "The strike rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceFloorPrice2(
    surface: ql.YoYCapFloorTermPriceSurface,
    period: qPeriod,
    strike: float,
    trigger=None,
) -> float:
    return surface.floorPrice(period, strike)


@xlo.func(
    help="Get the price for a YoY cap/floor term price surface at a specific date and strike.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
        "date": "The date.",
        "strike": "The strike rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfacePrice(
    surface: ql.YoYCapFloorTermPriceSurface,
    date: qDate,
    strike: float,
    trigger=None,
) -> float:
    return surface.price(date, strike)


@xlo.func(
    help="Get the price for a YoY cap/floor term price surface at a specific period and strike.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
        "period": "The period.",
        "strike": "The strike rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfacePrice2(
    surface: ql.YoYCapFloorTermPriceSurface,
    period: qPeriod,
    strike: float,
    trigger=None,
) -> float:
    return surface.price(period, strike)


@xlo.func(
    help="Get the ATM YoY swap rate from a YoY cap/floor term price surface for a specific date.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
        "date": "The date.",
        "extrapolate": "Whether to extrapolate if the date is outside the surface range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceAtmYoYSwapRate(
    surface: ql.YoYCapFloorTermPriceSurface,
    date: qDate,
    extrapolate: bool = True,
    trigger=None,
) -> float:
    return surface.atmYoYSwapRate(date, extrapolate)


@xlo.func(
    help="Get the ATM YoY swap rate from a YoY cap/floor term price surface for a specific period.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
        "period": "The period.",
        "extrapolate": "Whether to extrapolate if the period is outside the surface range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceAtmYoYSwapRate2(
    surface: ql.YoYCapFloorTermPriceSurface,
    period: qPeriod,
    extrapolate: bool = True,
    trigger=None,
) -> float:
    return surface.atmYoYSwapRate(period, extrapolate)


@xlo.func(
    help="Get the ATM YoY rate from a YoY cap/floor term price surface for a specific date.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
        "date": "The date.",
        "observation_lag": "The observation lag.",
        "extrapolate": "Whether to extrapolate if the date is outside the surface range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceAtmYoYRate(
    surface: ql.YoYCapFloorTermPriceSurface,
    date: qDate,
    observation_lag: qPeriod = ql.Period(-1, ql.Days),
    extrapolate: bool = True,
    trigger=None,
) -> float:
    return surface.atmYoYRate(date, observation_lag, extrapolate)


@xlo.func(
    help="Get the ATM YoY rate from a YoY cap/floor term price surface for a specific period.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
        "period": "The period.",
        "observation_lag": "The observation lag.",
        "extrapolate": "Whether to extrapolate if the period is outside the surface range.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceAtmYoYRate2(
    surface: ql.YoYCapFloorTermPriceSurface,
    period: qPeriod,
    observation_lag: qPeriod = ql.Period(-1, ql.Days),
    extrapolate: bool = True,
    trigger=None,
) -> float:
    return surface.atmYoYRate(period, observation_lag, extrapolate)


@xlo.func(
    help="Get the base date from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceBaseDate(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> ql.Date:
    return surface.baseDate()


@xlo.func(
    help="Get the strikes from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceStrikes(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> tuple:
    return surface.strikes()


@xlo.func(
    help="Get the cap strikes from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceCapStrikes(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> tuple:
    return surface.capStrikes()


@xlo.func(
    help="Get the floor strikes from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceFloorStrikes(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> tuple:
    return surface.floorStrikes()


@xlo.func(
    help="Get the maturities from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceMaturities(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> tuple:
    return surface.maturities()


@xlo.func(
    help="Get the minimum strike from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceMinStrike(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> float:
    return surface.minStrike()


@xlo.func(
    help="Get the maximum strike from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceMaxStrike(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> float:
    return surface.maxStrike()


@xlo.func(
    help="Get the minimum maturity from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceMinMaturity(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> ql.Date:
    return surface.minMaturity()


@xlo.func(
    help="Get the maximum maturity from a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceMaxMaturity(
    surface: ql.YoYCapFloorTermPriceSurface, trigger=None
) -> ql.Date:
    return surface.maxMaturity()


@xlo.func(
    help="Get the YoY option date from tenor for a YoY cap/floor term price surface.",
    args={
        "surface": "The YoY cap/floor term price surface handle.",
        "period": "The period tenor.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYCapFloorTermPriceSurfaceYoyOptionDateFromTenor(
    surface: ql.YoYCapFloorTermPriceSurface,
    period: qPeriod,
    trigger=None,
) -> ql.Date:
    return surface.yoyOptionDateFromTenor(period)


# uses BiCubic aund Cubic interpolators internally
# No handle is available for ql.YoYInflationCapFloorTermPriceSurface; use only as a shared pointer
@xlo.func(
    help="Create a YoY cap/floor term price surface from market prices (strikes × maturities).",
    args={
        "fixing_days": "Number of fixing days for the surface.",
        "yoy_lag": "Observation lag (e.g., 3M).",
        "yoy_index": "The YoY inflation index (e.g., YYEUHICP).",
        "interpolation": "CPI interpolation type: ASINDEX, FLAT, or LINEAR.",
        "nominal_term_structure": "Handle to the nominal yield term structure.",
        "day_counter": "Day counter (e.g., Actual/365).",
        "calendar": "Calendar (e.g., TARGET).",
        "business_day_convention": "Business day convention (e.g., Following).",
        "cap_strikes": "List of cap strike rates (as 1D array).",
        "floor_strikes": "List of floor strike rates (as 1D array).",
        "maturities": "List of maturities (as periods, e.g., 1Y, 5Y, 10Y).",
        "cap_prices": "Matrix of cap prices (strikes × maturities, as 2D array).",
        "floor_prices": "Matrix of floor prices (strikes × maturities, as 2D array).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationCapFloorTermPriceSurface(
    fixing_days: int,
    yoy_lag: qPeriod,
    yoy_index: ql.YoYInflationIndex,
    interpolation: qCPIInterpolationType,
    nominal_term_structure: ql.YieldTermStructureHandle,
    day_counter: qDayCounter,
    calendar: qCalendar,
    business_day_convention: qBusinessDayConvention,
    cap_strikes: xlo.Array(dims=1),
    floor_strikes: xlo.Array(dims=1),
    maturities: xlo.Array(dims=1),
    cap_prices: xlo.Array(dims=2),
    floor_prices: xlo.Array(dims=2),
    trigger=None,
) -> ql.YoYCapFloorTermPriceSurface:

    _cap_strikes = to_float_list(cap_strikes)
    _floor_strikes = to_float_list(floor_strikes)
    _maturities = [qPeriod.__wrapped__(length) for length in maturities]
    _cap_prices = ql.Matrix(to_float_matrix(cap_prices))
    _floor_prices = ql.Matrix(to_float_matrix(floor_prices))
    surface = ql.YoYInflationCapFloorTermPriceSurface(
        fixing_days,
        yoy_lag,
        yoy_index,
        interpolation,
        nominal_term_structure,
        day_counter,
        calendar,
        business_day_convention,
        _cap_strikes,
        _floor_strikes,
        _maturities,
        _cap_prices,
        _floor_prices,
    )
    return surface


## YoY Inflation Cap Floor Engines


@xlo.func(
    help="Create a QuantLib YoYInflationBlackCapFloorEngine object.",
    args={
        "index": "The YoY inflation index.",
        "vol": "The YoY optionlet volatility surface handle.",
        "nominal_term_structure": "The nominal term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationBlackCapFloorEngine(
    index: ql.YoYInflationIndex,
    vol: ql.YoYOptionletVolatilitySurfaceHandle,
    nominal_term_structure: ql.YieldTermStructureHandle,
    trigger=None,
) -> ql.YoYInflationBlackCapFloorEngine:
    return ql.YoYInflationBlackCapFloorEngine(index, vol, nominal_term_structure)


@xlo.func(
    help="Create a QuantLib YoYInflationUnitDisplacedBlackCapFloorEngine object.",
    args={
        "index": "The YoY inflation index.",
        "vol": "The YoY optionlet volatility surface handle.",
        "nominal_term_structure": "The nominal term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationUnitDisplacedBlackCapFloorEngine(
    index: ql.YoYInflationIndex,
    vol: ql.YoYOptionletVolatilitySurfaceHandle,
    nominal_term_structure: ql.YieldTermStructureHandle,
    trigger=None,
) -> ql.YoYInflationUnitDisplacedBlackCapFloorEngine:
    return ql.YoYInflationUnitDisplacedBlackCapFloorEngine(
        index, vol, nominal_term_structure
    )


@xlo.func(
    help="Create a QuantLib YoYInflationBachelierCapFloorEngine object.",
    args={
        "index": "The YoY inflation index.",
        "vol": "The YoY optionlet volatility surface handle.",
        "nominal_term_structure": "The nominal term structure handle.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYInflationBachelierCapFloorEngine(
    index: ql.YoYInflationIndex,
    vol: ql.YoYOptionletVolatilitySurfaceHandle,
    nominal_term_structure: ql.YieldTermStructureHandle,
    trigger=None,
) -> ql.YoYInflationBachelierCapFloorEngine:
    return ql.YoYInflationBachelierCapFloorEngine(index, vol, nominal_term_structure)


## YoY Optionlet Helper


@xlo.func(
    help="Create a QuantLib YoYOptionletHelper object for bootstrapping YoY inflation cap/floor surfaces.",
    args={
        "price": "The quote handle for the optionlet price.",
        "notional": "The notional amount.",
        "cap_floor_type": "The type (CAP, FLOOR, COLLAR).",
        "lag": "The observation lag period.",
        "yoy_day_counter": "The YoY day counter.",
        "payment_calendar": "The payment calendar.",
        "fixing_days": "The number of fixing days.",
        "index": "The YoY inflation index.",
        "interpolation": "The CPI interpolation type (ASINDEX, FLAT, LINEAR).",
        "strike": "The strike rate.",
        "n": "The number of optionlets.",
        "pricer": "The YoY inflation cap/floor pricing engine.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletHelper(
    price: qQuoteHandle,
    notional: float,
    cap_floor_type: qYoYInflationCapFloorType,
    lag: qPeriod,
    yoy_day_counter: qDayCounter,
    payment_calendar: qCalendar,
    fixing_days: int,
    index: ql.YoYInflationIndex,
    interpolation: qCPIInterpolationType,
    strike: float,
    n: int,
    pricer: ql.PricingEngine,
    trigger=None,
) -> ql.YoYOptionletHelper:
    return ql.YoYOptionletHelper(
        price,
        notional,
        cap_floor_type,
        lag,
        yoy_day_counter,
        payment_calendar,
        fixing_days,
        index,
        interpolation,
        strike,
        n,
        pricer,
    )


## YoY Optionlet Stripper


@xlo.func(
    help="Create a QuantLib YoYOptionletStripper object.",
    args={},
    group=EXCEL_GROUP_NAME,
)
def qlInterpolatedYoYInflationOptionletStripper(
    trigger=None,
) -> ql.YoYOptionletStripper:
    return ql.InterpolatedYoYInflationOptionletStripper()


@xlo.func(
    help="Initialize a YoYOptionletStripper with a surface and pricing engine.",
    args={
        "stripper": "The YoYOptionletStripper object.",
        "surf": "The YoY cap/floor term price surface handle.",
        "pricer": "The YoY inflation cap/floor pricing engine.",
        "slope": "The slope parameter for extrapolation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletStripperInitialize(
    stripper: ql.YoYOptionletStripper,
    surf: ql.YoYCapFloorTermPriceSurface,
    pricer: ql.PricingEngine,
    slope: float,
    trigger=None,
) -> bool:
    stripper.initialize(surf, pricer, slope)
    return True


@xlo.func(
    help="Get the maximum strike from a YoYOptionletStripper.",
    args={
        "stripper": "The YoYOptionletStripper object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletStripperMaxStrike(
    stripper: ql.YoYOptionletStripper,
    trigger=None,
) -> float:
    return stripper.maxStrike()


@xlo.func(
    help="Get the strikes from a YoYOptionletStripper.",
    args={
        "stripper": "The YoYOptionletStripper object.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletStripperStrikes(
    stripper: ql.YoYOptionletStripper,
    trigger=None,
) -> list[float]:
    return stripper.strikes()


@xlo.func(
    help="Get the volatility slice (strikes and volatilities) for a date from YoYOptionletStripper.",
    args={
        "stripper": "The YoYOptionletStripper object.",
        "date": "The date for which to get the slice.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlYoYOptionletStripperSlice(
    stripper: ql.YoYOptionletStripper,
    date: qDate,
    trigger=None,
) -> tuple[list[float], list[float]]:
    result = stripper.slice(date)
    return (result[0], result[1])


## Interpolated YoY Optionlet Volatility Curve


# uses Linear interpolator internally
@xlo.func(
    help="Create a QuantLib InterpolatedYoYOptionletVolatilityCurve with Linear interpolation.",
    args={
        "settlement_days": "The settlement days for the curve.",
        "calendar": "The calendar for the curve.",
        "bdc": "The business day convention.",
        "day_counter": "The day counter.",
        "lag": "The observation lag period.",
        "frequency": "The frequency of the curve.",
        "index_is_interpolated": "Whether the underlying index is interpolated.",
        "dates": "The list of dates for the curve.",
        "volatilities": "The list of volatilities corresponding to the dates.",
        "min_strike": "The minimum strike for the curve.",
        "max_strike": "The maximum strike for the curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterpolatedYoYInflationOptionletVolatilityCurve(
    settlement_days: int,
    calendar: qCalendar,
    bdc: qBusinessDayConvention,
    day_counter: qDayCounter,
    lag: qPeriod,
    frequency: qFrequency,
    index_is_interpolated: bool,
    dates: xlo.Array(dims=1),
    volatilities: xlo.Array(dims=1),
    min_strike: float,
    max_strike: float,
    trigger=None,
) -> ql.YoYOptionletVolatilitySurfaceHandle:
    _dates = _to_date_list(dates)
    _vols = to_float_list(volatilities)
    return ql.YoYOptionletVolatilitySurfaceHandle(
        ql.InterpolatedYoYInflationOptionletVolatilityCurve(
            settlement_days,
            calendar,
            bdc,
            day_counter,
            lag,
            frequency,
            index_is_interpolated,
            _dates,
            _vols,
            min_strike,
            max_strike,
        )
    )


## K Interpolated YoY Optionlet Volatility Surface


# uses Linear interpolator internally
@xlo.func(
    help="Create a QuantLib KInterpolatedYoYOptionletVolatilitySurface with Linear interpolation.",
    args={
        "settlement_days": "The settlement days for the surface.",
        "calendar": "The calendar for the surface.",
        "bdc": "The business day convention.",
        "day_counter": "The day counter.",
        "lag": "The observation lag period.",
        "cap_floor_prices": "The YoY cap/floor term price surface handle.",
        "pricer": "The YoY inflation cap/floor pricing engine.",
        "yoy_optionlet_stripper": "The YoY optionlet stripper.",
        "slope": "The slope parameter for extrapolation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlKInterpolatedYoYInflationOptionletVolatilitySurface(
    settlement_days: int,
    calendar: qCalendar,
    bdc: qBusinessDayConvention,
    day_counter: qDayCounter,
    lag: qPeriod,
    cap_floor_prices: ql.YoYCapFloorTermPriceSurface,
    pricer: ql.PricingEngine,
    yoy_optionlet_stripper: ql.YoYOptionletStripper,
    slope: float,
    trigger=None,
) -> ql.YoYOptionletVolatilitySurfaceHandle:
    return ql.YoYOptionletVolatilitySurfaceHandle(
        ql.KInterpolatedYoYInflationOptionletVolatilitySurface(
            settlement_days,
            calendar,
            bdc,
            day_counter,
            lag,
            cap_floor_prices,
            pricer,
            yoy_optionlet_stripper,
            slope,
        )
    )


@xlo.func(
    help="Get the Dslice (strikes and volatilities) for a date from KInterpolatedYoYOptionletVolatilitySurface.",
    args={
        "surface": "The KInterpolatedYoYOptionletVolatilitySurface object.",
        "date": "The date for which to get the slice.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlKInterpolatedYoYOptionletVolatilitySurfaceDslice(
    surface: ql.YoYOptionletVolatilitySurface,
    date: qDate,
    trigger=None,
) -> tuple[list[float], list[float]]:
    result = surface.Dslice(date)
    return (result[0], result[1])
