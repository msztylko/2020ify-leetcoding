import ctypes

c_lib = ctypes.CDLL('../solutions/1486-xor-array/xor-array.so')

def test_xor_array():
    n, start = 5, 0
    out = c_lib.xorOperation(n, start)
    assert out == 8
