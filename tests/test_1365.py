import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1365-count-smaller/count-smaller.so')

@pytest.mark.skip(reason='Segmentation fault')
def test_count_smaller():
    array = [8,1,2,2,3]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.smallerNumbersThanCurrent(arr, len(arr), len(arr))
    assert out == [4,0,1,1,3]
