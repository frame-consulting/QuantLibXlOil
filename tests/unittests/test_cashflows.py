import QuantLib as ql
import pytest

from quantlib_xloil.date import _qFrequency
from quantlib_xloil.termstructures import _qCompounding
from quantlib_xloil.cashflows import _qDurationType, _qRateAveragingType

from quantlib_xloil import (
    qlCalendar,
    qlDate,
    qlDayCounter,
    qlSimpleCashFlow,
    qlCashFlowAmount,
    qlCashFlowDate,
    qlCashFlowHasOccurred,
    qlAsCoupon,
    qlFixedRateCoupon,
    qlIborCoupon,
    qlCouponNominal,
    qlCouponAccrualStartDate,
    qlCouponAccrualEndDate,
    qlCouponReferencePeriodStart,
    qlCouponReferencePeriodEnd,
    qlCouponExCouponDate,
    qlCouponRate,
    qlCouponAccrualPeriod,
    qlCouponAccrualDays,
    qlCouponDayCounter,
    qlCouponAccruedAmount,
    qlFloatingRateCouponFixingDate,
    qlFloatingRateCouponFixingDays,
    qlFloatingRateCouponIsInArrears,
    qlFloatingRateCouponGearing,
    qlFloatingRateCouponSpread,
    qlFloatingRateCouponIndexFixing,
    qlFloatingRateCouponAdjustedFixing,
    qlFloatingRateCouponConvexityAdjustment,
    qlFloatingRateCouponPrice,
    qlFloatingRateCouponIndex,
    qlFloatingRateCouponSetPricer,
    qlCappedFlooredCouponIsCapped,
    qlCappedFlooredCouponIsFloored,
    qlCappedFlooredCouponCap,
    qlCappedFlooredCouponFloor,
    qlCappedFlooredCouponEffectiveCap,
    qlCappedFlooredCouponEffectiveFloor,
    qlOvernightIndexedCouponAveragingMethod,
    qlOvernightIndexedCouponCanApplyTelescopicFormula,
    qlOvernightIndexedCouponApplyObservationShift,
    qlOvernightIndexedCouponCompoundSpreadDaily,
    qlOvernightIndexedCouponLockoutDays,
    qlOvernightIndexedCouponRateComputationStartDate,
    qlOvernightIndexedCouponRateComputationEndDate,
    qlOvernightIndexedCouponValueDates,
    qlOvernightIndexedCouponFixingDates,
    qlOvernightIndexedCouponInterestDates,
    qlOvernightIndexedCouponDt,
    qlOvernightIndexedCouponIndexFixings,
    qlOvernightIndexedCouponEffectiveIndexFixing,
    qlOvernightIndexedCouponEffectiveSpread,
    qlCappedFlooredOvernightIndexedCouponUnderlying,
    qlCappedFlooredOvernightIndexedCouponNakedOption,
    qlCappedFlooredOvernightIndexedCouponDailyCapFloor,
    qlCappedFlooredOvernightIndexedCouponAveragingMethod,
    qlCappedFlooredOvernightIndexedCouponCompoundSpreadDaily,
    qlCappedFlooredOvernightIndexedCouponEffectiveCapletVolatility,
    qlCappedFlooredOvernightIndexedCouponEffectiveFloorletVolatility,
    qlFixedRateLeg,
    qlIborLeg,
    qlEuribor,
    qlSofr,
    qlCappedFlooredIborCoupon,
    qlOvernightIndexedCoupon,
    qlFlatForward,
    qlCashFlowsStartDate,
    qlCashFlowsMaturityDate,
    qlCashFlowsPreviousCashFlow,
    qlCashFlowsNextCashFlow,
    qlCashFlowsAccrualPeriod,
    qlCashFlowsAccrualDays,
    qlCashFlowsAccruedPeriod,
    qlCashFlowsAccruedDays,
    qlCashFlowsAccruedAmount,
    qlCashFlowsNpv,
    qlCashFlowsBps,
    qlCashFlowsBpsFromInterestRate,
    qlCashFlowsBpsFromRate,
    qlCashFlowsNpvBps,
    qlCashFlowsAtmRate,
    qlCashFlowsYieldRate,
    qlCashFlowsDurationFromRate,
    qlCashFlowsConvexityFromInterestRate,
    qlCashFlowsBasisPointValueFromInterestRate,
    qlCashFlowsBasisPointValueFromRate,
    qlCashFlowsZSpread,
    qlBlackIborCouponPricer,
    qlSetCouponPricer,
    qlCappedFlooredOvernightIndexedCoupon,
    qlAsOvernightIndexedCoupon,
    qlAsCappedFlooredOvernightIndexedCoupon,
    qlBlackCompoundingOvernightIndexedCouponPricer,
    qlBlackAveragingOvernightIndexedCouponPricer,
    qlCompoundingMultipleResetsPricer,
    qlAveragingMultipleResetsPricer,
)


