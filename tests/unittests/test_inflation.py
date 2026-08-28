import QuantLib as ql
import pytest


from quantlib_xloil.inflation import (
    qCPIInterpolationType,
    qYoYInflationCapFloorType,
    qlAUCPI,
    qlEUHICP,
    qlEUHICPXT,
    qlFRHICP,
    qlUKRPI,
    qlUKHICP,
    qlUSCPI,
    qlZACPI,
    qlYYEUHICP,
    qlYYEUHICP2,
    qlYYEUHICPXT,
    qlYYEUHICPXT2,
    qlYYFRHICP,
    qlYYFRHICP2,
    qlYYUKRPI,
    qlYYUKRPI2,
    qlYYUSCPI,
    qlYYUSCPI2,
    qlYYZACPI,
    qlYYZACPI2,
    qlBachelierYoYInflationCouponPricer,
    qlBlackYoYInflationCouponPricer,
    qlBootstrapHelperEarliestDate,
    qlBootstrapHelperImpliedQuote,  # TODO
    qlBootstrapHelperLatestDate,
    qlBootstrapHelperLatestRelevantDate,
    qlBootstrapHelperMaturityDate,
    qlBootstrapHelperPillarDate,
    qlBootstrapHelperQuote,
    qlBootstrapHelperQuoteError,  # TODO
    qlCPICashFlow,
    qlCPICashFlowFrequency,
    qlCPICashFlowInterpolation,
    qlCPICoupon,
    qlCPICoupon2,
    qlCPICoupon3,
    qlCPICouponAdjustedIndexGrowth,
    qlCPICouponBaseCPI,
    qlCPICouponBaseDate,
    qlCPICouponCPIIndex,
    qlCPICouponFixedRate,
    qlCPICouponIndexFixing,
    qlCPICouponIndexRatio,
    qlCPICouponObservationInterpolation,
    qlCPICouponPricer,
    qlCPICouponSetPricer,
    qlCPILeg,
    qlCPISwap,
    qlCPISwapFairRate,
    qlCPISwapFairSpread,
    qlCPISwapFloatLegNPV,
    qlCPISwapFixedLegNPV,
    qlCPISwapCPILeg,
    qlCPISwapFloatLeg,
    qlCustomRegion,
    qlCappedFlooredYoYInflationCoupon,
    qlCappedFlooredYoYInflationCouponCap,
    qlCappedFlooredYoYInflationCouponEffectiveCap,
    qlCappedFlooredYoYInflationCouponEffectiveFloor,
    qlCappedFlooredYoYInflationCouponFloor,
    qlCappedFlooredYoYInflationCouponIsCapped,
    qlCappedFlooredYoYInflationCouponIsFloored,
    qlCappedFlooredYoYInflationCouponRate,
    qlCappedFlooredYoYInflationCouponUnderlyingRate,
    qlInflationBaseDate,
    qlInflationCouponFixingDate,
    qlInflationCouponFixingDays,
    qlInflationCouponIndex,
    qlInflationCouponIndexFixing,
    qlInflationCouponObservationLag,
    qlInflationIndexAvailabilityLag,
    qlInflationIndexCurrency,
    qlInflationIndexFamilyName,
    qlInflationIndexFrequency,
    qlInflationIndexRegion,
    qlInflationIndexRevised,
    qlInflationPeriod,
    qlInflationTermStructureBaseDate,
    qlInflationTermStructureBaseRate,
    qlInflationTermStructureFrequency,
    qlInflationTermStructureHasExplicitBaseDate,
    qlInflationTermStructureHasSeasonality,
    qlInflationTermStructureObservationLag,
    qlInflationTermStructureSeasonality,
    qlInflationTermStructureSetSeasonality,
    qlInflationYearFraction,
    qlYoYInflationCurve,
    qlYoYInflationCurveAsIts,
    qlYoYInflationCurveData,
    qlYoYInflationCurveDates,
    qlYoYInflationCurveNodes,
    qlYoYInflationCurveRates,
    qlYoYInflationCurveTimes,
    qlZeroInflationCurve,
    qlZeroInflationCurveAsIts,
    qlZeroInflationCurveData,
    qlZeroInflationCurveDates,
    qlZeroInflationCurveNodes,
    qlZeroInflationCurveRates,
    qlZeroInflationCurveTimes,
    qlKerkhofSeasonality,
    qlKInterpolatedYoYInflationOptionletVolatilitySurface,  # TODO
    qlKInterpolatedYoYOptionletVolatilitySurfaceDslice,  # TODO
    qlMultiplicativePriceSeasonality,
    qlMultiplicativePriceSeasonalityFactor,
    qlMultiplicativePriceSeasonalityFactors,
    qlPiecewiseYoYInflation,
    qlPiecewiseYoYInflationAsIts,
    qlPiecewiseYoYInflationCurveData,
    qlPiecewiseYoYInflationCurveDates,
    qlPiecewiseYoYInflationCurveNodes,
    qlPiecewiseYoYInflationCurveTimes,
    qlPiecewiseZeroInflation,
    qlPiecewiseZeroInflationAsIts,
    qlPiecewiseZeroInflationCurveData,
    qlPiecewiseZeroInflationCurveDates,
    qlPiecewiseZeroInflationCurveNodes,
    qlPiecewiseZeroInflationCurveTimes,
    qlRegionCode,
    qlRegionName,
    qlMultiplicativePriceSeasonalitySeasonalityBaseDate,
    qlMultiplicativePriceSeasonalityFrequency,
    qlUnitDisplacedBlackYoYInflationCouponPricer,
    qlYearOnYearInflationSwap,
    qlYearOnYearInflationSwapFairRate,
    qlYearOnYearInflationSwapFairSpread,
    qlYearOnYearInflationSwapFixedLeg,
    qlYearOnYearInflationSwapFixedLegNPV,
    qlYearOnYearInflationSwapYoYLeg,
    qlYearOnYearInflationSwapYoYLegNPV,
    qlYoYInflationBlackCapFloorEngine,
    qlYoYInflationBachelierCapFloorEngine,
    qlYoYInflationCap,
    qlYoYInflationCapFloor,
    qlYoYInflationCapFloorTermPriceSurface,
    qlYoYInflationCapFloorImpliedVolatility,
    qlYoYInflationCapFloorOptionletPrices,
    qlYoYInflationCollar,
    qlYoYInflationCoupon,
    qlYoYInflationCouponAdjustedFixing,
    qlYoYInflationCouponGearing,
    qlYoYInflationCouponInterpolation,
    qlYoYInflationCouponSpread,
    qlYoYInflationCouponYoYIndex,
    qlYoYInflationFloor,
    qlYoYInflationIndex,
    qlYoYInflationIndex2,
    qlYoYInflationIndexClone,
    qlYoYInflationIndexInterpolated,
    qlYoYInflationIndexLastFixingDate,
    qlYoYInflationIndexNeedsForecast,
    qlYoYInflationIndexRatio,
    qlYoYInflationIndexUnderlyingIndex,
    qlYoYInflationIndexYoYInflationTermStructure,
    qlYoYInflationLeg,
    qlYoYInflationUnitDisplacedBlackCapFloorEngine,
    qlYoYOptionletHelper,
    qlInterpolatedYoYInflationOptionletStripper,
    qlYoYOptionletStripperInitialize,  # TODO
    qlYoYOptionletStripperMaxStrike,  # TODO
    qlYoYOptionletStripperSlice,  # TODO
    qlYoYOptionletStripperStrikes,  # TODO
    qlYoYInflationCouponSetPricer,
    qlInterpolatedYoYInflationOptionletVolatilityCurve,
    qlYoYCapFloorTermPriceSurfaceAtmYoYRate,
    qlYoYCapFloorTermPriceSurfaceAtmYoYRate2,
    qlYoYCapFloorTermPriceSurfaceAtmYoYSwapDateRates,
    qlYoYCapFloorTermPriceSurfaceAtmYoYSwapRate,
    qlYoYCapFloorTermPriceSurfaceAtmYoYSwapRate2,
    qlYoYCapFloorTermPriceSurfaceAtmYoYSwapTimeRates,
    qlYoYCapFloorTermPriceSurfaceBaseDate,
    qlYoYCapFloorTermPriceSurfaceBusinessDayConvention,
    qlYoYCapFloorTermPriceSurfaceCapPrice,
    qlYoYCapFloorTermPriceSurfaceCapPrice2,
    qlYoYCapFloorTermPriceSurfaceCapStrikes,
    qlYoYCapFloorTermPriceSurfaceFloorPrice,
    qlYoYCapFloorTermPriceSurfaceFloorPrice2,
    qlYoYCapFloorTermPriceSurfaceFloorStrikes,
    qlYoYCapFloorTermPriceSurfaceFrequency,
    qlYoYCapFloorTermPriceSurfaceFixingDays,
    qlYoYCapFloorTermPriceSurfaceMaxMaturity,
    qlYoYCapFloorTermPriceSurfaceMaxStrike,
    qlYoYCapFloorTermPriceSurfaceMinMaturity,
    qlYoYCapFloorTermPriceSurfaceMinStrike,
    qlYoYCapFloorTermPriceSurfaceMaturities,
    qlYoYCapFloorTermPriceSurfaceObservationLag,
    qlYoYCapFloorTermPriceSurfacePrice,
    qlYoYCapFloorTermPriceSurfacePrice2,
    qlYoYCapFloorTermPriceSurfaceStrikes,
    qlYoYCapFloorTermPriceSurfaceYoYTS,
    qlYoYCapFloorTermPriceSurfaceYoYIndex,
    qlYoYCapFloorTermPriceSurfaceYoyOptionDateFromTenor,
    qlYoYInflationTermStructureHandle,
    qlYoYInflationTermStructureYoYRate,
    qlYoYInflationTermStructureYoYRate2,
    qlYoYInflationTermStructureYoYRate3,
    qlZeroCouponInflationSwap,
    qlZeroCouponInflationSwapFairRate,
    qlZeroCouponInflationSwapFixedLeg,
    qlZeroCouponInflationSwapFixedLegBPS,
    qlZeroCouponInflationSwapFixedLegNPV,
    qlZeroCouponInflationSwapInflationLeg,
    qlZeroCouponInflationSwapInflationLegNPV,
    qlZeroCouponInflationSwapType,
    qlZeroInflationCashFlow,
    qlZeroInflationCashFlowBaseDate,
    qlZeroInflationCashFlowFixingDate,
    qlZeroInflationCashFlowGrowthOnly,
    qlZeroInflationCashFlowNotional,
    qlZeroInflationCashFlowObservationInterpolation,
    qlZeroInflationCashFlowZeroInflationIndex,
    qlZeroInflationIndex,
    qlZeroInflationIndexClone,
    qlZeroInflationIndexLastFixingDate,
    qlZeroInflationIndexNeedsForecast,
    qlZeroInflationIndexZeroInflationTermStructure,
    qlZeroInflationTermStructureHandle,
    qlZeroInflationTermStructureZeroRate,
    qlZeroInflationTermStructureZeroRate2,
    qlZeroInflationTermStructureZeroRate3,
    qlZeroCouponInflationSwapHelper,
    qlZeroCouponInflationSwapHelperSwap,
    qlYearOnYearInflationSwapHelper,
    qlYearOnYearInflationSwapHelperSwap,
    qlCPILaggedFixing,
    qlCPILaggedYoYRate,
)

from quantlib_xloil.calendars import qBusinessDayConvention, qCalendar
from quantlib_xloil.currencies import qCurrency
from quantlib_xloil.date import qFrequency, qPeriod
from quantlib_xloil.daycounters import qDayCounter
from quantlib_xloil.indexes import qlUSDLibor
from quantlib_xloil.instruments import qlInstrumentSetPricingEngine
from quantlib_xloil.termstructures import qlFlatForward
from quantlib_xloil.scheduler import qDateGenerationRule
from quantlib_xloil.swap import qSwapType


# Helper functions
def _region() -> ql.CustomRegion:
    return qlCustomRegion("TestRegion", "TR")


def _currency() -> ql.Currency:
    return qCurrency.__wrapped__("USD")


def _calendar() -> ql.Calendar:
    return qCalendar.__wrapped__("TARGET")


def _day_counter() -> ql.DayCounter:
    return qDayCounter.__wrapped__("ACTUAL365FIXED")


def _set_eval_date() -> None:
    ql.Settings.instance().evaluationDate = ql.Date(1, 1, 2024)


def _zero_inflation_index() -> ql.ZeroInflationIndex:
    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 10, 2023), ql.Date(1, 10, 2024), ql.Date(1, 10, 2029)]
    rates = [0.02, 0.02, 0.02]

    inflation_curve = qlZeroInflationCurve(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )
    return qlZeroInflationIndex(
        "TEST-ZERO",
        _region(),
        False,
        qFrequency.__wrapped__("ANNUAL"),
        qPeriod.__wrapped__("3M"),
        _currency(),
        inflation_curve,
    )


def _yoy_inflation_index() -> ql.YoYInflationIndex:
    return qlYoYInflationIndex2(
        "TEST-YOY",
        _region(),
        False,
        qFrequency.__wrapped__("ANNUAL"),
        qPeriod.__wrapped__("3M"),
        _currency(),
        interpolated=False,
    )


