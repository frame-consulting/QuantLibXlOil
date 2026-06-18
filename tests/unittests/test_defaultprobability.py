import QuantLib as ql
import pytest

from quantlib_xloil.calendars import qlCalendar
from quantlib_xloil.date import qlDate
from quantlib_xloil.defaultprobability import (
    qlDefaultDensityCurve,
    qlDefaultProbabilityHelperEarliestDate,
    qlDefaultProbabilityHelperImpliedQuote,
    qlDefaultProbabilityHelperLatestDate,
    qlDefaultProbabilityHelperLatestRelevantDate,
    qlDefaultProbabilityHelperMaturity,
    qlDefaultProbabilityHelperPillarDate,
    qlDefaultProbabilityHelperQuote,
    qlDefaultProbabilityHelperQuoteError,
    qlDefaultProbabilityTermStructureDefaultDensity,
    qlDefaultProbabilityTermStructureDefaultDensityFromTime,
    qlDefaultProbabilityTermStructureDefaultProbability,
    qlDefaultProbabilityTermStructureDefaultProbability2,
    qlDefaultProbabilityTermStructureDefaultProbabilityFromTime,
    qlDefaultProbabilityTermStructureDefaultProbabilityFromTime2,
    qlDefaultProbabilityTermStructureHazardRate,
    qlDefaultProbabilityTermStructureHazardRateFromTime,
    qlDefaultProbabilityTermStructureSurvivalProbability,
    qlDefaultProbabilityTermStructureSurvivalProbabilityFromTime,
    qlFlatHazardRate,
    qlHazardRateCurve,
    qlPiecewiseFlatHazardRate,
    qlPiecewiseFlatHazardRateAsDts,
    qlRiskyBondEngine,
    qlSpreadCdsHelper,
    qlSurvivalProbabilityCurve,
    qlUpfrontCdsHelper,
)


def _discount_curve(reference_date: ql.Date) -> ql.YieldTermStructureHandle:
    return ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.03, ql.Actual365Fixed())
    )


def test_flat_hazard_rate_term_structure_accessors():
    reference_date = qlDate(2025, 1, 2)
    day_counter = ql.Actual365Fixed()
    ts = qlFlatHazardRate(
        reference_date, ql.QuoteHandle(ql.SimpleQuote(0.02)), day_counter
    )

    date_1y = qlDate(2026, 1, 2)
    t = 1.0

    assert isinstance(ts, ql.DefaultProbabilityTermStructureHandle)
    assert qlDefaultProbabilityTermStructureDefaultProbability(
        ts, date_1y
    ) == pytest.approx(ts.defaultProbability(date_1y))
    assert qlDefaultProbabilityTermStructureDefaultProbabilityFromTime(
        ts, t
    ) == pytest.approx(ts.defaultProbability(t))
    assert qlDefaultProbabilityTermStructureDefaultProbability2(
        ts, reference_date, date_1y
    ) == pytest.approx(ts.defaultProbability(reference_date, date_1y))
    assert qlDefaultProbabilityTermStructureDefaultProbabilityFromTime2(
        ts, 0.5, 1.0
    ) == pytest.approx(ts.defaultProbability(0.5, 1.0))

    survival = qlDefaultProbabilityTermStructureSurvivalProbability(ts, date_1y)
    survival_time = qlDefaultProbabilityTermStructureSurvivalProbabilityFromTime(ts, t)
    assert survival == pytest.approx(ts.survivalProbability(date_1y))
    assert survival_time == pytest.approx(ts.survivalProbability(t))
    assert 0.0 < survival < 1.0

    assert qlDefaultProbabilityTermStructureHazardRate(ts, date_1y) == pytest.approx(
        ts.hazardRate(date_1y)
    )
    assert qlDefaultProbabilityTermStructureHazardRateFromTime(ts, t) == pytest.approx(
        ts.hazardRate(t)
    )
    assert qlDefaultProbabilityTermStructureDefaultDensity(
        ts, date_1y
    ) == pytest.approx(ts.defaultDensity(date_1y))
    assert qlDefaultProbabilityTermStructureDefaultDensityFromTime(
        ts, t
    ) == pytest.approx(ts.defaultDensity(t))


