def main():

    from output import multiply_numbers
    a1, b1 = 7, 7
    a2, b2 = 5, 5
    print(f"{a1} x {b1} = {multiply_numbers(a1, b1)}")
    print(f"{a2} x {b2} = {multiply_numbers(a2, b2)}")

if __name__ == "__main__":
    main()