def _schedule(start_date, end_date, tenor) -> ql.Schedule:
    return ql.Schedule(
        start_date,
        end_date,
        tenor,
        _calendar(),
        qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        qDateGenerationRule.__wrapped__("FORWARD"),
        False,
    )


# =============================================================================
# CPI Interpolation Type Tests
# =============================================================================


def test_qCPIInterpolationType():
    assert qCPIInterpolationType.__wrapped__("ASINDEX") == ql.CPI.AsIndex
    assert qCPIInterpolationType.__wrapped__("FLAT") == ql.CPI.Flat
    assert qCPIInterpolationType.__wrapped__("LINEAR") == ql.CPI.Linear


def test_qYoYInflationCapFloorType():
    assert qYoYInflationCapFloorType.__wrapped__("CAP") == ql.YoYInflationCapFloor.Cap
    assert (
        qYoYInflationCapFloorType.__wrapped__("FLOOR") == ql.YoYInflationCapFloor.Floor
    )
    assert (
        qYoYInflationCapFloorType.__wrapped__("COLLAR")
        == ql.YoYInflationCapFloor.Collar
    )


# =============================================================================
# Region Tests
# =============================================================================


def test_qlCustomRegion():
    region = qlCustomRegion("TestRegion", "TR")
    assert isinstance(region, ql.CustomRegion)
    assert qlRegionName(region) == "TestRegion"
    assert qlRegionCode(region) == "TR"


# =============================================================================
# Seasonality Tests
# =============================================================================


def test_qlMultiplicativePriceSeasonality():
    _set_eval_date()
    base_date = ql.Date(1, 1, 2024)
    factors = (1.0, 1.02, 1.01, 1.03)
    seasonality = qlMultiplicativePriceSeasonality(
        base_date, qFrequency.__wrapped__("QUARTERLY"), factors
    )
    assert isinstance(seasonality, ql.MultiplicativePriceSeasonality)
    assert qlMultiplicativePriceSeasonalitySeasonalityBaseDate(seasonality) == base_date
    assert qlMultiplicativePriceSeasonalityFrequency(seasonality) == "QUARTERLY"
    assert qlMultiplicativePriceSeasonalityFactors(seasonality) == factors


def test_qlMultiplicativePriceSeasonalityFactor():
    _set_eval_date()
    base_date = ql.Date(1, 1, 2024)
    factors = [1.0, 1.02, 1.01, 1.03]
    seasonality = qlMultiplicativePriceSeasonality(
        base_date, qFrequency.__wrapped__("QUARTERLY"), factors
    )
    test_date = ql.Date(1, 1, 2024)
    factor = qlMultiplicativePriceSeasonalityFactor(seasonality, test_date)
    assert isinstance(factor, float)


def test_qlKerkhofSeasonality():
    _set_eval_date()
    base_date = ql.Date(1, 1, 2024)
    factors = [
        1.0,
        1.02,
        1.01,
        1.03,
        1.0,
        1.02,
        1.01,
        1.03,
        1.0,
        1.02,
        1.01,
        1.03,
    ]
    seasonality = qlKerkhofSeasonality(base_date, factors)
    assert isinstance(seasonality, ql.KerkhofSeasonality)


# =============================================================================
# Inflation Term Structure Tests
# =============================================================================


def test_qlInflationTermStructure_getters_setters():

    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    index = _zero_inflation_index()
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    index = _zero_inflation_index()
    ts = ql.YieldTermStructureHandle()
    helper = qlZeroCouponInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2028),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_its=ts,
    )

    curve = qlPiecewiseZeroInflationAsIts(
        reference_date,
        base_date,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        [helper],
    )

    assert isinstance(qlInflationTermStructureBaseDate(curve), ql.Date)
    assert isinstance(qlInflationTermStructureObservationLag(curve), ql.Period)
    assert isinstance(qlInflationTermStructureHasExplicitBaseDate(curve), bool)
    assert qlInflationTermStructureSeasonality(curve) == None
    assert qlInflationTermStructureFrequency(curve) == "ANNUAL"

    with pytest.raises(RuntimeError) as exc_info:
        qlInflationTermStructureBaseRate(curve)
    assert str(exc_info.value) == "base rate not available"

    factors = [1.0, 1.02, 1.01, 1.03]
    seasonality = qlMultiplicativePriceSeasonality(
        base_date, qFrequency.__wrapped__("QUARTERLY"), factors
    )
    assert qlInflationTermStructureHasSeasonality(curve) == False
    qlInflationTermStructureSetSeasonality(curve, seasonality)

    assert qlInflationTermStructureHasSeasonality(curve) == True


# =============================================================================
# YoY Inflation Term Structure Tests
# =============================================================================


def test_qlYoYInflationTermStructureYoYRate():

    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)

    ts = qlFlatForward(reference_date, 0.03, _day_counter())

    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    index = _yoy_inflation_index()
    helper = qlYearOnYearInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2027),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=ts,
    )

    curve = qlPiecewiseYoYInflation(
        reference_date,
        base_date,
        0.02,
        qFrequency.__wrapped__("SEMIANNUAL"),
        _day_counter(),
        [helper],
    )

    test_date = ql.Date(1, 6, 2024)
    rate = qlYoYInflationTermStructureYoYRate(curve, test_date)
    assert isinstance(rate, float)
    observation_lag = qPeriod.__wrapped__("3M")
    rate2 = qlYoYInflationTermStructureYoYRate2(
        curve,
        test_date,
        observation_lag,
        force_linear_interpolation=False,
        extrapolate=False,
    )
    assert isinstance(rate2, float)
    test_time = 0.5
    rate3 = qlYoYInflationTermStructureYoYRate3(curve, test_time, extrapolate=False)
    assert isinstance(rate3, float)


def test_qlYoYInflationTermStructureYoYRate_with_extrapolation():

    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)

    ts = qlFlatForward(reference_date, 0.03, _day_counter())

    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    index = _yoy_inflation_index()
    helper = qlYearOnYearInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2027),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=ts,
    )

    curve = qlPiecewiseYoYInflation(
        reference_date,
        base_date,
        0.02,
        qFrequency.__wrapped__("SEMIANNUAL"),
        _day_counter(),
        [helper],
    )

    test_date = ql.Date(1, 6, 2024)
    rate = qlYoYInflationTermStructureYoYRate(curve, test_date, extrapolate=True)
    assert isinstance(rate, float)


# =============================================================================
# Zero Inflation Term Structure Tests
# =============================================================================


def test_qlZeroInflationTermStructureZeroRate():

    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 1, 2023), ql.Date(1, 1, 2024), ql.Date(1, 1, 2029)]
    rates = [0.02, 0.02, 0.02]

    inflation_curve = qlZeroInflationCurve(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    test_date = ql.Date(1, 6, 2024)
    rate = qlZeroInflationTermStructureZeroRate(inflation_curve, test_date)
    assert isinstance(rate, float)
    observation_lag = qPeriod.__wrapped__("2M")
    rate2 = qlZeroInflationTermStructureZeroRate2(
        inflation_curve, test_date, observation_lag, False, False
    )
    assert isinstance(rate2, float)
    time = 1.5
    rate3 = qlZeroInflationTermStructureZeroRate3(inflation_curve, time, False)
    assert isinstance(rate3, float)


# =============================================================================
# Inflation Index Tests
# =============================================================================


def test_qlInflationIndexFamilyName():
    index = _zero_inflation_index()
    name = qlInflationIndexFamilyName(index)
    assert name == "TEST-ZERO"


def test_qlInflationIndexRegion():
    index = _zero_inflation_index()
    region = qlInflationIndexRegion(index)
    assert isinstance(region, ql.Region)


def test_qlInflationIndexRevised():
    index = _zero_inflation_index()
    assert qlInflationIndexRevised(index) is False


def test_qlInflationIndexFrequency():
    index = _zero_inflation_index()
    freq = qlInflationIndexFrequency(index)
    assert freq == "ANNUAL"


def test_qlInflationIndexAvailabilityLag():
    index = _zero_inflation_index()
    lag = qlInflationIndexAvailabilityLag(index)
    assert isinstance(lag, ql.Period)


def test_qlInflationIndexCurrency():
    index = _zero_inflation_index()
    currency = qlInflationIndexCurrency(index)
    assert isinstance(currency, ql.Currency)


# =============================================================================
# Zero Inflation Index Tests
# =============================================================================


def test_qlZeroInflationIndex():
    index = _zero_inflation_index()
    assert isinstance(index, ql.ZeroInflationIndex)
    assert qlInflationIndexFamilyName(index) == "TEST-ZERO"


def test_qlZeroInflationIndexLastFixingDate():
    index = _zero_inflation_index()
    index.addFixing(ql.Date(1, 1, 2024), 100.0, forceOverwrite=True)
    date = qlZeroInflationIndexLastFixingDate(index)
    assert isinstance(date, ql.Date)


def test_qlZeroInflationIndexZeroInflationTermStructure():
    index = _zero_inflation_index()
    ts = qlZeroInflationIndexZeroInflationTermStructure(index)
    assert isinstance(ts, ql.ZeroInflationTermStructureHandle)


def test_qlZeroInflationIndexNeedsForecast():
    index = _zero_inflation_index()
    fixing_date = ql.Date(1, 6, 2024)
    result = qlZeroInflationIndexNeedsForecast(index, fixing_date)
    assert isinstance(result, bool)


# =============================================================================
# YoY Inflation Index Tests
# =============================================================================


def test_qlYoYInflationIndex():
    index = _yoy_inflation_index()
    index.addFixing(ql.Date(1, 1, 2024), 100.0, forceOverwrite=True)
    assert isinstance(index, ql.YoYInflationIndex)
    assert qlYoYInflationIndexLastFixingDate(index) is not None


def test_qlYoYInflationIndex2():
    index = qlYoYInflationIndex2(
        "TEST-YOY-2",
        _region(),
        False,
        qFrequency.__wrapped__("ANNUAL"),
        qPeriod.__wrapped__("3M"),
        _currency(),
        interpolated=True,
    )
    assert isinstance(index, ql.YoYInflationIndex)
    assert qlYoYInflationIndexInterpolated(index) is True


def test_qlYoYInflationIndexRatio():
    index = _yoy_inflation_index()
    result = qlYoYInflationIndexRatio(index)
    assert isinstance(result, bool)


def test_qlYoYInflationIndexInterpolated():
    index = _yoy_inflation_index()
    result = qlYoYInflationIndexInterpolated(index)
    assert isinstance(result, bool)


def test_qlYoYInflationIndexUnderlyingIndex():
    zero_index = _zero_inflation_index()
    yoy_index = qlYoYInflationIndex(zero_index)
    underlying = qlYoYInflationIndexUnderlyingIndex(yoy_index)
    assert isinstance(underlying, ql.ZeroInflationIndex)


def test_qlYoYInflationIndexYoYInflationTermStructure():
    index = _yoy_inflation_index()
    ts = qlYoYInflationIndexYoYInflationTermStructure(index)
    assert isinstance(ts, ql.YoYInflationTermStructureHandle)


def test_qlYoYInflationIndexClone():
    index = _yoy_inflation_index()
    ts = ql.YoYInflationTermStructureHandle()
    cloned = qlYoYInflationIndexClone(index, ts)
    assert isinstance(cloned, ql.YoYInflationIndex)


def test_qlYoYInflationIndexNeedsForecast():
    index = _yoy_inflation_index()
    fixing_date = ql.Date(1, 6, 2024)
    result = qlYoYInflationIndexNeedsForecast(index, fixing_date)
    assert isinstance(result, bool)


# =============================================================================
# Zero Inflation Index Tests
# =============================================================================


def _zeroindexinflationcurve() -> ql.ZeroInflationTermStructureHandle:
    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)
    ts_yield = qlFlatForward(reference_date, 0.03, _day_counter())

    index = _zero_inflation_index()
    index.addFixing(ql.Date(1, 1, 2024), 100.0, forceOverwrite=True)

    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    helper = qlZeroCouponInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2029),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_its=ts_yield,
    )

    inflation_curve = qlPiecewiseZeroInflation(
        reference_date,
        base_date,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        [helper],
    )

    return inflation_curve


def test_qlAUCPI():
    index = qlAUCPI(qFrequency.__wrapped__("QUARTERLY"), True)
    assert isinstance(index, ql.AUCPI)


def test_qlAUCPI_with_term_structure():
    ts_handle = _zeroindexinflationcurve()
    aucpi_index = qlAUCPI(qFrequency.__wrapped__("QUARTERLY"), True, ts_handle)
    assert isinstance(aucpi_index, ql.AUCPI)


def test_qlEUHICP():
    index = qlEUHICP()
    assert isinstance(index, ql.EUHICP)


def test_qlEUHICP_with_term_structure():
    ts_handle = _zeroindexinflationcurve()
    euhicp_index = qlEUHICP(ts_handle)
    assert isinstance(euhicp_index, ql.EUHICP)


def test_qlEUHICPXT():
    index = qlEUHICPXT()
    assert isinstance(index, ql.EUHICPXT)


def test_qlEUHICPXT_with_term_structure():
    ts_handle = _zeroindexinflationcurve()
    euhicpxt_index = qlEUHICPXT(ts_handle)
    assert isinstance(euhicpxt_index, ql.EUHICPXT)


def test_qlFRHICP():
    index = qlFRHICP()
    assert isinstance(index, ql.FRHICP)


