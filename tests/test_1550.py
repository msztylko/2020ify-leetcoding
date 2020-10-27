import ctypes

c_lib = ctypes.CDLL('../solutions/1550-consecutive-odd/consecutive-odd.so')

def test_consecutive_odd():
    array = [2,6,4,1]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.threeConsecutiveOdds(arr, len(arr))
    assert out == False
