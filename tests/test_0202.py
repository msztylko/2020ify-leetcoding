import ctypes

c_lib = ctypes.CDLL('../solutions/0202-happy-number/happy-number.so')

def test_is_happy():
    number = 19
    out = c_lib.isHappy(number)
    assert out == True
