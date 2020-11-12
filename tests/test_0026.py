import ctypes

c_lib = ctypes.CDLL('../solutions/0026-duplicate-sorted/duplicate-sorted.so')

def test_duplicate_sorted():
    array = [0,0,1,1,1,2,2,3,3,4]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.removeDuplicates(arr, len(arr))
    assert out == 5
