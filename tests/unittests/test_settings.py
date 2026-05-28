import QuantLib as ql

from quantlib_xloil.settings import (
	qlSettingsAnchorEvaluationDate,
	qlSettingsGetEnforcesTodaysHistoricFixings,
	qlSettingsGetEvaluationDate,
	qlSettingsGetIncludeReferenceDateEvents,
	qlSettingsGetIncludeTodaysCashFlows,
	qlSettingsResetEvaluationDate,
	qlSettingsSetEnforcesTodaysHistoricFixings,
	qlSettingsSetEvaluationDate,
	qlSettingsSetIncludeReferenceDateEvents,
	qlSettingsSetIncludeTodaysCashFlows,
)


def test_qlSettingsGetSetEvaluationDate():
	original = ql.Settings.instance().evaluationDate
	try:
		target = ql.Date(15, 1, 2026)
		result = qlSettingsSetEvaluationDate(target)

		assert isinstance(result, ql.Date)
		assert result == target
		assert qlSettingsGetEvaluationDate() == target
	finally:
		ql.Settings.instance().evaluationDate = original


def test_qlSettingsGetSetEnforcesTodaysHistoricFixings():
	original = ql.Settings.instance().enforcesTodaysHistoricFixings
	try:
		assert qlSettingsSetEnforcesTodaysHistoricFixings(True) is True
		assert qlSettingsGetEnforcesTodaysHistoricFixings() is True

		assert qlSettingsSetEnforcesTodaysHistoricFixings(False) is False
		assert qlSettingsGetEnforcesTodaysHistoricFixings() is False
	finally:
		ql.Settings.instance().enforcesTodaysHistoricFixings = original


def test_qlSettingsGetSetIncludeReferenceDateEvents():
	original = ql.Settings.instance().includeReferenceDateEvents
	try:
		assert qlSettingsSetIncludeReferenceDateEvents(True) is True
		assert qlSettingsGetIncludeReferenceDateEvents() is True

		assert qlSettingsSetIncludeReferenceDateEvents(False) is False
		assert qlSettingsGetIncludeReferenceDateEvents() is False
	finally:
		ql.Settings.instance().includeReferenceDateEvents = original


def test_qlSettingsGetSetIncludeTodaysCashFlows():
	original = ql.Settings.instance().includeTodaysCashFlows
	try:
		assert qlSettingsSetIncludeTodaysCashFlows(True) is True
		assert qlSettingsGetIncludeTodaysCashFlows() is True

		assert qlSettingsSetIncludeTodaysCashFlows(False) is False
		assert qlSettingsGetIncludeTodaysCashFlows() is False
	finally:
		ql.Settings.instance().includeTodaysCashFlows = original


def test_qlSettingsAnchorEvaluationDate_and_ResetEvaluationDate():
    original = ql.Settings.instance().evaluationDate
    try:
        target = ql.Date(15, 1, 2026)
        new_date = qlSettingsSetEvaluationDate(target)
        assert new_date == target

        assert qlSettingsAnchorEvaluationDate()
        assert qlSettingsResetEvaluationDate()

    finally:
        ql.Settings.instance().evaluationDate = original

