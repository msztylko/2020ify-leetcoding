import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0242-valid-anagram/valid-anagram.so'
c_lib = ctypes.CDLL(c_path)

def test_is_anagram():
    string1 = b"anagram"
    string2 = b"nagaram"
    assert c_lib.isAnagram(string1, string2)
