import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1394-lucky-number/lucky-number.so')

@pytest.mark.parametrize('array, ans',
[([2,2,3,4], 2),
 ([1,2,2,3,3,3], 3),
 ([2,2,2,3,3], -1),
 ([5], -1),
 ([7,7,7,7,7,7,7], 7)])
def test_lucky_number(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.findLucky(arr, len(arr))
    assert out == ans
