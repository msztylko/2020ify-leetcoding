import ctypes
import pathlib
import os

SOLUTIONS_PATH = '/home/marcin/code/2020ify-leetcoding/solutions/1323-maximum-69-number'

c_path = os.path.join(SOLUTIONS_PATH, 'maximum-69-number.so')
c_lib = ctypes.CDLL(c_path)
c_lib.maximum69Number.argtypes = [ctypes.c_int]

def test_maximum_69_number():
    number = 9669
    out = c_lib.maximum69Number(number)
    assert out == 9969
