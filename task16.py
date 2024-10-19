def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def count_prime_and_composite(numbers):
    prime_count = 0
    composite_count = 0
    for num in numbers:
        try:
            num = int(num)
            if num < 2:
                continue  # Skip numbers less than 2
            if is_prime(num):
                prime_count += 1
            else:
                composite_count += 1
        except ValueError:
            continue  # Skip non-integer inputs

    return prime_count, composite_count


def main():
    try:
        input_numbers = input("Enter the numbers separated by spaces: ").split(",")

        prime_count, composite_count = count_prime_and_composite(input_numbers)

        print(f"Prime number:{prime_count} Composite number:{composite_count}")

    except Exception as e:
        print(f"Error: {e}")


# Run the main function
main()

