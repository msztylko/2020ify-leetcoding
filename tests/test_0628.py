import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0628-max-product/max-product.so')

@pytest.mark.parametrize('array, ans',
                        [([1,2,3], 6),
                         ([1,2,3,4], 24),
                         ([-1,-2,-3], -6)])
def test_max_product(array, ans):
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.maximumProduct(arr, len(arr))
    assert out == ans
