import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0476-number-complement/number-complement.so')

@pytest.mark.parametrize('num, ans', [(5,2), (1,0), (257, 254)])
def test_complement_number(num, ans):
    out = c_lib.findComplement(num)
    assert out == ans
