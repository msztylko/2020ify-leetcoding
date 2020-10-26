import ctypes

c_lib = ctypes.CDLL('../solutions/0326-power-of-three/power-of-three.so')

def test_power_of_three():
    number = 27
    out = c_lib.isPowerOfThree(number)
    assert out == True
