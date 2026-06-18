import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import enum_value, first_key, UNKNOWN_KEY, UNKNOWN_VALUE

QL_CREDIT_DEFAULT_SWAP_PRICING_MODEL = {
    "MIDPOINT": ql.CreditDefaultSwap.Midpoint,
    "ISDA": ql.CreditDefaultSwap.ISDA,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qCreditDefaultSwapPricingModel(s: str) -> int:
    return enum_value(s, QL_CREDIT_DEFAULT_SWAP_PRICING_MODEL)


@xlo.converter()
def qCreditDefaultSwapPricingModel(s: str) -> int:
    return _qCreditDefaultSwapPricingModel(s)
