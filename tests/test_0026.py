import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0026-duplicate-sorted/duplicate-sorted.so')

@pytest.mark.parametrize('array, ans',
[([1,1,2], 2),
 ([0,0,1,1,1,2,2,3,3,4], 5)])
def test_duplicate_sorted(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.removeDuplicates(arr, len(arr))
    assert out == ans
