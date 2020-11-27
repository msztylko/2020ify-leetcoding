import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1550-consecutive-odd/consecutive-odd.so')

@pytest.mark.parametrize('array, ans',
                        [([2,6,4,1], False),
                         ([1,2,34,3,4,5,7,23,12], True)])
def test_consecutive_odd(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.threeConsecutiveOdds(arr, len(arr))
    assert out == ans
