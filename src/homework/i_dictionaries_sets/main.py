"""Interactive inventory menu for dictionary exercises.

Menu:
1-Add or Update Item
2-Delete Item
3-Exit

The program runs until the user chooses option 3.
"""

import os
import sys

# When the module is executed as a script (not as part of the package),
# ensure the repository root is on sys.path so package imports like
# `from src.homework...` work correctly.
if __package__ is None:
	# Compute repository root reliably from this file's location.
	# __file__ -> /.../course-anaaustincc/src/homework/i_dictionaries_sets/main.py
	# ascend 3 levels to reach the repository root (`course-anaaustincc`).
	project_root = os.path.abspath(
		os.path.join(os.path.dirname(__file__), '..', '..', '..')
	)
	if project_root not in sys.path:
		sys.path.insert(0, project_root)

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget


def print_menu() -> None:
	print("Inventory Menu")
	print("1-Add or Update Item")
	print("2-Delete Item")
	print("3-Exit")


def main() -> None:
	inventory = {}
	while True:
		print_menu()
		choice = input("Choose an option: ").strip()

		if choice == '1':
			name = input("Enter widget name: ").strip()
			qty_raw = input("Enter quantity (integer, may be negative to decrement): ").strip()
			try:
				qty = int(qty_raw)
			except ValueError:
				print("Invalid quantity. Please enter an integer.")
				continue

			try:
				add_inventory(inventory, name, qty)
				print(f"Updated inventory: {name} -> {inventory.get(name)}")
			except Exception as e:
				print(f"Error: {e}")

		elif choice == '2':
			name = input("Enter widget name to delete: ").strip()
			try:
				res = remove_inventory_widget(inventory, name)
				print(res)
			except Exception as e:
				print(f"Error: {e}")

		elif choice == '3':
			print("Exiting...")
			break

		else:
			print("Invalid option. Please select 1, 2, or 3.")


if __name__ == '__main__':
	main()
