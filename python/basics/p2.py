import pytest


@pytest.fixture
def structure():
    class MyStruct(object):
        text = ""
        num = 10
    return MyStruct()

def test_fix(structure):
    assert isinstance(structure.text, str)
    assert isinstance(structure.num, float)
