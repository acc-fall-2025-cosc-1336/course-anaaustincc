import unittest
from src.homework.c_decisions.decisions import numerical_to_letter_grade

class TestNumericalToLetterGrade(unittest.TestCase):
	def test_grades(self):
		self.assertEqual(numerical_to_letter_grade(95), 'A')
		self.assertEqual(numerical_to_letter_grade(85), 'B')
		self.assertEqual(numerical_to_letter_grade(75), 'C')
		self.assertEqual(numerical_to_letter_grade(65), 'D')
		self.assertEqual(numerical_to_letter_grade(50), 'F')

if __name__ == "__main__":
	unittest.main()