def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes_and_composites(numbers):
    prime_count = 0
    composite_count = 0

    for number in numbers:
        try:
            num = int(number)
            if num > 1:
                if is_prime(num):
                    prime_count += 1
                else:
                    composite_count += 1
        except ValueError:
            continue

    return prime_count, composite_count


def main():
    input_numbers = input("Enter the numbers (separated by commas): ").split(',')
    input_numbers = [num.strip() for num in input_numbers]

    prime_count, composite_count = count_primes_and_composites(input_numbers)

    print(f"Composite numbers: {composite_count}")
    print(f"Prime numbers: {prime_count}")


if __name__ == "__main__":
    main()
