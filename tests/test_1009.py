import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/1009-complement-base-10/complement-base-10.so'
c_lib = ctypes.CDLL(c_path)

def test_complement_base_10():
    number = 10
    out = c_lib.bitwiseComplement(number)
    assert out == 5
