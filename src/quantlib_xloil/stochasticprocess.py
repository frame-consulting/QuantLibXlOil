import numpy as np
import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .ratehelpers import qQuoteHandle
from .utilities import enum_value, first_key, UNKNOWN_KEY, UNKNOWN_VALUE


QL_HESTON_PROCESS_DISCRETIZATION = {
	"PARTIALTRUNCATION": ql.HestonProcess.PartialTruncation,
	"FULLTRUNCATION": ql.HestonProcess.FullTruncation,
	"REFLECTION": ql.HestonProcess.Reflection,
	"NONCENTRALCHISQUAREVARIANCE": ql.HestonProcess.NonCentralChiSquareVariance,
	"QUADRATICEXPONENTIAL": ql.HestonProcess.QuadraticExponential,
	"QUADRATICEXPONENTIALMARTINGALE": ql.HestonProcess.QuadraticExponentialMartingale,
	"BROADIEKAYAEXACTSCHEMELOBATTO": ql.HestonProcess.BroadieKayaExactSchemeLobatto,
	"BROADIEKAYAEXACTSCHEMELAGUERRE": ql.HestonProcess.BroadieKayaExactSchemeLaguerre,
	"BROADIEKAYAEXACTSCHEMETRAPEZOIDAL": ql.HestonProcess.BroadieKayaExactSchemeTrapezoidal,
	UNKNOWN_KEY: UNKNOWN_VALUE,
}

