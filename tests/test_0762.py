import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0762-count-prime-bits/count-prime-bits.so'
c_lib = ctypes.CDLL(c_path)

def test_count_prime_bits():
    left, right = 244, 269
    out = c_lib.countPrimeSetBits(left, right)
    assert out == 16
