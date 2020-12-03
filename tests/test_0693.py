import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0693-alternating-bits/alternating-bits.so')

@pytest.mark.parametrize('num, ans', 
                        [(5, True),
                         (7, False),
                         (11, False),
                         (10, True)]) 
def test_alternating_bits(num, ans):
    out = c_lib.hasAlternatingBits(num)
    assert out == ans
