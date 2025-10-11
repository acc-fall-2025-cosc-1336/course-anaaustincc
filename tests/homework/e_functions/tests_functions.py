import unittest
from src.homework.e_functions.value_return import get_gross_pay, get_fica_tax, get_federal_tax

class TestPayrollFunctions(unittest.TestCase):
	def test_gross_pay(self):
		# No overtime
		self.assertAlmostEqual(get_gross_pay(40, 10), 400.0)
		# With overtime
		self.assertAlmostEqual(get_gross_pay(45, 10), 475.0)  # 400 + 5*10*1.5 = 475
		# Different rate
		self.assertAlmostEqual(get_gross_pay(30, 10), 300.0)

	def test_fica_tax(self):
		self.assertAlmostEqual(get_fica_tax(400.0), 30.6)   # 400 * 0.0765
		self.assertAlmostEqual(get_fica_tax(475.0), 36.3375)
		self.assertAlmostEqual(get_fica_tax(300.0), 22.95)

	def test_federal_tax(self):
		self.assertAlmostEqual(get_federal_tax(400.0), 32.0)   # 400 * 0.08
		self.assertAlmostEqual(get_federal_tax(475.0), 38.0)
		self.assertAlmostEqual(get_federal_tax(300.0), 24.0)

if __name__ == "__main__":
	unittest.main()