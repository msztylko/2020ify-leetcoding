import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0762-count-prime-bits/count-prime-bits.so')

@pytest.mark.parametrize("left, right, ans",
                        [(6, 10, 4),
                         (10, 15, 5)])
def test_count_prime_bits(left, right, ans):
    out = c_lib.countPrimeSetBits(left, right)
    assert out == ans
