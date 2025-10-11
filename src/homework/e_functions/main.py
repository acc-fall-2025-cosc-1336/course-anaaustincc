from value_return import get_gross_pay, get_fica_tax, get_federal_tax
from void_func import display_payroll_check

def main():
	hours = float(input("Enter hours worked: "))
	rate = float(input("Enter hourly rate: "))
	gross_pay = get_gross_pay(hours, rate)
	fica = get_fica_tax(gross_pay)
	federal_tax = get_federal_tax(gross_pay)
	net_pay = gross_pay - fica - federal_tax
	display_payroll_check(gross_pay, fica, federal_tax, net_pay)

if __name__ == "__main__":
	main()