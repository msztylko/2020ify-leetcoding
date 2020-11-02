import ctypes

c_lib = ctypes.CDLL('../solutions/0268-missing-number/missing-number.so')

def test_missing_number():
    array = [9,6,4,2,3,5,7,0,1]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.missingNumber(arr, len(arr))
    assert out == 8
