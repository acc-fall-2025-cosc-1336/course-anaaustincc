
FICA_RATE = 0.0765  # 7.65%
FEDERAL_RATE = 0.08  # 8%


def multiply(a, b):
	result = 0
	for _ in range(int(abs(b))):
		result += a
	if b < 0:
		result = -result
	# Handle float multiplication
	decimal = b - int(b)
	if decimal != 0:
		result += a * decimal
	return result

def subtract(a, b):
	return a + (-b)

def get_gross_pay(hours, rate):
	# Account for overtime (over 40 hours)
	if hours > 40:
		overtime_hours = subtract(hours, 40)
		overtime_pay = multiply(multiply(overtime_hours, rate), 1.5)
		regular_pay = multiply(40, rate)
		return regular_pay + overtime_pay
	else:
		return multiply(hours, rate)


def get_fica_tax(gross_pay):
	return multiply(gross_pay, FICA_RATE)


def get_federal_tax(gross_pay):
	return multiply(gross_pay, FEDERAL_RATE)