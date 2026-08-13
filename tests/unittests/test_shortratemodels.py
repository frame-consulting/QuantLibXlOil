import QuantLib as ql

from quantlib_xloil.shortratemodels import (
    qlAnalyticBSMHullWhiteEngine,
    qlAnalyticCapFloorEngine,
    qlBlackKarasinski,
    qlBlackKarasinskiTermStructure,
    qlCoxIngersollRoss,
    qlExtendedCoxIngersollRoss,
    qlExtendedCoxIngersollRossTermStructure,
    qlFdG2SwaptionEngine,
    qlFdHullWhiteSwaptionEngine,
    qlG2Model,
    qlG2Discount,
    qlG2DiscountBond,
    qlG2DiscountBondOption,
    qlG2SwaptionEngine,
    qlG2TermStructure,
    qlHullWhite,
    qlHullWhiteConvexityBias,
    qlHullWhiteTermStructure,
    qlJamshidianSwaptionEngine,
    qlOneFactorAffineModelDiscountBond,
    qlOneFactorAffineModelDiscountBond2,
    qlOneFactorAffineModelDiscountBondOption,
    qllOneFactorAffineModelDiscount,
    qlTreeCapFloorEngine2,
    qlTreeCapFloorEngine,
    qlTreeSwaptionEngine2,
    qlTreeSwaptionEngine,
    qlVasicek,
)


def _flat_curve(
    reference_date: ql.Date, rate: float = 0.02
) -> ql.YieldTermStructureHandle:
    return ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, rate, ql.Actual365Fixed())
    )


def test_qlVasicek_default_params():
    model = qlVasicek()
    assert isinstance(model, ql.Vasicek)


def test_qlVasicek_custom_params():
    model = qlVasicek(r0=0.03, a=0.2, b=0.03, sigma=0.02, lambda_=0.5)
    assert isinstance(model, ql.Vasicek)


def test_qlVasicek_discount():
    model = qlVasicek(r0=0.05, a=0.1, b=0.05, sigma=0.01)
    discount = qllOneFactorAffineModelDiscount(model, 1.0)
    assert isinstance(discount, float)
    assert discount > 0.0


def test_qlHullWhite_construction():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlHullWhite(yts)
    assert isinstance(model, ql.HullWhite)


def test_qlHullWhite_with_params():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlHullWhite(yts, a=0.2, sigma=0.02)
    assert isinstance(model, ql.HullWhite)


def test_qlHullWhiteTermStructure():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlHullWhite(yts)
    ts = qlHullWhiteTermStructure(model)
    assert isinstance(ts, ql.YieldTermStructureHandle)


def test_qlHullWhiteConvexityBias():
    bias = qlHullWhiteConvexityBias(future_price=100.0, t=0.5, T=1.0, sigma=0.01, a=0.1)
    assert isinstance(bias, float)


def test_qlBlackKarasinski_construction():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlBlackKarasinski(yts)
    assert isinstance(model, ql.BlackKarasinski)


def test_qlBlackKarasinski_with_params():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlBlackKarasinski(yts, a=0.2, sigma=0.15)
    assert isinstance(model, ql.BlackKarasinski)


def test_qlBlackKarasinskiTermStructure():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlBlackKarasinski(yts)
    ts = qlBlackKarasinskiTermStructure(model)
    assert isinstance(ts, ql.YieldTermStructureHandle)


def test_qlCoxIngersollRoss_default_params():
    model = qlCoxIngersollRoss()
    assert isinstance(model, ql.CoxIngersollRoss)


def test_qlCoxIngersollRoss_custom_params():
    model = qlCoxIngersollRoss(r0=0.02, theta=0.05, k=0.3, sigma=0.15)
    assert isinstance(model, ql.CoxIngersollRoss)


def test_qlExtendedCoxIngersollRoss_construction():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlExtendedCoxIngersollRoss(yts)
    assert isinstance(model, ql.ExtendedCoxIngersollRoss)


def test_qlExtendedCoxIngersollRoss_with_params():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlExtendedCoxIngersollRoss(yts, theta=0.05, k=0.3, sigma=0.15, x0=0.03)
    assert isinstance(model, ql.ExtendedCoxIngersollRoss)


def test_qlExtendedCoxIngersollRossTermStructure():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlExtendedCoxIngersollRoss(yts)
    ts = qlExtendedCoxIngersollRossTermStructure(model)
    assert isinstance(ts, ql.YieldTermStructureHandle)


def test_qlG2Model_construction():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlG2Model(yts)
    assert isinstance(model, ql.G2)


def test_qlG2Model_with_params():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlG2Model(yts, a=0.2, sigma=0.02, b=0.15, eta=0.02, rho=-0.5)
    assert isinstance(model, ql.G2)


def test_qlG2TermStructure():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlG2Model(yts)
    ts = qlG2TermStructure(model)
    assert isinstance(ts, ql.YieldTermStructureHandle)


def test_qlG2Discount():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlG2Model(yts)
    discount = qlG2Discount(model, 1.0)
    assert isinstance(discount, float)


def test_qlG2DiscountBond():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlG2Model(yts)
    price = qlG2DiscountBond(model, 0.0, 1.0, [0.0, 0.0])
    assert isinstance(price, float)


def test_qlG2DiscountBondOption():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlG2Model(yts)
    price = qlG2DiscountBondOption(model, ql.Option.Call, 0.95, 0.5, 1.0)
    assert isinstance(price, float)


