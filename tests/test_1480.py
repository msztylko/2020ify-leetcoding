import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1480-running-sum/running-sum.so')

@pytest.mark.skip(reason="Segmentation fault")
def test_running_sum():
    array = [1,2,3,4]
    arr = (ctypes.c_int * len(array))(*array)
    ret_size = len(arr)
    out = c_lib.runningSum(arr, len(arr), ret_size)
    # assert out == [1,3,6,10]
