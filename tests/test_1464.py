import ctypes

c_lib = ctypes.CDLL('../solutions/1464-max-product/max-product.so')

def test_max_product():
    array = [3,4,5,2]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.maxProduct(arr, len(arr))
    assert out == 12
