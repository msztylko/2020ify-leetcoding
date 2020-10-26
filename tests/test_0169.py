import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0169-majority-element/majority-element.so')

@pytest.mark.parametrize("function", [c_lib.majorityElementBF, c_lib.majorityElementLC])
def test_majority_element_brute_force(function):
    array = [2,2,1,1,1,2,2]
    # Cast whole array to C integers
    arr = (ctypes.c_int * len(array))(*array)
    out = function(arr, len(arr))
    assert out == 2
