import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1137-tribonacci/tribonacci.so')

@pytest.mark.parametrize('num, ans',
                        [(4, 4),
                         (25, 1389537),
                         (37, 2082876103)])
@pytest.mark.parametrize('function', [c_lib.tribonacci, c_lib.tribonacci_array])
def test_tribonacci(num, ans, function):
    out = function(num)
    assert out == ans
