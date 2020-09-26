import ctypes
import pytest

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0169-majority-element/majority-element.so'
c_lib = ctypes.CDLL(c_path)
c_lib.majorityElementBF.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
c_lib.majorityElementLC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

@pytest.mark.parametrize("function", [c_lib.majorityElementBF, c_lib.majorityElementLC])
def test_majority_element_brute_force(function):
    array = [2,2,1,1,1,2,2]
    # Cast whole array to C integers
    arr = (ctypes.c_int * len(array))(*array)
    out = function(arr, len(arr))
    assert out == 2
