import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0007-reverse-integer/reverse-integer.so')

@pytest.mark.parametrize('x, ans', [(123, 321),
                                    (-123, -321),
                                    (120, 21),
                                    (0, 0)])
def test_reverse_integer(x, ans):
    out = c_lib.reverse(x)
    assert out == ans
