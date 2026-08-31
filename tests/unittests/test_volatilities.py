import pytest
import QuantLib as ql

from quantlib_xloil.volatilities import (
    qlBlackConstantVol,
    qlBlackVolTermStructureBlackForwardVariance,
    qlBlackVolTermStructureBlackForwardVarianceFromTime,
    qlBlackVolTermStructureBlackForwardVol,
    qlBlackVolTermStructureBlackForwardVolFromTime,
    qlBlackVolTermStructureBlackVariance,
    qlBlackVolTermStructureBlackVarianceFromTime,
    qlBlackVolTermStructureBlackVol,
    qlBlackVarianceCurve,
    qlBlackVarianceSurface,
    qlBlackVolTermStructureBlackVolFromTime,
    qlBlackVolTermStructureMaxStrike,
    qlBlackVolTermStructureMinStrike,
    qlConstantOptionletVolatility,
    qlConstantYoYOptionletVolatility,
    qlConstantSwaptionVolatility,
    qlCubicInterpolatedSmileSection,
    qlLocalVolTermStructureLocalVol,
    qlLocalVolTermStructureLocalVolFromTime,
    qlLinearInterpolatedSmileSection,
    qlMonotonicCubicInterpolatedSmileSection,
    qlOptionletVolatilityStructureBlackVariance,
    qlOptionletVolatilityStructureBlackVarianceFromTime,
    qlOptionletVolatilityStructureVolatility,
    qlOptionletVolatilityStructureVolatilityFromTime,
    qlSwaptionVolatilityStructureBlackVariance,
    qlSwaptionVolatilityStructureBlackVarianceFromTime,
    qlSwaptionVolatilityStructureOptionDateFromTenor,
    qlSwaptionVolatilityStructureShift,
    qlSwaptionVolatilityStructureShiftFromTime,
    qlSwaptionVolatilityStructureSmileSection,
    qlSwaptionVolatilityStructureSmileSectionFromTime,
    qlSwaptionVolatilityStructureVolatility,
    qlSwaptionVolatilityStructureVolatilityFromTime,
    qlSwaptionVolatilityMatrix,
    qlSabrFlochKennedyVolatility,
    qlSabrGuess,
    qlSABRInterpolation,
    qlSABRInterpolationAlpha,
    qlSABRInterpolationBeta,
    qlSABRInterpolationNu,
    qlSABRInterpolationRho,
    qlSABRInterpolationValue,
    qlSabrSmileSection,
    qlSabrSmileSectionFromTime,
    qlSabrVolatility,
    qlShiftedSabrVolatility,
    qlSviSmileSection,
    qlSviSmileSectionFromTime,
    qlSviInterpolatedSmileSection,
    qlSviInterpolatedSmileSectionA,
    qlSviInterpolatedSmileSectionB,
    qlSviInterpolatedSmileSectionM,
    qlSviInterpolatedSmileSectionRho,
    qlSviInterpolatedSmileSectionSigma,
    qlZabrFullFdSmileSection,
    qlZabrLocalVolatilitySmileSection,
    qlZabrShortMaturityLognormalSmileSection,
    qlZabrShortMaturityNormalSmileSection,
    qlSplineCubicInterpolatedSmileSection,
    qlFlatSmileSection,
    qlFlatSmileSectionFromTime,
    qlHestonBlackVolSurface,
    qlKahaleSmileSection,
    qlNoArbSabrSmileSection,
    qlNoArbSabrSmileSectionFromTime,
    qlNoArbSabrInterpolatedSmileSection,
    qlNoArbSabrInterpolatedSmileSectionAlpha,
    qlNoArbSabrInterpolatedSmileSectionBeta,
    qlNoArbSabrInterpolatedSmileSectionNu,
    qlNoArbSabrInterpolatedSmileSectionRho,
    qlPiecewiseBlackVarianceSurfaceFromGrid,
    qlSmileSectionAtmLevel,
    qlSmileSectionDensity,
    qlSmileSectionDigitalOptionPrice,
    qlSmileSectionExerciseDate,
    qlSmileSectionExerciseTime,
    qlSmileSectionMaxStrike,
    qlSmileSectionMinStrike,
    qlSmileSectionOptionPrice,
    qlSmileSectionShift,
    qlSmileSectionVariance,
    qlSmileSectionVega,
    qlSmileSectionVolatility,
    qlSmileSectionVolatilityType,
    qlSpreadedSwaptionVolatility,
    qBlackVarianceSurfaceExtrapolation,
    qVolatilityType,
)
from quantlib_xloil.calendars import qBusinessDayConvention, qlCalendar
from quantlib_xloil.date import qlDate, qlPeriod
from quantlib_xloil.daycounters import qlDayCounter, qlDayCounterYearFraction
from quantlib_xloil.ratehelpers import qQuoteHandle


