import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0009-palindrome-number/palindrome-number.so')

@pytest.mark.parametrize('num, ans', [(-121, False),
                                      (10, False)])
def test_palindrome_number(num, ans):
    out = c_lib.isPalindrome(num)
    assert out == ans
