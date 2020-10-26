import ctypes

c_lib = ctypes.CDLL('../solutions/0231-power-of-two/power-of-two.so')

def test_power_of_two_naive():
    number = 16
    out = c_lib.isPowerOfTwoNaive(number)
    assert out

def test_power_of_two_bit():
    number = 16
    out = c_lib.isPowerOfTwoBit(number)
    assert out
