import ctypes

c_lib = ctypes.CDLL('../solutions/0027-remove-element/remove-element.so')

def test_remove_element():
    array = [3,2,2,3]
    target = 3
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.removeElement(arr, len(arr), target)
    assert out == 2
