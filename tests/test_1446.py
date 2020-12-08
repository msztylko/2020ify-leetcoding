import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1446-consecutive-characters/consecutive-characters.so')

@pytest.mark.parametrize('string, ans',
[(b"leetcode", 2),
 (b"abbcccddddeeeeedcba", 5),
 (b"triplepillooooow", 5),
 (b"hooraaaaaaaaaaay", 11),
 (b"tourist", 1)])
def test_consecutive_characters(string, ans):
    out = c_lib.maxPower(string)
    assert out == ans
