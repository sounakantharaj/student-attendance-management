
import unittest

def attendance_percentage(present, total):
    if total == 0:
        return 0
    return (present / total) * 100


class TestAttendance(unittest.TestCase):

    def test_normal_percentage(self):
        self.assertEqual(attendance_percentage(18, 20), 90.0)

    def test_zero_classes(self):
        self.assertEqual(attendance_percentage(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
