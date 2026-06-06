import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME


@xlo.func(
    help='Create a QuantLib TimeGrid.',
    args={
        'end_time': 'The end time of the grid.',
        'steps': 'The number of steps in the grid.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlTimeGrid(end_time: float, steps: int, trigger=None) -> ql.TimeGrid:
    return ql.TimeGrid(end_time, steps)


@xlo.func(
    help='Create a QuantLib TimeGrid from a list of times.',
    args={
        'times': 'The times to include in the grid.'
    },
    group=EXCEL_GROUP_NAME,
)
def qlTimeGridFromTimes(times: xlo.Array(dims=1), trigger=None) -> ql.TimeGrid:
    times_ = [float(t) for t in times]
    return ql.TimeGrid(times_)


@xlo.func(
    help='Create a QuantLib TimeGrid with mandatory times and a specified number of steps.',
    args={
        'mandatory_times': 'The mandatory times to include in the grid.',
        'steps': 'The number of steps in the grid.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlTimeGridWithMandatoryTimes(mandatory_times: xlo.Array(dims=1), steps: int, trigger=None) -> ql.TimeGrid:
    mandatory_times_ = [float(t) for t in mandatory_times]
    return ql.TimeGrid(mandatory_times_, steps)


@xlo.func(
    help='Return the times in a QuantLib TimeGrid.',
    args={
        'grid': 'The TimeGrid to get times from.'
    },
    group=EXCEL_GROUP_NAME,
)
def qlTimeGridTimes(grid: ql.TimeGrid, trigger=None) -> list[float]:
    return list(grid)
