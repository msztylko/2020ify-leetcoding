import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0201-bitwise-and/bitwise-and.so')

@pytest.mark.parametrize('function', [c_lib.rangeBitwiseAndNaive, c_lib.rangeBitwiseAndFast])
@pytest.mark.parametrize('a, b, ans', 
                        [(0, 1, 0),
                         (0, 214748364, 0)])
def test_bitwise_and(a, b, ans, function):
    out = function(a, b)
    assert out == ans
