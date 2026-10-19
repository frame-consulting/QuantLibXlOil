import QuantLib as ql
import pytest

from quantlib_xloil.bonds import (
    qlAmortizingCmsRateBond,
    qlAmortizingFixedRateBond,
    qlAmortizingFloatingRateBond,
    qlBondCleanPriceFromZSpread,
    qlBlackCallableFixedRateBondEngine,
    qBondPriceType,
    qCallabilityType,
    qlCallableBondCallability,
    qlCallableBondCleanPriceOAS,
    qlCallableBondEffectiveConvexity,
    qlCallableBondEffectiveDuration,
    qlCallableBondImpliedVolatility,
    qlCallableBondOAS,
    qlCallableFixedRateBond,
    qlBondAccruedAmount,
    qlBondCalendar,
    qlBondCashFlows,
    qlBondCleanPrice,
    qlBondCleanPrice2,
    qlBondDirtyPrice,
    qlBondDirtyPrice2,
    qlBondIssueDate,
    qlBondMaturityDate,
    qlBondNotional,
    qlBondNotionals,
    qlBondPrice,
    qlBondPriceAmount,
    qlBondPriceIsValid,
    qlBondPriceType,
    qlBondSettlementDate,
    qlBondSettlementDays,
    qlBondSinkingSchedule,
    qlBondSinkingNotionals,
    qlCmsRateBond,
    qlCPIBond,
    qlDiscountingBondEngine,
    qlBondSettlementValue,
    qlBondSettlementValue2,
    qlBondYield,
    qlBondYield2,
    qlCallability,
    qlCallabilityDate,
    qlCallabilityPrice,
    qlCallabilityType,
    qlFixedRateBond,
    qlFloatingRateBond,
    qlSoftCallability,
    qlTreeCallableFixedRateBondEngine,
    qlTreeCallableFixedRateBondEngine2,
    qlZeroCouponBond,
)
from quantlib_xloil.calendars import qlCalendar
from quantlib_xloil.currencies import qCurrency
from quantlib_xloil.date import qFrequency, qPeriod, qlDate
from quantlib_xloil.daycounters import qlDayCounter
from quantlib_xloil.indexes import qlSwapIndex, qlUSDLibor
from quantlib_xloil.inflation import (
    qCPIInterpolationType,
    qlZeroInflationCurve,
    qlZeroInflationIndex,
    qlCustomRegion,
)
from quantlib_xloil.ratehelpers import qQuoteHandle
from quantlib_xloil.scheduler import qDateGenerationRule
from quantlib_xloil.termstructures import qCompounding


def _fixed_schedule(start: ql.Date, end: ql.Date) -> ql.Schedule:
    return ql.Schedule(
        start,
        end,
        ql.Period(ql.Semiannual),
        qlCalendar("TARGET"),
        ql.Unadjusted,
        ql.Unadjusted,
        ql.DateGeneration.Backward,
        False,
    )


def test_bond_price_and_callability_wrappers():
    clean_type = qBondPriceType.__wrapped__("CLEAN")
    price = qlBondPrice(101.25, clean_type)

    assert isinstance(price, ql.BondPrice)
    assert qlBondPriceAmount(price) == pytest.approx(101.25)
    assert qlBondPriceIsValid(price) is True
    assert qlBondPriceType(price) == "CLEAN"

    callability = qlCallability(
        price,
        qCallabilityType.__wrapped__("CALL"),
        qlDate(2030, 1, 2),
    )
    assert isinstance(callability, ql.Callability)
    assert qlCallabilityType(callability) == "CALL"
    assert qlCallabilityDate(callability) == qlDate(2030, 1, 2)
    assert qlCallabilityPrice(callability).amount() == pytest.approx(101.25)


def test_zero_coupon_bond():
    issue_date = qlDate(2025, 1, 2)
    maturity_date = qlDate(2030, 1, 2)
    bond = qlZeroCouponBond(
        2,
        qlCalendar("TARGET"),
        100.0,
        maturity_date,
        ql.Following,
        100.0,
        issue_date,
    )

    assert isinstance(bond, ql.ZeroCouponBond)
    assert qlBondSettlementDays(bond) == 2
    assert qlBondMaturityDate(bond) == maturity_date
    assert qlBondIssueDate(bond) == issue_date
    assert qlBondCalendar(bond).name() == qlCalendar("TARGET").name()
    assert qlBondSettlementDate(bond, issue_date) >= issue_date
    assert qlBondNotional(bond, issue_date) > 0.0


