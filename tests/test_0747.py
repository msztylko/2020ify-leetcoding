import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0747-dominant-index/dominant-index.so')

@pytest.mark.parametrize('array, ans',
                        [([3, 6, 1, 0], 1),
                         ([1, 2, 3, 4], -1)])
def test_dominat_index(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.dominantIndex(arr, len(arr))
    assert out == ans
