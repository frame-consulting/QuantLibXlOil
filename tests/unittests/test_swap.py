import QuantLib as ql
import pytest

from quantlib_xloil.calendars import qlCalendar
from quantlib_xloil.date import qlDate
from quantlib_xloil.swap import (
    qlAssetSwap,
    qlMakeMultipleResetsSwap,
    qlMultipleResetsSwap,
    qlMultipleResetsSwapAveragingMethod,
    qlMultipleResetsSwapFullResetSchedule,
    qlMultipleResetsSwapResetsPerCoupon,
    qSwapType,
    qlAsOvernightSwapIndex,
    qlEquityTotalReturnSwap,
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

        engine = qlDiscountingSwapEngine(discount_curve, True)
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
        zc_rate.setPricingEngine(qlDiscountingSwapEngine(curve, True))

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


def test_asset_swap_wrapper():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2024, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
        )
        ibor_index = ql.USDLibor(ql.Period("6M"), curve)
        ibor_index.addFixing(ql.Date(28, 12, 2023), 0.02, True)

        issue_date = qlDate(2024, 1, 2)
        maturity_date = qlDate(2028, 1, 2)
        bond_schedule = _schedule(issue_date, maturity_date, ql.Period("1Y"))

        bond = ql.FixedRateBond(
            2,
            1_000_000.0,
            bond_schedule,
            [0.03],
            ql.ActualActual(ql.ActualActual.Bond),
        )

        float_schedule = _schedule(eval_date, qlDate(2028, 1, 2), ql.Period("6M"))

        asset_swap = qlAssetSwap(
            pay_fixed_rate=True,
            bond=bond,
            bond_clean_price=100.0,
            index=ibor_index,
            spread=0.005,
            float_schedule=float_schedule,
            par_asset_swap=True,
        )

        assert isinstance(asset_swap, ql.AssetSwap)
    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_overnight_indexed_swap_constructor_and_accessors():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2024, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        overnight_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.021, ql.Actual365Fixed())
        )
        sofr = ql.Sofr(overnight_curve)
        sofr.addFixing(ql.Date(29, 12, 2023), 0.021)

        ois_schedule = _schedule(eval_date, qlDate(2026, 1, 2), ql.Period("3M"))

        ois = qlOvernightIndexedSwap(
            qSwapType.__wrapped__("PAYER"),
            nominal=1_000_000.0,
            schedule=ois_schedule,
            fixed_rate=0.025,
            fixed_dc=ql.Actual360(),
            index=sofr,
            spread=0.001,
            payment_lag=2,
            payment_adjustment=ql.Following,
            payment_calendar=qlCalendar("TARGET"),
            averaging_method=ql.RateAveraging.Compound,
            lookback_days=1,
            lockout_days=1,
            apply_observation_shift=True,
        )

        assert isinstance(ois, ql.OvernightIndexedSwap)

        assert qlSwapNumberOfLegs(ois) == 2
        assert qlSwapStartDate(ois) == eval_date
        assert qlSwapMaturityDate(ois) == ois_schedule.endDate()
        assert qlSwapPayer(ois, 0) is True
        assert qlSwapPayer(ois, 1) is False

        assert qlOvernightIndexedSwapOvernightIndex(ois).name() == sofr.name()
        assert qlOvernightIndexedSwapAveragingMethod(ois) == "COMPOUND"
        assert qlOvernightIndexedSwapLookbackDays(ois) == 1
        assert qlOvernightIndexedSwapLockoutDays(ois) == 1
        assert qlOvernightIndexedSwapApplyObservationShift(ois) is True
        assert qlOvernightIndexedSwapPaymentFrequency(ois) == "QUARTERLY"

        overnight_leg = qlOvernightIndexedSwapOvernightLeg(ois)
        assert len(overnight_leg) > 0

        discount_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
        )
        engine = qlDiscountingSwapEngine(discount_curve, False)
        ois.setPricingEngine(engine)

        assert qlOvernightIndexedSwapOvernightLegNPV(ois) == pytest.approx(
            ois.overnightLegNPV()
        )
        assert qlOvernightIndexedSwapOvernightLegBPS(ois) == pytest.approx(
            ois.overnightLegBPS()
        )

        assert qlSwapLegNPV(ois, 1) == pytest.approx(ois.legNPV(1))
        assert qlSwapLegBPS(ois, 1) == pytest.approx(ois.legBPS(1))

        assert isinstance(ois.NPV(), float)

    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_multiple_resets_swap_constructor_and_accessors():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2024, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        forecast_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
        )
        ibor_index = ql.USDLibor(ql.Period("6M"), forecast_curve)
        ibor_index.addFixing(ql.Date(28, 12, 2023), 0.02)

        fixed_schedule = _schedule(eval_date, qlDate(2026, 1, 2), ql.Period("1Y"))
        full_reset_schedule = _schedule(eval_date, qlDate(2026, 1, 2), ql.Period("3M"))

        mrs = qlMultipleResetsSwap(
            qSwapType.__wrapped__("PAYER"),
            nominal=1_000_000.0,
            fixed_schedule=fixed_schedule,
            fixed_rate=0.025,
            fixed_day_count=ql.Thirty360(ql.Thirty360.BondBasis),
            full_reset_schedule=full_reset_schedule,
            ibor_index=ibor_index,
            resets_per_coupon=4,
            spread=0.001,
            averaging_method=ql.RateAveraging.Compound,
            payment_convention=ql.Following,
            payment_lag=2,
            payment_calendar=qlCalendar("TARGET"),
        )

        assert isinstance(mrs, ql.MultipleResetsSwap)

        assert qlSwapNumberOfLegs(mrs) == 2
        assert qlSwapStartDate(mrs) == eval_date
        assert qlSwapMaturityDate(mrs) == full_reset_schedule.endDate()
        assert qlSwapPayer(mrs, 0) is True
        assert qlSwapPayer(mrs, 1) is False

        full_reset_schedule_result = qlMultipleResetsSwapFullResetSchedule(mrs)
        assert full_reset_schedule_result.startDate() == full_reset_schedule.startDate()
        assert full_reset_schedule_result.endDate() == full_reset_schedule.endDate()
        assert qlMultipleResetsSwapResetsPerCoupon(mrs) == 4
        assert qlMultipleResetsSwapAveragingMethod(mrs) == "COMPOUND"

        fixed_leg = qlSwapLeg(mrs, 0)
        assert len(fixed_leg) > 0

        floating_leg = qlSwapLeg(mrs, 1)
        assert len(floating_leg) > 0

        discount_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.019, ql.Actual365Fixed())
        )
        engine = qlDiscountingSwapEngine(discount_curve, True)
        mrs.setPricingEngine(engine)

        assert qlSwapLegNPV(mrs, 0) == pytest.approx(mrs.legNPV(0))
        assert qlSwapLegNPV(mrs, 1) == pytest.approx(mrs.legNPV(1))
        assert qlSwapLegBPS(mrs, 0) == pytest.approx(mrs.legBPS(0))
        assert qlSwapLegBPS(mrs, 1) == pytest.approx(mrs.legBPS(1))

        assert isinstance(mrs.NPV(), float)

    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_make_multiple_resets_swap_helper():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2024, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        forecast_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
        )
        ibor_index = ql.USDLibor(ql.Period("6M"), forecast_curve)
        ibor_index.addFixing(ql.Date(28, 12, 2023), 0.02)

        discount_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.019, ql.Actual365Fixed())
        )

        mrs = qlMakeMultipleResetsSwap(
            swap_tenor=ql.Period("1Y"),
            ibor_index=ibor_index,
            resets_per_coupon=3,
            receive_fixed=True,
            nominal=1_000_000.0,
            fixed_rate=0.025,
            fixed_leg_frequency=ql.Annual,
            fixed_leg_day_count=ql.Thirty360(ql.Thirty360.BondBasis),
            floating_leg_spread=0.001,
            averaging_method=ql.RateAveraging.Compound,
            discounting_term_structure=discount_curve,
        )

        assert isinstance(mrs, ql.MultipleResetsSwap)

        assert qlSwapNumberOfLegs(mrs) == 2
        assert (
            qlSwapStartDate(mrs) >= eval_date
        )  # Start date may be adjusted by settlement days
        assert qlSwapPayer(mrs, 0) is False  # receive fixed
        assert qlSwapPayer(mrs, 1) is True

        assert qlMultipleResetsSwapResetsPerCoupon(mrs) == 3
        assert qlMultipleResetsSwapAveragingMethod(mrs) == "COMPOUND"

        full_reset_schedule = qlMultipleResetsSwapFullResetSchedule(mrs)
        assert (
            full_reset_schedule.startDate() >= eval_date
        )  # May be adjusted by settlement days
        assert full_reset_schedule.endDate() > eval_date

        fixed_leg = qlSwapLeg(mrs, 0)
        assert len(fixed_leg) > 0

        floating_leg = qlSwapLeg(mrs, 1)
        assert len(floating_leg) > 0

        engine = qlDiscountingSwapEngine(discount_curve, True)
        mrs.setPricingEngine(engine)

        assert qlSwapLegNPV(mrs, 0) == pytest.approx(mrs.legNPV(0))
        assert qlSwapLegNPV(mrs, 1) == pytest.approx(mrs.legNPV(1))
        assert qlSwapLegBPS(mrs, 0) == pytest.approx(mrs.legBPS(0))
        assert qlSwapLegBPS(mrs, 1) == pytest.approx(mrs.legBPS(1))

        assert isinstance(mrs.NPV(), float)

    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_equity_total_return_swap_constructor_and_accessors():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2024, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
        )
        ibor_index = ql.USDLibor(ql.Period("6M"), curve)
        ibor_index.addFixing(ql.Date(28, 12, 2023), 0.02)

        schedule = _schedule(eval_date, qlDate(2026, 1, 2), ql.Period("1Y"))

        # Create a simple equity index with interest rate term structure
        equity_ts = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.015, ql.Actual365Fixed())
        )
        equity_index = ql.EquityIndex(
            "TEST_INDEX",
            ql.TARGET(),  # fixing calendar
            ql.USDCurrency(),
            equity_ts,  # interest rate term structure
        )
        equity_index.addFixing(ql.Date(2, 1, 2024), 100.0)
        equity_index.addFixing(ql.Date(2, 1, 2025), 105.0)

        etrs = qlEquityTotalReturnSwap(
            qSwapType.__wrapped__("PAYER"),
            nominal=1_000_000.0,
            schedule=schedule,
            equity_index=equity_index,
            interest_rate_index=ibor_index,
            day_counter=ql.Actual365Fixed(),
            margin=0.01,
            gearing=1.0,
            payment_calendar=qlCalendar("TARGET"),
            payment_convention=ql.Following,
            payment_delay=2,
        )

        assert isinstance(etrs, ql.EquityTotalReturnSwap)

        assert qlEquityTotalReturnSwapType(etrs) == "PAYER"
        assert qlEquityTotalReturnSwapNominal(etrs) == pytest.approx(1_000_000.0)
        assert qlEquityTotalReturnSwapMargin(etrs) == pytest.approx(0.01)
        assert qlEquityTotalReturnSwapGearing(etrs) == pytest.approx(1.0)

        assert qlEquityTotalReturnSwapEquityIndex(etrs).name() == "TEST_INDEX"
        assert (
            qlEquityTotalReturnSwapInterestRateIndex(etrs).name() == ibor_index.name()
        )
        assert (
            qlEquityTotalReturnSwapDayCounter(etrs).name() == ql.Actual365Fixed().name()
        )
        assert qlEquityTotalReturnSwapSchedule(etrs).startDate() == eval_date

        assert qlEquityTotalReturnSwapPaymentCalendar(etrs).name() == "TARGET"
        assert qlEquityTotalReturnSwapPaymentConvention(etrs) == "FOLLOWING"
        assert qlEquityTotalReturnSwapPaymentDelay(etrs) == 2

        equity_leg = qlEquityTotalReturnSwapEquityLeg(etrs)
        assert len(equity_leg) > 0

        interest_leg = qlEquityTotalReturnSwapInterestRateLeg(etrs)
        assert len(interest_leg) > 0

        discount_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.019, ql.Actual365Fixed())
        )
        engine = qlDiscountingSwapEngine(discount_curve, True)
        etrs.setPricingEngine(engine)

        assert qlEquityTotalReturnSwapEquityLegNPV(etrs) == pytest.approx(
            etrs.equityLegNPV()
        )
        assert qlEquityTotalReturnSwapInterestRateLegNPV(etrs) == pytest.approx(
            etrs.interestRateLegNPV()
        )
        assert qlEquityTotalReturnSwapFairMargin(etrs) == pytest.approx(
            etrs.fairMargin()
        )

        assert isinstance(etrs.NPV(), float)

    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_overnight_indexed_swap2_constructor_and_accessors():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2024, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        overnight_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.021, ql.Actual365Fixed())
        )
        sofr = ql.Sofr(overnight_curve)
        sofr.addFixing(ql.Date(29, 12, 2023), 0.021)

        fixed_schedule = _schedule(eval_date, qlDate(2026, 1, 2), ql.Period("1Y"))
        overnight_schedule = _schedule(eval_date, qlDate(2026, 1, 2), ql.Period("3M"))

        n_fixed = len(fixed_schedule) - 1
        n_overnight = len(overnight_schedule) - 1

        ois = qlOvernightIndexedSwap2(
            qSwapType.__wrapped__("RECEIVER"),
            fixed_nominals=[1_000_000.0] * n_fixed,
            fixed_schedule=fixed_schedule,
            fixed_rate=0.025,
            fixed_dc=ql.Actual360(),
            overnight_nominals=[1_000_000.0] * n_overnight,
            overnight_schedule=overnight_schedule,
            overnight_index=sofr,
            spread=0.0,
            payment_lag=0,
            payment_adjustment=ql.Following,
            payment_calendar=ql.TARGET(),
        )

        assert isinstance(ois, ql.OvernightIndexedSwap)

        assert qlSwapNumberOfLegs(ois) == 2
        assert qlSwapStartDate(ois) == eval_date
        assert qlSwapMaturityDate(ois) == overnight_schedule.endDate()
        assert qlSwapPayer(ois, 0) is False
        assert qlSwapPayer(ois, 1) is True

        assert qlOvernightIndexedSwapOvernightIndex(ois).name() == sofr.name()
        assert qlOvernightIndexedSwapAveragingMethod(ois) == "COMPOUND"

        overnight_leg = qlOvernightIndexedSwapOvernightLeg(ois)
        assert len(overnight_leg) > 0

        fixed_leg = qlSwapLeg(ois, 0)
        assert len(fixed_leg) == n_fixed

        discount_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
        )
        engine = qlDiscountingSwapEngine(discount_curve, True)
        ois.setPricingEngine(engine)

        assert qlOvernightIndexedSwapOvernightLegNPV(ois) == pytest.approx(
            ois.overnightLegNPV()
        )
        assert qlOvernightIndexedSwapOvernightLegBPS(ois) == pytest.approx(
            ois.overnightLegBPS()
        )

        assert qlSwapLegNPV(ois, 0) == pytest.approx(ois.legNPV(0))
        assert qlSwapLegNPV(ois, 1) == pytest.approx(ois.legNPV(1))
        assert qlSwapLegBPS(ois, 0) == pytest.approx(ois.legBPS(0))
        assert qlSwapLegBPS(ois, 1) == pytest.approx(ois.legBPS(1))

        assert isinstance(ois.NPV(), float)

    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_ql_make_ois_constructor_and_pricing():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2024, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        overnight_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.021, ql.Actual365Fixed())
        )
        discount_curve = ql.YieldTermStructureHandle(
            ql.FlatForward(eval_date, 0.02, ql.Actual365Fixed())
        )
        sofr = ql.Sofr(overnight_curve)
        sofr.addFixing(ql.Date(29, 12, 2023), 0.021)

        ois = qlMakeOIS(
            swap_tenor=ql.Period("2Y"),
            overnight_index=sofr,
            fixed_rate=0.025,
        )

        assert isinstance(ois, ql.OvernightIndexedSwap)
        assert qlSwapNumberOfLegs(ois) == 2
        assert qlSwapStartDate(ois) >= eval_date
        assert qlSwapMaturityDate(ois) > eval_date
        assert qlSwapPayer(ois, 0) is True
        assert qlSwapPayer(ois, 1) is False

        engine = qlDiscountingSwapEngine(discount_curve, True)
        ois.setPricingEngine(engine)
        assert isinstance(ois.NPV(), float)

        ois_custom = qlMakeOIS(
            swap_tenor=ql.Period("3Y"),
            overnight_index=sofr,
            fixed_rate=0.028,
            receive_fixed=False,
            nominal=2_000_000.0,
            settlement_days=2,
            payment_frequency=ql.Semiannual,
            fixed_leg_day_count=ql.Actual360(),
            overnight_leg_spread=0.001,
            averaging_method=ql.RateAveraging.Compound,
            payment_lag=2,
            payment_calendar=qlCalendar("TARGET"),
            payment_adjustment_convention=ql.Following,
            end_of_month=True,
            discounting_term_structure=discount_curve,
            pricing_engine=engine,
        )

        assert isinstance(ois_custom, ql.OvernightIndexedSwap)
        assert qlSwapNumberOfLegs(ois_custom) == 2
        assert qlSwapPayer(ois_custom, 0) is True
        assert qlSwapPayer(ois_custom, 1) is False

        # Verify the overnight index
        assert qlOvernightIndexedSwapOvernightIndex(ois_custom).name() == sofr.name()
        assert qlOvernightIndexedSwapAveragingMethod(ois_custom) == "COMPOUND"

        # Test leg accessors
        overnight_leg = qlOvernightIndexedSwapOvernightLeg(ois_custom)
        assert len(overnight_leg) > 0

        # Test NPV and BPS calculations
        assert qlOvernightIndexedSwapOvernightLegNPV(ois_custom) == pytest.approx(
            ois_custom.overnightLegNPV()
        )
        assert qlOvernightIndexedSwapOvernightLegBPS(ois_custom) == pytest.approx(
            ois_custom.overnightLegBPS()
        )
        assert qlSwapLegNPV(ois_custom, 0) == pytest.approx(ois_custom.legNPV(0))
        assert qlSwapLegNPV(ois_custom, 1) == pytest.approx(ois_custom.legNPV(1))
        assert qlSwapLegBPS(ois_custom, 0) == pytest.approx(ois_custom.legBPS(0))
        assert qlSwapLegBPS(ois_custom, 1) == pytest.approx(ois_custom.legBPS(1))

        # Test 3: OIS with swap_type parameter
        ois_type = qlMakeOIS(
            swap_tenor=ql.Period("1Y"),
            overnight_index=sofr,
            fixed_rate=0.022,
            swap_type="RECEIVER",
            nominal=1_000_000.0,
            discounting_term_structure=discount_curve,
            pricing_engine=engine,
        )

        assert isinstance(ois_type, ql.OvernightIndexedSwap)
        assert qlSwapPayer(ois_type, 0) is False

        assert isinstance(ois_type.NPV(), float)

    finally:
        ql.Settings.instance().evaluationDate = original_eval
