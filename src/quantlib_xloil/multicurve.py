import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME


# TODO: Move this to a separate file and combine with qlYieldTermStructureHandle from piecewiseyieldcurve.py
@xlo.func(
    help="Create an empty relinkable yield term structure handle.",
    group=EXCEL_GROUP_NAME,
)
def qlRelinkableYieldTermStructureHandle(
    trigger=None,
) -> ql.RelinkableYieldTermStructureHandle:
    return ql.RelinkableYieldTermStructureHandle()


@xlo.func(
    help="Create a QuantLib MultiCurve bootstrap.",
    args={"accuracy": "The accuracy used by the bootstrap."},
    group=EXCEL_GROUP_NAME,
)
def qlMultiCurve(accuracy: float, trigger=None) -> ql.MultiCurve:
    return ql.MultiCurve(accuracy)


@xlo.func(
    help="Add a bootstrapped curve to a MultiCurve bootstrap.",
    args={
        "multi_curve": "The MultiCurve bootstrap.",
        "internal_handle": "The relinkable handle used by the curve.",
        "curve": "The bootstrapped yield term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiCurveAddBootstrappedCurve(
    multi_curve: ql.MultiCurve,
    internal_handle: ql.RelinkableYieldTermStructureHandle,
    curve: ql.YieldTermStructureHandle,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    return multi_curve.addBootstrappedCurve(internal_handle, curve.currentLink())


@xlo.func(
    help="Add a non-bootstrapped curve to a MultiCurve bootstrap.",
    args={
        "multi_curve": "The MultiCurve bootstrap.",
        "internal_handle": "The relinkable handle used by the curve.",
        "curve": "The yield term structure.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMultiCurveAddNonBootstrappedCurve(
    multi_curve: ql.MultiCurve,
    internal_handle: ql.RelinkableYieldTermStructureHandle,
    curve: ql.YieldTermStructureHandle,
    trigger=None,
) -> ql.YieldTermStructureHandle:
    return multi_curve.addNonBootstrappedCurve(internal_handle, curve.currentLink())
