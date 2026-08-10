import QuantLib as ql
import pytest

from quantlib_xloil.calendars import qlCalendar
from quantlib_xloil.date import qlDate
from quantlib_xloil.fxforward import (
    qlDiscountingFxForwardEngine,
    qlFxForward,
    qlFxForward2,
    qlFxForwardFairForwardRate,
    qlFxForwardForwardRate,
    qlFxForwardMaturityDate,
    qlFxForwardNpvSourceCurrency,
    qlFxForwardNpvTargetCurrency,
    qlFxForwardPaySourceCurrency,
    qlFxForwardSettlementCalendar,
    qlFxForwardSettlementDate,
    qlFxForwardSettlementDays,
    qlFxForwardSourceCurrency,
    qlFxForwardSourceNominal,
    qlFxForwardTargetCurrency,
    qlFxForwardTargetNominal,
)


def _setup_simple_yield_curve(rate: float = 0.05) -> ql.YieldTermStructureHandle:
    """Create a simple flat yield curve for testing."""
    today = ql.Date(15, 6, 2024)
    ql.Settings.instance().evaluationDate = today
    return ql.YieldTermStructureHandle(ql.FlatForward(today, rate, ql.Actual365Fixed()))


def test_qlFxForward_constructor_with_nominals():
    """Test FxForward constructor with source and target nominals."""
    maturity_date = qlDate(2025, 6, 15)
    source_currency = ql.USDCurrency()
    target_currency = ql.EURCurrency()

    fx_forward = qlFxForward(
        source_nominal=1000000.0,
        source_currency=source_currency,
        target_nominal=850000.0,
        target_currency=target_currency,
        maturity_date=maturity_date,
        pay_source_currency=True,
    )

    assert isinstance(fx_forward, ql.FxForward)
    assert qlFxForwardSourceNominal(fx_forward) == pytest.approx(1000000.0)
    assert qlFxForwardTargetNominal(fx_forward) == pytest.approx(850000.0)
    assert qlFxForwardSourceCurrency(fx_forward).code() == "USD"
    assert qlFxForwardTargetCurrency(fx_forward).code() == "EUR"
    assert qlFxForwardMaturityDate(fx_forward) == maturity_date
    assert qlFxForwardPaySourceCurrency(fx_forward) is True
    assert isinstance(qlFxForwardSettlementCalendar(fx_forward), ql.Calendar)


def test_qlFxForward2_constructor_with_forward_rate():
    """Test FxForward constructor with forward rate."""
    maturity_date = qlDate(2025, 6, 15)
    source_currency = ql.USDCurrency()
    target_currency = ql.EURCurrency()

    fx_forward = qlFxForward2(
        source_nominal=1000000.0,
        source_currency=source_currency,
        target_currency=target_currency,
        forward_rate=1.1765,
        maturity_date=maturity_date,
        pay_source_currency=False,
    )

    assert isinstance(fx_forward, ql.FxForward)
    assert qlFxForwardSourceNominal(fx_forward) == pytest.approx(1000000.0)
    assert qlFxForwardForwardRate(fx_forward) == pytest.approx(1.1765)
    assert qlFxForwardSourceCurrency(fx_forward).code() == "USD"
    assert qlFxForwardTargetCurrency(fx_forward).code() == "EUR"
    assert qlFxForwardMaturityDate(fx_forward) == maturity_date
    assert qlFxForwardPaySourceCurrency(fx_forward) is False


def test_qlFxForward_settlement_properties():
    """Test FxForward settlement-related properties."""
    maturity_date = qlDate(2025, 6, 15)
    calendar = qlCalendar("TARGET")

    fx_forward = qlFxForward(
        source_nominal=1000000.0,
        source_currency=ql.USDCurrency(),
        target_nominal=850000.0,
        target_currency=ql.EURCurrency(),
        maturity_date=maturity_date,
        pay_source_currency=True,
        settlement_days=2,
        payment_calendar=calendar,
    )

    assert qlFxForwardSettlementDays(fx_forward) == 2
    assert qlFxForwardSettlementCalendar(fx_forward) == calendar


