from quantlib_xloil import qlHexVersion, qlVersion, qlXlOilVersion

from quantlib_xloil.__about__ import __version__


def test_qlVersion():

    version = qlVersion()
    assert isinstance(version, str)
    assert len(version) > 0


def test_qlHexVersion():
    hex_version = qlHexVersion()
    assert isinstance(hex_version, int)
    assert hex_version > 0


def test_qlXlOilVersion():
    ql_xl_oil_version = qlXlOilVersion()
    assert isinstance(ql_xl_oil_version, str)
    assert len(ql_xl_oil_version) > 0
    assert ql_xl_oil_version == __version__
    # check and compare with QuantLib version
    version_parts = ql_xl_oil_version.split(".")
    ql_version_parts = qlVersion().split(".")
    assert len(version_parts) == 3
    assert version_parts[0] == "0"  # major version should be 0 for now
    assert version_parts[1] == ql_version_parts[1]  # minor version
    #
    # We impose a safeguard to accidental minor version change.
    # See the comments in __about__.py.
    # This test should be updated manually when the minor version is changed.
    assert version_parts[1] == "41"
