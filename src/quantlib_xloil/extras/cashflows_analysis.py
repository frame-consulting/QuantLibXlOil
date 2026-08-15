import QuantLib as ql
import xloil as xlo

from ..utilities import (
    first_key,
    to_object_list,
    UNKNOWN_KEY,
)

from ..calendars import QL_BUSINESSDAYCONVENTION
from ..cashflows import QL_RATE_AVERAGING_TYPE

_EXCEL_GROUP_NAME = "QuantLibXlOil - CashFlows Analysis"


def __fixingConvention(cf):
    c = ql.as_floating_rate_coupon(cf).fixingConvention()
    return first_key(QL_BUSINESSDAYCONVENTION, c, UNKNOWN_KEY)


def __convexityAdjustment(cf):
    return ql.as_floating_rate_coupon(cf).convexityAdjustment()


def __averagingMethod(cf):
    cp = ql.as_capped_floored_overnight_indexed_coupon(cf)
    if cp is not None:
        value = cp.underlying().averagingMethod()
    else:
        value = ql.as_overnight_indexed_coupon(cf).averagingMethod()
    return first_key(QL_RATE_AVERAGING_TYPE, value, UNKNOWN_KEY)


def __canApplyTelescopicFormula(cf):
    cp = ql.as_capped_floored_overnight_indexed_coupon(cf)
    if cp is not None:
        value = cp.underlying().canApplyTelescopicFormula()
    else:
        value = ql.as_overnight_indexed_coupon(cf).canApplyTelescopicFormula()
    return value


def __applyObservationShift(cf):
    cp = ql.as_capped_floored_overnight_indexed_coupon(cf)
    if cp is not None:
        value = cp.underlying().applyObservationShift()
    else:
        value = ql.as_overnight_indexed_coupon(cf).applyObservationShift()
    return value


def __compoundSpreadDaily(cf):
    cp = ql.as_capped_floored_overnight_indexed_coupon(cf)
    if cp is not None:
        value = cp.underlying().compoundSpreadDaily()
    else:
        value = ql.as_overnight_indexed_coupon(cf).compoundSpreadDaily()
    return value


def __lockoutDays(cf):
    cp = ql.as_capped_floored_overnight_indexed_coupon(cf)
    if cp is not None:
        value = cp.underlying().lockoutDays()
    else:
        value = ql.as_overnight_indexed_coupon(cf).lockoutDays()
    return value


def __rateComputationStartDate(cf):
    cp = ql.as_capped_floored_overnight_indexed_coupon(cf)
    if cp is not None:
        value = cp.underlying().rateComputationStartDate()
    else:
        value = ql.as_overnight_indexed_coupon(cf).rateComputationStartDate()
    return value


def __rateComputationEndDate(cf):
    cp = ql.as_capped_floored_overnight_indexed_coupon(cf)
    if cp is not None:
        value = cp.underlying().rateComputationEndDate()
    else:
        value = ql.as_overnight_indexed_coupon(cf).rateComputationEndDate()
    return value


def __effectiveIndexFixing(cf):
    cp = ql.as_capped_floored_overnight_indexed_coupon(cf)
    if cp is not None:
        value = cp.underlying().effectiveIndexFixing()
    else:
        value = ql.as_overnight_indexed_coupon(cf).effectiveIndexFixing()
    return value


def __effectiveSpread(cf):
    cp = ql.as_capped_floored_overnight_indexed_coupon(cf)
    if cp is not None:
        value = cp.underlying().effectiveSpread()
    else:
        value = ql.as_overnight_indexed_coupon(cf).effectiveSpread()
    return value


def __nakedOption(cf):
    return ql.as_capped_floored_overnight_indexed_coupon(cf).nakedOption()


def __dailyCapFloor(cf):
    return ql.as_capped_floored_overnight_indexed_coupon(cf).dailyCapFloor()


def __effectiveCapletVolatility(cf):
    return ql.as_capped_floored_overnight_indexed_coupon(cf).effectiveCapletVolatility()


def __effectiveFloorletVolatility(cf):
    return ql.as_capped_floored_overnight_indexed_coupon(
        cf
    ).effectiveFloorletVolatility()


