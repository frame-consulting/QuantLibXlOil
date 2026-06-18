import QuantLib as ql
import pytest

from quantlib_xloil.bonds import (
    qlAmortizingFixedRateBond,
    qlAmortizingFloatingRateBond,
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
    qlBondSetDiscountingEngine,
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
    qlZeroCouponBond,
)
from quantlib_xloil.calendars import qlCalendar
from quantlib_xloil.date import qFrequency, qlDate
from quantlib_xloil.daycounters import qlDayCounter
from quantlib_xloil.ratehelpers import qQuoteHandle
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


def test_bond_price_and_callability_wrappers_roundtrip():
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


def test_zero_coupon_bond_accessors():
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
    original_eval = ql.Settings.instance().evaluationDate
    try:
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
        engine = qlBondSetDiscountingEngine(bond, discount_curve)

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
    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_amortizing_and_floating_bond_constructor_wrappers():
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


def test_callable_bond_analytics_wrappers_match_methods():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        eval_date = qlDate(2025, 1, 2)
        ql.Settings.instance().evaluationDate = eval_date

        start = qlDate(2025, 1, 2)
        end = qlDate(2032, 1, 2)
        schedule = _fixed_schedule(start, end)
        day_counter = qlDayCounter("ACTUAL365FIXED")

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

        # Wrapper currently forwards setPricingEngine return value (None).
        assert (
            qlBlackCallableFixedRateBondEngine(callable_bond, vol, curve_handle) is None
        )

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
    finally:
        ql.Settings.instance().evaluationDate = original_eval
