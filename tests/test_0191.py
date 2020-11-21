import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0191-number-1-bits/number-1-bits.so')

@pytest.mark.parametrize('num, ans',
[(0b00000000000000000000000000001011, 3),
 (0b00000000000000000000000010000000, 1),
 (0b11111111111111111111111111111101, 31)])
def test_number_of_1_bits(num, ans):
    out =  c_lib.hammingWeight(num)
    assert out == ans
