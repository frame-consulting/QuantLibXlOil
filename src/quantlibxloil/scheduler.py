import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .utilities import first_key, UNKNOWN_KEY, UNKNOWN_VALUE
from .date import qDate, qPeriod, _qDate, _qPeriod, _qFrequency
from .calendars import (
    qCalendar,
    qBusinessDayConvention,
    _qCalendar,
    _qBusinessDayConvention,
    QL_BUSINESSDAYCONVENTION,
)

QL_DATEGENERATION_RULE = {
    "BACKWARD": ql.DateGeneration.Backward,
    "CDS": ql.DateGeneration.CDS,
    "CDS2015": ql.DateGeneration.CDS2015,
    "FORWARD": ql.DateGeneration.Forward,
    "OLDCDS": ql.DateGeneration.OldCDS,
    "THIRDWEDNESDAY": ql.DateGeneration.ThirdWednesday,
    "THIRDWEDNESDAYINCLUSIVE": ql.DateGeneration.ThirdWednesdayInclusive,
    "TWENTIETH": ql.DateGeneration.Twentieth,
    "TWENTIETHIMM": ql.DateGeneration.TwentiethIMM,
    "ZERO": ql.DateGeneration.Zero,
    UNKNOWN_KEY: UNKNOWN_VALUE,
}

def _qDateGenerationRule(rule : str) -> ql.DateGeneration:
    return QL_DATEGENERATION_RULE.get(rule.upper())

@xlo.converter()
def qDateGenerationRule(rule : str) -> ql.DateGeneration:
    return _qDateGenerationRule(rule)


