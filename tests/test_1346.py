import ctypes

c_lib = ctypes.CDLL('../solutions/1346-check-exist/check-exist.so')

def test_check_exist():
    array = [7,1,14,11]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.checkIfExist(arr, len(arr))
    assert out
