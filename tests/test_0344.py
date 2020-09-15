import ctypes
import pathlib
import os

SOLUTIONS_PATH = '/home/marcin/code/2020ify-leetcoding/solutions/0344-reverse-string'

c_path = os.path.join(SOLUTIONS_PATH, 'reverse-string.so')
c_lib = ctypes.CDLL(c_path)
c_lib.reverseString.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.c_int]

def test_reverse_string():
    string = "Hello World"
    string_len = len(string)
    mutable_string = ctypes.create_string_buffer(string.encode())
    c_lib.reverseString(mutable_string, string_len)
    string_out = mutable_string.value.decode()
    assert string[::-1] == string_out