def test_qlFRHICP_with_term_structure():
    ts_handle = _zeroindexinflationcurve()
    frhicp_index = qlFRHICP(ts_handle)
    assert isinstance(frhicp_index, ql.FRHICP)


def test_qlUKRPI():
    index = qlUKRPI()
    assert isinstance(index, ql.UKRPI)


def test_qlUKRPI_with_term_structure():
    ts_handle = _zeroindexinflationcurve()
    ukrpi_index = qlUKRPI(ts_handle)
    assert isinstance(ukrpi_index, ql.UKRPI)


def test_qlUKHICP():
    index = qlUKHICP()
    assert isinstance(index, ql.UKHICP)


def test_qlUKHICP_with_term_structure():
    ts_handle = _zeroindexinflationcurve()
    ukhicp_index = qlUKHICP(ts_handle)
    assert isinstance(ukhicp_index, ql.UKHICP)


def test_qlUSCPI():
    index = qlUSCPI()
    assert isinstance(index, ql.USCPI)


def test_qlUSCPI_with_term_structure():
    ts_handle = _zeroindexinflationcurve()
    uscpi_index = qlUSCPI(ts_handle)
    assert isinstance(uscpi_index, ql.USCPI)


def test_qlZACPI():
    index = qlZACPI()
    assert isinstance(index, ql.ZACPI)


def test_qlZACPI_with_term_structure():
    ts_handle = _zeroindexinflationcurve()
    zacpi_index = qlZACPI(ts_handle)
    assert isinstance(zacpi_index, ql.ZACPI)


# =============================================================================
# YoY Inflation Index Tests
# =============================================================================


def _yoyindexinflationcurve() -> ql.YoYInflationTermStructureHandle:
    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)
    ts_yield = qlFlatForward(reference_date, 0.03, _day_counter())

    yoy_index = _yoy_inflation_index()
    yoy_index.addFixing(ql.Date(1, 1, 2023), 100.0, forceOverwrite=True)
    yoy_index.addFixing(ql.Date(1, 1, 2024), 102.0, forceOverwrite=True)

    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    helper = qlYearOnYearInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2029),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=yoy_index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=ts_yield,
    )

    yoy_curve = qlPiecewiseYoYInflation(
        reference_date,
        base_date,
        0.02,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        [helper],
    )

    return yoy_curve


def test_qlYYEUHICP():
    index = qlYYEUHICP()
    assert isinstance(index, ql.YYEUHICP)


def test_qlYYEUHICP_with_term_structure():
    ts_handle = _yoyindexinflationcurve()
    yy_index = qlYYEUHICP(ts_handle)
    assert isinstance(yy_index, ql.YYEUHICP)


def test_qlYYEUHICP2():
    index = qlYYEUHICP2(True)
    assert isinstance(index, ql.YYEUHICP)


def test_qlYYEUHICP2_with_term_structure():
    ts_handle = _yoyindexinflationcurve()
    yy_index = qlYYEUHICP2(False, ts_handle)
    assert isinstance(yy_index, ql.YYEUHICP)
    assert qlYoYInflationIndexInterpolated(yy_index) is False


def test_qlYYEUHICPXT():
    index = qlYYEUHICPXT()
    assert isinstance(index, ql.YYEUHICPXT)


def test_qlYYEUHICPXT_with_term_structure():
    ts_handle = _yoyindexinflationcurve()
    yy_index = qlYYEUHICPXT(ts_handle)
    assert isinstance(yy_index, ql.YYEUHICPXT)


def test_qlYYEUHICPXT2():
    index = qlYYEUHICPXT2(True)
    assert isinstance(index, ql.YYEUHICPXT)


def test_qlYYEUHICPXT2_with_term_structure():
    ts_handle = _yoyindexinflationcurve()
    yy_index = qlYYEUHICPXT2(True, ts_handle)
    assert isinstance(yy_index, ql.YYEUHICPXT)
    assert qlYoYInflationIndexInterpolated(yy_index) is True


def test_qlYYFRHICP():
    index = qlYYFRHICP()
    assert isinstance(index, ql.YYFRHICP)


def test_qlYYFRHICP_with_term_structure():
    ts_handle = _yoyindexinflationcurve()
    yy_index = qlYYFRHICP(ts_handle)
    assert isinstance(yy_index, ql.YYFRHICP)


def test_qlYYFRHICP2():
    index = qlYYFRHICP2(False)
    assert isinstance(index, ql.YYFRHICP)


def test_qlYYFRHICP2_with_term_structure():
    ts_handle = _yoyindexinflationcurve()
    yy_index = qlYYFRHICP2(True, ts_handle)
    assert isinstance(yy_index, ql.YYFRHICP)
    assert qlYoYInflationIndexInterpolated(yy_index) is True


def test_qlYYUKRPI():
    index = qlYYUKRPI()
    assert isinstance(index, ql.YYUKRPI)


def test_qlYYUKRPI_with_term_structure():
    ts_handle = _yoyindexinflationcurve()
    yy_index = qlYYUKRPI(ts_handle)
    assert isinstance(yy_index, ql.YYUKRPI)


def test_qlYYUKRPI2():
    index = qlYYUKRPI2(True)
    assert isinstance(index, ql.YYUKRPI)


def test_qlYYUKRPI2_with_term_structure():
    ts_handle = _yoyindexinflationcurve()
    yy_index = qlYYUKRPI2(False, ts_handle)
    assert isinstance(yy_index, ql.YYUKRPI)
    assert qlYoYInflationIndexInterpolated(yy_index) is False


def test_qlYYUSCPI():
    index = qlYYUSCPI()
    assert isinstance(index, ql.YYUSCPI)


def test_qlYYUSCPI_with_term_structure():
    ts_handle = _yoyindexinflationcurve()
    yy_index = qlYYUSCPI(ts_handle)
    assert isinstance(yy_index, ql.YYUSCPI)


def test_qlYYUSCPI2():
    index = qlYYUSCPI2(False)
    assert isinstance(index, ql.YYUSCPI)


def test_qlYYUSCPI2_with_term_structure():
    ts_handle = _yoyindexinflationcurve()
    yy_index = qlYYUSCPI2(True, ts_handle)
    assert isinstance(yy_index, ql.YYUSCPI)
    assert qlYoYInflationIndexInterpolated(yy_index) is True


def test_qlYYZACPI():
    index = qlYYZACPI()
    assert isinstance(index, ql.YYZACPI)


def test_qlYYZACPI_with_term_structure():
    ts_handle = _yoyindexinflationcurve()
    yy_index = qlYYZACPI(ts_handle)
    assert isinstance(yy_index, ql.YYZACPI)


def test_qlYYZACPI2():
    index = qlYYZACPI2(True)
    assert isinstance(index, ql.YYZACPI)


def test_qlYYZACPI2_with_term_structure():
    ts_handle = _yoyindexinflationcurve()
    yy_index = qlYYZACPI2(False, ts_handle)
    assert isinstance(yy_index, ql.YYZACPI)
    assert qlYoYInflationIndexInterpolated(yy_index) is False


# =============================================================================
# CPI Utilities Tests
# =============================================================================


def test_qlCPILaggedFixing():
    _set_eval_date()
    index = _zero_inflation_index()
    index.addFixing(ql.Date(1, 10, 2023), 100, forceOverwrite=True)
    date = ql.Date(1, 6, 2024)
    lag = ql.Period("3M")
    result = qlCPILaggedFixing(
        index, date, lag, qCPIInterpolationType.__wrapped__("ASINDEX")
    )
    assert isinstance(result, float)


def test_qlCPILaggedYoYRate():
    _set_eval_date()
    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 1, 2023), ql.Date(1, 1, 2024), ql.Date(1, 1, 2025)]
    rates = [0.02, 0.025, 0.03]

    yoy_curve = qlYoYInflationCurve(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    yoy_index = _yoy_inflation_index()
    yoy_index.addFixing(ql.Date(1, 1, 2023), 100.0, forceOverwrite=True)
    yoy_index.addFixing(ql.Date(1, 1, 2024), 102.0, forceOverwrite=True)
    yoy_index.addFixing(ql.Date(1, 1, 2025), 104.0, forceOverwrite=True)

    yoy_curve_handle = yoy_curve
    yoy_index_with_curve = qlYoYInflationIndexClone(yoy_index, yoy_curve_handle)

    date = ql.Date(1, 6, 2024)
    lag = ql.Period("3M")
    result = qlCPILaggedYoYRate(
        yoy_index_with_curve, date, lag, qCPIInterpolationType.__wrapped__("ASINDEX")
    )
    assert isinstance(result, float)


# =============================================================================
# Inflation Cash Flow Tests
# =============================================================================


def test_qlInflationCouponFixingDate():
    index = _zero_inflation_index()

    coupon = qlYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=_yoy_inflation_index(),
        observation_lag=ql.Period("3M"),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
    )
    fixing_date = qlInflationCouponFixingDate(coupon)
    assert isinstance(fixing_date, ql.Date)


def test_qlInflationCouponFixingDays():
    index = _zero_inflation_index()

    coupon = qlYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=2,
        index=_yoy_inflation_index(),
        observation_lag=ql.Period("3M"),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
    )
    fixing_days = qlInflationCouponFixingDays(coupon)
    assert fixing_days == 2


def test_qlInflationCouponObservationLag():
    index = _zero_inflation_index()

    coupon = qlYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=_yoy_inflation_index(),
        observation_lag=qPeriod.__wrapped__("3M"),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
    )
    lag = qlInflationCouponObservationLag(coupon)
    assert isinstance(lag, ql.Period)


def test_qlInflationCouponIndex():
    _set_eval_date()
    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 1, 2024), ql.Date(1, 1, 2025), ql.Date(1, 1, 2026)]
    rates = [0.02, 0.025, 0.03]

    yoy_curve = qlYoYInflationCurve(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    index = _yoy_inflation_index()
    index.addFixing(ql.Date(1, 1, 2024), 100.0, forceOverwrite=True)

    index_with_curve = qlYoYInflationIndexClone(index, yoy_curve)

    coupon = qlYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index_with_curve,
        observation_lag=qPeriod.__wrapped__("3M"),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
    )
    idx = qlInflationCouponIndex(coupon)
    assert isinstance(idx, ql.InflationIndex)
    assert isinstance(qlInflationCouponIndexFixing(coupon), float)


# =============================================================================
# CPI Coupon Tests
# =============================================================================


def test_qlCPICoupon():
    index = _zero_inflation_index()
    coupon = qlCPICoupon(
        base_cpi=100.0,
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        index=index,
        observation_lag=ql.Period("3M"),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        fixed_rate=0.02,
    )
    assert isinstance(coupon, ql.CPICoupon)
    assert qlCPICouponFixedRate(coupon) == 0.02


def test_qlCPICoupon2():
    index = _zero_inflation_index()
    coupon = qlCPICoupon2(
        base_date=ql.Date(1, 1, 2024),
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        index=index,
        observation_lag=qPeriod.__wrapped__("3M"),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        fixed_rate=0.02,
    )
    assert isinstance(coupon, ql.CPICoupon)
    assert qlCPICouponBaseDate(coupon) == ql.Date(1, 1, 2024)


def test_qlCPICoupon3():
    index = _zero_inflation_index()
    coupon = qlCPICoupon3(
        base_cpi=100.0,
        base_date=ql.Date(1, 1, 2024),
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        index=index,
        observation_lag=qPeriod.__wrapped__("3M"),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        fixed_rate=0.02,
    )
    assert isinstance(coupon, ql.CPICoupon)
    assert qlCPICouponBaseCPI(coupon) == 100.0


