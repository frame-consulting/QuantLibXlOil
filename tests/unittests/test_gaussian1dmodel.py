import QuantLib as ql
import pytest

from quantlib_xloil.gaussian1dmodel import (
    _qGaussian1dProbabilities,
    qlGaussian1dCapFloorEngine,
    qlGaussian1dFloatFloatSwaptionEngine,
    qlGaussian1dJamshidianSwaptionEngine,
    qlGaussian1dModelForwardRate,
    qlGaussian1dModelNumeraire,
    qlGaussian1dModelNumeraireFromTime,
    qlGaussian1dModelStateProcess,
    qlGaussian1dModelSwapAnnuity,
    qlGaussian1dModelSwapRate,
    qlGaussian1dModelZerobond,
    qlGaussian1dModelZerobondFromTime,
    qlGaussian1dModelZerobondOption,
    qlGaussian1dNonstandardSwaptionEngine,
    qlGaussian1dSwaptionEngine,
    qlGsr,
    qlGsrReversion,
    qlGsrVolatility,
    qlMarkovFunctionalVolatility,
)


def _flat_curve(
    reference_date: ql.Date, rate: float = 0.02
) -> ql.YieldTermStructureHandle:
    return ql.YieldTermStructureHandle(
        ql.FlatForward(reference_date, rate, ql.Actual365Fixed())
    )


def _gsr_model() -> ql.Gsr:
    reference_date = ql.Date(2, 1, 2024)
    yts = _flat_curve(reference_date)
    step_dates = [ql.Date(2, 1, 2025).serialNumber()]
    volatilities = [0.01, 0.011]
    reversions = [0.03]
    return qlGsr(yts, step_dates, volatilities, reversions, 60.0)


def test_qGaussian1dProbabilities_converter_helper():
    assert _qGaussian1dProbabilities("none") == ql.Gaussian1dSwaptionEngine.NoProb
    assert _qGaussian1dProbabilities("Naive") == ql.Gaussian1dSwaptionEngine.Naive
    assert _qGaussian1dProbabilities("DIGITAL") == ql.Gaussian1dSwaptionEngine.Digital

    with pytest.raises(ValueError, match="Cannot convert"):
        _qGaussian1dProbabilities("invalid")


def test_gaussian1d_model_passthrough_wrappers_with_dummy_model():
    class DummyGaussian1dModel:
        def __init__(self):
            self.calls = []

        def stateProcess(self):
            self.calls.append(("stateProcess",))
            return "state-process"

        def numeraire(self, *args):
            self.calls.append(("numeraire", args))
            return 1.23

        def zerobond(self, *args):
            self.calls.append(("zerobond", args))
            return 0.95

        def zerobondOption(self, *args):
            self.calls.append(("zerobondOption", args))
            return 0.12

        def forwardRate(self, *args):
            self.calls.append(("forwardRate", args))
            return 0.031

        def swapRate(self, *args):
            self.calls.append(("swapRate", args))
            return 0.029

        def swapAnnuity(self, *args):
            self.calls.append(("swapAnnuity", args))
            return 4.2

    model = DummyGaussian1dModel()
    reference_date = ql.Date(2, 1, 2024)
    maturity = ql.Date(2, 1, 2027)
    expiry = ql.Date(2, 1, 2025)
    value_date = ql.Date(2, 7, 2025)
    fixing = ql.Date(2, 4, 2024)
    tenor = ql.Period("5Y")

    assert qlGaussian1dModelStateProcess(model) == "state-process"
    assert qlGaussian1dModelNumeraireFromTime(model, 1.0, 0.1) == 1.23
    assert qlGaussian1dModelNumeraire(model, reference_date, 0.2) == 1.23

    assert qlGaussian1dModelZerobondFromTime(model, 3.0, 1.0, -0.1) == 0.95
    assert qlGaussian1dModelZerobond(model, maturity, reference_date, 0.0) == 0.95

    assert (
        qlGaussian1dModelZerobondOption(
            model,
            "call",
            expiry,
            value_date,
            maturity,
            0.95,
            reference_date,
        )
        == 0.12
    )
    assert (
        qlGaussian1dModelZerobondOption(
            model,
            "put",
            expiry,
            value_date,
            maturity,
            0.95,
            reference_date,
        )
        == 0.12
    )

    assert qlGaussian1dModelForwardRate(model, fixing, reference_date, 0.0) == 0.031
    assert qlGaussian1dModelSwapRate(model, fixing, tenor, reference_date, 0.0) == 0.029
    assert (
        qlGaussian1dModelSwapAnnuity(model, fixing, tenor, reference_date, 0.0) == 4.2
    )

    call_args = model.calls[5][1]
    put_args = model.calls[6][1]
    assert call_args[0] == ql.Option.Call
    assert put_args[0] == ql.Option.Put

    forward_args = model.calls[7][1]
    swap_rate_args = model.calls[8][1]
    swap_annuity_args = model.calls[9][1]
    assert isinstance(forward_args[3], ql.IborIndex)
    assert isinstance(swap_rate_args[4], ql.SwapIndex)
    assert isinstance(swap_annuity_args[4], ql.SwapIndex)


def test_qlGsr_and_gaussian1d_engine_wrappers():
    model = _gsr_model()

    assert isinstance(model, ql.Gsr)
    assert qlGsrVolatility(model) == pytest.approx([0.01, 0.011])
    assert qlGsrReversion(model) == pytest.approx([0.03])

    reference_date = ql.Date(2, 1, 2024)
    maturity = ql.Date(2, 1, 2026)

    assert isinstance(qlGaussian1dModelStateProcess(model), ql.StochasticProcess1D)
    assert qlGaussian1dModelNumeraireFromTime(model, 1.0, 0.0) > 0.0
    assert qlGaussian1dModelNumeraire(model, reference_date, 0.0) > 0.0
    assert qlGaussian1dModelZerobondFromTime(model, 2.0, 1.0, 0.0) > 0.0
    assert qlGaussian1dModelZerobond(model, maturity, reference_date, 0.0) > 0.0

    assert isinstance(qlGaussian1dSwaptionEngine(model), ql.Gaussian1dSwaptionEngine)
    assert isinstance(
        qlGaussian1dNonstandardSwaptionEngine(model),
        ql.Gaussian1dNonstandardSwaptionEngine,
    )
    assert isinstance(
        qlGaussian1dFloatFloatSwaptionEngine(model),
        ql.Gaussian1dFloatFloatSwaptionEngine,
    )
    assert isinstance(
        qlGaussian1dJamshidianSwaptionEngine(model),
        ql.Gaussian1dJamshidianSwaptionEngine,
    )
    assert isinstance(qlGaussian1dCapFloorEngine(model), ql.Gaussian1dCapFloorEngine)


def test_qlMarkovFunctionalVolatility_wrapper_returns_list():
    class DummyMarkovFunctional:
        def volatility(self):
            return (0.01, 0.02, 0.03)

    assert qlMarkovFunctionalVolatility(DummyMarkovFunctional()) == [0.01, 0.02, 0.03]
