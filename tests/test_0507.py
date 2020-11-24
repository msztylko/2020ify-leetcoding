import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0507-perfect-number/perfect-number.so')

@pytest.mark.parametrize('num, ans',
                        [(28, True),
                         (6, True),
                         (2, False)])
def test_perfect_number(num, ans):
    out = c_lib.checkPerfectNumber(num)
    assert out == ans