def _schedule(start: ql.Date, end: ql.Date) -> ql.Schedule:
    return ql.Schedule(
        start,
        end,
        ql.Period(ql.Annual),
        qlCalendar("TARGET"),
        ql.Unadjusted,
        ql.Unadjusted,
        ql.DateGeneration.Forward,
        False,
    )


def _curve(reference_date: ql.Date, rate: float = 0.05) -> ql.YieldTermStructureHandle:
    return qlFlatForward(
        reference_date,
        rate,
        qlDayCounter("ACTUAL365FIXED"),
        _qCompounding("COMPOUNDED"),
        _qFrequency("ANNUAL"),
        qlCalendar("TARGET"),
    )


def test_cashflow_converters():
    assert _qDurationType("simple") == ql.Duration.Simple
    assert _qDurationType("MODIFIED") == ql.Duration.Modified
    assert _qRateAveragingType("compound") == ql.RateAveraging.Compound


def test_simple_cashflow_accessors_and_cast():
    payment_date = qlDate(2025, 1, 2)
    cf = qlSimpleCashFlow(12.5, payment_date)

    assert qlCashFlowAmount(cf) == 12.5
    assert qlCashFlowDate(cf) == payment_date
    assert qlCashFlowHasOccurred(cf, qlDate(2024, 12, 31)) is False
    assert qlAsCoupon(cf) is None


def test_coupon_methods_on_fixed_rate_coupon():
    start_date = qlDate(2024, 1, 2)
    end_date = qlDate(2025, 1, 2)
    payment_date = end_date
    ref_period_start = start_date
    ref_period_end = end_date
    ex_coupon_date = ql.Date()
    day_counter = qlDayCounter("ACTUAL365FIXED")

    coupon = qlFixedRateCoupon(
        payment_date,
        100.0,
        0.05,
        day_counter,
        start_date,
        end_date,
        ref_period_start,
        ref_period_end,
        ex_coupon_date,
    )

    assert qlCouponNominal(coupon) == 100.0
    assert qlCouponAccrualStartDate(coupon) == start_date
    assert qlCouponAccrualEndDate(coupon) == end_date
    assert qlCouponReferencePeriodStart(coupon) == ref_period_start
    assert qlCouponReferencePeriodEnd(coupon) == ref_period_end
    assert qlCouponExCouponDate(coupon) == ex_coupon_date
    assert qlCouponRate(coupon) == 0.05
    assert qlCouponAccrualPeriod(coupon) > 0.0
    assert qlCouponAccrualDays(coupon) > 0
    assert qlCouponDayCounter(coupon).name() == day_counter.name()
    assert qlCouponAccruedAmount(coupon, qlDate(2024, 7, 2)) > 0.0


