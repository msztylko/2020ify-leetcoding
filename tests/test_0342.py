import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0342-power-of-four/power-of-four.so'
c_lib = ctypes.CDLL(c_path)
c_lib.isPowerOfFour.argtypes = [ctypes.c_int]

def test_power_of_four():
    number = 64
    out = c_lib.isPowerOfFour(number)
    assert out
