from decisions import numerical_to_letter_grade

def numerical_to_letter_grade_switch(numerical_grade):
	# Simulate switch-case using match-case (Python 3.10+)
	match numerical_grade:
		case grade if grade >= 95:
			print('A')
		case grade if grade >= 85:
			print('B')
		case grade if grade >= 75:
			print('C')
		case grade if grade >= 65:
			print('D')
		case _:
			print('F')

def main():
	print("MAIN MENU\n")
	print("1-Letter grade using if")
	print("2-Letter grade using switch")
	print("3-Exit\n")
	choice = input("Enter your choice: ")

	if choice == '1':
		num = int(input("Enter a number between 0 and 100: "))
		if 0 <= num <= 100:
			letter = numerical_to_letter_grade(num)
			print(f"Letter grade: {letter}")
		else:
			print("Number is out of range.")
	elif choice == '2':
		num = int(input("Enter a number between 0 and 100: "))
		if 0 <= num <= 100:
			letter = numerical_to_letter_grade_switch(num)
			print(f"Letter grade: {letter}")
		else:
			print("Number is out of range.")
	elif choice == '3':
		print("Exiting program.")
	else:
		print("Invalid choice.")

if __name__ == "__main__":
	main()