import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .currencies import qCurrency
from .date import _qDate, qDate, qFrequency, qPeriod
from .calendars import qBusinessDayConvention, qCalendar
from .daycounters import qDayCounter

## IndexManager

@xlo.func(
    help="Get the histories of all indices in the IndexManager.",
    group=EXCEL_GROUP_NAME,
)
def qlIndexManagerHistories(Trigger = None):
    return ql.IndexManager.instance().histories()

@xlo.func(
    help="Clear the histories of all indices in the IndexManager.",
    group=EXCEL_GROUP_NAME,
)
def qlIndexManagerClearHistories(Trigger = None):
    ql.IndexManager.instance().clearHistories()
    return True

## Index interface

@xlo.func(
    help="Get the name of an index.",
    args={
        "Index" : "The index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexName(index : ql.Index, Trigger = None) -> str:
    return index.name()


@xlo.func(
    help="Get the fixing calendar of an index.",
    args={
        "Index" : "The index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexFixingCalendar(index : ql.Index, Trigger = None) -> ql.Calendar:
    return index.fixingCalendar()


@xlo.func(
    help="Check if a date is a valid fixing date for an index.",
    args={
        "Index" : "The index to query.",
        "Date" : "The date to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexIsValidFixingDate(index : ql.Index, date : qDate, Trigger = None) -> bool:
    return index.isValidFixingDate(date)


@xlo.func(
    help="Check if an index has a historical fixing for a given date.",
    args={
        "Index" : "The index to query.",
        "Date" : "The date to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexHasHistoricalFixing(index : ql.Index, date : qDate, Trigger = None) -> bool:
    return index.hasHistoricalFixing(date)


@xlo.func(
    help="Get the (forecasted) fixing of an index for a given date.",
    args={
        "Index" : "The index to query.",
        "Date" : "The date to check.",
        "ForecastTodaysFixing" : "Whether to forecast today's fixing from curve.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexFixing(index : ql.Index, date : qDate, forecastTodaysFixing = False, Trigger = None) -> float:
    return index.fixing(date, forecastTodaysFixing)


@xlo.func(
    help="Get the past fixing of an index for a given date. Raises if no past fixing is available.",
    args={
        "Index" : "The index to query.",
        "Date" : "The date to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexPastFixing(index : ql.Index, date : qDate, Trigger = None) -> float:
    return index.pastFixing(date)


@xlo.func(
    help="Add a fixing for an index on a given date. Returns whether the fixing was added successfully.",
    args={
        "Index" : "The index to update.",
        "Date" : "The date of the fixing.",
        "Value" : "The value of the fixing.",
        "ForceOverwrite" : "Whether to force overwriting an existing fixing for the date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexAddFixing(index : ql.Index, date : qDate, value : float, forceOverwrite : bool = False, Trigger = None) -> bool:
    index.addFixing(date, value, forceOverwrite)
    return index.fixing(date) == value


@xlo.func(
    help="Add multiple fixings for an index. Returns whether all fixings were added successfully.",
    args={
        "Index" : "The index to update.",
        "Dates" : "The dates of the fixings.",
        "Values" : "The values of the fixings.",
        "ForceOverwrite" : "Whether to force overwriting existing fixings for the dates.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexAddFixings(
        index : ql.Index,
        dates : xlo.Array(dims=1),
        values : xlo.Array(dims=1),
        forceOverwrite : bool = False,
        Trigger = None
    ) -> bool:
    _dates = [_qDate(d) for d in dates]
    _values = [float(v) for v in values]
    index.addFixings(_dates, _values, forceOverwrite)
    return all(index.fixing(d) == v for d, v in zip(_dates, _values))


@xlo.func(
    help="Get the time series of fixings for an index.",
    args={
        "Index" : "The index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexTimeSeries(index : ql.Index, Trigger = None):
    return index.timeSeries()


@xlo.func(
    help="Clear all fixings for an index.",
    args={
        "Index" : "The index to update.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexClearFixings(index : ql.Index, Trigger = None) -> bool:
    index.clearFixings()
    return True


## Interest rate index interface

@xlo.func(
    help="Get the family name of an interest rate index.",
    args={
        "Index" : "The interest rate index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexFamilyName(index : ql.InterestRateIndex, Trigger = None) -> str:
    return index.familyName()


@xlo.func(
    help="Get the tenor of an interest rate index.",
    args={
        "Index" : "The interest rate index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexTenor(index : ql.InterestRateIndex, Trigger = None) -> ql.Period:
    return index.tenor()


@xlo.func(
    help="Get the fixing days of an interest rate index.",
    args={
        "Index" : "The interest rate index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexFixingDays(index : ql.InterestRateIndex, Trigger = None) -> int:
    return index.fixingDays()


@xlo.func(
    help="Get the fixing date for an interest rate index given a value date.",
    args={
        "Index" : "The interest rate index to query.",
        "ValueDate" : "The value date for which to get the fixing date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexFixingDate(index : ql.InterestRateIndex, valueDate : qDate, Trigger = None) -> ql.Date:
    return index.fixingDate(valueDate)


@xlo.func(
    help="Get the currency of an interest rate index.",
    args={
        "Index" : "The interest rate index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexCurrency(index : ql.InterestRateIndex, Trigger = None) -> ql.Currency:
    return index.currency()


@xlo.func(
    help="Get the day counter of an interest rate index.",
    args={
        "Index" : "The interest rate index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexDayCounter(index : ql.InterestRateIndex, Trigger = None) -> ql.DayCounter:
    return index.dayCounter()


@xlo.func(
    help="Get the maturity date for an interest rate index given a value date.",
    args={
        "Index" : "The interest rate index to query.",
        "ValueDate" : "The value date for which to get the maturity date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexMaturityDate(index : ql.InterestRateIndex, valueDate : qDate, Trigger = None) -> ql.Date:
    return index.maturityDate(valueDate)


@xlo.func(
    help="Get the value date for an interest rate index given a fixing date.",
    args={
        "Index" : "The interest rate index to query.",
        "FixingDate" : "The fixing date for which to get the value date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexValueDate(index : ql.InterestRateIndex, fixingDate : qDate, Trigger = None) -> ql.Date:
    return index.valueDate(fixingDate)


## Ibor index


@xlo.func(
    help="Create a QuantLib IborIndex object.",
    args={
        "FamilyName" : "The family name of the index.",
        "Tenor" : "The tenor of the index.",
        "SettlementDays" : "The number of settlement days for the index.",
        "Currency" : "The currency of the index.",
        "Calendar" : "The calendar used for fixing date calculations.",
        "Convention" : "The business day convention used for fixing date calculations.",
        "EndOfMonth" : "Whether to apply end-of-month rule for fixing date calculations.",
        "DayCounter" : "The day count convention used for the index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIborIndex(
    familyName : str,
    tenor : qPeriod,
    settlementDays : int,
    currency : qCurrency,
    calendar : qCalendar,
    convention : qBusinessDayConvention,
    endOfMonth : bool,
    dayCounter : qDayCounter,
    projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    Trigger = None
) -> ql.IborIndex:
    return ql.IborIndex(
        familyName,
        tenor,
        settlementDays,
        currency,
        calendar,
        convention,
        endOfMonth,
        dayCounter,
        projectionCurve
    )


@xlo.func(
    help="Create a QuantLib Cdor index object.",
    args={
        "Tenor" : "The tenor of the CDOR index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCdor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Cdor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib BBSW index object.",
    args={
        "Tenor" : "The tenor of the BBSW index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBbsw(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Bbsw(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib Bkbm index object.",
    args={
        "Tenor" : "The tenor of the Bkbm index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBkbm(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Bkbm(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib Euribor index object.",
    args={
        "Tenor" : "The tenor of the Euribor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEuribor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Euribor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib Euribor365 index object.",
    args={
        "Tenor" : "The tenor of the Euribor365 index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEuribor365(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Euribor365(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib Jibar index object.",
    args={
        "Tenor" : "The tenor of the Jibar index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlJibar(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Jibar(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib Mosprime index object.",
    args={
        "Tenor" : "The tenor of the Mosprime index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMosprime(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Mosprime(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib NZDLibor index object.",
    args={
        "Tenor" : "The tenor of the NZDLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNZDLibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.NZDLibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib Pribor index object.",
    args={
        "Tenor" : "The tenor of the Pribor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPribor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Pribor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib Robor index object.",
    args={
        "Tenor" : "The tenor of the Robor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRobor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Robor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib Shibor index object.",
    args={
        "Tenor" : "The tenor of the Shibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlShibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Shibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib Tibor index object.",
    args={
        "Tenor" : "The tenor of the Tibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Tibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib THBFIX index object.",
    args={
        "Tenor" : "The tenor of the THBFIX index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTHBFIX(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.THBFIX(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib Wibor index object.",
    args={
        "Tenor" : "The tenor of the Wibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlWibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Wibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib Zibor index object.",
    args={
        "Tenor" : "The tenor of the Zibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Zibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib AUDLibor index object.",
    args={
        "Tenor" : "The tenor of the AUDLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAUDLibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.AUDLibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib CADLibor index object.",
    args={
        "Tenor" : "The tenor of the CADLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCADLibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.CADLibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib CHFLibor index object.",
    args={
        "Tenor" : "The tenor of the CHFLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCHFLibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.CHFLibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib DKKLibor index object.",
    args={
        "Tenor" : "The tenor of the DKKLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDKKLibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.DKKLibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib EURLibor index object.",
    args={
        "Tenor" : "The tenor of the EURLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEURLibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.EURLibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib GBPLibor index object.",
    args={
        "Tenor" : "The tenor of the GBPLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGBPLibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.GBPLibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib JPYLibor index object.",
    args={
        "Tenor" : "The tenor of the JPYLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlJPYLibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.JPYLibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib SEKLibor index object.",
    args={
        "Tenor" : "The tenor of the SEKLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSEKLibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.SEKLibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib TRLibor index object.",
    args={
        "Tenor" : "The tenor of the TRLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTRLibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.TRLibor(tenor, projectionCurve)

@xlo.func(
    help="Create a QuantLib USDLibor index object.",
    args={
        "Tenor" : "The tenor of the USDLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlUSDLibor(tenor : qPeriod, projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.USDLibor(tenor, projectionCurve)


## Overnight index

@xlo.func(
    help="Create a QuantLib OvernightIndex object.",
    args={
        "FamilyName" : "The family name of the index.",
        "SettlementDays" : "The number of settlement days for the index.",
        "Currency" : "The currency of the index.",
        "Calendar" : "The calendar used for fixing date calculations.",
        "DayCounter" : "The day count convention used for the index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlOvernightIndex(
    familyName : str,
    settlementDays : int,
    currency : qCurrency,
    calendar : qCalendar,
    dayCounter : qDayCounter,
    projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    Trigger = None
) -> ql.OvernightIndex:
    return ql.OvernightIndex(
        familyName,
        settlementDays,
        currency,
        calendar,
        dayCounter,
        projectionCurve
    )

@xlo.func(
    help="Create a QuantLib Aonia index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAonia(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Aonia(projectionCurve)

@xlo.func(
    help="Create a QuantLib Cdi index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCdi(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Cdi(projectionCurve)

@xlo.func(
    help="Create a QuantLib Corra index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCorra(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Corra(projectionCurve)

@xlo.func(
    help="Create a QuantLib Destr index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDestr(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Destr(projectionCurve)

@xlo.func(
    help="Create a QuantLib Eonia index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEonia(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Eonia(projectionCurve)

@xlo.func(
    help="Create a QuantLib Estr index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEstr(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Estr(projectionCurve)

@xlo.func(
    help="Create a QuantLib FedFunds index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFedFunds(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.FedFunds(projectionCurve)

@xlo.func(
    help="Create a QuantLib Kofr index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlKofr(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Kofr(projectionCurve)

@xlo.func(
    help="Create a QuantLib Nzocr index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNzocr(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Nzocr(projectionCurve)

@xlo.func(
    help="Create a QuantLib Saron index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSaron(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Saron(projectionCurve)

@xlo.func(
    help="Create a QuantLib Sofr index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSofr(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Sofr(projectionCurve)

@xlo.func(
    help="Create a QuantLib Sonia index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSonia(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Sonia(projectionCurve)

@xlo.func(
    help="Create a QuantLib Swestr index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwestr(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Swestr(projectionCurve)

@xlo.func(
    help="Create a QuantLib Tonar index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTonar(projectionCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.IborIndex:
    return ql.Tonar(projectionCurve)


## Swap index

@xlo.func(
    help="Create a QuantLib SwapIndex object.",
    args={
        "FamilyName" : "The family name of the index.",
        "Tenor" : "The tenor of the swap index.",
        "SettlementDays" : "The number of settlement days for the index.",
        "Currency" : "The currency of the index.",
        "Calendar" : "The calendar used for fixing date calculations.",
        "FixedLegTenor" : "The tenor of the fixed leg.",
        "FixedLegConvention" : "The business day convention used for the fixed leg schedule generation.",
        "FixedLegDayCounter" : "The day count convention used for the fixed leg.",
        "IborIndex" : "The underlying Ibor index used for the floating leg.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the ibor index will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapIndex(
    familyName : str,
    tenor : qPeriod,
    settlementDays : int,
    currency : qCurrency,
    calendar : qCalendar,
    fixedLegTenor : qPeriod,
    fixedLegConvention : qBusinessDayConvention,
    fixedLegDayCounter : qDayCounter,
    iborIndex : ql.IborIndex,
    discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    Trigger = None
) -> ql.SwapIndex:
    if discountCurve:
        return ql.SwapIndex(
            familyName,
            tenor,
            settlementDays,
            currency,
            calendar,
            fixedLegTenor,
            fixedLegConvention,
            fixedLegDayCounter,
            iborIndex,
            discountCurve,
        )
    else:
        return ql.SwapIndex(
            familyName,
            tenor,
            settlementDays,
            currency,
            calendar,
            fixedLegTenor,
            fixedLegConvention,
            fixedLegDayCounter,
            iborIndex,
        )

@xlo.func(
    help="Create a QuantLib EuriborSwapIsdaFixA index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEuriborSwapIsdaFixA(swapTenor : qPeriod, projCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.SwapIndex:
    if projCurve and discountCurve:
        return ql.EuriborSwapIsdaFixA(swapTenor, projCurve, discountCurve)
    else:
        return ql.EuriborSwapIsdaFixA(swapTenor, projCurve)

@xlo.func(
    help="Create a QuantLib EuriborSwapIsdaFixB index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEuriborSwapIsdaFixB(swapTenor : qPeriod, projCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.SwapIndex:
    if projCurve and discountCurve:
        return ql.EuriborSwapIsdaFixB(swapTenor, projCurve, discountCurve)
    else:
        return ql.EuriborSwapIsdaFixB(swapTenor, projCurve)

@xlo.func(
    help="Create a QuantLib EuriborSwapIfrFix index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEuriborSwapIfrFix(swapTenor : qPeriod, projCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.SwapIndex:
    if projCurve and discountCurve:
        return ql.EuriborSwapIfrFix(swapTenor, projCurve, discountCurve)
    else:
        return ql.EuriborSwapIfrFix(swapTenor, projCurve)

@xlo.func(
    help="Create a QuantLib EurLiborSwapIsdaFixA index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEurLiborSwapIsdaFixA(swapTenor : qPeriod, projCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.SwapIndex:
    if projCurve and discountCurve:
        return ql.EurLiborSwapIsdaFixA(swapTenor, projCurve, discountCurve)
    else:
        return ql.EurLiborSwapIsdaFixA(swapTenor, projCurve)

@xlo.func(
    help="Create a QuantLib EurLiborSwapIsdaFixB index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEurLiborSwapIsdaFixB(swapTenor : qPeriod, projCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.SwapIndex:
    if projCurve and discountCurve:
        return ql.EurLiborSwapIsdaFixB(swapTenor, projCurve, discountCurve)
    else:
        return ql.EurLiborSwapIsdaFixB(swapTenor, projCurve)

@xlo.func(
    help="Create a QuantLib EurLiborSwapIfrFix index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEurLiborSwapIfrFix(swapTenor : qPeriod, projCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.SwapIndex:
    if projCurve and discountCurve:
        return ql.EurLiborSwapIfrFix(swapTenor, projCurve, discountCurve)
    else:
        return ql.EurLiborSwapIfrFix(swapTenor, projCurve)

@xlo.func(
    help="Create a QuantLib ChfLiborSwapIsdaFix index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlChfLiborSwapIsdaFix(swapTenor : qPeriod, projCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.SwapIndex:
    if projCurve and discountCurve:
        return ql.ChfLiborSwapIsdaFix(swapTenor, projCurve, discountCurve)
    else:
        return ql.ChfLiborSwapIsdaFix(swapTenor, projCurve)

@xlo.func(
    help="Create a QuantLib GbpLiborSwapIsdaFix index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGbpLiborSwapIsdaFix(swapTenor : qPeriod, projCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.SwapIndex:
    if projCurve and discountCurve:
        return ql.GbpLiborSwapIsdaFix(swapTenor, projCurve, discountCurve)
    else:
        return ql.GbpLiborSwapIsdaFix(swapTenor, projCurve)

@xlo.func(
    help="Create a QuantLib JpyLiborSwapIsdaFixAm index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlJpyLiborSwapIsdaFixAm(swapTenor : qPeriod, projCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.SwapIndex:
    if projCurve and discountCurve:
        return ql.JpyLiborSwapIsdaFixAm(swapTenor, projCurve, discountCurve)
    else:
        return ql.JpyLiborSwapIsdaFixAm(swapTenor, projCurve)

@xlo.func(
    help="Create a QuantLib JpyLiborSwapIsdaFixPm index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlJpyLiborSwapIsdaFixPm(swapTenor : qPeriod, projCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.SwapIndex:
    if projCurve and discountCurve:
        return ql.JpyLiborSwapIsdaFixPm(swapTenor, projCurve, discountCurve)
    else:
        return ql.JpyLiborSwapIsdaFixPm(swapTenor, projCurve)

@xlo.func(
    help="Create a QuantLib UsdLiborSwapIsdaFixAm index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlUsdLiborSwapIsdaFixAm(swapTenor : qPeriod, projCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.SwapIndex:
    if projCurve and discountCurve:
        return ql.UsdLiborSwapIsdaFixAm(swapTenor, projCurve, discountCurve)
    else:
        return ql.UsdLiborSwapIsdaFixAm(swapTenor, projCurve)

@xlo.func(
    help="Create a QuantLib UsdLiborSwapIsdaFixPm index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlUsdLiborSwapIsdaFixPm(swapTenor : qPeriod, projCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discountCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), Trigger = None) -> ql.SwapIndex:
    if projCurve and discountCurve:
        return ql.UsdLiborSwapIsdaFixPm(swapTenor, projCurve, discountCurve)
    else:
        return ql.UsdLiborSwapIsdaFixPm(swapTenor, projCurve)


## Swapspread index

@xlo.func(
    help="Create a QuantLib SwapSpreadIndex object.",
    args={
        "FamilyName" : "The family name of the index.",
        "SwapIndex1" : "The first underlying swap index.",
        "SwapIndex2" : "The second underlying swap index.",
        "Gearing1" : "The gearing applied to the first swap index (default is 1.0).",
        "Gearing2" : "The gearing applied to the second swap index (default is -1.0).",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapSpreadIndex(
    familyName : str,
    swapIndex1 : ql.SwapIndex,
    swapIndex2 : ql.SwapIndex,
    gearing1 : float = 1.0,
    gearing2 : float = -1.0,
    Trigger = None) -> ql.SwapSpreadIndex:
    return ql.SwapSpreadIndex(familyName, swapIndex1, swapIndex2, gearing1, gearing2)


@xlo.func(
    help="Forecast the fixing of a QuantLib SwapIndex.",
    args={
        "SwapIndex" : "The swap index for which to forecast the fixing.",
        "FixingDate" : "The date for which to forecast the fixing.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapIndexForecastFixing(swapIndex : ql.SwapIndex, fixingDate : qDate) -> ql.Swap:
    return swapIndex.forecastFixing(fixingDate)


# Equity index

@xlo.func(
    help="Create a QuantLib EquityIndex object.",
    args={
        "Name" : "The name of the equity index.",
        "FixingCalendar" : "The calendar used for fixing date calculations.",
        "Currency" : "The currency of the index.",
        "SpotPrice" : "The current spot price of the index.",
        "DiscCurve" : "An optional discount curve for the index.",
        "DivCurve" : "An optional dividend curve for the index.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEquityIndex(
        name : str,
        fixingCalendar : qCalendar,
        currency : qCurrency,
        spotPrice : float,
        discCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
        divCurve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
        Trigger = None
    ) -> ql.EquityIndex:
    qpotprice_qh = ql.QuoteHandle(ql.SimpleQuote(spotPrice))
    return ql.EquityIndex(name, fixingCalendar, currency, discCurve, divCurve, qpotprice_qh)
