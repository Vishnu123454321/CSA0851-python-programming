from math import gcd
from functools import reduce


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_of_list(numbers):
    return reduce(lcm, numbers)


def gcd_of_list(numbers):
    return reduce(gcd, numbers)


def main():
    try:
        n = int(input("Enter the number of values (N): "))
        if n <= 0:
            print("Invalid input: N should be greater than 0")
            return

        numbers = []
        for i in range(n):
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)

        lcm_result = lcm_of_list(numbers)
        gcd_result = gcd_of_list(numbers)

        print(f"LCM = {lcm_result}")
        print(f"GCD = {gcd_result}")

    except ValueError:
        print("Invalid input: Please enter valid integers")


if __name__ == "__main__":
    main()
