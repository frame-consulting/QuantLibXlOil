import QuantLib as ql
import pytest

from quantlib_xloil.exercise import _qExerciseType
from quantlib_xloil import (
	qlAmericanExercise,
	qlBermudanExercise,
	qlDate,
	qlEuropeanExercise,
	qlExerciseDate,
	qlExerciseDateAt,
	qlExerciseDates,
	qlExerciseType,
	qlRebatedExercise,
	qlSwingExercise,
)


def test__qExerciseType_case_insensitive_and_passthrough():
	assert _qExerciseType("european") == ql.Exercise.European
	assert _qExerciseType(" BERMUDAN ") == ql.Exercise.Bermudan
	assert _qExerciseType(ql.Exercise.American) == ql.Exercise.American


def test_qlEuropeanExercise_and_accessors():
	exercise_date = qlDate(2025, 1, 15)
	exercise = qlEuropeanExercise(exercise_date)

	assert isinstance(exercise, ql.EuropeanExercise)
	assert qlExerciseType(exercise) == "EUROPEAN"
	assert qlExerciseDate(exercise, 0) == exercise_date
	assert qlExerciseDateAt(exercise, 0) == exercise_date
	assert qlExerciseDates(exercise) == [exercise_date.serialNumber()]


def test_qlBermudanExercise_converts_dates_and_reports_all_dates():
	d1 = qlDate(2025, 1, 15)
	d2 = qlDate(2025, 7, 15)
	dates = [d1.serialNumber() + 0.4, d2.serialNumber() + 0.6]

	exercise = qlBermudanExercise(dates)

	assert isinstance(exercise, ql.BermudanExercise)
	assert qlExerciseType(exercise) == "BERMUDAN"
	assert qlExerciseDate(exercise, 0) == ql.Date(round(dates[0]))
	assert qlExerciseDateAt(exercise, 1) == ql.Date(round(dates[1]))
	assert qlExerciseDates(exercise) == [round(dates[0]), round(dates[1])]


def test_qlAmericanExercise_has_two_boundary_dates():
	first_date = qlDate(2025, 1, 1)
	last_date = qlDate(2025, 12, 31)
	exercise = qlAmericanExercise(first_date, last_date)

	assert isinstance(exercise, ql.AmericanExercise)
	assert qlExerciseType(exercise) == "AMERICAN"
	assert qlExerciseDate(exercise, 0) == first_date
	assert qlExerciseDateAt(exercise, 1) == last_date
	assert qlExerciseDates(exercise) == [first_date.serialNumber(), last_date.serialNumber()]


def test_qlRebatedExercise_from_bermudan():
	d1 = qlDate(2025, 1, 15)
	d2 = qlDate(2025, 7, 15)
	bermudan = qlBermudanExercise([d1, d2])

	rebated = qlRebatedExercise(bermudan, [1.0, 2.0], 2)

	assert isinstance(rebated, ql.RebatedExercise)
	assert qlExerciseType(rebated) == "BERMUDAN"
	assert qlExerciseDates(rebated) == [d1.serialNumber(), d2.serialNumber()]


def test_qlRebatedExercise_rejects_rebate_vector_for_non_bermudan():
	european = qlEuropeanExercise(qlDate(2025, 1, 15))

	with pytest.raises(RuntimeError, match="bermudan"):
		qlRebatedExercise(european, [1.0], 2)


def test_qlSwingExercise_construction_and_dates():
	d1 = qlDate(2025, 2, 1)
	d2 = qlDate(2025, 3, 1)
	d3 = qlDate(2025, 4, 1)
	swing = qlSwingExercise([d1, d2, d3])

	assert isinstance(swing, ql.SwingExercise)
	assert qlExerciseType(swing) == "BERMUDAN"
	assert qlExerciseDate(swing, 0) == d1
	assert qlExerciseDates(swing) == [d1.serialNumber(), d2.serialNumber(), d3.serialNumber()]
