import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0202-happy-number/happy-number.so')
@pytest.mark.parametrize('num, ans',
                        [(0, False),
                         (1, True),
                         (19, True)])
def test_is_happy(num, ans):
    out = c_lib.isHappy(num)
    assert out == ans
