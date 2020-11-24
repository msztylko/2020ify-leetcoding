import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0520-detect-capital/detect-capital.so')

@pytest.mark.parametrize('str, ans',
                        [(b"USA", True),
                         (b"FlaG", False)])
def test_detect_capital(str, ans):
    out = c_lib.detectCapitalUse(str)
    assert out == ans