def test_floatingratecoupon_methods_on_ibor_coupon():
    original_eval = ql.Settings.instance().evaluationDate

    start_date = qlDate(2024, 7, 2)
    end_date = qlDate(2025, 1, 2)
    payment_date = end_date
    fixing_days = 2
    day_counter = qlDayCounter("ACTUAL365FIXED")
    curve = _curve(qlDate(2024, 1, 2), 0.03)
    index = qlEuribor(ql.Period("6M"), curve)

    # Force forecasting path (instead of historical fixing lookup) for deterministic tests.
    ql.Settings.instance().evaluationDate = qlDate(2024, 1, 2)

    coupon = qlIborCoupon(
        payment_date,
        100.0,
        start_date,
        end_date,
        fixing_days,
        index,
        1.0,
        0.001,
        start_date,
        end_date,
        day_counter,
        False,
        ql.Date(),
    )

    assert qlFloatingRateCouponFixingDate(coupon) < start_date
    assert qlFloatingRateCouponFixingDays(coupon) == fixing_days
    assert qlFloatingRateCouponIsInArrears(coupon) is False
    assert qlFloatingRateCouponGearing(coupon) == 1.0
    assert qlFloatingRateCouponSpread(coupon) == 0.001

    try:
        index_fixing = qlFloatingRateCouponIndexFixing(coupon)
        adjusted_fixing = qlFloatingRateCouponAdjustedFixing(coupon)
        convexity_adjustment = qlFloatingRateCouponConvexityAdjustment(coupon)
        price = qlFloatingRateCouponPrice(coupon, curve)

        assert index_fixing > 0.0
        assert adjusted_fixing > 0.0
        assert convexity_adjustment >= 0.0
        assert price > 0.0
        assert qlFloatingRateCouponIndex(coupon) is not None

        pricer = qlBlackIborCouponPricer()
        assert qlFloatingRateCouponSetPricer(coupon, pricer) is True
    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_cappedflooredcoupon_methods_on_cappedfloored_ibor_coupon():
    start_date = qlDate(2024, 7, 2)
    end_date = qlDate(2025, 1, 2)
    payment_date = end_date
    fixing_days = 2
    day_counter = qlDayCounter("ACTUAL365FIXED")
    curve = _curve(qlDate(2024, 1, 2), 0.03)
    index = qlEuribor(ql.Period("6M"), curve)

    coupon = qlCappedFlooredIborCoupon(
        payment_date,
        100.0,
        start_date,
        end_date,
        fixing_days,
        index,
        1.0,
        0.0,
        0.06,
        0.01,
        start_date,
        end_date,
        day_counter,
        False,
        ql.Date(),
    )

    assert qlCappedFlooredCouponIsCapped(coupon) is True
    assert qlCappedFlooredCouponIsFloored(coupon) is True
    assert qlCappedFlooredCouponCap(coupon) == 0.06
    assert qlCappedFlooredCouponFloor(coupon) == 0.01
    assert qlCappedFlooredCouponEffectiveCap(coupon) == 0.06
    assert qlCappedFlooredCouponEffectiveFloor(coupon) == 0.01


