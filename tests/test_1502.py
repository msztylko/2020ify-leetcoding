import ctypes

c_lib = ctypes.CDLL('../solutions/1502-arithmetic-progression/arithmetic-progression.so')

def test_arithmetic_progression():
    array = [-509,-19,-439,-264,-404,-369,-299,-89,-229,-54,-194,16,-544,-159,-124,-474,-334]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.canMakeArithmeticProgression(arr, len(arr))
    assert out
