"""Interactive menu for list min/max (homework g_lists_and_tuples).

Menu:
1-Show the list low /high values
2-Exit

Option 1: prompt the user to enter list values until they opt to stop. After
the user has entered at least 3 values, the program will ask whether they want
to enter another value; before that it will continue collecting values.
"""

import os
import sys

# If executed as a script, ensure the project root is on sys.path so imports
# like `from src.homework...` work correctly.
if __package__ is None:
	project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
	if project_root not in sys.path:
		sys.path.insert(0, project_root)

from src.homework.g_lists_and_tuples.lists import (
	get_lowest_list_value,
	get_highest_list_value,
)


def print_menu() -> None:
	print("1-Show the list low /high values")
	print("2-Exit")


def read_values() -> list:
	"""Read list values from the user according to the spec.

	The function collects values (floats) in a list. It does not ask whether to
	continue until at least 3 values have been entered. After 3 or more entries
	the user is prompted: 'Do you want to enter another value? (y/n)'.
	"""
	values = []
	while True:
		entry = input("Enter a list value: ").strip()
		# try to parse as float (accept integers too)
		try:
			if entry == "":
				# empty input is considered invalid here; ask again
				print("Please enter a numeric value.")
				continue
			val = float(entry)
		except ValueError:
			print("Invalid number, please try again.")
			continue

		values.append(val)

		# Only ask whether to continue once at least 3 values entered
		if len(values) >= 3:
			resp = input("Do you want to enter another value? (y/n): ").strip().lower()
			if resp.startswith('y'):
				continue
			else:
				break
		# otherwise continue collecting until 3 values have been entered

	return values


def main() -> None:
	while True:
		print_menu()
		choice = input("Choose an option: ").strip()

		if choice == '1':
			values = read_values()
			if not values:
				print("No values entered.")
			else:
				try:
					low = get_lowest_list_value(values)
					high = get_highest_list_value(values)
					print(f"Lowest value: {low}")
					print(f"Highest value: {high}")
				except ValueError as e:
					print(f"Error computing min/max: {e}")

		elif choice == '2':
			print("Exiting...")
			break

		else:
			print("Invalid option. Please select 1 or 2.")


if __name__ == '__main__':
	main()
