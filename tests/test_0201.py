import ctypes
import pytest

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0201-bitwise-and/bitwise-and.so'
c_lib = ctypes.CDLL(c_path)

@pytest.mark.parametrize("function", [c_lib.rangeBitwiseAndNaive, c_lib.rangeBitwiseAndFast])
def test_bitwise_and(function):
    a, b = 0, 214748364
    out = function(a, b)
    assert out == 0
