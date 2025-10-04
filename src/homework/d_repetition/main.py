from repetition import get_factorial, sum_odd_numbers

def main():
	while True:
		print("\nHomework 4 Menu")
		print("1-Factorial")
		print("2-Sum odd numbers")
		print("3-Exit")
		choice = input("Enter your choice: ")

		if choice == '1':
			while True:
				num_str = input("Enter a number (1-9): ")
				try:
					num = float(num_str) if '.' in num_str else int(num_str)
					if 1 <= num <= 9:
						# Factorial only makes sense for integers
						if isinstance(num, float) and not num.is_integer():
							print("Please enter a whole number for factorial.")
							continue
						num = int(num)
						result = get_factorial(num)
						print(f"Factorial of {num} is {result}")
						break
					else:
						print("Number must be between 1 and 9.")
				except ValueError:
					print("Invalid input. Please enter a number.")

		elif choice == '2':
			while True:
				num_str = input("Enter a number (1-99): ")
				try:
					num = float(num_str) if '.' in num_str else int(num_str)
					if 1 <= num <= 99:
						# Sum odd numbers only makes sense for integers
						if isinstance(num, float) and not num.is_integer():
							print("Please enter a whole number for sum of odd numbers.")
							continue
						num = int(num)
						result = sum_odd_numbers(num)
						print(f"Sum of odd numbers up to {num} is {result}")
						break
					else:
						print("Number must be between 1 and 99.")
				except ValueError:
					print("Invalid input. Please enter a number.")

		elif choice == '3':
			print("Exiting program.")
			break
		else:
			print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
	main()