import ctypes

c_lib = ctypes.CDLL('../solutions/1394-lucky-number/lucky-number.so')

def test_lucky_number():
    array = [7,7,7,7,7,7,7]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.findLucky(arr, len(arr))
    assert out == 7
