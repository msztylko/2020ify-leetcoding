import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0344-reverse-string/reverse-string.so')

@pytest.mark.parametrize('string, ans',
                        [(b"Hello World", b"dlroW olleH"),
                         (b"Hannah", b"hannaH")])
def test_reverse_string(string, ans):
    c_lib.reverseString(string, len(string))
    assert string == ans
