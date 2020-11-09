import ctypes

c_lib = ctypes.CDLL('../solutions/0345-reverse-vowels/reverse-vowels.so')

def test_reverse_vowels():
    string = b"hello"
    c_lib.reverseVowels(string)
    assert string == b"holle"
