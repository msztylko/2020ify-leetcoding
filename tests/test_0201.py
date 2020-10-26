import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0201-bitwise-and/bitwise-and.so')

@pytest.mark.parametrize("function", [c_lib.rangeBitwiseAndNaive, c_lib.rangeBitwiseAndFast])
def test_bitwise_and(function):
    a, b = 0, 214748364
    out = function(a, b)
    assert out == 0
