import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0007-reverse-integer/reverse-integer.so'
c_lib = ctypes.CDLL(c_path)

def test_reverse_integer():
    x = 123
    out = c_lib.reverse(x)
    assert out == 321
