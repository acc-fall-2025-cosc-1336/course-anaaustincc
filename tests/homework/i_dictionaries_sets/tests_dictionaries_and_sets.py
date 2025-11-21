import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget


class Test_Config(unittest.TestCase):

	def test_add_inventory(self):
		inventory = {}
		# add new widget
		add_inventory(inventory, 'Widget1', 10)
		self.assertEqual(inventory.get('Widget1'), 10)

		# update existing widget
		add_inventory(inventory, 'Widget1', 25)
		self.assertEqual(inventory.get('Widget1'), 35)

		# add negative quantity (decrement)
		add_inventory(inventory, 'Widget1', -10)
		self.assertEqual(inventory.get('Widget1'), 25)

	def test_remove_inventory_widget(self):
		inventory = {}
		add_inventory(inventory, 'widget1', 5)
		add_inventory(inventory, 'widget2', 7)

		# remove widget1
		res = remove_inventory_widget(inventory, 'widget1')
		self.assertEqual(res, 'Record deleted')
		self.assertEqual(len(inventory), 1)
		self.assertIn('widget2', inventory)
