import QuantLib as ql
import pytest

from quantlib_xloil.ratehelpers import (
    qFuturesType,
    qPillarChoice,
    qQuoteHandle,
    qlDepositRateHelper,
    qlDepositRateHelper2,
    qlDepositRateHelper3,
    qlFRARateHelper2,
    qlFRARateHelper3,
    qlFRARateHelper4,
    qlFuturesRateConvexityAdjustment,
    qlFuturesRateHelper2,
    qlFuturesRateHelper3,
    qlFxSwapRateHelper,
    qlFxSwapRateHelperAdjustmentCalendar,
    qlFxSwapRateHelperCalendar,
    qlFxSwapRateHelperEndOfMonth,
    qlFxSwapRateHelperFixingDays,
    qlFxSwapRateHelperIsFxBaseCurrencyCollateralCurrency,
    qlFxSwapRateHelperSpot,
    qlFxSwapRateHelperTenor,
    qlFxSwapRateHelperTradingCalendar,
    qlMultipleResetsSwapRateHelper,
    qlOISRateHelper,
    qlOISRateHelperSwap,
    qlOvernightIndexFutureRateHelper,
    qlOvernightIndexFutureRateHelperConvexityAdjustment,
    qlRateHelperEarliestDate,
    qlRateHelperImpliedQuote,
    qlRateHelperLatestDate,
    qlRateHelperLatestRelevantDate,
    qlRateHelperMaturityDate,
    qlRateHelperPillarDate,
    qlRateHelperQuote,
    qlRateHelperQuoteError,
    qlSofrFutureRateHelper,
    qlSwapRateHelper,
    qlSwapRateHelper2,
    qlSwapRateHelperSpread,
    qlSwapRateHelperSwap,
    xQuoteHandle,
)
from quantlib_xloil.calendars import qBusinessDayConvention, qlCalendar
from quantlib_xloil.cashflows import qRateAveragingType
from quantlib_xloil.date import qFrequency, qlDate
from quantlib_xloil.daycounters import qlDayCounter
from quantlib_xloil.indexes import qlSofr, qlUSDLibor, qlUsdLiborSwapIsdaFixAm
from quantlib_xloil.scheduler import qDateGenerationRule
from quantlib_xloil.termstructures import qCompounding, qlFlatForward


def _set_eval_date() -> None:
    ql.Settings.instance().evaluationDate = qlDate(2024, 1, 2)


def test_ratehelper_enum_converters_case_insensitive():
    assert qPillarChoice.__wrapped__("lastrelevantdate") == ql.Pillar.LastRelevantDate
    assert qPillarChoice.__wrapped__("MATURITYDATE") == ql.Pillar.MaturityDate
    assert qFuturesType.__wrapped__("imm") == ql.Futures.IMM
    assert qFuturesType.__wrapped__("ASX") == ql.Futures.ASX


def test_qQuoteHandle_and_xQuoteHandle_wrapped():
    quote_handle = qQuoteHandle.__wrapped__(0.0123)
    assert isinstance(quote_handle, ql.QuoteHandle)
    assert quote_handle.value() == pytest.approx(0.0123)
    assert xQuoteHandle.__wrapped__(quote_handle) == pytest.approx(0.0123)

    existing = ql.QuoteHandle(ql.SimpleQuote(0.02))
    assert qQuoteHandle.__wrapped__(existing) is existing

    with pytest.raises(ValueError, match="Cannot convert"):
        qQuoteHandle.__wrapped__("not-a-quote")


