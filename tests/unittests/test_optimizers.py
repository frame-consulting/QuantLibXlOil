import QuantLib as ql
import pytest

from quantlib_xloil.optimizers import (
    qEndCriteriaType,
    qResetScheme,
    qlBFGS,
    qlBisection,
    qlBrent,
    qlBoundaryConstraint,
    qlCompositeConstraint,
    qlConjugateGradient,
    qlDifferentialEvolution,
    qlEndCriteria,
    qlEndCriteriaSucceded,
    qlFalsePosition,
    qlGaussianSimulatedAnnealing,
    qlLBFGSB,
    qlLBFGSBBounded,
    qlLevenbergMarquardt,
    qlLogNormalSimulatedAnnealing,
    qlMirrorGaussianSimulatedAnnealing,
    qlNewton,
    qlNewtonSafe,
    qlNoConstraint,
    qlNonhomogeneousBoundaryConstraint,
    qlPositiveConstraint,
    qlProbabilityBoltzmannDownhill,
    qlReannealingTrivial,
    qlRidder,
    qlSamplerGaussian,
    qlSamplerLogNormal,
    qlSamplerMirrorGaussian,
    qlSecant,
    qlSimplex,
    qlSteepestDescent,
    qlTemperatureExponential,
)


def test_constraint_constructors_return_expected_types():
    no_constraint = qlNoConstraint()
    positive_constraint = qlPositiveConstraint()
    boundary_constraint = qlBoundaryConstraint(0.0, 2.0)
    composite_constraint = qlCompositeConstraint(
        positive_constraint, boundary_constraint
    )

    assert isinstance(no_constraint, ql.NoConstraint)
    assert isinstance(positive_constraint, ql.PositiveConstraint)
    assert isinstance(boundary_constraint, ql.BoundaryConstraint)
    assert isinstance(composite_constraint, ql.CompositeConstraint)


def test_lbfgsb_constructor_overloads():
    unbounded = qlLBFGSB()
    bounded = qlLBFGSBBounded([-1.0, 0.0], [1.0, 2.0])

    assert isinstance(unbounded, ql.LBFGSB)
    assert isinstance(bounded, ql.LBFGSB)


def test_qlNonhomogeneousBoundaryConstraint_converts_inputs_and_constructs():
    constraint = qlNonhomogeneousBoundaryConstraint(["0.0", 1], [1.5, "2.0"])

    assert isinstance(constraint, ql.NonhomogeneousBoundaryConstraint)


def test_qlNonhomogeneousBoundaryConstraint_size_mismatch_raises():
    with pytest.raises(RuntimeError, match="boundaries sizes are inconsistent"):
        qlNonhomogeneousBoundaryConstraint([0.0], [1.0, 2.0])


def test_qEndCriteriaType_case_insensitive_and_passthrough():
    assert (
        qEndCriteriaType.__wrapped__("max_iterations") == ql.EndCriteria.MaxIterations
    )
    assert (
        qEndCriteriaType.__wrapped__("ZERO_GRADIENT_NORM")
        == ql.EndCriteria.ZeroGradientNorm
    )
    assert (
        qEndCriteriaType.__wrapped__(ql.EndCriteria.Unknown) == ql.EndCriteria.Unknown
    )


def test_qEndCriteriaType_invalid_raises():
    with pytest.raises(ValueError, match="Cannot convert"):
        qEndCriteriaType.__wrapped__("bad-end-criteria")


def test_qlEndCriteria_constructor_and_succeeded_wrapper():
    end_criteria = qlEndCriteria(100, 10, 1.0e-8, 1.0e-8, 1.0e-8)

    assert isinstance(end_criteria, ql.EndCriteria)
    assert (
        qlEndCriteriaSucceded(
            end_criteria, qEndCriteriaType.__wrapped__("MAX_ITERATIONS")
        )
        is False
    )
    assert (
        qlEndCriteriaSucceded(end_criteria, qEndCriteriaType.__wrapped__("UNKNOWN"))
        is False
    )


# 1D Solvers Tests


