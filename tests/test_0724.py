import ctypes

c_lib = ctypes.CDLL('../solutions/0724-pivot-index/pivot-index.so')

def test_pivot_index():
    array = [-1,-1,-1,0,1,1]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.pivotIndex(arr, len(arr))
    assert out == 0
