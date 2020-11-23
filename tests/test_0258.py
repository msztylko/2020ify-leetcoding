import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0258-add-digits/add-digits.so')

@pytest.mark.parametrize('num, ans', [(38, 2),
                                      (1, 1),
                                      (125, 8)])
def test_add_digits(num, ans):
    out = c_lib.addDigits(num)
    assert out == ans
