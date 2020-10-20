import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0693-alternating-bits/alternating-bits.so'
c_lib = ctypes.CDLL(c_path)

def test_alternating_bits():
    number = 3
    out = c_lib.hasAlternatingBits(number)
    assert out != True
