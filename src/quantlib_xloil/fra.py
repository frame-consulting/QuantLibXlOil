import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate
from .utilities import enum_value

QL_POSITION = {
    "LONG": ql.Position.Long,
    "SHORT": ql.Position.Short,
}


def _qPosition(position: str | int) -> int:
    return enum_value(position, QL_POSITION)


@xlo.converter()
def qPosition(position: str | int) -> int:
    return _qPosition(position)


@xlo.func(
    help="Create a QuantLib ForwardRateAgreement.",
    args={
        "index": "The Ibor index underlying the FRA.",
        "value_date": "The value date of the FRA.",
        "position": "The position ('Long' or 'Short').",
        "strike_forward_rate": "The FRA strike forward rate.",
        "notional": "The notional amount.",
        "discount_curve": "The optional discount curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlForwardRateAgreement(
    index: ql.IborIndex,
    value_date: qDate,
    position: qPosition,
    strike_forward_rate: float,
    notional: float,
    discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> ql.ForwardRateAgreement:
    return ql.ForwardRateAgreement(
        index, value_date, position, strike_forward_rate, notional, discount_curve
    )


@xlo.func(
    help="Create a QuantLib ForwardRateAgreement with an explicit maturity date.",
    args={
        "index": "The Ibor index underlying the FRA.",
        "value_date": "The value date of the FRA.",
        "maturity_date": "The maturity date of the FRA.",
        "position": "The position ('Long' or 'Short').",
        "strike_forward_rate": "The FRA strike forward rate.",
        "notional": "The notional amount.",
        "discount_curve": "The optional discount curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlForwardRateAgreement2(
    index: ql.IborIndex,
    value_date: qDate,
    maturity_date: qDate,
    position: qPosition,
    strike_forward_rate: float,
    notional: float,
    discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger=None,
) -> ql.ForwardRateAgreement:
    return ql.ForwardRateAgreement(
        index,
        value_date,
        maturity_date,
        position,
        strike_forward_rate,
        notional,
        discount_curve,
    )


@xlo.func(
    help="Return the amount of a QuantLib ForwardRateAgreement.",
    args={"fra": "The ForwardRateAgreement."},
    group=EXCEL_GROUP_NAME,
)
def qlForwardRateAgreementAmount(fra: ql.ForwardRateAgreement, trigger=None) -> float:
    return fra.amount()


@xlo.func(
    help="Return the fixing date of a QuantLib ForwardRateAgreement.",
    args={"fra": "The ForwardRateAgreement."},
    group=EXCEL_GROUP_NAME,
)
def qlForwardRateAgreementFixingDate(
    fra: ql.ForwardRateAgreement, trigger=None
) -> ql.Date:
    return fra.fixingDate()


@xlo.func(
    help="Return the forward rate of a QuantLib ForwardRateAgreement.",
    args={"fra": "The ForwardRateAgreement."},
    group=EXCEL_GROUP_NAME,
)
def qlForwardRateAgreementForwardRate(
    fra: ql.ForwardRateAgreement, trigger=None
) -> float:
    return fra.forwardRate().rate()