def test_1d_solvers_constructors():
    brent = qlBrent()
    bisection = qlBisection()
    false_position = qlFalsePosition()
    ridder = qlRidder()
    secant = qlSecant()
    newton = qlNewton()
    newton_safe = qlNewtonSafe()

    assert isinstance(brent, ql.Brent)
    assert isinstance(bisection, ql.Bisection)
    assert isinstance(false_position, ql.FalsePosition)
    assert isinstance(ridder, ql.Ridder)
    assert isinstance(secant, ql.Secant)
    assert isinstance(newton, ql.Newton)
    assert isinstance(newton_safe, ql.NewtonSafe)


# Additional Optimization Methods Tests


def test_additional_optimization_methods_constructors():
    conjugate_gradient = qlConjugateGradient()
    simplex = qlSimplex()
    steepest_descent = qlSteepestDescent()
    bfgs = qlBFGS()
    differential_evolution = qlDifferentialEvolution()

    assert isinstance(conjugate_gradient, ql.ConjugateGradient)
    assert isinstance(simplex, ql.Simplex)
    assert isinstance(steepest_descent, ql.SteepestDescent)
    assert isinstance(bfgs, ql.BFGS)
    assert isinstance(differential_evolution, ql.DifferentialEvolution)


def test_qlSimplex_with_lambda():
    simplex = qlSimplex(lambda_=0.5)
    assert isinstance(simplex, ql.Simplex)


def test_qlLevenbergMarquardt_constructor():
    default_lm = qlLevenbergMarquardt()
    custom_lm = qlLevenbergMarquardt(
        epsfcn=1.0e-10,
        xtol=1.0e-10,
        gtol=1.0e-10,
        use_cost_functions_jacobian=True,
    )

    assert isinstance(default_lm, ql.LevenbergMarquardt)
    assert isinstance(custom_lm, ql.LevenbergMarquardt)


def test_qlLevenbergMarquardt_parameter_variations():
    lm_default = qlLevenbergMarquardt()
    lm_epsfcn = qlLevenbergMarquardt(epsfcn=1.0e-6)
    lm_xtol = qlLevenbergMarquardt(xtol=1.0e-6)
    lm_gtol = qlLevenbergMarquardt(gtol=1.0e-6)
    lm_jacobian = qlLevenbergMarquardt(use_cost_functions_jacobian=True)
    lm_all_custom = qlLevenbergMarquardt(
        epsfcn=1.0e-9,
        xtol=1.0e-9,
        gtol=1.0e-9,
        use_cost_functions_jacobian=False,
    )

    assert isinstance(lm_default, ql.LevenbergMarquardt)
    assert isinstance(lm_epsfcn, ql.LevenbergMarquardt)
    assert isinstance(lm_xtol, ql.LevenbergMarquardt)
    assert isinstance(lm_gtol, ql.LevenbergMarquardt)
    assert isinstance(lm_jacobian, ql.LevenbergMarquardt)
    assert isinstance(lm_all_custom, ql.LevenbergMarquardt)


# Simulated Annealing Helper Classes Tests


def test_sampler_constructors():
    sampler_gaussian = qlSamplerGaussian()
    sampler_gaussian_with_seed = qlSamplerGaussian(seed=42)
    sampler_log_normal = qlSamplerLogNormal()
    sampler_log_normal_with_seed = qlSamplerLogNormal(seed=42)

    assert isinstance(sampler_gaussian, ql.SamplerGaussian)
    assert isinstance(sampler_gaussian_with_seed, ql.SamplerGaussian)
    assert isinstance(sampler_log_normal, ql.SamplerLogNormal)
    assert isinstance(sampler_log_normal_with_seed, ql.SamplerLogNormal)


def test_qlSamplerMirrorGaussian_constructor():
    sampler = qlSamplerMirrorGaussian(
        lower=[0.0, -1.0],
        upper=[1.0, 2.0],
        seed=42,
    )
    assert isinstance(sampler, ql.SamplerMirrorGaussian)


