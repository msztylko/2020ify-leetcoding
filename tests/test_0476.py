import ctypes

c_lib = ctypes.CDLL('../solutions/0476-number-complement/number-complement.so')

def test_complement_number():
    number = 5
    out = c_lib.findComplement(number)
    assert out == 2
