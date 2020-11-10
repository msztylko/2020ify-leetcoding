import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0027-remove-element/remove-element.so')

@pytest.mark.parametrize('function', [c_lib.removeElement,
                                      c_lib.removeElementFaster])
def test_remove_element(function):
    array = [3,2,2,3]
    target = 3
    arr = (ctypes.c_int * len(array))(*array)
    out = function(arr, len(arr), target)
    assert out == 2
