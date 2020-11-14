import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/1351-negative-matrix/negative-matrix.so')

@pytest.mark.skip(reason='Code matrix with ctypes')
def test_negative_matrix():
    pass