def test_probability_and_temperature_constructors():
    probability = qlProbabilityBoltzmannDownhill()
    probability_with_seed = qlProbabilityBoltzmannDownhill(seed=42)
    temperature = qlTemperatureExponential(100.0, 5, 0.95)
    temperature_default_power = qlTemperatureExponential(100.0, 5)
    reannealing = qlReannealingTrivial()

    assert isinstance(probability, ql.ProbabilityBoltzmannDownhill)
    assert isinstance(probability_with_seed, ql.ProbabilityBoltzmannDownhill)
    assert isinstance(temperature, ql.TemperatureExponential)
    assert isinstance(temperature_default_power, ql.TemperatureExponential)
    assert isinstance(reannealing, ql.ReannealingTrivial)


# ResetScheme Enum Tests


def test_qResetScheme_case_insensitive_and_passthrough():
    assert (
        qResetScheme.__wrapped__("NO_RESET_SCHEME")
        == ql.GaussianSimulatedAnnealing.NoResetScheme
    )
    assert (
        qResetScheme.__wrapped__("reset_to_best_point")
        == ql.GaussianSimulatedAnnealing.ResetToBestPoint
    )
    assert (
        qResetScheme.__wrapped__("RESET_TO_ORIGIN")
        == ql.GaussianSimulatedAnnealing.ResetToOrigin
    )


def test_qResetScheme_invalid_raises():
    with pytest.raises(ValueError, match="Cannot convert"):
        qResetScheme.__wrapped__("bad-reset-scheme")


# Simulated Annealing Optimization Methods Tests


def test_simulated_annealing_methods_constructors():
    sampler = qlSamplerGaussian(seed=42)
    probability = qlProbabilityBoltzmannDownhill(seed=42)
    temperature = qlTemperatureExponential(100.0, 5, 0.95)
    reannealing = qlReannealingTrivial()

    gaussian_sa = qlGaussianSimulatedAnnealing(
        sampler=sampler,
        probability=probability,
        temperature=temperature,
        reannealing=reannealing,
        start_temperature=200.0,
        end_temperature=0.01,
        re_anneal_steps=50,
        reset_scheme=qResetScheme.__wrapped__("RESET_TO_BEST_POINT"),
        reset_steps=150,
    )

    mirror_gaussian_sa = qlMirrorGaussianSimulatedAnnealing(
        sampler=qlSamplerMirrorGaussian(lower=[0.0, -1.0], upper=[1.0, 2.0], seed=42),
        probability=probability,
        temperature=temperature,
        reannealing=reannealing,
        start_temperature=200.0,
        end_temperature=0.01,
        re_anneal_steps=50,
        reset_scheme=qResetScheme.__wrapped__("RESET_TO_ORIGIN"),
        reset_steps=150,
    )

    log_normal_sa = qlLogNormalSimulatedAnnealing(
        sampler=qlSamplerLogNormal(seed=42),
        probability=probability,
        temperature=temperature,
        reannealing=reannealing,
        start_temperature=10.0,
        end_temperature=0.01,
        re_anneal_steps=50,
        reset_scheme=qResetScheme.__wrapped__("NO_RESET_SCHEME"),
        reset_steps=150,
    )

    assert isinstance(gaussian_sa, ql.GaussianSimulatedAnnealing)
    assert isinstance(mirror_gaussian_sa, ql.MirrorGaussianSimulatedAnnealing)
    assert isinstance(log_normal_sa, ql.LogNormalSimulatedAnnealing)


def test_simulated_annealing_default_parameters():
    sampler = qlSamplerGaussian()
    probability = qlProbabilityBoltzmannDownhill()
    temperature = qlTemperatureExponential(100.0, 5)

    gaussian_sa = qlGaussianSimulatedAnnealing(
        sampler=sampler,
        probability=probability,
        temperature=temperature,
    )

    mirror_gaussian_sa = qlMirrorGaussianSimulatedAnnealing(
        sampler=qlSamplerMirrorGaussian(lower=[0.0], upper=[1.0]),
        probability=probability,
        temperature=temperature,
    )

    log_normal_sa = qlLogNormalSimulatedAnnealing(
        sampler=qlSamplerLogNormal(),
        probability=probability,
        temperature=temperature,
    )

    assert isinstance(gaussian_sa, ql.GaussianSimulatedAnnealing)
    assert isinstance(mirror_gaussian_sa, ql.MirrorGaussianSimulatedAnnealing)
    assert isinstance(log_normal_sa, ql.LogNormalSimulatedAnnealing)
