import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .payoffs import qOptionType
from .utilities import to_float_list


@xlo.func(
    help="Return the discount factor for a given time.",
    args={
        "model": "The QuantLib OneFactorAffineModel.",
        "t": "Time in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qllOneFactorAffineModelDiscount(
    model: ql.OneFactorAffineModel, t: float, trigger=None
) -> float:
    return model.discount(t)


@xlo.func(
    help="Return the discount bond option price using factors.",
    args={
        "model": "The QuantLib OneFactorAffineModel.",
        "now": "Current time in years.",
        "maturity": "Maturity time in years.",
        "factors": "Array of factors.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneFactorAffineModelDiscountBond(
    model: ql.OneFactorAffineModel,
    now: float,
    maturity: float,
    factors: xlo.Array(dims=1),
    trigger=None,
) -> float:
    factors_ = ql.Array(to_float_list(factors))
    return model.discountBond(now, maturity, factors_)


@xlo.func(
    help="Return the discount bond price.",
    args={
        "model": "The QuantLib OneFactorAffineModel.",
        "now": "Current time in years.",
        "maturity": "Maturity time in years.",
        "rate": "Rate.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneFactorAffineModelDiscountBond2(
    model: ql.OneFactorAffineModel,
    now: float,
    maturity: float,
    rate: float,
    trigger=None,
) -> float:
    return model.discountBond(now, maturity, rate)


@xlo.func(
    help="Return the discount bond option price.",
    args={
        "model": "The QuantLib OneFactorAffineModel.",
        "option_type": "Option type ('Call' or 'Put').",
        "strike": "Strike price.",
        "maturity": "Maturity time in years.",
        "bond_maturity": "Bond maturity time in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOneFactorAffineModelDiscountBondOption(
    model: ql.OneFactorAffineModel,
    option_type: qOptionType,
    strike: float,
    maturity: float,
    bond_maturity: float,
    trigger=None,
) -> float:
    return model.discountBondOption(option_type, strike, maturity, bond_maturity)


@xlo.func(
    help="Create a QuantLib Vasicek short-rate model.",
    args={
        "r0": "Initial short rate (default 0.05).",
        "a": "Mean reversion speed (default 0.1).",
        "b": "Long-term mean rate (default 0.05).",
        "sigma": "Volatility (default 0.01).",
        "lambda": "Market price of risk (default 0.0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlVasicek(
    r0: float = 0.05,
    a: float = 0.1,
    b: float = 0.05,
    sigma: float = 0.01,
    lambda_: float = 0.0,
    trigger=None,
) -> ql.Vasicek:
    return ql.Vasicek(r0, a, b, sigma, lambda_)


@xlo.func(
    help="Create a QuantLib Hull-White short-rate model.",
    args={
        "term_structure": "Handle to the yield term structure.",
        "a": "Mean reversion speed (default 0.1).",
        "sigma": "Volatility (default 0.01).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHullWhite(
    term_structure: ql.YieldTermStructureHandle,
    a: float = 0.1,
    sigma: float = 0.01,
    trigger=None,
) -> ql.HullWhite:
    return ql.HullWhite(term_structure, a, sigma)


@xlo.func(
    help="Compute the convexity bias for Hull-White model.",
    args={
        "future_price": "Futures price.",
        "t": "Time to futures maturity in years.",
        "T": "Time to bond maturity in years.",
        "sigma": "Volatility.",
        "a": "Mean reversion speed.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHullWhiteConvexityBias(
    future_price: float,
    t: float,
    T: float,
    sigma: float,
    a: float,
    trigger=None,
) -> float:
    return ql.HullWhite.convexityBias(future_price, t, T, sigma, a)


@xlo.func(
    help="Get the term structure from a Hull-White model.",
    args={
        "model": "The QuantLib HullWhite model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlHullWhiteTermStructure(
    model: ql.HullWhite, trigger=None
) -> ql.YieldTermStructureHandle:
    return model.termStructure()


@xlo.func(
    help="Create a QuantLib Black-Karasinski short-rate model.",
    args={
        "term_structure": "Handle to the yield term structure.",
        "a": "Mean reversion speed (default 0.1).",
        "sigma": "Volatility (default 0.1).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackKarasinski(
    term_structure: ql.YieldTermStructureHandle,
    a: float = 0.1,
    sigma: float = 0.1,
    trigger=None,
) -> ql.BlackKarasinski:
    return ql.BlackKarasinski(term_structure, a, sigma)


@xlo.func(
    help="Get the term structure from a Black-Karasinski model.",
    args={
        "model": "The QuantLib BlackKarasinski model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackKarasinskiTermStructure(
    model: ql.BlackKarasinski, trigger=None
) -> ql.YieldTermStructureHandle:
    return model.termStructure()


@xlo.func(
    help="Create a QuantLib Cox-Ingersoll-Ross short-rate model.",
    args={
        "r0": "Initial short rate (default 0.01).",
        "theta": "Long-term mean rate (default 0.1).",
        "k": "Mean reversion speed (default 0.1).",
        "sigma": "Volatility (default 0.1).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCoxIngersollRoss(
    r0: float = 0.01,
    theta: float = 0.1,
    k: float = 0.1,
    sigma: float = 0.1,
    trigger=None,
) -> ql.CoxIngersollRoss:
    return ql.CoxIngersollRoss(r0, theta, k, sigma)


@xlo.func(
    help="Create a QuantLib Extended Cox-Ingersoll-Ross short-rate model.",
    args={
        "term_structure": "Handle to the yield term structure.",
        "theta": "Long-term mean rate (default 0.1).",
        "k": "Mean reversion speed (default 0.1).",
        "sigma": "Volatility (default 0.1).",
        "x0": "Initial value (default 0.05).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExtendedCoxIngersollRoss(
    term_structure: ql.YieldTermStructureHandle,
    theta: float = 0.1,
    k: float = 0.1,
    sigma: float = 0.1,
    x0: float = 0.05,
    trigger=None,
) -> ql.ExtendedCoxIngersollRoss:
    return ql.ExtendedCoxIngersollRoss(term_structure, theta, k, sigma, x0)


@xlo.func(
    help="Get the term structure from an Extended Cox-Ingersoll-Ross model.",
    args={
        "model": "The QuantLib ExtendedCoxIngersollRoss model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExtendedCoxIngersollRossTermStructure(
    model: ql.ExtendedCoxIngersollRoss, trigger=None
) -> ql.YieldTermStructureHandle:
    return model.termStructure()


# Registration of qlG2 fails in Excel. Function has been renamed to qlG2Model.
@xlo.func(
    help="Create a QuantLib G2 two-factor short-rate model.",
    args={
        "term_structure": "Handle to the yield term structure.",
        "a": "Mean reversion speed for first factor (default 0.1).",
        "sigma": "Volatility for first factor (default 0.01).",
        "b": "Mean reversion speed for second factor (default 0.1).",
        "eta": "Volatility for second factor (default 0.01).",
        "rho": "Correlation between factors (default -0.75).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlG2Model(
    term_structure: ql.YieldTermStructureHandle,
    a: float = 0.1,
    sigma: float = 0.01,
    b: float = 0.1,
    eta: float = 0.01,
    rho: float = -0.75,
    trigger=None,
) -> ql.G2:
    return ql.G2(term_structure, a, sigma, b, eta, rho)


@xlo.func(
    help="Get the term structure from a G2 model.",
    args={
        "model": "The QuantLib G2 model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlG2TermStructure(model: ql.G2, trigger=None) -> ql.YieldTermStructureHandle:
    return model.termStructure()


@xlo.func(
    help="Compute discount factor for G2 model.",
    args={
        "model": "The QuantLib G2 model.",
        "t": "Time in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlG2Discount(
    model: ql.G2,
    t: float,
    trigger=None,
) -> float:
    return model.discount(t)


@xlo.func(
    help="Compute discount bond price for G2 model.",
    args={
        "model": "The QuantLib G2 model.",
        "now": "Current time in years.",
        "maturity": "Maturity time in years.",
        "factors": "Array of factors.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlG2DiscountBond(
    model: ql.G2,
    now: float,
    maturity: float,
    factors: xlo.Array(dims=1),
    trigger=None,
) -> float:
    factors_ = ql.Array(to_float_list(factors))
    return model.discountBond(now, maturity, factors_)


@xlo.func(
    help="Compute discount bond option price for G2 model.",
    args={
        "model": "The QuantLib G2 model.",
        "option_type": "Option type ('Call' or 'Put').",
        "strike": "Strike price.",
        "maturity": "Maturity time in years.",
        "bond_maturity": "Bond maturity time in years.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlG2DiscountBondOption(
    model: ql.G2,
    option_type: qOptionType,
    strike: float,
    maturity: float,
    bond_maturity: float,
    trigger=None,
) -> float:
    return model.discountBondOption(option_type, strike, maturity, bond_maturity)


@xlo.func(
    help="Create a JamshidianSwaptionEngine for pricing swaptions.",
    args={
        "model": "The QuantLib OneFactorAffineModel.",
        "term_structure": "Optional handle to the yield term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlJamshidianSwaptionEngine(
    model: ql.OneFactorAffineModel,
    term_structure: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> ql.JamshidianSwaptionEngine:
    return ql.JamshidianSwaptionEngine(model, term_structure)


@xlo.func(
    help="Create a TreeSwaptionEngine for pricing swaptions using a tree.",
    args={
        "model": "The QuantLib ShortRateModel.",
        "time_steps": "Number of time steps.",
        "term_structure": "Optional handle to the yield term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTreeSwaptionEngine(
    model: ql.ShortRateModel,
    time_steps: int,
    term_structure: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> ql.TreeSwaptionEngine:
    return ql.TreeSwaptionEngine(model, time_steps, term_structure)


@xlo.func(
    help="Create a TreeSwaptionEngine for pricing swaptions using a time grid.",
    args={
        "model": "The QuantLib ShortRateModel.",
        "grid": "Time grid as array of times.",
        "term_structure": "Optional handle to the yield term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTreeSwaptionEngine2(
    model: ql.ShortRateModel,
    grid: xlo.Array(dims=1),
    term_structure: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> ql.TreeSwaptionEngine:
    grid_ = ql.TimeGrid(to_float_list(grid))
    return ql.TreeSwaptionEngine(model, grid_, term_structure)


@xlo.func(
    help="Create an AnalyticCapFloorEngine for pricing caps and floors.",
    args={
        "model": "The QuantLib OneFactorAffineModel.",
        "term_structure": "Optional handle to the yield term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticCapFloorEngine(
    model: ql.OneFactorAffineModel,
    term_structure: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> ql.AnalyticCapFloorEngine:
    return ql.AnalyticCapFloorEngine(model, term_structure)


@xlo.func(
    help="Create a TreeCapFloorEngine for pricing caps and floors using a tree.",
    args={
        "model": "The QuantLib ShortRateModel.",
        "time_steps": "Number of time steps.",
        "term_structure": "Optional handle to the yield term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTreeCapFloorEngine(
    model: ql.ShortRateModel,
    time_steps: int,
    term_structure: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> ql.TreeCapFloorEngine:
    return ql.TreeCapFloorEngine(model, time_steps, term_structure)


@xlo.func(
    help="Create a TreeCapFloorEngine for pricing caps and floors using a time grid.",
    args={
        "model": "The QuantLib ShortRateModel.",
        "grid": "Time grid as array of times.",
        "term_structure": "Optional handle to the yield term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTreeCapFloorEngine2(
    model: ql.ShortRateModel,
    grid: xlo.Array(dims=1),
    term_structure: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> ql.TreeCapFloorEngine:
    grid_ = ql.TimeGrid(to_float_list(grid))
    return ql.TreeCapFloorEngine(model, grid_, term_structure)


@xlo.func(
    help="Create a G2SwaptionEngine for pricing swaptions using G2 model.",
    args={
        "model": "The QuantLib G2 model.",
        "range": "Range for integration.",
        "intervals": "Number of intervals.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlG2SwaptionEngine(
    model: ql.G2,
    range_: float,
    intervals: int,
    trigger=None,
) -> ql.G2SwaptionEngine:
    return ql.G2SwaptionEngine(model, range_, intervals)


@xlo.func(
    help="Create a FdG2SwaptionEngine for pricing swaptions using finite differences.",
    args={
        "model": "The QuantLib G2 model.",
        "t_grid": "Number of time grid points (default 100).",
        "x_grid": "Number of x grid points (default 50).",
        "y_grid": "Number of y grid points (default 50).",
        "damping_steps": "Number of damping steps (default 0).",
        "inv_eps": "Inverse epsilon for damping (default 1e-5).",
        "scheme_desc": "Finite difference scheme descriptor (default 'Hundsdorfer').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdG2SwaptionEngine(
    model: ql.G2,
    t_grid: int = 100,
    x_grid: int = 50,
    y_grid: int = 50,
    damping_steps: int = 0,
    inv_eps: float = 1e-5,
    scheme_desc: ql.FdmSchemeDesc = ql.FdmSchemeDesc.Hundsdorfer(),
    trigger=None,
) -> ql.FdG2SwaptionEngine:
    return ql.FdG2SwaptionEngine(
        model, t_grid, x_grid, y_grid, damping_steps, inv_eps, scheme_desc
    )


@xlo.func(
    help="Create a FdHullWhiteSwaptionEngine for pricing swaptions using finite differences.",
    args={
        "model": "The QuantLib HullWhite model.",
        "t_grid": "Number of time grid points (default 100).",
        "x_grid": "Number of x grid points (default 100).",
        "damping_steps": "Number of damping steps (default 0).",
        "inv_eps": "Inverse epsilon for damping (default 1e-5).",
        "scheme_desc": "Finite difference scheme descriptor (default 'Douglas').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFdHullWhiteSwaptionEngine(
    model: ql.HullWhite,
    t_grid: int = 100,
    x_grid: int = 100,
    damping_steps: int = 0,
    inv_eps: float = 1e-5,
    scheme_desc: ql.FdmSchemeDesc = ql.FdmSchemeDesc.Douglas(),
    trigger=None,
) -> ql.FdHullWhiteSwaptionEngine:
    return ql.FdHullWhiteSwaptionEngine(
        model, t_grid, x_grid, damping_steps, inv_eps, scheme_desc
    )


@xlo.func(
    help="Create an AnalyticBSMHullWhiteEngine for pricing options.",
    args={
        "equity_short_rate_correlation": "Correlation between equity and short rate.",
        "process": "The QuantLib GeneralizedBlackScholesProcess.",
        "model": "The QuantLib HullWhite model.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAnalyticBSMHullWhiteEngine(
    equity_short_rate_correlation: float,
    process: ql.GeneralizedBlackScholesProcess,
    model: ql.HullWhite,
    trigger=None,
) -> ql.AnalyticBSMHullWhiteEngine:
    return ql.AnalyticBSMHullWhiteEngine(equity_short_rate_correlation, process, model)
