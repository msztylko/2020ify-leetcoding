import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1207-unique-number/unique-number.so')

@pytest.mark.parametrize('array, ans',
                        [([1,2,2,1,1,3], True),
                         ([1,2], False),
                         ([-3,0,1,-3,1,1,1,-3,10,0], True)])
def test_unique_number(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.uniqueOccurrences(arr, len(arr))
    assert out == ans
