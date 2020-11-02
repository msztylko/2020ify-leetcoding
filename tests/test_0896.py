import ctypes

c_lib = ctypes.CDLL('../solutions/0896-monotonic-array/monotonic-array.so')

def test_monotonic_array():
    array = [6,5,4,4]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.isMonotonic(arr, len(arr))
    assert out
