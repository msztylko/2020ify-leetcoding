import ctypes

c_lib = ctypes.CDLL('../solutions/0009-palindrome-number/palindrome-number.so')

def test_palindrome_number():
    number = 121
    out = c_lib.isPalindrome(number)
    assert out
