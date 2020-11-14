import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0728-self-dividing/self-dividing.so')

@pytest.mark.skip(reason='pointer in arguments?')
def test_self_dividing():
    left, right = 1, 22
    retSize = ctypes.POINTER(ctypes.c_int)
    out = c_lib.selfDividingNumbers(left, right, retSize)
    assert out == [1,2,3,4,5,6,7,8,9,11,12,15,22]
