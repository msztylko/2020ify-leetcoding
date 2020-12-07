import ctypes

c_lib = ctypes.CDLL('../solutions/1446-consecutive-characters/consecutive-characters.so')

def test_consecutive_characters():
    string = b"leetcode"
    out = c_lib.maxPower(string)
    assert out == 2
