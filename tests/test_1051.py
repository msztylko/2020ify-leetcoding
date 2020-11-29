import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1051-height-checker/height-checker.so')

@pytest.mark.parametrize('array, ans',
                        [([1,1,4,2,1,3], 3),
                         ([5,1,2,3,4], 5),
                         ([1,2,3,4,5], 0)])
def test_height_checker(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.heightChecker(arr, len(arr))
    assert out == ans
