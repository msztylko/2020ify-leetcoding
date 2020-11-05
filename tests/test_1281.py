import ctypes

c_lib = ctypes.CDLL('../solutions/1281-product-sum/product-sum.so')

def test_product_sum():
    number = 12345
    out = c_lib.subtractProductAndSum(number)
    assert out == 105
