import ctypes

c_lib = ctypes.CDLL('../solutions/0961-repeated-element/repeated-element.so')

def test_repeated_element():
    array = [1, 2, 3, 3]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.repeatedNTimes(arr, len(arr))
    assert out == 3 