def _constant_vol_handle(volatility: float = 0.20):
    return qlBlackConstantVol(
        qlDate(2024, 1, 2),
        qlCalendar("TARGET"),
        volatility,
        qlDayCounter("ACTUAL365FIXED"),
    )


def test_qlBlackConstantVol_creates_handle_with_valid_strike_range():
    handle = _constant_vol_handle()

    min_strike = qlBlackVolTermStructureMinStrike(handle)
    max_strike = qlBlackVolTermStructureMaxStrike(handle)

    assert min_strike < max_strike


def test_qlBlackVolTermStructure_black_vol_is_constant_for_date_and_time():
    volatility = 0.20
    strike = 100.0
    handle = _constant_vol_handle(volatility)

    by_date = qlBlackVolTermStructureBlackVol(handle, qlDate(2024, 7, 2), strike)
    by_time = qlBlackVolTermStructureBlackVolFromTime(handle, 0.5, strike)

    assert by_date == pytest.approx(volatility)
    assert by_time == pytest.approx(volatility)


def test_qlBlackVolTermStructure_black_variance_for_time_and_date():
    volatility = 0.20
    strike = 100.0
    handle = _constant_vol_handle(volatility)
    day_counter = qlDayCounter("ACTUAL365FIXED")
    reference_date = qlDate(2024, 1, 2)
    expiry_date = qlDate(2025, 1, 2)

    t = 2.0
    variance_by_time = qlBlackVolTermStructureBlackVarianceFromTime(handle, t, strike)
    variance_by_date = qlBlackVolTermStructureBlackVariance(handle, expiry_date, strike)
    expected_t_date = qlDayCounterYearFraction(day_counter, reference_date, expiry_date)

    assert variance_by_time == pytest.approx((volatility * volatility) * t)
    assert variance_by_date == pytest.approx(
        (volatility * volatility) * expected_t_date
    )


def test_qlBlackVolTermStructure_forward_vol_is_constant_for_date_and_time():
    volatility = 0.20
    strike = 100.0
    handle = _constant_vol_handle(volatility)

    forward_vol_by_date = qlBlackVolTermStructureBlackForwardVol(
        handle,
        qlDate(2024, 7, 2),
        qlDate(2025, 1, 2),
        strike,
    )
    forward_vol_by_time = qlBlackVolTermStructureBlackForwardVolFromTime(
        handle, 0.5, 1.0, strike
    )

    assert forward_vol_by_date == pytest.approx(volatility)
    assert forward_vol_by_time == pytest.approx(volatility)


def test_qlBlackVolTermStructure_forward_variance_matches_elapsed_time():
    volatility = 0.20
    strike = 100.0
    handle = _constant_vol_handle(volatility)
    day_counter = qlDayCounter("ACTUAL365FIXED")
    start_date = qlDate(2024, 7, 2)
    end_date = qlDate(2025, 1, 2)

    forward_variance_by_time = qlBlackVolTermStructureBlackForwardVarianceFromTime(
        handle, 0.5, 1.5, strike
    )
    forward_variance_by_date = qlBlackVolTermStructureBlackForwardVariance(
        handle,
        start_date,
        end_date,
        strike,
    )
    expected_forward_t = qlDayCounterYearFraction(day_counter, start_date, end_date)

    assert forward_variance_by_time == pytest.approx((volatility * volatility) * 1.0)
    assert forward_variance_by_date == pytest.approx(
        (volatility * volatility) * expected_forward_t
    )


