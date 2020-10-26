import ctypes

c_lib = ctypes.CDLL('../solutions/0693-alternating-bits/alternating-bits.so')

def test_alternating_bits():
    number = 3
    out = c_lib.hasAlternatingBits(number)
    assert out != True
