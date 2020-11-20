import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0013-roman-to-integer/roman-to-integer.so')

@pytest.mark.parametrize('roman, ans', 
                        [(b'III', 3),
                         (b'IV', 4),
                         (b'IX', 9),
                         (b'LVIII', 58),
                         (b'MCMXCIV', 1994)])
def test_roman_to_integer(roman, ans):
    out = c_lib.romanToInt(roman)
    assert out == ans
