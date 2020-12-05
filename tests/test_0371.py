import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0371-sum-two-integers/sum-two-integers.so')

@pytest.mark.parametrize('a, b, ans',
                        [(1, 2, 3),
                         (-2, 3, 1)])
def test_sum_two_integers(a, b, ans):
    out = c_lib.getSum(a, b)
    assert out == ans
