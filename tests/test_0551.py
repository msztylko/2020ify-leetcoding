import ctypes
import pytest

c_lib = ctypes.CDLL('../solutions/0551-student-attendance/student-attendance.so')

@pytest.mark.parametrize('array, ans',
                        [(b"PPALLP", True),
                         (b"PPALLL", False),
                         (b"PPPLPPLLLLPPPLLPPPLPLLAPLPPLPL", False)])
def test_student_attendance(array, ans):
    out = c_lib.checkRecord(array)
    assert out == ans
