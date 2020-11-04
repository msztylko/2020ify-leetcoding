import ctypes

c_lib = ctypes.CDLL('../solutions/0747-dominant-index/dominant-index.so')

def test_dominat_index():
    array = [0,0,1,2]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.dominantIndex(arr, len(arr))
    assert out == 3
