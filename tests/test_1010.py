import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1010-divisible-pairs/divisible-pairs.so')

@pytest.mark.parametrize("function", [c_lib.numPairsDivisibleBy60Naive,
                                      c_lib.numPairsDivisibleBy60Hash])
def test_divisible_pairs(function):
    array = [30,20,150,100,40]
    arr = (ctypes.c_int * len(array))(*array)
    out = function(arr, len(arr))
    assert out == 3