def test_fixed_rate_bond_pricing_and_yield_wrappers():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date

    start = qlDate(2025, 1, 2)
    end = qlDate(2030, 1, 2)
    schedule = _fixed_schedule(start, end)
    day_counter = qlDayCounter("ACTUAL365FIXED")

    bond = qlFixedRateBond(
        2,
        100.0,
        schedule,
        [0.05],
        day_counter,
    )

    discount_curve = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.03, day_counter)
    )

    engine = qlDiscountingBondEngine(discount_curve)
    bond.setPricingEngine(engine)

    assert isinstance(bond, ql.FixedRateBond)
    assert isinstance(engine, ql.DiscountingBondEngine)
    assert len(qlBondCashFlows(bond)) > 0
    assert len(qlBondNotionals(bond)) > 0

    clean_price = qlBondCleanPrice(bond)
    dirty_price = qlBondDirtyPrice(bond)
    assert clean_price == pytest.approx(bond.cleanPrice())
    assert dirty_price == pytest.approx(bond.dirtyPrice())
    assert dirty_price >= clean_price

    compounding = qCompounding.__wrapped__("COMPOUNDED")
    frequency = qFrequency.__wrapped__("ANNUAL")
    yld = qlBondYield(bond, day_counter, compounding, frequency)

    assert yld == pytest.approx(
        bond.bondYield(day_counter, compounding, frequency, 1.0e-8, 100)
    )
    assert qlBondCleanPrice2(
        bond, yld, day_counter, compounding, frequency
    ) == pytest.approx(bond.cleanPrice(yld, day_counter, compounding, frequency))
    assert qlBondDirtyPrice2(
        bond, yld, day_counter, compounding, frequency, ql.Date()
    ) == pytest.approx(
        bond.dirtyPrice(yld, day_counter, compounding, frequency, ql.Date())
    )

    clean_price_obj = ql.BondPrice(clean_price, ql.BondPrice.Clean)
    yld_from_price = qlBondYield2(
        bond,
        clean_price_obj,
        day_counter,
        compounding,
        frequency,
        ql.Date(),
    )
    assert yld_from_price == pytest.approx(
        bond.bondYield(
            clean_price_obj,
            day_counter,
            compounding,
            frequency,
            ql.Date(),
            1.0e-8,
            100,
            0.05,
        )
    )

    assert qlBondAccruedAmount(bond, ql.Date()) == pytest.approx(
        bond.accruedAmount(ql.Date())
    )
    assert qlBondSettlementValue(bond) == pytest.approx(bond.settlementValue())
    assert qlBondSettlementValue2(bond, clean_price) == pytest.approx(
        bond.settlementValue(clean_price)
    )


def test_amortizing_and_floating_bond():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date
    start = qlDate(2025, 1, 2)
    end = qlDate(2029, 1, 2)
    schedule = _fixed_schedule(start, end)
    day_counter = qlDayCounter("ACTUAL365FIXED")

    curve_handle = ql.YieldTermStructureHandle(ql.FlatForward(start, 0.03, day_counter))
    index = ql.Euribor(ql.Period("6M"), curve_handle)

    amortizing_fixed = qlAmortizingFixedRateBond(
        2,
        100.0,
        schedule,
        [0.04],
        day_counter,
    )
    amortizing_float = qlAmortizingFloatingRateBond(
        2,
        100.0,
        schedule,
        index,
        day_counter,
        ql.Following,
        2,
        [1.0],
        [0.001],
    )
    floating = qlFloatingRateBond(
        2,
        100.0,
        schedule,
        index,
        day_counter,
        ql.Following,
        2,
        [1.0],
        [0.001],
    )

    assert isinstance(amortizing_fixed, ql.AmortizingFixedRateBond)
    assert isinstance(amortizing_float, ql.AmortizingFloatingRateBond)
    assert isinstance(floating, ql.FloatingRateBond)
    assert len(amortizing_fixed.cashflows()) > 0
    assert len(amortizing_float.cashflows()) > 0
    assert len(floating.cashflows()) > 0


