import QuantLib as ql
import pytest

import quantlib_xloil
from quantlib_xloil import bondfunctions as bf
from quantlib_xloil.cashflows import qDurationType
from quantlib_xloil.date import qFrequency
from quantlib_xloil.termstructures import qCompounding


@pytest.fixture
def bond_data():
    settings = ql.Settings.instance()
    previous_date = settings.evaluationDate
    settings.evaluationDate = ql.Date(15, 3, 2025)
    day_counter = ql.Actual365Fixed()
    schedule = ql.Schedule(
        ql.Date(1, 1, 2025),
        ql.Date(1, 1, 2030),
        ql.Period(ql.Semiannual),
        ql.NullCalendar(),
        ql.Unadjusted,
        ql.Unadjusted,
        ql.DateGeneration.Backward,
        False,
    )
    bond = ql.FixedRateBond(2, 100.0, schedule, [0.05], day_counter)
    curve = ql.YieldTermStructureHandle(
        ql.FlatForward(settings.evaluationDate, 0.03, day_counter)
    )
    yield bond, curve, day_counter
    settings.evaluationDate = previous_date


def test_start_date(bond_data):
    bond, _, _ = bond_data
    assert bf.qlBondFunctionsStartDate(bond) == ql.Date(1, 1, 2025)
    assert quantlib_xloil.qlBondFunctionsStartDate is bf.qlBondFunctionsStartDate


@pytest.mark.parametrize(
    "wrapper,method",
    [
        (bf.qlBondFunctionsIsTradable, "isTradable"),
        (bf.qlBondFunctionsPreviousCashFlowAmount, "previousCashFlowAmount"),
        (bf.qlBondFunctionsNextCashFlowAmount, "nextCashFlowAmount"),
        (bf.qlBondFunctionsAccrualStartDate, "accrualStartDate"),
        (bf.qlBondFunctionsAccrualEndDate, "accrualEndDate"),
        (bf.qlBondFunctionsAccrualPeriod, "accrualPeriod"),
        (bf.qlBondFunctionsAccrualDays, "accrualDays"),
        (bf.qlBondFunctionsAccruedPeriod, "accruedPeriod"),
        (bf.qlBondFunctionsAccruedDays, "accruedDays"),
    ],
)
def test_date_dependent_functions(bond_data, wrapper, method):
    bond, _, _ = bond_data
    quantlib_function = getattr(ql.BondFunctions, method)
    date = ql.Date(15, 9, 2025)
    assert wrapper(bond) == quantlib_function(bond)
    assert wrapper(bond, date) == quantlib_function(bond, date)


def test_tradability_after_maturity(bond_data):
    bond, _, _ = bond_data
    assert not bf.qlBondFunctionsIsTradable(bond, ql.Date(2, 1, 2030))


@pytest.mark.parametrize(
    "wrapper,method",
    [
        (bf.qlBondFunctionsCleanPriceFromCurve, "cleanPrice"),
        (bf.qlBondFunctionsDirtyPriceFromCurve, "dirtyPrice"),
        (bf.qlBondFunctionsBpsFromCurve, "bps"),
    ],
)
def test_curve_functions(bond_data, wrapper, method):
    bond, curve, _ = bond_data
    quantlib_function = getattr(ql.BondFunctions, method)
    date = ql.Date(15, 9, 2025)
    assert wrapper(bond, curve) == pytest.approx(
        quantlib_function(bond, curve.currentLink())
    )
    assert wrapper(bond, curve, date) == pytest.approx(
        quantlib_function(bond, curve.currentLink(), date)
    )


def test_atm_rate(bond_data):
    bond, curve, _ = bond_data
    date = ql.Date(15, 9, 2025)
    price = ql.BondPrice(98.0, ql.BondPrice.Clean)
    assert bf.qlBondFunctionsAtmRate(bond, curve) == pytest.approx(
        ql.BondFunctions.atmRate(bond, curve.currentLink())
    )
    assert bf.qlBondFunctionsAtmRate(bond, curve, date, price) == pytest.approx(
        ql.BondFunctions.atmRate(bond, curve.currentLink(), date, price)
    )


