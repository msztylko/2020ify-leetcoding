import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1323-maximum-69-number/maximum-69-number.so')

@pytest.mark.parametrize('num, ans',
                        [(9669, 9969),
                         (9996, 9999),
                         (9999, 9999)])
def test_maximum_69_number(num, ans):
    out = c_lib.maximum69Number(num)
    assert out == ans