def test_qlLocalVolTermStructure_interface():
    lvol = ql.LocalConstantVol(qlDate(2024, 1, 2), 0.25, qlDayCounter("ACTUAL365FIXED"))
    lvol_handle = ql.LocalVolTermStructureHandle(lvol)

    assert qlLocalVolTermStructureLocalVol(
        lvol_handle, qlDate(2024, 7, 2), 100.0
    ) == pytest.approx(0.25)
    assert qlLocalVolTermStructureLocalVolFromTime(
        lvol_handle, 0.5, 100.0
    ) == pytest.approx(0.25)


def test_qlBlackVarianceCurve_creates_curve_from_dates_and_volatilities():
    reference_date = qlDate(2023, 1, 2)
    dates = [qlDate(2024, 1, 2), qlDate(2024, 7, 2), qlDate(2025, 1, 2)]
    volatilities = [0.20, 0.22, 0.24]

    curve = qlBlackVarianceCurve(
        reference_date=reference_date,
        dates=dates,
        volatilities=volatilities,
        day_counter=qlDayCounter("ACTUAL365FIXED"),
    )

    assert isinstance(curve, ql.BlackVarianceCurve)
    assert curve.blackVol(qlDate(2024, 1, 2), 100.0, False) == pytest.approx(0.20)


def test_qlBlackVarianceSurface_creates_handle_with_optional_extrapolation():
    reference_date = qlDate(2024, 1, 2)
    expiry_dates = [qlDate(2025, 1, 2), qlDate(2026, 1, 2)]
    strikes = [90.0, 110.0]
    black_vols = [[0.20, 0.21], [0.22, 0.23]]

    default_surface = qlBlackVarianceSurface(
        reference_date,
        qlCalendar("TARGET"),
        expiry_dates,
        strikes,
        black_vols,
        qlDayCounter("ACTUAL365FIXED"),
    )
    constant_extrapolation_surface = qlBlackVarianceSurface(
        reference_date,
        qlCalendar("TARGET"),
        expiry_dates,
        strikes,
        black_vols,
        qlDayCounter("ACTUAL365FIXED"),
        qBlackVarianceSurfaceExtrapolation.__wrapped__("CONSTANT"),
        qBlackVarianceSurfaceExtrapolation.__wrapped__("CONSTANT"),
        "",
    )

    assert isinstance(default_surface, ql.BlackVolTermStructureHandle)
    assert default_surface.blackVol(expiry_dates[0], strikes[0]) == pytest.approx(0.20)
    assert constant_extrapolation_surface.blackVol(
        expiry_dates[0], strikes[0]
    ) == pytest.approx(0.20)


def test_qlPiecewiseBlackVarianceSurfaceFromGrid_creates_handle():
    expiry_dates = [qlDate(2025, 1, 2), qlDate(2026, 1, 2)]
    strikes = [90.0, 110.0]
    vol_tsh = qlPiecewiseBlackVarianceSurfaceFromGrid(
        qlDate(2024, 1, 2),
        expiry_dates,
        strikes,
        [[0.20, 0.21], [0.22, 0.23]],
        qlDayCounter("ACTUAL365FIXED"),
    )

    assert isinstance(vol_tsh, ql.BlackVolTermStructureHandle)
    assert vol_tsh.blackVol(expiry_dates[0], strikes[0]) == pytest.approx(0.20)