@pytest.mark.parametrize(
    "wrapper,method",
    [
        (bf.qlBondFunctionsBpsFromRate, "bps"),
        (bf.qlBondFunctionsConvexity, "convexity"),
        (bf.qlBondFunctionsBasisPointValue, "basisPointValue"),
        (bf.qlBondFunctionsYieldValueBasisPoint, "yieldValueBasisPoint"),
    ],
)
def test_yield_functions(bond_data, wrapper, method):
    bond, _, day_counter = bond_data
    compounding = qCompounding.__wrapped__("COMPOUNDED")
    frequency = qFrequency.__wrapped__("SEMIANNUAL")
    args = (bond, 0.04, day_counter, compounding, frequency)
    date = ql.Date(15, 9, 2025)
    quantlib_function = getattr(ql.BondFunctions, method)
    assert wrapper(*args) == pytest.approx(quantlib_function(*args))
    assert wrapper(*args, date) == pytest.approx(quantlib_function(*args, date))


def test_duration(bond_data):
    bond, _, day_counter = bond_data
    args = (bond, 0.04, day_counter, ql.Compounded, ql.Semiannual)
    date = ql.Date(15, 9, 2025)
    duration_type = qDurationType.__wrapped__("MACAULAY")
    assert bf.qlBondFunctionsDuration(*args) == pytest.approx(
        ql.BondFunctions.duration(*args)
    )
    assert bf.qlBondFunctionsDuration(*args, duration_type, date) == pytest.approx(
        ql.BondFunctions.duration(*args, duration_type, date)
    )


def test_z_spread_prices_and_round_trip(bond_data):
    bond, curve, _ = bond_data
    args = (bond, curve, 0.012, ql.Compounded, ql.Semiannual)
    quantlib_args = (bond, curve.currentLink(), 0.012, ql.Compounded, ql.Semiannual)
    date = ql.Date(15, 9, 2025)
    for wrapper, method in [
        (bf.qlBondFunctionsCleanPriceFromZSpread, "cleanPrice"),
        (bf.qlBondFunctionsDirtyPriceFromZSpread, "dirtyPrice"),
    ]:
        quantlib_function = getattr(ql.BondFunctions, method)
        assert wrapper(*args) == pytest.approx(quantlib_function(*quantlib_args))
        assert wrapper(*args, date) == pytest.approx(
            quantlib_function(*quantlib_args, date)
        )

    price = ql.BondPrice(
        bf.qlBondFunctionsCleanPriceFromZSpread(*args, date), ql.BondPrice.Clean
    )
    assert bf.qlBondFunctionsZSpread(
        bond, price, curve, ql.Compounded, ql.Semiannual, date, 1.0e-12, 200, 0.01
    ) == pytest.approx(0.012, abs=1.0e-10)
    default_price = ql.BondPrice(
        bf.qlBondFunctionsCleanPriceFromZSpread(*args), ql.BondPrice.Clean
    )
    assert bf.qlBondFunctionsZSpread(
        bond, default_price, curve, ql.Compounded, ql.Semiannual
    ) == pytest.approx(0.012, abs=1.0e-8)


def test_relinked_discount_curve(bond_data):
    bond, curve, day_counter = bond_data
    handle = ql.RelinkableYieldTermStructureHandle()
    handle.linkTo(curve.currentLink())
    original_price = bf.qlBondFunctionsCleanPriceFromCurve(bond, handle)
    new_curve = ql.FlatForward(ql.Settings.instance().evaluationDate, 0.06, day_counter)
    handle.linkTo(new_curve)
    new_price = bf.qlBondFunctionsCleanPriceFromCurve(bond, handle)
    assert new_price == pytest.approx(ql.BondFunctions.cleanPrice(bond, new_curve))
    assert new_price < original_price
