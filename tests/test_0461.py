import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0461-hamming-distance/hamming-distance.so'
c_lib = ctypes.CDLL(c_path)

def test_hamming_distance():
    a, b = 1, 4
    out = c_lib.hammingDistance(a, b)
    assert out == 2
