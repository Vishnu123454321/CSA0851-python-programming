import math


def calculate_lcm(x, y):
    return abs(x * y) // math.gcd(x, y)


def calculate_gcd(numbers):
    gcd_result = numbers[0]
    for num in numbers[1:]:
        gcd_result = math.gcd(gcd_result, num)
    return gcd_result


def calculate_lcm_of_numbers(numbers):
    lcm_result = numbers[0]
    for num in numbers[1:]:
        lcm_result = calculate_lcm(lcm_result, num)
    return lcm_result


def find_lcm_and_gcd():
    try:
        N = int(input("N value: "))
        if N <= 0:
            print("Invalid input. N should be a positive integer.")
            return

        numbers = []
        for i in range(1, N + 1):
            num = int(input(f"Number {i}: "))
            numbers.append(num)

        if len(numbers) < 2:
            print("At least two numbers are required.")
            return

        lcm = calculate_lcm_of_numbers(numbers)
        gcd = calculate_gcd(numbers)

        print(f"LCM = {lcm}")
        print(f"GCD = {gcd}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")


# Test the function
find_lcm_and_gcd()
