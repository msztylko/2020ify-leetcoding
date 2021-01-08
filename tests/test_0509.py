import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0509-fibonacci-number/fibonacci-number.so')

@pytest.mark.parametrize('function', [c_lib.fib, c_lib.fibArray])
def test_fibonacci_number(function):
    number = 15
    out = function(number)
    assert out == 610
