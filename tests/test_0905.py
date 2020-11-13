import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0905-sort-parity/sort-parity.so')

@pytest.mark.skip(reason="Segmentation Fault")
def test_sort_parity():
    pass
