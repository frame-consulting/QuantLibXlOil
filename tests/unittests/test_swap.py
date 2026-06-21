import QuantLib as ql
import pytest

from quantlib_xloil.calendars import qlCalendar
from quantlib_xloil.date import qlDate
from quantlib_xloil.swap import (
    qSwapType,
    qlAsOvernightSwapIndex,
    qlEquityTotalReturnSwap,
    qlEquityTotalReturnSwap2,
    qlEquityTotalReturnSwapDayCounter,
    qlEquityTotalReturnSwapEquityIndex,
    qlEquityTotalReturnSwapEquityLeg,
    qlEquityTotalReturnSwapEquityLegNPV,
    qlEquityTotalReturnSwapFairMargin,
    qlEquityTotalReturnSwapGearing,
    qlEquityTotalReturnSwapInterestRateIndex,
    qlEquityTotalReturnSwapInterestRateLeg,
    qlEquityTotalReturnSwapInterestRateLegNPV,
    qlEquityTotalReturnSwapMargin,
    qlEquityTotalReturnSwapNominal,
    qlEquityTotalReturnSwapPaymentCalendar,
    qlEquityTotalReturnSwapPaymentConvention,
    qlEquityTotalReturnSwapPaymentDelay,
    qlEquityTotalReturnSwapSchedule,
    qlEquityTotalReturnSwapType,
    qlFloatFloatSwap,
    qlDiscountingSwapEngine,
    qlDiscountingSwapEngine2,
    qlMakeOIS,
    qlMakeVanillaSwap,
    qlNonstandardSwap,
    qlNonstandardSwapType,
    qlNonstandardSwapFixedNominal,
    qlNonstandardSwapFloatingNominal,
    qlNonstandardSwapFixedSchedule,
    qlNonstandardSwapFloatingSchedule,
    qlNonstandardSwapFixedRate,
    qlNonstandardSwapFixedDayCount,
    qlNonstandardSwapIborIndex,
    qlNonstandardSwapSpread,
    qlNonstandardSwapGearing,
    qlNonstandardSwapSpreads,
    qlNonstandardSwapGearings,
    qlNonstandardSwapFloatingDayCount,
    qlNonstandardSwapPaymentConvention,
    qlNonstandardSwapFixedLeg,
    qlNonstandardSwapFloatingLeg,
    qlOvernightIndexedSwap,
    qlOvernightIndexedSwap2,
    qlOvernightIndexedSwapOvernightLegBPS,
    qlOvernightIndexedSwapOvernightLegNPV,
    qlOvernightIndexedSwapPaymentFrequency,
    qlOvernightIndexedSwapOvernightIndex,
    qlOvernightIndexedSwapOvernightLeg,
    qlOvernightIndexedSwapAveragingMethod,
    qlOvernightIndexedSwapLookbackDays,
    qlOvernightIndexedSwapLockoutDays,
    qlOvernightIndexedSwapApplyObservationShift,
    qlOvernightIndexedSwapIndex,
    qlOvernightIndexedSwapIndexOvernightIndex,
    qlOvernightIndexedSwapIndexUnderlyingSwap,
    qlSwap,
    qlSwap2,
    qlSwapEndDiscounts,
    qlSwapLeg,
    qlSwapLegBPS,
    qlSwapLegNPV,
    qlSwapMaturityDate,
    qlSwapNpvDateDiscount,
    qlSwapNumberOfLegs,
    qlSwapPayer,
    qlSwapStartDate,
    qlSwapStartDiscounts,
    qlVanillaSwap,
    qlFixedVsFloatingSwapType,
    qlFixedVsFloatingSwapNominal,
    qlFixedVsFloatingSwapFixedRate,
    qlFixedVsFloatingSwapSpread,
    qlFixedVsFloatingSwapFixedLegBPS,
    qlFixedVsFloatingSwapFixedLegNPV,
    qlFixedVsFloatingSwapFloatingLegBPS,
    qlFixedVsFloatingSwapFloatingLegNPV,
    qlFixedVsFloatingSwapFairRate,
    qlFixedVsFloatingSwapFairSpread,
    qlZeroCouponSwap,
    qlZeroCouponSwap2,
    qlZeroCouponSwapBaseNominal,
    qlZeroCouponSwapFairFixedPayment,
    qlZeroCouponSwapFairFixedRate,
    qlZeroCouponSwapFixedLeg,
    qlZeroCouponSwapFixedLegNPV,
    qlZeroCouponSwapFixedPayment,
    qlZeroCouponSwapFloatingLeg,
    qlZeroCouponSwapFloatingLegNPV,
    qlZeroCouponSwapIborIndex,
    qlZeroCouponSwapType,
)


