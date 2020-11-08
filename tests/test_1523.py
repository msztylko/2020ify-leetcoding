import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1523-count-odd/count-odd.so')

@pytest.mark.parametrize("function", [c_lib.countOddsNaive,
                                      c_lib.countOddsFast,
                                      c_lib.countOddsMath])
def test_count_odds(function):
    low, high = 3, 7
    out = function(low, high)
    assert out == 3
