def decimal_to_binary(decimal_num):
    try:
        decimal_num = int(decimal_num)
        if decimal_num < 0:
            return "Invalid input. Decimal number cannot be negative."
        elif decimal_num == 0:
            return "Binary Number = 0"
        else:
            binary_num = bin(decimal_num)[2:]
            return f"Binary Number = {binary_num}"
    except ValueError:
        return "Invalid input. Please enter a valid decimal number."

def decimal_to_octal(decimal_num):
    try:
        decimal_num = int(decimal_num)
        if decimal_num < 0:
            return "Invalid input. Decimal number cannot be negative."
        elif decimal_num == 0:
            return "Octal = 0"
        else:
            octal_num = oct(decimal_num)[2:]
            return f"Octal = {octal_num}"
    except ValueError:
        return "Invalid input. Please enter a valid decimal number."

def main():
    decimal_num = input("Decimal Number: ")

    # Calculate and print binary number
    binary_result = decimal_to_binary(decimal_num)
    print(binary_result)

    # Calculate and print octal number
    octal_result = decimal_to_octal(decimal_num)
    print(octal_result)

# Run the main function
main()
