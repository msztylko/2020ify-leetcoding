import ctypes

c_lib = ctypes.CDLL('../solutions/0387-unique-character/unique-character.so')

def test_unique_character():
    string = b"loveleetcode"
    out = c_lib.firstUniqChar(string)
    assert out == 2
