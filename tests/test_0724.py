import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0724-pivot-index/pivot-index.so')

@pytest.mark.parametrize('array, ans',
                        [([1,7,3,6,5,6], 3),
                         ([1,2,3], -1)])
def test_pivot_index(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.pivotIndex(arr, len(arr))
    assert out == ans
