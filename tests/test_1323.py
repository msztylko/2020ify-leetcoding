import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/1323-maximum-69-number/maximum-69-number.so'
c_lib = ctypes.CDLL(c_path)

def test_maximum_69_number():
    number = 9669
    out = c_lib.maximum69Number(number)
    assert out == 9969
