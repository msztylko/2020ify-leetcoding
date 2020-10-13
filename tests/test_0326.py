import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0326-power-of-three/power-of-three.so'
c_lib = ctypes.CDLL(c_path)
c_lib.isPowerOfThree.argtypes = [ctypes.c_int]

def test_power_of_three():
    number = 27
    out = c_lib.isPowerOfThree(number)
    assert out == True
