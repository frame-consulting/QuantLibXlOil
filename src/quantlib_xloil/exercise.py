import QuantLib as ql
import xloil as xlo

from .calendars import qCalendar, qBusinessDayConvention
from .config import EXCEL_GROUP_NAME
from .date import qDate, _to_date_list
from .utilities import enum_value, first_key, UNKNOWN_KEY, UNKNOWN_VALUE

QL_EXERCISE_TYPE = {
    "AMERICAN": ql.Exercise.American,
    "BERMUDAN": ql.Exercise.Bermudan,
    "EUROPEAN": ql.Exercise.European,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qExerciseType(s: str) -> int:
    return enum_value(s, QL_EXERCISE_TYPE)


@xlo.converter()
def qExerciseType(s: str) -> int:
    return _qExerciseType(s)


# Exercise interface


@xlo.func(
    help="Return the type of a QuantLib Exercise as a string.",
    args={
        "exercise": "QuantLib Exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExerciseType(exercise: ql.Exercise, trigger=None) -> str:
    return first_key(QL_EXERCISE_TYPE, exercise.type(), UNKNOWN_VALUE)


@xlo.func(
    help="Return the exercise date for a given index.",
    args={
        "exercise": "QuantLib Exercise.",
        "idx": "Index of the exercise date to return.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExerciseDate(exercise: ql.Exercise, idx: int, trigger=None) -> ql.Date:
    return exercise.date(idx)


@xlo.func(
    help="Return the exercise date for a given index.",
    args={
        "exercise": "QuantLib Exercise.",
        "idx": "Index of the exercise date to return.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExerciseDateAt(exercise: ql.Exercise, idx: int, trigger=None) -> ql.Date:
    return exercise.dateAt(idx)


@xlo.func(
    help="Return the exercise dates for a given exercise.",
    args={
        "exercise": "QuantLib Exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlExerciseDates(exercise: ql.Exercise, trigger=None) -> list[int]:
    return [d.serialNumber() for d in exercise.dates()]


# Exercise constructors


@xlo.func(
    help="Create a European exercise.",
    args={"date": "The exercise date."},
    group=EXCEL_GROUP_NAME,
)
def qlEuropeanExercise(date: qDate, trigger=None) -> ql.EuropeanExercise:
    return ql.EuropeanExercise(date)


@xlo.func(
    help="Create a Bermudan exercise.",
    args={
        "dates": "The exercise dates.",
        "payoff_at_expiry": "Whether the payoff is at expiry or at exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlBermudanExercise(
    dates: xlo.Array(dims=1), payoff_at_expiry: bool = False, trigger=None
) -> ql.BermudanExercise:

    return ql.BermudanExercise(_to_date_list(dates), payoff_at_expiry)


@xlo.func(
    help="Create an American exercise.",
    args={
        "first_date": "The first exercise date.",
        "last_date": "The last exercise date.",
        "payoff_at_expiry": "Whether the payoff is at expiry or at exercise.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlAmericanExercise(
    first_date: qDate, last_date: qDate, payoff_at_expiry: bool = False, trigger=None
) -> ql.AmericanExercise:
    return ql.AmericanExercise(first_date, last_date, payoff_at_expiry)


@xlo.func(
    help="Create a rebated exercise.",
    args={
        "exercise": "The underlying exercise.",
        "rebates": "The rebate amounts.",
        "rebate_settlement_days": "The number of settlement days for the rebate.",
        "rebate_payment_calendar": "The calendar for rebate payment.",
        "rebate_payment_convention": "The business day convention for rebate payment.",
    },
    group=EXCEL_GROUP_NAME,
)
def qlRebatedExercise(
    exercise: ql.Exercise,
    rebates: xlo.Array(dims=1),
    rebate_settlement_days: int,
    rebate_payment_calendar: qCalendar = ql.NullCalendar(),
    rebate_payment_convention: qBusinessDayConvention = ql.Following,
    trigger=None,
) -> ql.RebatedExercise:
    return ql.RebatedExercise(
        exercise,
        rebates,
        rebate_settlement_days,
        rebate_payment_calendar,
        rebate_payment_convention,
    )


@xlo.func(
    help="Create a swing exercise.",
    args={"dates": "The exercise dates."},
    group=EXCEL_GROUP_NAME,
)
def qlSwingExercise(dates: xlo.Array(dims=1), trigger=None) -> ql.SwingExercise:
    return ql.SwingExercise(_to_date_list(dates))
