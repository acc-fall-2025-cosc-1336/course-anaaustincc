import unittest
from src.homework.b_in_proc_out.output import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-1, 5), -5)
        self.assertEqual(multiply_numbers(0, 10), 0)

    def test_floats(self):
        self.assertAlmostEqual(multiply_numbers(2.5, 4), 10.0)
        self.assertAlmostEqual(multiply_numbers(-1.5, 2), -3.0)
        self.assertAlmostEqual(multiply_numbers(0.0, 7.1), 0.0)

    def test_mixed_types(self):
        self.assertAlmostEqual(multiply_numbers(3, 2.5), 7.5)
        self.assertAlmostEqual(multiply_numbers(-2, 0.5), -1.0)

    def test_main_program_examples(self):
        self.assertEqual(multiply_numbers(7, 7), 49)
        self.assertEqual(multiply_numbers(5, 5), 25)

if __name__ == "__main__":
    unittest.main()
