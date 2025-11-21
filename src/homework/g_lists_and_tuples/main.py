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

from src.homework.g_lists_and_tuples.lists import get_p_distance_matrix


def print_menu() -> None:
	print("1-Get p distance matrix")
	print("2-Exit")


def read_sequences() -> list:
	"""Read a collection of equal-length DNA sequences from the user.

	Prompts for how many sequences to enter, then reads each sequence on its
	own line. Sequences are returned as a list of lists of single-character
	strings (e.g. ['A','C','G']). Input validation enforces at least 1
	sequence and that all sequences have the same length.
	"""
	while True:
		cnt_raw = input("How many sequences will you enter? ").strip()
		try:
			count = int(cnt_raw)
			if count <= 0:
				print("Please enter a positive integer.")
				continue
		except ValueError:
			print("Invalid number, please enter an integer.")
			continue
		break

	sequences = []
	expected_len = None
	i = 0
	while i < count:
		s = input(f"Enter sequence #{i+1}: ").strip()
		if s == "":
			print("Empty sequence not allowed; please re-enter.")
			continue
		# normalize to upper-case and convert to list of chars
		seq = [ch for ch in s.strip()]
		if expected_len is None:
			expected_len = len(seq)
			if expected_len == 0:
				print("Sequence must contain at least one character.")
				continue
		else:
			if len(seq) != expected_len:
				print(f"Sequence length must be {expected_len}; you entered length {len(seq)}. Please re-enter.")
				continue

		sequences.append(seq)
		i += 1

	return sequences


def main() -> None:
	while True:
		print_menu()
		choice = input("Choose an option: ").strip()

		if choice == '1':
			seqs = read_sequences()
			if not seqs:
				print("No sequences entered.")
			else:
				try:
					D = get_p_distance_matrix(seqs)
					# print matrix with 5 decimal places
					r = 0
					while r < len(D):
						row = D[r]
						c = 0
						out_parts = []
						while c < len(row):
							out_parts.append("{:.5f}".format(row[c]))
							c += 1
						print(" ".join(out_parts))
						r += 1
				except ValueError as e:
					print(f"Error computing p-distance matrix: {e}")

		elif choice == '2':
			print("Exiting...")
			break

		else:
			print("Invalid option. Please select 1 or 2.")


if __name__ == '__main__':
	main()
