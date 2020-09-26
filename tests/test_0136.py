import ctypes

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0136-single-number/single-number.so'
c_lib  = ctypes.CDLL(c_path)
c_lib.singleNumber.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

def test_single_number():
    array = [4, 1, 2, 1, 2]
    # Transform Python array to C arr
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.singleNumber(arr, len(arr))
    assert out == 4
