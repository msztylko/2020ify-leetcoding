import ctypes
import pathlib
import os

SOLUTIONS_PATH = '/home/marcin/code/2020ify-leetcoding/solutions/0169-majority-element'

c_path = os.path.join(SOLUTIONS_PATH, 'majority-element.so')
c_lib = ctypes.CDLL(c_path)
c_lib.majorityElementBF.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
c_lib.majorityElementLC.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

def test_majority_element_brute_force():
    array = [2,2,1,1,1,2,2]
    # Cast whole array to C integers
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.majorityElementBF(arr, len(arr))
    assert out == 2

def test_majority_element_leetcode():
    array = [2,2,1,1,1,2,2]
    # Cast whole array to C integers
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.majorityElementLC(arr, len(arr))
    assert out == 2

