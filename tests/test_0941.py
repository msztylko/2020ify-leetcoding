import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0941-mountain-array/mountain-array.so')

@pytest.mark.parametrize('array, ans',
                        [([2,1], False),
                         ([3,5,5], False),
                         ([0,3,2,1], True)])
def test_mountain_array(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.validMountainArray(arr, len(arr))
    assert out == ans
