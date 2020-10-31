import ctypes

c_lib = ctypes.CDLL('../solutions/1287-elem-appearing/elem-appearing.so')

def test_elem_appearing():
    array = [1,2,3,3]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.findSpecialInteger(arr, len(arr))
    assert out == 3
