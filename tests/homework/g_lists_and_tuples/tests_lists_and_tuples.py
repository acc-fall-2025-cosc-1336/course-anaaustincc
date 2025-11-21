import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, get_highest_list_value


class Test_ListFunctions(unittest.TestCase):

	def test_get_lowest_list_value(self):
		values = [8, 10, 1, 50, 20]
		self.assertEqual(get_lowest_list_value(values), 1)

	def test_get_highest_list_value(self):
		values = [8, 10, 1, 50, 20]
		self.assertEqual(get_highest_list_value(values), 50)


class Test_Config(unittest.TestCase):

	def test_p_distance(self):
		a = ['T','T','T','C','C','A','T','T','T','A']
		b = ['G','A','T','T','C','A','T','T','T','C']
		from src.homework.g_lists_and_tuples.lists import get_p_distance
		self.assertAlmostEqual(get_p_distance(a, b), 0.4, places=3)

	def test_get_p_distance_matrix(self):
		sets = [
			['T','T','T','C','C','A','T','T','T','A'],
			['G','A','T','T','C','A','T','T','T','C'],
			['T','T','T','C','C','A','T','T','T','T'],
			['G','T','T','C','C','A','T','T','T','A']
		]
		from src.homework.g_lists_and_tuples.lists import get_p_distance_matrix
		expected = [
			[0.0, 0.4, 0.1, 0.1],
			[0.4, 0.0, 0.4, 0.3],
			[0.1, 0.4, 0.0, 0.2],
			[0.1, 0.3, 0.2, 0.0]
		]
		result = get_p_distance_matrix(sets)
		# compare each entry with tolerance
		i = 0
		while i < len(expected):
			j = 0
			while j < len(expected[i]):
				self.assertAlmostEqual(result[i][j], expected[i][j], places=3)
				j += 1
			i += 1
