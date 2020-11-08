import ctypes

c_lib = ctypes.CDLL('../solutions/1051-height-checker/height-checker.so')

def test_height_checker():
    array = [5,1,2,3,4]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.heightChecker(arr, len(arr))
    assert out == 5
