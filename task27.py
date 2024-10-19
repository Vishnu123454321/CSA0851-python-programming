def calculate_tax(income):
    if income <= 150000:
        tax = 0
    elif income <= 300000:
        tax = (income - 150000) * 0.1
    elif income <= 500000:
        tax = 15000 + (income - 300000) * 0.2
    else:
        tax = 45000 + (income - 500000) * 0.3

    return tax


def main():
    try:
        income = float(input("Enter the income: "))
        if income < 0:
            raise ValueError("Income cannot be negative.")

        tax = calculate_tax(income)
        print(f"Tax = {tax}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")


# Run the main function
main()
