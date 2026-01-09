import unittest
from s_enq.student import calculate_grade

class TestStudentGrading(unittest.TestCase):

    def test_grade_S(self):
        self.assertEqual(calculate_grade([95, 90, 92]), 'S')

    def test_grade_A(self):
        self.assertEqual(calculate_grade([85, 80, 82]), 'A')

    def test_grade_F(self):
        self.assertEqual(calculate_grade([30, 20, 10]), 'F')

    def test_average_calculation(self):
        # Testing boundary case for Grade B (Average 65)
        self.assertEqual(calculate_grade([65, 65, 65]), 'B')

if __name__ == '__main__':
    unittest.main()