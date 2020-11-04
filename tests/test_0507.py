import ctypes

c_lib = ctypes.CDLL('../solutions/0507-perfect-number/perfect-number.so')

def test_perfect_number():
    number = 28
    out = c_lib.checkPerfectNumber(number)
    assert out
