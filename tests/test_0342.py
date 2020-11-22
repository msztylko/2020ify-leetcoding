import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0342-power-of-four/power-of-four.so')

@pytest.mark.parametrize('num, ans', [(16, True),
                                      (5, False),
                                      (1, True)])
def test_power_of_four(num, ans):
    out = c_lib.isPowerOfFour(num)
    assert out == ans
