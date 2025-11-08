import unittest
from tests.homework.e_functions import tests_functions

if __name__ == "__main__":
	from tests.homework.g_lists_and_tuples import tests_lists_and_tuples

	suite = unittest.TestLoader().loadTestsFromModule(tests_lists_and_tuples)
	unittest.TextTestRunner(verbosity=2).run(suite)