def test_qlCPICouponAdjustedIndexGrowth():
    _set_eval_date()

    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 10, 2023), ql.Date(1, 10, 2024), ql.Date(1, 10, 2029)]
    rates = [0.02, 0.02, 0.02]

    inflation_curve = qlZeroInflationCurve(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    index = qlZeroInflationIndex(
        "TEST-ZERO",
        _region(),
        False,
        qFrequency.__wrapped__("ANNUAL"),
        qPeriod.__wrapped__("3M"),
        _currency(),
        inflation_curve,
    )
    index.addFixing(ql.Date(1, 10, 2023), 100.0, forceOverwrite=True)

    coupon = qlCPICoupon(
        base_cpi=100.0,
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        index=index,
        observation_lag=qPeriod.__wrapped__("1M"),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        fixed_rate=0.02,
    )

    pricer = qlCPICouponPricer()
    qlCPICouponSetPricer(coupon, pricer)

    growth = qlCPICouponAdjustedIndexGrowth(coupon)
    assert isinstance(growth, float)


def test_qlCPICouponIndexFixing():
    index = _zero_inflation_index()
    coupon = qlCPICoupon(
        base_cpi=100.0,
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        index=index,
        observation_lag=qPeriod.__wrapped__("3M"),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        fixed_rate=0.02,
    )
    fixing = qlCPICouponIndexFixing(coupon)
    assert isinstance(fixing, float)


def test_qlCPICouponIndexRatio():
    ql.Settings.instance().evaluationDate = ql.Date(1, 1, 2024)

    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 10, 2023), ql.Date(1, 10, 2024), ql.Date(1, 10, 2029)]
    rates = [0.02, 0.02, 0.02]

    inflation_curve = qlZeroInflationCurve(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    index = qlZeroInflationIndex(
        "TEST-ZERO",
        _region(),
        False,
        qFrequency.__wrapped__("ANNUAL"),
        qPeriod.__wrapped__("3M"),
        _currency(),
        inflation_curve,
    )
    index.addFixing(ql.Date(1, 10, 2023), 100.0, forceOverwrite=True)

    coupon = qlCPICoupon(
        base_cpi=100.0,
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        index=index,
        observation_lag=qPeriod.__wrapped__("1M"),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        fixed_rate=0.02,
    )

    test_date = ql.Date(1, 6, 2024)
    ratio = qlCPICouponIndexRatio(coupon, test_date)
    assert isinstance(ratio, float)


def test_qlCPICouponCPIIndex():
    index = _zero_inflation_index()
    coupon = qlCPICoupon(
        base_cpi=100.0,
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        index=index,
        observation_lag=qPeriod.__wrapped__("3M"),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        fixed_rate=0.02,
    )
    cpi_index = qlCPICouponCPIIndex(coupon)
    assert isinstance(cpi_index, ql.ZeroInflationIndex)


def test_qlCPICouponObservationInterpolation():
    index = _zero_inflation_index()
    coupon = qlCPICoupon(
        base_cpi=100.0,
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        index=index,
        observation_lag=qPeriod.__wrapped__("3M"),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        fixed_rate=0.02,
    )
    interp = qlCPICouponObservationInterpolation(coupon)
    assert interp == "ASINDEX"


# =============================================================================
# CPI Cash Flow Tests
# =============================================================================


def test_qlCPICashFlow():
    index = _zero_inflation_index()
    cash_flow = qlCPICashFlow(
        notional=1000.0,
        index=index,
        base_date=ql.Date(1, 1, 2024),
        base_fixing=100.0,
        observation_date=ql.Date(1, 4, 2024),
        observation_lag=ql.Period(3, ql.Months),
        interpolation=ql.CPI.AsIndex,
        payment_date=ql.Date(1, 7, 2024),
        growth_only=False,
    )
    assert isinstance(cash_flow, ql.CPICashFlow)
    assert qlCPICashFlowFrequency(cash_flow) == "ANNUAL"
    assert qlCPICashFlowInterpolation(cash_flow) == "ASINDEX"


# =============================================================================
# Zero Inflation Cash Flow Tests
# =============================================================================


def test_qlZeroInflationCashFlow():
    index = _zero_inflation_index()
    cash_flow = qlZeroInflationCashFlow(
        notional=1000.0,
        index=index,
        observation_interpolation=ql.CPI.AsIndex,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        observation_lag=ql.Period(3, ql.Months),
        payment_date=ql.Date(1, 4, 2025),
        growth_only=False,
    )
    assert isinstance(cash_flow, ql.ZeroInflationCashFlow)
    assert qlZeroInflationCashFlowNotional(cash_flow) == 1000.0


def test_qlZeroInflationCashFlowBaseDate():
    index = _zero_inflation_index()
    cash_flow = qlZeroInflationCashFlow(
        notional=1000.0,
        index=index,
        observation_interpolation=ql.CPI.AsIndex,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        observation_lag=ql.Period(3, ql.Months),
        payment_date=ql.Date(1, 4, 2025),
        growth_only=False,
    )
    base_date = qlZeroInflationCashFlowBaseDate(cash_flow)
    assert isinstance(base_date, ql.Date)


def test_qlZeroInflationCashFlowFixingDate():
    index = _zero_inflation_index()
    cash_flow = qlZeroInflationCashFlow(
        notional=1000.0,
        index=index,
        observation_interpolation=ql.CPI.AsIndex,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        observation_lag=ql.Period(3, ql.Months),
        payment_date=ql.Date(1, 4, 2025),
        growth_only=False,
    )
    fixing_date = qlZeroInflationCashFlowFixingDate(cash_flow)
    assert isinstance(fixing_date, ql.Date)


def test_qlZeroInflationCashFlowGrowthOnly():
    index = _zero_inflation_index()
    cash_flow = qlZeroInflationCashFlow(
        notional=1000.0,
        index=index,
        observation_interpolation=ql.CPI.AsIndex,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        observation_lag=ql.Period(3, ql.Months),
        payment_date=ql.Date(1, 4, 2025),
        growth_only=True,
    )
    assert qlZeroInflationCashFlowGrowthOnly(cash_flow) is True


def test_qlZeroInflationCashFlowObservationInterpolation():
    index = _zero_inflation_index()
    cash_flow = qlZeroInflationCashFlow(
        notional=1000.0,
        index=index,
        observation_interpolation=ql.CPI.Linear,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        observation_lag=ql.Period(3, ql.Months),
        payment_date=ql.Date(1, 4, 2025),
        growth_only=False,
    )
    interp = qlZeroInflationCashFlowObservationInterpolation(cash_flow)
    assert interp == "LINEAR"


def test_qlZeroInflationCashFlowZeroInflationIndex():
    index = _zero_inflation_index()
    cash_flow = qlZeroInflationCashFlow(
        notional=1000.0,
        index=index,
        observation_interpolation=ql.CPI.AsIndex,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        observation_lag=ql.Period(3, ql.Months),
        payment_date=ql.Date(1, 4, 2025),
        growth_only=False,
    )
    idx = qlZeroInflationCashFlowZeroInflationIndex(cash_flow)
    assert isinstance(idx, ql.ZeroInflationIndex)


# =============================================================================
# CPI Leg Tests
# =============================================================================


def test_qlCPILeg():
    index = _zero_inflation_index()
    schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )
    leg = qlCPILeg(
        nominals=[1000000.0, 1000000.0, 1000000.0, 1000000.0, 1000000.0],
        schedule=schedule,
        index=index,
        base_cpi=100.0,
        observation_lag=ql.Period(3, ql.Months),
        payment_day_counter=_day_counter(),
    )
    assert isinstance(leg, (ql.Leg, tuple, list))
    assert len(leg) > 0


def test_qlCPILeg_full():
    index = _zero_inflation_index()
    schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )
    leg = qlCPILeg(
        nominals=[1000000.0, 1000000.0, 1000000.0, 1000000.0, 1000000.0],
        schedule=schedule,
        index=index,
        base_cpi=100.0,
        observation_lag=qPeriod.__wrapped__("3M"),
        payment_day_counter=_day_counter(),
        payment_convention=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        fixed_rates=[0.02, 0.02, 0.02, 0.02, 0.02],
        ex_coupon_period=qPeriod.__wrapped__("1M"),
        ex_coupon_calendar=_calendar(),
        ex_coupon_convention=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        ex_coupon_end_of_month=True,
        payment_calendar=_calendar(),
        growth_only=False,
        observation_interpolation=qCPIInterpolationType.__wrapped__("LINEAR"),
    )
    assert isinstance(leg, (ql.Leg, tuple, list))
    assert len(leg) > 0


# =============================================================================
# Bootstrap Helper Tests
# =============================================================================


def test_qlBootstrapHelper_getters():
    index = _zero_inflation_index()
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))

    helper = qlZeroCouponInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2029),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
    )

    assert isinstance(qlBootstrapHelperQuote(helper), ql.QuoteHandle)
    assert isinstance(qlBootstrapHelperLatestDate(helper), ql.Date)
    assert isinstance(qlBootstrapHelperEarliestDate(helper), ql.Date)
    assert isinstance(qlBootstrapHelperMaturityDate(helper), ql.Date)
    assert isinstance(qlBootstrapHelperLatestRelevantDate(helper), ql.Date)
    assert isinstance(qlBootstrapHelperPillarDate(helper), ql.Date)


# =============================================================================
# Zero Coupon Inflation Swap Helper Tests
# =============================================================================


def test_qlZeroCouponInflationSwapHelper_without_nominal_ts():
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    index = _zero_inflation_index()
    helper = qlZeroCouponInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2028),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
    )
    assert isinstance(helper, ql.ZeroCouponInflationSwapHelper)


def test_qlZeroCouponInflationSwapHelper():
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    index = _zero_inflation_index()
    ts = ql.YieldTermStructureHandle()
    helper = qlZeroCouponInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2028),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_its=ts,
    )
    assert isinstance(helper, ql.ZeroCouponInflationSwapHelper)


def test_qlZeroCouponInflationSwapHelperSwap():
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    index = _zero_inflation_index()
    helper = qlZeroCouponInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2028),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
    )
    swap = qlZeroCouponInflationSwapHelperSwap(helper)
    assert isinstance(swap, ql.ZeroCouponInflationSwap)


# =============================================================================
# Year On Year Inflation Swap Helper Tests
# =============================================================================


def test_qlYearOnYearInflationSwapHelper():
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    index = _yoy_inflation_index()
    ts = ql.YieldTermStructureHandle()
    helper = qlYearOnYearInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2028),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=ts,
    )
    assert isinstance(helper, ql.YearOnYearInflationSwapHelper)


def test_qlYearOnYearInflationSwapHelperSwap():
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    index = _yoy_inflation_index()
    ts = ql.YieldTermStructureHandle()
    helper = qlYearOnYearInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2028),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=ts,
    )
    swap = qlYearOnYearInflationSwapHelperSwap(helper)
    assert isinstance(swap, ql.YearOnYearInflationSwap)


# =============================================================================
# Piecewise Inflation Curve Tests
# =============================================================================


def test_qlPiecewiseZeroInflation():
    _set_eval_date()
    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 10, 2023)

    ts = qlFlatForward(reference_date, 0.03, _day_counter())
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    index = _zero_inflation_index()
    index.addFixing(ql.Date(1, 10, 2023), 100.0, forceOverwrite=True)
    index.addFixing(ql.Date(1, 1, 2024), 100.0, forceOverwrite=True)
    helper = qlZeroCouponInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2027),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_its=ts,
    )

    curve = qlPiecewiseZeroInflationAsIts(
        reference_date,
        base_date,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        [helper],
    )
    assert isinstance(curve, ql.PiecewiseZeroInflation)
    assert isinstance(qlPiecewiseZeroInflationCurveDates(curve), tuple)
    assert isinstance(qlPiecewiseZeroInflationCurveTimes(curve), tuple)
    assert isinstance(qlPiecewiseZeroInflationCurveData(curve), tuple)
    nodes = qlPiecewiseZeroInflationCurveNodes(curve)
    assert isinstance(nodes, tuple)
    assert len(nodes) > 0
    first_node = nodes[0]
    assert len(first_node) == 2
    assert isinstance(first_node[0], ql.Date)
    assert isinstance(first_node[1], (float, int))


def test_qlPiecewiseZeroInflation_with_seasonality():
    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)

    factors = [1.0, 1.02, 1.01, 1.03]
    seasonality = qlMultiplicativePriceSeasonality(
        base_date, qFrequency.__wrapped__("QUARTERLY"), factors
    )

    index = _zero_inflation_index()
    index.addFixing(ql.Date(1, 1, 2024), 100.0, forceOverwrite=True)

    ts_yield = qlFlatForward(reference_date, 0.03, _day_counter())

    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    helper = qlZeroCouponInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2028),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_its=ts_yield,
    )

    curve = qlPiecewiseZeroInflationAsIts(
        reference_date,
        base_date,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        [helper],
        seasonality=seasonality,
        accuracy=1.0e-12,
    )

    assert isinstance(curve, ql.PiecewiseZeroInflation)
    assert qlInflationTermStructureHasSeasonality(curve) is True
    assert isinstance(qlInflationTermStructureSeasonality(curve), ql.Seasonality)


def test_qlPiecewiseYoYInflation():
    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)
    ts = qlFlatForward(reference_date, 0.03, _day_counter())
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    index = _yoy_inflation_index()
    helper = qlYearOnYearInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2027),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=ts,
    )
    curve = qlPiecewiseYoYInflationAsIts(
        reference_date,
        base_date,
        0.02,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        [helper],
    )
    assert isinstance(curve, ql.PiecewiseYoYInflation)
    assert isinstance(qlPiecewiseYoYInflationCurveDates(curve), tuple)
    assert isinstance(qlPiecewiseYoYInflationCurveTimes(curve), tuple)
    assert isinstance(qlPiecewiseYoYInflationCurveData(curve), tuple)
    nodes = qlPiecewiseYoYInflationCurveNodes(curve)
    assert isinstance(nodes, tuple)
    assert len(nodes) > 0
    first_node = nodes[0]
    assert len(first_node) == 2
    assert isinstance(first_node[0], ql.Date)
    assert isinstance(first_node[1], (float, int))


def test_qlPiecewiseYoYInflation_with_seasonality():
    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)

    factors = [1.0, 1.02, 1.01, 1.03]
    seasonality = qlMultiplicativePriceSeasonality(
        base_date, qFrequency.__wrapped__("QUARTERLY"), factors
    )

    yoy_index = _yoy_inflation_index()
    yoy_index.addFixing(ql.Date(1, 1, 2023), 100.0, forceOverwrite=True)
    yoy_index.addFixing(ql.Date(1, 1, 2024), 102.0, forceOverwrite=True)

    ts_yield = qlFlatForward(reference_date, 0.03, _day_counter())

    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    helper = qlYearOnYearInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2027),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=yoy_index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=ts_yield,
    )

    curve = qlPiecewiseYoYInflationAsIts(
        reference_date,
        base_date,
        0.02,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        [helper],
        seasonality=seasonality,
        accuracy=1.0e-12,
    )

    assert isinstance(curve, ql.PiecewiseYoYInflation)
    assert qlInflationTermStructureHasSeasonality(curve) is True
    assert isinstance(qlInflationTermStructureSeasonality(curve), ql.Seasonality)


