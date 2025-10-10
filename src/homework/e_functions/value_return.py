
FICA_RATE = 0.0765  # 7.65%
FEDERAL_RATE = 0.08  # 8%

def get_gross_pay(hours, rate):
	# Account for overtime (over 40 hours)
	if hours > 40:
		overtime_hours = hours - 40
		overtime_pay = overtime_hours * rate * 1.5
		regular_pay = 40 * rate
		return regular_pay + overtime_pay
	else:
		return hours * rate

def get_fica_tax(gross_pay):
	return gross_pay * FICA_RATE

def get_federal_tax(gross_pay):
	return gross_pay * FEDERAL_RATE