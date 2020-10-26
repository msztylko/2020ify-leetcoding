import ctypes

c_lib = ctypes.CDLL('../solutions/0342-power-of-four/power-of-four.so')

def test_power_of_four():
    number = 64
    out = c_lib.isPowerOfFour(number)
    assert out
