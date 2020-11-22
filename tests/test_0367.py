import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0367-valid-perfect-square/valid-perfect-square.so')

@pytest.mark.parametrize('num, ans', [(0, False),
                                      (16, True),
                                      (14, False)])
def test_valid_perfect_square(num, ans):
    out = c_lib.isPerfectSquare(num)
    assert out == ans