def test_callable_bond():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date

    start = qlDate(2025, 1, 2)
    end = qlDate(2032, 1, 2)
    schedule = _fixed_schedule(start, end)
    day_counter = qlDayCounter("30/360")

    callability = qlCallability(
        ql.BondPrice(101.0, ql.BondPrice.Clean),
        qCallabilityType.__wrapped__("CALL"),
        qlDate(2028, 1, 2),
    )
    callable_bond = qlCallableFixedRateBond(
        2,
        100.0,
        schedule,
        [0.05],
        day_counter,
        ql.Following,
        100.0,
        start,
        callability,
    )

    assert isinstance(callable_bond, ql.CallableFixedRateBond)
    assert len(qlCallableBondCallability(callable_bond)) == 1

    curve_handle = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.03, day_counter)
    )
    vol = qQuoteHandle.__wrapped__(0.20)

    engine = qlBlackCallableFixedRateBondEngine(vol, curve_handle)
    callable_bond.setPricingEngine(engine)

    compounding = qCompounding.__wrapped__("COMPOUNDED")
    frequency = qFrequency.__wrapped__("ANNUAL")
    settlement = callable_bond.settlementDate()

    clean_price = qlCallableBondCleanPriceOAS(
        callable_bond,
        0.0,
        curve_handle,
        day_counter,
        compounding,
        frequency,
        settlement,
    )

    oas = qlCallableBondOAS(
        callable_bond,
        clean_price,
        curve_handle,
        day_counter,
        compounding,
        frequency,
        settlement,
        1e-10,
        100,
        0.0,
    )
    print(oas)
    assert oas == pytest.approx(
        callable_bond.OAS(
            clean_price,
            curve_handle,
            day_counter,
            compounding,
            frequency,
            settlement,
            1e-10,
            100,
            0.0,
        )
    )
    assert oas == pytest.approx(0.0, abs=1e-8)

    assert qlCallableBondCleanPriceOAS(
        callable_bond,
        oas,
        curve_handle,
        day_counter,
        compounding,
        frequency,
        settlement,
    ) == pytest.approx(
        callable_bond.cleanPriceOAS(
            oas,
            curve_handle,
            day_counter,
            compounding,
            frequency,
            settlement,
        )
    )
    assert qlCallableBondEffectiveDuration(
        callable_bond,
        oas,
        curve_handle,
        day_counter,
        compounding,
        frequency,
    ) == pytest.approx(
        callable_bond.effectiveDuration(
            oas,
            curve_handle,
            day_counter,
            compounding,
            frequency,
            2e-4,
        )
    )
    assert qlCallableBondEffectiveConvexity(
        callable_bond,
        oas,
        curve_handle,
        day_counter,
        compounding,
        frequency,
    ) == pytest.approx(
        callable_bond.effectiveConvexity(
            oas,
            curve_handle,
            day_counter,
            compounding,
            frequency,
            2e-4,
        )
    )

    target_price = ql.BondPrice(clean_price, ql.BondPrice.Clean)
    assert qlCallableBondImpliedVolatility(
        callable_bond,
        target_price,
        curve_handle,
        1e-8,
        100,
        1e-4,
        2.0,
    ) == pytest.approx(
        callable_bond.impliedVolatility(
            target_price,
            curve_handle,
            1e-8,
            100,
            1e-4,
            2.0,
        )
    )