def test_qlHestonBlackVolSurface_creates_handle_with_positive_volatility():
    spot = ql.QuoteHandle(ql.SimpleQuote(100.0))
    risk_free = ql.YieldTermStructureHandle(
        ql.FlatForward(qlDate(2026, 1, 2), 0.02, ql.Actual365Fixed())
    )
    dividend = ql.YieldTermStructureHandle(
        ql.FlatForward(qlDate(2026, 1, 2), 0.01, ql.Actual365Fixed())
    )
    process = ql.HestonProcess(risk_free, dividend, spot, 0.04, 1.50, 0.04, 0.25, -0.60)
    model_handle = ql.HestonModelHandle(ql.HestonModel(process))

    vol_tsh = qlHestonBlackVolSurface(model_handle, "GATHERAL", "GAUSS_LAGUERRE")

    assert isinstance(vol_tsh, ql.BlackVolTermStructureHandle)
    assert vol_tsh.blackVol(1.0, 100.0) > 0.0


def test_qlSabrVolatility_functions_and_guess():
    sabr_volatility = qlSabrVolatility(0.025, 0.025, 2.0, 0.20, 0.50, 0.30, -0.20)
    shifted_sabr_volatility = qlShiftedSabrVolatility(
        0.025,
        0.025,
        2.0,
        0.20,
        0.50,
        0.30,
        -0.20,
        0.0,
        "SHIFTEDLOGNORMAL",
    )
    floch_kennedy_volatility = qlSabrFlochKennedyVolatility(
        0.025, 0.025, 2.0, 0.20, 0.50, 0.30, -0.20
    )
    guess = qlSabrGuess(
        0.020,
        0.23,
        0.025,
        0.20,
        0.030,
        0.19,
        0.025,
        2.0,
        0.50,
        0.0,
        "SHIFTEDLOGNORMAL",
    )

    assert sabr_volatility > 0.0
    assert shifted_sabr_volatility == pytest.approx(sabr_volatility)
    assert floch_kennedy_volatility > 0.0
    assert len(guess) == 4
    assert all(isinstance(parameter, float) for parameter in guess)


def test_qlSABRInterpolation_evaluates_fixed_parameters():
    interpolation = qlSABRInterpolation(
        [0.02, 0.025, 0.03],
        [0.21, 0.20, 0.19],
        1.0,
        0.025,
        0.02,
        0.50,
        0.30,
        -0.20,
        True,
        True,
        True,
        True,
    )

    assert qlSABRInterpolationAlpha(interpolation) == pytest.approx(0.02)
    assert qlSABRInterpolationBeta(interpolation) == pytest.approx(0.50)
    assert qlSABRInterpolationNu(interpolation) == pytest.approx(0.30)
    assert qlSABRInterpolationRho(interpolation) == pytest.approx(-0.20)
    assert qlSABRInterpolationValue(interpolation, 0.025) > 0.0


def test_qlSabrSmileSection_creates_date_and_time_sections():
    date_section = qlSabrSmileSection(
        qlDate(2027, 1, 2), 0.025, [0.20, 0.50, 0.30, -0.20]
    )
    time_section = qlSabrSmileSectionFromTime(
        1.0, 0.025, [0.20, 0.50, 0.30, -0.20], 0.0, "SHIFTEDLOGNORMAL"
    )

    assert date_section.volatility(0.025) > 0.0
    assert time_section.volatility(0.025) > 0.0


def test_qlSviSmileSection_creates_date_and_time_sections():
    date_section = qlSviSmileSection(
        qlDate(2027, 1, 2), 0.025, [0.01, 0.10, 0.20, -0.20, 0.0]
    )
    time_section = qlSviSmileSectionFromTime(1.0, 0.025, [0.01, 0.10, 0.20, -0.20, 0.0])

    assert date_section.volatility(0.025) > 0.0
    assert time_section.volatility(0.025) > 0.0