def _schedule(start: ql.Date, end: ql.Date, tenor: ql.Period) -> ql.Schedule:
    return ql.Schedule(
        start,
        end,
        tenor,
        qlCalendar("TARGET"),
        ql.Following,
        ql.Following,
        ql.DateGeneration.Forward,
        False,
    )


def test_swap_type_converter():
    assert qSwapType.__wrapped__("payer") == 1
    assert qSwapType.__wrapped__("RECEIVER") == -1
    assert qSwapType.__wrapped__(1) == 1
    assert qSwapType.__wrapped__(-1.0) == -1


def test_qlswap_and_qlswap2_leg_accessors():
    d1 = qlDate(2025, 1, 2)
    d2 = qlDate(2025, 7, 2)
    d3 = qlDate(2026, 1, 2)

    leg1 = [ql.SimpleCashFlow(100.0, d2), ql.SimpleCashFlow(100.0, d3)]
    leg2 = [ql.SimpleCashFlow(95.0, d2), ql.SimpleCashFlow(95.0, d3)]

    swap = qlSwap(leg1, leg2)
    swap2 = qlSwap2([leg1, leg2], [True, False])

    for s in (swap, swap2):
        assert isinstance(s, ql.Swap)
        assert qlSwapNumberOfLegs(s) == 2
        assert len(qlSwapLeg(s, 0)) == 2
        assert len(qlSwapLeg(s, 1)) == 2
        assert qlSwapStartDate(s) <= qlSwapMaturityDate(s)
        assert qlSwapPayer(s, 0) is True
        assert qlSwapPayer(s, 1) is False


