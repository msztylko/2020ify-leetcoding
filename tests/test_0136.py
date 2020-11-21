import ctypes
import pytest

c_lib  = ctypes.CDLL('../solutions/0136-single-number/single-number.so')

@pytest.mark.parametrize('array, ans',
                        [([2,2,1], 1),
                         ([4,1,2,1,2], 4),
                         ([1], 1)])
def test_single_number(array, ans):
    # Transform Python array to C arr
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.singleNumber(arr, len(arr))
    assert out == ans
