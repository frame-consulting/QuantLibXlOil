import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .calendars import qCalendar, qBusinessDayConvention
from .date import _qDate, qDate
from .utilities import first_key, UNKNOWN_KEY, UNKNOWN_VALUE, enum_value


QL_EXERCISE_TYPE = {
    'EUROPEAN': ql.Exercise.European,
    'BERMUDAN': ql.Exercise.Bermudan,
    'AMERICAN': ql.Exercise.American,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}


def _qExerciseType(s: str) -> int:
    return enum_value(s, QL_EXERCISE_TYPE)

@xlo.converter()
def qExerciseType(s: str)-> int:
    return _qExerciseType(s)

# Exercise interface

@xlo.func(
    help='Return the type of a QuantLib Exercise as a string.',
    args={
        'exercise': 'QuantLib Exercise.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlExerciseType(exercise: ql.Exercise, trigger= None) -> str:
    return first_key(QL_EXERCISE_TYPE, exercise.type(), UNKNOWN_VALUE)


@xlo.func(
    help='Return the exercise date for a given index.',
    args={
        'exercise': 'QuantLib Exercise.',
        'idx': 'Index of the exercise date to return.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlExerciseDate(exercise: ql.Exercise, idx: int, trigger= None) -> ql.Date:
    return exercise.date(idx)


@xlo.func(
    help='Return the exercise date for a given index.',
    args={
        'exercise': 'QuantLib Exercise.',
        'idx': 'Index of the exercise date to return.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlExerciseDateAt(exercise: ql.Exercise, idx: int, trigger= None) -> ql.Date:
    return exercise.dateAt(idx)


@xlo.func(
    help='Return the exercise dates for a given exercise.',
    args={
        'exercise': 'QuantLib Exercise.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlExerciseDates(exercise: ql.Exercise, trigger= None) -> list[int]:
    return [ d.serialNumber() for d in exercise.dates() ]


# Exercise constructors

@xlo.func(
    help='Create a European exercise.',
    args={
        'date': 'The exercise date.'
    },
    group=EXCEL_GROUP_NAME,
)
def qlEuropeanExercise(date: qDate, trigger=None) -> ql.EuropeanExercise:
    return ql.EuropeanExercise(date)


@xlo.func(
    help='Create a Bermudan exercise.',
    args={
        'dates': 'The exercise dates.'
    },
    group=EXCEL_GROUP_NAME,
)
def qlBermudanExercise(dates: xlo.Array(dims=1), trigger=None) -> ql.BermudanExercise:
    dates_ = [_qDate(d) for d in dates]
    return ql.BermudanExercise(dates_)


@xlo.func(
    help='Create an American exercise.',
    args={
        'first_date': 'The first exercise date.',
        'last_date': 'The last exercise date.'
    },
    group=EXCEL_GROUP_NAME,
)
def qlAmericanExercise(first_date: qDate, last_date: qDate, trigger=None) -> ql.AmericanExercise:
    return ql.AmericanExercise(first_date, last_date)


@xlo.func(
    help='Create a rebated exercise.',
    args={
        'exercise': 'The underlying exercise.',
        'rebates': 'The rebate amounts.',
        'rebate_settlement_days': 'The number of settlement days for the rebate.',
        'rebate_payment_calendar': 'The calendar for rebate payment.',
        'rebate_payment_convention': 'The business day convention for rebate payment.'
    },
    group=EXCEL_GROUP_NAME,
)
def qlRebatedExercise(
        exercise: ql.Exercise,
        rebates: xlo.Array(dims=1),
        rebate_settlement_days: int,
        rebate_payment_calendar: qCalendar = ql.NullCalendar(),
        rebate_payment_convention: qBusinessDayConvention = ql.Following,
        trigger=None
) -> ql.RebatedExercise:
    return ql.RebatedExercise(
        exercise,
        rebates,
        rebate_settlement_days,
        rebate_payment_calendar,
        rebate_payment_convention,
    )


@xlo.func(
    help='Create a swing exercise.',
    args={
        'dates': 'The exercise dates.'
    },
    group=EXCEL_GROUP_NAME,
)
def qlSwingExercise(dates: xlo.Array(dims=1), trigger=None) -> ql.SwingExercise:
    dates_ = [_qDate(d) for d in dates]
    return ql.SwingExercise(dates_)
