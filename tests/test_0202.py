import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0202-happy-number/happy-number.so'
c_lib = ctypes.CDLL(c_path)
c_lib.isHappy.argtypes = [ctypes.c_int]

def test_is_happy():
    number = 19
    out = c_lib.isHappy(number)
    assert out == True
