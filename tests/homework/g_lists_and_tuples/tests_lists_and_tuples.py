import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, get_highest_list_value


class Test_ListFunctions(unittest.TestCase):

	def test_get_lowest_list_value(self):
		values = [8, 10, 1, 50, 20]
		self.assertEqual(get_lowest_list_value(values), 1)

	def test_get_highest_list_value(self):
		values = [8, 10, 1, 50, 20]
		self.assertEqual(get_highest_list_value(values), 50)
