import ctypes
import pytest
c_lib = ctypes.CDLL('../solutions/0917-reverse-letters/reverse-letters.so')

@pytest.mark.skip(reason="C Strings...")
def test_reverse_letters():
    string = "Test1ng-Leet=code-Q!"
    mutable_string = ctypes.create_string_buffer(string.encode())
    out = c_lib.reverseOnlyLetters(mutable_string)
    assert out == b"Qedo1ct-eeLg=ntse-T!"
