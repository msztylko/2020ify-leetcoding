import ctypes

c_lib = ctypes.CDLL('../solutions/0628-max-product/max-product.so')

def test_max_product():
    array = [-1,-2,-3]
    arr = (ctypes.c_int * len(array))(*array)
    out = c_lib.maximumProduct(arr, len(arr))
    assert out == -6
