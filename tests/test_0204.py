import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0204-count-primes/count-primes.so')

@pytest.mark.parametrize('num, ans',
                        [(10, 4),
                         (0, 0),
                         (1, 0)])
def test_count_primes(num, ans):
    out = c_lib.countPrimes(num)
    assert out == ans
