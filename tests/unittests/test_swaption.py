import QuantLib as ql
import pytest

from quantlib_xloil import (
    qlBachelierSwaptionEngine,
    qlBachelierSwaptionEngineFromQuote,
    qlBlackSwaptionEngine,
    qlBlackSwaptionEngineFromQuote,
    qlDate,
    qlEuropeanExercise,
    qlFlatForward,
    qlFloatFloatSwaption,
    qlFloatFloatSwaptionCalibrationBasket,
    qlFloatFloatSwaptionProbabilities,
    qlFloatFloatSwaptionUnderlyingSwap,
    qlFloatFloatSwaptionUnderlyingValue,
    qlInstrumentNPV,
    qlInstrumentSetPricingEngine,
    qlNonstandardSwaption,
    qlNonstandardSwaptionCalibrationBasket,
    qlNonstandardSwaptionProbabilities,
    qlNonstandardSwaptionUnderlyingSwap,
    qlSwaption,
    qlSwaptionAnnuity,
    qlSwaptionDelta,
    qlSwaptionForwardPrice,
    qlSwaptionSettlementMethod,
    qlSwaptionSettlementType,
    qlSwaptionType,
    qlSwaptionUnderlying,
    qlSwaptionVega,
)
from quantlib_xloil.swaption import (
    _qCashAnnuityModel,
    _qSettlementMethod,
    _qSettlementType,
    _qSwaptionPriceType,
)


def _set_eval_date() -> None:
    ql.Settings.instance().evaluationDate = qlDate(2024, 1, 2)


def _setup_curves():
    """Set up interest rate curves for testing."""
    reference_date = qlDate(2024, 1, 2)
    day_counter = ql.Actual365Fixed()

    risk_free = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.03, day_counter)
    )
    forecast = ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, 0.025, day_counter)
    )

    return reference_date, day_counter, risk_free, forecast


def _create_swap(settlement_date, maturity_date, fixed_rate, nominal, index):
    """Create a vanilla fixed-rate swap for testing."""
    fixed_schedule = ql.Schedule(
        settlement_date,
        maturity_date,
        ql.Period(1, ql.Years),
        ql.TARGET(),
        ql.ModifiedFollowing,
        ql.ModifiedFollowing,
        ql.DateGeneration.Forward,
        False,
    )

    floating_schedule = ql.Schedule(
        settlement_date,
        maturity_date,
        ql.Period(3, ql.Months),
        ql.TARGET(),
        ql.ModifiedFollowing,
        ql.ModifiedFollowing,
        ql.DateGeneration.Forward,
        False,
    )

    swap = ql.VanillaSwap(
        ql.VanillaSwap.Payer,
        nominal,
        fixed_schedule,
        fixed_rate,
        ql.Actual360(),
        floating_schedule,
        index,
        0.0,
        ql.Actual360(),
    )

    return swap


def test_swaption_converters():
    """Test converter functions for settlement type, method, price type, and cash annuity model."""
    assert _qSettlementType("PHYSICAL") == ql.Settlement.Physical
    assert _qSettlementType("CASH") == ql.Settlement.Cash

    assert _qSettlementMethod("PHYSICALOTC") == ql.Settlement.PhysicalOTC
    assert _qSettlementMethod("PHYSICALCLEARED") == ql.Settlement.PhysicalCleared
    assert (
        _qSettlementMethod("COLLATERALIZEDCASHPRICE")
        == ql.Settlement.CollateralizedCashPrice
    )
    assert _qSettlementMethod("PARYIELDCURVE") == ql.Settlement.ParYieldCurve
    assert _qSettlementMethod("CASH") == ql.Settlement.Cash

    assert _qSwaptionPriceType("SPOT") == ql.Swaption.Spot
    assert _qSwaptionPriceType("FORWARD") == ql.Swaption.Forward

    assert _qCashAnnuityModel("DISCOUNTCURVE") == ql.BlackSwaptionEngine.DiscountCurve
    assert _qCashAnnuityModel("SWAPRATE") == ql.BlackSwaptionEngine.SwapRate


def test_swaption_constructor_and_accessors():
    """Test Swaption construction and accessor methods."""
    _set_eval_date()
    reference_date, day_counter, risk_free, forecast = _setup_curves()

    settlement_date = reference_date + ql.Period(2, ql.Days)
    exercise_date = settlement_date + ql.Period(6, ql.Months)
    maturity_date = exercise_date + ql.Period(3, ql.Years)

    index = ql.Euribor3M(forecast)
    swap = _create_swap(settlement_date, maturity_date, 0.025, 100000.0, index)

    exercise = qlEuropeanExercise(exercise_date)
    # Use enum values for settlement type and method
    swaption = qlSwaption(
        swap, exercise, ql.Settlement.Physical, ql.Settlement.PhysicalOTC
    )

    assert isinstance(swaption, ql.Swaption)
    assert qlSwaptionSettlementType(swaption) == "PHYSICAL"
    assert qlSwaptionSettlementMethod(swaption) == "PHYSICALOTC"
    assert qlSwaptionType(swaption) == "PAYER"

    underlying = qlSwaptionUnderlying(swaption)
    assert isinstance(underlying, ql.FixedVsFloatingSwap)


