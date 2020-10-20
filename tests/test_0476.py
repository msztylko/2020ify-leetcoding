import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0476-number-complement/number-complement.so'
c_lib = ctypes.CDLL(c_path)

def test_complement_number():
    number = 5
    out = c_lib.findComplement(number)
    assert out == 2
