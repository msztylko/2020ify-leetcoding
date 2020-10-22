import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0371-sum-two-integers/sum-two-integers.so'
c_lib = ctypes.CDLL(c_path)

def test_sum_two_integers():
    a = 2
    b = -5
    out = c_lib.getSum(a, b)
    assert out == -3