# =============================================================================
# Inflation Utilities Tests
# =============================================================================


def test_qlInflationPeriod():
    date = ql.Date(15, 1, 2024)
    freq = qFrequency.__wrapped__("MONTHLY")
    period = qlInflationPeriod(date, freq)
    assert isinstance(period, tuple)
    assert len(period) == 2


def test_qlInflationYearFraction():
    freq = qFrequency.__wrapped__("ANNUAL")
    day_count = _day_counter()
    date1 = ql.Date(1, 1, 2024)
    date2 = ql.Date(1, 1, 2025)
    result = qlInflationYearFraction(freq, False, day_count, date1, date2)
    assert isinstance(result, float)


def test_qlInflationBaseDate():
    reference_date = ql.Date(1, 1, 2024)
    lag = ql.Period(3, ql.Months)
    freq = qFrequency.__wrapped__("ANNUAL")
    result = qlInflationBaseDate(reference_date, lag, freq, False)
    assert isinstance(result, ql.Date)


# =============================================================================
# YoY Inflation Coupon Tests
# =============================================================================


def test_qlYoYInflationCoupon():
    index = _yoy_inflation_index()
    coupon = qlYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        gearing=1.0,
        spread=0.0,
    )
    assert isinstance(coupon, ql.YoYInflationCoupon)
    assert qlYoYInflationCouponGearing(coupon) == 1.0
    assert qlYoYInflationCouponSpread(coupon) == 0.0


def test_qlYoYInflationCouponAdjustedFixing():
    _set_eval_date()

    base_index = _yoy_inflation_index()
    base_index.addFixing(ql.Date(1, 1, 2023), 100.0, forceOverwrite=True)
    base_index.addFixing(ql.Date(1, 1, 2024), 102.0, forceOverwrite=True)

    reference_date = ql.Date(1, 1, 2024)
    ts_yield = qlFlatForward(reference_date, 0.03, _day_counter())
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))
    helper = qlYearOnYearInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2026),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=base_index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=ts_yield,
    )
    inflation_curve = qlPiecewiseYoYInflation(
        reference_date,
        reference_date,
        0.02,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        [helper],
    )

    index = qlYoYInflationIndexClone(base_index, inflation_curve)

    coupon = qlYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
    )

    vol_surface = qlInterpolatedYoYInflationOptionletVolatilityCurve(
        settlement_days=2,
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        lag=qPeriod.__wrapped__("3M"),
        frequency=qFrequency.__wrapped__("ANNUAL"),
        index_is_interpolated=False,
        dates=[
            reference_date,
            ql.Date(1, 1, 2025),
            ql.Date(1, 1, 2026),
        ],
        volatilities=[0.02, 0.025, 0.03],
        min_strike=0.01,
        max_strike=0.10,
    )

    ts = qlFlatForward(reference_date, 0.03, _day_counter())

    pricer = qlBlackYoYInflationCouponPricer(vol_surface, ts)
    qlYoYInflationCouponSetPricer(coupon, pricer)

    adjusted = qlYoYInflationCouponAdjustedFixing(coupon)
    assert isinstance(adjusted, float)


def test_qlYoYInflationCouponYoYIndex():
    index = _yoy_inflation_index()
    coupon = qlYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
    )
    yoy_index = qlYoYInflationCouponYoYIndex(coupon)
    assert isinstance(yoy_index, ql.YoYInflationIndex)


def test_qlYoYInflationCouponInterpolation():
    index = _yoy_inflation_index()
    coupon = qlYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=ql.CPI.Linear,
        day_counter=_day_counter(),
    )
    interp = qlYoYInflationCouponInterpolation(coupon)
    assert interp == "LINEAR"


# =============================================================================
# Capped Floored YoY Inflation Coupon Tests
# =============================================================================


def test_qlCappedFlooredYoYInflationCoupon():
    index = _yoy_inflation_index()
    coupon = qlCappedFlooredYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        cap=0.05,
        floor=0.02,
    )
    assert isinstance(coupon, ql.CappedFlooredYoYInflationCoupon)
    assert qlCappedFlooredYoYInflationCouponCap(coupon) == 0.05
    assert qlCappedFlooredYoYInflationCouponFloor(coupon) == 0.02
    assert qlCappedFlooredYoYInflationCouponIsCapped(coupon) is True
    assert qlCappedFlooredYoYInflationCouponIsFloored(coupon) is True


def test_qlCappedFlooredYoYInflationCoupon2():
    index = _yoy_inflation_index()
    coupon = qlCappedFlooredYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
    )
    assert isinstance(coupon, ql.CappedFlooredYoYInflationCoupon)


def test_qlCappedFlooredYoYInflationCouponRate():
    base_index = _yoy_inflation_index()
    base_index.addFixing(ql.Date(1, 1, 2023), 100.0, forceOverwrite=True)
    base_index.addFixing(ql.Date(1, 1, 2024), 102.0, forceOverwrite=True)
    base_index.addFixing(ql.Date(1, 1, 2025), 104.0, forceOverwrite=True)

    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)
    ts_yield = qlFlatForward(reference_date, 0.03, _day_counter())
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))

    helper = qlYearOnYearInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2029),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=base_index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=ts_yield,
    )

    inflation_curve = qlPiecewiseYoYInflation(
        reference_date,
        base_date,
        0.02,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        [helper],
    )

    index = qlYoYInflationIndexClone(base_index, inflation_curve)

    coupon = qlCappedFlooredYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        cap=0.05,
        floor=0.02,
    )
    vol_curve = qlInterpolatedYoYInflationOptionletVolatilityCurve(
        settlement_days=2,
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        lag=qPeriod.__wrapped__("3M"),
        frequency=qFrequency.__wrapped__("ANNUAL"),
        index_is_interpolated=False,
        dates=[ql.Date(1, 1, 2024), ql.Date(1, 1, 2025), ql.Date(1, 1, 2026)],
        volatilities=[0.02, 0.025, 0.03],
        min_strike=0.01,
        max_strike=0.10,
    )

    ts = qlFlatForward(reference_date, 0.03, _day_counter())
    vol_surface = vol_curve
    pricer = qlBlackYoYInflationCouponPricer(vol_surface, ts)
    qlYoYInflationCouponSetPricer(coupon, pricer)

    rate = qlCappedFlooredYoYInflationCouponRate(coupon)
    assert isinstance(rate, float)


def test_qlCappedFlooredYoYInflationCouponEffectiveCap():
    index = _yoy_inflation_index()
    coupon = qlCappedFlooredYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        cap=0.05,
        floor=0.02,
    )
    effective_cap = qlCappedFlooredYoYInflationCouponEffectiveCap(coupon)
    assert isinstance(effective_cap, float)


def test_qlCappedFlooredYoYInflationCouponEffectiveFloor():
    index = _yoy_inflation_index()
    coupon = qlCappedFlooredYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        cap=0.05,
        floor=0.02,
    )
    effective_floor = qlCappedFlooredYoYInflationCouponEffectiveFloor(coupon)
    assert isinstance(effective_floor, float)


def test_qlCappedFlooredYoYInflationCouponUnderlyingRate():
    base_index = _yoy_inflation_index()
    base_index.addFixing(ql.Date(1, 1, 2023), 100.0, forceOverwrite=True)
    base_index.addFixing(ql.Date(1, 1, 2024), 102.0, forceOverwrite=True)
    base_index.addFixing(ql.Date(1, 1, 2025), 104.0, forceOverwrite=True)

    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)
    ts_yield = qlFlatForward(reference_date, 0.03, _day_counter())
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))

    helper = qlYearOnYearInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2029),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=base_index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=ts_yield,
    )

    inflation_curve = qlPiecewiseYoYInflation(
        reference_date,
        base_date,
        0.02,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        [helper],
    )

    index = qlYoYInflationIndexClone(base_index, inflation_curve)

    coupon = qlCappedFlooredYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
        cap=0.05,
        floor=0.02,
    )

    vol_curve = qlInterpolatedYoYInflationOptionletVolatilityCurve(
        settlement_days=2,
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        lag=qPeriod.__wrapped__("3M"),
        frequency=qFrequency.__wrapped__("ANNUAL"),
        index_is_interpolated=False,
        dates=[ql.Date(1, 1, 2024), ql.Date(1, 1, 2025)],
        volatilities=[0.02, 0.025],
        min_strike=0.01,
        max_strike=0.10,
    )
    ts = qlFlatForward(reference_date, 0.03, _day_counter())
    vol_surface = vol_curve
    pricer = qlBlackYoYInflationCouponPricer(vol_surface, ts)
    qlYoYInflationCouponSetPricer(coupon, pricer)

    underlying_rate = qlCappedFlooredYoYInflationCouponUnderlyingRate(coupon)
    assert isinstance(underlying_rate, float)


# =============================================================================
# YoY Inflation Leg Tests
# =============================================================================


def test_qlYoYInflationLeg():
    index = _yoy_inflation_index()
    schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )
    leg = qlYoYInflationLeg(
        schedule=schedule,
        calendar=_calendar(),
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        notionals=[1000000.0, 1000000.0, 1000000.0, 1000000.0, 1000000.0],
        payment_day_counter=_day_counter(),
    )
    assert isinstance(leg, (ql.Leg, tuple, list))
    assert len(leg) > 0


def test_qlYoYInflationLeg_full():
    index = _yoy_inflation_index()
    schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )
    leg = qlYoYInflationLeg(
        schedule=schedule,
        calendar=_calendar(),
        index=index,
        observation_lag=qPeriod.__wrapped__("3M"),
        interpolation=qCPIInterpolationType.__wrapped__("LINEAR"),
        notionals=[1000000.0, 1000000.0, 1000000.0, 1000000.0, 1000000.0],
        payment_day_counter=_day_counter(),
        payment_convention=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        fixing_days=2,
        gearings=[1.0, 1.0, 1.0, 1.0, 1.0],
        spreads=[0.01, 0.01, 0.01, 0.01, 0.01],
        caps=[0.05, 0.05, 0.05, 0.05, 0.05],
        floors=[0.0, 0.0, 0.0, 0.0, 0.0],
    )
    assert isinstance(leg, (ql.Leg, tuple, list))
    assert len(leg) > 0


# =============================================================================
# YoY Inflation Coupon Pricer Tests
# =============================================================================


def test_qlBlackYoYInflationCouponPricer():
    vol_surface = ql.YoYOptionletVolatilitySurfaceHandle()
    ts = ql.YieldTermStructureHandle()
    pricer = qlBlackYoYInflationCouponPricer(vol_surface, ts)
    assert isinstance(pricer, ql.BlackYoYInflationCouponPricer)


def test_qlUnitDisplacedBlackYoYInflationCouponPricer():
    vol_surface = ql.YoYOptionletVolatilitySurfaceHandle()
    ts = ql.YieldTermStructureHandle()
    pricer = qlUnitDisplacedBlackYoYInflationCouponPricer(vol_surface, ts)
    assert isinstance(pricer, ql.UnitDisplacedBlackYoYInflationCouponPricer)


def test_qlBachelierYoYInflationCouponPricer():
    vol_surface = ql.YoYOptionletVolatilitySurfaceHandle()
    ts = ql.YieldTermStructureHandle()
    pricer = qlBachelierYoYInflationCouponPricer(vol_surface, ts)
    assert isinstance(pricer, ql.BachelierYoYInflationCouponPricer)


# =============================================================================
# Zero Coupon Inflation Swap Tests
# =============================================================================


def test_qlZeroCouponInflationSwap():
    index = _zero_inflation_index()
    swap = qlZeroCouponInflationSwap(
        qSwapType.__wrapped__("PAYER"),
        nominal=1000000.0,
        start=ql.Date(1, 1, 2024),
        maturity=ql.Date(1, 1, 2029),
        calendar=_calendar(),
        convention=ql.ModifiedFollowing,
        day_counter=_day_counter(),
        fixed_rate=0.02,
        index=index,
        lag=ql.Period(3, ql.Months),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
    )
    assert isinstance(swap, ql.ZeroCouponInflationSwap)
    assert qlZeroCouponInflationSwapType(swap) == "PAYER"


def test_qlZeroCouponInflationSwap2():
    index = _zero_inflation_index()
    swap = qlZeroCouponInflationSwap(
        qSwapType.__wrapped__("PAYER"),
        nominal=1000000.0,
        start=ql.Date(1, 1, 2024),
        maturity=ql.Date(1, 1, 2029),
        calendar=_calendar(),
        convention=ql.ModifiedFollowing,
        day_counter=_day_counter(),
        fixed_rate=0.02,
        index=index,
        lag=ql.Period(3, ql.Months),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        inf_convention=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
    )
    assert isinstance(swap, ql.ZeroCouponInflationSwap)
    assert qlZeroCouponInflationSwapType(swap) == "PAYER"