def test_qlOneFactorAffineModelDiscountBond2():
    model = qlVasicek(r0=0.05, a=0.1, b=0.05, sigma=0.01)
    price = qlOneFactorAffineModelDiscountBond2(model, 0.0, 1.0, [0.0])
    assert isinstance(price, float)


def test_qlOneFactorAffineModelDiscountBondOption():
    model = qlVasicek(r0=0.05, a=0.1, b=0.05, sigma=0.01)
    price = qlOneFactorAffineModelDiscountBondOption(
        model, ql.Option.Call, 0.95, 0.5, 1.0
    )
    assert isinstance(price, float)


def test_qlOneFactorAffineModelDiscountBond():
    model = qlVasicek(r0=0.05, a=0.1, b=0.05, sigma=0.01)
    price = qlOneFactorAffineModelDiscountBond(model, 0.0, 1.0, [0.0])
    assert isinstance(price, float)


def test_qlJamshidianSwaptionEngine_construction():
    model = qlVasicek(r0=0.05, a=0.1, b=0.05, sigma=0.01)
    engine = qlJamshidianSwaptionEngine(model)
    assert isinstance(engine, ql.JamshidianSwaptionEngine)


def test_qlJamshidianSwaptionEngine_with_term_structure():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlVasicek(r0=0.05, a=0.1, b=0.05, sigma=0.01)
    engine = qlJamshidianSwaptionEngine(model, yts)
    assert isinstance(engine, ql.JamshidianSwaptionEngine)


def test_qlTreeSwaptionEngine_construction():
    model = qlVasicek(r0=0.05, a=0.1, b=0.05, sigma=0.01)
    engine = qlTreeSwaptionEngine(model, 100)
    assert isinstance(engine, ql.TreeSwaptionEngine)


def test_qlTreeSwaptionEngine2_construction():
    model = qlVasicek(r0=0.05, a=0.1, b=0.05, sigma=0.01)
    grid = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
    engine = qlTreeSwaptionEngine2(model, grid)
    assert isinstance(engine, ql.TreeSwaptionEngine)


def test_qlAnalyticCapFloorEngine_construction():
    model = qlVasicek(r0=0.05, a=0.1, b=0.05, sigma=0.01)
    engine = qlAnalyticCapFloorEngine(model)
    assert isinstance(engine, ql.AnalyticCapFloorEngine)


def test_qlTreeCapFloorEngine_construction():
    model = qlVasicek(r0=0.05, a=0.1, b=0.05, sigma=0.01)
    engine = qlTreeCapFloorEngine(model, 100)
    assert isinstance(engine, ql.TreeCapFloorEngine)


def test_qlTreeCapFloorEngine2_construction():
    model = qlVasicek(r0=0.05, a=0.1, b=0.05, sigma=0.01)
    grid = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
    engine = qlTreeCapFloorEngine2(model, grid)
    assert isinstance(engine, ql.TreeCapFloorEngine)


def test_qlG2SwaptionEngine_construction():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlG2Model(yts)
    engine = qlG2SwaptionEngine(model, range_=10.0, intervals=100)
    assert isinstance(engine, ql.G2SwaptionEngine)


def test_qlFdG2SwaptionEngine_default_params():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlG2Model(yts)
    engine = qlFdG2SwaptionEngine(model)
    assert isinstance(engine, ql.FdG2SwaptionEngine)


def test_qlFdG2SwaptionEngine_custom_params():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlG2Model(yts)
    engine = qlFdG2SwaptionEngine(
        model,
        t_grid=50,
        x_grid=25,
        y_grid=25,
        damping_steps=5,
        inv_eps=1e-6,
        scheme_desc=ql.FdmSchemeDesc.Hundsdorfer(),
    )
    assert isinstance(engine, ql.FdG2SwaptionEngine)


def test_qlFdHullWhiteSwaptionEngine_default_params():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlHullWhite(yts)
    engine = qlFdHullWhiteSwaptionEngine(model)
    assert isinstance(engine, ql.FdHullWhiteSwaptionEngine)


def test_qlFdHullWhiteSwaptionEngine_custom_params():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlHullWhite(yts)
    engine = qlFdHullWhiteSwaptionEngine(
        model,
        t_grid=50,
        x_grid=50,
        damping_steps=5,
        inv_eps=1e-6,
        scheme_desc=ql.FdmSchemeDesc.Douglas(),
    )
    assert isinstance(engine, ql.FdHullWhiteSwaptionEngine)


def test_qlAnalyticBSMHullWhiteEngine_construction():
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    model = qlHullWhite(yts)

    # Create a simple Generalized Black-Scholes process
    # Using FlatForward for the yield term structures
    flat_dividend = ql.FlatForward(reference_date, 0.0, ql.Actual365Fixed())
    flat_risk_free = ql.FlatForward(reference_date, 0.02, ql.Actual365Fixed())
    flat_vol = ql.BlackConstantVol(
        reference_date, ql.TARGET(), 0.20, ql.Actual365Fixed()
    )

    dividend_yield = ql.YieldTermStructureHandle(flat_dividend)
    risk_free_rate = ql.YieldTermStructureHandle(flat_risk_free)
    volatility = ql.BlackVolTermStructureHandle(flat_vol)

    bs_process = ql.GeneralizedBlackScholesProcess(
        ql.QuoteHandle(ql.SimpleQuote(100.0)),
        dividend_yield,
        risk_free_rate,
        volatility,
    )

    engine = qlAnalyticBSMHullWhiteEngine(
        equity_short_rate_correlation=0.5,
        process=bs_process,
        model=model,
    )
    assert isinstance(engine, ql.AnalyticBSMHullWhiteEngine)
