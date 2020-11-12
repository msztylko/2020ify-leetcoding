import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1464-max-product/max-product.so')

@pytest.mark.parametrize('function', [c_lib.maxProductNaive,
                                      c_lib.maxProductOnePass])
def test_max_product(function):
    array = [3,4,5,2]
    arr = (ctypes.c_int * len(array))(*array)
    out = function(arr, len(arr))
    assert out == 12