def test_ratehelper_accessors_and_bootstrap_metrics():
    _set_eval_date()
    helper = qlDepositRateHelper(
        0.05,
        ql.Period("3M"),
        2,
        qlCalendar("TARGET"),
        qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        False,
        qlDayCounter("ACTUAL360"),
    )

    quote_handle = qlRateHelperQuote(helper)
    assert isinstance(quote_handle, ql.QuoteHandle)
    assert quote_handle.value() == pytest.approx(0.05)

    earliest = qlRateHelperEarliestDate(helper)
    latest = qlRateHelperLatestDate(helper)
    maturity = qlRateHelperMaturityDate(helper)
    latest_relevant = qlRateHelperLatestRelevantDate(helper)
    pillar = qlRateHelperPillarDate(helper)

    assert earliest <= latest
    assert maturity == latest
    assert latest_relevant == latest
    assert pillar == latest

    with pytest.raises(RuntimeError, match="term structure not set"):
        qlRateHelperImpliedQuote(helper)

    curve = ql.PiecewiseFlatForward(
        qlDate(2024, 1, 2), [helper], qlDayCounter("ACTUAL365FIXED")
    )
    curve.recalculate()
    assert qlRateHelperImpliedQuote(helper) == pytest.approx(0.05)
    assert abs(qlRateHelperQuoteError(helper)) < 1e-10


def test_deposit_and_fra_helper_overloads():
    _set_eval_date()
    index = qlUSDLibor(ql.Period("3M"))

    dep2 = qlDepositRateHelper2(0.05, index)
    dep3 = qlDepositRateHelper3(
        ql.QuoteHandle(ql.SimpleQuote(0.05)),
        index.fixingDate(qlDate(2024, 1, 10)),
        index,
    )

    fra2 = qlFRARateHelper2(
        0.052, 3, index, qPillarChoice.__wrapped__("LASTRELEVANTDATE"), ql.Date(), True
    )
    fra3 = qlFRARateHelper3(
        0.053,
        1,
        2,
        index,
        qPillarChoice.__wrapped__("LASTRELEVANTDATE"),
        ql.Date(),
        True,
    )
    fra4 = qlFRARateHelper4(
        0.053,
        ql.Period("1M"),
        index,
        qPillarChoice.__wrapped__("LASTRELEVANTDATE"),
        ql.Date(),
        True,
    )

    assert isinstance(dep2, ql.DepositRateHelper)
    assert isinstance(dep3, ql.DepositRateHelper)
    assert isinstance(fra2, ql.FraRateHelper)
    assert isinstance(fra3, ql.FraRateHelper)
    assert isinstance(fra4, ql.FraRateHelper)


def test_futures_helpers_and_convexity_accessor():
    _set_eval_date()
    index = qlUSDLibor(ql.Period("3M"))
    quote_95 = ql.QuoteHandle(ql.SimpleQuote(95.0))
    quote_0 = ql.QuoteHandle(ql.SimpleQuote(0.0))

    fut2 = qlFuturesRateHelper2(
        quote_95,
        qlDate(2024, 3, 20),
        qlDate(2024, 6, 20),
        qlDayCounter("ACTUAL360"),
        quote_0,
        qFuturesType.__wrapped__("IMM"),
    )
    fut3 = qlFuturesRateHelper3(
        quote_95, qlDate(2024, 3, 20), index, quote_0, qFuturesType.__wrapped__("IMM")
    )

    assert isinstance(fut2, ql.FuturesRateHelper)
    assert isinstance(fut3, ql.FuturesRateHelper)
    assert qlFuturesRateConvexityAdjustment(fut2) == pytest.approx(0.0)


def test_swap_helpers_and_accessors():
    _set_eval_date()
    index = qlUSDLibor(ql.Period("3M"))
    swap1 = qlSwapRateHelper(
        0.03,
        ql.Period("5Y"),
        qlCalendar("TARGET"),
        qFrequency.__wrapped__("ANNUAL"),
        qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        qlDayCounter("THIRTY360"),
        index,
        pillar=qPillarChoice.__wrapped__("LASTRELEVANTDATE"),
    )
    swap2 = qlSwapRateHelper2(
        0.03,
        qlUsdLiborSwapIsdaFixAm(ql.Period("5Y")),
        pillar=qPillarChoice.__wrapped__("LASTRELEVANTDATE"),
    )

    assert isinstance(swap1, ql.SwapRateHelper)
    assert isinstance(swap2, ql.SwapRateHelper)
    assert isinstance(qlSwapRateHelperSwap(swap1), ql.VanillaSwap)
    assert qlSwapRateHelperSpread(swap2) == pytest.approx(0.0)


