import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0069-sqrt/sqrt.so'
c_lib = ctypes.CDLL(c_path)

def test_sqrt():
    number = 17
    out = c_lib.mySqrt(number)
    assert out == 4 