def test_overnightindexedcoupon_methods_on_sofr_coupon():
    original_eval = ql.Settings.instance().evaluationDate

    start_date = qlDate(2024, 1, 2)
    end_date = qlDate(2024, 7, 2)
    payment_date = end_date
    day_counter = qlDayCounter("ACTUAL365FIXED")
    curve = _curve(start_date, 0.03)
    index = qlSofr(curve)

    # Force forecasting path for stable fixing-dependent quantities.
    ql.Settings.instance().evaluationDate = start_date

    coupon = qlOvernightIndexedCoupon(
        payment_date,
        100.0,
        start_date,
        end_date,
        index,
        1.0,
        0.0,
        start_date,
        end_date,
        day_counter,
        False,
        _qRateAveragingType("COMPOUND"),
        ql.nullInt(),
        0,
        False,
        False,
    )

    try:
        assert qlOvernightIndexedCouponAveragingMethod(coupon) == "COMPOUND"
        assert isinstance(qlOvernightIndexedCouponCanApplyTelescopicFormula(coupon), bool)
        assert qlOvernightIndexedCouponApplyObservationShift(coupon) is False
        assert qlOvernightIndexedCouponCompoundSpreadDaily(coupon) is False
        assert qlOvernightIndexedCouponLockoutDays(coupon) == 0

        assert qlOvernightIndexedCouponRateComputationStartDate(coupon) is not None
        assert qlOvernightIndexedCouponRateComputationEndDate(coupon) is not None

        value_dates = qlOvernightIndexedCouponValueDates(coupon)
        fixing_dates = qlOvernightIndexedCouponFixingDates(coupon)
        interest_dates = qlOvernightIndexedCouponInterestDates(coupon)
        dt = qlOvernightIndexedCouponDt(coupon)
        index_fixings = qlOvernightIndexedCouponIndexFixings(coupon)

        assert len(value_dates) > 1
        assert len(fixing_dates) == len(value_dates) - 1
        assert len(interest_dates) == len(value_dates)
        assert len(dt) == len(fixing_dates)
        assert len(index_fixings) == len(fixing_dates)
        assert qlOvernightIndexedCouponEffectiveIndexFixing(coupon) > 0.0
        assert qlOvernightIndexedCouponEffectiveSpread(coupon) == 0.0
    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_cappedflooredovernightindexedcoupon_methods():
    original_eval = ql.Settings.instance().evaluationDate

    start_date = qlDate(2024, 1, 2)
    end_date = qlDate(2024, 7, 2)
    payment_date = end_date
    day_counter = qlDayCounter("ACTUAL365FIXED")
    curve = _curve(start_date, 0.03)
    index = qlSofr(curve)

    ql.Settings.instance().evaluationDate = start_date

    underlying = qlOvernightIndexedCoupon(
        payment_date,
        100.0,
        start_date,
        end_date,
        index,
        1.0,
        0.0,
        start_date,
        end_date,
        day_counter,
        False,
        _qRateAveragingType("COMPOUND"),
        ql.nullInt(),
        0,
        False,
        False,
    )
    coupon = qlCappedFlooredOvernightIndexedCoupon(underlying, 0.06, 0.01, False, False)

    try:
        assert qlCappedFlooredOvernightIndexedCouponUnderlying(coupon) is not None
        assert qlCappedFlooredOvernightIndexedCouponNakedOption(coupon) is False
        assert qlCappedFlooredOvernightIndexedCouponDailyCapFloor(coupon) is False
        assert qlCappedFlooredOvernightIndexedCouponAveragingMethod(coupon) == "COMPOUND"
        assert qlCappedFlooredOvernightIndexedCouponCompoundSpreadDaily(coupon) is False

        # These two accessors require a compatible pricer setup in QuantLib.
        with pytest.raises(RuntimeError):
            qlCappedFlooredOvernightIndexedCouponEffectiveCapletVolatility(coupon)
        with pytest.raises(RuntimeError):
            qlCappedFlooredOvernightIndexedCouponEffectiveFloorletVolatility(coupon)
    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_fixed_rate_leg_cashflows_analytics():
    start = qlDate(2024, 1, 2)
    end = qlDate(2027, 1, 2)
    schedule = _schedule(start, end)
    day_counter = qlDayCounter("ACTUAL365FIXED")

    leg = qlFixedRateLeg(schedule, day_counter, [100.0], [0.05])
    curve = _curve(start, 0.05)

    assert qlCashFlowsStartDate(leg) == start
    assert qlCashFlowsMaturityDate(leg) == end

    npv = qlCashFlowsNpv(leg, curve, False)
    ytm = qlCashFlowsYieldRate(
        leg,
        npv,
        day_counter,
        _qCompounding("COMPOUNDED"),
        _qFrequency("ANNUAL"),
        False,
    )
    duration = qlCashFlowsDurationFromRate(
        leg,
        ytm,
        day_counter,
        _qCompounding("COMPOUNDED"),
        _qFrequency("ANNUAL"),
        _qDurationType("MODIFIED"),
        False,
    )
    bpv = qlCashFlowsBasisPointValueFromRate(
        leg,
        ytm,
        day_counter,
        _qCompounding("COMPOUNDED"),
        _qFrequency("ANNUAL"),
        False,
    )
    z_spread = qlCashFlowsZSpread(
        leg,
        npv,
        curve.currentLink(),
        day_counter,
        _qCompounding("COMPOUNDED"),
        _qFrequency("ANNUAL"),
        False,
    )

    assert npv > 0.0
    assert ytm > 0.0
    assert duration > 0.0
    assert abs(bpv) > 0.0
    assert abs(z_spread) < 1.0e-6


def test_cashflows_step3_objects_and_accruals():
    start = qlDate(2024, 1, 2)
    end = qlDate(2027, 1, 2)
    schedule = _schedule(start, end)
    day_counter = qlDayCounter("ACTUAL365FIXED")
    leg = qlFixedRateLeg(schedule, day_counter, [100.0], [0.05])

    # Settlement before first coupon: only next cash flow should exist.
    settlement_early = qlDate(2024, 1, 15)
    prev_cf_early = qlCashFlowsPreviousCashFlow(leg, False, settlement_early)
    next_cf_early = qlCashFlowsNextCashFlow(leg, False, settlement_early)
    assert prev_cf_early is None
    assert next_cf_early is not None

    # Settlement after maturity: only previous cash flow should exist.
    settlement_late = qlDate(2028, 1, 15)
    prev_cf_late = qlCashFlowsPreviousCashFlow(leg, False, settlement_late)
    next_cf_late = qlCashFlowsNextCashFlow(leg, False, settlement_late)
    assert prev_cf_late is not None
    assert next_cf_late is None

    accrual_period = qlCashFlowsAccrualPeriod(leg, False, settlement_early)
    accrual_days = qlCashFlowsAccrualDays(leg, False, settlement_early)
    accrued_period = qlCashFlowsAccruedPeriod(leg, False, settlement_early)
    accrued_days = qlCashFlowsAccruedDays(leg, False, settlement_early)
    accrued_amount = qlCashFlowsAccruedAmount(leg, False, settlement_early)

    assert accrual_period > 0.0
    assert accrual_days > 0
    assert accrued_period >= 0.0
    assert accrued_days >= 0
    assert accrued_amount >= 0.0


