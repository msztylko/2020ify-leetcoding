import ctypes

c_lib = ctypes.CDLL('../solutions/1137-tribonacci/tribonacci.so')

def test_tribonacci():
    number = 35
    out = c_lib.tribonacci(number)
    assert out == 615693474