def test_bond_clean_price_from_z_spread():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date

    day_counter = qlDayCounter("ACTUAL365FIXED")
    calendar = qlCalendar("TARGET")

    start = qlDate(2025, 1, 2)
    end = qlDate(2030, 1, 2)
    schedule = _fixed_schedule(start, end)

    bond = qlFixedRateBond(
        2,
        100.0,
        schedule,
        [0.05],
        day_counter,
        ql.Following,
        100.0,
        start,
    )
    discount_curve = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.04, day_counter)
    )

    clean_price_default = qlBondCleanPriceFromZSpread(
        bond,
        discount_curve,
        z_spread=0.005,
        dc=day_counter,
        compounding=ql.Compounded,
        freq=ql.Annual,
        settlement_date=eval_date,
    )
    assert isinstance(clean_price_default, float)
    assert clean_price_default > 0.0
    assert clean_price_default < 200.0

    clean_price_explicit = qlBondCleanPriceFromZSpread(
        bond,
        discount_curve,
        z_spread=0.005,
        dc=day_counter,
        compounding=ql.Compounded,
        freq=ql.Annual,
        settlement_date=eval_date,
    )
    assert isinstance(clean_price_explicit, float)
    assert clean_price_explicit > 0.0
    assert clean_price_explicit < 200.0
    clean_price_zero_spread = qlBondCleanPriceFromZSpread(
        bond,
        discount_curve,
        z_spread=0.0,
        dc=day_counter,
        compounding=ql.Compounded,
        freq=ql.Annual,
        settlement_date=eval_date,
    )
    assert isinstance(clean_price_zero_spread, float)
    assert clean_price_zero_spread > 0.0


def test_callable_bond_implied_volatility_wrapper():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date

    start = qlDate(2025, 1, 2)
    end = qlDate(2032, 1, 2)
    schedule = _fixed_schedule(start, end)
    day_counter = qlDayCounter("ACTUAL365FIXED")
    callability = qlCallability(
        ql.BondPrice(105.0, ql.BondPrice.Clean),
        qCallabilityType.__wrapped__("CALL"),
        qlDate(2028, 1, 2),
    )
    callable_bond = qlCallableFixedRateBond(
        2,
        100.0,
        schedule,
        [0.06],
        day_counter,
        ql.Following,
        100.0,
        start,
        [callability],
    )

    assert isinstance(callable_bond, ql.CallableFixedRateBond)

    curve_handle = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.03, day_counter)
    )
    test_vol = 0.20
    vol = qQuoteHandle.__wrapped__(test_vol)
    engine = qlBlackCallableFixedRateBondEngine(vol, curve_handle)
    callable_bond.setPricingEngine(engine)
    actual_price = callable_bond.cleanPrice()

    assert actual_price > 80.0, f"Bond price {actual_price} is too low"
    assert actual_price < 120.0, f"Bond price {actual_price} is too high"

    target_price = ql.BondPrice(actual_price, ql.BondPrice.Clean)
    implied_vol = qlCallableBondImpliedVolatility(
        callable_bond,
        target_price,
        curve_handle,
        accuracy=1e-6,
        max_evaluations=100,
        min_vol=0.01,
        max_vol=0.5,
    )
    assert isinstance(implied_vol, float)
    assert implied_vol >= 0.0
    assert implied_vol == pytest.approx(test_vol, rel=0.1)

    higher_vol = 0.25
    vol_higher = qQuoteHandle.__wrapped__(higher_vol)
    engine_higher = ql.BlackCallableFixedRateBondEngine(vol_higher, curve_handle)
    callable_bond.setPricingEngine(engine_higher)
    higher_price_value = callable_bond.cleanPrice()
    higher_price = ql.BondPrice(higher_price_value, ql.BondPrice.Clean)

    callable_bond.setPricingEngine(engine)

    implied_vol_higher = qlCallableBondImpliedVolatility(
        callable_bond,
        higher_price,
        curve_handle,
        accuracy=1e-6,
        max_evaluations=100,
        min_vol=0.01,
        max_vol=0.5,
    )
    assert isinstance(implied_vol_higher, float)
    assert implied_vol_higher >= 0.0
    assert implied_vol_higher == pytest.approx(higher_vol, rel=0.1)