def test_swaption_engines_only():
    """Test Swaption engine creation without pricing."""
    _set_eval_date()
    reference_date, day_counter, risk_free, forecast = _setup_curves()

    settlement_date = reference_date + ql.Period(2, ql.Days)
    exercise_date = settlement_date + ql.Period(6, ql.Months)
    maturity_date = exercise_date + ql.Period(3, ql.Years)

    index = ql.Euribor3M(forecast)
    swap = _create_swap(settlement_date, maturity_date, 0.025, 100000.0, index)

    exercise = qlEuropeanExercise(exercise_date)
    swaption = qlSwaption(
        swap, exercise, ql.Settlement.Physical, ql.Settlement.PhysicalOTC
    )

    # Create a Black swaption engine
    swaption_vol = ql.SwaptionVolatilityStructureHandle(
        ql.ConstantSwaptionVolatility(
            reference_date, ql.TARGET(), ql.Following, 0.20, day_counter
        )
    )

    engine = qlBlackSwaptionEngine(
        risk_free, swaption_vol, ql.BlackSwaptionEngine.DiscountCurve
    )
    assert isinstance(engine, ql.PricingEngine)

    # Set the pricing engine
    assert qlInstrumentSetPricingEngine(swaption, engine) is True


def test_black_swaption_engines():
    """Test Black swaption engine constructors and variants."""
    _set_eval_date()
    reference_date, day_counter, risk_free, forecast = _setup_curves()

    # Black engine with volatility structure
    swaption_vol = ql.SwaptionVolatilityStructureHandle(
        ql.ConstantSwaptionVolatility(
            reference_date, ql.TARGET(), ql.Following, 0.20, day_counter
        )
    )

    engine1 = qlBlackSwaptionEngine(
        risk_free, swaption_vol, ql.BlackSwaptionEngine.DiscountCurve
    )
    assert isinstance(engine1, ql.BlackSwaptionEngine)

    # Black engine with constant quote
    vol_quote = ql.QuoteHandle(ql.SimpleQuote(0.20))
    engine2 = qlBlackSwaptionEngineFromQuote(
        risk_free,
        vol_quote,
        ql.Actual365Fixed(),
        0.0,
        ql.BlackSwaptionEngine.DiscountCurve,
    )
    assert isinstance(engine2, ql.BlackSwaptionEngine)


def test_bachelier_swaption_engines():
    """Test Bachelier swaption engine constructors and variants."""
    _set_eval_date()
    reference_date, day_counter, risk_free, forecast = _setup_curves()

    # Bachelier engine with volatility structure (using normal volatility)
    swaption_vol = ql.SwaptionVolatilityStructureHandle(
        ql.ConstantSwaptionVolatility(
            reference_date, ql.TARGET(), ql.Following, 0.0050, day_counter, ql.Normal
        )
    )

    engine1 = qlBachelierSwaptionEngine(
        risk_free, swaption_vol, ql.BachelierSwaptionEngine.DiscountCurve
    )
    assert isinstance(engine1, ql.BachelierSwaptionEngine)

    # Bachelier engine with constant quote
    vol_quote = ql.QuoteHandle(ql.SimpleQuote(0.0050))
    engine2 = qlBachelierSwaptionEngineFromQuote(
        risk_free,
        vol_quote,
        ql.Actual365Fixed(),
        ql.BachelierSwaptionEngine.DiscountCurve,
    )
    assert isinstance(engine2, ql.BachelierSwaptionEngine)


def test_swaption_settlement_types():
    """Test different settlement types and methods."""
    _set_eval_date()
    reference_date, day_counter, risk_free, forecast = _setup_curves()

    settlement_date = reference_date + ql.Period(2, ql.Days)
    exercise_date = settlement_date + ql.Period(6, ql.Months)
    maturity_date = exercise_date + ql.Period(3, ql.Years)

    index = ql.Euribor3M(forecast)
    swap = _create_swap(settlement_date, maturity_date, 0.025, 100000.0, index)
    exercise = qlEuropeanExercise(exercise_date)

    # Test Cash settlement
    swaption_cash = qlSwaption(
        swap, exercise, ql.Settlement.Cash, ql.Settlement.CollateralizedCashPrice
    )
    assert isinstance(swaption_cash, ql.Swaption)
    assert qlSwaptionSettlementType(swaption_cash) == "CASH"
    assert qlSwaptionSettlementMethod(swaption_cash) == "COLLATERALIZEDCASHPRICE"

    # Test Physical settlement with ParYieldCurve method
    swaption_phys = qlSwaption(
        swap, exercise, ql.Settlement.Physical, ql.Settlement.ParYieldCurve
    )
    assert isinstance(swaption_phys, ql.Swaption)
    assert qlSwaptionSettlementType(swaption_phys) == "PHYSICAL"
    assert qlSwaptionSettlementMethod(swaption_phys) == "PARYIELDCURVE"


def test_black_engine_models():
    """Test Black engine with different cash annuity models."""
    _set_eval_date()
    reference_date, day_counter, risk_free, forecast = _setup_curves()

    swaption_vol = ql.SwaptionVolatilityStructureHandle(
        ql.ConstantSwaptionVolatility(
            reference_date, ql.TARGET(), ql.Following, 0.20, day_counter
        )
    )

    # Test DiscountCurve model
    engine_dc = qlBlackSwaptionEngine(
        risk_free, swaption_vol, ql.BlackSwaptionEngine.DiscountCurve
    )
    assert isinstance(engine_dc, ql.BlackSwaptionEngine)

    # Test SwapRate model
    engine_sr = qlBlackSwaptionEngine(
        risk_free, swaption_vol, ql.BlackSwaptionEngine.SwapRate
    )
    assert isinstance(engine_sr, ql.BlackSwaptionEngine)