def test_qlZeroCouponInflationSwapFairRate():
    _set_eval_date()

    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 10, 2023), ql.Date(1, 10, 2024), ql.Date(1, 10, 2029)]
    rates = [0.02, 0.02, 0.02]

    inflation_curve = qlZeroInflationCurve(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    index = qlEUHICP(inflation_curve)
    index.addFixing(ql.Date(1, 10, 2023), 100, forceOverwrite=True)

    swap = qlZeroCouponInflationSwap(
        swap_type=qSwapType.__wrapped__("PAYER"),
        nominal=1000000.0,
        start=ql.Date(1, 1, 2024),
        maturity=ql.Date(1, 1, 2029),
        calendar=_calendar(),
        convention=ql.ModifiedFollowing,
        day_counter=_day_counter(),
        fixed_rate=0.02,
        index=index,
        lag=ql.Period(3, ql.Months),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
    )

    ts = qlFlatForward(ql.Date(1, 1, 2024), 0.03, _day_counter())
    engine = ql.DiscountingSwapEngine(ts)
    qlInstrumentSetPricingEngine(swap, engine)

    rate = qlZeroCouponInflationSwapFairRate(swap)
    assert isinstance(rate, float)


def test_qlZeroCouponInflationSwapNPV():
    _set_eval_date()

    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 10, 2023), ql.Date(1, 10, 2024), ql.Date(1, 10, 2029)]
    rates = [0.02, 0.02, 0.02]

    inflation_curve = qlZeroInflationCurve(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    index = qlEUHICP(inflation_curve)
    index.addFixing(ql.Date(1, 10, 2023), 100, forceOverwrite=True)

    swap = qlZeroCouponInflationSwap(
        swap_type=qSwapType.__wrapped__("PAYER"),
        nominal=1000000.0,
        start=ql.Date(1, 1, 2024),
        maturity=ql.Date(1, 1, 2029),
        calendar=_calendar(),
        convention=ql.ModifiedFollowing,
        day_counter=_day_counter(),
        fixed_rate=0.02,
        index=index,
        lag=ql.Period(3, ql.Months),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
    )

    ts = qlFlatForward(ql.Date(1, 1, 2024), 0.03, _day_counter())
    engine = ql.DiscountingSwapEngine(ts)
    qlInstrumentSetPricingEngine(swap, engine)

    assert isinstance(qlZeroCouponInflationSwapFixedLegNPV(swap), float)
    assert isinstance(qlZeroCouponInflationSwapInflationLegNPV(swap), float)
    assert isinstance(qlZeroCouponInflationSwapFixedLegBPS(swap), float)


def test_qlZeroCouponInflationSwapLegs():
    index = _zero_inflation_index()
    swap = qlZeroCouponInflationSwap(
        swap_type=qSwapType.__wrapped__("PAYER"),
        nominal=1000000.0,
        start=ql.Date(1, 1, 2024),
        maturity=ql.Date(1, 1, 2029),
        calendar=_calendar(),
        convention=ql.ModifiedFollowing,
        day_counter=_day_counter(),
        fixed_rate=0.02,
        index=index,
        lag=ql.Period(3, ql.Months),
        observation_interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
    )
    assert isinstance(qlZeroCouponInflationSwapFixedLeg(swap), (ql.Leg, tuple, list))
    assert isinstance(
        qlZeroCouponInflationSwapInflationLeg(swap), (ql.Leg, tuple, list)
    )


# =============================================================================
# Year On Year Inflation Swap Tests
# =============================================================================


def test_qlYearOnYearInflationSwap():
    index = _yoy_inflation_index()
    fixed_schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )
    yoy_schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )

    swap = qlYearOnYearInflationSwap(
        swap_type=qSwapType.__wrapped__("PAYER"),
        nominal=1000000.0,
        fixed_schedule=fixed_schedule,
        fixed_rate=0.02,
        fixed_day_counter=_day_counter(),
        yoy_schedule=yoy_schedule,
        index=index,
        lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        spread=0.0,
        yoy_day_counter=_day_counter(),
        payment_calendar=_calendar(),
    )
    assert isinstance(swap, ql.YearOnYearInflationSwap)


def test_qlYearOnYearInflationSwapFairRate():
    _set_eval_date()
    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 10, 2023), ql.Date(1, 10, 2024), ql.Date(1, 10, 2029)]
    rates = [0.02, 0.02, 0.02]

    inflation_curve = qlYoYInflationCurve(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    index = qlYYEUHICP(inflation_curve)
    index.addFixing(ql.Date(1, 10, 2023), 100, forceOverwrite=True)

    fixed_schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )
    yoy_schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )

    swap = qlYearOnYearInflationSwap(
        swap_type=qSwapType.__wrapped__("PAYER"),
        nominal=1000000.0,
        fixed_schedule=fixed_schedule,
        fixed_rate=0.02,
        fixed_day_counter=_day_counter(),
        yoy_schedule=yoy_schedule,
        index=index,
        lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        spread=0.0,
        yoy_day_counter=_day_counter(),
        payment_calendar=_calendar(),
    )

    ts = qlFlatForward(ql.Date(1, 1, 2024), 0.03, _day_counter())
    engine = ql.DiscountingSwapEngine(ts)
    qlInstrumentSetPricingEngine(swap, engine)

    assert isinstance(qlYearOnYearInflationSwapFairRate(swap), float)
    assert isinstance(qlYearOnYearInflationSwapFairSpread(swap), float)


def test_qlYearOnYearInflationSwapNPV():
    index = _yoy_inflation_index()
    index.addFixing(ql.Date(1, 1, 2023), 100.0, forceOverwrite=True)
    index.addFixing(ql.Date(1, 1, 2024), 102.0, forceOverwrite=True)
    index.addFixing(ql.Date(1, 1, 2025), 104.0, forceOverwrite=True)

    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)
    ts_yield = qlFlatForward(reference_date, 0.03, _day_counter())
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))

    helper = qlYearOnYearInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2029),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=ts_yield,
    )

    inflation_curve = qlPiecewiseYoYInflation(
        reference_date,
        base_date,
        0.02,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        [helper],
    )

    index_with_curve = qlYoYInflationIndexClone(index, inflation_curve)

    fixed_schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )
    yoy_schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )

    swap = qlYearOnYearInflationSwap(
        swap_type=qSwapType.__wrapped__("PAYER"),
        nominal=1000000.0,
        fixed_schedule=fixed_schedule,
        fixed_rate=0.02,
        fixed_day_counter=_day_counter(),
        yoy_schedule=yoy_schedule,
        index=index_with_curve,
        lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        spread=0.0,
        yoy_day_counter=_day_counter(),
        payment_calendar=_calendar(),
    )

    ts = qlFlatForward(ql.Date(1, 1, 2024), 0.03, _day_counter())
    engine = ql.DiscountingSwapEngine(ts)
    qlInstrumentSetPricingEngine(swap, engine)

    assert isinstance(qlYearOnYearInflationSwapFixedLegNPV(swap), float)
    assert isinstance(qlYearOnYearInflationSwapYoYLegNPV(swap), float)


def test_qlYearOnYearInflationSwapLegs():
    index = _yoy_inflation_index()
    fixed_schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )
    yoy_schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )

    swap = qlYearOnYearInflationSwap(
        swap_type=qSwapType.__wrapped__("PAYER"),
        nominal=1000000.0,
        fixed_schedule=fixed_schedule,
        fixed_rate=0.02,
        fixed_day_counter=_day_counter(),
        yoy_schedule=yoy_schedule,
        index=index,
        lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        spread=0.0,
        yoy_day_counter=_day_counter(),
        payment_calendar=_calendar(),
    )
    assert isinstance(qlYearOnYearInflationSwapFixedLeg(swap), (ql.Leg, tuple, list))
    assert isinstance(qlYearOnYearInflationSwapYoYLeg(swap), (ql.Leg, tuple, list))


# =============================================================================
# CPI Swap Tests
# =============================================================================


def test_qlCPISwap():

    fixed_schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )
    float_schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(6, ql.Months)
    )
    float_index = qlUSDLibor(ql.Period(6, ql.Months))

    swap = qlCPISwap(
        swap_type=qSwapType.__wrapped__("PAYER"),
        nominal=1000000.0,
        subtract_inflation_nominal=True,
        spread=0.0,
        float_day_count=_day_counter(),
        float_schedule=float_schedule,
        float_roll=ql.ModifiedFollowing,
        fixing_days=2,
        float_index=float_index,
        fixed_rate=0.02,
        base_cpi=100.0,
        fixed_day_count=_day_counter(),
        fixed_schedule=fixed_schedule,
        fixed_roll=ql.ModifiedFollowing,
        observation_lag=ql.Period(3, ql.Months),
        fixed_index=_zero_inflation_index(),
    )
    assert isinstance(swap, ql.CPISwap)


def test_qlCPISwap_getters():
    _set_eval_date()
    fixed_schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )
    float_schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(6, ql.Months)
    )
    libor_ts = qlFlatForward(
        ql.Date(1, 1, 2024), 0.03, qDayCounter.__wrapped__("ACTUAL360")
    )

    float_index = ql.IborIndex(
        "USDLibor6M",
        ql.Period(6, ql.Months),
        2,
        _currency(),
        _calendar(),
        qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        False,
        qDayCounter.__wrapped__("ACTUAL360"),
        libor_ts,
    )
    float_index.addFixing(ql.Date(28, 12, 2023), 0.03, forceOverwrite=True)

    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 10, 2023), ql.Date(1, 10, 2024), ql.Date(1, 10, 2029)]
    rates = [0.02, 0.02, 0.02]

    inflation_curve = qlZeroInflationCurve(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    index = qlEUHICP(inflation_curve)
    index.addFixing(ql.Date(1, 10, 2023), 100, forceOverwrite=True)

    swap = qlCPISwap(
        swap_type=qSwapType.__wrapped__("PAYER"),
        nominal=1000000.0,
        subtract_inflation_nominal=True,
        spread=0.0,
        float_day_count=qDayCounter.__wrapped__("ACTUAL360"),
        float_schedule=float_schedule,
        float_roll=ql.ModifiedFollowing,
        fixing_days=2,
        float_index=float_index,
        fixed_rate=0.02,
        base_cpi=100.0,
        fixed_day_count=_day_counter(),
        fixed_schedule=fixed_schedule,
        fixed_roll=ql.ModifiedFollowing,
        observation_lag=ql.Period(3, ql.Months),
        fixed_index=index,
    )

    ts = qlFlatForward(ql.Date(1, 1, 2024), 0.03, _day_counter())
    engine = ql.DiscountingSwapEngine(ts)
    qlInstrumentSetPricingEngine(swap, engine)

    assert isinstance(qlCPISwapFairRate(swap), float)
    assert isinstance(qlCPISwapFairSpread(swap), float)
    assert isinstance(qlCPISwapFloatLegNPV(swap), float)
    assert isinstance(qlCPISwapFixedLegNPV(swap), float)
    assert isinstance(qlCPISwapCPILeg(swap), (ql.Leg, tuple, list))
    assert isinstance(qlCPISwapFloatLeg(swap), (ql.Leg, tuple, list))


# =============================================================================
# YoY Inflation Cap Floor Tests
# =============================================================================


def test_qlYoYInflationCapFloor():
    index = _yoy_inflation_index()
    schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )

    leg = qlYoYInflationLeg(
        schedule,
        _calendar(),
        index,
        ql.Period(3, ql.Months),
        qCPIInterpolationType.__wrapped__("ASINDEX"),
        [1000000.0],
        _day_counter(),
    )

    capfloor = qlYoYInflationCapFloor(
        capfloor_type=qYoYInflationCapFloorType.__wrapped__("CAP"),
        yoy_leg=leg,
        strikes=[0.03, 0.04, 0.05],
    )
    assert isinstance(capfloor, ql.YoYInflationCapFloor)


def test_qlYoYInflationCapFloorImpliedVolatility():
    index = _yoy_inflation_index()
    schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )

    leg = qlYoYInflationLeg(
        schedule,
        _calendar(),
        index,
        ql.Period(3, ql.Months),
        qCPIInterpolationType.__wrapped__("ASINDEX"),
        [1000000.0],
        _day_counter(),
    )

    capfloor = qlYoYInflationCapFloor(
        capfloor_type=qYoYInflationCapFloorType.__wrapped__("CAP"),
        yoy_leg=leg,
        strikes=[0.03, 0.04, 0.05],
    )
    curve = ql.YoYInflationTermStructureHandle()

    with pytest.raises(RuntimeError) as exc_info:
        qlYoYInflationCapFloorImpliedVolatility(
            capfloor,
            price=0.01,
            curve=curve,
            guess=0.02,
        )
    assert str(exc_info.value) == "not implemented yet"