def test_cashflows_step3_empty_leg_edge_cases():
    empty_leg = []
    settlement = qlDate(2024, 1, 2)

    assert qlCashFlowsPreviousCashFlow(empty_leg, False, settlement) is None
    assert qlCashFlowsNextCashFlow(empty_leg, False, settlement) is None
    assert qlCashFlowsAccrualPeriod(empty_leg, False, settlement) == 0.0
    assert qlCashFlowsAccrualDays(empty_leg, False, settlement) == 0
    assert qlCashFlowsAccruedPeriod(empty_leg, False, settlement) == 0.0
    assert qlCashFlowsAccruedDays(empty_leg, False, settlement) == 0
    assert qlCashFlowsAccruedAmount(empty_leg, False, settlement) == 0.0


def test_cashflows_overload_analytics_step2():
    start = qlDate(2024, 1, 2)
    end = qlDate(2027, 1, 2)
    schedule = _schedule(start, end)
    day_counter = qlDayCounter("ACTUAL365FIXED")
    compounding = _qCompounding("COMPOUNDED")
    frequency = _qFrequency("ANNUAL")

    leg = qlFixedRateLeg(schedule, day_counter, [100.0], [0.05])
    curve_handle = _curve(start, 0.05)

    npv = qlCashFlowsNpv(leg, curve_handle, False)
    assert npv > 0.0

    bps = qlCashFlowsBps(leg, curve_handle, False)
    assert bps > 0.0

    ytm = qlCashFlowsYieldRate(leg, npv, day_counter, compounding, frequency, False)
    ir = ql.InterestRate(ytm, day_counter, compounding, frequency)

    bps_ir = qlCashFlowsBpsFromInterestRate(leg, ir, False)
    bps_rate = qlCashFlowsBpsFromRate(leg, ytm, day_counter, compounding, frequency, False)
    assert abs(bps_ir - bps_rate) < 1.0e-10

    npvbps = qlCashFlowsNpvBps(leg, curve_handle, False)
    assert len(npvbps) == 2
    assert abs(npvbps[0] - npv) < 1.0e-10
    assert abs(npvbps[1] - bps) < 1.0e-10

    atm_rate = qlCashFlowsAtmRate(leg, curve_handle, False)
    assert atm_rate > 0.0

    convexity_ir = qlCashFlowsConvexityFromInterestRate(leg, ir, False)
    bpv_ir = qlCashFlowsBasisPointValueFromInterestRate(leg, ir, False)
    assert convexity_ir > 0.0
    assert abs(bpv_ir) > 0.0


def test_ibor_leg_pricer_assignment_smoke():
    start = qlDate(2024, 1, 2)
    end = qlDate(2026, 1, 2)
    schedule = _schedule(start, end)
    curve = _curve(start, 0.03)

    index = qlEuribor(ql.Period("6M"), curve)
    leg = qlIborLeg([100.0], schedule, index)
    pricer = qlBlackIborCouponPricer()

    assert len(leg) > 0
    assert qlSetCouponPricer(leg, pricer) is True


def test_overnight_cappedfloored_coupon_and_casts():
    start = qlDate(2024, 1, 2)
    end = qlDate(2024, 7, 2)
    payment_date = end
    curve = _curve(start, 0.03)
    overnight_index = qlSofr(curve)

    underlying = qlOvernightIndexedCoupon(
        payment_date,
        100.0,
        start,
        end,
        overnight_index,
    )
    capped_floored = qlCappedFlooredOvernightIndexedCoupon(underlying, 0.07, 0.01)

    assert qlAsOvernightIndexedCoupon(underlying) is not None
    assert qlAsCappedFlooredOvernightIndexedCoupon(capped_floored) is not None


def test_additional_pricer_constructors():
    assert isinstance(qlBlackCompoundingOvernightIndexedCouponPricer(), ql.BlackCompoundingOvernightIndexedCouponPricer)
    assert isinstance(qlBlackAveragingOvernightIndexedCouponPricer(), ql.BlackAveragingOvernightIndexedCouponPricer)
    assert isinstance(qlCompoundingMultipleResetsPricer(), ql.CompoundingMultipleResetsPricer)
    assert isinstance(qlAveragingMultipleResetsPricer(), ql.AveragingMultipleResetsPricer)
