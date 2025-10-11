import unittest

from src.homework.b_in_proc_out.output import get_sales_tax_amount, get_tip_amount, TAX_RATE

class TestSalesTaxAndTip(unittest.TestCase):

    def test_get_sales_tax_amount(self):
        subtotal = 100
        expected_tax = subtotal * TAX_RATE
        self.assertAlmostEqual(get_sales_tax_amount(subtotal), expected_tax)

    def test_get_tip_amount(self):
        subtotal = 100
        tip_rate = 0.15
        expected_tip = subtotal * tip_rate
        self.assertAlmostEqual(get_tip_amount(subtotal, tip_rate), expected_tip)
