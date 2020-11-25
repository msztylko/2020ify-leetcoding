import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0852-peak-index/peak-index.so')

@pytest.mark.parametrize('array, ans',
[([0,1,0], 1),
 ([0,2,1,0], 1),
 ([0,10,5,2], 1),
 ([3,4,5,1], 2),
 ([24,69,100,99,79,78,67,36,26,19], 2)])
def test_peak_index(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.peakIndexInMountainArray(arr, len(arr))
    assert out == ans
