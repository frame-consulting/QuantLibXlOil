import QuantLib as ql
import pytest

from quantlib_xloil.calendars import qlCalendar
from quantlib_xloil.creditdefaultswap import (
    _qCreditDefaultSwapPricingModel,
    _qIsdaCdsEngineAccrualBias,
    _qIsdaCdsEngineForwardsInCouponPeriod,
    _qIsdaCdsEngineNumericalFix,
    qlBlackCdsOptionEngine,
    qlClaimAmount,
    qlCdsMaturity,
    qlCdsOption,
    qlCreditDefaultSwap,
    qlCreditDefaultSwapAccrualRebate,
    qlCreditDefaultSwapAccrualRebateNPV,
    qlCreditDefaultSwapCashSettlementDays,
    qlCreditdefaultswapPaysAtDefaultTime,
    qlCreditDefaultSwapCouponLegBPS,
    qlCreditDefaultSwapCouponLegNPV,
    qlCreditDefaultSwapCoupons,
    qlCreditDefaultSwapDefaultLegNPV,
    qlCreditDefaultSwapFairSpread,
    qlCreditDefaultSwapImpliedHazardRate,
    qlCreditDefaultSwapNotional,
    qlCreditDefaultSwapProtectionEndDate,
    qlCreditDefaultSwapProtectionStartDate,
    qlCreditDefaultSwapRebatesAccrual,
    qlCreditDefaultSwapRunningSpread,
    qlCreditdefaultswapSide,
    qlCreditdefaultSwapSettlesAccrual,
    qlCreditDefaultSwapTradeDate,
    qlCreditDefaultSwapUpfront,
    qlCreditDefaultSwapUpfrontBPS,
    qlCreditDefaultswapUpfrontPayment,
    qlCreditDefaultSwapUpfrontNPV,
    qlCreditDefaultSwapWithUpfront,
    qlFaceValueClaim,
    qlIntegralCdsEngine,
    qlIsdaCdsEngine,
    qlMidPointCdsEngine,
)


def _curves(reference_date: ql.Date):
    dc = ql.Actual365Fixed()
    default_curve = ql.DefaultProbabilityTermStructureHandle(
        ql.FlatHazardRate(reference_date, ql.QuoteHandle(ql.SimpleQuote(0.02)), dc)
    )
    discount_curve = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.01, dc)
    )
    return default_curve, discount_curve


def _cds_schedule(start: ql.Date, end: ql.Date) -> ql.Schedule:
    return ql.Schedule(
        start,
        end,
        ql.Period(ql.Quarterly),
        qlCalendar("TARGET"),
        ql.Following,
        ql.Following,
        ql.DateGeneration.CDS,
        False,
    )


def test_creditdefaultswap_converters():
    assert _qCreditDefaultSwapPricingModel("midpoint") == ql.CreditDefaultSwap.Midpoint
    assert _qCreditDefaultSwapPricingModel("ISDA") == ql.CreditDefaultSwap.ISDA
    assert _qIsdaCdsEngineNumericalFix("TAYLOR") == ql.IsdaCdsEngine.Taylor
    assert _qIsdaCdsEngineAccrualBias("NO_BIAS") == ql.IsdaCdsEngine.NoBias
    assert _qIsdaCdsEngineForwardsInCouponPeriod("FLAT") == ql.IsdaCdsEngine.Flat


