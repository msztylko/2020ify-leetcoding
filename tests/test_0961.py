import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0961-repeated-element/repeated-element.so')

@pytest.mark.parametrize('array, ans',
                        [([1,2,3,3], 3),
                         ([2,1,2,5,3,2], 2),
                         ([5,1,5,2,5,3,5,4], 5)])
@pytest.mark.parametrize('function', [c_lib.repeatedNTimes, 
                                      c_lib.repeatedNTimesHashTable])
def test_repeated_element(function, array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = function(arr, len(arr))
    assert out == ans 
