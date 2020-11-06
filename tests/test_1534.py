import ctypes

c_lib = ctypes.CDLL('../solutions/1534-count-triplets/count-triplets.so')

def test_count_triplets():
    array = [3,0,1,1,9,7]
    a = 7
    b = 2
    c = 3
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.countGoodTriplets(arr, len(arr), a, b, c)
    assert out == 4