QL_GJRGARCH_PROCESS_DISCRETIZATION = {
	"PARTIALTRUNCATION": ql.GJRGARCHProcess.PartialTruncation,
	"FULLTRUNCATION": ql.GJRGARCHProcess.FullTruncation,
	"REFLECTION": ql.GJRGARCHProcess.Reflection,
	UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _to_float_list(values) -> list[float]:
	if values is None:
		return []
	if isinstance(values, (int, float)):
		return [float(values)]
	if isinstance(values, (list, tuple)):
		return [float(v) for v in values]
	if isinstance(values, np.ndarray):
		return values.astype(float).ravel().tolist()
	return [float(v) for v in list(values)]


def _to_float_matrix(values) -> list[list[float]]:
	if values is None:
		return []
	if isinstance(values, np.ndarray):
		return values.astype(float).tolist()
	if isinstance(values, ql.Matrix):
		return [[float(values[i][j]) for j in range(values.columns())] for i in range(values.rows())]
	return [[float(v) for v in row] for row in values]


def _qHestonProcessDiscretization(discretization: str) -> int:
	return enum_value(discretization, QL_HESTON_PROCESS_DISCRETIZATION)


def _qGJRGARCHProcessDiscretization(discretization: str) -> int:
	return enum_value(discretization, QL_GJRGARCH_PROCESS_DISCRETIZATION)


@xlo.converter()
def qHestonProcessDiscretization(discretization: str) -> int:
	return _qHestonProcessDiscretization(discretization)


@xlo.converter()
def qGJRGARCHProcessDiscretization(discretization: str) -> int:
	return _qGJRGARCHProcessDiscretization(discretization)


@xlo.func(
	help="Return stochastic-process size.",
	args={
		"process": "QuantLib stochastic process.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcessSize(process: ql.StochasticProcess, trigger=None) -> int:
	return process.size()


@xlo.func(
	help="Return stochastic-process factor count.",
	args={
		"process": "QuantLib stochastic process.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcessFactors(process: ql.StochasticProcess, trigger=None) -> int:
	return process.factors()


@xlo.func(
	help="Return stochastic-process initial values.",
	args={
		"process": "QuantLib stochastic process.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcessInitialValues(process: ql.StochasticProcess, trigger=None) -> list[float]:
	return _to_float_list(process.initialValues())


@xlo.func(
	help="Return stochastic-process drift.",
	args={
		"process": "QuantLib stochastic process.",
		"t": "Time.",
		"x": "State vector.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcessDrift(process: ql.StochasticProcess, t: float, x: xlo.Array(dims=1), trigger=None) -> list[float]:
	return _to_float_list(process.drift(t, ql.Array(_to_float_list(x))))


@xlo.func(
	help="Return stochastic-process diffusion.",
	args={
		"process": "QuantLib stochastic process.",
		"t": "Time.",
		"x": "State vector.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcessDiffusion(process: ql.StochasticProcess, t: float, x: xlo.Array(dims=1), trigger=None) -> list[list[float]]:
	return _to_float_matrix(process.diffusion(t, ql.Array(_to_float_list(x))))


@xlo.func(
	help="Return stochastic-process expectation.",
	args={
		"process": "QuantLib stochastic process.",
		"t0": "Start time.",
		"x0": "Initial state vector.",
		"dt": "Time step.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcessExpectation(process: ql.StochasticProcess, t0: float, x0: xlo.Array(dims=1), dt: float, trigger=None) -> list[float]:
	return _to_float_list(process.expectation(t0, ql.Array(_to_float_list(x0)), dt))


@xlo.func(
	help="Return stochastic-process standard deviation matrix.",
	args={
		"process": "QuantLib stochastic process.",
		"t0": "Start time.",
		"x0": "Initial state vector.",
		"dt": "Time step.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcessStdDeviation(process: ql.StochasticProcess, t0: float, x0: xlo.Array(dims=1), dt: float, trigger=None) -> list[list[float]]:
	return _to_float_matrix(process.stdDeviation(t0, ql.Array(_to_float_list(x0)), dt))


@xlo.func(
	help="Return stochastic-process covariance matrix.",
	args={
		"process": "QuantLib stochastic process.",
		"t0": "Start time.",
		"x0": "Initial state vector.",
		"dt": "Time step.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcessCovariance(process: ql.StochasticProcess, t0: float, x0: xlo.Array(dims=1), dt: float, trigger=None) -> list[list[float]]:
	return _to_float_matrix(process.covariance(t0, ql.Array(_to_float_list(x0)), dt))


@xlo.func(
	help="Evolve a stochastic process.",
	args={
		"process": "QuantLib stochastic process.",
		"t0": "Start time.",
		"x0": "Initial state vector.",
		"dt": "Time step.",
		"dw": "Brownian increment vector.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcessEvolve(process: ql.StochasticProcess, t0: float, x0: xlo.Array(dims=1), dt: float, dw: xlo.Array(dims=1), trigger=None) -> list[float]:
	return _to_float_list(process.evolve(t0, ql.Array(_to_float_list(x0)), dt, ql.Array(_to_float_list(dw))))


@xlo.func(
	help="Return 1D stochastic-process state value.",
	args={
		"process": "QuantLib 1D stochastic process.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcess1DX0(process: ql.StochasticProcess1D, trigger=None) -> float:
	return process.x0()


@xlo.func(
	help="Return 1D stochastic-process drift.",
	args={
		"process": "QuantLib 1D stochastic process.",
		"t": "Time.",
		"x": "State value.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcess1DDrift(process: ql.StochasticProcess1D, t: float, x: float, trigger=None) -> float:
	return process.drift(t, x)


@xlo.func(
	help="Return 1D stochastic-process diffusion.",
	args={
		"process": "QuantLib 1D stochastic process.",
		"t": "Time.",
		"x": "State value.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcess1DDiffusion(process: ql.StochasticProcess1D, t: float, x: float, trigger=None) -> float:
	return process.diffusion(t, x)


@xlo.func(
	help="Return 1D stochastic-process expectation.",
	args={
		"process": "QuantLib 1D stochastic process.",
		"t0": "Start time.",
		"x0": "Initial state value.",
		"dt": "Time step.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcess1DExpectation(process: ql.StochasticProcess1D, t0: float, x0: float, dt: float, trigger=None) -> float:
	return process.expectation(t0, x0, dt)


@xlo.func(
	help="Return 1D stochastic-process standard deviation.",
	args={
		"process": "QuantLib 1D stochastic process.",
		"t0": "Start time.",
		"x0": "Initial state value.",
		"dt": "Time step.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcess1DStdDeviation(process: ql.StochasticProcess1D, t0: float, x0: float, dt: float, trigger=None) -> float:
	return process.stdDeviation(t0, x0, dt)


@xlo.func(
	help="Return 1D stochastic-process variance.",
	args={
		"process": "QuantLib 1D stochastic process.",
		"t0": "Start time.",
		"x0": "Initial state value.",
		"dt": "Time step.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcess1DVariance(process: ql.StochasticProcess1D, t0: float, x0: float, dt: float, trigger=None) -> float:
	return process.variance(t0, x0, dt)


@xlo.func(
	help="Evolve a 1D stochastic process.",
	args={
		"process": "QuantLib 1D stochastic process.",
		"t0": "Start time.",
		"x0": "Initial state value.",
		"dt": "Time step.",
		"dw": "Brownian increment.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcess1DEvolve(process: ql.StochasticProcess1D, t0: float, x0: float, dt: float, dw: float, trigger=None) -> float:
	return process.evolve(t0, x0, dt, dw)


@xlo.func(
	help="Apply a 1D stochastic process increment.",
	args={
		"process": "QuantLib 1D stochastic process.",
		"x0": "Initial state value.",
		"dx": "Increment.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcess1DApply(process: ql.StochasticProcess1D, x0: float, dx: float, trigger=None) -> float:
	return process.apply(x0, dx)


@xlo.func(
	help="Create a QuantLib GeneralizedBlackScholesProcess object.",
	args={
		"s0": "Initial underlying quote handle.",
		"dividend_ts": "Dividend yield term structure handle.",
		"risk_free_ts": "Risk-free yield term structure handle.",
		"vol_ts": "Black volatility term structure handle.",
		"local_vol_ts": "Local volatility term structure handle.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGeneralizedBlackScholesProcess(
	s0: qQuoteHandle,
	dividend_ts: ql.YieldTermStructureHandle,
	risk_free_ts: ql.YieldTermStructureHandle,
	vol_ts: ql.BlackVolTermStructureHandle,
	local_vol_ts: ql.LocalVolTermStructureHandle = None,
	trigger=None,
) -> ql.GeneralizedBlackScholesProcess:
	if local_vol_ts is None:
		return ql.GeneralizedBlackScholesProcess(s0, dividend_ts, risk_free_ts, vol_ts)
	return ql.GeneralizedBlackScholesProcess(s0, dividend_ts, risk_free_ts, vol_ts, local_vol_ts)


@xlo.func(
	help="Return the state variable of a GeneralizedBlackScholesProcess.",
	args={
		"process": "QuantLib GeneralizedBlackScholesProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGeneralizedBlackScholesProcessStateVariable(process: ql.GeneralizedBlackScholesProcess, trigger=None) -> ql.QuoteHandle:
	return process.stateVariable()


@xlo.func(
	help="Return the dividend yield of a GeneralizedBlackScholesProcess.",
	args={
		"process": "QuantLib GeneralizedBlackScholesProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGeneralizedBlackScholesProcessDividendYield(process: ql.GeneralizedBlackScholesProcess, trigger=None) -> ql.YieldTermStructureHandle:
	return process.dividendYield()


@xlo.func(
	help="Return the risk-free rate of a GeneralizedBlackScholesProcess.",
	args={
		"process": "QuantLib GeneralizedBlackScholesProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGeneralizedBlackScholesProcessRiskFreeRate(process: ql.GeneralizedBlackScholesProcess, trigger=None) -> ql.YieldTermStructureHandle:
	return process.riskFreeRate()


@xlo.func(
	help="Return the Black volatility of a GeneralizedBlackScholesProcess.",
	args={
		"process": "QuantLib GeneralizedBlackScholesProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGeneralizedBlackScholesProcessBlackVolatility(process: ql.GeneralizedBlackScholesProcess, trigger=None) -> ql.BlackVolTermStructureHandle:
	return process.blackVolatility()


@xlo.func(
	help="Return the local volatility of a GeneralizedBlackScholesProcess.",
	args={
		"process": "QuantLib GeneralizedBlackScholesProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGeneralizedBlackScholesProcessLocalVolatility(process: ql.GeneralizedBlackScholesProcess, trigger=None) -> ql.LocalVolTermStructureHandle:
	return process.localVolatility()


@xlo.func(
	help="Create a QuantLib BlackScholesProcess object.",
	args={
		"s0": "Initial underlying quote handle.",
		"risk_free_ts": "Risk-free yield term structure handle.",
		"vol_ts": "Black volatility term structure handle.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlBlackScholesProcess(
	s0: qQuoteHandle,
	risk_free_ts: ql.YieldTermStructureHandle,
	vol_ts: ql.BlackVolTermStructureHandle,
	trigger=None,
) -> ql.BlackScholesProcess:
	return ql.BlackScholesProcess(s0, risk_free_ts, vol_ts)


@xlo.func(
	help="Create a QuantLib BlackScholesMertonProcess object.",
	args={
		"s0": "Initial underlying quote handle.",
		"dividend_ts": "Dividend yield term structure handle.",
		"risk_free_ts": "Risk-free yield term structure handle.",
		"vol_ts": "Black volatility term structure handle.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlBlackScholesMertonProcess(
	s0: qQuoteHandle,
	dividend_ts: ql.YieldTermStructureHandle,
	risk_free_ts: ql.YieldTermStructureHandle,
	vol_ts: ql.BlackVolTermStructureHandle,
	trigger=None,
) -> ql.BlackScholesMertonProcess:
	return ql.BlackScholesMertonProcess(s0, dividend_ts, risk_free_ts, vol_ts)


@xlo.func(
	help="Create a QuantLib BlackProcess object.",
	args={
		"s0": "Initial underlying quote handle.",
		"risk_free_ts": "Risk-free yield term structure handle.",
		"vol_ts": "Black volatility term structure handle.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlBlackProcess(
	s0: qQuoteHandle,
	risk_free_ts: ql.YieldTermStructureHandle,
	vol_ts: ql.BlackVolTermStructureHandle,
	trigger=None,
) -> ql.BlackProcess:
	return ql.BlackProcess(s0, risk_free_ts, vol_ts)


@xlo.func(
	help="Create a QuantLib GarmanKohlagenProcess object.",
	args={
		"s0": "Initial underlying quote handle.",
		"foreign_risk_free_ts": "Foreign risk-free yield term structure handle.",
		"domestic_risk_free_ts": "Domestic risk-free yield term structure handle.",
		"vol_ts": "Black volatility term structure handle.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGarmanKohlagenProcess(
	s0: qQuoteHandle,
	foreign_risk_free_ts: ql.YieldTermStructureHandle,
	domestic_risk_free_ts: ql.YieldTermStructureHandle,
	vol_ts: ql.BlackVolTermStructureHandle,
	trigger=None,
) -> ql.GarmanKohlagenProcess:
	return ql.GarmanKohlagenProcess(s0, foreign_risk_free_ts, domestic_risk_free_ts, vol_ts)


@xlo.func(
	help="Create a QuantLib Merton76Process object.",
	args={
		"state_variable": "State variable quote handle.",
		"dividend_ts": "Dividend yield term structure handle.",
		"risk_free_ts": "Risk-free yield term structure handle.",
		"vol_ts": "Black volatility term structure handle.",
		"jump_intensity": "Jump intensity quote handle.",
		"mean_log_jump": "Mean log jump quote handle.",
		"jump_volatility": "Jump volatility quote handle.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlMerton76Process(
	state_variable: qQuoteHandle,
	dividend_ts: ql.YieldTermStructureHandle,
	risk_free_ts: ql.YieldTermStructureHandle,
	vol_ts: ql.BlackVolTermStructureHandle,
	jump_intensity: qQuoteHandle,
	mean_log_jump: qQuoteHandle,
	jump_volatility: qQuoteHandle,
	trigger=None,
) -> ql.Merton76Process:
	return ql.Merton76Process(
		state_variable,
		dividend_ts,
		risk_free_ts,
		vol_ts,
		jump_intensity,
		mean_log_jump,
		jump_volatility,
	)


def _to_stochastic_process_list(processes) -> list[ql.StochasticProcess]:
    if processes is None:
        return []
    if isinstance(processes, ql.StochasticProcess):
        return [processes]
    if isinstance(processes, (list, tuple)):
        return [p for p in processes]
    if isinstance(processes, np.ndarray):
        return processes.ravel().tolist()
    raise ValueError(f"Cannot convert {processes} to list of QuantLib CashFlows.")


@xlo.func(
	help="Create a QuantLib StochasticProcessArray object.",
	args={
		"array": "Array of 1D stochastic processes.",
		"correlation": "Correlation matrix.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlStochasticProcessArray(
	array: xlo.Array(dims=1),
	correlation: xlo.Array(dims=2),
	trigger=None,
) -> ql.StochasticProcessArray:
	return ql.StochasticProcessArray(_to_stochastic_process_list(array), ql.Matrix(_to_float_matrix(correlation)))


@xlo.func(
	help="Create a QuantLib GeometricBrownianMotionProcess object.",
	args={
		"initial_value": "Initial state value.",
		"mu": "Drift.",
		"sigma": "Volatility.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGeometricBrownianMotionProcess(
	initial_value: float,
	mu: float,
	sigma: float,
	trigger=None,
) -> ql.GeometricBrownianMotionProcess:
	return ql.GeometricBrownianMotionProcess(initial_value, mu, sigma)


@xlo.func(
	help="Create a QuantLib VarianceGammaProcess object.",
	args={
		"s0": "Initial underlying quote handle.",
		"dividend_yield": "Dividend yield term structure handle.",
		"risk_free_rate": "Risk-free yield term structure handle.",
		"sigma": "Volatility parameter.",
		"nu": "Variance gamma parameter.",
		"theta": "Variance gamma parameter.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlVarianceGammaProcess(
	s0: qQuoteHandle,
	dividend_yield: ql.YieldTermStructureHandle,
	risk_free_rate: ql.YieldTermStructureHandle,
	sigma: float,
	nu: float,
	theta: float,
	trigger=None,
) -> ql.VarianceGammaProcess:
	return ql.VarianceGammaProcess(s0, dividend_yield, risk_free_rate, sigma, nu, theta)


@xlo.func(
	help="Create a QuantLib HestonProcess object.",
	args={
		"risk_free_ts": "Risk-free yield term structure handle.",
		"dividend_ts": "Dividend yield term structure handle.",
		"s0": "Initial underlying quote handle.",
		"v0": "Initial variance.",
		"kappa": "Mean reversion speed.",
		"theta": "Long run variance.",
		"sigma": "Vol of vol.",
		"rho": "Correlation.",
		"discretization": "Discretization scheme.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlHestonProcess(
	risk_free_ts: ql.YieldTermStructureHandle,
	dividend_ts: ql.YieldTermStructureHandle,
	s0: qQuoteHandle,
	v0: float,
	kappa: float,
	theta: float,
	sigma: float,
	rho: float,
	discretization: qHestonProcessDiscretization = ql.HestonProcess.QuadraticExponentialMartingale,
	trigger=None,
) -> ql.HestonProcess:
	return ql.HestonProcess(risk_free_ts, dividend_ts, s0, v0, kappa, theta, sigma, rho, discretization)


@xlo.func(
	help="Return the state quote of a HestonProcess.",
	args={
		"process": "QuantLib HestonProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlHestonProcessS0(process: ql.HestonProcess, trigger=None) -> ql.QuoteHandle:
	return process.s0()


@xlo.func(
	help="Return the dividend yield of a HestonProcess.",
	args={
		"process": "QuantLib HestonProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlHestonProcessDividendYield(process: ql.HestonProcess, trigger=None) -> ql.YieldTermStructureHandle:
	return process.dividendYield()


@xlo.func(
	help="Return the risk-free rate of a HestonProcess.",
	args={
		"process": "QuantLib HestonProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlHestonProcessRiskFreeRate(process: ql.HestonProcess, trigger=None) -> ql.YieldTermStructureHandle:
	return process.riskFreeRate()


@xlo.func(
	help="Create a QuantLib BatesProcess object.",
	args={
		"risk_free_rate": "Risk-free yield term structure handle.",
		"dividend_yield": "Dividend yield term structure handle.",
		"s0": "Initial underlying quote handle.",
		"v0": "Initial variance.",
		"kappa": "Mean reversion speed.",
		"theta": "Long run variance.",
		"sigma": "Vol of vol.",
		"rho": "Correlation.",
		"lambda_parameter": "Jump intensity parameter.",
		"nu": "Mean jump size parameter.",
		"delta": "Jump volatility parameter.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlBatesProcess(
	risk_free_rate: ql.YieldTermStructureHandle,
	dividend_yield: ql.YieldTermStructureHandle,
	s0: qQuoteHandle,
	v0: float,
	kappa: float,
	theta: float,
	sigma: float,
	rho: float,
	lambda_parameter: float,
	nu: float,
	delta: float,
	trigger=None,
) -> ql.BatesProcess:
	return ql.BatesProcess(
		risk_free_rate,
		dividend_yield,
		s0,
		v0,
		kappa,
		theta,
		sigma,
		rho,
		lambda_parameter,
		nu,
		delta,
	)


@xlo.func(
	help="Create a QuantLib HullWhiteProcess object.",
	args={
		"risk_free_ts": "Risk-free yield term structure handle.",
		"a": "Mean reversion speed.",
		"sigma": "Volatility.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlHullWhiteProcess(
	risk_free_ts: ql.YieldTermStructureHandle,
	a: float,
	sigma: float,
	trigger=None,
) -> ql.HullWhiteProcess:
	return ql.HullWhiteProcess(risk_free_ts, a, sigma)


@xlo.func(
	help="Create a QuantLib HullWhiteForwardProcess object.",
	args={
		"risk_free_ts": "Risk-free yield term structure handle.",
		"a": "Mean reversion speed.",
		"sigma": "Volatility.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlHullWhiteForwardProcess(
	risk_free_ts: ql.YieldTermStructureHandle,
	a: float,
	sigma: float,
	trigger=None,
) -> ql.HullWhiteForwardProcess:
	return ql.HullWhiteForwardProcess(risk_free_ts, a, sigma)


@xlo.func(
	help="Return Hull-White alpha.",
	args={
		"process": "QuantLib HullWhiteForwardProcess.",
		"t": "Time.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlHullWhiteForwardProcessAlpha(process: ql.HullWhiteForwardProcess, t: float, trigger=None) -> float:
	return process.alpha(t)


@xlo.func(
	help="Return Hull-White M_T.",
	args={
		"process": "QuantLib HullWhiteForwardProcess.",
		"s": "Start time.",
		"t": "End time.",
		"t_measure": "Forward measure time.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlHullWhiteForwardProcessMT(process: ql.HullWhiteForwardProcess, s: float, t: float, t_measure: float, trigger=None) -> float:
	return process.M_T(s, t, t_measure)


@xlo.func(
	help="Return Hull-White B.",
	args={
		"process": "QuantLib HullWhiteForwardProcess.",
		"s": "Start time.",
		"t": "End time.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlHullWhiteForwardProcessB(process: ql.HullWhiteForwardProcess, s: float, t: float, trigger=None) -> float:
	return process.B(s, t)


@xlo.func(
	help="Set Hull-White forward measure time.",
	args={
		"process": "QuantLib HullWhiteForwardProcess.",
		"t": "Forward measure time.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlHullWhiteForwardProcessSetForwardMeasureTime(process: ql.HullWhiteForwardProcess, t: float, trigger=None) -> bool:
	process.setForwardMeasureTime(t)
	return True


@xlo.func(
	help="Create a QuantLib G2Process object.",
	args={
		"a": "Mean reversion speed.",
		"sigma": "Volatility.",
		"b": "Second mean reversion speed.",
		"eta": "Second volatility.",
		"rho": "Correlation.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlG2Process(
	a: float,
	sigma: float,
	b: float,
	eta: float,
	rho: float,
	trigger=None,
) -> ql.G2Process:
	return ql.G2Process(a, sigma, b, eta, rho)


@xlo.func(
	help="Create a QuantLib G2ForwardProcess object.",
	args={
		"a": "Mean reversion speed.",
		"sigma": "Volatility.",
		"b": "Second mean reversion speed.",
		"eta": "Second volatility.",
		"rho": "Correlation.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlG2ForwardProcess(
	a: float,
	sigma: float,
	b: float,
	eta: float,
	rho: float,
	trigger=None,
) -> ql.G2ForwardProcess:
	return ql.G2ForwardProcess(a, sigma, b, eta, rho)


@xlo.func(
	help="Set G2 forward measure time.",
	args={
		"process": "QuantLib G2ForwardProcess.",
		"t": "Forward measure time.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlG2ForwardProcessSetForwardMeasureTime(process: ql.G2ForwardProcess, t: float, trigger=None) -> bool:
	process.setForwardMeasureTime(t)
	return True


@xlo.func(
	help="Create a QuantLib GsrProcess object.",
	args={
		"times": "Switch times.",
		"vols": "Volatilities.",
		"reversions": "Mean reversions.",
		"t": "Horizon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGsrProcess(
	times: xlo.Array(dims=1),
	vols: xlo.Array(dims=1),
	reversions: xlo.Array(dims=1),
	t: float = 60.0,
	trigger=None,
) -> ql.GsrProcess:
    times_ = ql.Array(_to_float_list(times))
    vols_ = ql.Array(_to_float_list(vols))
    reversions_ = ql.Array(_to_float_list(reversions))
    return ql.GsrProcess(times_, vols_, reversions_, t)


@xlo.func(
	help="Return GSR sigma.",
	args={
		"process": "QuantLib GsrProcess.",
		"t": "Time.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGsrProcessSigma(process: ql.GsrProcess, t: float, trigger=None) -> float:
	raise NotImplementedError("qlGsrProcessSigma is currently broken.")
	# return process.sigma(t)


@xlo.func(
	help="Return GSR reversion.",
	args={
		"process": "QuantLib GsrProcess.",
		"t": "Time.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGsrProcessReversion(process: ql.GsrProcess, t: float, trigger=None) -> float:
	raise NotImplementedError("qlGsrProcessReversion is currently broken.")
	# return process.reversion(t)


@xlo.func(
	help="Return GSR y.",
	args={
		"process": "QuantLib GsrProcess.",
		"t": "Time.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGsrProcessY(process: ql.GsrProcess, t: float, trigger=None) -> float:
	raise NotImplementedError("qlGsrProcessY is currently broken.")
    # return process.y(t)


@xlo.func(
	help="Return GSR G.",
	args={
		"process": "QuantLib GsrProcess.",
		"t": "Start time.",
		"T": "End time.",
		"x": "State value.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGsrProcessG(process: ql.GsrProcess, t: float, T: float, x: float, trigger=None) -> float:
	raise NotImplementedError("qlGsrProcessG is currently broken.")
	# return process.G(t, T, x)


@xlo.func(
	help="Set GSR forward measure time.",
	args={
		"process": "QuantLib GsrProcess.",
		"t": "Forward measure time.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGsrProcessSetForwardMeasureTime(process: ql.GsrProcess, t: float, trigger=None) -> bool:
	raise NotImplementedError("qlGsrProcessSetForwardMeasureTime is currently broken.")
	# process.setForwardMeasureTime(t)
	# return True


@xlo.func(
	help="Create a QuantLib OrnsteinUhlenbeckProcess object.",
	args={
		"speed": "Mean reversion speed.",
		"vol": "Volatility.",
		"x0": "Initial value.",
		"level": "Long-run level.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOrnsteinUhlenbeckProcess(
	speed: float,
	vol: float,
	x0: float = 0.0,
	level: float = 0.0,
	trigger=None,
) -> ql.OrnsteinUhlenbeckProcess:
	return ql.OrnsteinUhlenbeckProcess(speed, vol, x0, level)


@xlo.func(
	help="Return Ornstein-Uhlenbeck speed.",
	args={
		"process": "QuantLib OrnsteinUhlenbeckProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOrnsteinUhlenbeckProcessSpeed(process: ql.OrnsteinUhlenbeckProcess, trigger=None) -> float:
	return process.speed()


@xlo.func(
	help="Return Ornstein-Uhlenbeck volatility.",
	args={
		"process": "QuantLib OrnsteinUhlenbeckProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOrnsteinUhlenbeckProcessVolatility(process: ql.OrnsteinUhlenbeckProcess, trigger=None) -> float:
	return process.volatility()


@xlo.func(
	help="Return Ornstein-Uhlenbeck level.",
	args={
		"process": "QuantLib OrnsteinUhlenbeckProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlOrnsteinUhlenbeckProcessLevel(process: ql.OrnsteinUhlenbeckProcess, trigger=None) -> float:
	return process.level()


@xlo.func(
	help="Create a QuantLib ExtendedOrnsteinUhlenbeckProcess object.",
	args={
		"speed": "Mean reversion speed.",
		"sigma": "Volatility.",
		"x0": "Initial value.",
		"function": "Function used in the process.",
		"int_eps": "Integration epsilon.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlExtendedOrnsteinUhlenbeckProcess(
	speed: float,
	sigma: float,
	x0: float,
	function,
	int_eps: float = 1.0e-4,
	trigger=None,
) -> ql.ExtendedOrnsteinUhlenbeckProcess:
	return ql.ExtendedOrnsteinUhlenbeckProcess(speed, sigma, x0, function, int_eps)


@xlo.func(
    help="Create a constant function for use in ExtendedOrnsteinUhlenbeckProcess.",
    args={
        "x": "Constant value.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExtendedOrnsteinUhlenbeckProcessConstantFunction(x: float):
    f = lambda t: x
    return f


@xlo.func(
	help="Create a QuantLib ExtOUWithJumpsProcess object.",
	args={
		"process": "Extended Ornstein-Uhlenbeck process.",
		"Y0": "Initial level.",
		"beta": "Beta parameter.",
		"jump_intensity": "Jump intensity.",
		"eta": "Jump size parameter.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlExtOUWithJumpsProcess(
	process: ql.ExtendedOrnsteinUhlenbeckProcess,
	Y0: float,
	beta: float,
	jump_intensity: float,
	eta: float,
	trigger=None,
) -> ql.ExtOUWithJumpsProcess:
	return ql.ExtOUWithJumpsProcess(process, Y0, beta, jump_intensity, eta)


@xlo.func(
	help="Create a QuantLib KlugeExtOUProcess object.",
	args={
		"rho": "Correlation parameter.",
		"kluge": "ExtOU-with-jumps process.",
		"ext_ou": "Extended Ornstein-Uhlenbeck process.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlKlugeExtOUProcess(
	rho: float,
	kluge: ql.ExtOUWithJumpsProcess,
	ext_ou: ql.ExtendedOrnsteinUhlenbeckProcess,
	trigger=None,
) -> ql.KlugeExtOUProcess:
	return ql.KlugeExtOUProcess(rho, kluge, ext_ou)


@xlo.func(
	help="Create a QuantLib GJRGARCHProcess object.",
	args={
		"risk_free_rate": "Risk-free yield term structure handle.",
		"dividend_yield": "Dividend yield term structure handle.",
		"s0": "Initial underlying quote handle.",
		"v0": "Initial variance.",
		"omega": "Omega parameter.",
		"alpha": "Alpha parameter.",
		"beta": "Beta parameter.",
		"gamma": "Gamma parameter.",
		"lambda_parameter": "Lambda parameter.",
		"days_per_year": "Days per year.",
		"discretization": "Discretization scheme.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGJRGARCHProcess(
	risk_free_rate: ql.YieldTermStructureHandle,
	dividend_yield: ql.YieldTermStructureHandle,
	s0: qQuoteHandle,
	v0: float,
	omega: float,
	alpha: float,
	beta: float,
	gamma: float,
	lambda_parameter: float,
	days_per_year: float = 252.0,
	discretization: qGJRGARCHProcessDiscretization = ql.GJRGARCHProcess.FullTruncation,
	trigger=None,
) -> ql.GJRGARCHProcess:
	return ql.GJRGARCHProcess(
		risk_free_rate,
		dividend_yield,
		s0,
		v0,
		omega,
		alpha,
		beta,
		gamma,
		lambda_parameter,
		days_per_year,
		discretization,
	)


@xlo.func(
	help="Return the state quote of a GJRGARCHProcess.",
	args={
		"process": "QuantLib GJRGARCHProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGJRGARCHProcessS0(process: ql.GJRGARCHProcess, trigger=None) -> ql.QuoteHandle:
	return process.s0()


@xlo.func(
	help="Return the dividend yield of a GJRGARCHProcess.",
	args={
		"process": "QuantLib GJRGARCHProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGJRGARCHProcessDividendYield(process: ql.GJRGARCHProcess, trigger=None) -> ql.YieldTermStructureHandle:
	return process.dividendYield()


@xlo.func(
	help="Return the risk-free rate of a GJRGARCHProcess.",
	args={
		"process": "QuantLib GJRGARCHProcess.",
	},
	group=EXCEL_GROUP_NAME,
)
def qlGJRGARCHProcessRiskFreeRate(process: ql.GJRGARCHProcess, trigger=None) -> ql.YieldTermStructureHandle:
	return process.riskFreeRate()
