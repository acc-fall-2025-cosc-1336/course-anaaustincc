TAX_RATE = 0.0675 # 6.75% tax rate

def get_sales_tax_amount(meal_amount):
    """Calculate the sales tax amount for a given meal amount."""
    return meal_amount * TAX_RATE

def get_tip_amount(meal_amount, tip_rate):
    """Calculate the tip amount for a given meal amount and tip rate."""
    return meal_amount * tip_rate