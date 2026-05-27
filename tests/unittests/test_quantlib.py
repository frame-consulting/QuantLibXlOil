
def test_qlVersion():
    from quantlib_xloil import qlVersion
    version = qlVersion()
    assert isinstance(version, str)
    assert len(version) > 0

def test_qlHexVersion():
    from quantlib_xloil import qlHexVersion
    hex_version = qlHexVersion()
    assert isinstance(hex_version, int)
    assert hex_version > 0
