import ctypes

c_lib = ctypes.CDLL('../solutions/0258-add-digits/add-digits.so')

def test_add_digits():
    number = 38
    out = c_lib.addDigits(number)
    assert out == 2 
