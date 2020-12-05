import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0190-reverse-bits/reverse-bits.so')

@pytest.mark.parametrize('num, ans',
[(0b00000010100101000001111010011100, 964176192),
 (0b11111111111111111111111111111101, 3221225471)])
def test_reverse_bits(num, ans):
    out = c_lib.reverseBits(num)
    # "cast" to unsigned. Underlying representation stays the same
    assert out & 0xffffffff == ans
