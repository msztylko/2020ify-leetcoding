import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1502-arithmetic-progression/arithmetic-progression.so')

@pytest.mark.parametrize('array, ans', 
[([-509,-19,-439,-264,-404,-369,-299,-89,-229,-54,-194,16,-544,-159,-124,-474,-334], True),
 ([3,5,1], True),
 ([1,2,4], False)])
def test_arithmetic_progression(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.canMakeArithmeticProgression(arr, len(arr))
    assert out == ans
