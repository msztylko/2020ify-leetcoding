import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0509-fibonacci-number/fibonacci-number.so'
c_lib = ctypes.CDLL(c_path)

def test_fibonacci_number():
    number = 15
    out = c_lib.fib(number)
    assert out == 610
