import ctypes
import pytest

c_path = '/home/marcin/code/2020ify-leetcoding/solutions/0965-univalued-binary-tree/univalued-binary-tree.so'
c_lib = ctypes.CDLL(c_path)

@pytest.mark.skip(reason="TODO")
def test_univalued_binary_tree():
    pass
