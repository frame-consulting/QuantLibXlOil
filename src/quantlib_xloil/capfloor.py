import QuantLib as ql
import xloil as xlo

from .calendars import qBusinessDayConvention, qCalendar
from .config import EXCEL_GROUP_NAME
from .date import qDate, qPeriod
from .daycounters import qDayCounter
from .ratehelpers import qQuoteHandle
from .scheduler import qDateGenerationRule
from .utilities import enum_value, first_key
from .volatilities import qVolatilityType

QL_CAPFLOOR_TYPE = {
    "CAP": 0,
    "FLOOR": 1,
    "COLLAR": 2,
}


def _qCapFloorType(type: str):
    return enum_value(type, QL_CAPFLOOR_TYPE)


@xlo.converter()
def qCapFloorType(type: str):
    return _qCapFloorType(type)


@xlo.func(
    help="Calculate the implied volatility of a cap/floor given its price.",
    args={
        "capfloor": "QuantLib CapFloor object",
        "price": "Market price of the cap/floor",
        "disc": "QuantLib YieldTermStructureHandle for discounting",
        "guess": "Initial guess for the implied volatility",
        "accuracy": "Desired accuracy for the implied volatility calculation (default: 1.0e-4)",
        "max_evaluations": "Maximum number of evaluations for the implied volatility calculation (default: 100)",
        "min_vol": "Minimum volatility for the implied volatility calculation (default: 1.0e-7)",
        "max_vol": "Maximum volatility for the implied volatility calculation (default: 4.0)",
        "type": "Volatility type (default: ShiftedLognormal)",
        "displacement": "Displacement for the shifted lognormal volatility (default: 0.0)",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCapFloorImpliedVolatility(
    capfloor: ql.CapFloor,
    price: float,
    disc: ql.YieldTermStructureHandle,
    guess: float,
    accuracy: float = 1.0e-4,
    max_evaluations: int = 100,
    min_vol: float = 1.0e-7,
    max_vol: float = 4.0,
    type: qVolatilityType = ql.ShiftedLognormal,
    displacement: float = 0.0,
    trigger=None,
) -> float:
    return capfloor.impliedVolatility(
        price,
        disc,
        guess,
        accuracy,
        max_evaluations,
        min_vol,
        max_vol,
        type,
        displacement,
    )


@xlo.func(
    help="Get the floating leg of a cap/floor.",
    args={
        "capfloor": "QuantLib CapFloor object",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCapFloorFloatingLeg(capfloor: ql.CapFloor, trigger=None) -> ql.FloatingRateCoupon:
    return capfloor.floatingLeg()


@xlo.func(
    help="Get the cap rates of a cap/floor.",
    args={
        "capfloor": "QuantLib CapFloor object",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCapFloorCapRates(capfloor: ql.CapFloor, trigger=None) -> list:
    return capfloor.capRates()


@xlo.func(
    help="Get the floor rates of a cap/floor.",
    args={
        "capfloor": "QuantLib CapFloor object",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCapFloorFloorRates(capfloor: ql.CapFloor, trigger=None) -> list:
    return capfloor.floorRates()


@xlo.func(
    help="Get the start date of a cap/floor.",
    args={
        "capfloor": "QuantLib CapFloor object",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCapFloorStartDate(capfloor: ql.CapFloor, trigger=None) -> ql.Date:
    return capfloor.startDate()


@xlo.func(
    help="Get the maturity date of a cap/floor.",
    args={
        "capfloor": "QuantLib CapFloor object",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCapFloorMaturityDate(capfloor: ql.CapFloor, trigger=None) -> ql.Date:
    return capfloor.maturityDate()


@xlo.func(
    help="Get the type of a cap/floor.",
    args={
        "capfloor": "QuantLib CapFloor object",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCapFloorType(capfloor: ql.CapFloor, trigger=None) -> str:
    capfloor_type = capfloor.type()
    return first_key(QL_CAPFLOOR_TYPE, capfloor_type)


# TODO swig does not support the use of YieldtermstructureHandle in the atmRate function
@xlo.func(
    help="Get the at-the-money rate of a cap/floor.",
    args={
        "capfloor": "QuantLib CapFloor object",
        "discount_curve": "QuantLib YieldTermStructureHandle for discounting",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCapFloorAtmRate(
    capfloor: ql.CapFloor, discount_curve: ql.YieldTermStructureHandle, trigger=None
) -> float:
    return capfloor.atmRate(discount_curve.currentLink())


@xlo.func(
    help="Create a cap object.",
    args={
        "leg": "List of cash flows",
        "cap_rates": "List of cap rates",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCapFloorCap(
    leg: xlo.Array(dims=1), cap_rates: xlo.Array(dims=1), trigger=None
) -> ql.Cap:
    return ql.Cap(leg, cap_rates)


@xlo.func(
    help="Create a floor object.",
    args={
        "leg": "List of cash flows",
        "floor_rates": "List of floor rates",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCapFloorFloor(
    leg: xlo.Array(dims=1), floor_rates: xlo.Array(dims=1), trigger=None
) -> ql.Floor:
    return ql.Floor(leg, floor_rates)


@xlo.func(
    help="Create a collar object.",
    args={
        "leg": "List of cash flows",
        "cap_rates": "List of cap rates",
        "floor_rates": "List of floor rates",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCapFloorCollar(
    leg: xlo.Array(dims=1),
    cap_rates: xlo.Array(dims=1),
    floor_rates: xlo.Array(dims=1),
    trigger=None,
) -> ql.Collar:
    return ql.Collar(leg, cap_rates, floor_rates)


@xlo.func(
    help="Create a Black cap/floor engine.",
    args={
        "term_structure": "QuantLib YieldTermStructureHandle for discounting",
        "vol": "Volatility of the cap/floor (float)",
        "day_counter": "QuantLib DayCounter for the volatility (default: Actual/365 Fixed)",
        "displacement": "Displacement for the shifted lognormal volatility (default: 0.0)",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCapFloorEngine(
    term_structure: ql.YieldTermStructureHandle,
    vol: qQuoteHandle,
    day_counter: ql.DayCounter = ql.Actual365Fixed(),
    displacement: float = 0.0,
    trigger=None,
) -> ql.BlackCapFloorEngine:
    return ql.BlackCapFloorEngine(term_structure, vol, day_counter, displacement)


@xlo.func(
    help="Create a Black cap/floor engine with default day counter.",
    args={
        "term_structure": "QuantLib YieldTermStructureHandle for discounting",
        "vol": "Volatility of the cap/floor (ql.OptionletVolatilityStructureHandle)",
        "displacement": "Displacement for the shifted lognormal volatility",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBlackCapFloorEngine2(
    term_structure: ql.YieldTermStructureHandle,
    vol: ql.OptionletVolatilityStructureHandle,
    displacement: float = ql.nullDouble(),
) -> ql.BlackCapFloorEngine:
    return ql.BlackCapFloorEngine(term_structure, vol, displacement)


@xlo.func(
    help="Create a Bachelier cap/floor engine.",
    args={
        "term_structure": "QuantLib YieldTermStructureHandle for discounting",
        "vol": "Volatility of the cap/floor (float)",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCapFloorEngine(
    term_structure: ql.YieldTermStructureHandle,
    vol: qQuoteHandle,
    trigger=None,
) -> ql.BachelierCapFloorEngine:
    return ql.BachelierCapFloorEngine(term_structure, vol)


@xlo.func(
    help="Create a Bachelier cap/floor engine with default day counter.",
    args={
        "term_structure": "QuantLib YieldTermStructureHandle for discounting",
        "vol": "Volatility of the cap/floor (ql.OptionletVolatilityStructureHandle)",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBachelierCapFloorEngine2(
    term_structure: ql.YieldTermStructureHandle,
    vol: ql.OptionletVolatilityStructureHandle,
    trigger=None,
) -> ql.BachelierCapFloorEngine:
    return ql.BachelierCapFloorEngine(term_structure, vol)


# TODO Passing the `effective_date` parameter with bool 'firstCapletExcluded`
@xlo.func(
    help="Create a QuantLib CapFloor object using the MakeCapFloor helper.",
    args={
        "type": "The cap/floor type (Cap, Floor, Collar).",
        "cap_floor_tenor": "The tenor of the cap/floor.",
        "ibor_index": "The Ibor index used to build the cap/floor.",
        "strike": "The strike rate (default: None).",
        "forward_start": "The forward start period (default: 0 Days).",
        "nominal": "The nominal amount (default: None).",
        "effective_date": "The effective date (default: None).",
        "calendar": "The calendar (default: None).",
        "convention": "The business day convention (default: None).",
        "termination_date_convention": "The termination date convention (default: None).",
        "rule": "The date generation rule (default: None).",
        "end_of_month": "Whether to use end-of-month adjustment (default: None).",
        "first_date": "The first date (default: None).",
        "next_to_last_date": "The next-to-last date (default: None).",
        "day_count": "The day counter (default: None).",
        "as_optionlet": "Whether to build as optionlets (default: None).",
        "pricing_engine": "The pricing engine (default: None).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMakeCapFloor(
    type: str | qCapFloorType,
    cap_floor_tenor: qPeriod,
    ibor_index: ql.IborIndex,
    strike=None,
    forward_start: qPeriod = ql.Period(0, ql.Days),
    nominal=None,
    effective_date=None,
    calendar=None,
    convention=None,
    termination_date_convention=None,
    rule=None,
    end_of_month=None,
    first_date=None,
    next_to_last_date=None,
    day_count=None,
    as_optionlet=None,
    pricing_engine=None,
    trigger=None,
) -> ql.CapFloor:
    cap_floor_type = _qCapFloorType(type)

    if cap_floor_tenor is not None:
        cap_floor_tenor = qPeriod.__wrapped__(cap_floor_tenor)
    if forward_start is not None:
        forward_start = qPeriod.__wrapped__(forward_start)
    if strike is not None:
        strike = float(strike)
    if nominal is not None:
        nominal = float(nominal)
    if effective_date is not None:
        effective_date = qDate.__wrapped__(effective_date)
    first_caplet_excluded = False
    if calendar is not None:
        calendar = qCalendar.__wrapped__(calendar)
    if convention is not None:
        convention = qBusinessDayConvention.__wrapped__(convention)
    if termination_date_convention is not None:
        termination_date_convention = qBusinessDayConvention.__wrapped__(
            termination_date_convention
        )
    if rule is not None:
        rule = qDateGenerationRule.__wrapped__(rule)
    if end_of_month is not None:
        end_of_month = bool(end_of_month)
    if first_date is not None:
        first_date = qDate.__wrapped__(first_date)
    if next_to_last_date is not None:
        next_to_last_date = qDate.__wrapped__(next_to_last_date)
    if day_count is not None:
        day_count = qDayCounter.__wrapped__(day_count)
    if as_optionlet is not None:
        as_optionlet = bool(as_optionlet)

    _MAKECAPFLOOR_KWARGS = {
        "nominal": "nominal",
        "calendar": "calendar",
        "convention": "convention",
        "termination_date_convention": "terminationDateConvention",
        "rule": "rule",
        "end_of_month": "endOfMonth",
        "first_date": "firstDate",
        "next_to_last_date": "nextToLastDate",
        "day_count": "dayCount",
        "as_optionlet": "asOptionlet",
        "pricing_engine": "pricingEngine",
    }

    kwargs = {}
    for param_name, kw_name in _MAKECAPFLOOR_KWARGS.items():
        value = locals()[param_name]
        if value is not None:
            kwargs[kw_name] = value

    return ql.MakeCapFloor(
        cap_floor_type,
        cap_floor_tenor,
        ibor_index,
        strike,
        forward_start,
        **kwargs,
    )
