import ctypes

c_lib = ctypes.CDLL('../solutions/0088-merge-sorted-array/merge-sorted-array.so')

def test_merge_sorted_array():
    array1 = [1,2,3,0,0,0] 
    array2 = [2,5,6]
    m = 3
    n = 3
    arr1 = (ctypes.c_int * len(array1))(*array1)
    arr2 = (ctypes.c_int * len(array2))(*array2)
    c_lib.merge(arr1, len(arr1), m, arr2, len(arr2), n)
    assert list(arr1) == [1,2,2,3,5,6]
