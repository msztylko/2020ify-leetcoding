import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1486-xor-array/xor-array.so')

@pytest.mark.parametrize('n, start, ans',
                        [(5, 0, 8),
                         (4, 3, 8),
                         (1, 7, 7),
                         (10, 5, 2)])
def test_xor_array(n, start, ans):
    out = c_lib.xorOperation(n, start)
    assert out == ans
