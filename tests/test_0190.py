import ctypes

c_lib = ctypes.CDLL('../solutions/0190-reverse-bits/reverse-bits.so')

def test_reverse_bits():
    number = 0b00000010100101000001111010011100
    out = c_lib.reverseBits(number)
    assert out == 964176192
