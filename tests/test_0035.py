import ctypes

c_lib = ctypes.CDLL('../solutions/0035-search-insert/search-insert.so')

def test_search_insert():
    array = [1,3,5,6]
    target = 2
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.searchInsert(arr, len(arr), target)
    assert out == 1
