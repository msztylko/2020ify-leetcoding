import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1009-complement-base-10/complement-base-10.so')

@pytest.mark.parametrize('num, ans', [(5, 2), 
                                      (7, 0),
                                      (10, 5)])
def test_complement_base_10(num, ans):
    out = c_lib.bitwiseComplement(num)
    assert out == ans
