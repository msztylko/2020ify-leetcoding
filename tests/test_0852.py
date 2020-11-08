import ctypes

c_lib = ctypes.CDLL('../solutions/0852-peak-index/peak-index.so')

def test_peak_index():
    array = [24,69,100,99,79,78,67,36,26,19]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.peakIndexInMountainArray(arr, len(arr))
    assert out == 2
