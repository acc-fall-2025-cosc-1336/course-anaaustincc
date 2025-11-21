
def numerical_to_letter_grade(numerical_grade):
	"""
	Converts a numerical grade to a letter grade.
	Args:
		numerical_grade (int or float): The numerical grade to convert.
	Returns:
		str: The letter grade (A, B, C, D, F)
	"""
	if numerical_grade >= 95:
		return 'A'
	elif numerical_grade >= 85:
		return 'B'
	elif numerical_grade >= 75:
		return 'C'
	elif numerical_grade >= 65:
		return 'D'
	else:
		return 'F'