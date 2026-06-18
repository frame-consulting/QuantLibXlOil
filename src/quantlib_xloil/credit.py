import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import enum_value, first_key, UNKNOWN_KEY, UNKNOWN_VALUE

QL_PROTECTION_SIDE = {
    "BUY": ql.Protection.Buyer,
    "BUYER": ql.Protection.Buyer,
    "SELL": ql.Protection.Seller,
    "SELLER": ql.Protection.Seller,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qlProtectionSide(s: str) -> int:
    return enum_value(s, QL_PROTECTION_SIDE)


@xlo.converter()
def qlProtectionSide(s: str) -> int:
    return _qlProtectionSide(s)