def test_qlYoYInflationCapFloorOptionletPrices():
    base_index = _yoy_inflation_index()
    base_index.addFixing(ql.Date(1, 1, 2023), 100.0, forceOverwrite=True)
    base_index.addFixing(ql.Date(1, 1, 2024), 102.0, forceOverwrite=True)
    base_index.addFixing(ql.Date(1, 1, 2025), 104.0, forceOverwrite=True)

    reference_date = ql.Date(1, 1, 2024)
    ts_yield = qlFlatForward(reference_date, 0.03, _day_counter())
    quote = ql.QuoteHandle(ql.SimpleQuote(0.02))

    helper = qlYearOnYearInflationSwapHelper(
        quote=quote,
        lag=qPeriod.__wrapped__("3M"),
        maturity=ql.Date(1, 1, 2029),
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        index=base_index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=ts_yield,
    )

    inflation_curve = qlPiecewiseYoYInflation(
        reference_date,
        reference_date,
        0.02,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        [helper],
    )

    index = qlYoYInflationIndexClone(base_index, inflation_curve)

    schedule = _schedule(
        ql.Date(1, 1, 2024), ql.Date(1, 1, 2029), ql.Period(1, ql.Years)
    )

    leg = qlYoYInflationLeg(
        schedule,
        _calendar(),
        index,
        ql.Period(3, ql.Months),
        qCPIInterpolationType.__wrapped__("ASINDEX"),
        [1000000.0],
        _day_counter(),
    )

    capfloor = qlYoYInflationCapFloor(
        capfloor_type=qYoYInflationCapFloorType.__wrapped__("CAP"),
        yoy_leg=leg,
        strikes=[0.03, 0.04, 0.05],
    )

    vol_curve = qlInterpolatedYoYInflationOptionletVolatilityCurve(
        settlement_days=2,
        calendar=_calendar(),
        bdc=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        day_counter=_day_counter(),
        lag=qPeriod.__wrapped__("3M"),
        frequency=qFrequency.__wrapped__("ANNUAL"),
        index_is_interpolated=False,
        dates=[
            ql.Date(1, 1, 2024),
            ql.Date(1, 1, 2025),
            ql.Date(1, 1, 2026),
            ql.Date(1, 1, 2027),
            ql.Date(1, 1, 2028),
            ql.Date(1, 1, 2029),
        ],
        volatilities=[0.02, 0.022, 0.024, 0.026, 0.028, 0.03],
        min_strike=0.01,
        max_strike=0.10,
    )
    vol_surface = vol_curve

    ts = qlFlatForward(ql.Date(1, 1, 2024), 0.03, _day_counter())

    engine = qlYoYInflationBlackCapFloorEngine(index, vol_surface, ts)
    qlInstrumentSetPricingEngine(capfloor, engine)

    prices = qlYoYInflationCapFloorOptionletPrices(capfloor)
    assert isinstance(prices, tuple)


# =============================================================================
# YoY Inflation Cap/Floor/Collar Tests
# =============================================================================


def test_qlYoYInflationCap():

    index = _yoy_inflation_index()
    coupon = qlYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
    )

    cap = qlYoYInflationCap([coupon], [0.05])
    assert isinstance(cap, ql.YoYInflationCap)


def test_qlYoYInflationFloor():

    index = _yoy_inflation_index()
    coupon = qlYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
    )

    floor = qlYoYInflationFloor([coupon], [0.02])
    assert isinstance(floor, ql.YoYInflationFloor)


def test_qlYoYInflationCollar():

    index = _yoy_inflation_index()
    coupon = qlYoYInflationCoupon(
        payment_date=ql.Date(1, 1, 2025),
        nominal=1000.0,
        start_date=ql.Date(1, 1, 2024),
        end_date=ql.Date(1, 1, 2025),
        fixing_days=0,
        index=index,
        observation_lag=ql.Period(3, ql.Months),
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        day_counter=_day_counter(),
    )

    collar = qlYoYInflationCollar([coupon], [0.05], [0.02])
    assert isinstance(collar, ql.YoYInflationCollar)


# =============================================================================
# Interpolated Zero Inflation Curve Tests
# =============================================================================


def test_qlZeroInflationCurve():
    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 1, 2024), ql.Date(1, 1, 2025), ql.Date(1, 1, 2026)]
    rates = [0.01, 0.02, 0.03]

    curve = qlZeroInflationCurveAsIts(
        reference_date,
        dates,
        rates,
        ql.Semiannual,
        _day_counter(),
    )
    assert isinstance(curve, ql.ZeroInflationTermStructure)
    assert isinstance(qlZeroInflationCurveDates(curve), tuple)
    assert isinstance(qlZeroInflationCurveTimes(curve), tuple)
    assert isinstance(qlZeroInflationCurveData(curve), tuple)
    assert isinstance(qlZeroInflationCurveRates(curve), tuple)
    nodes = qlZeroInflationCurveNodes(curve)
    assert isinstance(nodes, tuple)
    assert len(nodes) > 0
    first_node = nodes[0]
    assert len(first_node) == 2
    assert isinstance(first_node[0], ql.Date)
    assert isinstance(first_node[1], (float, int))


def test_qlZeroInflationCurve_with_seasonality():
    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)

    factors = [1.0, 1.02, 1.01, 1.03]
    seasonality = qlMultiplicativePriceSeasonality(
        base_date, qFrequency.__wrapped__("QUARTERLY"), factors
    )

    dates = [ql.Date(1, 1, 2024), ql.Date(1, 1, 2025), ql.Date(1, 1, 2026)]
    rates = [0.01, 0.02, 0.03]

    curve = qlZeroInflationCurveAsIts(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        seasonality=seasonality,
    )

    assert isinstance(curve, ql.ZeroInflationTermStructure)
    assert qlInflationTermStructureHasSeasonality(curve) is True
    assert isinstance(qlInflationTermStructureSeasonality(curve), ql.Seasonality)
    assert isinstance(qlZeroInflationCurveDates(curve), tuple)
    assert isinstance(qlZeroInflationCurveTimes(curve), tuple)
    assert isinstance(qlZeroInflationCurveData(curve), tuple)
    assert isinstance(qlZeroInflationCurveRates(curve), tuple)
    nodes = qlZeroInflationCurveNodes(curve)
    assert len(nodes) > 0
    first_node = nodes[0]
    assert len(first_node) == 2
    assert isinstance(first_node[0], ql.Date)
    assert isinstance(first_node[1], (float, int))


# =============================================================================
# Interpolated YoY Inflation Curve Tests
# =============================================================================


def test_qlYoYInflationCurve():
    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 1, 2024), ql.Date(1, 1, 2025), ql.Date(1, 1, 2026)]
    rates = [0.01, 0.02, 0.03]

    curve = qlYoYInflationCurveAsIts(
        reference_date,
        dates,
        rates,
        ql.Semiannual,
        _day_counter(),
    )
    assert isinstance(curve, ql.YoYInflationTermStructure)
    assert isinstance(qlYoYInflationCurveDates(curve), tuple)
    assert isinstance(qlYoYInflationCurveTimes(curve), tuple)
    assert isinstance(qlYoYInflationCurveData(curve), tuple)
    assert isinstance(qlYoYInflationCurveRates(curve), tuple)
    nodes = qlYoYInflationCurveNodes(curve)
    assert isinstance(nodes, tuple)
    assert len(nodes) > 0
    first_node = nodes[0]
    assert len(first_node) == 2
    assert isinstance(first_node[0], ql.Date)
    assert isinstance(first_node[1], (float, int))


def test_qlYoYInflationCurve_with_seasonality():
    reference_date = ql.Date(1, 1, 2024)
    base_date = ql.Date(1, 1, 2024)

    factors = [1.0, 1.02, 1.01, 1.03]
    seasonality = qlMultiplicativePriceSeasonality(
        base_date, qFrequency.__wrapped__("QUARTERLY"), factors
    )

    dates = [ql.Date(1, 1, 2024), ql.Date(1, 1, 2025), ql.Date(1, 1, 2026)]
    rates = [0.01, 0.02, 0.03]

    curve = qlYoYInflationCurveAsIts(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
        seasonality=seasonality,
    )

    assert isinstance(curve, ql.YoYInflationTermStructure)
    assert qlInflationTermStructureHasSeasonality(curve) is True
    assert isinstance(qlInflationTermStructureSeasonality(curve), ql.Seasonality)
    assert isinstance(qlYoYInflationCurveDates(curve), tuple)
    assert isinstance(qlYoYInflationCurveTimes(curve), tuple)
    assert isinstance(qlYoYInflationCurveData(curve), tuple)
    assert isinstance(qlYoYInflationCurveRates(curve), tuple)
    nodes = qlYoYInflationCurveNodes(curve)
    assert len(nodes) > 0
    first_node = nodes[0]
    assert len(first_node) == 2
    assert isinstance(first_node[0], ql.Date)
    assert isinstance(first_node[1], (float, int))


# =============================================================================
# YoY Cap/Floor Term Price Surface Tests
# =============================================================================


def test_qlYoYCapFloorTermPriceSurface_creation():

    settlement_days = 2
    calendar = _calendar()
    bdc = qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING")
    day_counter = _day_counter()
    lag = qPeriod.__wrapped__("3M")
    frequency = qFrequency.__wrapped__("ANNUAL")

    dates = [ql.Date(1, 1, 2024), ql.Date(1, 1, 2025)]
    volatilities = [0.02, 0.03]

    surface = qlInterpolatedYoYInflationOptionletVolatilityCurve(
        settlement_days=settlement_days,
        calendar=calendar,
        bdc=bdc,
        day_counter=day_counter,
        lag=lag,
        frequency=frequency,
        index_is_interpolated=False,
        dates=dates,
        volatilities=volatilities,
        min_strike=0.01,
        max_strike=0.10,
    )
    assert isinstance(surface, ql.YoYOptionletVolatilitySurfaceHandle)


def test_qlYoYCapFloorTermPriceSurface_getters():
    ql.Settings.instance().evaluationDate = ql.Date(1, 1, 2024)

    reference_date = ql.Date(1, 1, 2024)
    calendar = _calendar()
    day_counter = _day_counter()
    bdc = qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING")
    lag = qPeriod.__wrapped__("3M")
    nominal_ts = qlFlatForward(reference_date, 0.03, day_counter)

    index = _yoy_inflation_index()

    cap_floor_surface = qlYoYInflationCapFloorTermPriceSurface(
        fixing_days=2,
        yoy_lag=lag,
        yoy_index=index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        nominal_term_structure=nominal_ts,
        day_counter=day_counter,
        calendar=calendar,
        business_day_convention=bdc,
        cap_strikes=[0.02, 0.03, 0.04, 0.05],
        floor_strikes=[0.02, 0.03, 0.04, 0.05],
        maturities=[
            qPeriod.__wrapped__("1Y"),
            qPeriod.__wrapped__("2Y"),
            qPeriod.__wrapped__("3Y"),
            qPeriod.__wrapped__("5Y"),
        ],
        cap_prices=[
            [0.012, 0.018, 0.025, 0.035],
            [0.010, 0.015, 0.020, 0.030],
            [0.008, 0.012, 0.015, 0.025],
            [0.006, 0.009, 0.012, 0.020],
        ],
        floor_prices=[
            [0.005, 0.008, 0.012, 0.018],
            [0.007, 0.010, 0.015, 0.022],
            [0.009, 0.013, 0.018, 0.025],
            [0.012, 0.016, 0.020, 0.030],
        ],
    )

    assert isinstance(cap_floor_surface, ql.YoYCapFloorTermPriceSurface)
    rate = qlYoYCapFloorTermPriceSurfaceAtmYoYRate(
        cap_floor_surface, ql.Date(1, 1, 2024)
    )
    assert isinstance(rate, float)
    period_1y = qPeriod.__wrapped__("1Y")
    rate_1y = qlYoYCapFloorTermPriceSurfaceAtmYoYRate2(
        cap_floor_surface, period_1y, lag, extrapolate=True
    )
    assert isinstance(rate_1y, float)
    period_2y = qPeriod.__wrapped__("2Y")
    rate_2y = qlYoYCapFloorTermPriceSurfaceAtmYoYRate2(
        cap_floor_surface, period_2y, lag, extrapolate=True
    )
    assert isinstance(rate_2y, float)
    rate_no_extrap = qlYoYCapFloorTermPriceSurfaceAtmYoYRate2(
        cap_floor_surface, period_1y, lag, extrapolate=False
    )
    assert isinstance(rate_no_extrap, float)
    time_rates = qlYoYCapFloorTermPriceSurfaceAtmYoYSwapTimeRates(cap_floor_surface)
    assert isinstance(time_rates, tuple)
    assert len(time_rates) == 2
    assert len(time_rates[0]) > 0
    assert len(time_rates[1]) > 0
    date_rates = qlYoYCapFloorTermPriceSurfaceAtmYoYSwapDateRates(cap_floor_surface)
    test_date = ql.Date(1, 1, 2025)
    swap_rate = qlYoYCapFloorTermPriceSurfaceAtmYoYSwapRate(
        cap_floor_surface, test_date, extrapolate=True
    )
    assert isinstance(swap_rate, float)
    test_period = qPeriod.__wrapped__("2Y")
    swap_rate2 = qlYoYCapFloorTermPriceSurfaceAtmYoYSwapRate2(
        cap_floor_surface, test_period, extrapolate=True
    )
    assert isinstance(swap_rate2, float)
    base_date = qlYoYCapFloorTermPriceSurfaceBaseDate(cap_floor_surface)
    assert isinstance(base_date, ql.Date)
    bdc_result = qlYoYCapFloorTermPriceSurfaceBusinessDayConvention(cap_floor_surface)
    assert bdc_result == "MODIFIEDFOLLOWING"
    test_date_cap = ql.Date(1, 1, 2025)
    test_strike_cap = 0.03
    cap_price = qlYoYCapFloorTermPriceSurfaceCapPrice(
        cap_floor_surface, test_date_cap, test_strike_cap
    )
    assert isinstance(cap_price, float)
    test_period_cap = qPeriod.__wrapped__("1Y")
    cap_price2 = qlYoYCapFloorTermPriceSurfaceCapPrice2(
        cap_floor_surface, test_period_cap, test_strike_cap
    )
    assert isinstance(cap_price2, float)
    floor_price = qlYoYCapFloorTermPriceSurfaceFloorPrice(
        cap_floor_surface, test_date_cap, test_strike_cap
    )
    assert isinstance(floor_price, float)
    floor_price2 = qlYoYCapFloorTermPriceSurfaceFloorPrice2(
        cap_floor_surface, test_period_cap, test_strike_cap
    )
    assert isinstance(floor_price2, float)
    price = qlYoYCapFloorTermPriceSurfacePrice(
        cap_floor_surface, test_date_cap, test_strike_cap
    )
    assert isinstance(price, float)
    price2 = qlYoYCapFloorTermPriceSurfacePrice2(
        cap_floor_surface, test_period_cap, test_strike_cap
    )
    assert isinstance(price2, float)
    yoy_ts = qlYoYCapFloorTermPriceSurfaceYoYTS(cap_floor_surface)
    assert isinstance(yoy_ts, ql.YoYInflationTermStructure)
    yoy_index = qlYoYCapFloorTermPriceSurfaceYoYIndex(cap_floor_surface)
    assert isinstance(yoy_index, ql.YoYInflationIndex)
    observation_lag = qlYoYCapFloorTermPriceSurfaceObservationLag(cap_floor_surface)
    assert isinstance(observation_lag, ql.Period)
    assert observation_lag == lag
    frequency = qlYoYCapFloorTermPriceSurfaceFrequency(cap_floor_surface)
    assert frequency == "ANNUAL"
    fixing_days = qlYoYCapFloorTermPriceSurfaceFixingDays(cap_floor_surface)
    assert isinstance(fixing_days, int)
    assert fixing_days == 2
    strikes = qlYoYCapFloorTermPriceSurfaceStrikes(cap_floor_surface)
    assert isinstance(strikes, tuple)
    assert len(strikes) > 0
    cap_strikes = qlYoYCapFloorTermPriceSurfaceCapStrikes(cap_floor_surface)
    assert isinstance(cap_strikes, tuple)
    assert len(cap_strikes) > 0
    floor_strikes = qlYoYCapFloorTermPriceSurfaceFloorStrikes(cap_floor_surface)
    assert isinstance(floor_strikes, tuple)
    assert len(floor_strikes) > 0
    maturities = qlYoYCapFloorTermPriceSurfaceMaturities(cap_floor_surface)
    assert isinstance(maturities, tuple)
    assert len(maturities) > 0
    min_strike = qlYoYCapFloorTermPriceSurfaceMinStrike(cap_floor_surface)
    assert isinstance(min_strike, float)
    max_strike = qlYoYCapFloorTermPriceSurfaceMaxStrike(cap_floor_surface)
    assert isinstance(max_strike, float)
    min_maturity = qlYoYCapFloorTermPriceSurfaceMinMaturity(cap_floor_surface)
    assert isinstance(min_maturity, ql.Date)
    max_maturity = qlYoYCapFloorTermPriceSurfaceMaxMaturity(cap_floor_surface)
    assert isinstance(max_maturity, ql.Date)
    option_date = qlYoYCapFloorTermPriceSurfaceYoyOptionDateFromTenor(
        cap_floor_surface, test_period_cap
    )
    assert isinstance(option_date, ql.Date)


