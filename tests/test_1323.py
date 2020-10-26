import ctypes

c_lib = ctypes.CDLL('../solutions/1323-maximum-69-number/maximum-69-number.so')

def test_maximum_69_number():
    number = 9669
    out = c_lib.maximum69Number(number)
    assert out == 9969
