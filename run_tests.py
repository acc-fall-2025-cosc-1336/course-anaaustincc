import unittest
from tests.homework.d_repetition import tests_repetition

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
	unittest.TextTestRunner(verbosity=2).run(suite)

