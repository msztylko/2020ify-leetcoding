import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0013-roman-to-integer/roman-to-integer.so'
c_lib = ctypes.CDLL(c_path)
# c_lib.romanToInt.argtypes = [ctypes.POINTER(ctypes.c_char)]

def test_roman_to_integer():
    roman = 'V'
    out = c_lib.romanToInt(roman)
    assert out ==5
