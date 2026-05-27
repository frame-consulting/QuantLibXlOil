import QuantLib as ql

from quantlib_xloil.scheduler import (
	_qDateGenerationRule,
	qDateGenerationRule,
	qlMakeSchedule,
	qlSchedule,
	qlScheduleAfter,
	qlScheduleBusinessDayConvention,
	qlScheduleCalendar,
	qlScheduleDates,
	qlScheduleEndDate,
	qlScheduleEndOfMonth,
	qlScheduleFromDates,
	qlScheduleHasEndOfMonth,
	qlScheduleHasIsRegular,
	qlScheduleHasRule,
	qlScheduleHasTenor,
	qlScheduleHasTerminationDateBusinessDayConvention,
	qlScheduleIsRegular,
	qlScheduleIsRegular2,
	qlScheduleNextDate,
	qlSchedulePreviousDate,
	qlScheduleRule,
	qlScheduleStartDate,
	qlScheduleTenor,
	qlScheduleTerminationDateBusinessDayConvention,
	qlScheduleUntil,
)


def _sample_schedule() -> ql.Schedule:
	return qlSchedule(
		ql.Date(1, 1, 2024),
		ql.Date(1, 1, 2025),
		ql.Period("3M"),
		ql.TARGET(),
		ql.Following,
		ql.Following,
		ql.DateGeneration.Forward,
		False,
	)


def test_qDateGenerationRule():
	assert _qDateGenerationRule("Forward") == ql.DateGeneration.Forward
	assert _qDateGenerationRule("cds") == ql.DateGeneration.CDS


def test_qlSchedule_constructor_and_qlScheduleDates():
	schedule = _sample_schedule()
	dates = qlScheduleDates(schedule)
	assert isinstance(schedule, ql.Schedule)
	assert len(dates) > 2
	assert dates[0] == ql.Date(2, 1, 2024) # New Year's Day
	assert dates[-1] == ql.Date(2, 1, 2025)


def test_qlScheduleFromDates():
	source_dates = [
		ql.Date(1, 1, 2024).serialNumber(),
		ql.Date(1, 4, 2024).serialNumber(),
		ql.Date(1, 7, 2024).serialNumber(),
	]
	schedule = qlScheduleFromDates(source_dates)
	dates = qlScheduleDates(schedule)
	assert dates == [ql.Date(1, 1, 2024), ql.Date(1, 4, 2024), ql.Date(1, 7, 2024)]


def test_qlSchedulePreviousDate_and_qlScheduleNextDate():
	schedule = _sample_schedule()
	ref_date = ql.Date(15, 5, 2024)

	previous_date = qlSchedulePreviousDate(schedule, ref_date)
	next_date = qlScheduleNextDate(schedule, ref_date)

	assert previous_date <= ref_date
	assert next_date >= ref_date
	assert previous_date < next_date


def test_qlScheduleHasIsRegular_and_qlScheduleIsRegular_and_qlScheduleIsRegular2():
	schedule = _sample_schedule()
	regular_flags = qlScheduleIsRegular2(schedule)

	assert qlScheduleHasIsRegular(schedule) is True
	assert len(regular_flags) == len(schedule) - 1
	assert all(isinstance(flag, bool) for flag in regular_flags)
	assert qlScheduleIsRegular(schedule, 1) is True


def test_qlScheduleCalendar_and_start_end_dates():
	schedule = _sample_schedule()

	calendar = qlScheduleCalendar(schedule)
	start_date = qlScheduleStartDate(schedule)
	end_date = qlScheduleEndDate(schedule)

	assert isinstance(calendar, ql.Calendar)
	assert calendar.name() == ql.TARGET().name()
	assert start_date == ql.Date(2, 1, 2024)
	assert end_date == ql.Date(2, 1, 2025)


def test_qlScheduleHasTenor_and_qlScheduleTenor():
	schedule = _sample_schedule()

	assert qlScheduleHasTenor(schedule) is True
	assert qlScheduleTenor(schedule) == ql.Period("3M")


def test_qlScheduleBusinessDayConvention():
	schedule = _sample_schedule()
	assert qlScheduleBusinessDayConvention(schedule) == "FOLLOWING"


def test_qlScheduleTerminationDateBusinessDayConvention_and_has_flag():
	schedule = _sample_schedule()
	assert qlScheduleHasTerminationDateBusinessDayConvention(schedule) is True
	assert qlScheduleTerminationDateBusinessDayConvention(schedule) == "FOLLOWING"


def test_qlScheduleHasRule_and_qlScheduleRule():
	schedule = _sample_schedule()
	assert qlScheduleHasRule(schedule) is True
	assert qlScheduleRule(schedule) == "FORWARD"


def test_qlScheduleHasEndOfMonth_and_qlScheduleEndOfMonth():
	schedule = _sample_schedule()
	assert qlScheduleHasEndOfMonth(schedule) is True
	assert qlScheduleEndOfMonth(schedule) is False


def test_qlScheduleAfter_and_qlScheduleUntil():
	schedule = _sample_schedule()

	after_schedule = qlScheduleAfter(schedule, ql.Date(15, 5, 2024))
	until_schedule = qlScheduleUntil(schedule, ql.Date(15, 5, 2024))

	assert isinstance(after_schedule, ql.Schedule)
	assert isinstance(until_schedule, ql.Schedule)
	assert after_schedule.startDate() >= ql.Date(15, 5, 2024)
	assert until_schedule.endDate() <= ql.Date(15, 5, 2024)


def test_qlMakeSchedule_with_string_inputs():
	schedule = qlMakeSchedule(
		effectiveDate=ql.Date(1, 1, 2024).serialNumber(),
		terminationDate=ql.Date(1, 1, 2025).serialNumber(),
		tenor="3M",
		calendar="TARGET",
		convention="FOLLOWING",
		terminalDateConvention="PRECEDING",
		rule="FORWARD",
		endOfMonth=False,
	)

	assert isinstance(schedule, ql.Schedule)
	assert schedule.startDate() == ql.Date(2, 1, 2024)
	assert schedule.endDate() == ql.Date(31, 12, 2024)