# =============================================================================
# YoY Inflation Cap Floor Engine Tests
# =============================================================================


def test_qlYoYInflationBlackCapFloorEngine():
    index = _yoy_inflation_index()
    vol_surface = ql.YoYOptionletVolatilitySurfaceHandle()
    ts = ql.YieldTermStructureHandle()
    engine = qlYoYInflationBlackCapFloorEngine(index, vol_surface, ts)
    assert isinstance(engine, ql.YoYInflationBlackCapFloorEngine)


def test_qlYoYInflationUnitDisplacedBlackCapFloorEngine():
    index = _yoy_inflation_index()
    vol_surface = ql.YoYOptionletVolatilitySurfaceHandle()
    ts = ql.YieldTermStructureHandle()
    engine = qlYoYInflationUnitDisplacedBlackCapFloorEngine(index, vol_surface, ts)
    assert isinstance(engine, ql.YoYInflationUnitDisplacedBlackCapFloorEngine)


def test_qlYoYInflationBachelierCapFloorEngine():
    index = _yoy_inflation_index()
    vol_surface = ql.YoYOptionletVolatilitySurfaceHandle()
    ts = ql.YieldTermStructureHandle()
    engine = qlYoYInflationBachelierCapFloorEngine(index, vol_surface, ts)
    assert isinstance(engine, ql.YoYInflationBachelierCapFloorEngine)


# =============================================================================
# YoY Optionlet Helper Tests
# =============================================================================


def test_qlYoYOptionletHelper():

    price = ql.QuoteHandle(ql.SimpleQuote(0.01))
    index = _yoy_inflation_index()
    vol_surface = ql.YoYOptionletVolatilitySurfaceHandle()
    ts = ql.YieldTermStructureHandle()
    engine = qlYoYInflationBlackCapFloorEngine(index, vol_surface, ts)

    helper = qlYoYOptionletHelper(
        price=price,
        notional=1000000.0,
        cap_floor_type=qYoYInflationCapFloorType.__wrapped__("CAP"),
        lag=qPeriod.__wrapped__("3M"),
        yoy_day_counter=_day_counter(),
        payment_calendar=_calendar(),
        fixing_days=0,
        index=index,
        interpolation=qCPIInterpolationType.__wrapped__("ASINDEX"),
        strike=0.03,
        n=5,
        pricer=engine,
    )
    assert isinstance(helper, ql.YoYOptionletHelper)


# =============================================================================
# YoY Optionlet Stripper Tests
# =============================================================================


def test_qlYoYOptionletStripper():
    stripper = qlInterpolatedYoYInflationOptionletStripper()
    assert isinstance(stripper, ql.InterpolatedYoYInflationOptionletStripper)


# =============================================================================
# Interpolated YoY Optionlet Volatility Curve Tests
# =============================================================================


def test_qlInterpolatedYoYInflationOptionletVolatilityCurve():
    settlement_days = 2
    calendar = _calendar()
    bdc = ql.ModifiedFollowing
    day_counter = _day_counter()
    lag = ql.Period(3, ql.Months)
    frequency = ql.Annual

    dates = [ql.Date(1, 1, 2024), ql.Date(1, 1, 2025)]
    volatilities = [0.02, 0.03]

    curve = qlInterpolatedYoYInflationOptionletVolatilityCurve(
        settlement_days=settlement_days,
        calendar=calendar,
        bdc=bdc,
        day_counter=day_counter,
        lag=lag,
        frequency=frequency,
        index_is_interpolated=False,
        dates=dates,
        volatilities=volatilities,
        min_strike=0.01,
        max_strike=0.10,
    )
    assert isinstance(curve, ql.YoYOptionletVolatilitySurfaceHandle)


def test_qlYoYInflationCapFloorTermPriceSurface():

    reference_date = ql.Date(1, 1, 2024)
    calendar = _calendar()
    day_counter = _day_counter()
    bdc = qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING")

    yoy_index = _yoy_inflation_index()
    yoy_index.addFixing(ql.Date(1, 1, 2023), 100.0, forceOverwrite=True)
    yoy_index.addFixing(ql.Date(1, 1, 2024), 102.0, forceOverwrite=True)

    nominal_ts = qlFlatForward(reference_date, 0.03, day_counter)

    fixing_days = 2
    yoy_lag = qPeriod.__wrapped__("3M")
    interpolation = qCPIInterpolationType.__wrapped__("ASINDEX")

    cap_strikes = [0.02, 0.03, 0.04, 0.05]
    floor_strikes = [0.02, 0.03, 0.04, 0.05]

    maturities = [
        qPeriod.__wrapped__("1Y"),
        qPeriod.__wrapped__("2Y"),
        qPeriod.__wrapped__("3Y"),
        qPeriod.__wrapped__("5Y"),
    ]

    cap_prices = [
        [0.012, 0.018, 0.025, 0.035],  # Strike 0.02
        [0.010, 0.015, 0.020, 0.030],  # Strike 0.03
        [0.008, 0.012, 0.015, 0.025],  # Strike 0.04
        [0.006, 0.009, 0.012, 0.020],  # Strike 0.05
    ]

    floor_prices = [
        [0.005, 0.008, 0.012, 0.018],  # Strike 0.02
        [0.007, 0.010, 0.015, 0.022],  # Strike 0.03
        [0.009, 0.013, 0.018, 0.025],  # Strike 0.04
        [0.012, 0.016, 0.020, 0.030],  # Strike 0.05
    ]

    surface = qlYoYInflationCapFloorTermPriceSurface(
        fixing_days=fixing_days,
        yoy_lag=yoy_lag,
        yoy_index=yoy_index,
        interpolation=interpolation,
        nominal_term_structure=nominal_ts,
        day_counter=day_counter,
        calendar=calendar,
        business_day_convention=bdc,
        cap_strikes=cap_strikes,
        floor_strikes=floor_strikes,
        maturities=maturities,
        cap_prices=cap_prices,
        floor_prices=floor_prices,
    )

    assert isinstance(surface, ql.YoYCapFloorTermPriceSurface)


def test_zero_inflation_index_with_termstructure():
    ql.Settings.instance().evaluationDate = ql.Date(1, 1, 2024)
    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 1, 2024), ql.Date(1, 1, 2025), ql.Date(1, 1, 2026)]
    rates = [0.01, 0.02, 0.03]

    curve = qlZeroInflationCurve(
        reference_date,
        dates,
        rates,
        ql.Semiannual,
        _day_counter(),
    )

    index = qlZeroInflationIndex(
        "TEST-ZERO",
        _region(),
        False,
        qFrequency.__wrapped__("ANNUAL"),
        qPeriod.__wrapped__("3M"),
        _currency(),
        curve,
    )
    index.addFixing(ql.Date(1, 1, 2024), 100.0, forceOverwrite=True)

    assert isinstance(index, ql.ZeroInflationIndex)


def test_qlZeroInflationIndexClone():
    reference_date = ql.Date(1, 1, 2024)

    original_dates = [ql.Date(1, 10, 2023), ql.Date(1, 10, 2024), ql.Date(1, 10, 2025)]
    original_rates = [0.02, 0.025, 0.03]

    original_curve = qlZeroInflationCurve(
        reference_date,
        original_dates,
        original_rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    original_index = qlZeroInflationIndex(
        "ORIGINAL-TEST",
        _region(),
        False,
        qFrequency.__wrapped__("ANNUAL"),
        qPeriod.__wrapped__("3M"),
        _currency(),
        original_curve,
    )
    original_index.addFixing(ql.Date(1, 10, 2023), 100.0, forceOverwrite=True)

    new_dates = [ql.Date(1, 1, 2024), ql.Date(1, 1, 2025), ql.Date(1, 1, 2026)]
    new_rates = [0.015, 0.02, 0.025]

    new_curve = qlZeroInflationCurve(
        reference_date,
        new_dates,
        new_rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    cloned_index = qlZeroInflationIndexClone(original_index, new_curve)

    assert isinstance(cloned_index, ql.ZeroInflationIndex)
    assert qlInflationIndexFamilyName(cloned_index) == "ORIGINAL-TEST"
    assert qlInflationIndexFrequency(cloned_index) == "ANNUAL"
    assert qlInflationIndexCurrency(cloned_index) == _currency()

    cloned_ts = qlZeroInflationIndexZeroInflationTermStructure(cloned_index)
    assert isinstance(cloned_ts, ql.ZeroInflationTermStructureHandle)


def test_qlZeroInflationTermStructureHandle():
    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 1, 2024), ql.Date(1, 1, 2025), ql.Date(1, 1, 2026)]
    rates = [0.01, 0.02, 0.03]

    curve = qlZeroInflationCurveAsIts(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    curve_handle = qlZeroInflationTermStructureHandle(curve)

    assert isinstance(curve_handle, ql.ZeroInflationTermStructureHandle)
    test_date = ql.Date(1, 6, 2024)
    rate = qlZeroInflationTermStructureZeroRate(curve_handle, test_date)
    assert isinstance(rate, float)


def test_qlYoYInflationTermStructureHandle():
    reference_date = ql.Date(1, 1, 2024)
    dates = [ql.Date(1, 1, 2024), ql.Date(1, 1, 2025), ql.Date(1, 1, 2026)]
    rates = [0.01, 0.02, 0.03]

    curve = qlYoYInflationCurveAsIts(
        reference_date,
        dates,
        rates,
        qFrequency.__wrapped__("ANNUAL"),
        _day_counter(),
    )

    curve_handle = qlYoYInflationTermStructureHandle(curve)

    assert isinstance(curve_handle, ql.YoYInflationTermStructureHandle)
    test_date = ql.Date(1, 6, 2024)
    rate = qlYoYInflationTermStructureYoYRate(curve_handle, test_date)
    assert isinstance(rate, float)
