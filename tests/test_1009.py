import ctypes

c_lib = ctypes.CDLL('../solutions/1009-complement-base-10/complement-base-10.so')

def test_complement_base_10():
    number = 10
    out = c_lib.bitwiseComplement(number)
    assert out == 5
