import pytest
import sys

def division(a,b):
    return a/float(b)

#@pytest.mark.skipif(sys.version_info[0]==3, reason ="Only Python 2")
@pytest.mark.parametrize("a",[1,2,3,4])
def test_division_param(a):
    assert division(a,1) == a