def test_qlSviInterpolatedSmileSection_returns_fixed_parameters():
    section = qlSviInterpolatedSmileSection(
        qlDate(2027, 1, 2),
        0.025,
        [0.02, 0.025, 0.03],
        False,
        0.20,
        [0.21, 0.20, 0.19],
        0.01,
        0.10,
        0.20,
        -0.20,
        0.0,
        True,
        True,
        True,
        True,
        True,
    )

    assert qlSviInterpolatedSmileSectionA(section) == pytest.approx(0.01)
    assert qlSviInterpolatedSmileSectionB(section) == pytest.approx(0.10)
    assert qlSviInterpolatedSmileSectionSigma(section) == pytest.approx(0.20)
    assert qlSviInterpolatedSmileSectionRho(section) == pytest.approx(-0.20)
    assert qlSviInterpolatedSmileSectionM(section) == pytest.approx(0.0)


def test_qlNoArbSabrInterpolatedSmileSection_returns_fixed_parameters():
    section = qlNoArbSabrInterpolatedSmileSection(
        qlDate(2027, 1, 2),
        0.025,
        [0.02, 0.025, 0.03],
        False,
        0.20,
        [0.21, 0.20, 0.19],
        0.02,
        0.50,
        0.30,
        -0.20,
        True,
        True,
        True,
        True,
    )

    assert qlNoArbSabrInterpolatedSmileSectionAlpha(section) == pytest.approx(0.02)
    assert qlNoArbSabrInterpolatedSmileSectionBeta(section) == pytest.approx(0.50)
    assert qlNoArbSabrInterpolatedSmileSectionNu(section) == pytest.approx(0.30)
    assert qlNoArbSabrInterpolatedSmileSectionRho(section) == pytest.approx(-0.20)


def test_qlFlatSmileSection_creates_date_and_time_sections():
    date_section = qlFlatSmileSection(
        qlDate(2027, 1, 2), 0.20, qlDayCounter("ACTUAL365FIXED")
    )
    time_section = qlFlatSmileSectionFromTime(
        1.0, 0.20, qlDayCounter("ACTUAL365FIXED"), 0.025, "SHIFTEDLOGNORMAL"
    )

    assert date_section.volatility(0.025) == pytest.approx(0.20)
    assert time_section.volatility(0.025) == pytest.approx(0.20)


def test_qlNoArbSabrSmileSection_creates_date_and_time_sections():
    date_section = qlNoArbSabrSmileSection(
        qlDate(2027, 1, 2), 0.025, [0.02, 0.50, 0.30, -0.20]
    )
    time_section = qlNoArbSabrSmileSectionFromTime(
        1.0, 0.025, [0.02, 0.50, 0.30, -0.20], 0.0, "SHIFTEDLOGNORMAL"
    )

    assert date_section.volatility(0.025) > 0.0
    assert time_section.volatility(0.025) > 0.0


def test_qlZabrSmileSections_create_sections():
    constructors = (
        qlZabrShortMaturityLognormalSmileSection,
        qlZabrShortMaturityNormalSmileSection,
        qlZabrLocalVolatilitySmileSection,
        # qlZabrFullFdSmileSection,
    )
    for constructor in constructors:
        section = constructor(1.0, 0.025, [0.02, 0.50, 0.30, -0.20, 0.10])
        assert section.volatility(0.025) > 0.0


def test_qlInterpolatedSmileSections_create_sections_at_input_nodes():
    constructors = (
        qlLinearInterpolatedSmileSection,
        qlCubicInterpolatedSmileSection,
        qlMonotonicCubicInterpolatedSmileSection,
        qlSplineCubicInterpolatedSmileSection,
    )

    for constructor in constructors:
        smile_section = constructor(
            1.0,
            [0.02, 0.025, 0.03],
            [0.21, 0.20, 0.19],
            0.025,
            qlDayCounter("ACTUAL365FIXED"),
            "SHIFTEDLOGNORMAL",
        )
        assert smile_section.volatility(0.025) == pytest.approx(0.20)


