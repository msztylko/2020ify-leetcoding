import ctypes
import pytest

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0283-move-zeroes/move-zeroes.so'
c_lib = ctypes.CDLL(c_path)
c_lib.moveZeroes.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

def test_move_zeroes():
    arr = [0,1,0,3,12]
    c_arr = (ctypes.c_int * len(arr))(*arr)
    c_lib.moveZeroes(c_arr, len(c_arr))
    assert list(c_arr) == [1,3,12,0,0]
