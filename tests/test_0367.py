import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0367-valid-perfect-square/valid-perfect-square.so'
c_lib = ctypes.CDLL(c_path)

def test_valid_perfect_square():
    number = 256
    out = c_lib.isPerfectSquare(number)
    assert out
