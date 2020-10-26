import ctypes

c_lib = ctypes.CDLL('../solutions/0367-valid-perfect-square/valid-perfect-square.so')

def test_valid_perfect_square():
    number = 256
    out = c_lib.isPerfectSquare(number)
    assert out
