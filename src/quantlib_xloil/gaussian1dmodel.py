import QuantLib as ql
import xloil as xlo
from typing import Optional

from .config import EXCEL_GROUP_NAME
from .date import qDate, qPeriod
from .ratehelpers import qQuoteHandle
from .utilities import (
    enum_value,
    first_key,
    to_float_list,
    to_object_list,
    UNKNOWN_KEY,
    UNKNOWN_VALUE,
)

# Probabilities enum for Gaussian1d engines

QL_GAUSSIAN1D_PROBABILITIES = {
    "NONE": ql.Gaussian1dSwaptionEngine.NoProb,
    "NAIVE": ql.Gaussian1dSwaptionEngine.Naive,
    "DIGITAL": ql.Gaussian1dSwaptionEngine.Digital,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qGaussian1dProbabilities(s: str) -> int:
    return enum_value(s, QL_GAUSSIAN1D_PROBABILITIES)


@xlo.converter()
def qGaussian1dProbabilities(s: str) -> int:
    return _qGaussian1dProbabilities(s)


# Gaussian1dModel interface


@xlo.func(
    help="Return the stochastic process of a Gaussian1d model.",
    args={"model": "QuantLib Gaussian1dModel object."},
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dModelStateProcess(
    model: ql.Gaussian1dModel, trigger=None
) -> ql.StochasticProcess1D:
    return model.stateProcess()


@xlo.func(
    help="Return the numeraire value for a Gaussian1d model.",
    args={
        "model": "QuantLib Gaussian1dModel object.",
        "t": "Time in years.",
        "y": "Normalised state variable.",
        "yts": "Optional handle to the yield term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dModelNumeraireFromTime(
    model: ql.Gaussian1dModel,
    t: float,
    y: float = 0.0,
    yts: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> float:
    return model.numeraire(t, y, yts)


@xlo.func(
    help="Return the numeraire value for a Gaussian1d model at a given date.",
    args={
        "model": "QuantLib Gaussian1dModel object.",
        "reference_date": "Reference date.",
        "y": "Normalised state variable.",
        "yts": "Optional handle to the yield term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dModelNumeraire(
    model: ql.Gaussian1dModel,
    reference_date: qDate,
    y: float = 0.0,
    yts: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> float:
    return model.numeraire(reference_date, y, yts)


@xlo.func(
    help="Return the zero bond price P(t, T) from a Gaussian1d model using times.",
    args={
        "model": "QuantLib Gaussian1dModel object.",
        "T": "Maturity time in years.",
        "t": "Reference time in years.",
        "y": "Normalised state variable.",
        "yts": "Optional handle to the yield term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dModelZerobondFromTime(
    model: ql.Gaussian1dModel,
    T: float,
    t: float = 0.0,
    y: float = 0.0,
    yts: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> float:
    return model.zerobond(T, t, y, yts)


@xlo.func(
    help="Return the zero bond price P(maturity, referenceDate) from a Gaussian1d model using dates.",
    args={
        "model": "QuantLib Gaussian1dModel object.",
        "maturity": "Maturity date.",
        "reference_date": "Reference date (defaults to today).",
        "y": "Normalised state variable.",
        "yts": "Optional handle to the yield term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dModelZerobond(
    model: ql.Gaussian1dModel,
    maturity: qDate,
    reference_date: qDate = ql.Date(),
    y: float = 0.0,
    yts: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> float:
    return model.zerobond(maturity, reference_date, y, yts)


@xlo.func(
    help="Return the zero bond option price from a Gaussian1d model.",
    args={
        "model": "QuantLib Gaussian1dModel object.",
        "option_type": "Option type ('Call' or 'Put').",
        "expiry": "Option expiry date.",
        "value_date": "Value date of the underlying bond.",
        "maturity": "Maturity date of the underlying bond.",
        "strike": "Strike price.",
        "reference_date": "Reference date (defaults to today).",
        "y": "Normalised state variable.",
        "yts": "Optional handle to the yield term structure.",
        "y_std_devs": "Number of standard deviations for grid.",
        "y_grid_points": "Number of grid points.",
        "extrapolate_payoff": "Whether to extrapolate the payoff.",
        "flat_payoff_extrapolation": "Whether to use flat payoff extrapolation.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dModelZerobondOption(
    model: ql.Gaussian1dModel,
    option_type: str,
    expiry: qDate,
    value_date: qDate,
    maturity: qDate,
    strike: float,
    reference_date: qDate = ql.Date(),
    y: float = 0.0,
    yts: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    y_std_devs: float = 7.0,
    y_grid_points: int = 64,
    extrapolate_payoff: bool = True,
    flat_payoff_extrapolation: bool = False,
    trigger=None,
) -> float:
    opt_type = (
        ql.Option.Call if option_type.strip().upper() == "CALL" else ql.Option.Put
    )
    return model.zerobondOption(
        opt_type,
        expiry,
        value_date,
        maturity,
        strike,
        reference_date,
        y,
        yts,
        y_std_devs,
        y_grid_points,
        extrapolate_payoff,
        flat_payoff_extrapolation,
    )


@xlo.func(
    help="Return the forward rate for an Ibor index from a Gaussian1d model.",
    args={
        "model": "QuantLib Gaussian1dModel object.",
        "fixing": "Fixing date of the Ibor rate.",
        "reference_date": "Reference date (defaults to today).",
        "y": "Normalised state variable.",
        "ibor_index": "Optional Ibor index.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dModelForwardRate(
    model: ql.Gaussian1dModel,
    fixing: qDate,
    reference_date: qDate = ql.Date(),
    y: float = 0.0,
    ibor_index: Optional[ql.IborIndex] = None,
    trigger=None,
) -> float:
    if ibor_index is None:
        ibor_index = ql.IborIndex.__new__(ql.IborIndex)
    return model.forwardRate(fixing, reference_date, y, ibor_index)


@xlo.func(
    help="Return the swap rate for a swap index from a Gaussian1d model.",
    args={
        "model": "QuantLib Gaussian1dModel object.",
        "fixing": "Fixing date of the swap rate.",
        "tenor": "Tenor of the swap.",
        "reference_date": "Reference date (defaults to today).",
        "y": "Normalised state variable.",
        "swap_index": "Optional swap index.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dModelSwapRate(
    model: ql.Gaussian1dModel,
    fixing: qDate,
    tenor: qPeriod,
    reference_date: qDate = ql.Date(),
    y: float = 0.0,
    swap_index: Optional[ql.SwapIndex] = None,
    trigger=None,
) -> float:
    if swap_index is None:
        swap_index = ql.SwapIndex.__new__(ql.SwapIndex)
    return model.swapRate(fixing, tenor, reference_date, y, swap_index)


@xlo.func(
    help="Return the swap annuity from a Gaussian1d model.",
    args={
        "model": "QuantLib Gaussian1dModel object.",
        "fixing": "Fixing date of the swap.",
        "tenor": "Tenor of the swap.",
        "reference_date": "Reference date (defaults to today).",
        "y": "Normalised state variable.",
        "swap_index": "Optional swap index.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dModelSwapAnnuity(
    model: ql.Gaussian1dModel,
    fixing: qDate,
    tenor: qPeriod,
    reference_date: qDate = ql.Date(),
    y: float = 0.0,
    swap_index: Optional[ql.SwapIndex] = None,
    trigger=None,
) -> float:
    if swap_index is None:
        swap_index = ql.SwapIndex.__new__(ql.SwapIndex)
    return model.swapAnnuity(fixing, tenor, reference_date, y, swap_index)


# Gsr model


@xlo.func(
    help="Create a QuantLib Gsr (Gaussian short-rate) model.",
    args={
        "term_structure": "Handle to the yield term structure.",
        "vol_step_dates": "Array of volatility step dates.",
        "volatilities": "Array of volatility quote handles.",
        "reversions": "Array of mean reversion quote handles.",
        "T": "Terminal time in years (default 60.0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGsr(
    term_structure: ql.YieldTermStructureHandle,
    vol_step_dates: xlo.Array(dims=1),
    volatilities: xlo.Array(dims=1),
    reversions: xlo.Array(dims=1),
    T: float = 60.0,
    trigger=None,
) -> ql.Gsr:
    step_dates = [ql.Date(int(d)) for d in vol_step_dates]
    vols = [qQuoteHandle.__wrapped__(v) for v in volatilities]
    revs = [qQuoteHandle.__wrapped__(r) for r in reversions]
    return ql.Gsr(term_structure, step_dates, vols, revs, T)


@xlo.func(
    help="Return the volatility array of a Gsr model.",
    args={"model": "QuantLib Gsr model object."},
    group=EXCEL_GROUP_NAME,
)
def qlGsrVolatility(model: ql.Gsr, trigger=None) -> list[float]:
    return list(model.volatility())


@xlo.func(
    help="Return the reversion array of a Gsr model.",
    args={"model": "QuantLib Gsr model object."},
    group=EXCEL_GROUP_NAME,
)
def qlGsrReversion(model: ql.Gsr, trigger=None) -> list[float]:
    return list(model.reversion())


@xlo.func(
    help="Iteratively calibrate the volatilities of a Gsr model to a set of Black calibration helpers.",
    args={
        "model": "QuantLib Gsr model object.",
        "helpers": "Array of BlackCalibrationHelper objects.",
        "optimization_method": "The optimization method to use.",
        "end_criteria": "The end criteria to use.",
        "constraint": "Optional constraint.",
        "weights": "Optional weights.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGsrCalibrateVolatilitiesIterative(
    model: ql.Gsr,
    helpers: xlo.Array(dims=1),
    optimization_method: ql.OptimizationMethod,
    end_criteria: ql.EndCriteria,
    constraint: ql.Constraint = ql.NoConstraint(),
    weights: xlo.Array(dims=1) = [],
    trigger=None,
) -> bool:
    helpers_ = to_object_list(helpers, ql.BlackCalibrationHelper)
    weights_ = [float(w) for w in weights]
    model.calibrateVolatilitiesIterative(
        helpers_, optimization_method, end_criteria, constraint, weights_
    )
    return True


# MarkovFunctional model


@xlo.func(
    help="Create a QuantLib MarkovFunctional model calibrated to a swaption smile.",
    args={
        "term_structure": "Handle to the yield term structure.",
        "reversion": "Mean reversion speed.",
        "vol_step_dates": "Array of volatility step dates.",
        "volatilities": "Array of initial volatility values.",
        "swaption_vol": "Handle to the swaption volatility structure.",
        "swaption_expiries": "Array of swaption expiry dates.",
        "swaption_tenors": "Array of swaption tenors.",
        "swap_index_base": "Swap index for the underlying swap.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMarkovFunctional(
    term_structure: ql.YieldTermStructureHandle,
    reversion: float,
    vol_step_dates: xlo.Array(dims=1),
    volatilities: xlo.Array(dims=1),
    swaption_vol: ql.SwaptionVolatilityStructureHandle,
    swaption_expiries: xlo.Array(dims=1),
    swaption_tenors: xlo.Array(dims=1),
    swap_index_base: ql.SwapIndex,
    trigger=None,
) -> ql.MarkovFunctional:
    step_dates = [ql.Date(int(d)) for d in vol_step_dates]
    vols = to_float_list(volatilities)
    expiries = [ql.Date(int(d)) for d in swaption_expiries]
    tenors = [qPeriod.__wrapped__(t) for t in swaption_tenors]
    return ql.MarkovFunctional(
        term_structure,
        reversion,
        step_dates,
        vols,
        swaption_vol,
        expiries,
        tenors,
        swap_index_base,
    )


@xlo.func(
    help="Create a QuantLib MarkovFunctional model calibrated to a caplet smile.",
    args={
        "term_structure": "Handle to the yield term structure.",
        "reversion": "Mean reversion speed.",
        "vol_step_dates": "Array of volatility step dates.",
        "volatilities": "Array of initial volatility values.",
        "caplet_vol": "Handle to the optionlet volatility structure.",
        "caplet_expiries": "Array of caplet expiry dates.",
        "ibor_index": "Ibor index for the underlying caplets.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMarkovFunctionalFromCaplets(
    term_structure: ql.YieldTermStructureHandle,
    reversion: float,
    vol_step_dates: xlo.Array(dims=1),
    volatilities: xlo.Array(dims=1),
    caplet_vol: ql.OptionletVolatilityStructureHandle,
    caplet_expiries: xlo.Array(dims=1),
    ibor_index: ql.IborIndex,
    trigger=None,
) -> ql.MarkovFunctional:
    step_dates = [ql.Date(int(d)) for d in vol_step_dates]
    vols = to_float_list(volatilities)
    expiries = [ql.Date(int(d)) for d in caplet_expiries]
    return ql.MarkovFunctional(
        term_structure,
        reversion,
        step_dates,
        vols,
        caplet_vol,
        expiries,
        ibor_index,
    )


@xlo.func(
    help="Return the volatility array of a MarkovFunctional model.",
    args={"model": "QuantLib MarkovFunctional model object."},
    group=EXCEL_GROUP_NAME,
)
def qlMarkovFunctionalVolatility(
    model: ql.MarkovFunctional, trigger=None
) -> list[float]:
    return list(model.volatility())


# Gaussian1d pricing engines


@xlo.func(
    help="Create a Gaussian1dSwaptionEngine for pricing swaptions.",
    args={
        "model": "QuantLib Gaussian1dModel object.",
        "integration_points": "Number of integration points (default 64).",
        "stddevs": "Number of standard deviations for the grid (default 7.0).",
        "extrapolate_payoff": "Whether to extrapolate the payoff (default True).",
        "flat_payoff_extrapolation": "Whether to use flat payoff extrapolation (default False).",
        "discount_curve": "Optional handle to the discount curve.",
        "probabilities": "Probabilities output ('None', 'Naive', 'Digital').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dSwaptionEngine(
    model: ql.Gaussian1dModel,
    integration_points: int = 64,
    stddevs: float = 7.0,
    extrapolate_payoff: bool = True,
    flat_payoff_extrapolation: bool = False,
    discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    probabilities: qGaussian1dProbabilities = ql.Gaussian1dSwaptionEngine.NoProb,
    trigger=None,
) -> ql.Gaussian1dSwaptionEngine:
    return ql.Gaussian1dSwaptionEngine(
        model,
        integration_points,
        stddevs,
        extrapolate_payoff,
        flat_payoff_extrapolation,
        discount_curve,
        probabilities,
    )


@xlo.func(
    help="Create a Gaussian1dNonstandardSwaptionEngine for pricing nonstandard swaptions.",
    args={
        "model": "QuantLib Gaussian1dModel object.",
        "integration_points": "Number of integration points (default 64).",
        "stddevs": "Number of standard deviations for the grid (default 7.0).",
        "extrapolate_payoff": "Whether to extrapolate the payoff (default True).",
        "flat_payoff_extrapolation": "Whether to use flat payoff extrapolation (default False).",
        "oas": "Optional handle to the OAS quote (continuously compounded).",
        "discount_curve": "Optional handle to the discount curve.",
        "probabilities": "Probabilities output ('None', 'Naive', 'Digital').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dNonstandardSwaptionEngine(
    model: ql.Gaussian1dModel,
    integration_points: int = 64,
    stddevs: float = 7.0,
    extrapolate_payoff: bool = True,
    flat_payoff_extrapolation: bool = False,
    oas: ql.QuoteHandle = ql.QuoteHandle(),
    discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    probabilities: qGaussian1dProbabilities = ql.Gaussian1dNonstandardSwaptionEngine.NoProb,
    trigger=None,
) -> ql.Gaussian1dNonstandardSwaptionEngine:
    return ql.Gaussian1dNonstandardSwaptionEngine(
        model,
        integration_points,
        stddevs,
        extrapolate_payoff,
        flat_payoff_extrapolation,
        oas,
        discount_curve,
        probabilities,
    )


@xlo.func(
    help="Create a Gaussian1dFloatFloatSwaptionEngine for pricing float-float swaptions.",
    args={
        "model": "QuantLib Gaussian1dModel object.",
        "integration_points": "Number of integration points (default 64).",
        "stddevs": "Number of standard deviations for the grid (default 7.0).",
        "extrapolate_payoff": "Whether to extrapolate the payoff (default True).",
        "flat_payoff_extrapolation": "Whether to use flat payoff extrapolation (default False).",
        "oas": "Optional handle to the OAS quote (continuously compounded).",
        "discount_curve": "Optional handle to the discount curve.",
        "include_todays_exercise": "Whether to include today's exercise date (default False).",
        "probabilities": "Probabilities output ('None', 'Naive', 'Digital').",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dFloatFloatSwaptionEngine(
    model: ql.Gaussian1dModel,
    integration_points: int = 64,
    stddevs: float = 7.0,
    extrapolate_payoff: bool = True,
    flat_payoff_extrapolation: bool = False,
    oas: ql.QuoteHandle = ql.QuoteHandle(),
    discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    include_todays_exercise: bool = False,
    probabilities: qGaussian1dProbabilities = ql.Gaussian1dFloatFloatSwaptionEngine.NoProb,
    trigger=None,
) -> ql.Gaussian1dFloatFloatSwaptionEngine:
    return ql.Gaussian1dFloatFloatSwaptionEngine(
        model,
        integration_points,
        stddevs,
        extrapolate_payoff,
        flat_payoff_extrapolation,
        oas,
        discount_curve,
        include_todays_exercise,
        probabilities,
    )


@xlo.func(
    help="Create a Gaussian1dJamshidianSwaptionEngine for pricing swaptions via Jamshidian decomposition.",
    args={"model": "QuantLib Gaussian1dModel object."},
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dJamshidianSwaptionEngine(
    model: ql.Gaussian1dModel, trigger=None
) -> ql.Gaussian1dJamshidianSwaptionEngine:
    return ql.Gaussian1dJamshidianSwaptionEngine(model)


@xlo.func(
    help="Create a Gaussian1dCapFloorEngine for pricing caps and floors.",
    args={
        "model": "QuantLib Gaussian1dModel object.",
        "integration_points": "Number of integration points (default 64).",
        "stddevs": "Number of standard deviations for the grid (default 7.0).",
        "extrapolate_payoff": "Whether to extrapolate the payoff (default True).",
        "flat_payoff_extrapolation": "Whether to use flat payoff extrapolation (default False).",
        "discount_curve": "Optional handle to the discount curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGaussian1dCapFloorEngine(
    model: ql.Gaussian1dModel,
    integration_points: int = 64,
    stddevs: float = 7.0,
    extrapolate_payoff: bool = True,
    flat_payoff_extrapolation: bool = False,
    discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> ql.Gaussian1dCapFloorEngine:
    return ql.Gaussian1dCapFloorEngine(
        model,
        integration_points,
        stddevs,
        extrapolate_payoff,
        flat_payoff_extrapolation,
        discount_curve,
    )
