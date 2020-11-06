import ctypes

c_lib  = ctypes.CDLL('../solutions/1089-duplicate-zeros/duplicate-zeros.so')

def test_duplicate_zeros():
    array = [1,0,2,3,0,4,5,0]
    arr = (ctypes.c_int * len(array))(*array)
    c_lib.duplicateZeros(arr, len(arr))
    assert list(arr) == [1,0,0,2,3,0,0,4]