QL_CASH_FLOW_COLUMN = {
    # Cash flow interface attributes
    "AMOUNT": lambda cf, _: cf.amount(),
    "DATE": lambda cf, _: cf.date(),
    # Coupon-specific attributes
    "NOMINAL": lambda cf, _: ql.as_coupon(cf).nominal(),
    "ACCRUALSTARTDATE": lambda cf, _: ql.as_coupon(cf).accrualStartDate(),
    "ACCRUALENDDATE": lambda cf, _: ql.as_coupon(cf).accrualEndDate(),
    "REFERENCEPERIODSTART": lambda cf, _: ql.as_coupon(cf).referencePeriodStart(),
    "REFERENCEPERIODEND": lambda cf, _: ql.as_coupon(cf).referencePeriodEnd(),
    "EXCOUPONDATE": lambda cf, _: ql.as_coupon(cf).exCouponDate(),
    "RATE": lambda cf, _: ql.as_coupon(cf).rate(),
    "ACCRUALPERIOD": lambda cf, _: ql.as_coupon(cf).accrualPeriod(),
    "ACCRUALDAYS": lambda cf, _: ql.as_coupon(cf).accrualDays(),
    "DAYCOUNTER": lambda cf, _: ql.as_coupon(cf).dayCounter().name(),
    "ACCRUEDAMOUNT": lambda cf, _: ql.as_coupon(cf).accruedAmount(),
    # floating-rate coupon-specific attributes
    "FIXINGDATE": lambda cf, _: ql.as_floating_rate_coupon(cf).fixingDate(),
    "FIXINGDAYS": lambda cf, _: ql.as_floating_rate_coupon(cf).fixingDays(),
    "FIXINGCONVENTION": lambda cf, _: __fixingConvention(cf),
    "ISINARREARS": lambda cf, _: ql.as_floating_rate_coupon(cf).isInArrears(),
    "GEARING": lambda cf, _: ql.as_floating_rate_coupon(cf).gearing(),
    "SPREAD": lambda cf, _: ql.as_floating_rate_coupon(cf).spread(),
    "INDEXFIXING": lambda cf, _: ql.as_floating_rate_coupon(cf).indexFixing(),
    "ADJUSTEDFIXING": lambda cf, _: ql.as_floating_rate_coupon(cf).adjustedFixing(),
    "CONVEXITYADJUTMENT": lambda cf, _: __convexityAdjustment(cf),
    "INDEX": lambda cf, _: ql.as_floating_rate_coupon(cf).index().name(),
    # capped/floored coupon-specific attributes, incl. capped/floored OIS
    "ISCAPPED": lambda cf, _: cf.isCapped(),
    "ISFLOORED": lambda cf, _: cf.isFloored(),
    "CAP": lambda cf, _: cf.cap(),
    "FLOOR": lambda cf, _: cf.floor(),
    "EFFECTIVECAP": lambda cf, _: cf.effectiveCap(),
    "EFFECTIVEFLOOR": lambda cf, _: cf.effectiveFloor(),
    # Overnight-indexed coupon-specific attributes
    "AVERAGINGMETHOD": lambda cf, _: __averagingMethod(cf),
    "CANAPPLYTELESCOPICFORMULA": lambda cf, _: __canApplyTelescopicFormula(cf),
    "APPLYOBSERVATIONSHIFT": lambda cf, _: __applyObservationShift(cf),
    "COMPOUNDSPREADDAILY": lambda cf, _: __compoundSpreadDaily(cf),
    "LOCKOUTDAYS": lambda cf, _: __lockoutDays(cf),
    "RATECOMPUTATIONSTARTDATE": lambda cf, _: __rateComputationStartDate(cf),
    "RATECOMPUTATIONENDDATE": lambda cf, _: __rateComputationEndDate(cf),
    "EFFECTIVEINDEXFIXING": lambda cf, _: __effectiveIndexFixing(cf),
    "EFFECTIVESPREAD": lambda cf, _: __effectiveSpread(cf),
    # Capped/floored overnight-indexed coupon-specific attributes
    "NAKEDOPTION": lambda cf, _: __nakedOption(cf),
    "DAILYCAPFLOOR": lambda cf, _: __dailyCapFloor(cf),
    "EFFECTIVECAPLETVOLATILITY": lambda cf, _: __effectiveCapletVolatility(cf),
    "EFFECTIVEFLOORLETVOLATILITY": lambda cf, _: __effectiveFloorletVolatility(cf),
    # Discounted cash flow value
    "DISCOUNTFACTOR": lambda cf, ts: ts.discount(cf.date()),
    "NPV": lambda cf, ts: cf.amount() * ts.discount(cf.date()),
}


def _table(dict_list: list[dict], with_header):
    if len(dict_list) == 0:
        raise ValueError("Empty list provided.")
    d0 = dict_list[0]
    if not isinstance(d0, dict):
        raise TypeError(f"Element {d0} must be a dictionary.")
    header = [key for key in d0]
    table = [header] if with_header else []
    for d in dict_list:
        if not isinstance(d, dict):
            raise TypeError(f"Element {d} must be a dictionary.")
        values = [d[key] for key in d]
        table.append(values)
    return table


def _cashflow_analysis(
    cash_flows: list[ql.CashFlow],
    columns: list[str],
    discount_curve: ql.YieldTermStructureHandle = None,
):
    for c in columns:
        if not c in QL_CASH_FLOW_COLUMN:
            raise ValueError(f"Invalid column: {c}")

    def cf_value(cf, c):
        try:
            return QL_CASH_FLOW_COLUMN[c](cf, discount_curve)
        except Exception as e:
            return None

    res = []
    for cf in cash_flows:
        d = {c: cf_value(cf, c) for c in columns}
        res.append(d)
    return res


@xlo.func(
    help="Returns a list of available cash flow analysis columns.",
    group=_EXCEL_GROUP_NAME,
)
def qlCashFlowsAnalysisColumns():
    return list(QL_CASH_FLOW_COLUMN.keys())


@xlo.func(
    help="Returns a table with cash flow details for a leg.",
    args={
        "leg": "Cash-flow leg.",
        "columns": "List of column names to include.",
        "discount_curve": "Discount curve for discounted cash flow values.",
    },
    group=_EXCEL_GROUP_NAME,
)
def qlCashFlowsAnalysis(
    leg: xlo.Array(dims=1),
    columns: xlo.Array(dims=1),
    discount_curve: ql.YieldTermStructureHandle = None,
    with_header: bool = True,
    trigger=None,
):
    leg = to_object_list(leg, ql.CashFlow)
    columns = [str(c).upper() for c in columns]
    dict_list = _cashflow_analysis(leg, columns, discount_curve)
    table = _table(dict_list, with_header)
    return table
