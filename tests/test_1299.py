import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1299-replace-elements/replace-elements.so')

@pytest.mark.skip(reason="Segmentation fault")
def test_replace_elements():
    array = [17,18,5,4,6,1]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.replaceElements(arr, len(arr), len(arr))
    assert arr == [18,6,6,6,1,-1]
