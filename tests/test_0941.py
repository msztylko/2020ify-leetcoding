import ctypes

c_lib = ctypes.CDLL('../solutions/0941-mountain-array/mountain-array.so')

def test_mountain_array():
    array = [0,3,2,1]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.validMountainArray(arr, len(arr))
    assert out
