import ctypes

c_lib = ctypes.CDLL('../solutions/0283-move-zeroes/move-zeroes.so')

def test_move_zeroes():
    arr = [0,1,0,3,12]
    c_arr = (ctypes.c_int * len(arr))(*arr)
    c_lib.moveZeroes(c_arr, len(c_arr))
    assert list(c_arr) == [1,3,12,0,0]
