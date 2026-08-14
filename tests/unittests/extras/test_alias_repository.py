import datetime
import pytest

from quantlib_xloil.extras.alias_repository import (
    _normalised_alias,
    _alias_suffix,
    _envelope,
    _set,
    _get,
    _get_envelope,
    _delete,
    _get_repository,
    _clear_repository,
    _REPOSITORY,
    _ENV_ALIAS,
    _ENV_OBJ,
    _ENV_VERSION,
    _ENV_CREATED,
    _ENV_UPDATED,
    _ALIAS_DELIMITER,
)


class TestNormalisedKey:
    """Tests for _normalised_alias function."""

    def test_normalised_alias_basic(self):
        """Test basic alias normalization."""
        assert _normalised_alias("test") == "TEST"
        assert _normalised_alias("Test") == "TEST"
        assert _normalised_alias("TEST") == "TEST"

    def test_normalised_alias_with_whitespace(self):
        """Test alias normalization with whitespace."""
        assert _normalised_alias("  test  ") == "TEST"
        assert _normalised_alias(" test ") == "TEST"
        assert _normalised_alias("\ttest\t") == "TEST"

    def test_normalised_alias_with_delimiter(self):
        """Test alias normalization with delimiter."""
        assert _normalised_alias("test#1") == "TEST"
        assert _normalised_alias("test#0") == "TEST"
        assert _normalised_alias("TEST#99") == "TEST"

    def test_normalised_alias_type_error(self):
        """Test that non-string aliass raise TypeError."""
        with pytest.raises(TypeError, match="alias .* must be a string"):
            _normalised_alias(123)

        with pytest.raises(TypeError, match="alias .* must be a string"):
            _normalised_alias(None)

        with pytest.raises(TypeError, match="alias .* must be a string"):
            _normalised_alias(["test"])


class TestKeySuffix:
    """Tests for _alias_suffix function."""

    def test_alias_suffix_none(self):
        """Test aliass without suffix return None."""
        assert _alias_suffix("test") is None
        assert _alias_suffix("TEST") is None
        assert _alias_suffix("  test  ") is None

    def test_alias_suffix_valid(self):
        """Test aliass with valid suffixes."""
        assert _alias_suffix("test#1") == 1
        assert _alias_suffix("TEST#0") == 0
        assert _alias_suffix("test#99") == 99

    def test_alias_suffix_with_whitespace(self):
        """Test aliass with whitespace around suffix."""
        assert _alias_suffix("test#1") == 1
        assert _alias_suffix(" test # 1 ") == 1

    def test_alias_suffix_type_error(self):
        """Test that non-string aliass raise TypeError."""
        with pytest.raises(TypeError, match="alias .* must be a string"):
            _alias_suffix(123)

    def test_alias_suffix_too_many_parts(self):
        """Test aliass with too many parts raise ValueError."""
        with pytest.raises(
            ValueError, match="alias .* must be of the form 'name#suffix'"
        ):
            _alias_suffix("test#1#2")

    def test_alias_suffix_non_integer(self):
        """Test aliass with non-integer suffix raise ValueError."""
        with pytest.raises(ValueError, match="alias .* suffix must be an integer"):
            _alias_suffix("test#abc")

    def test_alias_suffix_negative(self):
        """Test aliass with negative suffix raise ValueError."""
        with pytest.raises(
            ValueError, match="alias .* suffix must be a non-negative integer"
        ):
            _alias_suffix("test#-1")


class TestEnvelope:
    """Tests for _envelope function."""

    def test_envelope_structure(self):
        """Test envelope has correct structure."""
        alias = "test"
        obj = {"data": "value"}

        env = _envelope(alias, obj)

        assert env[_ENV_ALIAS] == alias
        assert env[_ENV_OBJ] == obj
        assert env[_ENV_VERSION] == 0
        assert isinstance(env[_ENV_CREATED], datetime.datetime)
        assert isinstance(env[_ENV_UPDATED], datetime.datetime)

    def test_envelope_created_updated_same(self):
        """Test that a new envelope has valid creation and update timestamps."""
        env = _envelope("test", {"data": "value"})
        assert env[_ENV_CREATED] <= env[_ENV_UPDATED]


class TestSet:
    """Tests for _set function."""

    def setup_method(self):
        """Clear repository before each test."""
        _clear_repository()

    def teardown_method(self):
        """Clear repository after each test."""
        _clear_repository()

    def test_set_new_alias(self):
        """Test setting a new alias."""
        result = _set("test", {"data": "value"})

        assert "TEST" in _REPOSITORY
        assert _REPOSITORY["TEST"][_ENV_ALIAS] == "TEST"
        assert _REPOSITORY["TEST"][_ENV_OBJ] == {"data": "value"}
        assert _REPOSITORY["TEST"][_ENV_VERSION] == 0
        assert result == "TEST#0"

    def test_set_existing_alias_same_type(self):
        """Test updating an existing alias with same type."""
        _set("test", {"data": "value1"})
        result = _set("test", {"data": "value2"})

        assert _REPOSITORY["TEST"][_ENV_OBJ] == {"data": "value2"}
        assert _REPOSITORY["TEST"][_ENV_VERSION] == 1
        assert result == "TEST#1"

    def test_set_existing_alias_different_type(self):
        """Test updating an existing alias with different type raises TypeError."""
        _set("test", {"data": "value"})

        with pytest.raises(TypeError, match="Alias TEST already exists"):
            _set("test", ["list", "data"])

    def test_set_alias_normalization(self):
        """Test that aliass are normalized when set."""
        _set("  Test  ", {"data": "value"})

        assert "TEST" in _REPOSITORY
        assert "  Test  " not in _REPOSITORY

    def test_set_with_delimiter_in_alias(self):
        """Test setting with delimiter in alias."""
        result = _set("test#1", {"data": "value"})

        assert "TEST" in _REPOSITORY
        assert result == "TEST#0"  # Version is 0 for new entry


