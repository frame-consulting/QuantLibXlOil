import xloil as xlo

from ..__about__ import __version__
from ..config import EXCEL_GROUP_NAME


@xlo.func(
    help="Get the version of the QuantLibXlOil.",
    group=EXCEL_GROUP_NAME,
)
def qlXlOilVersion(trigger=None) -> str:
    return __version__
