import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1491-average-salary/average-salary.so')
c_lib.average.restype = ctypes.c_double

@pytest.mark.parametrize('array, ans',
[([4000,3000,1000,2000], 2500.0),
 ([1000,2000,3000], 2000.0),
 ([6000,5000,4000,3000,2000,1000], 3500.0),
 ([8000,9000,2000,3000,6000,1000], 4750.0)])
def test_average_salary(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.average(arr, len(arr))
    assert out == ans