def test_tree_callable_fixed_rate_bond_engine():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date

    day_counter = qlDayCounter("ACTUAL365FIXED")
    curve_handle = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.05, day_counter)
    )
    mean_reversion = 0.03
    volatility = 0.01
    hw_model = ql.HullWhite(
        curve_handle,
        mean_reversion,
        volatility,
    )

    engine_with_steps = qlTreeCallableFixedRateBondEngine(
        hw_model,
        time_steps=100,
    )
    assert isinstance(engine_with_steps, ql.TreeCallableFixedRateBondEngine)

    engine_with_steps_and_ts = qlTreeCallableFixedRateBondEngine(
        hw_model,
        time_steps=50,
        term_structure=curve_handle,
    )
    assert isinstance(engine_with_steps_and_ts, ql.TreeCallableFixedRateBondEngine)

    end_time = 10.0
    time_grid = ql.TimeGrid(end_time, 100)

    engine_with_grid = qlTreeCallableFixedRateBondEngine2(
        hw_model,
        time_grid=time_grid,
    )
    assert isinstance(engine_with_grid, ql.TreeCallableFixedRateBondEngine)

    engine_with_grid_and_ts = qlTreeCallableFixedRateBondEngine2(
        hw_model,
        time_grid=time_grid,
        term_structure=curve_handle,
    )
    assert isinstance(engine_with_grid_and_ts, ql.TreeCallableFixedRateBondEngine)


def test_callable_bond_with_tree_engine_clean_price():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date

    start = qlDate(2025, 1, 2)
    end = qlDate(2030, 1, 2)
    schedule = _fixed_schedule(start, end)
    day_counter = qlDayCounter("ACTUAL365FIXED")

    call_dates = [
        qlDate(2026, 1, 2),
        qlDate(2027, 1, 2),
        qlDate(2028, 1, 2),
        qlDate(2029, 1, 2),
    ]
    call_prices = [102.0, 101.5, 101.0, 100.5]
    callabilities = []
    for date, price in zip(call_dates, call_prices):
        callability = qlCallability(
            ql.BondPrice(price, ql.BondPrice.Clean),
            qCallabilityType.__wrapped__("CALL"),
            date,
        )
        callabilities.append(callability)

    curve_handle = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.04, day_counter)
    )

    callable_bond = qlCallableFixedRateBond(
        2,
        100.0,
        schedule,
        [0.05],
        day_counter,
        ql.Following,
        100.0,
        start,
        callabilities,
    )

    cash_flow_dates = [cf.date() for cf in callable_bond.cashflows()]

    mean_reversion = 0.05
    volatility = 0.01
    hw_model = ql.HullWhite(
        curve_handle,
        mean_reversion,
        volatility,
    )

    all_times = [0.0]
    call_dates_times = [day_counter.yearFraction(eval_date, cd) for cd in call_dates]
    cf_times = [day_counter.yearFraction(eval_date, d) for d in cash_flow_dates]
    all_times = sorted(set(all_times + cf_times + call_dates_times))
    if all_times:
        max_time = all_times[-1]
        n_additional = 100
        additional_times = [
            max_time + i * (0.5 / n_additional) for i in range(1, n_additional + 1)
        ]
        all_times = sorted(set(all_times + additional_times))
    time_grid = ql.TimeGrid(all_times)

    engine = qlTreeCallableFixedRateBondEngine2(
        hw_model,
        time_grid=time_grid,
        term_structure=curve_handle,
    )
    callable_bond.setPricingEngine(engine)

    clean_price = qlBondCleanPrice(callable_bond)

    assert isinstance(callable_bond, ql.CallableFixedRateBond)
    assert len(callabilities) == 4
    assert isinstance(engine, ql.TreeCallableFixedRateBondEngine)
    assert isinstance(clean_price, float)
    assert clean_price > 0.0
    assert clean_price < 120.0
    assert clean_price == pytest.approx(callable_bond.cleanPrice())