def test_qlKahaleSmileSection_creates_arbitrage_free_smile():
    source = qlFlatSmileSectionFromTime(
        1.0, 0.20, qlDayCounter("ACTUAL365FIXED"), 0.025
    )
    smile_section = qlKahaleSmileSection(
        source, 0.025, interpolate=True, moneyness_grid=[0.9, 1.0, 1.1]
    )

    assert isinstance(smile_section, ql.KahaleSmileSection)
    assert smile_section.volatility(0.025) == pytest.approx(0.20)


def test_qlSmileSection_accessors_and_evaluators():
    smile_section = qlFlatSmileSection(
        qlDate(2027, 1, 2),
        0.20,
        qlDayCounter("ACTUAL365FIXED"),
        qlDate(2026, 1, 2),
        0.025,
    )

    assert qlSmileSectionAtmLevel(smile_section) == pytest.approx(0.025)
    assert qlSmileSectionExerciseDate(smile_section) == qlDate(2027, 1, 2)
    assert qlSmileSectionExerciseTime(smile_section) == pytest.approx(1.0)
    assert qlSmileSectionMinStrike(smile_section) < 0.025
    assert qlSmileSectionMaxStrike(smile_section) > 0.025
    assert qlSmileSectionVolatility(smile_section, 0.025) == pytest.approx(0.20)
    assert qlSmileSectionVariance(smile_section, 0.025) == pytest.approx(0.04)
    assert qlSmileSectionOptionPrice(smile_section, 0.025, "CALL") > 0.0
    assert qlSmileSectionDigitalOptionPrice(smile_section, 0.025, "CALL") > 0.0
    assert qlSmileSectionDensity(smile_section, 0.025) > 0.0
    assert qlSmileSectionVega(smile_section, 0.025) > 0.0
    assert qlSmileSectionShift(smile_section) == pytest.approx(0.0)
    assert qlSmileSectionVolatilityType(smile_section) == ql.ShiftedLognormal


def test_qlConstantYoYOptionletVolatility_creates_handle():
    handle = qlConstantYoYOptionletVolatility(
        0.20,
        2,
        qlCalendar("TARGET"),
        qBusinessDayConvention.__wrapped__("FOLLOWING"),
        qlDayCounter("ACTUAL365FIXED"),
        qlPeriod(3, ql.Months),
        ql.Annual,
        False,
        0.0,
        1.0,
    )

    assert isinstance(handle, ql.YoYOptionletVolatilitySurfaceHandle)
    assert handle.minStrike() == pytest.approx(0.0)
    assert handle.maxStrike() == pytest.approx(1.0)


# Helper functions for optionlet and swaption volatility tests


def _constant_optionlet_vol_handle(volatility: float = 0.20):
    return qlConstantOptionletVolatility(
        reference_date=qlDate(2024, 1, 2),
        calendar=qlCalendar("TARGET"),
        business_day_convention=qBusinessDayConvention.__wrapped__("FOLLOWING"),
        volatility=qQuoteHandle.__wrapped__(volatility),
        day_counter=qlDayCounter("ACTUAL365FIXED"),
        volatility_type=qVolatilityType.__wrapped__("SHIFTEDLOGNORMAL"),
        shift=0.0,
    )


def _constant_swaption_vol_handle(volatility: float = 0.20):
    return qlConstantSwaptionVolatility(
        reference_date=qlDate(2024, 1, 2),
        calendar=qlCalendar("TARGET"),
        business_day_convention=qBusinessDayConvention.__wrapped__("FOLLOWING"),
        volatility=qQuoteHandle.__wrapped__(volatility),
        day_counter=qlDayCounter("ACTUAL365FIXED"),
        volatility_type=qVolatilityType.__wrapped__("SHIFTEDLOGNORMAL"),
        shift=0.0,
    )


# OptionletVolatilityStructure tests


def test_qlConstantOptionletVolatility_creates_handle():
    handle = _constant_optionlet_vol_handle()
    assert isinstance(handle, ql.OptionletVolatilityStructureHandle)