def test_vanilla_swap_pricing_and_wrapper_parity():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2024, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        fixed_schedule = _schedule(eval_date, qlDate(2029, 1, 2), ql.Period("1Y"))
        float_schedule = _schedule(eval_date, qlDate(2029, 1, 2), ql.Period("6M"))

        day_count_fixed = ql.Thirty360(ql.Thirty360.BondBasis)
        day_count_float = ql.Actual360()

        discount_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
        )
        forecast_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.021, ql.Actual365Fixed())
        )
        ibor = ql.USDLibor(ql.Period("6M"), forecast_curve)
        ibor.addFixing(ql.Date(28, 12, 2023), 0.021)

        swap = qlVanillaSwap(
            qSwapType.__wrapped__("PAYER"),
            1_000_000.0,
            fixed_schedule,
            0.025,
            day_count_fixed,
            float_schedule,
            ibor,
            0.001,
            day_count_float,
            ql.Following,
        )

        engine = qlDiscountingSwapEngine(discount_curve)
        swap.setPricingEngine(engine)

        assert isinstance(swap, ql.VanillaSwap)
        assert qlFixedVsFloatingSwapType(swap) == "PAYER"
        assert qlFixedVsFloatingSwapNominal(swap) == pytest.approx(1_000_000.0)
        assert qlFixedVsFloatingSwapFixedRate(swap) == pytest.approx(0.025)
        assert qlFixedVsFloatingSwapSpread(swap) == pytest.approx(0.001)

        assert qlSwapLegNPV(swap, 0) == pytest.approx(swap.legNPV(0))
        assert qlSwapLegNPV(swap, 1) == pytest.approx(swap.legNPV(1))
        assert qlSwapLegBPS(swap, 0) == pytest.approx(swap.legBPS(0))
        assert qlSwapLegBPS(swap, 1) == pytest.approx(swap.legBPS(1))
        assert qlSwapStartDiscounts(swap, 0) == pytest.approx(swap.startDiscounts(0))
        assert qlSwapEndDiscounts(swap, 0) == pytest.approx(swap.endDiscounts(0))
        assert qlSwapNpvDateDiscount(swap) == pytest.approx(swap.npvDateDiscount())

        assert qlFixedVsFloatingSwapFixedLegBPS(swap) == pytest.approx(
            swap.fixedLegBPS()
        )
        assert qlFixedVsFloatingSwapFixedLegNPV(swap) == pytest.approx(
            swap.fixedLegNPV()
        )
        assert qlFixedVsFloatingSwapFloatingLegBPS(swap) == pytest.approx(
            swap.floatingLegBPS()
        )
        assert qlFixedVsFloatingSwapFloatingLegNPV(swap) == pytest.approx(
            swap.floatingLegNPV()
        )
        assert qlFixedVsFloatingSwapFairRate(swap) == pytest.approx(swap.fairRate())
        assert qlFixedVsFloatingSwapFairSpread(swap) == pytest.approx(swap.fairSpread())
    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_make_vanilla_swap_and_discounting_engine2():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2024, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        forecast_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
        )
        discount_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.019, ql.Actual365Fixed())
        )
        ibor = ql.USDLibor(ql.Period("6M"), forecast_curve)
        ibor.addFixing(ql.Date(28, 12, 2023), 0.02, True)

        swap = qlMakeVanillaSwap(
            ql.Period("5Y"),
            ibor,
            fixed_rate=0.025,
            nominal=1_000_000.0,
            settlement_days=0,
            effective_date=eval_date,
            termination_date=qlDate(2029, 1, 2),
            floating_leg_spread=0.001,
            discounting_term_structure=discount_curve,
        )

        assert isinstance(swap, ql.VanillaSwap)
        assert abs(swap.NPV()) > 0.0

        with pytest.raises(TypeError, match="Wrong number or type of arguments"):
            qlDiscountingSwapEngine2(discount_curve)
    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_nonstandard_swap_wrapper_accessors():
    eval_date = qlDate(2024, 1, 2)
    fixed_schedule = _schedule(eval_date, qlDate(2029, 1, 2), ql.Period("1Y"))
    float_schedule = _schedule(eval_date, qlDate(2029, 1, 2), ql.Period("6M"))

    forecast_curve = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.021, ql.Actual365Fixed())
    )
    ibor = ql.USDLibor(ql.Period("6M"), forecast_curve)

    n_fixed = len(fixed_schedule) - 1
    n_float = len(float_schedule) - 1

    swap = qlNonstandardSwap(
        qSwapType.__wrapped__("PAYER"),
        [1_000_000.0] * n_fixed,
        [1_000_000.0] * n_float,
        fixed_schedule,
        [0.025] * n_fixed,
        ql.Thirty360(ql.Thirty360.BondBasis),
        float_schedule,
        ibor,
        [1.0] * n_float,
        [0.001] * n_float,
        ql.Actual360(),
    )

    assert isinstance(swap, ql.NonstandardSwap)
    assert qlNonstandardSwapType(swap) == "PAYER"
    assert qlNonstandardSwapFixedNominal(swap) == pytest.approx(swap.fixedNominal())
    assert qlNonstandardSwapFloatingNominal(swap) == pytest.approx(
        swap.floatingNominal()
    )
    assert (
        qlNonstandardSwapFixedSchedule(swap).startDate()
        == swap.fixedSchedule().startDate()
    )
    assert (
        qlNonstandardSwapFloatingSchedule(swap).endDate()
        == swap.floatingSchedule().endDate()
    )
    assert qlNonstandardSwapFixedRate(swap) == pytest.approx(swap.fixedRate())
    assert qlNonstandardSwapFixedDayCount(swap).name() == swap.fixedDayCount().name()
    assert qlNonstandardSwapIborIndex(swap).name() == swap.iborIndex().name()
    with pytest.raises(RuntimeError, match="spread is a vector"):
        qlNonstandardSwapSpread(swap)
    with pytest.raises(RuntimeError, match="gearing is a vector"):
        qlNonstandardSwapGearing(swap)
    assert qlNonstandardSwapSpreads(swap) == pytest.approx(swap.spreads())
    assert qlNonstandardSwapGearings(swap) == pytest.approx(swap.gearings())
    assert (
        qlNonstandardSwapFloatingDayCount(swap).name() == swap.floatingDayCount().name()
    )
    assert qlNonstandardSwapPaymentConvention(swap) == "FOLLOWING"
    assert len(qlNonstandardSwapFixedLeg(swap)) > 0
    assert len(qlNonstandardSwapFloatingLeg(swap)) > 0


