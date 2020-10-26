import ctypes

c_lib = ctypes.CDLL('../solutions/0461-hamming-distance/hamming-distance.so')

def test_hamming_distance():
    a, b = 1, 4
    out = c_lib.hammingDistance(a, b)
    assert out == 2