class TestGet:
    """Tests for _get function."""

    def setup_method(self):
        """Clear repository before each test."""
        _clear_repository()

    def teardown_method(self):
        """Clear repository after each test."""
        _clear_repository()

    def test_get_existing_alias(self):
        """Test getting an existing alias."""
        _set("test", {"data": "value"})
        result = _get("test")

        assert result == {"data": "value"}

    def test_get_existing_alias_case_insensitive(self):
        """Test getting with different case."""
        _set("test", {"data": "value"})
        result = _get("TEST")

        assert result == {"data": "value"}

    def test_get_with_version_suffix(self):
        """Test getting the current version by its versioned alias."""
        _set("test", {"data": "value1"})
        _set("test", {"data": "value2"})  # Version becomes 1

        result = _get("test#1")
        assert result == {"data": "value2"}

        with pytest.raises(KeyError, match="Key .* version .* not found in repository"):
            _get("test#0")

    def test_get_nonexistent_alias(self):
        """Test getting non-existent alias raises KeyError."""
        with pytest.raises(KeyError, match="Key .* not found in repository"):
            _get("nonexistent")

    def test_get_nonexistent_version(self):
        """Test getting non-existent version raises KeyError."""
        _set("test", {"data": "value"})

        with pytest.raises(KeyError, match="Key .* version .* not found in repository"):
            _get("test#5")


class TestGetEnvelope:
    """Tests for _get_envelope function."""

    def setup_method(self):
        """Clear repository before each test."""
        _clear_repository()

    def teardown_method(self):
        """Clear repository after each test."""
        _clear_repository()

    def test_get_envelope_existing_alias(self):
        """Test getting envelope for existing alias."""
        _set("test", {"data": "value"})
        result = _get_envelope("test")

        assert isinstance(result, list)
        assert len(result) == 5  # 5 fields in envelope

        # Convert to dict for easier testing
        env_dict = dict(result)
        assert env_dict[_ENV_ALIAS] == "TEST"
        assert env_dict[_ENV_OBJ] == {"data": "value"}
        assert env_dict[_ENV_VERSION] == 0

    def test_get_envelope_nonexistent_alias(self):
        """Test getting envelope for non-existent alias raises KeyError."""
        with pytest.raises(KeyError, match="Key .* not found in repository"):
            _get_envelope("nonexistent")

    def test_get_envelope_nonexistent_version(self):
        """Test getting envelope for non-existent version raises KeyError."""
        _set("test", {"data": "value"})

        with pytest.raises(KeyError, match="Key .* version .* not found in repository"):
            _get_envelope("test#5")


class TestDelete:
    """Tests for _delete function."""

    def setup_method(self):
        """Clear repository before each test."""
        _clear_repository()

    def teardown_method(self):
        """Clear repository after each test."""
        _clear_repository()

    def test_delete_existing_alias(self):
        """Test deleting an existing alias."""
        _set("test", {"data": "value"})
        result = _delete("test")

        assert result is True
        assert "TEST" not in _REPOSITORY

    def test_delete_nonexistent_alias(self):
        """Test deleting non-existent alias raises KeyError."""
        with pytest.raises(KeyError, match="Key .* not found in repository"):
            _delete("nonexistent")

    def test_delete_case_insensitive(self):
        """Test deleting with different case."""
        _set("test", {"data": "value"})
        result = _delete("TEST")

        assert result is True
        assert "TEST" not in _REPOSITORY


class TestGetRepository:
    """Tests for _get_repository function."""

    def setup_method(self):
        """Clear repository before each test."""
        _clear_repository()

    def teardown_method(self):
        """Clear repository after each test."""
        _clear_repository()

    def test_get_repository_empty(self):
        """Test getting empty repository."""
        result = _get_repository()

        assert isinstance(result, list)
        assert len(result) == 1  # Only header row
        assert result[0] == [
            _ENV_ALIAS,
            _ENV_OBJ,
            _ENV_VERSION,
            _ENV_CREATED,
            _ENV_UPDATED,
        ]

    def test_get_repository_with_items(self):
        """Test getting repository with items."""
        _set("test1", {"data": "value1"})
        _set("test2", {"data": "value2"})

        result = _get_repository()

        assert isinstance(result, list)
        assert len(result) == 3  # Header + 2 items

        # Check header
        assert result[0] == [
            _ENV_ALIAS,
            _ENV_OBJ,
            _ENV_VERSION,
            _ENV_CREATED,
            _ENV_UPDATED,
        ]

        # Check that our items are in there (order may vary)
        aliass = [row[0] for row in result[1:]]
        assert "TEST1" in aliass
        assert "TEST2" in aliass


