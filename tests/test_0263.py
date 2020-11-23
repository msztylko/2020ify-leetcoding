import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0263-ugly-number/ugly-number.so')

@pytest.mark.parametrize('num, ans', [(6, True),
                                      (512, True),
                                      (14, False),
                                      (1, True)])
def test_ugly_number(num, ans):
    out =  c_lib.isUgly(num)
    assert out == ans
