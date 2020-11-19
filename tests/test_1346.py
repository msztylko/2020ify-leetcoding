import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1346-check-exist/check-exist.so')

@pytest.mark.parametrize('array, ans', 
                        [([10,2,5,3], True),
                         ([7,1,14,11], True),
                         ([3,1,7,11], False)])
                        
def test_check_exist(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.checkIfExist(arr, len(arr))
    assert out == ans