def test_creditdefaultswap_construction_accessors_and_midpoint_pricing():
    original_eval = ql.Settings.instance().evaluationDate
    try:
        reference_date = ql.Date(2, 1, 2025)
        ql.Settings.instance().evaluationDate = reference_date
        end = ql.Date(2, 1, 2030)

        default_curve, discount_curve = _curves(reference_date)
        schedule = _cds_schedule(reference_date, end)

        cds = qlCreditDefaultSwap(
            ql.Protection.Buyer,
            1_000_000.0,
            0.01,
            schedule,
            ql.Following,
            ql.Actual360(),
            True,
            True,
            reference_date,
            qlFaceValueClaim(),
            None,
            True,
            reference_date,
        )
        engine = qlMidPointCdsEngine(default_curve, 0.40, discount_curve)
        cds.setPricingEngine(engine)

        assert isinstance(cds, ql.CreditDefaultSwap)
        assert qlCreditdefaultswapSide(cds) == "BUY"
        assert qlCreditDefaultSwapNotional(cds) == pytest.approx(1_000_000.0)
        assert qlCreditDefaultSwapRunningSpread(cds) == pytest.approx(0.01)
        assert qlCreditdefaultSwapSettlesAccrual(cds) is True
        assert qlCreditdefaultswapPaysAtDefaultTime(cds) is True
        assert qlCreditDefaultSwapRebatesAccrual(cds) is True
        assert qlCreditDefaultSwapTradeDate(cds) == reference_date
        assert qlCreditDefaultSwapCashSettlementDays(cds) == cds.cashSettlementDays()
        assert len(qlCreditDefaultSwapCoupons(cds)) > 0
        assert qlCreditDefaultSwapProtectionStartDate(cds) == cds.protectionStartDate()
        assert qlCreditDefaultSwapProtectionEndDate(cds) == cds.protectionEndDate()

        assert qlCreditDefaultSwapFairSpread(cds) == pytest.approx(cds.fairSpread())
        assert qlCreditDefaultSwapCouponLegBPS(cds) == pytest.approx(cds.couponLegBPS())
        with pytest.raises(RuntimeError, match="upfront BPS not available"):
            qlCreditDefaultSwapUpfrontBPS(cds)
        with pytest.raises(RuntimeError, match="upfront BPS not available"):
            cds.upfrontBPS()
        assert qlCreditDefaultSwapCouponLegNPV(cds) == pytest.approx(cds.couponLegNPV())
        assert qlCreditDefaultSwapDefaultLegNPV(cds) == pytest.approx(
            cds.defaultLegNPV()
        )
        assert qlCreditDefaultSwapUpfrontNPV(cds) == pytest.approx(cds.upfrontNPV())
        assert qlCreditDefaultSwapAccrualRebateNPV(cds) == pytest.approx(
            cds.accrualRebateNPV()
        )

        implied_h = qlCreditDefaultSwapImpliedHazardRate(
            cds,
            cds.NPV(),
            discount_curve,
            ql.Actual365Fixed(),
            0.40,
            1e-7,
            ql.CreditDefaultSwap.Midpoint,
        )
        assert implied_h > 0.0
    finally:
        ql.Settings.instance().evaluationDate = original_eval


def test_creditdefaultswap_upfront_and_option_engine_wrappers():
    reference_date = ql.Date(2, 1, 2025)
    end = ql.Date(2, 1, 2030)
    default_curve, discount_curve = _curves(reference_date)
    schedule = _cds_schedule(reference_date, end)

    cds = qlCreditDefaultSwapWithUpfront(
        ql.Protection.Seller,
        2_000_000.0,
        0.02,
        0.01,
        schedule,
        ql.Following,
        ql.Actual360(),
        True,
        True,
        reference_date,
        reference_date,
        qlFaceValueClaim(),
        None,
        True,
        reference_date,
        3,
    )

    assert qlCreditdefaultswapSide(cds) == "SELL"
    assert qlCreditDefaultSwapNotional(cds) == pytest.approx(2_000_000.0)
    assert qlCreditDefaultSwapUpfront(cds) == pytest.approx(0.02)

    upfront_payment = qlCreditDefaultswapUpfrontPayment(cds)
    accrual_rebate = qlCreditDefaultSwapAccrualRebate(cds)
    assert upfront_payment is None or isinstance(upfront_payment, ql.CashFlow)
    assert accrual_rebate is None or isinstance(accrual_rebate, ql.CashFlow)

    assert isinstance(
        qlIntegralCdsEngine(ql.Period("1D"), default_curve, 0.40, discount_curve),
        ql.IntegralCdsEngine,
    )
    assert isinstance(
        qlIsdaCdsEngine(default_curve, 0.40, discount_curve),
        ql.IsdaCdsEngine,
    )

    maturity = qlCdsMaturity(reference_date, ql.Period("5Y"), ql.DateGeneration.CDS)
    assert isinstance(maturity, ql.Date)

    running_cds = qlCreditDefaultSwap(
        ql.Protection.Buyer,
        1_000_000.0,
        0.01,
        schedule,
        ql.Following,
        ql.Actual360(),
        True,
        True,
        reference_date,
        qlFaceValueClaim(),
        None,
        True,
        reference_date,
    )
    option = qlCdsOption(
        running_cds, ql.EuropeanExercise(reference_date + ql.Period("1Y"))
    )
    assert isinstance(option, ql.CdsOption)
    assert isinstance(
        qlBlackCdsOptionEngine(
            default_curve,
            0.40,
            discount_curve,
            ql.QuoteHandle(ql.SimpleQuote(0.30)),
        ),
        ql.BlackCdsOptionEngine,
    )


def test_claim_wrapper_parity():
    claim = qlFaceValueClaim()
    default_date = ql.Date(15, 1, 2026)

    with pytest.raises(TypeError, match="takes 4 positional arguments"):
        qlClaimAmount(claim, default_date, 1_000_000.0, 0.40)
    assert claim.amount(default_date, 1_000_000.0, 0.40) > 0.0