def test_qlOptionletVolatilityStructure_volatility_constant_for_date_and_time():
    volatility = 0.20
    strike = 100.0
    handle = _constant_optionlet_vol_handle(volatility)

    vol_by_date = qlOptionletVolatilityStructureVolatility(
        handle, qlDate(2024, 7, 2), strike
    )
    vol_by_time = qlOptionletVolatilityStructureVolatilityFromTime(handle, 0.5, strike)

    assert vol_by_date == pytest.approx(volatility)
    assert vol_by_time == pytest.approx(volatility)


def test_qlOptionletVolatilityStructure_black_variance():
    volatility = 0.20
    strike = 100.0
    handle = _constant_optionlet_vol_handle(volatility)
    day_counter = qlDayCounter("ACTUAL365FIXED")
    reference_date = qlDate(2024, 1, 2)
    option_date = qlDate(2025, 1, 2)

    t = 1.0
    variance_by_time = qlOptionletVolatilityStructureBlackVarianceFromTime(
        handle, t, strike
    )
    variance_by_date = qlOptionletVolatilityStructureBlackVariance(
        handle, option_date, strike
    )
    expected_t_date = qlDayCounterYearFraction(day_counter, reference_date, option_date)

    assert variance_by_time == pytest.approx((volatility * volatility) * t)
    assert variance_by_date == pytest.approx(
        (volatility * volatility) * expected_t_date
    )


# SwaptionVolatilityStructure tests


def test_qlConstantSwaptionVolatility_creates_handle():
    handle = _constant_swaption_vol_handle()
    assert isinstance(handle, ql.SwaptionVolatilityStructureHandle)


def test_qlSpreadedSwaptionVolatility_adds_quote_spread():
    base_handle = _constant_swaption_vol_handle(0.20)
    handle = qlSpreadedSwaptionVolatility(base_handle, qQuoteHandle.__wrapped__(0.01))

    assert isinstance(handle, ql.SwaptionVolatilityStructureHandle)
    assert qlSwaptionVolatilityStructureVolatility(
        handle, qlDate(2027, 1, 2), qlPeriod(5, ql.Years), 0.025
    ) == pytest.approx(0.21)


def test_qlSwaptionVolatilityStructure_volatility_constant_for_date_and_time():
    volatility = 0.20
    strike = 100.0
    handle = _constant_swaption_vol_handle(volatility)

    vol_by_date = qlSwaptionVolatilityStructureVolatility(
        handle,
        option_date=qlDate(2024, 7, 2),
        swap_tenor=ql.Period("5Y"),
        strike=strike,
    )
    vol_by_time = qlSwaptionVolatilityStructureVolatilityFromTime(
        handle, option_time=0.5, swap_length=5.0, strike=strike
    )

    assert vol_by_date == pytest.approx(volatility)
    assert vol_by_time == pytest.approx(volatility)


def test_qlSwaptionVolatilityStructure_black_variance():
    volatility = 0.20
    strike = 100.0
    handle = _constant_swaption_vol_handle(volatility)

    option_date = qlDate(2024, 7, 2)
    option_time = handle.timeFromReference(option_date)
    swap_tenor = ql.Period("5Y")
    swap_length = 5.0

    variance_by_date = qlSwaptionVolatilityStructureBlackVariance(
        handle,
        option_date=option_date,
        swap_tenor=swap_tenor,
        strike=strike,
    )

    variance_by_time = qlSwaptionVolatilityStructureBlackVarianceFromTime(
        handle, option_time=option_time, swap_length=swap_length, strike=strike
    )

    # For constant volatility, variance = vol^2 * time
    # The time here is the option time (0.5 years)
    assert variance_by_time == pytest.approx((volatility * volatility) * option_time)
    assert variance_by_date == pytest.approx((volatility * volatility) * option_time)


