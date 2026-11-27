import QuantLib as ql
import xloil as xlo

from .cashflows import qDurationType
from .config import EXCEL_GROUP_NAME
from .date import qDate, qFrequency
from .daycounters import qDayCounter
from .termstructures import qCompounding


@xlo.func(
    help="Return the start date of a bond.",
    args={"bond": "Bond."},
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsStartDate(bond: ql.Bond, trigger=None) -> ql.Date:
    return ql.BondFunctions.startDate(bond)


@xlo.func(
    help="Check whether a bond is tradable at settlement.",
    args={
        "bond": "Bond.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsIsTradable(
    bond: ql.Bond, settlement_date: qDate = ql.Date(), trigger=None
) -> bool:
    return ql.BondFunctions.isTradable(bond, settlement_date)


@xlo.func(
    help="Return the previous bond cash-flow amount.",
    args={
        "bond": "Bond.",
        "ref_date": "Reference date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsPreviousCashFlowAmount(
    bond: ql.Bond, ref_date: qDate = ql.Date(), trigger=None
) -> float:
    return ql.BondFunctions.previousCashFlowAmount(bond, ref_date)


@xlo.func(
    help="Return the next bond cash-flow amount.",
    args={
        "bond": "Bond.",
        "ref_date": "Reference date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsNextCashFlowAmount(
    bond: ql.Bond, ref_date: qDate = ql.Date(), trigger=None
) -> float:
    return ql.BondFunctions.nextCashFlowAmount(bond, ref_date)


@xlo.func(
    help="Return the bond coupon accrual start date at settlement.",
    args={
        "bond": "Bond.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsAccrualStartDate(
    bond: ql.Bond, settlement_date: qDate = ql.Date(), trigger=None
) -> ql.Date:
    return ql.BondFunctions.accrualStartDate(bond, settlement_date)


@xlo.func(
    help="Return the bond coupon accrual end date at settlement.",
    args={
        "bond": "Bond.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsAccrualEndDate(
    bond: ql.Bond, settlement_date: qDate = ql.Date(), trigger=None
) -> ql.Date:
    return ql.BondFunctions.accrualEndDate(bond, settlement_date)


@xlo.func(
    help="Return the bond coupon accrual period at settlement.",
    args={
        "bond": "Bond.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsAccrualPeriod(
    bond: ql.Bond, settlement_date: qDate = ql.Date(), trigger=None
) -> float:
    return ql.BondFunctions.accrualPeriod(bond, settlement_date)


@xlo.func(
    help="Return the bond coupon accrual days at settlement.",
    args={
        "bond": "Bond.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsAccrualDays(
    bond: ql.Bond, settlement_date: qDate = ql.Date(), trigger=None
) -> int:
    return ql.BondFunctions.accrualDays(bond, settlement_date)


@xlo.func(
    help="Return the bond accrued period at settlement.",
    args={
        "bond": "Bond.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsAccruedPeriod(
    bond: ql.Bond, settlement_date: qDate = ql.Date(), trigger=None
) -> float:
    return ql.BondFunctions.accruedPeriod(bond, settlement_date)


@xlo.func(
    help="Return the bond accrued days at settlement.",
    args={
        "bond": "Bond.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsAccruedDays(
    bond: ql.Bond, settlement_date: qDate = ql.Date(), trigger=None
) -> int:
    return ql.BondFunctions.accruedDays(bond, settlement_date)


@xlo.func(
    help="Return the bond clean price from a discount curve.",
    args={
        "bond": "Bond.",
        "discount_curve": "Discount curve handle.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsCleanPriceFromCurve(
    bond: ql.Bond,
    discount_curve: ql.YieldTermStructureHandle,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.BondFunctions.cleanPrice(
        bond, discount_curve.currentLink(), settlement_date
    )


@xlo.func(
    help="Return the bond dirty price from a discount curve.",
    args={
        "bond": "Bond.",
        "discount_curve": "Discount curve handle.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsDirtyPriceFromCurve(
    bond: ql.Bond,
    discount_curve: ql.YieldTermStructureHandle,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.BondFunctions.dirtyPrice(
        bond, discount_curve.currentLink(), settlement_date
    )


@xlo.func(
    help="Return the bond coupon basis-point sensitivity from a discount curve.",
    args={
        "bond": "Bond.",
        "discount_curve": "Discount curve handle.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsBpsFromCurve(
    bond: ql.Bond,
    discount_curve: ql.YieldTermStructureHandle,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.BondFunctions.bps(bond, discount_curve.currentLink(), settlement_date)


@xlo.func(
    help="Return the bond ATM coupon rate from a discount curve and optional price.",
    args={
        "bond": "Bond.",
        "discount_curve": "Discount curve handle.",
        "settlement_date": "Settlement date; default is bond settlement.",
        "price": "Bond price; default is the curve-implied price.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsAtmRate(
    bond: ql.Bond,
    discount_curve: ql.YieldTermStructureHandle,
    settlement_date: qDate = ql.Date(),
    price: ql.BondPrice = None,
    trigger=None,
) -> float:
    if price is None:
        return ql.BondFunctions.atmRate(
            bond, discount_curve.currentLink(), settlement_date
        )
    return ql.BondFunctions.atmRate(
        bond, discount_curve.currentLink(), settlement_date, price
    )


@xlo.func(
    help="Return the bond coupon basis-point sensitivity from a yield.",
    args={
        "bond": "Bond.",
        "yield_rate": "Bond yield.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsBpsFromRate(
    bond: ql.Bond,
    yield_rate: float,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.BondFunctions.bps(
        bond, yield_rate, day_counter, compounding, frequency, settlement_date
    )


@xlo.func(
    help="Return the bond duration from a yield.",
    args={
        "bond": "Bond.",
        "yield_rate": "Bond yield.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "duration_type": "Duration type; default is modified.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsDuration(
    bond: ql.Bond,
    yield_rate: float,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    duration_type: qDurationType = ql.Duration.Modified,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.BondFunctions.duration(
        bond,
        yield_rate,
        day_counter,
        compounding,
        frequency,
        duration_type,
        settlement_date,
    )


@xlo.func(
    help="Return the bond convexity from a yield.",
    args={
        "bond": "Bond.",
        "yield_rate": "Bond yield.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsConvexity(
    bond: ql.Bond,
    yield_rate: float,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.BondFunctions.convexity(
        bond, yield_rate, day_counter, compounding, frequency, settlement_date
    )


@xlo.func(
    help="Return the bond price change for a one-basis-point yield change.",
    args={
        "bond": "Bond.",
        "yield_rate": "Bond yield.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsBasisPointValue(
    bond: ql.Bond,
    yield_rate: float,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.BondFunctions.basisPointValue(
        bond, yield_rate, day_counter, compounding, frequency, settlement_date
    )


@xlo.func(
    help="Return the bond yield change for a one-basis-point price change.",
    args={
        "bond": "Bond.",
        "yield_rate": "Bond yield.",
        "day_counter": "Day count convention.",
        "compounding": "Compounding convention.",
        "frequency": "Compounding frequency.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsYieldValueBasisPoint(
    bond: ql.Bond,
    yield_rate: float,
    day_counter: qDayCounter,
    compounding: qCompounding,
    frequency: qFrequency,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.BondFunctions.yieldValueBasisPoint(
        bond, yield_rate, day_counter, compounding, frequency, settlement_date
    )


@xlo.func(
    help="Return the bond clean price from a discount curve and z-spread.",
    args={
        "bond": "Bond.",
        "discount_curve": "Discount curve handle.",
        "z_spread": "Z-spread.",
        "compounding": "Spread compounding convention.",
        "frequency": "Spread compounding frequency.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsCleanPriceFromZSpread(
    bond: ql.Bond,
    discount_curve: ql.YieldTermStructureHandle,
    z_spread: float,
    compounding: qCompounding,
    frequency: qFrequency,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.BondFunctions.cleanPrice(
        bond,
        discount_curve.currentLink(),
        z_spread,
        compounding,
        frequency,
        settlement_date,
    )


@xlo.func(
    help="Return the bond dirty price from a discount curve and z-spread.",
    args={
        "bond": "Bond.",
        "discount_curve": "Discount curve handle.",
        "z_spread": "Z-spread.",
        "compounding": "Spread compounding convention.",
        "frequency": "Spread compounding frequency.",
        "settlement_date": "Settlement date; default is bond settlement.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsDirtyPriceFromZSpread(
    bond: ql.Bond,
    discount_curve: ql.YieldTermStructureHandle,
    z_spread: float,
    compounding: qCompounding,
    frequency: qFrequency,
    settlement_date: qDate = ql.Date(),
    trigger=None,
) -> float:
    return ql.BondFunctions.dirtyPrice(
        bond,
        discount_curve.currentLink(),
        z_spread,
        compounding,
        frequency,
        settlement_date,
    )


@xlo.func(
    help="Return the bond z-spread implied by a price and discount curve.",
    args={
        "bond": "Bond.",
        "price": "Bond price.",
        "discount_curve": "Discount curve handle.",
        "compounding": "Spread compounding convention.",
        "frequency": "Spread compounding frequency.",
        "settlement_date": "Settlement date; default is bond settlement.",
        "accuracy": "Solver accuracy.",
        "max_iterations": "Maximum solver iterations.",
        "guess": "Initial spread guess.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBondFunctionsZSpread(
    bond: ql.Bond,
    price: ql.BondPrice,
    discount_curve: ql.YieldTermStructureHandle,
    compounding: qCompounding,
    frequency: qFrequency,
    settlement_date: qDate = ql.Date(),
    accuracy: float = 1.0e-10,
    max_iterations: int = 100,
    guess: float = 0.0,
    trigger=None,
) -> float:
    return ql.BondFunctions.zSpread(
        bond,
        price,
        discount_curve.currentLink(),
        compounding,
        frequency,
        settlement_date,
        accuracy,
        max_iterations,
        guess,
    )
