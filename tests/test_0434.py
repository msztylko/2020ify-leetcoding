import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0434-segment-string/segment-string.so')

@pytest.mark.parametrize('str, ans',
[(b'Hello, my name is John', 5),
 (b'Hello', 1),
 (b"love live! mu'sic forever", 4),
 (b"", 0)])
def test_segment_string(str, ans):
    out = c_lib.countSegments(str)
    assert out == ans
