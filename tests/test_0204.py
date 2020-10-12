import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0204-count-primes/count-primes.so'
c_lib = ctypes.CDLL(c_path)
c_lib.countPrimes.argtypes = [ctypes.c_int]

def test_count_primes():
    number = 10
    out = c_lib.countPrimes(number)
    assert out == 4
