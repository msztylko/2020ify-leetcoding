import ctypes

c_lib = ctypes.CDLL('../solutions/0013-roman-to-integer/roman-to-integer.so')

def test_roman_to_integer():
    roman = 'V'
    out = c_lib.romanToInt(roman)
    assert out == 5
