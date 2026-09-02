# Volatilities Wrapper Progress

- Interface: `volatilities.i`; source pinned to QuantLib/SWIG `v1.42.1`.
- Branch: `wip/add-more-volatilities`.
- Environment commands must run in CMD:
  `cmd.exe /d /c 'call C:\ProgramData\miniconda3\Scripts\activate.bat && conda activate xloil && ...'`.

## Completed Commits

- `3f943f6` BlackVarianceSurface wrapper.
- `68060a0` SABR utilities, simple smiles, ConstantYoYOptionletVolatility, SpreadedSwaptionVolatility.
- `b680073` SmileSection accessors/evaluators.
- `fb393fc` Four time-based interpolated smile sections.
- `3954208` KahaleSmileSection.
- `27a7841` SABRInterpolation.
- `49672f9` HestonBlackVolSurface.
- `54064b1` SviInterpolatedSmileSection.
- `88d50b4` NoArbSabrInterpolatedSmileSection.
- `a1c7176` Four ZABR smile wrappers; `ZabrFullFdSmileSection` remains imported but commented out in its test because it takes too long.
- `619cb5a` PiecewiseBlackVarianceSurface `makeFromGrid` wrapper.
- `e91dc71` BlackVolatilitySurfaceDelta with delta/ATM/interpolation enum converters. It delegates advanced optional parameters to QuantLib because SWIG rejects Python `None` for optional delta enums.
- `ce14dcf` InterpolatedSwaptionVolatilityCube and nested quote-handle matrix helper.

## Latest Focused Validation

- `pytest tests\unittests\test_volatilities.py -v`: 37 passed after `ce14dcf`.
- The full-FD ZABR constructor is excluded only from the looped ZABR test by a commented line.

## Remaining Interface Work

- `SabrSwaptionVolatilityCube` and `ZabrSwaptionVolatilityCube`.
- Four calibrated ZABR interpolated smile-section variants.
- `AndreasenHugeVolatilityInterpl` and its Black/local-vol adapters.
- `CmsMarket`, `CmsMarketCalibration`.

## SABR Cube Investigation

- Constructor accepts a 2x2 tenor grid, `volSpreads` as four rows of QuoteHandle vectors, `parametersGuess` as four rows of `[alpha, beta, nu, rho]` QuoteHandles, and fixed-parameter flags.
- Evaluation requires historical fixings for both 5Y and 10Y `EuriborSwapIsdaFixA` indexes at all option dates (Jan 2 2025 and Jan 2 2026 in the explored fixture).
- With provisional fixed parameters `[0.02, 0.5, 0.3, -0.2]` and spreads `+/-0.01`, evaluation fails calibration tolerance. Use SABR-consistent volatility spreads/parameters or allow calibration and establish a stable fixture before adding the wrapper.
