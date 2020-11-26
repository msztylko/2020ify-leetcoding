import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1137-tribonacci/tribonacci.so')

@pytest.mark.parametrize('num, ans',
                        [(4, 4),
                         (25, 1389537),
                         (37, 2082876103)])
def test_tribonacci(num, ans):
    out = c_lib.tribonacci(num)
    assert out == ans
