import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1512-good-pair/good-pair.so')

@pytest.mark.parametrize('function', [c_lib.numIdenticalPairsSpace,
                                      c_lib.numIdenticalPairsTime])
def test_good_pair(function):
    array = [1,2,3,1,1,3]
    arr = (ctypes.c_int * len(array))(*array)
    out = function(arr, len(arr))
    assert out == 4
