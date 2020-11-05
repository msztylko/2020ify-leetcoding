import ctypes

c_lib = ctypes.CDLL('../solutions/1512-good-pair/good-pair.so')

def test_good_pair():
    array = [1,2,3,1,1,3]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.numIdenticalPairs(arr, len(arr))
    assert out == 4
