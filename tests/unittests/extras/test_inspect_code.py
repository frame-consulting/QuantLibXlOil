import pytest

from quantlib_xloil.extras import inspect_code


@pytest.fixture(autouse=True)
def reset_inspection_registries():
    inspect_code.QL_DICTIONARIES = {}
    inspect_code.QL_FUNCTIONS = {}
    yield
    inspect_code.QL_DICTIONARIES = {}
    inspect_code.QL_FUNCTIONS = {}


def test_initialise_lists_discovers_dictionaries_and_functions():
    inspect_code._intitialise_lists()

    assert "QL_CALENDAR" in inspect_code.QL_DICTIONARIES
    assert "qlCalendar" in inspect_code.QL_FUNCTIONS
    assert inspect_code.QL_DICTIONARIES["QL_CALENDAR"].startswith(
        inspect_code._url_to_blob
    )
    assert inspect_code.QL_FUNCTIONS["qlCalendar"].endswith("calendars.py#L180")


def test_initialise_lists_is_idempotent():
    inspect_code._intitialise_lists()
    dictionaries = inspect_code.QL_DICTIONARIES
    functions = inspect_code.QL_FUNCTIONS

    inspect_code._intitialise_lists()

    assert inspect_code.QL_DICTIONARIES is dictionaries
    assert inspect_code.QL_FUNCTIONS is functions


def test_dictionary_entries_returns_sorted_values_without_unknown_key():
    inspect_code._intitialise_lists()

    entries = inspect_code._dictionary_entries("QL_CALENDAR")
    keys = [entry[0] for entry in entries]

    assert keys == sorted(keys)
    assert ["UNKNOWN", "-1"] not in entries
    assert ["TARGET", "<class 'QuantLib.QuantLib.TARGET'>"] in entries


def test_dictionary_entries_rejects_unknown_dictionary():
    inspect_code._intitialise_lists()

    with pytest.raises(ValueError, match="Dictionary DOES_NOT_EXIST not found"):
        inspect_code._dictionary_entries("DOES_NOT_EXIST")


def test_list_dictionaries_supports_links_and_header():
    result = inspect_code.qlListDictionaries(with_links=True, with_header=True)

    assert result[0] == ["Dictionary Name", "Link"]
    assert result[1][0] == sorted(row[0] for row in result[1:])[0]
    assert result[1][1].startswith(inspect_code._url_to_blob)


def test_list_functions_without_links_returns_single_column():
    result = inspect_code.qlListFunctions(with_links=False, with_header=True)

    assert result[0] == ["Function Name"]
    assert all(len(row) == 1 for row in result[1:])
    assert ["qlCalendar"] in result


def test_list_dictionary_entries_supports_values_and_header():
    result = inspect_code.qlListDictionaryEntries(
        "QL_RATE_AVERAGING_TYPE", with_values=True, with_header=True
    )

    assert result[0] == ["Key", "Value"]
    assert ["COMPOUND", "1"] in result


def test_list_dictionary_entries_without_values_returns_keys_only():
    result = inspect_code.qlListDictionaryEntries(
        "QL_RATE_AVERAGING_TYPE", with_values=False, with_header=False
    )

    assert all(len(row) == 1 for row in result)
    assert ["COMPOUND"] in result
