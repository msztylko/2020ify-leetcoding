import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/1491-average-salary/average-salary.so'
c_lib = ctypes.CDLL(c_path)
c_lib.average.restype = ctypes.c_double

def test_average_salary():
    array = [4000, 3000, 1000 ,2000]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.average(arr, len(arr))
    assert out == 2500.0