class TestClearRepository:
    """Tests for _clear_repository function."""

    def setup_method(self):
        """Clear repository before each test."""
        _clear_repository()

    def test_clear_repository(self):
        """Test clearing repository."""
        _set("test1", {"data": "value1"})
        _set("test2", {"data": "value2"})

        result = _clear_repository()

        assert result is True
        assert len(_REPOSITORY) == 0

    def test_clear_repository_empty(self):
        """Test clearing empty repository."""
        result = _clear_repository()

        assert result is True
        assert len(_REPOSITORY) == 0


class TestIntegration:
    """Integration tests for object dictionary workflows."""

    def setup_method(self):
        """Clear repository before each test."""
        _clear_repository()

    def teardown_method(self):
        """Clear repository after each test."""
        _clear_repository()

    def test_full_workflow(self):
        """Test complete workflow: set, get, update, delete."""
        # Set initial value
        alias1 = _set("myalias", {"value": 42})
        assert alias1 == "MYALIAS#0"

        # Get value
        obj = _get("myalias")
        assert obj == {"value": 42}

        # Update value
        alias2 = _set("myalias", {"value": 43})
        assert alias2 == "MYALIAS#1"

        # Get updated value
        obj = _get("myalias")
        assert obj == {"value": 43}

        # Historical versions are not retained.
        with pytest.raises(KeyError):
            _get("myalias#0")

        # Delete
        result = _delete("myalias")
        assert result is True

        # Verify deleted
        with pytest.raises(KeyError):
            _get("myalias")

    def test_multiple_objects_different_types(self):
        """Test storing different types of objects."""
        _set("string_alias", "string_value")
        _set("int_alias", 42)
        _set("list_alias", [1, 2, 3])
        _set("dict_alias", {"nested": "value"})

        assert _get("string_alias") == "string_value"
        assert _get("int_alias") == 42
        assert _get("list_alias") == [1, 2, 3]
        assert _get("dict_alias") == {"nested": "value"}

    def test_type_mismatch_prevention(self):
        """Test that type mismatches are prevented."""
        _set("test", "string_value")

        # Should be able to update with same type
        _set("test", "another_string")

        # Should not be able to update with different type
        with pytest.raises(TypeError, match="Alias TEST already exists"):
            _set("test", 42)

        # Original value should still be there
        assert _get("test") == "another_string"

    def test_repository_table_structure(self):
        """Test that repository table has correct structure."""
        _set("test", {"data": "value"})

        repo = _get_repository()

        # Should have header and one data row
        assert len(repo) == 2

        # Header should have all required fields
        header = repo[0]
        assert _ENV_ALIAS in header
        assert _ENV_OBJ in header
        assert _ENV_VERSION in header
        assert _ENV_CREATED in header
        assert _ENV_UPDATED in header

        # Data row should have corresponding values
        data_row = repo[1]
        assert data_row[0] == "TEST"  # Key
        assert data_row[1] == {"data": "value"}  # Object
        assert data_row[2] == 0  # Version


class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def setup_method(self):
        """Clear repository before each test."""
        _clear_repository()

    def teardown_method(self):
        """Clear repository after each test."""
        _clear_repository()

    def test_empty_string_alias(self):
        """Test empty string alias."""
        result = _set("", {"data": "value"})
        assert result == "#0"

        obj = _get("")
        assert obj == {"data": "value"}

    def test_alias_with_only_delimiter(self):
        """Test alias that is only delimiter."""
        result = _set("#", {"data": "value"})
        assert result == "#0"

    def test_whitespace_only_alias(self):
        """Test whitespace only alias."""
        result = _set("   ", {"data": "value"})
        assert result == "#0"  # Empty after normalization

    def test_special_characters_in_alias(self):
        """Test aliass with special characters."""
        result = _set("test-alias_with.special$chars", {"data": "value"})
        assert result == "TEST-ALIAS_WITH.SPECIAL$CHARS#0"

        obj = _get("test-alias_with.special$chars")
        assert obj == {"data": "value"}

    def test_large_version_numbers(self):
        """Test with large version numbers."""
        for i in range(100):
            _set("test", {"version": i})

        # Should be able to get the latest version
        obj = _get("test")
        assert obj == {"version": 99}

        # Historical versions are not retained.
        with pytest.raises(KeyError):
            _get("test#50")

    def test_none_object(self):
        """Test storing None object."""
        _set("none_alias", None)
        obj = _get("none_alias")
        assert obj is None

    def test_object_with_none_values(self):
        """Test storing objects with None values."""
        _set("complex_alias", {"a": None, "b": "value", "c": None})
        obj = _get("complex_alias")
        assert obj == {"a": None, "b": "value", "c": None}
