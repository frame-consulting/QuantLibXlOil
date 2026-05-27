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
def qlIndexManagerHistories(trigger = None):
    return ql.IndexManager.instance().histories()

@xlo.func(
    help="Clear the histories of all indices in the IndexManager.",
    group=EXCEL_GROUP_NAME,
)
def qlIndexManagerClearHistories(trigger = None):
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
def qlIndexName(index : ql.Index, trigger = None) -> str:
    return index.name()


@xlo.func(
    help="Get the fixing calendar of an index.",
    args={
        "Index" : "The index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexFixingCalendar(index : ql.Index, trigger = None) -> ql.Calendar:
    return index.fixingCalendar()


@xlo.func(
    help="Check if a date is a valid fixing date for an index.",
    args={
        "Index" : "The index to query.",
        "Date" : "The date to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexIsValidFixingDate(index : ql.Index, date : qDate, trigger = None) -> bool:
    return index.isValidFixingDate(date)


@xlo.func(
    help="Check if an index has a historical fixing for a given date.",
    args={
        "Index" : "The index to query.",
        "Date" : "The date to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexHasHistoricalFixing(index : ql.Index, date : qDate, trigger = None) -> bool:
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
def qlIndexFixing(index : ql.Index, date : qDate, forecast_todays_fixing = False, trigger = None) -> float:
    return index.fixing(date, forecast_todays_fixing)


@xlo.func(
    help="Get the past fixing of an index for a given date. Raises if no past fixing is available.",
    args={
        "Index" : "The index to query.",
        "Date" : "The date to check.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexPastFixing(index : ql.Index, date : qDate, trigger = None) -> float:
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
def qlIndexAddFixing(index : ql.Index, date : qDate, value : float, force_overwrite : bool = False, trigger = None) -> bool:
    index.addFixing(date, value, force_overwrite)
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
        force_overwrite : bool = False,
        trigger = None
    ) -> bool:
    _dates = [_qDate(d) for d in dates]
    _values = [float(v) for v in values]
    index.addFixings(_dates, _values, force_overwrite)
    return all(index.fixing(d) == v for d, v in zip(_dates, _values))


@xlo.func(
    help="Get the time series of fixings for an index.",
    args={
        "Index" : "The index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexTimeSeries(index : ql.Index, trigger = None):
    return index.timeSeries()


@xlo.func(
    help="Clear all fixings for an index.",
    args={
        "Index" : "The index to update.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlIndexClearFixings(index : ql.Index, trigger = None) -> bool:
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
def qlInterestRateIndexFamilyName(index : ql.InterestRateIndex, trigger = None) -> str:
    return index.familyName()


@xlo.func(
    help="Get the tenor of an interest rate index.",
    args={
        "Index" : "The interest rate index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexTenor(index : ql.InterestRateIndex, trigger = None) -> ql.Period:
    return index.tenor()


@xlo.func(
    help="Get the fixing days of an interest rate index.",
    args={
        "Index" : "The interest rate index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexFixingDays(index : ql.InterestRateIndex, trigger = None) -> int:
    return index.fixingDays()


@xlo.func(
    help="Get the fixing date for an interest rate index given a value date.",
    args={
        "Index" : "The interest rate index to query.",
        "ValueDate" : "The value date for which to get the fixing date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexFixingDate(index : ql.InterestRateIndex, value_date : qDate, trigger = None) -> ql.Date:
    return index.fixingDate(value_date)


@xlo.func(
    help="Get the currency of an interest rate index.",
    args={
        "Index" : "The interest rate index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexCurrency(index : ql.InterestRateIndex, trigger = None) -> ql.Currency:
    return index.currency()


@xlo.func(
    help="Get the day counter of an interest rate index.",
    args={
        "Index" : "The interest rate index to query.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexDayCounter(index : ql.InterestRateIndex, trigger = None) -> ql.DayCounter:
    return index.dayCounter()


@xlo.func(
    help="Get the maturity date for an interest rate index given a value date.",
    args={
        "Index" : "The interest rate index to query.",
        "ValueDate" : "The value date for which to get the maturity date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexMaturityDate(index : ql.InterestRateIndex, value_date : qDate, trigger = None) -> ql.Date:
    return index.maturityDate(value_date)


@xlo.func(
    help="Get the value date for an interest rate index given a fixing date.",
    args={
        "Index" : "The interest rate index to query.",
        "FixingDate" : "The fixing date for which to get the value date.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlInterestRateIndexValueDate(index : ql.InterestRateIndex, fixing_date : qDate, trigger = None) -> ql.Date:
    return index.valueDate(fixing_date)


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
    family_name : str,
    tenor : qPeriod,
    settlement_days : int,
    currency : qCurrency,
    calendar : qCalendar,
    convention : qBusinessDayConvention,
    end_of_month : bool,
    day_counter : qDayCounter,
    projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger = None
) -> ql.IborIndex:
    return ql.IborIndex(
        family_name,
        tenor,
        settlement_days,
        currency,
        calendar,
        convention,
        end_of_month,
        day_counter,
        projection_curve
    )


@xlo.func(
    help="Create a QuantLib Cdor index object.",
    args={
        "Tenor" : "The tenor of the CDOR index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCdor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Cdor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib BBSW index object.",
    args={
        "Tenor" : "The tenor of the BBSW index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBbsw(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Bbsw(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib Bkbm index object.",
    args={
        "Tenor" : "The tenor of the Bkbm index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBkbm(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Bkbm(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib Euribor index object.",
    args={
        "Tenor" : "The tenor of the Euribor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEuribor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Euribor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib Euribor365 index object.",
    args={
        "Tenor" : "The tenor of the Euribor365 index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEuribor365(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Euribor365(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib Jibar index object.",
    args={
        "Tenor" : "The tenor of the Jibar index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlJibar(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Jibar(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib Mosprime index object.",
    args={
        "Tenor" : "The tenor of the Mosprime index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlMosprime(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Mosprime(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib NZDLibor index object.",
    args={
        "Tenor" : "The tenor of the NZDLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNZDLibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.NZDLibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib Pribor index object.",
    args={
        "Tenor" : "The tenor of the Pribor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlPribor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Pribor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib Robor index object.",
    args={
        "Tenor" : "The tenor of the Robor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRobor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Robor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib Shibor index object.",
    args={
        "Tenor" : "The tenor of the Shibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlShibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Shibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib Tibor index object.",
    args={
        "Tenor" : "The tenor of the Tibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Tibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib THBFIX index object.",
    args={
        "Tenor" : "The tenor of the THBFIX index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTHBFIX(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.THBFIX(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib Wibor index object.",
    args={
        "Tenor" : "The tenor of the Wibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlWibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Wibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib Zibor index object.",
    args={
        "Tenor" : "The tenor of the Zibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlZibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Zibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib AUDLibor index object.",
    args={
        "Tenor" : "The tenor of the AUDLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAUDLibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.AUDLibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib CADLibor index object.",
    args={
        "Tenor" : "The tenor of the CADLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCADLibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.CADLibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib CHFLibor index object.",
    args={
        "Tenor" : "The tenor of the CHFLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCHFLibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.CHFLibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib DKKLibor index object.",
    args={
        "Tenor" : "The tenor of the DKKLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDKKLibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.DKKLibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib EURLibor index object.",
    args={
        "Tenor" : "The tenor of the EURLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEURLibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.EURLibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib GBPLibor index object.",
    args={
        "Tenor" : "The tenor of the GBPLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGBPLibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.GBPLibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib JPYLibor index object.",
    args={
        "Tenor" : "The tenor of the JPYLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlJPYLibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.JPYLibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib SEKLibor index object.",
    args={
        "Tenor" : "The tenor of the SEKLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSEKLibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.SEKLibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib TRLibor index object.",
    args={
        "Tenor" : "The tenor of the TRLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTRLibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.TRLibor(tenor, projection_curve)

@xlo.func(
    help="Create a QuantLib USDLibor index object.",
    args={
        "Tenor" : "The tenor of the USDLibor index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlUSDLibor(tenor : qPeriod, projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.USDLibor(tenor, projection_curve)


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
    family_name : str,
    settlement_days : int,
    currency : qCurrency,
    calendar : qCalendar,
    day_counter : qDayCounter,
    projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger = None
) -> ql.OvernightIndex:
    return ql.OvernightIndex(
        family_name,
        settlement_days,
        currency,
        calendar,
        day_counter,
        projection_curve
    )

@xlo.func(
    help="Create a QuantLib Aonia index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAonia(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Aonia(projection_curve)

@xlo.func(
    help="Create a QuantLib Cdi index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCdi(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Cdi(projection_curve)

@xlo.func(
    help="Create a QuantLib Corra index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlCorra(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Corra(projection_curve)

@xlo.func(
    help="Create a QuantLib Destr index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlDestr(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Destr(projection_curve)

@xlo.func(
    help="Create a QuantLib Eonia index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEonia(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Eonia(projection_curve)

@xlo.func(
    help="Create a QuantLib Estr index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEstr(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Estr(projection_curve)

@xlo.func(
    help="Create a QuantLib FedFunds index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlFedFunds(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.FedFunds(projection_curve)

@xlo.func(
    help="Create a QuantLib Kofr index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlKofr(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Kofr(projection_curve)

@xlo.func(
    help="Create a QuantLib Nzocr index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlNzocr(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Nzocr(projection_curve)

@xlo.func(
    help="Create a QuantLib Saron index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSaron(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Saron(projection_curve)

@xlo.func(
    help="Create a QuantLib Sofr index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSofr(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Sofr(projection_curve)

@xlo.func(
    help="Create a QuantLib Sonia index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSonia(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Sonia(projection_curve)

@xlo.func(
    help="Create a QuantLib Swestr index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwestr(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Swestr(projection_curve)

@xlo.func(
    help="Create a QuantLib Tonar index object.",
    args={
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlTonar(projection_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.IborIndex:
    return ql.Tonar(projection_curve)


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
    family_name : str,
    tenor : qPeriod,
    settlement_days : int,
    currency : qCurrency,
    calendar : qCalendar,
    fixed_leg_tenor : qPeriod,
    fixed_leg_convention : qBusinessDayConvention,
    fixed_leg_day_counter : qDayCounter,
    ibor_index : ql.IborIndex,
    discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
    trigger = None
) -> ql.SwapIndex:
    if discount_curve:
        return ql.SwapIndex(
            family_name,
            tenor,
            settlement_days,
            currency,
            calendar,
            fixed_leg_tenor,
            fixed_leg_convention,
            fixed_leg_day_counter,
            ibor_index,
            discount_curve,
        )
    else:
        return ql.SwapIndex(
            family_name,
            tenor,
            settlement_days,
            currency,
            calendar,
            fixed_leg_tenor,
            fixed_leg_convention,
            fixed_leg_day_counter,
            ibor_index,
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
def qlEuriborSwapIsdaFixA(swap_tenor : qPeriod, proj_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.SwapIndex:
    if proj_curve and discount_curve:
        return ql.EuriborSwapIsdaFixA(swap_tenor, proj_curve, discount_curve)
    else:
        return ql.EuriborSwapIsdaFixA(swap_tenor, proj_curve)

@xlo.func(
    help="Create a QuantLib EuriborSwapIsdaFixB index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEuriborSwapIsdaFixB(swap_tenor : qPeriod, proj_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.SwapIndex:
    if proj_curve and discount_curve:
        return ql.EuriborSwapIsdaFixB(swap_tenor, proj_curve, discount_curve)
    else:
        return ql.EuriborSwapIsdaFixB(swap_tenor, proj_curve)

@xlo.func(
    help="Create a QuantLib EuriborSwapIfrFix index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEuriborSwapIfrFix(swap_tenor : qPeriod, proj_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.SwapIndex:
    if proj_curve and discount_curve:
        return ql.EuriborSwapIfrFix(swap_tenor, proj_curve, discount_curve)
    else:
        return ql.EuriborSwapIfrFix(swap_tenor, proj_curve)

@xlo.func(
    help="Create a QuantLib EurLiborSwapIsdaFixA index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEurLiborSwapIsdaFixA(swap_tenor : qPeriod, proj_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.SwapIndex:
    if proj_curve and discount_curve:
        return ql.EurLiborSwapIsdaFixA(swap_tenor, proj_curve, discount_curve)
    else:
        return ql.EurLiborSwapIsdaFixA(swap_tenor, proj_curve)

@xlo.func(
    help="Create a QuantLib EurLiborSwapIsdaFixB index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEurLiborSwapIsdaFixB(swap_tenor : qPeriod, proj_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.SwapIndex:
    if proj_curve and discount_curve:
        return ql.EurLiborSwapIsdaFixB(swap_tenor, proj_curve, discount_curve)
    else:
        return ql.EurLiborSwapIsdaFixB(swap_tenor, proj_curve)

@xlo.func(
    help="Create a QuantLib EurLiborSwapIfrFix index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlEurLiborSwapIfrFix(swap_tenor : qPeriod, proj_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.SwapIndex:
    if proj_curve and discount_curve:
        return ql.EurLiborSwapIfrFix(swap_tenor, proj_curve, discount_curve)
    else:
        return ql.EurLiborSwapIfrFix(swap_tenor, proj_curve)

@xlo.func(
    help="Create a QuantLib ChfLiborSwapIsdaFix index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlChfLiborSwapIsdaFix(swap_tenor : qPeriod, proj_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.SwapIndex:
    if proj_curve and discount_curve:
        return ql.ChfLiborSwapIsdaFix(swap_tenor, proj_curve, discount_curve)
    else:
        return ql.ChfLiborSwapIsdaFix(swap_tenor, proj_curve)

@xlo.func(
    help="Create a QuantLib GbpLiborSwapIsdaFix index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlGbpLiborSwapIsdaFix(swap_tenor : qPeriod, proj_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.SwapIndex:
    if proj_curve and discount_curve:
        return ql.GbpLiborSwapIsdaFix(swap_tenor, proj_curve, discount_curve)
    else:
        return ql.GbpLiborSwapIsdaFix(swap_tenor, proj_curve)

@xlo.func(
    help="Create a QuantLib JpyLiborSwapIsdaFixAm index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlJpyLiborSwapIsdaFixAm(swap_tenor : qPeriod, proj_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.SwapIndex:
    if proj_curve and discount_curve:
        return ql.JpyLiborSwapIsdaFixAm(swap_tenor, proj_curve, discount_curve)
    else:
        return ql.JpyLiborSwapIsdaFixAm(swap_tenor, proj_curve)

@xlo.func(
    help="Create a QuantLib JpyLiborSwapIsdaFixPm index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlJpyLiborSwapIsdaFixPm(swap_tenor : qPeriod, proj_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.SwapIndex:
    if proj_curve and discount_curve:
        return ql.JpyLiborSwapIsdaFixPm(swap_tenor, proj_curve, discount_curve)
    else:
        return ql.JpyLiborSwapIsdaFixPm(swap_tenor, proj_curve)

@xlo.func(
    help="Create a QuantLib UsdLiborSwapIsdaFixAm index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlUsdLiborSwapIsdaFixAm(swap_tenor : qPeriod, proj_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.SwapIndex:
    if proj_curve and discount_curve:
        return ql.UsdLiborSwapIsdaFixAm(swap_tenor, proj_curve, discount_curve)
    else:
        return ql.UsdLiborSwapIsdaFixAm(swap_tenor, proj_curve)

@xlo.func(
    help="Create a QuantLib UsdLiborSwapIsdaFixPm index object.",
    args={
        "SwapTenor" : "The tenor of the swap index.",
        "ProjectionCurve" : "An optional projection curve for forecasting fixings.",
        "DiscountCurve" : "An optional discount curve. If not provided, the curve from the projection curve will be used for discounting.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlUsdLiborSwapIsdaFixPm(swap_tenor : qPeriod, proj_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None) -> ql.SwapIndex:
    if proj_curve and discount_curve:
        return ql.UsdLiborSwapIsdaFixPm(swap_tenor, proj_curve, discount_curve)
    else:
        return ql.UsdLiborSwapIsdaFixPm(swap_tenor, proj_curve)


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
    family_name : str,
    swap_index1 : ql.SwapIndex,
    swap_index2 : ql.SwapIndex,
    gearing1 : float = 1.0,
    gearing2 : float = -1.0,
    trigger = None) -> ql.SwapSpreadIndex:
    return ql.SwapSpreadIndex(family_name, swap_index1, swap_index2, gearing1, gearing2)


@xlo.func(
    help="Forecast the fixing of a QuantLib SwapIndex.",
    args={
        "SwapIndex" : "The swap index for which to forecast the fixing.",
        "FixingDate" : "The date for which to forecast the fixing.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwapIndexForecastFixing(swap_index : ql.SwapIndex, fixing_date : qDate) -> ql.Swap:
    return swap_index.forecastFixing(fixing_date)


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
        fixing_calendar : qCalendar,
        currency : qCurrency,
        spot_price : float,
        disc_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
        div_curve : ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(),
        trigger = None
    ) -> ql.EquityIndex:
    qpotprice_qh = ql.QuoteHandle(ql.SimpleQuote(spot_price))
    return ql.EquityIndex(name, fixing_calendar, currency, disc_curve, div_curve, qpotprice_qh)
