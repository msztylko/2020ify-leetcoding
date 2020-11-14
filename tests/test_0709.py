import ctypes

c_lib = ctypes.CDLL('../solutions/0709-to-lower/to-lower.so')

def test_to_lower():
    string = b"Hello"
    c_lib.toLowerCase(string)
    assert string == b"hello"
