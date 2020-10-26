import ctypes

c_lib = ctypes.CDLL('../solutions/0762-count-prime-bits/count-prime-bits.so')

def test_count_prime_bits():
    left, right = 244, 269
    out = c_lib.countPrimeSetBits(left, right)
    assert out == 16
