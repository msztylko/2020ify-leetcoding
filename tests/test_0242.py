import ctypes

c_lib = ctypes.CDLL('../solutions/0242-valid-anagram/valid-anagram.so')

def test_is_anagram():
    string1 = b"anagram"
    string2 = b"nagaram"
    assert c_lib.isAnagram(string1, string2)
