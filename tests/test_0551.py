import ctypes

c_lib = ctypes.CDLL('../solutions/0551-student-attendance/student-attendance.so')

def test_student_attendance():
    array = b"PPPLPPLLLLPPPLLPPPLPLLAPLPPLPL"
    out = c_lib.checkRecord(array)
    assert not out