def test_cpi_bond():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date

    reference_date = ql.Date(2, 1, 2025)
    inflation_dates = [
        ql.Date(2, 1, 2024),
        ql.Date(2, 1, 2030),
    ]
    inflation_rates = [0.02, 0.02]

    inflation_curve = qlZeroInflationCurve(
        reference_date,
        inflation_dates,
        inflation_rates,
        qFrequency.__wrapped__("ANNUAL"),
        qlDayCounter("ACTUAL365FIXED"),
    )

    region = qlCustomRegion("TestRegion", "TR")
    currency = qCurrency.__wrapped__("USD")
    cpi_index = qlZeroInflationIndex(
        "TEST-CPI",
        region,
        False,
        qFrequency.__wrapped__("ANNUAL"),
        qPeriod.__wrapped__("3M"),
        currency,
        inflation_curve,
    )

    cpi_index.addFixing(ql.Date(2, 1, 2024), 100, forceOverwrite=True)
    start = qlDate(2025, 1, 2)
    end = qlDate(2030, 1, 2)
    schedule = ql.Schedule(
        start,
        end,
        ql.Period(ql.Semiannual),
        qlCalendar("TARGET"),
        ql.Unadjusted,
        ql.Unadjusted,
        qDateGenerationRule.__wrapped__("BACKWARD"),
        False,
    )

    settlement_days = 2
    cpi_bond = qlCPIBond(
        settlement_days,
        face_amount=100.0,
        growth_only=False,
        base_cpi=100.0,
        observation_lag=qPeriod.__wrapped__("3M"),
        cpi_index=cpi_index,
        observation_interpolation=qCPIInterpolationType.__wrapped__("LINEAR"),
        schedule=schedule,
        coupons=[0.03],
        accrual_day_counter=qlDayCounter("ACTUAL365FIXED"),
        payment_convention=ql.ModifiedFollowing,
        issue_date=start,
    )

    day_counter = qlDayCounter("ACTUAL365FIXED")
    discount_curve = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.03, day_counter)
    )

    engine = qlDiscountingBondEngine(discount_curve)
    cpi_bond.setPricingEngine(engine)
    clean_price = qlBondCleanPrice(cpi_bond)

    assert isinstance(cpi_bond, ql.CPIBond)
    assert isinstance(engine, ql.DiscountingBondEngine)
    assert isinstance(clean_price, float)
    assert cpi_bond.settlementDays() == settlement_days
    assert len(cpi_bond.cashflows()) > 0
    assert qlBondSettlementDays(cpi_bond) == settlement_days
    assert qlBondMaturityDate(cpi_bond) == end
    assert qlBondIssueDate(cpi_bond) == start
    assert clean_price > 0.0
    assert clean_price < 200.0
    assert clean_price == pytest.approx(cpi_bond.cleanPrice())


def test_bond_sinking_schedule():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date

    sinking_start_date = qlDate(2025, 1, 2)
    bond_length = qPeriod.__wrapped__("5Y")
    frequency = qFrequency.__wrapped__("ANNUAL")
    payment_calendar = qlCalendar("TARGET")

    sinking_schedule = qlBondSinkingSchedule(
        start_date=sinking_start_date,
        bond_length=bond_length,
        frequency=frequency,
        payment_calendar=payment_calendar,
    )

    assert isinstance(sinking_schedule, ql.Schedule)
    assert len(sinking_schedule) > 0

    assert sinking_schedule.startDate() == sinking_start_date


def test_bond_sinking_notionals():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date

    bond_length = qPeriod.__wrapped__("5Y")
    frequency = qFrequency.__wrapped__("ANNUAL")
    coupon_rate = 0.05
    initial_notional = 1000000.0

    sinking_notionals = qlBondSinkingNotionals(
        bond_length=bond_length,
        frequency=frequency,
        coupon_rate=coupon_rate,
        initial_notional=initial_notional,
    )

    assert isinstance(sinking_notionals, tuple)
    assert all(isinstance(notional, float) for notional in sinking_notionals)
    assert len(sinking_notionals) > 0
    for notional in sinking_notionals:
        assert notional >= 0

    total_notionals = sum(sinking_notionals)
    assert total_notionals > 0


