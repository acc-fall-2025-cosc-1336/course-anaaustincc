
import unittest
from tests.homework.c_decisions import tests_decisions

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
	unittest.TextTestRunner(verbosity=2).run(suite)

