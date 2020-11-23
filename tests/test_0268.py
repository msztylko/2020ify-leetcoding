import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0268-missing-number/missing-number.so')

@pytest.mark.parametrize('array, ans', 
                        [([3,0,1], 2),
                         ([0,1], 2),
                         ([9,6,4,2,3,5,7,0,1], 8),
                         ([0], 1)])
def test_missing_number(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.missingNumber(arr, len(arr))
    assert out == ans
