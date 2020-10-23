import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/1486-xor-array/xor-array.so'
c_lib = ctypes.CDLL(c_path)

def test_xor_array():
    n, start = 5, 0
    out = c_lib.xorOperation(n, start)
    assert out == 8