def test_ois_helper_and_swap_accessor():
    _set_eval_date()
    ois = qlOISRateHelper(
        2,
        ql.Period("1Y"),
        0.025,
        qlSofr(),
        payment_convention=qBusinessDayConvention.__wrapped__("FOLLOWING"),
        payment_frequency=qFrequency.__wrapped__("ANNUAL"),
        payment_calendar=qlCalendar("NULLCALENDAR"),
        pillar=qPillarChoice.__wrapped__("LASTRELEVANTDATE"),
        averaging_method=qRateAveragingType.__wrapped__("COMPOUND"),
        fixed_payment_frequency=qFrequency.__wrapped__("NOFREQUENCY"),
        fixed_calendar=qlCalendar("NULLCALENDAR"),
        rule=qDateGenerationRule.__wrapped__("BACKWARD"),
        overnight_calendar=qlCalendar("NULLCALENDAR"),
        convention=qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
    )

    assert isinstance(ois, ql.OISRateHelper)
    assert isinstance(qlOISRateHelperSwap(ois), ql.OvernightIndexedSwap)


def test_fx_swap_helper_and_accessors():
    _set_eval_date()
    curve = qlFlatForward(
        qlDate(2024, 1, 2),
        0.02,
        qlDayCounter("ACTUAL365FIXED"),
        qCompounding.__wrapped__("COMPOUNDED"),
        qFrequency.__wrapped__("ANNUAL"),
        qlCalendar("TARGET"),
    )
    helper = qlFxSwapRateHelper(
        ql.QuoteHandle(ql.SimpleQuote(0.0)),
        ql.QuoteHandle(ql.SimpleQuote(1.1)),
        ql.Period("1M"),
        2,
        qlCalendar("TARGET"),
        qBusinessDayConvention.__wrapped__("MODIFIEDFOLLOWING"),
        False,
        True,
        curve,
        qlCalendar("NULLCALENDAR"),
    )

    assert isinstance(helper, ql.FxSwapRateHelper)
    assert qlFxSwapRateHelperSpot(helper) == pytest.approx(1.1)
    assert qlFxSwapRateHelperTenor(helper) == ql.Period("1M")
    assert qlFxSwapRateHelperFixingDays(helper) == 2
    assert isinstance(qlFxSwapRateHelperCalendar(helper), ql.Calendar)
    assert isinstance(qlFxSwapRateHelperTradingCalendar(helper), ql.Calendar)
    assert isinstance(qlFxSwapRateHelperAdjustmentCalendar(helper), ql.Calendar)
    assert qlFxSwapRateHelperEndOfMonth(helper) is False
    assert qlFxSwapRateHelperIsFxBaseCurrencyCollateralCurrency(helper) is True


def test_multiple_resets_swap_rate_helper_constructs():
    _set_eval_date()
    index = qlUSDLibor(ql.Period("3M"))
    helper = qlMultipleResetsSwapRateHelper(
        settlement_days=2,
        tenor=ql.Period("1Y"),
        fixed_rate=0.03,
        ibor_index=index,
        resets_per_coupon=5,
        fixed_frequency=qFrequency.__wrapped__("ANNUAL"),
    )

    assert isinstance(helper, ql.MultipleResetsSwapRateHelper)


def test_overnight_and_sofr_future_helpers():
    _set_eval_date()
    quote_95 = ql.QuoteHandle(ql.SimpleQuote(95.0))
    quote_0 = ql.QuoteHandle(ql.SimpleQuote(0.0))

    overnight = qlOvernightIndexFutureRateHelper(
        quote_95,
        qlDate(2024, 6, 1),
        qlDate(2024, 6, 30),
        qlSofr(),
        quote_0,
        qRateAveragingType.__wrapped__("COMPOUND"),
    )
    sofr = qlSofrFutureRateHelper(
        quote_95, 6, 2024, qFrequency.__wrapped__("QUARTERLY"), quote_0
    )

    assert isinstance(overnight, ql.OvernightIndexFutureRateHelper)
    assert qlOvernightIndexFutureRateHelperConvexityAdjustment(
        overnight
    ) == pytest.approx(0.0)
    assert isinstance(sofr, ql.SofrFutureRateHelper)
