import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0896-monotonic-array/monotonic-array.so')

@pytest.mark.parametrize('array, ans',
[([1,2,2,3], True),
 ([6,5,4,4], True),
 ([1,3,2], False),
 ([1,2,4,5], True),
 ([1,1,1], True)])
def test_monotonic_array(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.isMonotonic(arr, len(arr))
    assert out == ans
