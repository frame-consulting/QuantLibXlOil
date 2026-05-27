import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME

QL_CURRENCIES = {
    'AED' : ql.AEDCurrency,
    'AOA' : ql.AOACurrency,
    'ARS' : ql.ARSCurrency,
    'ATS' : ql.ATSCurrency,
    'AUD' : ql.AUDCurrency,
    'BDT' : ql.BDTCurrency,
    'BEF' : ql.BEFCurrency,
    'BHD' : ql.BHDCurrency,
    'BGL' : ql.BGLCurrency,
    'BGN' : ql.BGNCurrency,
    'BRL' : ql.BRLCurrency,
    'BWP' : ql.BWPCurrency,
    'BYR' : ql.BYRCurrency,
    'CAD' : ql.CADCurrency,
    'CHF' : ql.CHFCurrency,
    'CLF' : ql.CLFCurrency,
    'CLP' : ql.CLPCurrency,
    'CNH' : ql.CNHCurrency,
    'CNY' : ql.CNYCurrency,
    'COP' : ql.COPCurrency,
    'COU' : ql.COUCurrency,
    'CYP' : ql.CYPCurrency,
    'CZK' : ql.CZKCurrency,
    'DEM' : ql.DEMCurrency,
    'DKK' : ql.DKKCurrency,
    'EEK' : ql.EEKCurrency,
    'EGP' : ql.EGPCurrency,
    'ESP' : ql.ESPCurrency,
    'ETB' : ql.ETBCurrency,
    'EUR' : ql.EURCurrency,
    'FIM' : ql.FIMCurrency,
    'FRF' : ql.FRFCurrency,
    'GEL' : ql.GELCurrency,
    'GBP' : ql.GBPCurrency,
    'GHS' : ql.GHSCurrency,
    'GRD' : ql.GRDCurrency,
    'HKD' : ql.HKDCurrency,
    'HRK' : ql.HRKCurrency,
    'HUF' : ql.HUFCurrency,
    'IDR' : ql.IDRCurrency,
    'IEP' : ql.IEPCurrency,
    'ILS' : ql.ILSCurrency,
    'INR' : ql.INRCurrency,
    'IQD' : ql.IQDCurrency,
    'IRR' : ql.IRRCurrency,
    'ISK' : ql.ISKCurrency,
    'ITL' : ql.ITLCurrency,
    'JOD' : ql.JODCurrency,
    'JPY' : ql.JPYCurrency,
    'KES' : ql.KESCurrency,
    'KRW' : ql.KRWCurrency,
    'KWD' : ql.KWDCurrency,
    'KZT' : ql.KZTCurrency,
    'LKR' : ql.LKRCurrency,
    'LTL' : ql.LTLCurrency,
    'LUF' : ql.LUFCurrency,
    'LVL' : ql.LVLCurrency,
    'MAD' : ql.MADCurrency,
    'MTL' : ql.MTLCurrency,
    'MUR' : ql.MURCurrency,
    'MXN' : ql.MXNCurrency,
    'MXV' : ql.MXVCurrency,
    'MYR' : ql.MYRCurrency,
    'NGN' : ql.NGNCurrency,
    'NLG' : ql.NLGCurrency,
    'NOK' : ql.NOKCurrency,
    'NPR' : ql.NPRCurrency,
    'NZD' : ql.NZDCurrency,
    'OMR' : ql.OMRCurrency,
    'PEH' : ql.PEHCurrency,
    'PEI' : ql.PEICurrency,
    'PEN' : ql.PENCurrency,
    'PHP' : ql.PHPCurrency,
    'PKR' : ql.PKRCurrency,
    'PLN' : ql.PLNCurrency,
    'PTE' : ql.PTECurrency,
    'QAR' : ql.QARCurrency,
    'ROL' : ql.ROLCurrency,
    'RON' : ql.RONCurrency,
    'RSD' : ql.RSDCurrency,
    'RUB' : ql.RUBCurrency,
    'SAR' : ql.SARCurrency,
    'SEK' : ql.SEKCurrency,
    'SGD' : ql.SGDCurrency,
    'SIT' : ql.SITCurrency,
    'SKK' : ql.SKKCurrency,
    'THB' : ql.THBCurrency,
    'TND' : ql.TNDCurrency,
    'TRL' : ql.TRLCurrency,
    'TRY' : ql.TRYCurrency,
    'TTD' : ql.TTDCurrency,
    'TWD' : ql.TWDCurrency,
    'UAH' : ql.UAHCurrency,
    'UGX' : ql.UGXCurrency,
    'USD' : ql.USDCurrency,
    'UYU' : ql.UYUCurrency,
    'VEB' : ql.VEBCurrency,
    'VND' : ql.VNDCurrency,
    'XOF' : ql.XOFCurrency,
    'ZAR' : ql.ZARCurrency,
    'ZMW' : ql.ZMWCurrency,
    # Cryptocurrencies
    'BCH' : ql.BCHCurrency,
    'BTC' : ql.BTCCurrency,
    'DASH' : ql.DASHCurrency,
    'ETC' : ql.ETCCurrency,
    'ETH' : ql.ETHCurrency,
    'LTC' : ql.LTCCurrency,
    'XRP' : ql.XRPCurrency,
    'ZEC' : ql.ZECCurrency,
}