def test_overnight_swap_and_make_ois_wrappers():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2024, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        discount_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
        )
        overnight_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.021, ql.Actual365Fixed())
        )
        sofr = ql.Sofr(overnight_curve)
        sched = _schedule(qlDate(2024, 1, 4), qlDate(2029, 1, 4), ql.Period("1Y"))

        ois = qlOvernightIndexedSwap(
            qSwapType.__wrapped__("PAYER"),
            1_000_000.0,
            sched,
            0.023,
            ql.Actual360(),
            sofr,
            spread=0.0005,
            payment_lag=2,
            payment_adjustment=ql.Following,
            averaging_method=ql.RateAveraging.Compound,
            lookback_days=0,
            lockout_days=0,
            apply_observation_shift=False,
        )
        ois.setPricingEngine(qlDiscountingSwapEngine(discount_curve))

        assert isinstance(ois, ql.OvernightIndexedSwap)
        assert qlOvernightIndexedSwapOvernightLegBPS(ois) == pytest.approx(
            ois.overnightLegBPS()
        )
        assert qlOvernightIndexedSwapOvernightLegNPV(ois) == pytest.approx(
            ois.overnightLegNPV()
        )
        assert qlOvernightIndexedSwapPaymentFrequency(ois) == "ANNUAL"
        assert qlOvernightIndexedSwapOvernightIndex(ois).name() == sofr.name()
        assert len(qlOvernightIndexedSwapOvernightLeg(ois)) > 0
        assert qlOvernightIndexedSwapAveragingMethod(ois) == "COMPOUND"
        assert qlOvernightIndexedSwapLookbackDays(ois) == 0
        assert qlOvernightIndexedSwapLockoutDays(ois) == 0
        assert qlOvernightIndexedSwapApplyObservationShift(ois) is False

        ois2 = qlOvernightIndexedSwap2(
            qSwapType.__wrapped__("PAYER"),
            [1_000_000.0],
            sched,
            0.023,
            ql.Actual360(),
            [1_000_000.0],
            sched,
            sofr,
        )
        assert isinstance(ois2, ql.OvernightIndexedSwap)

        made_ois = qlMakeOIS(
            ql.Period("5Y"),
            sofr,
            fixed_rate=0.023,
            nominal=1_000_000.0,
            settlement_days=0,
            effective_date=qlDate(2024, 1, 4),
            termination_date=qlDate(2029, 1, 4),
            discounting_term_structure=discount_curve,
            payment_frequency=ql.Annual,
            averaging_method=ql.RateAveraging.Compound,
        )
        assert isinstance(made_ois, ql.OvernightIndexedSwap)
    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_overnight_swap_index_wrappers():
    eval_date = qlDate(2024, 1, 2)
    overnight_curve = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.021, ql.Actual365Fixed())
    )
    sofr = ql.Sofr(overnight_curve)

    index = qlOvernightIndexedSwapIndex(
        "SOFR-OIS",
        ql.Period("1Y"),
        2,
        ql.USDCurrency(),
        sofr,
        False,
        ql.RateAveraging.Compound,
    )

    assert isinstance(index, ql.OvernightIndexedSwapIndex)
    assert qlOvernightIndexedSwapIndexOvernightIndex(index).name() == sofr.name()

    underlying = qlOvernightIndexedSwapIndexUnderlyingSwap(index, qlDate(2024, 1, 8))
    assert isinstance(underlying, ql.OvernightIndexedSwap)

    casted = qlAsOvernightSwapIndex(index)
    assert casted is None


def test_float_float_swap_constructor():
    eval_date = qlDate(2024, 1, 2)
    curve = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
    )
    index3m = ql.USDLibor(ql.Period("3M"), curve)
    index6m = ql.USDLibor(ql.Period("6M"), curve)

    schedule1 = _schedule(eval_date, qlDate(2026, 1, 2), ql.Period("3M"))
    schedule2 = _schedule(eval_date, qlDate(2026, 1, 2), ql.Period("6M"))

    swap = qlFloatFloatSwap(
        qSwapType.__wrapped__("PAYER"),
        [1_000_000.0] * (len(schedule1) - 1),
        [1_000_000.0] * (len(schedule2) - 1),
        schedule1,
        index3m,
        ql.Actual360(),
        schedule2,
        index6m,
        ql.Actual360(),
    )

    assert isinstance(swap, ql.FloatFloatSwap)
    assert swap.numberOfLegs() == 2
    assert len(swap.leg(0)) > 0
    assert len(swap.leg(1)) > 0


