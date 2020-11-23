import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0242-valid-anagram/valid-anagram.so')

@pytest.mark.parametrize('str1, str2, ans',
                        [(b"anagram", b"nagaram", True),
                         (b"rat", b"car", False)])
def test_is_anagram(str1, str2, ans):
    assert c_lib.isAnagram(str1, str2) == ans
