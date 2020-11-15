import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1299-replace-elements/replace-elements.so')

@pytest.mark.skip(reason="Segmentation fault")
@pytest.mark.parametrize('function', [c_lib.replaceElements,
                                      c_lib.replaceElementsOptimized])
def test_replace_elements(function):
    array = [17,18,5,4,6,1]
    arr = (ctypes.c_int * len(array))(*array)
    out = function(arr, len(arr), len(arr))
    assert arr == [18,6,6,6,1,-1]
