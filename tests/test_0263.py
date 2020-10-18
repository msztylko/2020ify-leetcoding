import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0263-ugly-number/ugly-number.so'
c_lib = ctypes.CDLL(c_path)

def test_ugly_number():
    number = 512
    out =  c_lib.isUgly(number)
    assert out
