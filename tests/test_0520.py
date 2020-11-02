import ctypes

c_lib = ctypes.CDLL('../solutions/0520-detect-capital/detect-capital.so')

def test_detect_capital():
    string = b"FlaG"
    out = c_lib.detectCapitalUse(string)
    assert not out