def test_qlFxForward_fair_forward_rate():
    """Test FxForward fair forward rate calculation with pricing engine."""
    today = ql.Date(15, 6, 2024)
    ql.Settings.instance().evaluationDate = today
    maturity_date = today + ql.Period("1Y")

    source_curve = _setup_simple_yield_curve(0.05)
    target_curve = _setup_simple_yield_curve(0.03)
    spot_fx = 1.10

    engine = qlDiscountingFxForwardEngine(
        source_currency_discount_curve=source_curve,
        target_currency_discount_curve=target_curve,
        spot_fx=spot_fx,
    )

    fx_forward = qlFxForward2(
        source_nominal=1000000.0,
        source_currency=ql.USDCurrency(),
        target_currency=ql.EURCurrency(),
        forward_rate=1.15,
        maturity_date=maturity_date,
        pay_source_currency=True,
    )

    fx_forward.setPricingEngine(engine)

    fair_rate = qlFxForwardFairForwardRate(fx_forward)
    assert isinstance(fair_rate, float)


def test_qlFxForward_npv_without_engine():
    """Test FxForward NPV methods without pricing engine raise error."""
    maturity_date = qlDate(2025, 6, 15)

    fx_forward = qlFxForward(
        source_nominal=1000000.0,
        source_currency=ql.USDCurrency(),
        target_nominal=850000.0,
        target_currency=ql.EURCurrency(),
        maturity_date=maturity_date,
        pay_source_currency=True,
    )

    with pytest.raises(RuntimeError, match="null pricing engine"):
        qlFxForwardNpvSourceCurrency(fx_forward)

    with pytest.raises(RuntimeError, match="null pricing engine"):
        qlFxForwardNpvTargetCurrency(fx_forward)


def test_qlDiscountingFxForwardEngine_constructor():
    """Test DiscountingFxForwardEngine constructor."""
    source_curve = _setup_simple_yield_curve(0.05)
    target_curve = _setup_simple_yield_curve(0.03)
    spot_fx = 1.10

    engine = qlDiscountingFxForwardEngine(
        source_currency_discount_curve=source_curve,
        target_currency_discount_curve=target_curve,
        spot_fx=spot_fx,
    )

    assert isinstance(engine, ql.DiscountingFxForwardEngine)


def test_qlFxForward_npv_with_engine():
    """Test FxForward NPV calculation with DiscountingFxForwardEngine."""
    today = ql.Date(15, 6, 2024)
    ql.Settings.instance().evaluationDate = today
    maturity_date = today + ql.Period("1Y")

    source_curve = _setup_simple_yield_curve(0.05)
    target_curve = _setup_simple_yield_curve(0.03)
    spot_fx = 1.10

    engine = qlDiscountingFxForwardEngine(
        source_currency_discount_curve=source_curve,
        target_currency_discount_curve=target_curve,
        spot_fx=spot_fx,
    )

    fx_forward = qlFxForward2(
        source_nominal=1000000.0,
        source_currency=ql.USDCurrency(),
        target_currency=ql.EURCurrency(),
        forward_rate=1.15,
        maturity_date=maturity_date,
        pay_source_currency=True,
    )

    fx_forward.setPricingEngine(engine)

    npv_source = qlFxForwardNpvSourceCurrency(fx_forward)
    npv_target = qlFxForwardNpvTargetCurrency(fx_forward)

    assert isinstance(npv_source, float)
    assert isinstance(npv_target, float)


def test_qlFxForward_settlement_date():
    """Test FxForward settlement date calculation."""
    today = ql.Date(15, 6, 2024)
    ql.Settings.instance().evaluationDate = today
    maturity_date = today + ql.Period("1Y")

    fx_forward = qlFxForward(
        source_nominal=1000000.0,
        source_currency=ql.USDCurrency(),
        target_nominal=850000.0,
        target_currency=ql.EURCurrency(),
        maturity_date=maturity_date,
        pay_source_currency=True,
        settlement_days=2,
    )

    settlement_date = qlFxForwardSettlementDate(fx_forward)
    assert isinstance(settlement_date, ql.Date)
    assert settlement_date > today
