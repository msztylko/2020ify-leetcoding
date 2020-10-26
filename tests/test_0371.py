import ctypes

c_lib = ctypes.CDLL('../solutions/0371-sum-two-integers/sum-two-integers.so')

def test_sum_two_integers():
    a = 2
    b = -5
    out = c_lib.getSum(a, b)
    assert out == -3
