import QuantLib as ql
import pytest

from quantlib_xloil.extras.cashflows_analysis import (
    QL_CASH_FLOW_COLUMN,
    _cashflow_analysis,
    _table,
    qlCashFlowsAnalysisColumns,
)


def _fixed_rate_leg():
    calendar = ql.TARGET()
    start = ql.Date(1, ql.January, 2024)
    end = ql.Date(1, ql.January, 2025)
    schedule = ql.Schedule(
        start,
        end,
        ql.Period(ql.Annual),
        calendar,
        ql.Unadjusted,
        ql.Unadjusted,
        ql.DateGeneration.Forward,
        False,
    )
    return ql.FixedRateLeg(schedule, ql.Actual365Fixed(), [1000.0], [0.05])


def test_cashflow_analysis_columns_contains_expected_keys():
    columns = qlCashFlowsAnalysisColumns()

    assert "AMOUNT" in columns
    assert "DATE" in columns
    assert "RATE" in columns
    assert "NOMINAL" in columns
    assert "NPV" in columns
    assert len(columns) == len(QL_CASH_FLOW_COLUMN)


def test_table_helper_formats_rows_with_header():
    rows = [
        {"AMOUNT": 10.0, "DATE": "2024-01-01"},
        {"AMOUNT": 20.0, "DATE": "2024-02-01"},
    ]

    table = _table(rows, with_header=True)

    assert table == [["AMOUNT", "DATE"], [10.0, "2024-01-01"], [20.0, "2024-02-01"]]


def test_cashflow_analysis_returns_expected_coupon_values():
    leg = list(_fixed_rate_leg())

    result = _cashflow_analysis(leg, ["AMOUNT", "DATE", "RATE", "NOMINAL"], None)

    assert len(result) == 1
    assert result[0]["AMOUNT"] == pytest.approx(50.136986301369866)
    assert result[0]["DATE"] == ql.Date(2, ql.January, 2025)
    assert result[0]["RATE"] == pytest.approx(0.05)
    assert result[0]["NOMINAL"] == pytest.approx(1000.0)


def test_cashflow_analysis_invalid_column_raises_value_error():
    with pytest.raises(ValueError, match="Invalid column"):
        _cashflow_analysis(list(_fixed_rate_leg()), ["NOT_A_REAL_COLUMN"], None)