def test_cms_rate_bond():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date

    start = qlDate(2025, 1, 2)
    end = qlDate(2030, 1, 2)
    schedule = _fixed_schedule(start, end)
    day_counter = qlDayCounter("ACTUAL365FIXED")

    calendar = qlCalendar("TARGET")
    currency = qCurrency.__wrapped__("EUR")

    forward_curve = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.03, day_counter, ql.Quarterly)
    )

    ibor_index = ql.Euribor(ql.Period("3M"))

    swap_index = qlSwapIndex(
        family_name="TestSwapIndex",
        tenor=ql.Period("3M"),
        settlement_days=2,
        currency=currency,
        calendar=calendar,
        fixed_leg_tenor=ql.Period("12M"),
        fixed_leg_convention=ql.Following,
        fixed_leg_day_counter=day_counter,
        ibor_index=ibor_index,
        discount_curve=forward_curve,
    )

    bond = qlCmsRateBond(
        settlement_days=2,
        face_amount=100.0,
        schedule=schedule,
        index=swap_index,
        payment_day_counter=day_counter,
        payment_convention=ql.Following,
        fixing_days=2,
        gearings=[0.0],
        spreads=[0.005],
        caps=[0.05],
        floors=[0.01],
        in_arrears=False,
        redemption=100.0,
        issue_date=start,
    )

    discount_curve = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.03, day_counter)
    )

    engine = qlDiscountingBondEngine(discount_curve)
    bond.setPricingEngine(engine)

    assert isinstance(bond, ql.CmsRateBond)
    assert qlBondSettlementDays(bond) == 2
    assert qlBondMaturityDate(bond) == end
    assert qlBondIssueDate(bond) == start
    assert len(qlBondCashFlows(bond)) > 0

    clean_price = qlBondCleanPrice(bond)
    dirty_price = qlBondDirtyPrice(bond)

    assert isinstance(engine, ql.DiscountingBondEngine)
    assert isinstance(clean_price, float)
    assert isinstance(dirty_price, float)
    assert clean_price > 0.0
    assert clean_price < 200.0
    assert dirty_price >= clean_price - 1.0
    assert clean_price == pytest.approx(bond.cleanPrice())
    assert dirty_price == pytest.approx(bond.dirtyPrice())


def test_amortizing_cms_rate_bond():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date

    start = qlDate(2025, 1, 2)
    end = qlDate(2030, 1, 2)
    schedule = _fixed_schedule(start, end)
    day_counter = qlDayCounter("ACTUAL365FIXED")

    calendar = qlCalendar("TARGET")
    currency = qCurrency.__wrapped__("USD")

    forward_curve = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.03, day_counter)
    )

    ibor_index = qlUSDLibor(ql.Period("6M"), forward_curve)

    swap_index = qlSwapIndex(
        family_name="TestSwapIndex",
        tenor=ql.Period("10Y"),
        settlement_days=2,
        currency=currency,
        calendar=calendar,
        fixed_leg_tenor=ql.Period("6M"),
        fixed_leg_convention=ql.ModifiedFollowing,
        fixed_leg_day_counter=day_counter,
        ibor_index=ibor_index,
        discount_curve=forward_curve,
    )

    notionals = [100.0, 90.0, 80.0, 70.0, 60.0]

    bond = qlAmortizingCmsRateBond(
        settlement_days=2,
        notionals=notionals,
        schedule=schedule,
        index=swap_index,
        payment_day_counter=day_counter,
        payment_convention=ql.Following,
        fixing_days=2,
        gearings=[0.0],
        spreads=[0.0],
        caps=[0.05],
        floors=[0.01],
        in_arrears=False,
        issue_date=start,
    )

    discount_curve = ql.YieldTermStructureHandle(
        ql.FlatForward(eval_date, 0.03, day_counter)
    )

    engine = qlDiscountingBondEngine(discount_curve)
    bond.setPricingEngine(engine)

    assert isinstance(bond, ql.AmortizingCmsRateBond)
    assert qlBondSettlementDays(bond) == 2
    assert qlBondMaturityDate(bond) == end
    assert qlBondIssueDate(bond) == start
    assert len(qlBondCashFlows(bond)) > 0

    clean_price = qlBondCleanPrice(bond)
    dirty_price = qlBondDirtyPrice(bond)

    assert isinstance(engine, ql.DiscountingBondEngine)
    assert isinstance(clean_price, float)
    assert isinstance(dirty_price, float)
    assert clean_price > 0.0
    assert clean_price < 200.0
    assert dirty_price >= clean_price - 1.0
    assert clean_price == pytest.approx(bond.cleanPrice())
    assert dirty_price == pytest.approx(bond.dirtyPrice())


def test_soft_callability():
    eval_date = qlDate(2025, 1, 2)
    ql.Settings.instance().evaluationDate = eval_date

    bond_price = qlBondPrice(102.5, qBondPriceType.__wrapped__("CLEAN"))

    call_date = qlDate(2028, 1, 2)

    trigger_value = 0.045
    soft_call = qlSoftCallability(bond_price, call_date, trigger_value)

    assert isinstance(soft_call, ql.SoftCallability)
    assert isinstance(soft_call, ql.Callability)
