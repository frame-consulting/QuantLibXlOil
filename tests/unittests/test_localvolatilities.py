import QuantLib as ql
import pytest

from quantlib_xloil import (
	qlBlackConstantVol,
	qlDate,
	qlDayCounter,
	qlFixedLocalVolSurface,
	qlFlatForward,
	qlLocalConstantVol,
	qlLocalVolSurface,
	qlNoExceptLocalVolSurface,
)
from quantlib_xloil.localvolatilities import _qFixedLocalVolSurfaceExtrapolation


def _reference_date() -> ql.Date:
	return qlDate(2024, 1, 2)


def _day_counter() -> ql.DayCounter:
	return qlDayCounter("ACTUAL365FIXED")


def _black_vol_handle(volatility: float = 0.20) -> ql.BlackVolTermStructureHandle:
	return qlBlackConstantVol(_reference_date(), ql.TARGET(), volatility, _day_counter())


def _flat_curve(rate: float) -> ql.YieldTermStructureHandle:
	return qlFlatForward(_reference_date(), rate, _day_counter())


def test_fixed_local_vol_surface_extrapolation_converter():
	assert _qFixedLocalVolSurfaceExtrapolation("constant") == ql.FixedLocalVolSurface.ConstantExtrapolation
	assert _qFixedLocalVolSurfaceExtrapolation("DEFAULT") == ql.FixedLocalVolSurface.InterpolatorDefaultExtrapolation

	with pytest.raises(ValueError, match="Cannot convert"):
		_qFixedLocalVolSurfaceExtrapolation("invalid")


def test_qlLocalConstantVol_returns_handle_with_constant_local_vol():
	local_vol = 0.25
	lvol_tsh = qlLocalConstantVol(_reference_date(), local_vol, _day_counter())

	assert isinstance(lvol_tsh, ql.LocalVolTermStructureHandle)
	assert lvol_tsh.currentLink() is not None
	assert lvol_tsh.localVol(qlDate(2024, 7, 2), 100.0, True) == pytest.approx(local_vol)
	assert lvol_tsh.localVol(0.5, 100.0, True) == pytest.approx(local_vol)


def test_qlLocalVolSurface_and_qlNoExceptLocalVolSurface_create_valid_handles():
	black_vol_tsh = _black_vol_handle(0.20)
	risk_free_ytsh = _flat_curve(0.03)
	dividend_ytsh = _flat_curve(0.01)
	underlying = ql.QuoteHandle(ql.SimpleQuote(100.0))

	lvol_surface = qlLocalVolSurface(black_vol_tsh, risk_free_ytsh, dividend_ytsh, underlying)
	noexcept_surface = qlNoExceptLocalVolSurface(black_vol_tsh, risk_free_ytsh, dividend_ytsh, underlying, 0.30)

	assert isinstance(lvol_surface, ql.LocalVolTermStructureHandle)
	assert isinstance(noexcept_surface, ql.LocalVolTermStructureHandle)
	assert lvol_surface.currentLink() is not None
	assert noexcept_surface.currentLink() is not None
	assert lvol_surface.localVol(qlDate(2024, 7, 2), 100.0, True) > 0.0
	assert noexcept_surface.localVol(qlDate(2024, 7, 2), 100.0, True) > 0.0


def test_qlFixedLocalVolSurface_returns_handle_and_matches_grid_knots():
	reference_date = _reference_date()
	day_counter = _day_counter()

	expiry1 = qlDate(2024, 7, 2)
	expiry2 = qlDate(2025, 1, 2)
	dates = [expiry1.serialNumber(), expiry2.serialNumber()]
	strikes = [80.0, 100.0, 120.0]
	local_vol_matrix = [
		[0.20, 0.21],
		[0.20, 0.22],
		[0.22, 0.23],
	]

	lvol_tsh = qlFixedLocalVolSurface(
		reference_date,
		dates,
		strikes,
		local_vol_matrix,
		day_counter,
		"LINEAR",
		_qFixedLocalVolSurfaceExtrapolation("CONSTANT"),
		_qFixedLocalVolSurfaceExtrapolation("DEFAULT"),
	)

	assert isinstance(lvol_tsh, ql.LocalVolTermStructureHandle)
	assert lvol_tsh.currentLink() is not None
	assert lvol_tsh.localVol(expiry1, strikes[0], True) == pytest.approx(local_vol_matrix[0][0])
	assert lvol_tsh.localVol(expiry2, strikes[1], True) == pytest.approx(local_vol_matrix[1][1])
