import sys
from pathlib import Path

# Ensure repository root is on sys.path so `import src...` works when running
# this script directly.
repo_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(repo_root))

from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement


def print_menu() -> None:
	print("1-Hamming Distance")
	print("2-Dna Complement")
	print("3-Exit")


def main() -> None:
	while True:
		print_menu()
		choice = input("Choose an option: ").strip()

		if choice == '1':
			s1 = input("Enter first string: ").strip()
			s2 = input("Enter second string: ").strip()
			try:
				dist = get_hamming_distance(s1, s2)
				print(f"Hamming distance: {dist}")
			except ValueError as e:
				print(f"Error: {e}")

		elif choice == '2':
			s = input("Enter DNA string: ").strip()
			try:
				comp = get_dna_complement(s)
				print(f"DNA complement: {comp}")
			except ValueError as e:
				print(f"Error: {e}")

		elif choice == '3':
			print("Exiting...")
			break

		else:
			print("Invalid option. Please select 1, 2, or 3.")


if __name__ == '__main__':
	main()
