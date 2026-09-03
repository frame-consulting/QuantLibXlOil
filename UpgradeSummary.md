# QuantLib Upgrade Summary

- **From Version**: `v1.42.1`
- **To Version**: `v1.43`

## SWIG Interface Changes
- Added: `None`
- Modified: `SWIG/basketoptions.i`, `SWIG/bonds.i`, `SWIG/calendars.i`, `SWIG/cashflows.i`, `SWIG/currencies.i`, `SWIG/date.i`, `SWIG/fdm.i`, `SWIG/indexes.i`, `SWIG/inflation.i`, `SWIG/optimizers.i`, `SWIG/ql.i`, `SWIG/ratehelpers.i`, `SWIG/spreaddiscountcurve.i`, `SWIG/stochasticprocess.i`, `SWIG/swap.i`, `SWIG/volatilities.i`
- Removed: `None`

## Wrapper Module Changes
- Added:
  - `src/quantlib_xloil/volatilities.py`: added `qlBlackVolTermStructureSmileSection`, `qlBlackVolTermStructureSmileSectionFromTime`, `qlBlackVolTermStructureAtmLevel` and related Black-volatility query wrappers for QuantLib 1.43
  - `src/quantlib_xloil/swap.py`: added cross-currency swap wrappers and the `DiscountingConstNotionalCrossCurrencySwapEngine` factory, including `qlConstNotionalCrossCurrencyFixedVsFloatingSwap`, `qlConstNotionalCrossCurrencyBasisSwap`, and in-currency leg accessors
- Modified:
  - `src/quantlib_xloil/calendars.py`: enabled `Croatia`, `Malta`, `Montenegro`, `NorthMacedonia`, `Serbia`, `Slovenia`, `Uzbekistan`; added `qlCalendarAddedHolidays`, `qlCalendarRemovedHolidays`
  - `src/quantlib_xloil/cashflows.py`: updated overnight coupon and overnight leg wrappers to match QuantLib 1.43 optional arguments (`ex_coupon_date`, rounding precision, etc.) and use `NullCalendar` instead of invalid generic `Calendar()` defaults
  - `src/quantlib_xloil/currencies.py`: added currency codes `MKD`, `UZS`
  - `src/quantlib_xloil/date.py`: added ECB wrappers `qlECBIsECBDate`, `qlECBIsECBCode`, `qlECBCode`, `qlECBDate`, `qlECBDateFromCode`, `qlECBNextDate`, `qlECBNextDateFromCode`, `qlECBNextDates`, `qlECBNextDatesFromCode`, `qlECBNextCode`, `qlECBNextCodeFromCode`
  - `src/quantlib_xloil/indexes.py`: added `qlBMAIndex`, `qlShir`, `qlZaronia`
  - `src/quantlib_xloil/optimizers.py`: added `qlLBFGSB`
  - `src/quantlib_xloil/ratehelpers.py`: added the full QuantLib 1.43 ratehelper surface, including `qlBMASwapRateHelper` and the additional basis/cross-currency helper wrappers used in the upgrade
  - `src/quantlib_xloil/stochasticprocess.py`: updated `qlG2Process` and `qlG2ForwardProcess` with optional forwarding term structure; added `qlG2ProcessPhi`, `qlG2ProcessShortRate`, `qlG2ForwardProcessPhi`, `qlG2ForwardProcessShortRate`
- Removed/Deprecated: `None`

## Test Changes
- Added:
  - `tests/unittests/test_volatilities.py`: added Black volatility regression coverage for the QuantLib 1.43 smile-section and ATM-level APIs
  - `tests/unittests/test_cashflows.py`: added overnight coupon/leg optional-argument regression coverage
  - `tests/unittests/test_swap.py`: added cross-currency swap smoke coverage and pricing-engine setup checks
- Modified:
  - `tests/unittests/test_calendars.py`
  - `tests/unittests/test_currencies.py`
  - `tests/unittests/test_date.py`
  - `tests/unittests/test_indexes.py`
  - `tests/unittests/test_optimizers.py`
  - `tests/unittests/test_ratehelpers.py`
  - `tests/unittests/test_stochasticprocess.py`
- Removed: `None`

## Validation Status
- `tests/unittests/test_volatilities.py`: passed (`19 passed`)
- `tests/unittests/test_cashflows.py`: passed (`15 passed`)
- `tests/unittests/test_ratehelpers.py`: passed (`11 passed`)
- `tests/unittests/test_swap.py`: passed (`11 passed`)
- Overall module-by-module upgrade status: complete for the modules updated in this pass under QuantLib 1.43
