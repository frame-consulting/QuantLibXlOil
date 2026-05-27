import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .date import qDate

@xlo.func(
    help="Get the current evaluation date from QuantLib settings.",
    group=EXCEL_GROUP_NAME,
)
def qlSettingsGetEvaluationDate(trigger = None) -> ql.Date:
    return ql.Settings.instance().evaluationDate

@xlo.func(
    help="Set the evaluation date in QuantLib settings.",
    args={
        'Date': 'New evaluation date.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSettingsSetEvaluationDate(date: qDate, trigger = None) -> ql.Date:
    ql.Settings.instance().evaluationDate = date
    return ql.Settings.instance().evaluationDate

@xlo.func(
    help="Get whether QuantLib settings enforces today's historic fixings.",
    group=EXCEL_GROUP_NAME,
)
def qlSettingsGetEnforcesTodaysHistoricFixings(trigger = None) -> bool:
    return ql.Settings.instance().enforcesTodaysHistoricFixings

@xlo.func(
    help="Set whether QuantLib settings enforces today's historic fixings.",
    args={
        'Enforces': 'Whether to enforce today\'s historic fixings.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSettingsSetEnforcesTodaysHistoricFixings(enforces: bool, trigger = None) -> bool:
    ql.Settings.instance().enforcesTodaysHistoricFixings = enforces
    return ql.Settings.instance().enforcesTodaysHistoricFixings

@xlo.func(
    help="Get whether QuantLib settings include reference date events.",
    group=EXCEL_GROUP_NAME,
)
def qlSettingsGetIncludeReferenceDateEvents(trigger = None) -> bool:
    return ql.Settings.instance().includeReferenceDateEvents

@xlo.func(
    help="Set whether QuantLib settings include reference date events.",
    args={
        'Include': 'Whether to include reference date events.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSettingsSetIncludeReferenceDateEvents(include: bool, trigger = None) -> bool:
    ql.Settings.instance().includeReferenceDateEvents = include
    return ql.Settings.instance().includeReferenceDateEvents

@xlo.func(
    help="Get whether QuantLib settings include today's cash flows.",
    group=EXCEL_GROUP_NAME,
)
def qlSettingsGetIncludeTodaysCashFlows(trigger = None) -> bool:
    return ql.Settings.instance().includeTodaysCashFlows

@xlo.func(
    help="Set whether QuantLib settings include today's cash flows.",
    args={
        'Include': 'Whether to include today\'s cash flows.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlSettingsSetIncludeTodaysCashFlows(include: bool, trigger = None) -> bool:
    ql.Settings.instance().includeTodaysCashFlows = include
    return ql.Settings.instance().includeTodaysCashFlows

@xlo.func(
    help="Prevent the evaluation date to change at midnight. Useful when running calculations overnight and you want to keep the same evaluation date.",
    group=EXCEL_GROUP_NAME,
)
def qlSettingsAnchorEvaluationDate(trigger = None) -> ql.Date:
    ql.Settings.instance().anchorEvaluationDate()
    return ql.Settings.instance().evaluationDate

@xlo.func(
    help="Reset the evaluation date to today\s Date and allow it to change at midnight.",
    group=EXCEL_GROUP_NAME,
)
def qlSettingsResetEvaluationDate(trigger = None) -> ql.Date:
    ql.Settings.instance().resetEvaluationDate()
    return ql.Settings.instance().evaluationDate
