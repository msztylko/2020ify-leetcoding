import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0961-repeated-element/repeated-element.so'
c_lib = ctypes.CDLL(c_path)

def test_repeated_element():
    array = [1, 2, 3, 3]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.repeatedNTimes(arr, len(arr))
    assert out == 3 
