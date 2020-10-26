import ctypes

c_lib = ctypes.CDLL('../solutions/0007-reverse-integer/reverse-integer.so')

def test_reverse_integer():
    x = 123
    out = c_lib.reverse(x)
    assert out == 321
