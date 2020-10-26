import ctypes

c_lib = ctypes.CDLL('../solutions/0204-count-primes/count-primes.so')

def test_count_primes():
    number = 10
    out = c_lib.countPrimes(number)
    assert out == 4