def test_qlSwaptionVolatilityStructure_option_date_from_tenor():
    handle = _constant_swaption_vol_handle()
    reference_date = qlDate(2024, 1, 2)

    option_date = qlSwaptionVolatilityStructureOptionDateFromTenor(
        handle, option_tenor=ql.Period(6, ql.Months)
    )

    expected_date = reference_date + ql.Period(6, ql.Months)
    assert option_date == expected_date


def test_qlSwaptionVolatilityStructure_shift():
    shift = 0.01
    handle = qlConstantSwaptionVolatility(
        reference_date=qlDate(2024, 1, 2),
        calendar=qlCalendar("TARGET"),
        business_day_convention=qBusinessDayConvention.__wrapped__("FOLLOWING"),
        volatility=qQuoteHandle.__wrapped__(0.20),
        day_counter=qlDayCounter("ACTUAL365FIXED"),
        volatility_type=qVolatilityType.__wrapped__("SHIFTEDLOGNORMAL"),
        shift=shift,
    )

    shift_by_date = qlSwaptionVolatilityStructureShift(
        handle,
        option_date=qlDate(2024, 7, 2),
        swap_tenor=ql.Period("5Y"),
    )
    shift_by_time = qlSwaptionVolatilityStructureShiftFromTime(
        handle, option_time=0.5, swap_length=5.0
    )

    assert shift_by_date == pytest.approx(shift)
    assert shift_by_time == pytest.approx(shift)


def test_qlSwaptionVolatilityStructure_smile_section():
    handle = _constant_swaption_vol_handle(0.20)

    smile_by_date = qlSwaptionVolatilityStructureSmileSection(
        handle,
        option_date=qlDate(2024, 7, 2),
        swap_tenor=qlPeriod(5, ql.Years),
    )
    smile_by_time = qlSwaptionVolatilityStructureSmileSectionFromTime(
        handle, option_time=0.5, swap_length=5.0
    )

    assert isinstance(smile_by_date, ql.SmileSection)
    assert isinstance(smile_by_time, ql.SmileSection)


def test_qlVolatilityType_converter():
    assert qVolatilityType.__wrapped__("NORMAL") == ql.Normal
    assert qVolatilityType.__wrapped__("SHIFTEDLOGNORMAL") == ql.ShiftedLognormal


def test_qlSwaptionVolatilityMatrix_creates_handle_and_interpolates():
    import numpy as np

    reference_date = qlDate(2024, 1, 2)
    day_counter = qlDayCounter("ACTUAL365FIXED")

    # Define a 2x2 vol matrix: 2 expiries x 2 swap tenors
    expiry_dates = np.array(
        [
            qlDate(2025, 1, 2),
            qlDate(2026, 1, 2),
        ]
    )
    lengths = np.array([qlPeriod(2, ql.Years), qlPeriod(5, ql.Years)])
    vols = np.array([[0.20, 0.22], [0.18, 0.21]])

    handle = qlSwaptionVolatilityMatrix(
        reference_date=reference_date,
        expiry_dates=expiry_dates,
        lengths=lengths,
        vols=vols,
        day_counter=day_counter,
        flat_extrapolation=True,
        volatility_type=qVolatilityType.__wrapped__("SHIFTEDLOGNORMAL"),
        shifts=None,
    )

    assert isinstance(handle, ql.SwaptionVolatilityStructureHandle)

    # Volatility at grid nodes should match input
    vol_1y_2y = qlSwaptionVolatilityStructureVolatility(
        handle,
        option_date=expiry_dates[0],
        swap_tenor=lengths[0],
        strike=0.025,
    )
    vol_2y_5y = qlSwaptionVolatilityStructureVolatility(
        handle,
        option_date=expiry_dates[1],
        swap_tenor=lengths[1],
        strike=0.025,
    )

    assert vol_1y_2y == pytest.approx(vols[0, 0], rel=1e-4)
    assert vol_2y_5y == pytest.approx(vols[1, 1], rel=1e-4)
