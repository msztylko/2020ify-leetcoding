import ctypes

c_lib = ctypes.CDLL('../solutions/0191-number-1-bits/number-1-bits.so')

def test_number_of_1_bits():
    number = 0b00000000000000000000000000001011
    out =  c_lib.hammingWeight(number)
    assert out == 3
