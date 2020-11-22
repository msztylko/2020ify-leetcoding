import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0326-power-of-three/power-of-three.so')

@pytest.mark.parametrize('num, ans', [(27, True),
                                      (0, False),
                                      (9, True),
                                      (45, False)])
def test_power_of_three(num, ans):
    out = c_lib.isPowerOfThree(num)
    assert out == ans
