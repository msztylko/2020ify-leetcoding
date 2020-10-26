import ctypes

c_lib = ctypes.CDLL('../solutions/0069-sqrt/sqrt.so')

def test_sqrt():
    number = 17
    out = c_lib.mySqrt(number)
    assert out == 4 
