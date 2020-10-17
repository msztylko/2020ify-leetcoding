import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0231-power-of-two/power-of-two.so'
c_lib = ctypes.CDLL(c_path)
c_lib.isPowerOfTwo.argtypes = [ctypes.c_int]

def test_power_of_two():
    number = 16
    out = c_lib.isPowerOfTwo(number)
    assert out
