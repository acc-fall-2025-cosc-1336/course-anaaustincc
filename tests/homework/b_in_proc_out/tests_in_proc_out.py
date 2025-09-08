import unittest
from src.homework.b_in_proc_out.output import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply_integers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-2, 3), -6)
        self.assertEqual(multiply_numbers(0, 3), 0)
        self.assertEqual(multiply_numbers(0, 0), 0)

    def test_multiply_floats(self):
        self.assertEqual(multiply_numbers(2.0, 3.0), 6.0)
        self.assertEqual(multiply_numbers(-2.5, 4.0), -10.0)
        self.assertEqual(multiply_numbers(0.0, 5.0), 0.0)

    def test_multiply_int_and_float(self):
        self.assertEqual(multiply_numbers(2, 3.5), 7.0)
        self.assertEqual(multiply_numbers(-2, 3.5), -7.0)

if __name__ == "__main__":
    unittest.main()