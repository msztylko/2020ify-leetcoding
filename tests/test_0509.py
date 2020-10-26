import ctypes

c_lib = ctypes.CDLL('../solutions/0509-fibonacci-number/fibonacci-number.so')

def test_fibonacci_number():
    number = 15
    out = c_lib.fib(number)
    assert out == 610