def test_zero_coupon_swap_wrappers_and_accessors():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2024, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
        )
        index6m = ql.USDLibor(ql.Period("6M"), curve)
        index6m.addFixing(ql.Date(28, 12, 2023), 0.02, True)

        zc_payment = qlZeroCouponSwap(
            qSwapType.__wrapped__("PAYER"),
            1_000_000.0,
            eval_date,
            qlDate(2026, 1, 2),
            60_000.0,
            index6m,
            qlCalendar("TARGET"),
        )
        assert isinstance(zc_payment, ql.ZeroCouponSwap)

        zc_rate = qlZeroCouponSwap2(
            qSwapType.__wrapped__("PAYER"),
            1_000_000.0,
            eval_date,
            qlDate(2026, 1, 2),
            0.03,
            ql.Actual365Fixed(),
            index6m,
            qlCalendar("TARGET"),
        )
        zc_rate.setPricingEngine(qlDiscountingSwapEngine(curve))

        assert isinstance(zc_rate, ql.ZeroCouponSwap)
        assert qlZeroCouponSwapType(zc_rate) == "PAYER"
        assert qlZeroCouponSwapBaseNominal(zc_rate) == pytest.approx(
            zc_rate.baseNominal()
        )
        assert qlZeroCouponSwapIborIndex(zc_rate).name() == zc_rate.iborIndex().name()
        assert len(qlZeroCouponSwapFixedLeg(zc_rate)) > 0
        assert len(qlZeroCouponSwapFloatingLeg(zc_rate)) > 0
        assert qlZeroCouponSwapFixedPayment(zc_rate) == pytest.approx(
            zc_rate.fixedPayment()
        )
        assert qlZeroCouponSwapFixedLegNPV(zc_rate) == pytest.approx(
            zc_rate.fixedLegNPV()
        )
        assert qlZeroCouponSwapFloatingLegNPV(zc_rate) == pytest.approx(
            zc_rate.floatingLegNPV()
        )
        assert qlZeroCouponSwapFairFixedPayment(zc_rate) == pytest.approx(
            zc_rate.fairFixedPayment()
        )
        assert qlZeroCouponSwapFairFixedRate(
            zc_rate, ql.Actual365Fixed()
        ) == pytest.approx(zc_rate.fairFixedRate(ql.Actual365Fixed()))
    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_equity_total_return_swap_wrappers_and_accessors():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2024, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        discount_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
        )
        forecast_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.021, ql.Actual365Fixed())
        )
        div_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.01, ql.Actual365Fixed())
        )

        ibor = ql.USDLibor(ql.Period("6M"), forecast_curve)
        sofr = ql.Sofr(forecast_curve)
        schedule = _schedule(qlDate(2024, 1, 4), qlDate(2026, 1, 4), ql.Period("6M"))

        equity_index = ql.EquityIndex(
            "SPX",
            qlCalendar("TARGET"),
            ql.USDCurrency(),
            discount_curve,
            div_curve,
            ql.QuoteHandle(ql.SimpleQuote(100.0)),
        )

        trs = qlEquityTotalReturnSwap(
            qSwapType.__wrapped__("PAYER"),
            1_000_000.0,
            schedule,
            equity_index,
            ibor,
            ql.Actual360(),
            0.001,
        )
        trs.setPricingEngine(qlDiscountingSwapEngine(discount_curve))

        assert isinstance(trs, ql.EquityTotalReturnSwap)
        assert qlEquityTotalReturnSwapType(trs) == "PAYER"
        assert qlEquityTotalReturnSwapNominal(trs) == pytest.approx(trs.nominal())
        assert (
            qlEquityTotalReturnSwapEquityIndex(trs).name() == trs.equityIndex().name()
        )
        assert (
            qlEquityTotalReturnSwapInterestRateIndex(trs).name()
            == trs.interestRateIndex().name()
        )
        assert (
            qlEquityTotalReturnSwapSchedule(trs).startDate()
            == trs.schedule().startDate()
        )
        assert qlEquityTotalReturnSwapDayCounter(trs).name() == trs.dayCounter().name()
        assert qlEquityTotalReturnSwapMargin(trs) == pytest.approx(trs.margin())
        assert qlEquityTotalReturnSwapGearing(trs) == pytest.approx(trs.gearing())
        assert (
            qlEquityTotalReturnSwapPaymentCalendar(trs).name()
            == trs.paymentCalendar().name()
        )
        assert qlEquityTotalReturnSwapPaymentConvention(trs) == "UNADJUSTED"
        assert qlEquityTotalReturnSwapPaymentDelay(trs) == trs.paymentDelay()
        assert len(qlEquityTotalReturnSwapEquityLeg(trs)) > 0
        assert len(qlEquityTotalReturnSwapInterestRateLeg(trs)) > 0
        assert qlEquityTotalReturnSwapEquityLegNPV(trs) == pytest.approx(
            trs.equityLegNPV()
        )
        assert qlEquityTotalReturnSwapInterestRateLegNPV(trs) == pytest.approx(
            trs.interestRateLegNPV()
        )
        assert qlEquityTotalReturnSwapFairMargin(trs) == pytest.approx(trs.fairMargin())

        trs_overnight = qlEquityTotalReturnSwap2(
            qSwapType.__wrapped__("RECEIVER"),
            1_000_000.0,
            schedule,
            equity_index,
            sofr,
            ql.Actual360(),
            0.001,
        )
        assert isinstance(trs_overnight, ql.EquityTotalReturnSwap)
    finally:
        ql.Settings.instance().evaluationDate = original_eval
