import ctypes

c_lib = ctypes.CDLL('../solutions/0263-ugly-number/ugly-number.so')

def test_ugly_number():
    number = 512
    out =  c_lib.isUgly(number)
    assert out
