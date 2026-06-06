import QuantLib as ql
import pytest

from quantlib_xloil import (
	qlTimeGrid,
	qlTimeGridFromTimes,
	qlTimeGridTimes,
	qlTimeGridWithMandatoryTimes,
)


def test_qlTimeGrid_uniform_times_from_end_time_and_steps():
	grid = qlTimeGrid(1.0, 4)
	times = qlTimeGridTimes(grid)

	assert isinstance(grid, ql.TimeGrid)
	assert times == pytest.approx([0.0, 0.25, 0.5, 0.75, 1.0])


def test_qlTimeGridFromTimes_converts_sorts_and_deduplicates():
	grid = qlTimeGridFromTimes([1.0, "0.0", 0.5, 0.5])

	assert isinstance(grid, ql.TimeGrid)
	assert qlTimeGridTimes(grid) == pytest.approx([0.0, 0.5, 1.0])


def test_qlTimeGridWithMandatoryTimes_includes_mandatory_times():
	mandatory_times = [0.0, 0.7, 1.0]
	grid = qlTimeGridWithMandatoryTimes(mandatory_times, 4)
	times = qlTimeGridTimes(grid)

	assert isinstance(grid, ql.TimeGrid)
	assert len(times) == 5
	assert any(abs(t - 0.7) < 1e-12 for t in times)
	assert times[0] == pytest.approx(0.0)
	assert times[-1] == pytest.approx(1.0)


def test_qlTimeGridTimes_returns_plain_python_list():
	grid = qlTimeGridFromTimes([0.0, 0.3, 1.0])
	times = qlTimeGridTimes(grid)

	assert isinstance(times, list)
	assert all(isinstance(t, float) for t in times)


def test_qlTimeGridFromTimes_negative_time_raises():
	with pytest.raises(RuntimeError, match="negative times not allowed"):
		qlTimeGridFromTimes([-0.1, 0.0])
