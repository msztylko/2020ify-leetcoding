import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1534-count-triplets/count-triplets.so')

@pytest.mark.parametrize('array, a, b, c, ans',
                [([3,0,1,1,9,7], 7, 2, 3, 4),
                 ([1,1,2,2,3],   0, 0, 1, 0)])
def test_count_triplets(array, a, b, c, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.countGoodTriplets(arr, len(arr), a, b, c)
    assert out == ans