def test_hazard_density_and_survival_curve_builders():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        d0 = qlDate(2025, 1, 2)
        ql.Settings.instance().evaluationDate = d0
        dates = [qlDate(2025, 7, 2), qlDate(2026, 1, 2), qlDate(2027, 1, 2)]
        dc = ql.Actual365Fixed()

        hazard_ts = qlHazardRateCurve(
            dates, [0.01, 0.015, 0.02], dc, qlCalendar("TARGET")
        )
        density_ts = qlDefaultDensityCurve(
            dates, [0.01, 0.012, 0.014], dc, qlCalendar("TARGET")
        )
        survival_ts = qlSurvivalProbabilityCurve(
            [d0] + dates, [1.0, 0.99, 0.97, 0.93], dc, qlCalendar("TARGET")
        )

        assert isinstance(hazard_ts, ql.DefaultProbabilityTermStructureHandle)
        assert isinstance(density_ts, ql.DefaultProbabilityTermStructureHandle)
        assert isinstance(survival_ts, ql.DefaultProbabilityTermStructureHandle)

        assert (
            qlDefaultProbabilityTermStructureHazardRate(hazard_ts, dates[0], True)
            >= 0.0
        )
        assert (
            qlDefaultProbabilityTermStructureDefaultDensity(density_ts, dates[0], True)
            >= 0.0
        )
        assert (
            0.0
            < qlDefaultProbabilityTermStructureSurvivalProbability(
                survival_ts, d0, True
            )
            <= 1.0
        )
    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_default_probability_helpers_piecewise_and_risky_bond_engine():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        reference_date = qlDate(2025, 1, 2)
        ql.Settings.instance().evaluationDate = reference_date

        discount_curve = _discount_curve(reference_date)
        day_counter = ql.Actual360()
        tenor_spread = ql.Period("3Y")
        tenor_upfront = ql.Period("5Y")

        spread_helper = qlSpreadCdsHelper(
            0.01,
            tenor_spread,
            2,
            qlCalendar("TARGET"),
            ql.Quarterly,
            ql.Following,
            ql.DateGeneration.CDS,
            day_counter,
            0.40,
            discount_curve,
            start_date=reference_date,
        )
        upfront_helper = qlUpfrontCdsHelper(
            0.02,
            0.05,
            tenor_upfront,
            2,
            qlCalendar("TARGET"),
            ql.Quarterly,
            ql.Following,
            ql.DateGeneration.CDS,
            day_counter,
            0.40,
            discount_curve,
            start_date=reference_date,
        )

        assert isinstance(spread_helper, ql.SpreadCdsHelper)
        assert isinstance(upfront_helper, ql.UpfrontCdsHelper)

        for helper in (spread_helper, upfront_helper):
            quote = qlDefaultProbabilityHelperQuote(helper)
            assert isinstance(quote, ql.QuoteHandle)
            assert qlDefaultProbabilityHelperLatestDate(
                helper
            ) >= qlDefaultProbabilityHelperEarliestDate(helper)
            assert qlDefaultProbabilityHelperMaturity(
                helper
            ) >= qlDefaultProbabilityHelperEarliestDate(helper)
            assert qlDefaultProbabilityHelperLatestRelevantDate(
                helper
            ) >= qlDefaultProbabilityHelperEarliestDate(helper)
            assert qlDefaultProbabilityHelperPillarDate(
                helper
            ) >= qlDefaultProbabilityHelperEarliestDate(helper)

        # Trigger bootstrap, then helper implied/quote-error methods are available.
        piecewise_ts = qlPiecewiseFlatHazardRate(
            reference_date, [spread_helper], day_counter
        )
        assert isinstance(piecewise_ts, ql.DefaultProbabilityTermStructureHandle)
        assert (
            qlDefaultProbabilityTermStructureSurvivalProbability(
                piecewise_ts, qlDate(2026, 1, 2), True
            )
            > 0.0
        )

        piecewise_dts = qlPiecewiseFlatHazardRateAsDts(
            reference_date, [spread_helper], day_counter
        )
        assert isinstance(piecewise_dts, ql.PiecewiseFlatHazardRate)

        assert isinstance(qlDefaultProbabilityHelperImpliedQuote(spread_helper), float)
        assert isinstance(qlDefaultProbabilityHelperQuoteError(spread_helper), float)

        engine = qlRiskyBondEngine(piecewise_ts, 0.40, discount_curve)
        assert isinstance(engine, ql.RiskyBondEngine)
    finally:
        try:
            ql.Settings.instance().evaluationDate = original_eval
        except RuntimeError:
            # Some helper/observer graphs can reject date rollback during teardown.
            pass
