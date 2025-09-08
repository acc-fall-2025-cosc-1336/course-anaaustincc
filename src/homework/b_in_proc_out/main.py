from output import multiply_numbers

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = multiply_numbers(a, b)
    print(f"The product of {a} and {b} is {result}")

if __name__ == "__main__":
    main()