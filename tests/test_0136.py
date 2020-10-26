import ctypes

c_lib  = ctypes.CDLL('../solutions/0136-single-number/single-number.so')

def test_single_number():
    array = [4, 1, 2, 1, 2]
    # Transform Python array to C arr
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.singleNumber(arr, len(arr))
    assert out == 4
