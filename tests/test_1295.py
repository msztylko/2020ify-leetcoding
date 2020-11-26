import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1295-even-digits/even-digits.so')

@pytest.mark.parametrize('array, ans',
                        [([12,345,2,6,7896], 2),
                         ([555,901,482,1771], 1)])
def test_even_digits(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.findNumbers(arr, len(arr))
    assert out == ans
