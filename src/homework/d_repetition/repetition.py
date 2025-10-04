def get_factorial(n):
	"""
	Returns the factorial of n using a for loop.
	"""
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result

def sum_odd_numbers(n):
	"""
	Returns the sum of all odd numbers up to n using a while loop.
	"""
	total = 0
	i = 1
	while i <= n:
		if i % 2 == 1:
			total += i
		i += 1
	return total