import ctypes

c_lib = ctypes.CDLL('../solutions/0434-segment-string/segment-string.so')

def test_segment_string():
    array = b"Of all the gin joints in all the towns in all the world,   "
    out = c_lib.countSegments(array)
    assert out == 13
