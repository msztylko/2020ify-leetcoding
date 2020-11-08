import ctypes

c_lib = ctypes.CDLL('../solutions/1207-unique-number/unique-number.so')

def test_unique_number():
    array = [1,2,2,1,1,3]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.uniqueOccurrences(arr, len(arr))
    assert out
