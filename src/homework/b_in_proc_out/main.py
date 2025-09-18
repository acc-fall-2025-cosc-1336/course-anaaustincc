from output import get_sales_tax_amount, get_tip_amount, TAX_RATE

def main():
    # Prompt user for meal amount
    meal_amount = float(input("Enter the meal amount (e.g., 20.00): "))
    # Prompt user for tip rate
    tip_rate = float(input("Enter the tip rate as a decimal (e.g., 0.15 for 15%): "))

    # Calculate sales tax and tip
    sales_tax = get_sales_tax_amount(meal_amount)
    tip_amount = get_tip_amount(meal_amount, tip_rate)
    total = meal_amount + sales_tax + tip_amount

    # Display receipt
    print(f"Receipt")
    print(f"Meal Amount:   {meal_amount:.2f}")
    print(f"Sales Tax:     {sales_tax:.2f}")
    print(f"Tip Amount:    {tip_amount:.2f}")
    print(f"Total:         {total:.2f}")

if __name__ == "__main__":
    main()