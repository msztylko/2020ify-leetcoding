import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1281-product-sum/product-sum.so')

@pytest.mark.parametrize('num, ans', [(234, 15),
                                      (4421, 21)])
def test_product_sum(num, ans):
    out = c_lib.subtractProductAndSum(num)
    assert out == ans
