import ctypes

c_lib = ctypes.CDLL('../solutions/1342-number-steps/number-steps.so')

def test_number_steps():
    number = 123456
    out = c_lib.numberOfSteps(number)
    assert out == 22
