import ctypes

c_lib = ctypes.CDLL('../solutions/1295-even-digits/even-digits.so')

def test_even_digits():
    array = [12,345,2,6,7896]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.findNumbers(arr, len(arr))
    assert out == 2