@xlo.func(
    help='Create a QuantLib Schedule object.',
    args={
        'EffectiveDate': 'The effective date of the schedule.',
        'TerminationDate': 'The termination date of the schedule.',
        'Tenor': 'The tenor of the schedule.',
        'Calendar': 'The calendar to use for date adjustments.',
        'Convention': 'The business day convention to use for date adjustments.',
        'TerminationDateConvention': 'The business day convention to use for adjusting the termination date.',
        'DateGenerationRule': 'Backward, Forward, CDS, etc.',
        'EndOfMonth': 'Whether to adjust dates to the end of the month.',
        'FirstDate': 'The first date of the schedule (optional).',
        'LastDate': 'The last date of the schedule (optional).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSchedule(
    effectiveDate: qDate,
    terminationDate: qDate,
    tenor: qPeriod,
    calendar: qCalendar,
    convention: qBusinessDayConvention,
    terminationDateConvention: qBusinessDayConvention,
    dateGenerationRule: qDateGenerationRule,
    endOfMonth: bool,
    firstDate : qDate = ql.Date(),
    lastDate : qDate = ql.Date(),
    Trigger = None,
    ) -> ql.Schedule:
    return ql.Schedule(
        effectiveDate,
        terminationDate,
        tenor,
        calendar,
        convention,
        terminationDateConvention,
        dateGenerationRule,
        endOfMonth,
        firstDate,
        lastDate,
    )


@xlo.func(
    help='Create a QuantLib Schedule object from a list of dates.',
    args={
        'Dates': 'A list of dates to create the schedule from.',
        'Calendar': 'The calendar to use for date adjustments (optional). Default is NullCalendar.',
        'Convention': 'The business day convention to use for date adjustments (optional). Default is Unadjusted.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleFromDates(
        dates : xlo.Array(dims=1),
        calendar: qCalendar = ql.NullCalendar(),
        convention: qBusinessDayConvention = ql.Unadjusted,
        Trigger = None,
    ) -> ql.Schedule:
    _dates = [ ql.Date(round(d)) for d in dates ]
    _dates
    return ql.Schedule(
        _dates,
        calendar,
        convention,
    )

@xlo.func(
    help='Return the list of dates in a QuantLib Schedule.',
    args={
        'Schedule': 'The QuantLib Schedule to extract dates from.',
     },
     group=EXCEL_GROUP_NAME,
)
def qlScheduleDates(schedule : ql.Schedule, Trigger = None) -> list:
    return [ d for d in schedule.dates() ]


@xlo.func(
    help='Return the schedule date before a reference date.',
    args={
        'Schedule': 'QuantLib Schedule.',
        'RefDate': 'Reference date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSchedulePreviousDate(schedule : ql.Schedule, refDate : qDate, Trigger = None) -> qDate:
    return schedule.previousDate(refDate)


@xlo.func(
    help='Return the schedule date at or after a reference date.',
    args={
        'Schedule': 'QuantLib Schedule.',
        'RefDate': 'Reference date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleNextDate(schedule : ql.Schedule, refDate : qDate, Trigger = None) -> qDate:
    return schedule.nextDate(refDate)


@xlo.func(
    help='Return whether regularity flags are available for a QuantLib Schedule.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleHasIsRegular(schedule : ql.Schedule, Trigger = None) -> bool:
    return schedule.hasIsRegular()


@xlo.func(
    help='Return whether the i-th interval in a QuantLib Schedule is regular.',
    args={
        'Schedule': 'QuantLib Schedule.',
        'I': 'The interval index (one-based).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleIsRegular(schedule : ql.Schedule, i : int, Trigger = None) -> bool:
    return schedule.isRegular(i)


@xlo.func(
    help='Return regularity flags for all intervals in a QuantLib Schedule.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleIsRegular2(schedule : ql.Schedule, Trigger = None) -> list:
    return list(schedule.isRegular())


@xlo.func(
    help='Return the calendar used by a QuantLib Schedule.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleCalendar(schedule : ql.Schedule, Trigger = None) -> qCalendar:
    return schedule.calendar()


@xlo.func(
    help='Return the start date of a QuantLib Schedule.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleStartDate(schedule : ql.Schedule, Trigger = None) -> qDate:
    return schedule.startDate()


@xlo.func(
    help='Return the end date of a QuantLib Schedule.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleEndDate(schedule : ql.Schedule, Trigger = None) -> qDate:
    return schedule.endDate()


@xlo.func(
    help='Return whether a QuantLib Schedule has an associated tenor.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleHasTenor(schedule : ql.Schedule, Trigger = None) -> bool:
    return schedule.hasTenor()


@xlo.func(
    help='Return the tenor of a QuantLib Schedule.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleTenor(schedule : ql.Schedule, Trigger = None) -> qPeriod:
    return schedule.tenor()


@xlo.func(
    help='Return the business day convention of a QuantLib Schedule.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleBusinessDayConvention(schedule : ql.Schedule, Trigger = None) -> str:
    return first_key(QL_BUSINESSDAYCONVENTION, schedule.businessDayConvention(), UNKNOWN_VALUE)


@xlo.func(
    help='Return whether a QuantLib Schedule has a termination date convention.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleHasTerminationDateBusinessDayConvention(schedule : ql.Schedule, Trigger = None) -> bool:
    return schedule.hasTerminationDateBusinessDayConvention()


@xlo.func(
    help='Return the termination date business day convention of a QuantLib Schedule.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleTerminationDateBusinessDayConvention(schedule : ql.Schedule, Trigger = None) -> str:
    return first_key(QL_BUSINESSDAYCONVENTION, schedule.terminationDateBusinessDayConvention(), UNKNOWN_VALUE)


@xlo.func(
    help='Return whether a QuantLib Schedule has a date generation rule.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleHasRule(schedule : ql.Schedule, Trigger = None) -> bool:
    return schedule.hasRule()


@xlo.func(
    help='Return the date generation rule of a QuantLib Schedule.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleRule(schedule : ql.Schedule, Trigger = None) -> str:
    return first_key(QL_DATEGENERATION_RULE, schedule.rule(), UNKNOWN_VALUE)


@xlo.func(
    help='Return whether a QuantLib Schedule has an end-of-month flag.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleHasEndOfMonth(schedule : ql.Schedule, Trigger = None) -> bool:
    return schedule.hasEndOfMonth()


@xlo.func(
    help='Return the end-of-month flag of a QuantLib Schedule.',
    args={
        'Schedule': 'QuantLib Schedule.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleEndOfMonth(schedule : ql.Schedule, Trigger = None) -> bool:
    return schedule.endOfMonth()


@xlo.func(
    help='Return a QuantLib Schedule truncated after a date.',
    args={
        'Schedule': 'QuantLib Schedule.',
        'TruncationDate': 'Truncation date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleAfter(schedule : ql.Schedule, truncationDate : qDate, Trigger = None) -> ql.Schedule:
    return schedule.after(truncationDate)


@xlo.func(
    help='Return a QuantLib Schedule truncated until a date.',
    args={
        'Schedule': 'QuantLib Schedule.',
        'TruncationDate': 'Truncation date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlScheduleUntil(schedule : ql.Schedule, truncationDate : qDate, Trigger = None) -> ql.Schedule:
    return schedule.until(truncationDate)


@xlo.func(
    help='Create a QuantLib Schedule object with flexible arguments.',
    args={
        'EffectiveDate': 'The effective date of the schedule (optional).',
        'TerminationDate': 'The termination date of the schedule (optional).',
        'Tenor': 'The tenor of the schedule (optional).',
        'Frequency': 'The frequency of the schedule (optional).',
        'Calendar': 'The calendar to use for date adjustments (optional).',
        'Convention': 'The business day convention to use for date adjustments (optional).',
        'TerminationDateConvention': 'The business day convention to use for adjusting the termination date (optional).',
        'DateGenerationRule': 'Backward, Forward, CDS, etc. (optional).',
        'Forwards': 'Whether to generate dates forwards (optional).',
        'Backwards': 'Whether to generate dates backwards (optional).',
        'EndOfMonth': 'Whether to adjust dates to the end of the month (optional).',
        'FirstDate': 'The first date of the schedule (optional).',
        'NextToLastDate': 'The next-to-last date of the schedule (optional).',
    },
    group=EXCEL_GROUP_NAME,
)
def qlMakeSchedule(
    effectiveDate=None,
    terminationDate=None,
    tenor=None,
    frequency=None,
    calendar=None,
    convention=None,
    terminalDateConvention=None,
    rule=None,
    forwards=False,
    backwards=False,
    endOfMonth=None,
    firstDate=None,
    nextToLastDate=None,
    Trigger = None,
) -> ql.Schedule:
    # we cannot use converters for None defaults
    if effectiveDate is not None:
        effectiveDate = _qDate(effectiveDate)
    if terminationDate is not None:
        terminationDate = _qDate(terminationDate)
    if tenor is not None:
        tenor = _qPeriod(tenor)
    if frequency is not None:
        frequency = _qFrequency(frequency)
    if calendar is not None:
        calendar = _qCalendar(calendar)
    if convention is not None:
        convention = _qBusinessDayConvention(convention)
    if terminalDateConvention is not None:
        terminalDateConvention = _qBusinessDayConvention(terminalDateConvention)
    if rule is not None:
        rule = _qDateGenerationRule(rule)
    if forwards:
        forwards = bool(forwards)
    if backwards:
        backwards = bool(backwards)
    if endOfMonth is not None:
        endOfMonth = bool(endOfMonth)
    if firstDate is not None:
        firstDate = _qDate(firstDate)
    if nextToLastDate is not None:
        nextToLastDate = _qDate(nextToLastDate)
    return ql.MakeSchedule(
        effectiveDate,
        terminationDate,
        tenor,
        frequency,
        calendar,
        convention,
        terminalDateConvention,
        rule,
        forwards,
        backwards,
        endOfMonth,
        firstDate,
        nextToLastDate,
    )

