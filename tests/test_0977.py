import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0977-sorted-squares/sorted-squares.so')

@pytest.mark.skip(reason="how to check C allocated array?")
def test_sorted_squares():
    array = [-4,-1,0,3,10]
    arr = (ctypes.c_int * len(array))(*array)
    # out = (ctypes.c_int * len(array))(*array)
    arr_out = (ctypes.c_int * len(array))(*array)
    arr_out = c_lib.sortedSquares(arr, len(arr), arr_out)
    assert list(arr_out) == [0,1,9,16,100]
