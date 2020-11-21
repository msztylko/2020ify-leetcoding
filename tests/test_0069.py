import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0069-sqrt/sqrt.so')

@pytest.mark.parametrize('num, ans', [(4,2), (8,2)])
def test_sqrt(num, ans):
    out = c_lib.mySqrt(num)
    assert out == ans
