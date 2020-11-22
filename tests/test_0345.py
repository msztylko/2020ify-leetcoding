import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0345-reverse-vowels/reverse-vowels.so')

@pytest.mark.parametrize('string, ans', 
                        [(b'hello', b'holle'),
                         (b'leetcode', b'leotcede')])
def test_reverse_vowels(string, ans):
    c_lib.reverseVowels(string)
    assert string == ans
