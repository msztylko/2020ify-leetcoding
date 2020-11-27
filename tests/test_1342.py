import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1342-number-steps/number-steps.so')

@pytest.mark.parametrize('num, ans', [(14, 6), 
                                      (8, 4),
                                      (123, 12)])
def test_number_steps(num, ans):
    out = c_lib.numberOfSteps(num)
    assert out == ans
