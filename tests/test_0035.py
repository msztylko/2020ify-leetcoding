import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0035-search-insert/search-insert.so')

@pytest.mark.parametrize('array, target, ans',
                        [([1,3,5,6], 5, 2),
                         ([1,3,5,6], 2, 1),
                         ([1,3,5,6], 7, 4),
                         ([1,3,5,6], 0, 0),
                         ([1], 0, 0)])
def test_search_insert(array, target, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.searchInsert(arr, len(arr), target)
    assert out == ans