def _qCurrency(code : str) -> ql.Currency:
    if isinstance(code, ql.Currency):  # capture default value
        return code
    code = code.strip().upper()
    if code in QL_CURRENCIES:
        return QL_CURRENCIES[code]()
    raise ValueError(f"Unknown currency code: {code}")


@xlo.converter()
def qCurrency(code : str) -> ql.Currency:
    return _qCurrency(code)


@xlo.func(
    help="Create a QuantLib Currency object.",
    args={
        "name" : "The name of the currency.",
        "code" : "The code of the currency.",
        "numerical_code" : "The numerical code of the currency.",
        "symbol" : "The symbol of the currency.",
        "fraction_symbol" : "The fraction symbol of the currency.",
        "fractions_per_unit" : "The number of fractions per unit of the currency.",
        "rounding" : "The rounding method to use for the currency.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCurrency(
    name : str,
    code : str,
    numerical_code : int,
    symbol : str,
    fraction_symbol : str,
    fractions_per_unit : int,
    rounding : ql.Rounding,
    trigger = None,
    ) -> ql.Currency:
    # Triangulation currency is not implemented yet.
    return ql.Currency(
        name,
        code,
        numerical_code,
        symbol,
        fraction_symbol,
        fractions_per_unit,
        rounding,
    )


@xlo.func(
    help="Get the name of a QuantLib Currency object.",
    args={
        "currency" : "The QuantLib Currency object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCurrencyName(currency : qCurrency, trigger = None) -> str:
    return currency.name()

@xlo.func(
    help="Get the code of a QuantLib Currency object.",
    args={
        "currency" : "The QuantLib Currency object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCurrencyCode(currency : qCurrency, trigger = None) -> str:
    return currency.code()

@xlo.func(
    help="Get the numerical code of a QuantLib Currency object.",
    args={
        "currency" : "The QuantLib Currency object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCurrencyNumericalCode(currency : qCurrency, trigger = None) -> int:
    return currency.numericCode()

@xlo.func(
    help="Get the symbol of a QuantLib Currency object.",
    args={
        "currency" : "The QuantLib Currency object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCurrencySymbol(currency : qCurrency, trigger = None) -> str:
    return currency.symbol()

@xlo.func(
    help="Get the fraction symbol of a QuantLib Currency object.",
    args={
        "currency" : "The QuantLib Currency object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCurrencyFractionSymbol(currency : qCurrency, trigger = None) -> str:
    return currency.fractionSymbol()

@xlo.func(
    help="Get the number of fractions per unit of a QuantLib Currency object.",
    args={
        "currency" : "The QuantLib Currency object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCurrencyFractionsPerUnit(currency : qCurrency, trigger = None) -> int:
    return currency.fractionsPerUnit()

@xlo.func(
    help="Get the rounding method of a QuantLib Currency object.",
    args={
        "currency" : "The QuantLib Currency object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCurrencyRounding(currency : qCurrency, trigger = None) -> ql.Rounding:
    return currency.rounding()

@xlo.func(
    help="Get the triangulation currency of a QuantLib Currency object.",
    args={
        "currency" : "The QuantLib Currency object to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCurrencyTriangulationCurrency(currency : qCurrency, trigger = None) -> ql.Currency:
    return currency.triangulationCurrency()